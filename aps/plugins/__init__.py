'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-09 20:38:23
LastEditors: Arthur
LastEditTime: 2023-04-15 18:23:26
Description: plugin interface definition
'''
from yapsy.IPlugin import IPlugin
from aps.apstypes import ApsData, ApsContext


class ISinkerPlugin(IPlugin):
    """ISinkerPlugin SinkerPlugin Interface
    """
    categoryName = "SinkerPlugin"

    def write(data: ApsData) -> int:
        raise NotImplementedError("Not Implemented")


class IFieldPlugin(IPlugin):
    """IFieldPlugin FieldPlugin Interface
    """
    categoryName = "FieldPlugin"
    fieldName: str = ""

    def __init__(self):
        super().__init__()
        self.data: ApsData = None
        self.config: ApsContext = None

    def set(self, data: ApsData, context: ApsContext = None):
        self.data = data
        self.config = context

    def before(self) -> bool:
        raise NotImplementedError("Not Implemented")

    def transform(self) -> ApsData:
        assert self.data is not None
        raise NotImplementedError("Not Implemented")

    def after(self) -> bool:
        raise NotImplementedError("Not Implemented")
