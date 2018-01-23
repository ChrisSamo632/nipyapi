# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.5.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ControllerConfigurationEntity(object):
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
        'revision': 'RevisionDTO',
        'permissions': 'PermissionsDTO',
        'component': 'ControllerConfigurationDTO'
    }

    attribute_map = {
        'revision': 'revision',
        'permissions': 'permissions',
        'component': 'component'
    }

    def __init__(self, revision=None, permissions=None, component=None):
        """
        ControllerConfigurationEntity - a model defined in Swagger
        """

        self._revision = None
        self._permissions = None
        self._component = None

        if revision is not None:
          self.revision = revision
        if permissions is not None:
          self.permissions = permissions
        if component is not None:
          self.component = component

    @property
    def revision(self):
        """
        Gets the revision of this ControllerConfigurationEntity.
        The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses.

        :return: The revision of this ControllerConfigurationEntity.
        :rtype: RevisionDTO
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this ControllerConfigurationEntity.
        The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses.

        :param revision: The revision of this ControllerConfigurationEntity.
        :type: RevisionDTO
        """

        self._revision = revision

    @property
    def permissions(self):
        """
        Gets the permissions of this ControllerConfigurationEntity.
        The permissions for this component.

        :return: The permissions of this ControllerConfigurationEntity.
        :rtype: PermissionsDTO
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this ControllerConfigurationEntity.
        The permissions for this component.

        :param permissions: The permissions of this ControllerConfigurationEntity.
        :type: PermissionsDTO
        """

        self._permissions = permissions

    @property
    def component(self):
        """
        Gets the component of this ControllerConfigurationEntity.
        The controller configuration.

        :return: The component of this ControllerConfigurationEntity.
        :rtype: ControllerConfigurationDTO
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this ControllerConfigurationEntity.
        The controller configuration.

        :param component: The component of this ControllerConfigurationEntity.
        :type: ControllerConfigurationDTO
        """

        self._component = component

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
        if not isinstance(other, ControllerConfigurationEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
