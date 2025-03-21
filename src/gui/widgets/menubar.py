from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QAction, QDesktopServices, QIcon
from PySide6.QtWidgets import QFileDialog, QMenu, QMenuBar

from src.core.plugins.loader import register_plugin


class Menubar(QMenuBar):
    """A custom menubar class that sets up the UI and handles menu actions."""

    def setup_ui(self):
        """Initialize and configure the UI elements for the menubar."""

        # Create actions for the menu items
        self.actionRegister = QAction()
        self.actionRegister.setObjectName("actionRegister")
        self.actionRegister.setIcon(QIcon(":/icons/register.svg"))
        self.actionRegister.setShortcut(Qt.KeyboardModifier.ControlModifier |
                                        Qt.KeyboardModifier.AltModifier | Qt.Key.Key_R)

        self.actionList = QAction()
        self.actionList.setObjectName("actionList")
        self.actionList.setIcon(QIcon(":/icons/list.svg"))
        self.actionList.setShortcut(Qt.KeyboardModifier.ControlModifier |
                                        Qt.KeyboardModifier.ShiftModifier | Qt.Key.Key_X)
        
        self.actionExport = QAction()
        self.actionExport.setObjectName("actionExport")
        self.actionExport.setIcon(QIcon(":/icons/export.svg"))

        self.actionImport = QAction()
        self.actionImport.setObjectName("actionImport")
        self.actionImport.setIcon(QIcon(":/icons/import.svg"))

        self.actionPreferences = QAction()
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionPreferences.setIcon(QIcon(":/icons/preferences.svg"))

        self.actionContact = QAction()
        self.actionContact.setObjectName("actionContact")
        self.actionContact.setIcon(QIcon(":/icons/contact-phonebook-support.svg"))
        self.actionContact.setShortcut(Qt.Key.Key_F1 | Qt.KeyboardModifier.ControlModifier)
        

        self.actionHelp = QAction()
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelp.setIcon(QIcon(":/icons/help.svg"))
        self.actionHelp.setShortcut(Qt.Key.Key_F1)

        self.actionInfo = QAction()
        self.actionInfo.setObjectName("actionInfo")
        self.actionInfo.setIcon(QIcon(":/icons/info-square.svg"))
        self.actionInfo.setShortcut(Qt.Key.Key_F1 | Qt.KeyboardModifier.AltModifier)

        # Create menus and submenus
        self.menuFile = QMenu()  # Main "File" menu
        self.menuFile.setObjectName("menuFile")

        self.menuPlugin = QMenu(self.menuFile)  # Submenu for "Plugins" under "File"
        self.menuPlugin.setObjectName("menuPlugin")
        self.menuPlugin.setIcon(QIcon(":/icons/plugin-2.svg"))

        self.menuData = QMenu(self.menuFile)  # Submenu for "Data" under "File"
        self.menuData.setObjectName("menuData")
        self.menuData.setIcon(QIcon(":/icons/data.svg"))

        self.menuSettings = QMenu()  # Main "Settings" menu
        self.menuSettings.setObjectName("menuSettings")

        self.menuHelp = QMenu()  # Main "Help" menu
        self.menuHelp.setObjectName("menuHelp")

        # Add menus to the menubar
        self.addAction(self.menuFile.menuAction())
        self.addAction(self.menuSettings.menuAction())
        self.addAction(self.menuHelp.menuAction())

        # Add submenus and actions to the "File" menu
        self.menuFile.addAction(self.menuPlugin.menuAction())
        self.menuFile.addAction(self.menuData.menuAction())

        # Add actions to the "Plugins" submenu
        self.menuPlugin.addAction(self.actionRegister)
        self.menuPlugin.addAction(self.actionList)

        # Add actions to the "Data" submenu
        self.menuData.addAction(self.actionExport)
        self.menuData.addAction(self.actionImport)

        # Add actions to the "Settings" menu
        self.menuSettings.addAction(self.actionPreferences)

        # Add actions to the "Help" menu
        self.menuHelp.addAction(self.actionContact)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionInfo)

        # Translate UI elements (set text for actions and menus)
        self.retranslateUi()

        # Connect the "Register" action to its handler
        self.actionRegister.triggered.connect(self.register_plugin)
        self.actionContact.triggered.connect(self.open_contact)

    def retranslateUi(self):
        """Set the display text for all UI elements (actions and menus)."""
        self.actionRegister.setText(self.tr("Register"))
        self.actionList.setText(self.tr("List"))
        self.actionExport.setText(self.tr("Export"))
        self.actionImport.setText(self.tr("Import"))
        self.actionPreferences.setText(self.tr("Preferences"))  # Fixed typo in "Preferences"
        self.actionContact.setText(self.tr("Contact Us"))  # Fixed typo in "Contact Us"
        self.actionHelp.setText(self.tr("Help"))
        self.actionInfo.setText(self.tr("Info"))
        self.menuFile.setTitle(self.tr("File"))
        self.menuPlugin.setTitle(self.tr("Plugins"))
        self.menuData.setTitle(self.tr("Data"))
        self.menuSettings.setTitle(self.tr("Settings"))
        self.menuHelp.setTitle(self.tr("Help"))

    def register_plugin(self):
        """Handle the 'Register' action by opening a file dialog to select a folder."""
        # Open a directory selection dialog
        folder_path = QFileDialog.getExistingDirectory(
            self,  # Parent widget
            self.tr("Select Folder"),  # Dialog title
            ".",  # Start directory (user's home directory)
            # os.path.expanduser("~"),  # Start directory (user's home directory)
            QFileDialog.ShowDirsOnly  # Only show directories
        )

        # Check if a folder was selected
        if folder_path:
            main_window = self.parent()
            register_plugin(path=Path(folder_path), main_window=main_window)

    def open_contact(self):
        # Define the URL
        url = QUrl("https://github.com/bambier/Accounting-Software/discussions")

        # Open the URL in the default web browser
        if not QDesktopServices.openUrl(url):
            print("Failed to open URL")
