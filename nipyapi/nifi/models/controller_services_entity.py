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


class ControllerServicesEntity(object):
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
        'current_time': 'str',
        'controller_services': 'list[ControllerServiceEntity]'
    }

    attribute_map = {
        'current_time': 'currentTime',
        'controller_services': 'controllerServices'
    }

    def __init__(self, current_time=None, controller_services=None):
        """
        ControllerServicesEntity - a model defined in Swagger
        """

        self._current_time = None
        self._controller_services = None

        if current_time is not None:
          self.current_time = current_time
        if controller_services is not None:
          self.controller_services = controller_services

    @property
    def current_time(self):
        """
        Gets the current_time of this ControllerServicesEntity.
        The current time on the system.

        :return: The current_time of this ControllerServicesEntity.
        :rtype: str
        """
        return self._current_time

    @current_time.setter
    def current_time(self, current_time):
        """
        Sets the current_time of this ControllerServicesEntity.
        The current time on the system.

        :param current_time: The current_time of this ControllerServicesEntity.
        :type: str
        """

        self._current_time = current_time

    @property
    def controller_services(self):
        """
        Gets the controller_services of this ControllerServicesEntity.

        :return: The controller_services of this ControllerServicesEntity.
        :rtype: list[ControllerServiceEntity]
        """
        return self._controller_services

    @controller_services.setter
    def controller_services(self, controller_services):
        """
        Sets the controller_services of this ControllerServicesEntity.

        :param controller_services: The controller_services of this ControllerServicesEntity.
        :type: list[ControllerServiceEntity]
        """

        self._controller_services = controller_services

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
        if not isinstance(other, ControllerServicesEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
