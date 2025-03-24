from typing import Dict, TypedDict


class PluginConfigStructExt(TypedDict):
    name: str
    entrypoint: str
    verstion: str
    author: str


class PluginConfigStructSoft(TypedDict):
    version: str
    location: str


class PluginConfigStruct(TypedDict):
    extention: PluginConfigStructExt
    software: PluginConfigStructSoft


class PluginsItemConfigFileStruct(TypedDict):
    path: str
    installed: bool


class PluginsConfigFileStruct(TypedDict):
    plugins: Dict[str, PluginsItemConfigFileStruct]
