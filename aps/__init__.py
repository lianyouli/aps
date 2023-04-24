'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 16:09:35
LastEditors: Arthur
LastEditTime: 2023-04-23 11:05:36
Description: Arthur's Payment System
'''
import pathlib

__VERSION__ = "1.0.0"
__VERSION_EPOCH__ = 1680957107

__APS_PLUGINS_HOME__ = pathlib.Path(__file__).absolute().parent.joinpath("plugins").as_posix()

from aps.utils.log import logger

# Aps Role
from aps.apstypes import ApsRole

APSROLE = ApsRole.ALL_MEMBERS

APSROLE_ACCEPTOR = '156100002901'
APSROLE_ACQUIERE = '156100002900'
APSROLE_FORWARDER = '15610000000'
APSROLE_NETWORKSCHEME = '156900000000'
APSROLE_ISSUER = '156600000000'

# Aps F1 Message fieldName
APS_FIELD_F1FIELDNAME = "f1messagetype"
