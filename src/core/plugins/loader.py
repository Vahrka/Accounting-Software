import importlib
from pathlib import Path
from typing import Any, Dict, Optional, Set

import yaml
from PySide6.QtCore import QSettings
from PySide6.QtWidgets import QMainWindow

from src.core.plugins.plugin_base import PluginBase
from src.core.utils.DataStructure import (PluginConfigStruct,
                                          PluginsConfigFileStruct)
from src.core.utils.logger import get_logger
from src.core.utils.settings import BASE_DIR

logger = get_logger()


def validate_plugins_config(plugins_config: Dict[str, Any]) -> PluginsConfigFileStruct:
    """
    Validate the structure of the plugins configuration.
    If the configuration is invalid, return a default configuration with an empty plugins dictionary.
    """
    if not isinstance(plugins_config, dict) or not isinstance(plugins_config.get("plugins", {}), dict):
        return {"plugins": {}}
    return plugins_config


def write_plugin_config(path: Path, name: str) -> None:
    """
    Write the plugin configuration to the plugins.yml file.
    If the plugins.yml file does not exist, it will be created.
    """
    plugins_folder_path = BASE_DIR / "plugins"
    plugins_folder_path.mkdir(parents=True, exist_ok=True)
    plugins_list_file_path = plugins_folder_path / "plugins.yml"

    # Read the existing configuration
    with plugins_list_file_path.open("r", encoding="utf-8") as plugins_file:
        raw_configs = plugins_file.read()
        plugins_config: PluginsConfigFileStruct = yaml.safe_load(raw_configs) or {"plugins": {}}
        plugins_config = validate_plugins_config(plugins_config)

        # Update the configuration with the new plugin
        plugins_config["plugins"][name] = {
            "path": str(path),
            "installed": True
        }

    # Write the updated configuration back to the file
    with plugins_list_file_path.open("w", encoding="utf-8") as f:
        yaml.dump(plugins_config, f)


def remove_plugin_config(path: Path, name: str, remove: bool = False) -> None:
    plugins_folder_path = BASE_DIR / "plugins"
    plugins_folder_path.mkdir(parents=True, exist_ok=True)
    plugins_list_file_path = plugins_folder_path / "plugins.yml"

    # Read the existing configuration
    with plugins_list_file_path.open("r", encoding="utf-8") as plugins_file:
        raw_configs = plugins_file.read()
        plugins_config: PluginsConfigFileStruct = yaml.safe_load(raw_configs) or {"plugins": {}}
        plugins_config = validate_plugins_config(plugins_config)

        # Update the configuration with the new plugin
        if remove:
            plugins_config["plugins"].pop(name)
        else:
            plugins_config["plugins"][name] = {
                "path": str(path),
                "installed": False
            }

    # Write the updated configuration back to the file
    with plugins_list_file_path.open("w", encoding="utf-8") as f:
        yaml.dump(plugins_config, f)


def load_plugin_config(path: Path) -> Optional[PluginConfigStruct]:
    """
    Load the plugin configuration from the config.yml file.
    Returns None if the file is not found or the configuration is invalid.
    """
    try:
        with open(path / "config.yml", "r") as file:
            return yaml.safe_load(file)
    except (FileNotFoundError, yaml.YAMLError) as e:
        logger.error(f"Failed to load plugin config: {e}")
        return None


def get_plugin_class(module_name: str, class_name: str) -> Optional[type]:
    """
    Dynamically import the plugin module and retrieve the plugin class.
    Returns None if the module or class is not found.
    """
    try:
        plugin_module = importlib.import_module(module_name, "plugins")
        if hasattr(plugin_module, class_name):
            return getattr(plugin_module, class_name)
        else:
            logger.error(f"Module '{module_name}' has no attribute '{class_name}'")
            return None
    except ImportError as e:
        logger.critical(f"Cannot import '{module_name}': {e}")
        return None


def get_registerd_plugins() -> Set[str]:
    setting = QSettings()
    registerd_plugins:  Set[str] = setting.value("installed_plugins", set())
    return registerd_plugins


