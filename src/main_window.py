from PySide6.QtCore import QEvent, Qt, Slot
from PySide6.QtWidgets import QMainWindow, QPushButton

import controllers
from ui.main_window_ui import Ui_MainWindow
from utils.logger import get_logger
from utils.mixins import RetranslateMixin
from widgets.base_screen import BaseScreen
from widgets.menubar import Menubar

# Codes Here


logger = get_logger()


class MainWindow(RetranslateMixin, QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.MainSideNav.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.menubar_controler = Menubar(self)
        self.menubar_controler.setup_ui()

        self._nav_screens: list[tuple[QPushButton, BaseScreen]] = []

        self.load_screens()

        # Set initial screen to first one (index 0)
        if self.ui.MainStackView.count() > 0:
            self.go_to_screen(0)

    def changeEvent(self, event: QEvent, /) -> None:
        """Refresh nav button labels whenever the app language changes."""
        super().changeEvent(event)

        if event.type() == QEvent.Type.LanguageChange:
            for btn, screen in self._nav_screens:
                btn.setText(screen.NAME)

    def add_to_screen(self, btn: QPushButton, screen: BaseScreen):
        """Add buttons to the side navigation and corresponding screen."""
        index = self.ui.MainStackView.addWidget(screen)
        btn.setProperty("index", index)
        self.ui.MainSideNav.addWidget(btn)
        self._nav_screens.append((btn, screen))

        # Use functools.partial for more reliable connections
        btn.clicked.connect(lambda checked, idx=index: self.go_to_screen(idx))

    def remove_plugin_btn_screen(self, obj_name: str):
        """Safely removes buttons and screens, updating all indices."""
        btn = self.ui.MainSideNavFrame.findChild(QPushButton, obj_name)
        if not btn:
            logger.error(f"Button {obj_name} not found")
            return

        removed_index = btn.property("index")
        if removed_index is None:
            logger.error(f"Button {obj_name} has no index property")
            return

        # Remove from navigation
        layout = self.ui.MainSideNav
        layout.takeAt(layout.indexOf(btn)).widget().deleteLater()  # type: ignore
        self._nav_screens = [(b, s) for b, s in self._nav_screens if b is not btn]

        # Remove from stack if exists
        if 0 <= removed_index < self.ui.MainStackView.count():
            widget = self.ui.MainStackView.widget(removed_index)
            if widget:
                self.ui.MainStackView.removeWidget(widget)
                widget.deleteLater()

        # Update all remaining button indices
        self.update_all_button_indices(removed_index)

        self.verify_stack_consistency()  # Optional debug check

    def update_all_button_indices(self, removed_index: int):
        """Updates indices for all buttons after a removal."""
        layout = self.ui.MainSideNav

        # First collect all buttons and their current indices
        buttons = []
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item and item.widget():
                btn = item.widget()
                current_index = btn.property("index")  # type: ignore
                if current_index is not None:
                    buttons.append((btn, current_index))

        # Then update indices and reconnect signals
        for btn, current_index in buttons:
            if current_index > removed_index:
                new_index = current_index - 1
                btn.setProperty("index", new_index)

                # Disconnect all existing connections
                try:
                    btn.clicked.disconnect()
                except RuntimeError:  # No connections exist
                    pass

                # Reconnect with correct index using partial
                btn.clicked.connect(
                    lambda checked, idx=new_index: self.go_to_screen(idx)
                )

    @Slot(int, name="Go to screen")  # type: ignore
    def go_to_screen(self, screen: int):
        """Switch to a specific screen in the stack view."""
        if 0 <= screen < self.ui.MainStackView.count():
            self.ui.MainStackView.setCurrentIndex(screen)

            # Update button styles
            for i in range(self.ui.MainSideNav.count()):
                item = self.ui.MainSideNav.itemAt(i)
                if item and item.widget():
                    btn = item.widget()
                    if isinstance(btn, QPushButton):
                        btn_index = btn.property("index")
                        if btn_index == screen:
                            # Add "active" class to current button
                            current_classes = btn.property("class") or ""
                            btn.setProperty("class", f"{current_classes} active".strip())
                            btn.style().unpolish(btn)
                            btn.style().polish(btn)
                        else:
                            # Remove "active" class from other buttons
                            current_classes = btn.property("class") or ""
                            new_classes = " ".join(c for c in current_classes.split() if c != "active")
                            btn.setProperty("class", new_classes if new_classes else "")
                            btn.style().unpolish(btn)
                            btn.style().polish(btn)
        else:
            logger.error(f"Invalid screen index: {screen}")

    def verify_stack_consistency(self):
        """Debug method to verify button indices match stack widgets."""
        for i in range(self.ui.MainSideNav.count()):
            item = self.ui.MainSideNav.itemAt(i)
            if item and item.widget():
                btn = item.widget()
                btn_index = btn.property("index")  # type: ignore
                if btn_index is None:
                    continue

                if btn_index >= self.ui.MainStackView.count():
                    logger.error(f"Warning: Button {btn.objectName()} points to invalid index {btn_index}")  # type: ignore

    def load_screens(self):
        """Load all screens into the application."""
        for screen_class in controllers.__all__:
            # Get the actual class from the controllers module
            screen = getattr(controllers, screen_class)()
            logger.info(f"Loading screen: {screen.NAME}")
            try:
                screen.setup_ui()
                btn = QPushButton(screen.NAME)
            except Exception as e:
                logger.error(f"Failed to setup screen {screen.NAME}: {e}")
                exit(1)
                
            try:
                self.add_to_screen(btn, screen)
            except Exception as e:
                logger.error(f"Failed to add screen {screen.NAME}: {e}")
