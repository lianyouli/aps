'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-15 15:03:41
LastEditors: Arthur
LastEditTime: 2023-04-17 22:14:30
Description: PAN
'''

from aps.plugins import IFieldPlugin
from aps.apstypes import ApsData, ApsRouter, ApsRecord
from aps.apstypes.messagetype import MessageType


class F2PanRecord(ApsRecord):
    """F2PanRecord F2Pan Record
    """
    pan: str

    @property
    def length(self):
        return len(self.pan)

    def __init__(self, pan):
        self.pan = pan

    def binNumber(self, length=8):
        return self.pan[:length]


class F2Pan(IFieldPlugin):
    fieldName = "f2pan"

    def before(self) -> bool:
        raise NotImplementedError("Not Implemented")

    def transform(self) -> ApsData:
        # do nothing
        return self.data

    def after(self) -> bool:
        raise NotImplementedError("Not Implemented")
