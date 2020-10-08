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


class ControllerBulletinsEntity(object):
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
        'bulletins': 'list[BulletinEntity]',
        'controller_service_bulletins': 'list[BulletinEntity]',
        'reporting_task_bulletins': 'list[BulletinEntity]'
    }

    attribute_map = {
        'bulletins': 'bulletins',
        'controller_service_bulletins': 'controllerServiceBulletins',
        'reporting_task_bulletins': 'reportingTaskBulletins'
    }

    def __init__(self, bulletins=None, controller_service_bulletins=None, reporting_task_bulletins=None):
        """
        ControllerBulletinsEntity - a model defined in Swagger
        """

        self._bulletins = None
        self._controller_service_bulletins = None
        self._reporting_task_bulletins = None

        if bulletins is not None:
          self.bulletins = bulletins
        if controller_service_bulletins is not None:
          self.controller_service_bulletins = controller_service_bulletins
        if reporting_task_bulletins is not None:
          self.reporting_task_bulletins = reporting_task_bulletins

    @property
    def bulletins(self):
        """
        Gets the bulletins of this ControllerBulletinsEntity.
        System level bulletins to be reported to the user.

        :return: The bulletins of this ControllerBulletinsEntity.
        :rtype: list[BulletinEntity]
        """
        return self._bulletins

    @bulletins.setter
    def bulletins(self, bulletins):
        """
        Sets the bulletins of this ControllerBulletinsEntity.
        System level bulletins to be reported to the user.

        :param bulletins: The bulletins of this ControllerBulletinsEntity.
        :type: list[BulletinEntity]
        """

        self._bulletins = bulletins

    @property
    def controller_service_bulletins(self):
        """
        Gets the controller_service_bulletins of this ControllerBulletinsEntity.
        Controller service bulletins to be reported to the user.

        :return: The controller_service_bulletins of this ControllerBulletinsEntity.
        :rtype: list[BulletinEntity]
        """
        return self._controller_service_bulletins

    @controller_service_bulletins.setter
    def controller_service_bulletins(self, controller_service_bulletins):
        """
        Sets the controller_service_bulletins of this ControllerBulletinsEntity.
        Controller service bulletins to be reported to the user.

        :param controller_service_bulletins: The controller_service_bulletins of this ControllerBulletinsEntity.
        :type: list[BulletinEntity]
        """

        self._controller_service_bulletins = controller_service_bulletins

    @property
    def reporting_task_bulletins(self):
        """
        Gets the reporting_task_bulletins of this ControllerBulletinsEntity.
        Reporting task bulletins to be reported to the user.

        :return: The reporting_task_bulletins of this ControllerBulletinsEntity.
        :rtype: list[BulletinEntity]
        """
        return self._reporting_task_bulletins

    @reporting_task_bulletins.setter
    def reporting_task_bulletins(self, reporting_task_bulletins):
        """
        Sets the reporting_task_bulletins of this ControllerBulletinsEntity.
        Reporting task bulletins to be reported to the user.

        :param reporting_task_bulletins: The reporting_task_bulletins of this ControllerBulletinsEntity.
        :type: list[BulletinEntity]
        """

        self._reporting_task_bulletins = reporting_task_bulletins

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
        if not isinstance(other, ControllerBulletinsEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
