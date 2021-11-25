# coding: utf-8

"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.15.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PeerDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'hostname': 'str',
        'port': 'int',
        'secure': 'bool',
        'flow_file_count': 'int'
    }

    attribute_map = {
        'hostname': 'hostname',
        'port': 'port',
        'secure': 'secure',
        'flow_file_count': 'flowFileCount'
    }

    def __init__(self, hostname=None, port=None, secure=None, flow_file_count=None):
        """
        PeerDTO - a model defined in Swagger
        """

        self._hostname = None
        self._port = None
        self._secure = None
        self._flow_file_count = None

        if hostname is not None:
          self.hostname = hostname
        if port is not None:
          self.port = port
        if secure is not None:
          self.secure = secure
        if flow_file_count is not None:
          self.flow_file_count = flow_file_count

    @property
    def hostname(self):
        """
        Gets the hostname of this PeerDTO.
        The hostname of this peer.

        :return: The hostname of this PeerDTO.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this PeerDTO.
        The hostname of this peer.

        :param hostname: The hostname of this PeerDTO.
        :type: str
        """

        self._hostname = hostname

    @property
    def port(self):
        """
        Gets the port of this PeerDTO.
        The port number of this peer.

        :return: The port of this PeerDTO.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this PeerDTO.
        The port number of this peer.

        :param port: The port of this PeerDTO.
        :type: int
        """

        self._port = port

    @property
    def secure(self):
        """
        Gets the secure of this PeerDTO.
        Returns if this peer connection is secure.

        :return: The secure of this PeerDTO.
        :rtype: bool
        """
        return self._secure

    @secure.setter
    def secure(self, secure):
        """
        Sets the secure of this PeerDTO.
        Returns if this peer connection is secure.

        :param secure: The secure of this PeerDTO.
        :type: bool
        """

        self._secure = secure

    @property
    def flow_file_count(self):
        """
        Gets the flow_file_count of this PeerDTO.
        The number of flowFiles this peer holds.

        :return: The flow_file_count of this PeerDTO.
        :rtype: int
        """
        return self._flow_file_count

    @flow_file_count.setter
    def flow_file_count(self, flow_file_count):
        """
        Sets the flow_file_count of this PeerDTO.
        The number of flowFiles this peer holds.

        :param flow_file_count: The flow_file_count of this PeerDTO.
        :type: int
        """

        self._flow_file_count = flow_file_count

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PeerDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
