'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 20:45:02
LastEditors: Arthur
LastEditTime: 2023-04-15 18:42:29
Description: data type definitions
'''
from typing import Dict, Union
# from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from functools import reduce
from aps import logger


@dataclass
class ApsRouter:
    """ Aps router
    """
    destinationID: str
    sourceID: str
    batchNo: str
    headerLength: int = 0
    totalMessageLength: int = 0
    transactionInfo: str = None
    userInfo: str = None
    version: str = "20230410.1681135544"
    rejectionCode: str = '000000'

    def __post_init__(self):
        logger.debug(f"the headerLength will be counted these values: {self.__dict__.values()}")
        self.headerLength = reduce(lambda x, y: x + y, [len(str(v)) for v in self.__dict__.values() if v])

        self.totalMessageLength = self.headerLength


@dataclass
class ApsRejectRouter(ApsRouter):
    """reject router which is based on `ApsRouter` with extra rejection information
    """
    rejectedByField: str = ""
    rejectionReason: str = ""

    def __post_init__(self):
        super().__post_init__()
        rejectLength = len(self.rejectedByField) + len(self.rejectionReason)
        self.headerLength = self.headerLength + rejectLength
        self.totalMessageLength = self.totalMessageLength + rejectLength


@dataclass
class ApsRecord:
    length: int = 0

    @property
    def length(self):
        raise NotImplementedError("Not Implemented")


@dataclass
class ApsData:
    """ Aps Data which contains the router:`Union[ApsRouter, ApsRejectRouter]` ,
    the message: `dict` and the aux(auxiliary): `dict`
    """
    router: Union[ApsRouter, ApsRejectRouter]
    message: Dict[str, ApsRecord]
    aux: Dict[str, ApsRecord]

    def __post_init__(self):
        if self.message:
            messageLengthList = [getattr(i, 'length') for i in self.message.values() if hasattr(i, 'length')]
            logger.debug(f"the message's messageLengthList is {messageLengthList}")
            self.router.totalMessageLength += reduce(lambda a, b: a + b, messageLengthList)
        if self.aux:
            messageLengthList = [getattr(i, 'length') for i in self.aux.values() if hasattr(i, 'length')]
            logger.debug(f"the aux's messageLengthList is {messageLengthList}")
            self.router.totalMessageLength += reduce(lambda a, b: a + b, messageLengthList)


@dataclass
class ApsContext:
    context: Dict
