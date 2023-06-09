'''
Author: Arthur lianyoucq@163.com
Date: 2023-04-09 21:41:44
LastEditors: Arthur
LastEditTime: 2023-04-25 22:04:56
Description: Test apstypes module
'''
import unittest
from tests import logger
from aps.apstypes.messagetype import MessageType
from aps.apstypes import ApsData, ApsRouter, ApsRole
from aps.plugins.fields.iso8583.f1messagetype import F1MessageTypeRecord


class TestApsRole(unittest.TestCase):

    def testRole(self):
        assert ApsRole.ACCETPOR == 1
        assert ApsRole.ACQUIRER == 1 << 1
        assert ApsRole.FORDWARDER == 1 << 2
        assert ApsRole.NETWORKSCHEME == 1 << 3
        assert ApsRole.ISSUER == 1 << 4
        assert ApsRole.ACQUIRERING_MEMBERS == 1 + (1 << 1) + (1 << 2)
        assert ApsRole.ALL_MEMBERS == 1 + (1 << 1) + (1 << 2) + (1 << 3) + (1 << 4)


class TestApsTypes(unittest.TestCase):

    def setUp(self):
        self.destId = "90010000"
        self.srcId = "34010000"
        self.batchNo = "01"
        self.version = "20230410.1681135544"

    def test_header_length(self):

        router = ApsRouter(destinationID=self.destId, sourceID=self.srcId, batchNo=self.batchNo, version=self.version)
        self.assertEqual(router.headerLength,
                         len(self.destId) + len(self.srcId) + len(self.batchNo) + len(self.version) + len("000000"))
        self.assertEqual(router.totalMessageLength, router.headerLength)

    def test_message_length(self):
        router = ApsRouter(destinationID=self.destId, sourceID=self.srcId, batchNo=self.batchNo, version=self.version)
        data = ApsData(router,
                       message={"f1messagetype": F1MessageTypeRecord(MessageType.ACCOUNT_VERIFICATION_REQUEST)},
                       aux=None)
        assert data.router.totalMessageLength == data.router.headerLength + \
            len(MessageType.ACCOUNT_VERIFICATION_REQUEST)


class TestApsTypesMessageType(unittest.TestCase):

    def test_message_type_by_code(self):
        self.assertEqual(MessageType.M0100.value, '0100')
        self.assertEqual(MessageType.M0110.value, '0110')

    def test_message_type_by_value(self):
        # msgSubType is None
        self.assertEqual(MessageType.AUTH_REQUEST.value, '0100')
        self.assertEqual(MessageType.AUTH_RESPONSE.value, '0110')
        self.assertEqual(MessageType.ACCOUNT_VERIFICATION_REQUEST.value, '0100')
        self.assertEqual(MessageType.ACCOUNT_VERIFICATION_RESPONSE.value, '0110')

        # msgSubType is not None
        self.assertNotEqual(MessageType.PRE_AUTH_CANCELATION_REQUEST, '0100')

    def test_message_type_by_display(self):
        logger.debug(MessageType.PRE_AUTH_CANCELATION_RESPONSE.display)
        self.assertEqual(MessageType.PRE_AUTH_CANCELATION_RESPONSE.display, 'PRE_AUTH_CANCELATION_RESPONSE')

    def test_message_type_by_length(self):
        self.assertEqual(len(MessageType.PRE_AUTH_CANCELATION_REQUEST), 4)
        self.assertEqual(len(MessageType.A0620), 4)
        self.assertEqual(len(MessageType.ACCOUNT_VERIFICATION_REQUEST), 4)

    def test_message_type_equalation(self):
        self.assertEqual(MessageType.ACCOUNT_VERIFICATION_REQUEST, MessageType.M0100)
        self.assertNotEqual(MessageType.ACCOUNT_VERIFICATION_REQUEST, MessageType.I0000)
        self.assertNotEqual(MessageType.PRE_AUTH_CANCELATION_REQUEST, MessageType.M0100)
        self.assertNotEqual(MessageType.PRE_AUTH_CANCELATION_REQUEST, MessageType.PRE_AUTH_CANCELATION_RESPONSE)

    def test_show_message_type_repr(self):
        logger.debug(MessageType.PRE_AUTH_CANCELATION_REQUEST)
        logger.debug(MessageType.PRE_AUTH_CANCELATION_RESPONSE.display)
        logger.debug(MessageType.PRE_AUTH_CANCELATION_RESPONSE.value)


if __name__ == "__main__":
    # try:
    #     import xmlrunner  # type: ignore[import]
    #     testRunner = xmlrunner.XMLTestRunner(output='tests/test-reports', verbosity=2)
    # except ImportError:
    #     testRunner = None
    # unittest.main(testRunner=testRunner, verbosity=2)
    unittest.main()
