from pathlib import Path

import yaml

from src.core.utils.settings import BASE_DIR
from src.core.utils.DataStructure import PluginConfigStruct

def register_plugin(path: Path):
    with open(path / "config.yml", "r") as file:
        data: PluginConfigStruct = yaml.load(file.read(), yaml.Loader)
        data["extention"]["name"]