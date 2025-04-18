"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class StatusDescriptorDTO(object):
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
        'field': 'str',
        'label': 'str',
        'description': 'str',
        'formatter': 'str'
    }

    attribute_map = {
        'field': 'field',
        'label': 'label',
        'description': 'description',
        'formatter': 'formatter'
    }

    def __init__(self, field=None, label=None, description=None, formatter=None):
        """
        StatusDescriptorDTO - a model defined in Swagger
        """

        self._field = None
        self._label = None
        self._description = None
        self._formatter = None

        if field is not None:
          self.field = field
        if label is not None:
          self.label = label
        if description is not None:
          self.description = description
        if formatter is not None:
          self.formatter = formatter

    @property
    def field(self):
        """
        Gets the field of this StatusDescriptorDTO.
        The name of the status field.

        :return: The field of this StatusDescriptorDTO.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this StatusDescriptorDTO.
        The name of the status field.

        :param field: The field of this StatusDescriptorDTO.
        :type: str
        """

        self._field = field

    @property
    def label(self):
        """
        Gets the label of this StatusDescriptorDTO.
        The label for the status field.

        :return: The label of this StatusDescriptorDTO.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this StatusDescriptorDTO.
        The label for the status field.

        :param label: The label of this StatusDescriptorDTO.
        :type: str
        """

        self._label = label

    @property
    def description(self):
        """
        Gets the description of this StatusDescriptorDTO.
        The description of the status field.

        :return: The description of this StatusDescriptorDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this StatusDescriptorDTO.
        The description of the status field.

        :param description: The description of this StatusDescriptorDTO.
        :type: str
        """

        self._description = description

    @property
    def formatter(self):
        """
        Gets the formatter of this StatusDescriptorDTO.
        The formatter for the status descriptor.

        :return: The formatter of this StatusDescriptorDTO.
        :rtype: str
        """
        return self._formatter

    @formatter.setter
    def formatter(self, formatter):
        """
        Sets the formatter of this StatusDescriptorDTO.
        The formatter for the status descriptor.

        :param formatter: The formatter of this StatusDescriptorDTO.
        :type: str
        """

        self._formatter = formatter

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
        if not isinstance(other, StatusDescriptorDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
