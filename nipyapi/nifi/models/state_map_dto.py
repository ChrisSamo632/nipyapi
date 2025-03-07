# coding: utf-8

"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class StateMapDTO(object):
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
        'scope': 'str',
        'total_entry_count': 'int',
        'state': 'list[StateEntryDTO]'
    }

    attribute_map = {
        'scope': 'scope',
        'total_entry_count': 'totalEntryCount',
        'state': 'state'
    }

    def __init__(self, scope=None, total_entry_count=None, state=None):
        """
        StateMapDTO - a model defined in Swagger
        """

        self._scope = None
        self._total_entry_count = None
        self._state = None

        if scope is not None:
          self.scope = scope
        if total_entry_count is not None:
          self.total_entry_count = total_entry_count
        if state is not None:
          self.state = state

    @property
    def scope(self):
        """
        Gets the scope of this StateMapDTO.
        The scope of this StateMap.

        :return: The scope of this StateMapDTO.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this StateMapDTO.
        The scope of this StateMap.

        :param scope: The scope of this StateMapDTO.
        :type: str
        """

        self._scope = scope

    @property
    def total_entry_count(self):
        """
        Gets the total_entry_count of this StateMapDTO.
        The total number of state entries. When the state map is lengthy, only of portion of the entries are returned.

        :return: The total_entry_count of this StateMapDTO.
        :rtype: int
        """
        return self._total_entry_count

    @total_entry_count.setter
    def total_entry_count(self, total_entry_count):
        """
        Sets the total_entry_count of this StateMapDTO.
        The total number of state entries. When the state map is lengthy, only of portion of the entries are returned.

        :param total_entry_count: The total_entry_count of this StateMapDTO.
        :type: int
        """

        self._total_entry_count = total_entry_count

    @property
    def state(self):
        """
        Gets the state of this StateMapDTO.
        The state.

        :return: The state of this StateMapDTO.
        :rtype: list[StateEntryDTO]
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this StateMapDTO.
        The state.

        :param state: The state of this StateMapDTO.
        :type: list[StateEntryDTO]
        """

        self._state = state

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
        if not isinstance(other, StateMapDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
