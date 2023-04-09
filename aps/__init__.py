'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 16:09:35
LastEditors: Arthur
LastEditTime: 2023-04-09 20:39:25
Description: Arthur's Payment System
'''
import pathlib

__version__ = "1.0.0"
__VERSION_EPOCH__ = 1680957107

__APS_PLUGINS_HOME__ = pathlib.Path(__file__).absolute().parent.joinpath("plugins").as_posix()