def register_plugin(path: Path, main_window: QMainWindow) -> bool:
    """
    Register a plugin by loading its configuration, dynamically importing the plugin class,
    and initializing it. If the plugin is already registered, it will not be registered again.
    """
    # Load the plugin configuration
    data = load_plugin_config(path)
    if not data or not isinstance(data.get("extention"), dict):
        logger.critical("Extension config file doesn't have the correct structure")
        return False

    extention = data["extention"]
    name = extention.get("name", "").lower()
    entry_point = extention.get("entrypoint", "")

    if not name or not entry_point:
        logger.critical(
            "Extension config file doesn't have the correct structure at ['extention']['name'] or ['extention']['entrypoint']")
        return False

    # Check if the plugin is already registered
    register_plugin = get_registerd_plugins()

    if name in register_plugin:
        logger.info(f"Plugin '{name}' is already registered.")
        return True
    else:
        setting = QSettings()
        register_plugin.add(name)
        setting.setValue("installed_plugins", register_plugin)

    # Construct the module and class names
    module_name = f"plugins.{name}.{entry_point.split('.')[0]}"
    class_name = entry_point.split(".")[-1]

    # Dynamically import the plugin class
    plugin_class = get_plugin_class(module_name, class_name)
    if not plugin_class or not issubclass(plugin_class, PluginBase):
        logger.error(f"Class '{plugin_class}' is not a subclass of '{PluginBase}'")
        return False

    # Initialize and register the plugin
    plugin: PluginBase = plugin_class(main_window)
    plugin.register()
    write_plugin_config(path, name)
    logger.info(f"'{plugin}' registered successfully.")
    return True


def unregister_plugin(path: Path, main_window: QMainWindow, remove: False) -> None:
    """
    Unregister a plugin by loading its configuration, dynamically importing the plugin class,
    and calling its unregister method.
    """
    data = load_plugin_config(path)
    if not data or not isinstance(data.get("extention"), dict):
        logger.critical("Extension config file doesn't have the correct structure")
        return

    extention = data["extention"]
    name = extention.get("name", "").lower()
    entry_point = extention.get("entrypoint", "")

    if not name or not entry_point:
        logger.critical(
            "Extension config file doesn't have the correct structure at ['extention']['name'] or ['extention']['entrypoint']")
        return

    # Construct the module and class names
    module_name = f"plugins.{name}.{entry_point.split('.')[0]}"
    class_name = entry_point.split(".")[-1]

    # Dynamically import the plugin class
    plugin_class = get_plugin_class(module_name, class_name)
    if not plugin_class or not issubclass(plugin_class, PluginBase):
        logger.error(f"Class '{plugin_class}' is not a subclass of '{PluginBase}'")
        return

    # Initialize and unregister the plugin
    plugin: PluginBase = plugin_class(main_window)
    plugin.unregister()
    remove_plugin_config(path, name, remove)
    logger.info(f"'{plugin}' unregistered successfully.")


def load_plugins(main_window: QMainWindow) -> None:
    """
    Load all plugins listed in the plugins.yml file and register them if they are not already registered.
    """
    plugins_path = BASE_DIR / "plugins"
    plugins_path.mkdir(parents=True, exist_ok=True)
    config_file_path = plugins_path / "plugins.yml"

    if not config_file_path.exists() or not config_file_path.is_file():
        logger.error("Plugins configuration file does not exist.")
        return

    # Load the plugins configuration
    with config_file_path.open("r", encoding="utf-8") as plugin_file:
        plugins_config = yaml.safe_load(plugin_file) or {"plugins": {}}
        plugins_config = validate_plugins_config(plugins_config)

        # Iterate through all plugins and register them if they are not already registered
        for name, plugin in plugins_config["plugins"].items():
            if plugin.get("installed"):
                path = Path(plugin["path"])
                if path.exists():
                    try:
                        logger.info(f"Registering Plugin '{name}'")
                        register_plugin(path, main_window)
                    except Exception as e:
                        logger.critical(f"Failed to load plugin '{name}': {e}")
                else:
                    logger.error(f"Plugin '{name}' does not exist at '{path}'")
            else:
                logger.info(f"Plugin '{name}' is not marked for installation.")
