'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 20:25:20
LastEditors: Arthur
LastEditTime: 2023-04-18 22:06:55
Description: f1 message type
'''
from aps.plugins import IFieldPlugin
from aps.apstypes import ApsData, ApsRouter, ApsRecord, ApsContext
from aps.apstypes.messagetype import MessageType
from aps.exceptions import ApsException
from typing import Union


class F1MessageTypeRecord(ApsRecord):
    messageType: MessageType

    @property
    def length(self):
        return len(self.messageType)

    def __init__(self, messageType):
        self.messageType = messageType


class F1MessageType(IFieldPlugin):
    fieldName = "f1messagetype"
    fieldId = 1001

    def transform(self) -> ApsData:
        # ApsData(router=None, message={"f1messagetype": "0000"}, aux={})
        return NotImplementedError("Not Implemented")
