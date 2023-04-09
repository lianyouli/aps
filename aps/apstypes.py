'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 20:45:02
LastEditors: Arthur
LastEditTime: 2023-04-09 09:00:54
Description: data type definitions
'''
from typing import Dict, Union
from dataclasses import dataclass
from functools import reduce


@dataclass
class ApsRouter:
    """ Aps router
    """
    _headerLength: int
    version: str
    _totalMessageLength: int
    destinationID: str
    sourceID: str
    batchNo: str
    transactionInfo: str
    userInfo: str
    rejectionCode: str

    @property
    def headerLength(self) -> int:
        return reduce(lambda x, y: x + y, [len(v) for _, v in locals()])

    @property
    def totalMessageLength(self) -> int:
        return self._totalMessageLength

    @totalMessageLength.setter
    def totalMessageLength(self, messageLength: int = 0):
        assert messageLength >= 0
        self._totalMessageLength = self.headerLength + messageLength

    def __init__(self,
                 destinationID: str,
                 sourceID: str,
                 batchNo: str,
                 transactionInfo: str = None,
                 userInfo: str = None,
                 version: str = "1.0.0",
                 rejectionCode: str = '000000'):
        self.version = version
        self.destinationID = destinationID
        self.sourceID = sourceID
        self.batchNo = batchNo
        self.transactionInfo = transactionInfo
        self.userInfo = userInfo
        self.rejectionCode = rejectionCode


@dataclass
class ApsRejectRouter(ApsRouter):
    """reject router which is based on `ApsRouter` with extra rejection information
    """
    rejectedByField: str
    rejectionReason: str

    def __init__(self,
                 destinationID: str,
                 sourceID: str,
                 batchNo: str,
                 rejectedByField: str,
                 rejectionReason: str,
                 transactionInfo: str = None,
                 userInfo: str = None,
                 version: str = "1.0.0",
                 rejectionCode: str = '000000'):
        self.version = version
        self.destinationID = destinationID
        self.sourceID = sourceID
        self.batchNo = batchNo
        self.transactionInfo = transactionInfo
        self.userInfo = userInfo
        self.rejectionCode = rejectionCode
        self.rejectedByField = rejectedByField
        self.rejectionReason = rejectionReason


@dataclass
class ApsData:
    """ Aps Data which contains the router:`Union[ApsRouter, ApsRejectRouter]` ,
    the message: `dict` and the aux(auxiliary): `dict`
    """
    router: Union[ApsRouter, ApsRejectRouter]
    message: Dict
    aux: Dict


@dataclass
class ApsConfig:
    config: Dict
