'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-08 22:35:59
LastEditors: Arthur
LastEditTime: 2023-04-09 20:55:45
Description: test the plugins
'''
import unittest
from yapsy.PluginManager import PluginManager
from aps.plugins import IFieldPlugin
# from yapsy import PluginInfo
from tests import logger
import aps
from aps.apstypes import ApsConfig, ApsRouter, ApsRejectRouter, ApsData


class TestPlugins(unittest.TestCase):

    def setUp(self) -> None:
        self.manager = PluginManager(directories_list=[aps.__APS_PLUGINS_HOME__],
                                     categories_filter={IFieldPlugin.categoryName: IFieldPlugin})
        self.manager.collectPlugins()

    def test_show_plugins_info(self):
        self.assertGreater(len(self.manager.getAllPlugins()), 0, 'the plugins must be existing')
        for p in self.manager.getAllPlugins():
            logger.info(f"{p.author}, {p.name}, {p.version}, {p.website}, {p.description}")
            # logger.debug(dir(p.plugin_object))

    def test_f1essageType(self):
        logger.info(f"category: {IFieldPlugin.categoryName}")
        f1msgtype = self.manager.getPluginByName("f1messagetype", category=IFieldPlugin.categoryName)
        self.assertIsNotNone(f1msgtype)

        f1: IFieldPlugin = f1msgtype.plugin_object
        self.assertIsNotNone(f1)

        logger.debug(dir(f1))

        f1.set(data=ApsData(ApsRouter(destinationID="90010000", sourceID="31040000", batchNo="01"), message={}, aux={}),
               config=ApsConfig(config={}))

        logger.info(f1.transform())


if __name__ == "__main__":
    unittest.main()
