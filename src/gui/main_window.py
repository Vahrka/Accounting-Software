from PySide6.QtCore import Qt, QSettings
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QMainWindow,
                               QStackedWidget, QVBoxLayout, QWidget)

from src.controlers.main_controler import MainControler
from src.gui.widgets.menubar import Menubar

# Codes Here


class MainWindow(QMainWindow, MainControler):
    def __init__(self):
        super().__init__()
        
        self.setting = QSettings()

        # Create main container
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Setup top Munubar
        menubar = Menubar()
        menubar.setup_ui()
        self.setMenuBar(menubar)

        # Modern layout
        self.main_window = QHBoxLayout()

        main_widget.setLayout(self.main_window)

        # Setup main side navigation
        self.main_side_nav_frame = QFrame()
        self.main_side_nav_frame.setFixedWidth(240)
        self.main_side_nav_frame.setObjectName("MainSideNav")
        self.main_side_nav_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.main_side_nav_frame.setFrameShadow(QFrame.Shadow(QFrame.Shadow.Raised))
        self.side_nav = QVBoxLayout(self.main_side_nav_frame)
        self.side_nav.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.main_window.addWidget(self.main_side_nav_frame)

        # Setup main content Area
        self.stacked_widget = QStackedWidget()  # Manages screens
        self.main_window.addWidget(self.stacked_widget)
