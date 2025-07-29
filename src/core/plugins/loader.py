import importlib
from pathlib import Path
from typing import Callable, Optional

import yaml
from PySide6.QtCore import QSettings

from src.core.utils.DataStructure import (PluginConfigStruct,
                                          PluginsConfigFileStruct)
from src.core.utils.logger import get_logger
from src.plugins import *

logger = get_logger()


def list_plugins_from_storage() -> PluginsConfigFileStruct:
    """
    Validate the structure of the plugins configuration stored in QSettings.
    Returns a default configuration if invalid.
    """
    settings = QSettings()
    plugins_config = settings.value("plugins_config", None)

    if not isinstance(plugins_config, dict):
        return {"plugins": {}}

    plugins = plugins_config.get("plugins", {})
    if not isinstance(plugins, dict):
        return {"plugins": {}}

    return plugins_config


def get_registerd_plugins() -> set:
    return set(QSettings().value("registerd_plugins", set()))


def write_plugin_config(path: Path, name: str) -> None:
    """
    Write the plugin configuration to QSettings.
    """
    plugins_config = list_plugins_from_storage()
    plugins_config["plugins"][name] = {
        "path": str(path.absolute()),  # Store absolute path
        "installed": True
    }

    registered_plugins = get_registerd_plugins()
    registered_plugins.add(name)
    QSettings().setValue('plugins_config', plugins_config)
    QSettings().setValue("registerd_plugins", registered_plugins)


def remove_plugin_config(name: str, remove: bool = False) -> None:
    """
    Update plugin configuration in QSettings when uninstalling/disabling.
    """

    plugins_config = list_plugins_from_storage()
    registered_plugins = get_registerd_plugins()
    registered_plugins.remove(name)
    if remove:
        plugins_config["plugins"].pop(name, None)
    else:
        plugin = plugins_config["plugins"].get(name)
        if plugin:
            plugin["installed"] = False

    QSettings().setValue("plugins_config", plugins_config)
    QSettings().setValue("registerd_plugins", registered_plugins)


def load_plugin_config(path: Path) -> Optional[PluginConfigStruct]:
    """
    Load plugin configuration from config.yml with validation.
    """
    try:
        config_path = path / "config.yml"
        if config_path.exists() and config_path.is_file():
            with config_path.open("r", encoding="utf-8") as file:
                config = yaml.safe_load(file)
                return config

    except (FileNotFoundError, yaml.YAMLError) as e:
        logger.error(f"Failed to load plugin config from {path}: {e}")
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


def register_plugin(path: Path, add_func: Callable) -> bool:
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
    if name in get_registerd_plugins():
        return True

    # Construct the module and class names
    module_name = f"plugins.{name}.{entry_point.split('.')[0]}"
    class_name = entry_point.split(".")[-1]

    # Dynamically import the plugin class
    plugin_class = get_plugin_class(module_name, class_name)
    if not plugin_class or not hasattr(plugin_class, "register"):
        logger.error(
            f"Class '{plugin_class}' does't has correct stucture or does not exist.\nNo method named `register`")
        return False

    # Initialize and register the plugin
    plugin = plugin_class(add_func=add_func)
    plugin.register()
    write_plugin_config(path, name)
    return True


def unregister_plugin(path: Path, remove_func: Callable,  remove: bool = False) -> bool:
    """
    Unregister a plugin by loading its configuration, dynamically importing the plugin class,
    and calling its unregister method.
    """
    data = load_plugin_config(path)
    if not data or not isinstance(data.get("extention"), dict):
        logger.critical("Extension config file doesn't have the correct structure.")
        return False

    extention = data["extention"]
    name = extention.get("name", "").lower()
    entry_point = extention.get("entrypoint", "")

    if not name or not entry_point:
        logger.critical(
            "Extension config file doesn't have the correct structure at ['extention']['name'] or ['extention']['entrypoint']")
        return False

    # Construct the module and class names
    module_name = f"plugins.{name}.{entry_point.split('.')[0]}"
    class_name = entry_point.split(".")[-1]

    # Dynamically import the plugin class
    plugin_class = get_plugin_class(module_name, class_name)
    if not plugin_class or not hasattr(plugin_class, "unregister"):
        logger.error(
            f"Class '{plugin_class}' does not exist or does't has correct stracture.\nNo method named `unregister`")
        return False

    # Initialize and unregister the plugin
    plugin = plugin_class(remove_func=remove_func)
    plugin.unregister()
    remove_plugin_config(name, remove)

    return True


def load_external_plugins(add_func: Callable) -> None:
    """
    Load all plugins listed in the plugins.yml file and register them if they are not already registered.
    """
    # Load the plugins configuration
    plugins_config = list_plugins_from_storage()

    # Iterate through all plugins and register them if they are not already registered
    for name, plugin in plugins_config["plugins"].items():
        if plugin.get("installed") is True:
            path = Path(plugin["path"])
            if path.exists():
                try:
                    register_plugin(path, add_func)
                except Exception as e:
                    logger.critical(f"Failed to load plugin '{name}'\nError: {e}")
            else:
                logger.error(f"Plugin '{name}' does not exist at '{path}'")


def load_internal_plugins(add_func: Callable) -> None:
    """
    Load all interal plugins.
    """
    # Load the plugins configuration
    Sales(add_func=add_func).register()
