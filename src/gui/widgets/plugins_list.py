from PySide6.QtWidgets import QDialog

from src.gui.ui.plugin_list_dialog_ui import Ui_Dialog


class PluginsListView(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        print("UI")
