'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 20:23:09
LastEditors: Arthur
LastEditTime: 2023-04-09 07:50:36
Description: testing
'''
import logging

# DEBUG = logging.DEBUG
# CRITICAL = logging.CRITICAL
# INFO = logging.INFO
# WARNING = logging.WARNING
# ERROR = logging.ERROR

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)
logger = logging.getLogger("aps.tests")
# logger.setLevel(level=logging.DEBUG)
