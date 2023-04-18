'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-09 20:38:23
LastEditors: Arthur
LastEditTime: 2023-04-18 22:06:06
Description: plugin interface definition
'''
from yapsy.IPlugin import IPlugin
from aps.apstypes import ApsData, ApsContext
from aps import logger
from abc import ABCMeta, abstractmethod
from aps.exceptions import ApsException
from typing import Union


class ISinkerPlugin(IPlugin):
    """ISinkerPlugin SinkerPlugin Interface
    """
    categoryName = "SinkerPlugin"

    def write(data: ApsData) -> int:
        raise NotImplementedError("Not Implemented")


class IFieldPlugin(IPlugin, metaclass=ABCMeta):
    """IFieldPlugin FieldPlugin Interface
    """
    categoryName = "FieldPlugin"
    fieldName: str = ""
    fieldId: int = 0

    def __init__(self):
        super().__init__()
        self.data: ApsData = None
        self.config: ApsContext = None

    def set(self, data: ApsData, context: ApsContext = None):
        self.data: ApsData = data
        self.config: ApsContext = context

    def enter(self) -> bool:
        return True

    @abstractmethod
    def transform(self) -> Union[ApsData, ApsException]:
        assert self.data is not None
        raise NotImplementedError("Not Implemented")

    def exit(self) -> bool:
        return True

    def process(self) -> Union[ApsData, ApsException]:
        if self.enter():
            logger.info(f"{self.fieldName} enters the processing successfully")
            data = self.transform()

            if self.exit():
                logger.info(f"{self.fieldName} exits the processing successfully")
            else:
                logger.error(f"{self.fieldName} exits the processing with failure")
            return data

        raise ApsException(f"{self.fieldName} enters the processing successfully")
