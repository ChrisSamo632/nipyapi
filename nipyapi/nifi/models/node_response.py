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


class NodeResponse(object):
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
        'http_method': 'str',
        'request_uri': 'str',
        'response': 'Response',
        'node_id': 'NodeIdentifier',
        'throwable': 'Throwable',
        'updated_entity': 'Entity',
        'request_id': 'str',
        'input_stream': 'InputStream',
        'status': 'int',
        'client_response': 'Response',
        'is5xx': 'bool',
        'is2xx': 'bool'
    }

    attribute_map = {
        'http_method': 'httpMethod',
        'request_uri': 'requestUri',
        'response': 'response',
        'node_id': 'nodeId',
        'throwable': 'throwable',
        'updated_entity': 'updatedEntity',
        'request_id': 'requestId',
        'input_stream': 'inputStream',
        'status': 'status',
        'client_response': 'clientResponse',
        'is5xx': 'is5xx',
        'is2xx': 'is2xx'
    }

    def __init__(self, http_method=None, request_uri=None, response=None, node_id=None, throwable=None, updated_entity=None, request_id=None, input_stream=None, status=None, client_response=None, is5xx=None, is2xx=None):
        """
        NodeResponse - a model defined in Swagger
        """

        self._http_method = None
        self._request_uri = None
        self._response = None
        self._node_id = None
        self._throwable = None
        self._updated_entity = None
        self._request_id = None
        self._input_stream = None
        self._status = None
        self._client_response = None
        self._is5xx = None
        self._is2xx = None

        if http_method is not None:
          self.http_method = http_method
        if request_uri is not None:
          self.request_uri = request_uri
        if response is not None:
          self.response = response
        if node_id is not None:
          self.node_id = node_id
        if throwable is not None:
          self.throwable = throwable
        if updated_entity is not None:
          self.updated_entity = updated_entity
        if request_id is not None:
          self.request_id = request_id
        if input_stream is not None:
          self.input_stream = input_stream
        if status is not None:
          self.status = status
        if client_response is not None:
          self.client_response = client_response
        if is5xx is not None:
          self.is5xx = is5xx
        if is2xx is not None:
          self.is2xx = is2xx

    @property
    def http_method(self):
        """
        Gets the http_method of this NodeResponse.

        :return: The http_method of this NodeResponse.
        :rtype: str
        """
        return self._http_method

    @http_method.setter
    def http_method(self, http_method):
        """
        Sets the http_method of this NodeResponse.

        :param http_method: The http_method of this NodeResponse.
        :type: str
        """

        self._http_method = http_method

    @property
    def request_uri(self):
        """
        Gets the request_uri of this NodeResponse.

        :return: The request_uri of this NodeResponse.
        :rtype: str
        """
        return self._request_uri

    @request_uri.setter
    def request_uri(self, request_uri):
        """
        Sets the request_uri of this NodeResponse.

        :param request_uri: The request_uri of this NodeResponse.
        :type: str
        """

        self._request_uri = request_uri

    @property
    def response(self):
        """
        Gets the response of this NodeResponse.

        :return: The response of this NodeResponse.
        :rtype: Response
        """
        return self._response

    @response.setter
    def response(self, response):
        """
        Sets the response of this NodeResponse.

        :param response: The response of this NodeResponse.
        :type: Response
        """

        self._response = response

    @property
    def node_id(self):
        """
        Gets the node_id of this NodeResponse.

        :return: The node_id of this NodeResponse.
        :rtype: NodeIdentifier
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this NodeResponse.

        :param node_id: The node_id of this NodeResponse.
        :type: NodeIdentifier
        """

        self._node_id = node_id

    @property
    def throwable(self):
        """
        Gets the throwable of this NodeResponse.

        :return: The throwable of this NodeResponse.
        :rtype: Throwable
        """
        return self._throwable

    @throwable.setter
    def throwable(self, throwable):
        """
        Sets the throwable of this NodeResponse.

        :param throwable: The throwable of this NodeResponse.
        :type: Throwable
        """

        self._throwable = throwable

    @property
    def updated_entity(self):
        """
        Gets the updated_entity of this NodeResponse.

        :return: The updated_entity of this NodeResponse.
        :rtype: Entity
        """
        return self._updated_entity

    @updated_entity.setter
    def updated_entity(self, updated_entity):
        """
        Sets the updated_entity of this NodeResponse.

        :param updated_entity: The updated_entity of this NodeResponse.
        :type: Entity
        """

        self._updated_entity = updated_entity

    @property
    def request_id(self):
        """
        Gets the request_id of this NodeResponse.

        :return: The request_id of this NodeResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this NodeResponse.

        :param request_id: The request_id of this NodeResponse.
        :type: str
        """

        self._request_id = request_id

    @property
    def input_stream(self):
        """
        Gets the input_stream of this NodeResponse.

        :return: The input_stream of this NodeResponse.
        :rtype: InputStream
        """
        return self._input_stream

    @input_stream.setter
    def input_stream(self, input_stream):
        """
        Sets the input_stream of this NodeResponse.

        :param input_stream: The input_stream of this NodeResponse.
        :type: InputStream
        """

        self._input_stream = input_stream

    @property
    def status(self):
        """
        Gets the status of this NodeResponse.

        :return: The status of this NodeResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this NodeResponse.

        :param status: The status of this NodeResponse.
        :type: int
        """

        self._status = status

    @property
    def client_response(self):
        """
        Gets the client_response of this NodeResponse.

        :return: The client_response of this NodeResponse.
        :rtype: Response
        """
        return self._client_response

    @client_response.setter
    def client_response(self, client_response):
        """
        Sets the client_response of this NodeResponse.

        :param client_response: The client_response of this NodeResponse.
        :type: Response
        """

        self._client_response = client_response

    @property
    def is5xx(self):
        """
        Gets the is5xx of this NodeResponse.

        :return: The is5xx of this NodeResponse.
        :rtype: bool
        """
        return self._is5xx

    @is5xx.setter
    def is5xx(self, is5xx):
        """
        Sets the is5xx of this NodeResponse.

        :param is5xx: The is5xx of this NodeResponse.
        :type: bool
        """

        self._is5xx = is5xx

    @property
    def is2xx(self):
        """
        Gets the is2xx of this NodeResponse.

        :return: The is2xx of this NodeResponse.
        :rtype: bool
        """
        return self._is2xx

    @is2xx.setter
    def is2xx(self, is2xx):
        """
        Sets the is2xx of this NodeResponse.

        :param is2xx: The is2xx of this NodeResponse.
        :type: bool
        """

        self._is2xx = is2xx

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
        if not isinstance(other, NodeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
