'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 20:23:09
LastEditors: Arthur
LastEditTime: 2023-04-23 21:26:03
Description: testing
'''
import logging

# DEBUG = logging.DEBUG
# CRITICAL = logging.CRITICAL
# INFO = logging.INFO
# WARNING = logging.WARNING
# ERROR = logging.ERROR

# logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)
logging.basicConfig(format="%(filename)s - %(funcName)s - %(lineno)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.DEBUG)
logger = logging.getLogger("aps.tests")
# logger.setLevel(level=logging.DEBUG)
