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


class DifferenceDTO(object):
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
        'difference_type': 'str',
        'difference': 'str'
    }

    attribute_map = {
        'difference_type': 'differenceType',
        'difference': 'difference'
    }

    def __init__(self, difference_type=None, difference=None):
        """
        DifferenceDTO - a model defined in Swagger
        """

        self._difference_type = None
        self._difference = None

        if difference_type is not None:
          self.difference_type = difference_type
        if difference is not None:
          self.difference = difference

    @property
    def difference_type(self):
        """
        Gets the difference_type of this DifferenceDTO.
        The type of difference

        :return: The difference_type of this DifferenceDTO.
        :rtype: str
        """
        return self._difference_type

    @difference_type.setter
    def difference_type(self, difference_type):
        """
        Sets the difference_type of this DifferenceDTO.
        The type of difference

        :param difference_type: The difference_type of this DifferenceDTO.
        :type: str
        """

        self._difference_type = difference_type

    @property
    def difference(self):
        """
        Gets the difference of this DifferenceDTO.
        Description of the difference

        :return: The difference of this DifferenceDTO.
        :rtype: str
        """
        return self._difference

    @difference.setter
    def difference(self, difference):
        """
        Sets the difference of this DifferenceDTO.
        Description of the difference

        :param difference: The difference of this DifferenceDTO.
        :type: str
        """

        self._difference = difference

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
        if not isinstance(other, DifferenceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
