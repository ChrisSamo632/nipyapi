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


class ComponentValidationResultsEntity(object):
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
        'validation_results': 'list[ComponentValidationResultEntity]'
    }

    attribute_map = {
        'validation_results': 'validationResults'
    }

    def __init__(self, validation_results=None):
        """
        ComponentValidationResultsEntity - a model defined in Swagger
        """

        self._validation_results = None

        if validation_results is not None:
          self.validation_results = validation_results

    @property
    def validation_results(self):
        """
        Gets the validation_results of this ComponentValidationResultsEntity.
        A List of ComponentValidationResultEntity, one for each component that is validated

        :return: The validation_results of this ComponentValidationResultsEntity.
        :rtype: list[ComponentValidationResultEntity]
        """
        return self._validation_results

    @validation_results.setter
    def validation_results(self, validation_results):
        """
        Sets the validation_results of this ComponentValidationResultsEntity.
        A List of ComponentValidationResultEntity, one for each component that is validated

        :param validation_results: The validation_results of this ComponentValidationResultsEntity.
        :type: list[ComponentValidationResultEntity]
        """

        self._validation_results = validation_results

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
        if not isinstance(other, ComponentValidationResultsEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
