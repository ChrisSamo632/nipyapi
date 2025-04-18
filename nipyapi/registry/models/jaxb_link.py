"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class JaxbLink(object):
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
        'href': 'str',
        'params': 'dict(str, str)'
    }

    attribute_map = {
        'href': 'href',
        'params': 'params'
    }

    def __init__(self, href=None, params=None):
        """
        JaxbLink - a model defined in Swagger
        """

        self._href = None
        self._params = None

        if href is not None:
          self.href = href
        if params is not None:
          self.params = params

    @property
    def href(self):
        """
        Gets the href of this JaxbLink.
        The href for the link

        :return: The href of this JaxbLink.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """
        Sets the href of this JaxbLink.
        The href for the link

        :param href: The href of this JaxbLink.
        :type: str
        """

        self._href = href

    @property
    def params(self):
        """
        Gets the params of this JaxbLink.
        The params for the link

        :return: The params of this JaxbLink.
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """
        Sets the params of this JaxbLink.
        The params for the link

        :param params: The params of this JaxbLink.
        :type: dict(str, str)
        """

        self._params = params

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
        if not isinstance(other, JaxbLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
