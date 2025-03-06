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


class ExtensionRepoVersionSummary(object):
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
        'link': 'JaxbLink',
        'bucket_name': 'str',
        'group_id': 'str',
        'artifact_id': 'str',
        'version': 'str',
        'author': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'link': 'link',
        'bucket_name': 'bucketName',
        'group_id': 'groupId',
        'artifact_id': 'artifactId',
        'version': 'version',
        'author': 'author',
        'timestamp': 'timestamp'
    }

    def __init__(self, link=None, bucket_name=None, group_id=None, artifact_id=None, version=None, author=None, timestamp=None):
        """
        ExtensionRepoVersionSummary - a model defined in Swagger
        """

        self._link = None
        self._bucket_name = None
        self._group_id = None
        self._artifact_id = None
        self._version = None
        self._author = None
        self._timestamp = None

        if link is not None:
          self.link = link
        if bucket_name is not None:
          self.bucket_name = bucket_name
        if group_id is not None:
          self.group_id = group_id
        if artifact_id is not None:
          self.artifact_id = artifact_id
        if version is not None:
          self.version = version
        if author is not None:
          self.author = author
        if timestamp is not None:
          self.timestamp = timestamp

    @property
    def link(self):
        """
        Gets the link of this ExtensionRepoVersionSummary.
        An WebLink to this entity.

        :return: The link of this ExtensionRepoVersionSummary.
        :rtype: JaxbLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """
        Sets the link of this ExtensionRepoVersionSummary.
        An WebLink to this entity.

        :param link: The link of this ExtensionRepoVersionSummary.
        :type: JaxbLink
        """

        self._link = link

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this ExtensionRepoVersionSummary.
        The bucket name

        :return: The bucket_name of this ExtensionRepoVersionSummary.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this ExtensionRepoVersionSummary.
        The bucket name

        :param bucket_name: The bucket_name of this ExtensionRepoVersionSummary.
        :type: str
        """

        self._bucket_name = bucket_name

    @property
    def group_id(self):
        """
        Gets the group_id of this ExtensionRepoVersionSummary.
        The group id

        :return: The group_id of this ExtensionRepoVersionSummary.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this ExtensionRepoVersionSummary.
        The group id

        :param group_id: The group_id of this ExtensionRepoVersionSummary.
        :type: str
        """

        self._group_id = group_id

    @property
    def artifact_id(self):
        """
        Gets the artifact_id of this ExtensionRepoVersionSummary.
        The artifact id

        :return: The artifact_id of this ExtensionRepoVersionSummary.
        :rtype: str
        """
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, artifact_id):
        """
        Sets the artifact_id of this ExtensionRepoVersionSummary.
        The artifact id

        :param artifact_id: The artifact_id of this ExtensionRepoVersionSummary.
        :type: str
        """

        self._artifact_id = artifact_id

    @property
    def version(self):
        """
        Gets the version of this ExtensionRepoVersionSummary.
        The version

        :return: The version of this ExtensionRepoVersionSummary.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ExtensionRepoVersionSummary.
        The version

        :param version: The version of this ExtensionRepoVersionSummary.
        :type: str
        """

        self._version = version

    @property
    def author(self):
        """
        Gets the author of this ExtensionRepoVersionSummary.
        The identity of the user that created this version

        :return: The author of this ExtensionRepoVersionSummary.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this ExtensionRepoVersionSummary.
        The identity of the user that created this version

        :param author: The author of this ExtensionRepoVersionSummary.
        :type: str
        """

        self._author = author

    @property
    def timestamp(self):
        """
        Gets the timestamp of this ExtensionRepoVersionSummary.
        The timestamp of when this version was created

        :return: The timestamp of this ExtensionRepoVersionSummary.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this ExtensionRepoVersionSummary.
        The timestamp of when this version was created

        :param timestamp: The timestamp of this ExtensionRepoVersionSummary.
        :type: int
        """

        self._timestamp = timestamp

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
        if not isinstance(other, ExtensionRepoVersionSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
