from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QCheckBox, QDialog, QHBoxLayout, QListWidget,
                               QListWidgetItem, QMainWindow, QMessageBox,
                               QPushButton, QWidget)

from src.core.plugins.loader import (get_registerd_plugins,
                                     list_plugins_from_storage,
                                     register_plugin, unregister_plugin)
from src.core.utils.logger import get_logger
from src.gui.ui.plugin_list_dialog_ui import Ui_Dialog

logger = get_logger()


class PluginsListView(QDialog):
    def __init__(self, main_window: QMainWindow):
        super().__init__(main_window)
        self.main_window = main_window
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Set object names for styling
        self.setObjectName("pluginManager")
        self.ui.listWidget.setObjectName("pluginList")

        # Apply initial layout config
        self._setup_layout()
        self.load_plugins()

    def _setup_layout(self):
        """Configure layout properties"""
        self.ui.listWidget.setSpacing(4)
        self.ui.listWidget.setVerticalScrollMode(QListWidget.ScrollPerPixel)
        self.ui.listWidget.setHorizontalScrollMode(QListWidget.ScrollPerPixel)

    def load_plugins(self):
        """Load plugins into the list widget"""
        self.ui.listWidget.clear()
        plugin_data = list_plugins_from_storage()
        self.plugin_names = plugin_data.get('plugins', {})
        registered_plugins = get_registerd_plugins()

        for plugin_name, plugin_info in self.plugin_names.items():
            self._create_plugin_item(plugin_name, plugin_info, plugin_name in registered_plugins)

    def _create_plugin_item(self, plugin_name, plugin_info, is_enabled):
        """Create a plugin item widget with classic checkbox"""
        widget = QWidget()
        widget.setObjectName("pluginItem")
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(16)

        # Classic checkbox - no custom styling
        checkbox = QCheckBox(plugin_name)
        checkbox.setObjectName("pluginCheckbox")
        checkbox.setChecked(is_enabled)
        checkbox.setProperty("state", "enabled" if is_enabled else "disabled")

        # Delete button (styled in QSS)
        delete_btn = QPushButton(self.tr("Remove"))
        delete_btn.setObjectName("pluginDeleteBtn")
        delete_btn.setProperty("state", "enabled" if is_enabled else "disabled")
        delete_btn.setCursor(Qt.PointingHandCursor)
        delete_btn.setFixedSize(90, 30)

        layout.addWidget(checkbox, 1)
        layout.addWidget(delete_btn)

        item = QListWidgetItem()
        item.setData(Qt.UserRole, plugin_info['path'])
        item.setSizeHint(widget.sizeHint())

        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setItemWidget(item, widget)

        checkbox.toggled.connect(lambda checked, pn=plugin_name: self._on_plugin_toggled(pn, checked))
        delete_btn.clicked.connect(lambda _, pn=plugin_name: self._on_delete_clicked(pn))

    def _on_plugin_toggled(self, plugin_name, enabled):
        """Handle plugin toggle"""
        plugin = self.plugin_names[plugin_name]
        path = Path(plugin['path'])

        if enabled:
            register_plugin(path, self.main_window.add_to_screen)
        else:
            unregister_plugin(path, self.main_window.remove_plugin_btn_screen, remove=False)

        self._update_item_state(plugin_name, enabled)

    def _on_delete_clicked(self, plugin_name):
        """Handle delete button click"""
        reply = QMessageBox(
            QMessageBox.Warning,
            self.tr("Remove Plugin"),
            self.tr(f"Are you sure you want to remove '{plugin_name}'?"),
            QMessageBox.Yes | QMessageBox.No,
            self
        )
        reply.setObjectName("pluginMessageBox")

        if reply.exec() == QMessageBox.Yes:
            self._delete_plugin(plugin_name)

    def _delete_plugin(self, plugin_name):
        """Delete plugin completely"""
        plugin = self.plugin_names[plugin_name]
        path = Path(plugin['path'])
        unregister_plugin(path, self.main_window.remove_plugin_btn_screen, remove=True)
        self.load_plugins()

    def _update_item_state(self, plugin_name, enabled):
        """Update item visual state"""
        for i in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(i)
            widget = self.ui.listWidget.itemWidget(item)

            if widget and widget.findChild(QCheckBox).text() == plugin_name:
                state = "enabled" if enabled else "disabled"
                widget.findChild(QCheckBox).setProperty("state", state)
                widget.findChild(QPushButton).setProperty("state", state)

                # Force style update
                widget.style().unpolish(widget)
                widget.style().polish(widget)
                break
