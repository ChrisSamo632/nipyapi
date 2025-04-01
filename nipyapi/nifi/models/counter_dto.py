"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class CounterDTO(object):
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
        'id': 'str',
        'context': 'str',
        'name': 'str',
        'value_count': 'int',
        'value': 'str'
    }

    attribute_map = {
        'id': 'id',
        'context': 'context',
        'name': 'name',
        'value_count': 'valueCount',
        'value': 'value'
    }

    def __init__(self, id=None, context=None, name=None, value_count=None, value=None):
        """
        CounterDTO - a model defined in Swagger
        """

        self._id = None
        self._context = None
        self._name = None
        self._value_count = None
        self._value = None

        if id is not None:
          self.id = id
        if context is not None:
          self.context = context
        if name is not None:
          self.name = name
        if value_count is not None:
          self.value_count = value_count
        if value is not None:
          self.value = value

    @property
    def id(self):
        """
        Gets the id of this CounterDTO.
        The id of the counter.

        :return: The id of this CounterDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CounterDTO.
        The id of the counter.

        :param id: The id of this CounterDTO.
        :type: str
        """

        self._id = id

    @property
    def context(self):
        """
        Gets the context of this CounterDTO.
        The context of the counter.

        :return: The context of this CounterDTO.
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this CounterDTO.
        The context of the counter.

        :param context: The context of this CounterDTO.
        :type: str
        """

        self._context = context

    @property
    def name(self):
        """
        Gets the name of this CounterDTO.
        The name of the counter.

        :return: The name of this CounterDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CounterDTO.
        The name of the counter.

        :param name: The name of this CounterDTO.
        :type: str
        """

        self._name = name

    @property
    def value_count(self):
        """
        Gets the value_count of this CounterDTO.
        The value count.

        :return: The value_count of this CounterDTO.
        :rtype: int
        """
        return self._value_count

    @value_count.setter
    def value_count(self, value_count):
        """
        Sets the value_count of this CounterDTO.
        The value count.

        :param value_count: The value_count of this CounterDTO.
        :type: int
        """

        self._value_count = value_count

    @property
    def value(self):
        """
        Gets the value of this CounterDTO.
        The value of the counter.

        :return: The value of this CounterDTO.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this CounterDTO.
        The value of the counter.

        :param value: The value of this CounterDTO.
        :type: str
        """

        self._value = value

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
        if not isinstance(other, CounterDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
