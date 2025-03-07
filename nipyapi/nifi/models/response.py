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


class Response(object):
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
        'status': 'int',
        'metadata': 'dict(str, list[object])',
        'entity': 'object'
    }

    attribute_map = {
        'status': 'status',
        'metadata': 'metadata',
        'entity': 'entity'
    }

    def __init__(self, status=None, metadata=None, entity=None):
        """
        Response - a model defined in Swagger
        """

        self._status = None
        self._metadata = None
        self._entity = None

        if status is not None:
          self.status = status
        if metadata is not None:
          self.metadata = metadata
        if entity is not None:
          self.entity = entity

    @property
    def status(self):
        """
        Gets the status of this Response.

        :return: The status of this Response.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Response.

        :param status: The status of this Response.
        :type: int
        """

        self._status = status

    @property
    def metadata(self):
        """
        Gets the metadata of this Response.

        :return: The metadata of this Response.
        :rtype: dict(str, list[object])
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Response.

        :param metadata: The metadata of this Response.
        :type: dict(str, list[object])
        """

        self._metadata = metadata

    @property
    def entity(self):
        """
        Gets the entity of this Response.

        :return: The entity of this Response.
        :rtype: object
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """
        Sets the entity of this Response.

        :param entity: The entity of this Response.
        :type: object
        """

        self._entity = entity

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
        if not isinstance(other, Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
