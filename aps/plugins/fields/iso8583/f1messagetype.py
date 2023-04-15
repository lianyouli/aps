'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 20:25:20
LastEditors: Arthur
LastEditTime: 2023-04-15 18:22:53
Description: f1 message type
'''
from aps.plugins import IFieldPlugin
from aps.apstypes import ApsData, ApsRouter, ApsRecord
from aps.apstypes.messagetype import MessageType


class F1MessageTypeRecord(ApsRecord):
    messageType: MessageType

    @property
    def length(self):
        return len(self.messageType)

    def __init__(self, messageType):
        self.messageType = messageType


class F1MessageType(IFieldPlugin):
    fieldName = "f1messagetype"

    def before(self) -> bool:
        raise NotImplementedError("Not Implemented")

    def transform(self) -> ApsData:
        # ApsData(router=None, message={"f1messagetype": "0000"}, aux={})
        return NotImplementedError("Not Implemented")

    def after(self) -> bool:
        raise NotImplementedError("Not Implemented")
