'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-09 21:41:44
LastEditors: Arthur
LastEditTime: 2023-04-15 13:00:09
Description: Test apstypes module
'''
import unittest
from tests import logger
from aps.apstypes.messagetype import MessageType
from aps.apstypes import ApsData, ApsRouter, ApsContext, ApsRecord
from aps.plugins.fields.iso8583.f1messagetype import F1MessageTypeRecord


class TestApsTypes(unittest.TestCase):
    def setUp(self):
        self.destId = "90010000"
        self.srcId = "34010000"
        self.batchNo = "01"
        self.version = "20230410.1681135544"

    def test_header_length(self):

        router = ApsRouter(destinationID=self.destId,
                           sourceID=self.srcId, batchNo=self.batchNo, version=self.version)
        self.assertEqual(router.headerLength,
                         len(self.destId) + len(self.srcId) + len(self.batchNo) + len(self.version) + len("000000"))
        self.assertEqual(router.totalMessageLength, router.headerLength)

    def test_message_length(self):
        router = ApsRouter(destinationID=self.destId,
                           sourceID=self.srcId, batchNo=self.batchNo, version=self.version)
        data = ApsData(router, message={"f1messagetype": F1MessageTypeRecord(
            MessageType.ACCOUNT_VERIFICATION_REQUEST)}, aux=None)
        assert data.router.totalMessageLength == data.router.headerLength + \
            len(MessageType.ACCOUNT_VERIFICATION_REQUEST)


class TestApsTypesMessageType(unittest.TestCase):
    def test_single_message_type_by_code(self):
        self.assertEqual(MessageType.S0100, '0100')
        self.assertEqual(MessageType.S0110, '0110')

    def test_single_message_type_by_name(self):
        self.assertEqual(MessageType.AUTH_REQUEST, '0100')
        self.assertEqual(MessageType.AUTH_RESPONSE, '0110')
        self.assertEqual(MessageType.ACCOUNT_VERIFICATION_REQUEST, '0100')
        self.assertEqual(MessageType.ACCOUNT_VERIFICATION_RESPONSE, '0110')


if __name__ == "__main__":
    unittest.main()
