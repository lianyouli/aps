'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 20:45:02
LastEditors: Arthur
LastEditTime: 2023-04-09 21:40:22
Description: Message Type Code
'''


from enum import Enum


class MessageType(str, Enum):
    S0100 = '0100'
    S0110 = '0110'
    S0200 = '0200'
    S0210 = '0210'
    S0220 = '0220'
    S0230 = '0230'
    S0420 = '0420'
    S0430 = '0430'
    D0100 = '0100'
    D0110 = '0110'
    D0220 = '0220'
    D0230 = '0230'
    D0420 = '0420'
    D0430 = '0430'
    A0620 = '0620'
    A0630 = '0630'
    A0800 = '0800'
    A0810 = '0810'
    A0820 = '0820'
    A0830 = '0830'
    
    AUTH_REQUEST = S0100
    AUTH_RESPONSE = S0110
    PRE_AUTH_REQUEST = S0100
    PRE_AUTH_RESPONSE = S0110
    PRE_AUTH_CANCELATION_REQUEST = S0100
    PRE_AUTH_CANCELATION_RESPONSE = S0110
    ACCOUNT_VERIFICATION_REQUEST = S0100
    ACCOUNT_VERIFICATION_RESPONSE = S0110
