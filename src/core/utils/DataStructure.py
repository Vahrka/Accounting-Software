from typing import TypedDict


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
