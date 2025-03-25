from pathlib import Path

from PySide6.QtCore import QUrl, Slot
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QFileDialog, QMainWindow

from src.core.plugins.loader import register_plugin
from src.core.utils.logger import get_logger
from src.gui.ui.main_window_ui import Ui_MainWindow
from src.gui.widgets.plugins_list import PluginsListView

logger = get_logger()


class Menubar:
    """A custom menubar class that sets up the UI and handles menu actions."""

    def __init__(self, main_window: QMainWindow = None):
        self.ui: Ui_MainWindow = main_window.ui
        self.parent = main_window

        self.actionContact = self.ui.actionContact
        self.actionInfo = self.ui.actionInfo
        self.actionHelp = self.ui.actionHelp

        self.actionRegister = self.ui.actionRegister
        self.actionList = self.ui.actionList
        self.actionImport = self.ui.actionImport
        self.actionExport = self.ui.actionExport

        self.actionPrefrences = self.ui.actionPrefrences

    def setup_ui(self):
        """Initialize and configure the actions for the menubar."""
        # Connect the actions to their handlers
        self.actionRegister.triggered.connect(self.register_plugin)
        self.actionContact.triggered.connect(self.open_contact)
        self.actionList.triggered.connect(self.open_plugins_list)
        self.actionImport.triggered.connect(self.import_data)
        self.actionExport.triggered.connect(self.export_data)

    @Slot()
    def register_plugin(self):
        """Handle the 'Register' action by opening a file dialog to select a folder."""
        folder_path = Path(QFileDialog.getExistingDirectory()).absolute()

        if folder_path:
            main_window = self.parent
            register_plugin(path=folder_path, main_window=main_window)

    @Slot()
    def open_contact(self):
        """Open the contact URL in the web browser."""
        url = QUrl("https://github.com/bambier/Accounting-Software/discussions")
        if not QDesktopServices.openUrl(url):
            logger.error(f"Failed to open URL: {url}")

    @Slot()
    def open_plugins_list(self):
        """Show the plugins list in a new window."""
        self.plugins_list = PluginsListView(main_window=self.parent)
        self.plugins_list.show()

    @Slot()
    def import_data(self):
        """Handle the import action."""
        # Add your import functionality here
        pass

    @Slot()
    def export_data(self):
        """Handle the export action."""
        # Add your export functionality here
        pass
