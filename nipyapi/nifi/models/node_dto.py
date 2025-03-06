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


class NodeDTO(object):
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
        'node_id': 'str',
        'address': 'str',
        'api_port': 'int',
        'status': 'str',
        'heartbeat': 'str',
        'connection_requested': 'str',
        'roles': 'list[str]',
        'active_thread_count': 'int',
        'queued': 'str',
        'events': 'list[NodeEventDTO]',
        'node_start_time': 'str'
    }

    attribute_map = {
        'node_id': 'nodeId',
        'address': 'address',
        'api_port': 'apiPort',
        'status': 'status',
        'heartbeat': 'heartbeat',
        'connection_requested': 'connectionRequested',
        'roles': 'roles',
        'active_thread_count': 'activeThreadCount',
        'queued': 'queued',
        'events': 'events',
        'node_start_time': 'nodeStartTime'
    }

    def __init__(self, node_id=None, address=None, api_port=None, status=None, heartbeat=None, connection_requested=None, roles=None, active_thread_count=None, queued=None, events=None, node_start_time=None):
        """
        NodeDTO - a model defined in Swagger
        """

        self._node_id = None
        self._address = None
        self._api_port = None
        self._status = None
        self._heartbeat = None
        self._connection_requested = None
        self._roles = None
        self._active_thread_count = None
        self._queued = None
        self._events = None
        self._node_start_time = None

        if node_id is not None:
          self.node_id = node_id
        if address is not None:
          self.address = address
        if api_port is not None:
          self.api_port = api_port
        if status is not None:
          self.status = status
        if heartbeat is not None:
          self.heartbeat = heartbeat
        if connection_requested is not None:
          self.connection_requested = connection_requested
        if roles is not None:
          self.roles = roles
        if active_thread_count is not None:
          self.active_thread_count = active_thread_count
        if queued is not None:
          self.queued = queued
        if events is not None:
          self.events = events
        if node_start_time is not None:
          self.node_start_time = node_start_time

    @property
    def node_id(self):
        """
        Gets the node_id of this NodeDTO.
        The id of the node.

        :return: The node_id of this NodeDTO.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """
        Sets the node_id of this NodeDTO.
        The id of the node.

        :param node_id: The node_id of this NodeDTO.
        :type: str
        """

        self._node_id = node_id

    @property
    def address(self):
        """
        Gets the address of this NodeDTO.
        The node's host/ip address.

        :return: The address of this NodeDTO.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this NodeDTO.
        The node's host/ip address.

        :param address: The address of this NodeDTO.
        :type: str
        """

        self._address = address

    @property
    def api_port(self):
        """
        Gets the api_port of this NodeDTO.
        The port the node is listening for API requests.

        :return: The api_port of this NodeDTO.
        :rtype: int
        """
        return self._api_port

    @api_port.setter
    def api_port(self, api_port):
        """
        Sets the api_port of this NodeDTO.
        The port the node is listening for API requests.

        :param api_port: The api_port of this NodeDTO.
        :type: int
        """

        self._api_port = api_port

    @property
    def status(self):
        """
        Gets the status of this NodeDTO.
        The node's status.

        :return: The status of this NodeDTO.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this NodeDTO.
        The node's status.

        :param status: The status of this NodeDTO.
        :type: str
        """

        self._status = status

    @property
    def heartbeat(self):
        """
        Gets the heartbeat of this NodeDTO.
        the time of the nodes's last heartbeat.

        :return: The heartbeat of this NodeDTO.
        :rtype: str
        """
        return self._heartbeat

    @heartbeat.setter
    def heartbeat(self, heartbeat):
        """
        Sets the heartbeat of this NodeDTO.
        the time of the nodes's last heartbeat.

        :param heartbeat: The heartbeat of this NodeDTO.
        :type: str
        """

        self._heartbeat = heartbeat

    @property
    def connection_requested(self):
        """
        Gets the connection_requested of this NodeDTO.
        The time of the node's last connection request.

        :return: The connection_requested of this NodeDTO.
        :rtype: str
        """
        return self._connection_requested

    @connection_requested.setter
    def connection_requested(self, connection_requested):
        """
        Sets the connection_requested of this NodeDTO.
        The time of the node's last connection request.

        :param connection_requested: The connection_requested of this NodeDTO.
        :type: str
        """

        self._connection_requested = connection_requested

    @property
    def roles(self):
        """
        Gets the roles of this NodeDTO.
        The roles of this node.

        :return: The roles of this NodeDTO.
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this NodeDTO.
        The roles of this node.

        :param roles: The roles of this NodeDTO.
        :type: list[str]
        """

        self._roles = roles

    @property
    def active_thread_count(self):
        """
        Gets the active_thread_count of this NodeDTO.
        The active threads for the NiFi on the node.

        :return: The active_thread_count of this NodeDTO.
        :rtype: int
        """
        return self._active_thread_count

    @active_thread_count.setter
    def active_thread_count(self, active_thread_count):
        """
        Sets the active_thread_count of this NodeDTO.
        The active threads for the NiFi on the node.

        :param active_thread_count: The active_thread_count of this NodeDTO.
        :type: int
        """

        self._active_thread_count = active_thread_count

    @property
    def queued(self):
        """
        Gets the queued of this NodeDTO.
        The queue the NiFi on the node.

        :return: The queued of this NodeDTO.
        :rtype: str
        """
        return self._queued

    @queued.setter
    def queued(self, queued):
        """
        Sets the queued of this NodeDTO.
        The queue the NiFi on the node.

        :param queued: The queued of this NodeDTO.
        :type: str
        """

        self._queued = queued

    @property
    def events(self):
        """
        Gets the events of this NodeDTO.
        The node's events.

        :return: The events of this NodeDTO.
        :rtype: list[NodeEventDTO]
        """
        return self._events

    @events.setter
    def events(self, events):
        """
        Sets the events of this NodeDTO.
        The node's events.

        :param events: The events of this NodeDTO.
        :type: list[NodeEventDTO]
        """

        self._events = events

    @property
    def node_start_time(self):
        """
        Gets the node_start_time of this NodeDTO.
        The time at which this Node was last refreshed.

        :return: The node_start_time of this NodeDTO.
        :rtype: str
        """
        return self._node_start_time

    @node_start_time.setter
    def node_start_time(self, node_start_time):
        """
        Sets the node_start_time of this NodeDTO.
        The time at which this Node was last refreshed.

        :param node_start_time: The node_start_time of this NodeDTO.
        :type: str
        """

        self._node_start_time = node_start_time

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
        if not isinstance(other, NodeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
