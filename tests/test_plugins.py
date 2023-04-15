'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 22:35:59
LastEditors: Arthur
LastEditTime: 2023-04-15 18:40:11
Description: test the plugins
'''
from aps.apstypes import ApsContext, ApsRouter, ApsData
import aps
from aps.plugins.fields.iso8583.f1messagetype import F1MessageType
from aps.plugins.fields.iso8583.f2pan import F2Pan, F2PanRecord
from aps.plugins import IFieldPlugin
from yapsy.PluginManager import PluginManager
import unittest
from tests import logger
import logging

logging.getLogger("yapsy").setLevel(logging.DEBUG)
# from yapsy import PluginInfo


class TestPlugins(unittest.TestCase):

    def setUp(self) -> None:
        self.assertIsNotNone(IFieldPlugin)
        categoryName = IFieldPlugin.categoryName
        self.assertIsNotNone(categoryName)

        self.manager = PluginManager(directories_list=[aps.__APS_PLUGINS_HOME__],
                                     categories_filter={IFieldPlugin.categoryName: IFieldPlugin},
                                     plugin_info_ext="plugin")
        self.manager.collectPlugins()

    def test_show_plugins_info(self):
        self.assertGreater(len(self.manager.getAllPlugins()), 0, 'the plugins must be existing')
        for p in self.manager.getAllPlugins():
            logger.info(f"{p.author}, {p.name}, {p.version}, {p.website}, {p.description}")
            # logger.debug(dir(p.plugin_object))

    def test_f1messageType(self):
        logger.info(f"category: {IFieldPlugin.categoryName}")
        f1msgtype = self.manager.getPluginByName("f1messagetype", category=IFieldPlugin.categoryName)
        logger.debug(f"{dir(f1msgtype)}")
        self.assertIsNotNone(f1msgtype)

        f1: IFieldPlugin = f1msgtype.plugin_object
        self.assertIsNotNone(f1)

        logger.debug(dir(f1))

        f1.set(data=ApsData(ApsRouter(destinationID="90010000", sourceID="31040000", batchNo="01"), message=None, aux=None),
               context=ApsContext(context={}))

        logger.info(f1.transform())

    def test_f1messageType_by_type(self):
        logger.info(f"category: {F1MessageType.categoryName}")
        f1msgtype = self.manager.getPluginByName(F1MessageType.fieldName, category=F1MessageType.categoryName)
        self.assertIsNotNone(f1msgtype)

        f1: F1MessageType = f1msgtype.plugin_object
        self.assertIsNotNone(f1)

        logger.debug(dir(f1))
        data = ApsData(ApsRouter(destinationID="90010000", sourceID="31040000", batchNo="01"), message={}, aux={})
        f1.set(data=data, context=ApsContext(context={}))

        logger.info(f1.transform())

    def test_f2pan(self):
        logger.info(f"category: {F2Pan.categoryName}")
        f2pan = self.manager.getPluginByName(F2Pan.fieldName, category=F2Pan.categoryName)
        self.assertIsNotNone(f2pan)

        f2: F2Pan = f2pan.plugin_object
        self.assertIsNotNone(f2)

        logger.debug(dir(f2))
        data = ApsData(ApsRouter(destinationID="90010000", sourceID="31040000", batchNo="01"), message={}, aux={})
        f2.set(data=data, context=ApsContext(context={}))

        logger.info(f2.transform())
        assert f2.data == f2.transform()

    def test_f2pan_pan_and_bin(self):
        logger.info(f"category: {F2Pan.categoryName}")
        f2pan = self.manager.getPluginByName(F2Pan.fieldName, category=F2Pan.categoryName)
        self.assertIsNotNone(f2pan)

        f2: F2Pan = f2pan.plugin_object
        self.assertIsNotNone(f2)

        logger.debug(dir(f2))
        pan = "891234567890123"
        data = ApsData(ApsRouter(destinationID="90010000", sourceID="31040000", batchNo="01"),
                       message={"f2pan": F2PanRecord(pan)},
                       aux={})
        f2.set(data=data, context=ApsContext(context={}))

        logger.info(f2.transform())
        assert f2.data == f2.transform()
        f2Record: F2PanRecord = f2.data.message.get(f2.fieldName)
        assert f2Record is not None
        assert f2Record.length == len(pan)
        assert f2Record.binNumber() == pan[:8]
        assert data.router.totalMessageLength == data.router.headerLength + f2Record.length


if __name__ == "__main__":
    unittest.main()
