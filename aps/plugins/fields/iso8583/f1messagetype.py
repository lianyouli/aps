'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 20:25:20
LastEditors: Arthur
LastEditTime: 2023-04-09 20:52:00
Description: f1 message type
'''
from aps.plugins import IFieldPlugin
from aps.apstypes import ApsData, ApsRouter


class F1MessageType(IFieldPlugin):
    pluginName = "f1messagetype"

    def before(self) -> bool:
        raise NotImplementedError("Not Implemented")

    def transform(self) -> ApsData:
        return ApsData(router=None, message={"f1messagetype": "0000"}, aux={})

    def after(self) -> bool:
        raise NotImplementedError("Not Implemented")
