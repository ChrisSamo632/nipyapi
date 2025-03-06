# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ResourceDefinition(object):
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
        'cardinality': 'str',
        'resource_types': 'list[str]'
    }

    attribute_map = {
        'cardinality': 'cardinality',
        'resource_types': 'resourceTypes'
    }

    def __init__(self, cardinality=None, resource_types=None):
        """
        ResourceDefinition - a model defined in Swagger
        """

        self._cardinality = None
        self._resource_types = None

        if cardinality is not None:
          self.cardinality = cardinality
        if resource_types is not None:
          self.resource_types = resource_types

    @property
    def cardinality(self):
        """
        Gets the cardinality of this ResourceDefinition.
        The cardinality of the resource definition

        :return: The cardinality of this ResourceDefinition.
        :rtype: str
        """
        return self._cardinality

    @cardinality.setter
    def cardinality(self, cardinality):
        """
        Sets the cardinality of this ResourceDefinition.
        The cardinality of the resource definition

        :param cardinality: The cardinality of this ResourceDefinition.
        :type: str
        """
        allowed_values = ["SINGLE", "MULTIPLE"]
        if cardinality not in allowed_values:
            raise ValueError(
                "Invalid value for `cardinality` ({0}), must be one of {1}"
                .format(cardinality, allowed_values)
            )

        self._cardinality = cardinality

    @property
    def resource_types(self):
        """
        Gets the resource_types of this ResourceDefinition.
        The types of resources

        :return: The resource_types of this ResourceDefinition.
        :rtype: list[str]
        """
        return self._resource_types

    @resource_types.setter
    def resource_types(self, resource_types):
        """
        Sets the resource_types of this ResourceDefinition.
        The types of resources

        :param resource_types: The resource_types of this ResourceDefinition.
        :type: list[str]
        """
        allowed_values = ["FILE", "DIRECTORY", "TEXT", "URL"]
        if not set(resource_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `resource_types` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(resource_types)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._resource_types = resource_types

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
        if not isinstance(other, ResourceDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
