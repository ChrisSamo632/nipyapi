"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class RepositoryUsageDTO(object):
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
        'file_store_hash': 'str',
        'free_space': 'str',
        'total_space': 'str',
        'free_space_bytes': 'int',
        'total_space_bytes': 'int',
        'utilization': 'str'
    }

    attribute_map = {
        'name': 'name',
        'file_store_hash': 'fileStoreHash',
        'free_space': 'freeSpace',
        'total_space': 'totalSpace',
        'free_space_bytes': 'freeSpaceBytes',
        'total_space_bytes': 'totalSpaceBytes',
        'utilization': 'utilization'
    }

    def __init__(self, name=None, file_store_hash=None, free_space=None, total_space=None, free_space_bytes=None, total_space_bytes=None, utilization=None):
        """
        RepositoryUsageDTO - a model defined in Swagger
        """

        self._name = None
        self._file_store_hash = None
        self._free_space = None
        self._total_space = None
        self._free_space_bytes = None
        self._total_space_bytes = None
        self._utilization = None

        if name is not None:
          self.name = name
        if file_store_hash is not None:
          self.file_store_hash = file_store_hash
        if free_space is not None:
          self.free_space = free_space
        if total_space is not None:
          self.total_space = total_space
        if free_space_bytes is not None:
          self.free_space_bytes = free_space_bytes
        if total_space_bytes is not None:
          self.total_space_bytes = total_space_bytes
        if utilization is not None:
          self.utilization = utilization

    @property
    def name(self):
        """
        Gets the name of this RepositoryUsageDTO.
        The name of the repository

        :return: The name of this RepositoryUsageDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RepositoryUsageDTO.
        The name of the repository

        :param name: The name of this RepositoryUsageDTO.
        :type: str
        """

        self._name = name

    @property
    def file_store_hash(self):
        """
        Gets the file_store_hash of this RepositoryUsageDTO.
        A SHA-256 hash of the File Store name/path that is used to store the repository's data. This information is exposed as a hash in order to avoid exposing potentially sensitive information that is not generally relevant. What is typically relevant is whether or not multiple repositories on the same node are using the same File Store, as this indicates that the repositories are competing for the resources of the backing disk/storage mechanism.

        :return: The file_store_hash of this RepositoryUsageDTO.
        :rtype: str
        """
        return self._file_store_hash

    @file_store_hash.setter
    def file_store_hash(self, file_store_hash):
        """
        Sets the file_store_hash of this RepositoryUsageDTO.
        A SHA-256 hash of the File Store name/path that is used to store the repository's data. This information is exposed as a hash in order to avoid exposing potentially sensitive information that is not generally relevant. What is typically relevant is whether or not multiple repositories on the same node are using the same File Store, as this indicates that the repositories are competing for the resources of the backing disk/storage mechanism.

        :param file_store_hash: The file_store_hash of this RepositoryUsageDTO.
        :type: str
        """

        self._file_store_hash = file_store_hash

    @property
    def free_space(self):
        """
        Gets the free_space of this RepositoryUsageDTO.
        Amount of free space.

        :return: The free_space of this RepositoryUsageDTO.
        :rtype: str
        """
        return self._free_space

    @free_space.setter
    def free_space(self, free_space):
        """
        Sets the free_space of this RepositoryUsageDTO.
        Amount of free space.

        :param free_space: The free_space of this RepositoryUsageDTO.
        :type: str
        """

        self._free_space = free_space

    @property
    def total_space(self):
        """
        Gets the total_space of this RepositoryUsageDTO.
        Amount of total space.

        :return: The total_space of this RepositoryUsageDTO.
        :rtype: str
        """
        return self._total_space

    @total_space.setter
    def total_space(self, total_space):
        """
        Sets the total_space of this RepositoryUsageDTO.
        Amount of total space.

        :param total_space: The total_space of this RepositoryUsageDTO.
        :type: str
        """

        self._total_space = total_space

    @property
    def free_space_bytes(self):
        """
        Gets the free_space_bytes of this RepositoryUsageDTO.
        The number of bytes of free space.

        :return: The free_space_bytes of this RepositoryUsageDTO.
        :rtype: int
        """
        return self._free_space_bytes

    @free_space_bytes.setter
    def free_space_bytes(self, free_space_bytes):
        """
        Sets the free_space_bytes of this RepositoryUsageDTO.
        The number of bytes of free space.

        :param free_space_bytes: The free_space_bytes of this RepositoryUsageDTO.
        :type: int
        """

        self._free_space_bytes = free_space_bytes

    @property
    def total_space_bytes(self):
        """
        Gets the total_space_bytes of this RepositoryUsageDTO.
        The number of bytes of total space.

        :return: The total_space_bytes of this RepositoryUsageDTO.
        :rtype: int
        """
        return self._total_space_bytes

    @total_space_bytes.setter
    def total_space_bytes(self, total_space_bytes):
        """
        Sets the total_space_bytes of this RepositoryUsageDTO.
        The number of bytes of total space.

        :param total_space_bytes: The total_space_bytes of this RepositoryUsageDTO.
        :type: int
        """

        self._total_space_bytes = total_space_bytes

    @property
    def utilization(self):
        """
        Gets the utilization of this RepositoryUsageDTO.
        Utilization of this storage location.

        :return: The utilization of this RepositoryUsageDTO.
        :rtype: str
        """
        return self._utilization

    @utilization.setter
    def utilization(self, utilization):
        """
        Sets the utilization of this RepositoryUsageDTO.
        Utilization of this storage location.

        :param utilization: The utilization of this RepositoryUsageDTO.
        :type: str
        """

        self._utilization = utilization

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
        if not isinstance(other, RepositoryUsageDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
