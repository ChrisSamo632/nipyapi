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


class TenantsEntity(object):
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
        'users': 'list[TenantEntity]',
        'user_groups': 'list[TenantEntity]'
    }

    attribute_map = {
        'users': 'users',
        'user_groups': 'userGroups'
    }

    def __init__(self, users=None, user_groups=None):
        """
        TenantsEntity - a model defined in Swagger
        """

        self._users = None
        self._user_groups = None

        if users is not None:
          self.users = users
        if user_groups is not None:
          self.user_groups = user_groups

    @property
    def users(self):
        """
        Gets the users of this TenantsEntity.

        :return: The users of this TenantsEntity.
        :rtype: list[TenantEntity]
        """
        return self._users

    @users.setter
    def users(self, users):
        """
        Sets the users of this TenantsEntity.

        :param users: The users of this TenantsEntity.
        :type: list[TenantEntity]
        """

        self._users = users

    @property
    def user_groups(self):
        """
        Gets the user_groups of this TenantsEntity.

        :return: The user_groups of this TenantsEntity.
        :rtype: list[TenantEntity]
        """
        return self._user_groups

    @user_groups.setter
    def user_groups(self, user_groups):
        """
        Sets the user_groups of this TenantsEntity.

        :param user_groups: The user_groups of this TenantsEntity.
        :type: list[TenantEntity]
        """

        self._user_groups = user_groups

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
        if not isinstance(other, TenantsEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
