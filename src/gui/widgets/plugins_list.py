from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QListWidgetItem, QMainWindow

from src.core.plugins.loader import (get_registerd_plugins,
                                     list_plugins_from_storage,
                                     register_plugin, unregister_plugin)
from src.core.utils.logger import get_logger
from src.gui.ui.plugin_list_dialog_ui import Ui_Dialog

# Codes Here

logger = get_logger()


class PluginsListView(QDialog):
    def __init__(self, main_window: QMainWindow):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Get plugin names (assuming list_plugins_from_storage() returns a list of strings)
        self.plugin_names = list_plugins_from_storage()['plugins']
        self.get_registerd_plugins = get_registerd_plugins

        for plugin_name in self.plugin_names:
            item = QListWidgetItem(plugin_name)

            # Make the item checkable
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            if plugin_name in self.get_registerd_plugins():
                item.setCheckState(Qt.Checked)  # Default unchecked
            else:
                item.setCheckState(Qt.Unchecked)  # Default unchecked
                

            self.ui.listWidget.addItem(item)

        # Connect signal to handle checkbox changes
        self.ui.listWidget.itemChanged.connect(self.on_item_changed)

    def on_item_changed(self, item):
        """Called when a checkbox state changes"""
        plugin_name = item.text()
        plugin = self.plugin_names[plugin_name]
        path = Path(plugin['path'])
        if item.checkState() == Qt.Checked:
            register_plugin(path, self.main_window)
        else:
            unregister_plugin(path, self.main_window, False)
