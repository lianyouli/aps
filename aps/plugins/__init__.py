'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-09 20:38:23
LastEditors: Arthur
LastEditTime: 2023-04-09 20:48:10
Description: plugin interface definition
'''
from yapsy.IPlugin import IPlugin
from aps.apstypes import ApsData, ApsConfig


class IFieldPlugin(IPlugin):
    categoryName = "FieldPlugin"

    def __init__(self):
        super().__init__()
        self.data: ApsData = None
        self.config: ApsConfig = None

    def set(self, data: ApsData, config: ApsConfig = None):
        self.data = data
        self.config = config

    def activate(self):
        return super().activate()

    def deactivate(self):
        return super().deactivate()

    def before(self) -> bool:
        raise NotImplementedError("Not Implemented")

    def transform(self) -> ApsData:
        assert self.data is not None
        raise NotImplementedError("Not Implemented")

    def after(self) -> bool:
        raise NotImplementedError("Not Implemented")
