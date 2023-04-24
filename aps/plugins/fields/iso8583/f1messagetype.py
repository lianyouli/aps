'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 20:25:20
LastEditors: Arthur
LastEditTime: 2023-04-23 21:30:34
Description: f1 message type
'''
from aps.plugins import IFieldPlugin
from aps.apstypes import ApsData, ApsRouter, ApsRecord, ApsContext
from aps.apstypes.messagetype import MessageType
from aps.exceptions import ApsException
from typing import Union
from aps import APS_FIELD_F1FIELDNAME
from dataclasses import dataclass


@dataclass
class F1MessageTypeRecord(ApsRecord):
    messageType: str

    @property
    def length(self):
        return len(self.messageType)

    def __init__(self, messageType):
        self.messageType = messageType


class F1MessageType(IFieldPlugin):
    fieldName = APS_FIELD_F1FIELDNAME
    fieldId = 1001

    def transform(self) -> ApsData:
        # ApsData(router=None, message={"f1messagetype": "0000"}, aux={})
        # return NotImplementedError("Not Implemented")
        return self.context.data
