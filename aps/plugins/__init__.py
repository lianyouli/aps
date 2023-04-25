'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-09 20:38:23
LastEditors: Arthur
LastEditTime: 2023-04-23 10:16:27
Description: plugin interface definition
'''
from yapsy.IPlugin import IPlugin
from aps.apstypes import ApsData, ApsContext
from aps import logger
from abc import ABCMeta, abstractmethod
from enum import IntEnum


class TransformActionType(IntEnum):
    PASS = 1 << 0
    REJECT = 1 << 1
    PASS_WITH_DRAPBACK = 1 << 2


class ISinkerPlugin(IPlugin):
    """ISinkerPlugin SinkerPlugin Interface
    """
    categoryName = "SinkerPlugin"

    def write(context: ApsContext) -> int:
        raise NotImplementedError("Not Implemented")


class IFieldPlugin(IPlugin, metaclass=ABCMeta):
    """IFieldPlugin FieldPlugin Interface
    """
    categoryName = "FieldPlugin"
    fieldName: str = ""
    fieldId: int = 0

    def __init__(self):
        super().__init__()
        self.context: ApsContext = None

    def set(self, context: ApsContext = None):
        self.context: ApsContext = context

    def beforeTransform(self, action=TransformActionType.PASS) -> ApsContext:
        if action == TransformActionType.PASS:
            logger.info(f"{self.fieldName}-with {TransformActionType.PASS.name} will do nothing")
            return self.context
        elif action == TransformActionType.PASS_WITH_DRAPBACK:
            # with {TransformActionType.PASS.name} will do pass the process with drawback")
            raise NotImplementedError("You should implement the drawback handling")
        else:
            # reject
            raise NotImplementedError("You should implement the reject handling")

    @abstractmethod
    def transform(self) -> ApsData:
        assert self.context is not None
        raise NotImplementedError("Not Implemented")

    def afterTransform(self):
        pass

    def process(self) -> ApsData:
        self.context = self.beforeTransform()
        data = self.transform()
        self.afterTransform()
        return data
