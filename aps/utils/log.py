'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 20:32:24
LastEditors: Arthur
LastEditTime: 2023-04-09 07:47:04
Description: logging configuration
'''
import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)
logger = logging.getLogger('aps')
