from PySide6.QtWidgets import QPushButton

from src.core.plugins.plugin_base import PluginBase


class Account(PluginBase):

    def register(self):
        self.button = QPushButton(self.tr("Push me"))
        self.main_window.add_btn_to_nav(self.button)
