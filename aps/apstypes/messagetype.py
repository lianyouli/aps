'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 20:45:02
LastEditors: Arthur
LastEditTime: 2023-04-24 22:17:10
Description: Message Type Code
'''

from enum import Enum
from abc import abstractmethod, ABCMeta
import os
from aps.apstypes import ApsContext, ApsData
from aps import logger, APS_FIELD_F1FIELDNAME
from statemachine import State, StateMachine
from dataclasses import dataclass


class _MessageTypeEnum(Enum):
    """_MessageTypeEnum 消息类型枚举值父类型
    受 https://github.com/loggi/python-choicesenum 启发
    :param value: 真实枚举值
    :param display: 枚举值描述信息
    :param msgType: 枚举值类型，主要是区分同一个枚举值对应多种枚举类型
    """

    def __new__(cls, value, display=None, msgType=None):
        """__new__ _summary_

        :param value: 真实枚举值
        :param display: 枚举值描述信息
        :param msgType: 枚举值类型，主要是区分同一个枚举值对应多种枚举类型
        :return: _description_
        """
        obj = object.__new__(cls)
        obj._value_ = f"{value}{msgType}" if msgType is not None else value
        obj._display_ = display
        obj._msgType_ = msgType
        return obj

    @property
    def display(self):
        """display 属性方式访问
        返回display消息，如果没有设置display，则返回使用空格替换_的name的大写形式
        """
        return self._display_ if self._display_ is not None else self.name.replace("_", " ").upper()

    def __len__(self) -> int:
        """__len__ 返回真实value的值的长度
        """
        return len(self.value) if self._msgType_ is None else len(self.value) - len(self._msgType_)

    def __str__(self) -> str:
        return str(self.value) if self._msgType_ is None else str(self.value)[:(len(str(self.value)) - len(self._msgType_))]

    def __hash__(self) -> int:
        return hash(self.value)

    def __repr__(self) -> str:
        curr_value = self.value
        if self._msgType_ is not None:
            curr_value = self.value[:(len(self.value) - len(self._msgType_))]

        return str({"name": self.name, "value": curr_value, "display": self.display, "type": self._msgType_})

    @staticmethod
    def _get_value(item):
        return getattr(item, 'value', item)

    def __eq__(self, other) -> bool:
        return self.value == self._get_value(other)


class MessageType(_MessageTypeEnum):
    """MessageType message type enum
    - I stands for Initial
    - S stands for Single message
    - D stands for Dual message
    - A stands for Administration
    """
    # I stands for Initial
    # Initial message type
    I0000 = '0000', "INIT"

    # M stands for Message[single or dual]
    M0100 = '0100', "AUTH_REQUEST"
    M0110 = '0110', "AUTH_RESPONSE"
    M0200 = '0200', "FIN_REQUEST"
    M0210 = '0210', "FIN_RESPONSE"
    M0220 = '0220', "FIN_NOTIFICATION_REQUEST"
    M0230 = '0230', "FIN_NOTIFICATION_RESPONSE"
    M0420 = '0420', "REVERSAL_REQUEST"
    M0430 = '0430', "REVERSAL_RESPONSE"

    # A stands for Administration
    A0620 = '0620'
    A0630 = '0630'
    A0800 = '0800'
    A0810 = '0810'
    A0820 = '0820'
    A0830 = '0830'

    AUTH_REQUEST = M0100
    AUTH_RESPONSE = M0110
    PRE_AUTH_REQUEST = M0100
    PRE_AUTH_RESPONSE = M0110
    PRE_AUTH_CANCELATION_REQUEST = '0100', "PRE_AUTH_CANCELATION_REQUEST", "CANCELATION"
    PRE_AUTH_CANCELATION_RESPONSE = '0110', "PRE_AUTH_CANCELATION_RESPONSE", "CANCELATION"
    ACCOUNT_VERIFICATION_REQUEST = M0100
    ACCOUNT_VERIFICATION_RESPONSE = M0110


class MessageTypeMachine(StateMachine):
    INITIAL_REQUEST = State(value=MessageType.I0000, initial=True)

    # SINGLE_AUTH_REQUEST = INITIAL_REQUEST
    AUTH_REQUEST = State(value=MessageType.M0100)
    AUTH_RESPONSE = State(value=MessageType.M0110)

    # SINGLE_PRE_AUTH_REQUEST = INITIAL_REQUEST
    PRE_AUTH_REQUEST = State(value=MessageType.M0100)
    PRE_AUTH_RESPONSE = State(value=MessageType.M0110)

    # SINGLE_PRE_AUTH_CANCELATION_REQUEST = INITIAL_REQUEST
    PRE_AUTH_CANCELATION_RESPONSE = State(value=MessageType.PRE_AUTH_CANCELATION_REQUEST)

    # SINGLE_ACCOUNT_VERIFICATION_REQUEST = INITIAL_REQUEST
    ACCOUNT_VERIFICATION_REQUEST = State(value=MessageType.M0100)
    ACCOUNT_VERIFICATION_RESPONSE = State(value=MessageType.M0110)

    authenticate = INITIAL_REQUEST.to(AUTH_REQUEST, cond="initialize") \
                      | AUTH_REQUEST.to(AUTH_RESPONSE, cond="mandate")

    pre_authenticate = INITIAL_REQUEST.to(PRE_AUTH_REQUEST, cond="initialize") \
                          | PRE_AUTH_REQUEST.to(PRE_AUTH_RESPONSE, cond='mandate', unless="cancel_mandate") \
                          | PRE_AUTH_REQUEST.to(PRE_AUTH_CANCELATION_RESPONSE, cond='cancel_mandate')

    verify_account = INITIAL_REQUEST.to(ACCOUNT_VERIFICATION_REQUEST, cond="initialize") \
                        | ACCOUNT_VERIFICATION_REQUEST.to(ACCOUNT_VERIFICATION_RESPONSE, cond="mandate")

    def initialize(self, currentMessageType):
        logger.debug(f"the current messageType is {currentMessageType}")
        return True

    def mandate(self, currentMessageType: MessageType):
        logger.debug(f"the current messageType is {currentMessageType} \t {MessageType.M0110.value}")
        return MessageType.M0110.value == currentMessageType.value if currentMessageType is not None else False

    def cancel_mandate(self, currentMessageType: MessageType):
        logger.debug(f"current MessageType Name: {currentMessageType.name} and its value {currentMessageType.value}")
        return MessageType.PRE_AUTH_CANCELATION_RESPONSE.value == currentMessageType.value \
            and MessageType.PRE_AUTH_CANCELATION_RESPONSE.display == currentMessageType.display \
                if currentMessageType is not None else False

    def financialize(self, currentMessageType: MessageType):
        return MessageType.M0210.value == currentMessageType.value if currentMessageType is not None else False

    def notify(self, currentMessageType: MessageType):
        return MessageType.M0230.value == currentMessageType.value if currentMessageType is not None else False

    def reversalize(self, currentMessageType: MessageType):
        return MessageType.M0430.value == currentMessageType.value if currentMessageType is not None else False


class AbstractPersistentModel(metaclass=ABCMeta):

    def __init__(self) -> None:
        self._state = None

    def __repr__(self) -> str:
        return f"{type(self).__name__}(state={self.state})"

    @property
    def state(self):
        if self._state is None:
            self._state = self._read_state()

        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self._write_state(value)

    @abstractmethod
    def _read_state(self):
        ...

    @abstractmethod
    def _write_state(self, value):
        ...


class InMemoryMessageTypePersistentModel(AbstractPersistentModel):

    def __init__(self, data: ApsData) -> None:
        super().__init__()
        self.data = data

    def _read_state(self):
        messageTypeRecord = self.data.message.get(APS_FIELD_F1FIELDNAME)
        logger.debug(f"the messageType value: {messageTypeRecord.messageType} will be read into state")
        return messageTypeRecord.messageType if messageTypeRecord is not None and messageTypeRecord.messageType != "" else None

    def _write_state(self, value):
        logger.debug(f"the messageType persistent {value}")
        self.data.message.get(APS_FIELD_F1FIELDNAME).messageType = value


class FileMessageTypePersistentModel(AbstractPersistentModel):

    def __init__(self, file) -> None:
        super().__init__()
        self.file = file  # type: os.TextIOWrapper

    def _read_state(self):
        self.file.seek(0)
        state = self.file.read().strip()
        return state if state != "" else None

    def _write_state(self, value):
        self.file.seek(0)
        self.file.truncate(0)
        self.file.write(value)
