from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import QMainWindow, QPushButton

from src.core.utils.logger import get_logger
from src.gui.ui.main_window_ui import Ui_MainWindow
from src.gui.widgets.base_screen import BaseScreen
from src.gui.widgets.menubar import Menubar

# Codes Here


logger = get_logger()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.MainSideNav.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.menubar_controler = Menubar(self)
        self.menubar_controler.setup_ui()

        self.clear_stacked_layout()

    def add_to_screen(self, btn: QPushButton, screen: BaseScreen):
        """Add buttons to the side navigation and corresponding screen."""
        index = self.ui.MainStackView.addWidget(screen)
        btn.setProperty("index", index)
        self.ui.MainSideNav.addWidget(btn)

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
        layout.takeAt(layout.indexOf(btn)).widget().deleteLater()

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
                current_index = btn.property("index")
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

    @Slot(int, name="Go to screen")
    def go_to_screen(self, screen: int):
        """Switch to a specific screen in the stack view."""
        if 0 <= screen < self.ui.MainStackView.count():
            self.ui.MainStackView.setCurrentIndex(screen)
        else:
            logger.error(f"Invalid screen index: {screen}")

    def clear_stacked_layout(self):
        """Clear all widgets from the stacked layout."""
        while self.ui.MainStackView.count():
            widget = self.ui.MainStackView.widget(0)
            if widget:
                self.ui.MainStackView.removeWidget(widget)
                widget.deleteLater()

    def verify_stack_consistency(self):
        """Debug method to verify button indices match stack widgets."""
        for i in range(self.ui.MainSideNav.count()):
            item = self.ui.MainSideNav.itemAt(i)
            if item and item.widget():
                btn = item.widget()
                btn_index = btn.property("index")
                if btn_index is None:
                    continue

                if btn_index >= self.ui.MainStackView.count():
                    logger.error(f"Warning: Button {btn.objectName()} points to invalid index {btn_index}")
