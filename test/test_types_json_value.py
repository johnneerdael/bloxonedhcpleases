# coding: utf-8

"""
    DHCP Leases API

    The DHCP Leases application is a BloxOne DDI service that stores information about leases. Please note that hosts are authoritative for their lease data. Changes to leases are periodically replicated to the cloud and stored by this service for display purposes. There is no lease history, so only current leases are available. In other words, every dhcp/host_lease or dhcp/lease for that matter, represents a lease that is currently active. Note that fixed addresses do not have leases.   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import bloxonedhcpleases
from bloxonedhcpleases.models.types_json_value import TypesJSONValue  # noqa: E501
from bloxonedhcpleases.rest import ApiException


class TestTypesJSONValue(unittest.TestCase):
    """TypesJSONValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTypesJSONValue(self):
        """Test TypesJSONValue"""
        # FIXME: construct object with mandatory attributes with example values
        # model = bloxonedhcpleases.models.types_json_value.TypesJSONValue()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
