"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class ConnectionStatusDTO(object):
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
        'group_id': 'str',
        'name': 'str',
        'stats_last_refreshed': 'str',
        'source_id': 'str',
        'source_name': 'str',
        'destination_id': 'str',
        'destination_name': 'str',
        'aggregate_snapshot': 'ConnectionStatusSnapshotDTO',
        'node_snapshots': 'list[NodeConnectionStatusSnapshotDTO]'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'groupId',
        'name': 'name',
        'stats_last_refreshed': 'statsLastRefreshed',
        'source_id': 'sourceId',
        'source_name': 'sourceName',
        'destination_id': 'destinationId',
        'destination_name': 'destinationName',
        'aggregate_snapshot': 'aggregateSnapshot',
        'node_snapshots': 'nodeSnapshots'
    }

    def __init__(self, id=None, group_id=None, name=None, stats_last_refreshed=None, source_id=None, source_name=None, destination_id=None, destination_name=None, aggregate_snapshot=None, node_snapshots=None):
        """
        ConnectionStatusDTO - a model defined in Swagger
        """

        self._id = None
        self._group_id = None
        self._name = None
        self._stats_last_refreshed = None
        self._source_id = None
        self._source_name = None
        self._destination_id = None
        self._destination_name = None
        self._aggregate_snapshot = None
        self._node_snapshots = None

        if id is not None:
          self.id = id
        if group_id is not None:
          self.group_id = group_id
        if name is not None:
          self.name = name
        if stats_last_refreshed is not None:
          self.stats_last_refreshed = stats_last_refreshed
        if source_id is not None:
          self.source_id = source_id
        if source_name is not None:
          self.source_name = source_name
        if destination_id is not None:
          self.destination_id = destination_id
        if destination_name is not None:
          self.destination_name = destination_name
        if aggregate_snapshot is not None:
          self.aggregate_snapshot = aggregate_snapshot
        if node_snapshots is not None:
          self.node_snapshots = node_snapshots

    @property
    def id(self):
        """
        Gets the id of this ConnectionStatusDTO.
        The ID of the connection

        :return: The id of this ConnectionStatusDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ConnectionStatusDTO.
        The ID of the connection

        :param id: The id of this ConnectionStatusDTO.
        :type: str
        """

        self._id = id

    @property
    def group_id(self):
        """
        Gets the group_id of this ConnectionStatusDTO.
        The ID of the Process Group that the connection belongs to

        :return: The group_id of this ConnectionStatusDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this ConnectionStatusDTO.
        The ID of the Process Group that the connection belongs to

        :param group_id: The group_id of this ConnectionStatusDTO.
        :type: str
        """

        self._group_id = group_id

    @property
    def name(self):
        """
        Gets the name of this ConnectionStatusDTO.
        The name of the connection

        :return: The name of this ConnectionStatusDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConnectionStatusDTO.
        The name of the connection

        :param name: The name of this ConnectionStatusDTO.
        :type: str
        """

        self._name = name

    @property
    def stats_last_refreshed(self):
        """
        Gets the stats_last_refreshed of this ConnectionStatusDTO.
        The timestamp of when the stats were last refreshed

        :return: The stats_last_refreshed of this ConnectionStatusDTO.
        :rtype: str
        """
        return self._stats_last_refreshed

    @stats_last_refreshed.setter
    def stats_last_refreshed(self, stats_last_refreshed):
        """
        Sets the stats_last_refreshed of this ConnectionStatusDTO.
        The timestamp of when the stats were last refreshed

        :param stats_last_refreshed: The stats_last_refreshed of this ConnectionStatusDTO.
        :type: str
        """

        self._stats_last_refreshed = stats_last_refreshed

    @property
    def source_id(self):
        """
        Gets the source_id of this ConnectionStatusDTO.
        The ID of the source component

        :return: The source_id of this ConnectionStatusDTO.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this ConnectionStatusDTO.
        The ID of the source component

        :param source_id: The source_id of this ConnectionStatusDTO.
        :type: str
        """

        self._source_id = source_id

    @property
    def source_name(self):
        """
        Gets the source_name of this ConnectionStatusDTO.
        The name of the source component

        :return: The source_name of this ConnectionStatusDTO.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this ConnectionStatusDTO.
        The name of the source component

        :param source_name: The source_name of this ConnectionStatusDTO.
        :type: str
        """

        self._source_name = source_name

    @property
    def destination_id(self):
        """
        Gets the destination_id of this ConnectionStatusDTO.
        The ID of the destination component

        :return: The destination_id of this ConnectionStatusDTO.
        :rtype: str
        """
        return self._destination_id

    @destination_id.setter
    def destination_id(self, destination_id):
        """
        Sets the destination_id of this ConnectionStatusDTO.
        The ID of the destination component

        :param destination_id: The destination_id of this ConnectionStatusDTO.
        :type: str
        """

        self._destination_id = destination_id

    @property
    def destination_name(self):
        """
        Gets the destination_name of this ConnectionStatusDTO.
        The name of the destination component

        :return: The destination_name of this ConnectionStatusDTO.
        :rtype: str
        """
        return self._destination_name

    @destination_name.setter
    def destination_name(self, destination_name):
        """
        Sets the destination_name of this ConnectionStatusDTO.
        The name of the destination component

        :param destination_name: The destination_name of this ConnectionStatusDTO.
        :type: str
        """

        self._destination_name = destination_name

    @property
    def aggregate_snapshot(self):
        """
        Gets the aggregate_snapshot of this ConnectionStatusDTO.
        The status snapshot that represents the aggregate stats of the cluster

        :return: The aggregate_snapshot of this ConnectionStatusDTO.
        :rtype: ConnectionStatusSnapshotDTO
        """
        return self._aggregate_snapshot

    @aggregate_snapshot.setter
    def aggregate_snapshot(self, aggregate_snapshot):
        """
        Sets the aggregate_snapshot of this ConnectionStatusDTO.
        The status snapshot that represents the aggregate stats of the cluster

        :param aggregate_snapshot: The aggregate_snapshot of this ConnectionStatusDTO.
        :type: ConnectionStatusSnapshotDTO
        """

        self._aggregate_snapshot = aggregate_snapshot

    @property
    def node_snapshots(self):
        """
        Gets the node_snapshots of this ConnectionStatusDTO.
        A list of status snapshots for each node

        :return: The node_snapshots of this ConnectionStatusDTO.
        :rtype: list[NodeConnectionStatusSnapshotDTO]
        """
        return self._node_snapshots

    @node_snapshots.setter
    def node_snapshots(self, node_snapshots):
        """
        Sets the node_snapshots of this ConnectionStatusDTO.
        A list of status snapshots for each node

        :param node_snapshots: The node_snapshots of this ConnectionStatusDTO.
        :type: list[NodeConnectionStatusSnapshotDTO]
        """

        self._node_snapshots = node_snapshots

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
        if not isinstance(other, ConnectionStatusDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
