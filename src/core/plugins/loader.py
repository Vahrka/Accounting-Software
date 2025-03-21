import importlib
from pathlib import Path

import yaml
from PySide6.QtWidgets import QMainWindow

from src.core.plugins.plugin_base import PluginBase
from src.core.utils.DataStructure import PluginConfigStruct
from src.core.utils.logger import get_logger

logger = get_logger()


def register_plugin(path: Path, main_window: QMainWindow):
    """
    Register a plugin by loading its configuration and entry point.

    Args:
        path (Path): The path to the plugin directory containing the `config.yml` file.
        main_window (QMainWindow): The main window instance to pass to the plugin.

    Raises:
        ImportError: If the plugin module or class cannot be imported.
        AttributeError: If the specified class does not exist in the module.
    """
    try:
        # Load the plugin configuration from the YAML file
        with open(path / "config.yml", "r") as file:
            data: PluginConfigStruct = yaml.safe_load(file)  # Use safe_load for security
            name = data["extention"]["name"].lower()
            entry_point = data["extention"]["entrypoint"]

        # Construct the module name and extract the class name
        module_name = f"plugins.{name}.{entry_point.split('.')[0]}"
        class_name = entry_point.split(".")[-1]

        # Dynamically import the plugin module
        plugin_module = importlib.import_module(module_name, "plugins")

        # Check if the specified class exists in the module
        if not hasattr(plugin_module, class_name):
            logger.error(f"Module '{module_name}' has no attribute '{class_name}'")
            return

        # Get the plugin class
        plugin_class = getattr(plugin_module, class_name)

        # Ensure the plugin class is a subclass of PluginBase
        if not issubclass(plugin_class, PluginBase):
            logger.error(f"Class '{plugin_class}' is not a subclass of '{PluginBase}'")
            return

        # Create an instance of the plugin class
        plugin: PluginBase = plugin_class(main_window)

        # Register the plugin
        plugin.register()
        logger.debug(f"'{plugin}' registered successfully.")

    except ImportError as e:
        logger.critical(f"Cannot import '{entry_point}' from '{name}'. Ensure the path is correct.", exc_info=e)
    except Exception as e:
        logger.critical(f"Failed to register plugin: {e}", exc_info=e)


def unregister_plugin(path: Path, main_window: QMainWindow):
    """
    Unregister a plugin by loading its configuration and entry point.

    Args:
        path (Path): The path to the plugin directory containing the `config.yml` file.
        main_window (QMainWindow): The main window instance to pass to the plugin.

    Raises:
        ImportError: If the plugin module or class cannot be imported.
        AttributeError: If the specified class does not exist in the module.
    """
    try:
        # Load the plugin configuration from the YAML file
        with open(path / "config.yml", "r") as file:
            data: PluginConfigStruct = yaml.safe_load(file)  # Use safe_load for security
            name = data["extention"]["name"].lower()
            entry_point = data["extention"]["entrypoint"]

        # Construct the module name and extract the class name
        module_name = f"plugins.{name}.{entry_point.split('.')[0]}"
        class_name = entry_point.split(".")[-1]

        # Dynamically import the plugin module
        plugin_module = importlib.import_module(module_name, "plugins")

        # Check if the specified class exists in the module
        if not hasattr(plugin_module, class_name):
            logger.error(f"Module '{module_name}' has no attribute '{class_name}'")
            return

        # Get the plugin class
        plugin_class = getattr(plugin_module, class_name)

        # Ensure the plugin class is a subclass of PluginBase
        if not issubclass(plugin_class, PluginBase):
            logger.error(f"Class '{plugin_class}' is not a subclass of '{PluginBase}'")
            return

        # Create an instance of the plugin class
        plugin: PluginBase = plugin_class(main_window)

        # Unregister the plugin
        plugin.unregister()
        logger.debug(f"'{plugin}' unregistered successfully.")

    except ImportError as e:
        logger.critical(f"Cannot import '{entry_point}' from '{name}'. Ensure the path is correct.", exc_info=e)
    except Exception as e:
        logger.critical(f"Failed to unregister plugin: {e}", exc_info=e)
