# coding: utf-8

"""
    DHCP Leases API

    The DHCP Leases application is a BloxOne DDI service that stores information about leases. Please note that hosts are authoritative for their lease data. Changes to leases are periodically replicated to the cloud and stored by this service for display purposes. There is no lease history, so only current leases are available. In other words, every dhcp/host_lease or dhcp/lease for that matter, represents a lease that is currently active. Note that fixed addresses do not have leases.   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LeasesFingerprintRule(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'prefix': 'str',
        'prl': 'list[str]',
        'vendor': 'str',
        'vendor_compare': 'str'
    }

    attribute_map = {
        'prefix': 'prefix',
        'prl': 'prl',
        'vendor': 'vendor',
        'vendor_compare': 'vendor_compare'
    }

    def __init__(self, prefix=None, prl=None, vendor=None, vendor_compare=None):  # noqa: E501
        """LeasesFingerprintRule - a model defined in Swagger"""  # noqa: E501

        self._prefix = None
        self._prl = None
        self._vendor = None
        self._vendor_compare = None
        self.discriminator = None

        if prefix is not None:
            self.prefix = prefix
        if prl is not None:
            self.prl = prl
        if vendor is not None:
            self.vendor = vendor
        if vendor_compare is not None:
            self.vendor_compare = vendor_compare

    @property
    def prefix(self):
        """Gets the prefix of this LeasesFingerprintRule.  # noqa: E501

        The value to use to match the first three bytes of the hardware address.  # noqa: E501

        :return: The prefix of this LeasesFingerprintRule.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this LeasesFingerprintRule.

        The value to use to match the first three bytes of the hardware address.  # noqa: E501

        :param prefix: The prefix of this LeasesFingerprintRule.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def prl(self):
        """Gets the prl of this LeasesFingerprintRule.  # noqa: E501

        The value to use to match the parameter request list option (option 55).  # noqa: E501

        :return: The prl of this LeasesFingerprintRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._prl

    @prl.setter
    def prl(self, prl):
        """Sets the prl of this LeasesFingerprintRule.

        The value to use to match the parameter request list option (option 55).  # noqa: E501

        :param prl: The prl of this LeasesFingerprintRule.  # noqa: E501
        :type: list[str]
        """

        self._prl = prl

    @property
    def vendor(self):
        """Gets the vendor of this LeasesFingerprintRule.  # noqa: E501


        :return: The vendor of this LeasesFingerprintRule.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this LeasesFingerprintRule.


        :param vendor: The vendor of this LeasesFingerprintRule.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def vendor_compare(self):
        """Gets the vendor_compare of this LeasesFingerprintRule.  # noqa: E501

        The operation to use when matching the vendor class ID.  One of the following values {equals, not_equals}, defaults to \"equals\".  # noqa: E501

        :return: The vendor_compare of this LeasesFingerprintRule.  # noqa: E501
        :rtype: str
        """
        return self._vendor_compare

    @vendor_compare.setter
    def vendor_compare(self, vendor_compare):
        """Sets the vendor_compare of this LeasesFingerprintRule.

        The operation to use when matching the vendor class ID.  One of the following values {equals, not_equals}, defaults to \"equals\".  # noqa: E501

        :param vendor_compare: The vendor_compare of this LeasesFingerprintRule.  # noqa: E501
        :type: str
        """

        self._vendor_compare = vendor_compare

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(LeasesFingerprintRule, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LeasesFingerprintRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
