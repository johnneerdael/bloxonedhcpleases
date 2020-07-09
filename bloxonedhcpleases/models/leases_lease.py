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


class LeasesLease(object):
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
        'address': 'str',
        'client_id': 'str',
        'ends': 'datetime',
        'fingerprint': 'str',
        'fingerprint_processed': 'str',
        'ha_group': 'str',
        'hardware': 'str',
        'host': 'str',
        'hostname': 'str',
        'last_updated': 'datetime',
        'options': 'str',
        'space': 'str',
        'starts': 'datetime',
        'state': 'str'
    }

    attribute_map = {
        'address': 'address',
        'client_id': 'client_id',
        'ends': 'ends',
        'fingerprint': 'fingerprint',
        'fingerprint_processed': 'fingerprint_processed',
        'ha_group': 'ha_group',
        'hardware': 'hardware',
        'host': 'host',
        'hostname': 'hostname',
        'last_updated': 'last_updated',
        'options': 'options',
        'space': 'space',
        'starts': 'starts',
        'state': 'state'
    }

    def __init__(self, address=None, client_id=None, ends=None, fingerprint=None, fingerprint_processed=None, ha_group=None, hardware=None, host=None, hostname=None, last_updated=None, options=None, space=None, starts=None, state=None):  # noqa: E501
        """LeasesLease - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._client_id = None
        self._ends = None
        self._fingerprint = None
        self._fingerprint_processed = None
        self._ha_group = None
        self._hardware = None
        self._host = None
        self._hostname = None
        self._last_updated = None
        self._options = None
        self._space = None
        self._starts = None
        self._state = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if client_id is not None:
            self.client_id = client_id
        if ends is not None:
            self.ends = ends
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if fingerprint_processed is not None:
            self.fingerprint_processed = fingerprint_processed
        if ha_group is not None:
            self.ha_group = ha_group
        if hardware is not None:
            self.hardware = hardware
        if host is not None:
            self.host = host
        if hostname is not None:
            self.hostname = hostname
        if last_updated is not None:
            self.last_updated = last_updated
        if options is not None:
            self.options = options
        if space is not None:
            self.space = space
        if starts is not None:
            self.starts = starts
        if state is not None:
            self.state = state

    @property
    def address(self):
        """Gets the address of this LeasesLease.  # noqa: E501

        Read-only Field. IP Address in the form \"a.b.c.d\" of the Lease object. This address will be marked as \"leased\" in IPAM while the Lease exists.  # noqa: E501

        :return: The address of this LeasesLease.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this LeasesLease.

        Read-only Field. IP Address in the form \"a.b.c.d\" of the Lease object. This address will be marked as \"leased\" in IPAM while the Lease exists.  # noqa: E501

        :param address: The address of this LeasesLease.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def client_id(self):
        """Gets the client_id of this LeasesLease.  # noqa: E501

        Read-only Field. Client ID. It might be empty.  # noqa: E501

        :return: The client_id of this LeasesLease.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this LeasesLease.

        Read-only Field. Client ID. It might be empty.  # noqa: E501

        :param client_id: The client_id of this LeasesLease.  # noqa: E501
        :type: str
        """

        self._client_id = client_id

    @property
    def ends(self):
        """Gets the ends of this LeasesLease.  # noqa: E501

        Read-only Field. Time when the Lease will expire.  # noqa: E501

        :return: The ends of this LeasesLease.  # noqa: E501
        :rtype: datetime
        """
        return self._ends

    @ends.setter
    def ends(self, ends):
        """Sets the ends of this LeasesLease.

        Read-only Field. Time when the Lease will expire.  # noqa: E501

        :param ends: The ends of this LeasesLease.  # noqa: E501
        :type: datetime
        """

        self._ends = ends

    @property
    def fingerprint(self):
        """Gets the fingerprint of this LeasesLease.  # noqa: E501

        Read-only Field. String of a fingerprint.  # noqa: E501

        :return: The fingerprint of this LeasesLease.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this LeasesLease.

        Read-only Field. String of a fingerprint.  # noqa: E501

        :param fingerprint: The fingerprint of this LeasesLease.  # noqa: E501
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def fingerprint_processed(self):
        """Gets the fingerprint_processed of this LeasesLease.  # noqa: E501

        The field indicates if this lease has been fingerprinted yet.  # noqa: E501

        :return: The fingerprint_processed of this LeasesLease.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint_processed

    @fingerprint_processed.setter
    def fingerprint_processed(self, fingerprint_processed):
        """Sets the fingerprint_processed of this LeasesLease.

        The field indicates if this lease has been fingerprinted yet.  # noqa: E501

        :param fingerprint_processed: The fingerprint_processed of this LeasesLease.  # noqa: E501
        :type: str
        """

        self._fingerprint_processed = fingerprint_processed

    @property
    def ha_group(self):
        """Gets the ha_group of this LeasesLease.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The ha_group of this LeasesLease.  # noqa: E501
        :rtype: str
        """
        return self._ha_group

    @ha_group.setter
    def ha_group(self, ha_group):
        """Sets the ha_group of this LeasesLease.

        The resource identifier.  # noqa: E501

        :param ha_group: The ha_group of this LeasesLease.  # noqa: E501
        :type: str
        """

        self._ha_group = ha_group

    @property
    def hardware(self):
        """Gets the hardware of this LeasesLease.  # noqa: E501

        Read-only Field. Hardware Address. It consists of six groups of two hex digits in lower-case separated by colons, e.g. \"aa:bb:cc:dd:ee:ff\".  # noqa: E501

        :return: The hardware of this LeasesLease.  # noqa: E501
        :rtype: str
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this LeasesLease.

        Read-only Field. Hardware Address. It consists of six groups of two hex digits in lower-case separated by colons, e.g. \"aa:bb:cc:dd:ee:ff\".  # noqa: E501

        :param hardware: The hardware of this LeasesLease.  # noqa: E501
        :type: str
        """

        self._hardware = hardware

    @property
    def host(self):
        """Gets the host of this LeasesLease.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The host of this LeasesLease.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this LeasesLease.

        The resource identifier.  # noqa: E501

        :param host: The host of this LeasesLease.  # noqa: E501
        :type: str
        """

        self._host = host

    @property
    def hostname(self):
        """Gets the hostname of this LeasesLease.  # noqa: E501

        Read-only Field. Client Hostname. It is a fully qualified domain name, consisting of a series of labels separated by dots, e.g. \"www.infoblox.com\". It might be empty.  # noqa: E501

        :return: The hostname of this LeasesLease.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this LeasesLease.

        Read-only Field. Client Hostname. It is a fully qualified domain name, consisting of a series of labels separated by dots, e.g. \"www.infoblox.com\". It might be empty.  # noqa: E501

        :param hostname: The hostname of this LeasesLease.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def last_updated(self):
        """Gets the last_updated of this LeasesLease.  # noqa: E501

        Read-only Field. Time when the Lease was last updated.  # noqa: E501

        :return: The last_updated of this LeasesLease.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this LeasesLease.

        Read-only Field. Time when the Lease was last updated.  # noqa: E501

        :param last_updated: The last_updated of this LeasesLease.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def options(self):
        """Gets the options of this LeasesLease.  # noqa: E501

        Read-only data. DHCP options in JSON format.  # noqa: E501

        :return: The options of this LeasesLease.  # noqa: E501
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this LeasesLease.

        Read-only data. DHCP options in JSON format.  # noqa: E501

        :param options: The options of this LeasesLease.  # noqa: E501
        :type: str
        """

        self._options = options

    @property
    def space(self):
        """Gets the space of this LeasesLease.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The space of this LeasesLease.  # noqa: E501
        :rtype: str
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this LeasesLease.

        The resource identifier.  # noqa: E501

        :param space: The space of this LeasesLease.  # noqa: E501
        :type: str
        """

        self._space = space

    @property
    def starts(self):
        """Gets the starts of this LeasesLease.  # noqa: E501

        Read-only Field. Time when the Lease was issued.  # noqa: E501

        :return: The starts of this LeasesLease.  # noqa: E501
        :rtype: datetime
        """
        return self._starts

    @starts.setter
    def starts(self, starts):
        """Sets the starts of this LeasesLease.

        Read-only Field. Time when the Lease was issued.  # noqa: E501

        :param starts: The starts of this LeasesLease.  # noqa: E501
        :type: datetime
        """

        self._starts = starts

    @property
    def state(self):
        """Gets the state of this LeasesLease.  # noqa: E501

        Read-only Field. The state of the lease and its value could be \"used\" or \"abandoned\". Leases with a state of deleted are not returned to queries, they are for internal use.  # noqa: E501

        :return: The state of this LeasesLease.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this LeasesLease.

        Read-only Field. The state of the lease and its value could be \"used\" or \"abandoned\". Leases with a state of deleted are not returned to queries, they are for internal use.  # noqa: E501

        :param state: The state of this LeasesLease.  # noqa: E501
        :type: str
        """

        self._state = state

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
        if issubclass(LeasesLease, dict):
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
        if not isinstance(other, LeasesLease):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
