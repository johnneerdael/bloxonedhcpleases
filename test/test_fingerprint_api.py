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
from bloxonedhcpleases.api.fingerprint_api import FingerprintApi  # noqa: E501
from bloxonedhcpleases.rest import ApiException


class TestFingerprintApi(unittest.TestCase):
    """FingerprintApi unit test stubs"""

    def setUp(self):
        self.api = bloxonedhcpleases.api.fingerprint_api.FingerprintApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_fingerprint_create(self):
        """Test case for fingerprint_create

        Create Fingerprint object.  # noqa: E501
        """
        pass

    def test_fingerprint_delete(self):
        """Test case for fingerprint_delete

        Delete the Fingerprint object.  # noqa: E501
        """
        pass

    def test_fingerprint_list(self):
        """Test case for fingerprint_list

        List Fingerprint objects.  # noqa: E501
        """
        pass

    def test_fingerprint_read(self):
        """Test case for fingerprint_read

        Read the Fingerprint object.  # noqa: E501
        """
        pass

    def test_fingerprint_update(self):
        """Test case for fingerprint_update

        Update the Fingerprint object.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
