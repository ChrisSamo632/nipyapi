# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.12.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ParameterDTO(object):
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
        'name': 'str',
        'description': 'str',
        'sensitive': 'bool',
        'value': 'str',
        'referencing_components': 'list[AffectedComponentEntity]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'sensitive': 'sensitive',
        'value': 'value',
        'referencing_components': 'referencingComponents'
    }

    def __init__(self, name=None, description=None, sensitive=None, value=None, referencing_components=None):
        """
        ParameterDTO - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._sensitive = None
        self._value = None
        self._referencing_components = None

        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if sensitive is not None:
          self.sensitive = sensitive
        if value is not None:
          self.value = value
        if referencing_components is not None:
          self.referencing_components = referencing_components

    @property
    def name(self):
        """
        Gets the name of this ParameterDTO.
        The name of the Parameter

        :return: The name of this ParameterDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ParameterDTO.
        The name of the Parameter

        :param name: The name of this ParameterDTO.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ParameterDTO.
        The description of the Parameter

        :return: The description of this ParameterDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ParameterDTO.
        The description of the Parameter

        :param description: The description of this ParameterDTO.
        :type: str
        """

        self._description = description

    @property
    def sensitive(self):
        """
        Gets the sensitive of this ParameterDTO.
        Whether or not the Parameter is sensitive

        :return: The sensitive of this ParameterDTO.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """
        Sets the sensitive of this ParameterDTO.
        Whether or not the Parameter is sensitive

        :param sensitive: The sensitive of this ParameterDTO.
        :type: bool
        """

        self._sensitive = sensitive

    @property
    def value(self):
        """
        Gets the value of this ParameterDTO.
        The value of the Parameter

        :return: The value of this ParameterDTO.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this ParameterDTO.
        The value of the Parameter

        :param value: The value of this ParameterDTO.
        :type: str
        """

        self._value = value

    @property
    def referencing_components(self):
        """
        Gets the referencing_components of this ParameterDTO.
        The set of all components in the flow that are referencing this Parameter

        :return: The referencing_components of this ParameterDTO.
        :rtype: list[AffectedComponentEntity]
        """
        return self._referencing_components

    @referencing_components.setter
    def referencing_components(self, referencing_components):
        """
        Sets the referencing_components of this ParameterDTO.
        The set of all components in the flow that are referencing this Parameter

        :param referencing_components: The referencing_components of this ParameterDTO.
        :type: list[AffectedComponentEntity]
        """

        self._referencing_components = referencing_components

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
        if not isinstance(other, ParameterDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
