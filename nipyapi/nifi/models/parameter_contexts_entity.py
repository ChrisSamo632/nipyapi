"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class ParameterContextsEntity(object):
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
        'parameter_contexts': 'list[ParameterContextEntity]',
        'current_time': 'str'
    }

    attribute_map = {
        'parameter_contexts': 'parameterContexts',
        'current_time': 'currentTime'
    }

    def __init__(self, parameter_contexts=None, current_time=None):
        """
        ParameterContextsEntity - a model defined in Swagger
        """

        self._parameter_contexts = None
        self._current_time = None

        if parameter_contexts is not None:
          self.parameter_contexts = parameter_contexts
        if current_time is not None:
          self.current_time = current_time

    @property
    def parameter_contexts(self):
        """
        Gets the parameter_contexts of this ParameterContextsEntity.
        The Parameter Contexts

        :return: The parameter_contexts of this ParameterContextsEntity.
        :rtype: list[ParameterContextEntity]
        """
        return self._parameter_contexts

    @parameter_contexts.setter
    def parameter_contexts(self, parameter_contexts):
        """
        Sets the parameter_contexts of this ParameterContextsEntity.
        The Parameter Contexts

        :param parameter_contexts: The parameter_contexts of this ParameterContextsEntity.
        :type: list[ParameterContextEntity]
        """

        self._parameter_contexts = parameter_contexts

    @property
    def current_time(self):
        """
        Gets the current_time of this ParameterContextsEntity.
        The current time on the system.

        :return: The current_time of this ParameterContextsEntity.
        :rtype: str
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        """
        Sets the current_time of this ParameterContextsEntity.
        The current time on the system.

        :param current_time: The current_time of this ParameterContextsEntity.
        :type: str
        """

        self._current_time = current_time

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in self.swagger_types.items():
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
        if not isinstance(other, ParameterContextsEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
