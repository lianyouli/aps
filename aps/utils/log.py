'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 20:32:24
LastEditors: Arthur
LastEditTime: 2023-04-23 21:25:48
Description: logging configuration
'''
import logging

logging.basicConfig(format="%(filename)s - %(funcName)s - %(lineno)d - %(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.DEBUG)
# logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#                     level=logging.DEBUG)
logger = logging.getLogger('aps')
