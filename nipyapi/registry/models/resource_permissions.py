"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class ResourcePermissions(object):
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
        'buckets': 'Permissions',
        'tenants': 'Permissions',
        'policies': 'Permissions',
        'proxy': 'Permissions',
        'any_top_level_resource': 'Permissions'
    }

    attribute_map = {
        'buckets': 'buckets',
        'tenants': 'tenants',
        'policies': 'policies',
        'proxy': 'proxy',
        'any_top_level_resource': 'anyTopLevelResource'
    }

    def __init__(self, buckets=None, tenants=None, policies=None, proxy=None, any_top_level_resource=None):
        """
        ResourcePermissions - a model defined in Swagger
        """

        self._buckets = None
        self._tenants = None
        self._policies = None
        self._proxy = None
        self._any_top_level_resource = None

        if buckets is not None:
          self.buckets = buckets
        if tenants is not None:
          self.tenants = tenants
        if policies is not None:
          self.policies = policies
        if proxy is not None:
          self.proxy = proxy
        if any_top_level_resource is not None:
          self.any_top_level_resource = any_top_level_resource

    @property
    def buckets(self):
        """
        Gets the buckets of this ResourcePermissions.
        The access that the current user has to the top level /buckets resource of this NiFi Registry (i.e., access to all buckets)

        :return: The buckets of this ResourcePermissions.
        :rtype: Permissions
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """
        Sets the buckets of this ResourcePermissions.
        The access that the current user has to the top level /buckets resource of this NiFi Registry (i.e., access to all buckets)

        :param buckets: The buckets of this ResourcePermissions.
        :type: Permissions
        """

        self._buckets = buckets

    @property
    def tenants(self):
        """
        Gets the tenants of this ResourcePermissions.
        The access that the current user has to the top level /tenants resource of this NiFi Registry

        :return: The tenants of this ResourcePermissions.
        :rtype: Permissions
        """
        return self._tenants

    @tenants.setter
    def tenants(self, tenants):
        """
        Sets the tenants of this ResourcePermissions.
        The access that the current user has to the top level /tenants resource of this NiFi Registry

        :param tenants: The tenants of this ResourcePermissions.
        :type: Permissions
        """

        self._tenants = tenants

    @property
    def policies(self):
        """
        Gets the policies of this ResourcePermissions.
        The access that the current user has to the top level /policies resource of this NiFi Registry

        :return: The policies of this ResourcePermissions.
        :rtype: Permissions
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """
        Sets the policies of this ResourcePermissions.
        The access that the current user has to the top level /policies resource of this NiFi Registry

        :param policies: The policies of this ResourcePermissions.
        :type: Permissions
        """

        self._policies = policies

    @property
    def proxy(self):
        """
        Gets the proxy of this ResourcePermissions.
        The access that the current user has to the top level /proxy resource of this NiFi Registry

        :return: The proxy of this ResourcePermissions.
        :rtype: Permissions
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """
        Sets the proxy of this ResourcePermissions.
        The access that the current user has to the top level /proxy resource of this NiFi Registry

        :param proxy: The proxy of this ResourcePermissions.
        :type: Permissions
        """

        self._proxy = proxy

    @property
    def any_top_level_resource(self):
        """
        Gets the any_top_level_resource of this ResourcePermissions.
        The access that the current user has to any top level resources (a logical 'OR' of all other values)

        :return: The any_top_level_resource of this ResourcePermissions.
        :rtype: Permissions
        """
        return self._any_top_level_resource

    @any_top_level_resource.setter
    def any_top_level_resource(self, any_top_level_resource):
        """
        Sets the any_top_level_resource of this ResourcePermissions.
        The access that the current user has to any top level resources (a logical 'OR' of all other values)

        :param any_top_level_resource: The any_top_level_resource of this ResourcePermissions.
        :type: Permissions
        """

        self._any_top_level_resource = any_top_level_resource

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
        if not isinstance(other, ResourcePermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
