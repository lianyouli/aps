'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-15 15:03:41
LastEditors: Arthur
LastEditTime: 2023-04-18 22:07:07
Description: PAN
'''

from aps.plugins import IFieldPlugin
from aps.apstypes import ApsData, ApsRouter, ApsRecord, ApsContext
from aps.apstypes.messagetype import MessageType
from aps.exceptions import ApsException
from typing import Union


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
    fieldId = 1002

    def transform(self) -> Union[ApsData, ApsException]:
        assert self.data is not None
        return self.data
