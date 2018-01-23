# coding: utf-8

"""
    NiFi Registry REST API

    The Rest Api provides an interface to a registry with operations for saving,                                             versioning, reading NiFi flows                                             and components.

    OpenAPI spec version: 0.1.1-SNAPSHOT
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Bucket(object):
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
        'link': 'Link',
        'identifier': 'str',
        'name': 'str',
        'created_timestamp': 'int',
        'description': 'str',
        'permissions': 'Permissions'
    }

    attribute_map = {
        'link': 'link',
        'identifier': 'identifier',
        'name': 'name',
        'created_timestamp': 'createdTimestamp',
        'description': 'description',
        'permissions': 'permissions'
    }

    def __init__(self, link=None, identifier=None, name=None, created_timestamp=None, description=None, permissions=None):
        """
        Bucket - a model defined in Swagger
        """

        self._link = None
        self._identifier = None
        self._name = None
        self._created_timestamp = None
        self._description = None
        self._permissions = None

        if link is not None:
          self.link = link
        if identifier is not None:
          self.identifier = identifier
        if name is not None:
          self.name = name
        if created_timestamp is not None:
          self.created_timestamp = created_timestamp
        if description is not None:
          self.description = description
        if permissions is not None:
          self.permissions = permissions

    @property
    def link(self):
        """
        Gets the link of this Bucket.
        An WebLink to this entity.

        :return: The link of this Bucket.
        :rtype: Link
        """
        return self._link

    @link.setter
    def link(self, link):
        """
        Sets the link of this Bucket.
        An WebLink to this entity.

        :param link: The link of this Bucket.
        :type: Link
        """

        self._link = link

    @property
    def identifier(self):
        """
        Gets the identifier of this Bucket.
        An ID to uniquely identify this object.

        :return: The identifier of this Bucket.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this Bucket.
        An ID to uniquely identify this object.

        :param identifier: The identifier of this Bucket.
        :type: str
        """

        self._identifier = identifier

    @property
    def name(self):
        """
        Gets the name of this Bucket.
        The name of the bucket.

        :return: The name of this Bucket.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Bucket.
        The name of the bucket.

        :param name: The name of this Bucket.
        :type: str
        """

        self._name = name

    @property
    def created_timestamp(self):
        """
        Gets the created_timestamp of this Bucket.
        The timestamp of when the bucket was first created. This is set by the server at creation time.

        :return: The created_timestamp of this Bucket.
        :rtype: int
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp):
        """
        Sets the created_timestamp of this Bucket.
        The timestamp of when the bucket was first created. This is set by the server at creation time.

        :param created_timestamp: The created_timestamp of this Bucket.
        :type: int
        """
        if created_timestamp is not None and created_timestamp < 1:
            raise ValueError("Invalid value for `created_timestamp`, must be a value greater than or equal to `1`")

        self._created_timestamp = created_timestamp

    @property
    def description(self):
        """
        Gets the description of this Bucket.
        A description of the bucket.

        :return: The description of this Bucket.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Bucket.
        A description of the bucket.

        :param description: The description of this Bucket.
        :type: str
        """

        self._description = description

    @property
    def permissions(self):
        """
        Gets the permissions of this Bucket.
        The access that the current user has to this bucket.

        :return: The permissions of this Bucket.
        :rtype: Permissions
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this Bucket.
        The access that the current user has to this bucket.

        :param permissions: The permissions of this Bucket.
        :type: Permissions
        """

        self._permissions = permissions

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
        if not isinstance(other, Bucket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
