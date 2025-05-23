"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class RemoteProcessGroupStatusDTO(object):
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
        'group_id': 'str',
        'id': 'str',
        'name': 'str',
        'target_uri': 'str',
        'transmission_status': 'str',
        'stats_last_refreshed': 'str',
        'validation_status': 'str',
        'aggregate_snapshot': 'RemoteProcessGroupStatusSnapshotDTO',
        'node_snapshots': 'list[NodeRemoteProcessGroupStatusSnapshotDTO]'
    }

    attribute_map = {
        'group_id': 'groupId',
        'id': 'id',
        'name': 'name',
        'target_uri': 'targetUri',
        'transmission_status': 'transmissionStatus',
        'stats_last_refreshed': 'statsLastRefreshed',
        'validation_status': 'validationStatus',
        'aggregate_snapshot': 'aggregateSnapshot',
        'node_snapshots': 'nodeSnapshots'
    }

    def __init__(self, group_id=None, id=None, name=None, target_uri=None, transmission_status=None, stats_last_refreshed=None, validation_status=None, aggregate_snapshot=None, node_snapshots=None):
        """
        RemoteProcessGroupStatusDTO - a model defined in Swagger
        """

        self._group_id = None
        self._id = None
        self._name = None
        self._target_uri = None
        self._transmission_status = None
        self._stats_last_refreshed = None
        self._validation_status = None
        self._aggregate_snapshot = None
        self._node_snapshots = None

        if group_id is not None:
          self.group_id = group_id
        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if target_uri is not None:
          self.target_uri = target_uri
        if transmission_status is not None:
          self.transmission_status = transmission_status
        if stats_last_refreshed is not None:
          self.stats_last_refreshed = stats_last_refreshed
        if validation_status is not None:
          self.validation_status = validation_status
        if aggregate_snapshot is not None:
          self.aggregate_snapshot = aggregate_snapshot
        if node_snapshots is not None:
          self.node_snapshots = node_snapshots

    @property
    def group_id(self):
        """
        Gets the group_id of this RemoteProcessGroupStatusDTO.
        The unique ID of the process group that the Processor belongs to

        :return: The group_id of this RemoteProcessGroupStatusDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this RemoteProcessGroupStatusDTO.
        The unique ID of the process group that the Processor belongs to

        :param group_id: The group_id of this RemoteProcessGroupStatusDTO.
        :type: str
        """

        self._group_id = group_id

    @property
    def id(self):
        """
        Gets the id of this RemoteProcessGroupStatusDTO.
        The unique ID of the Processor

        :return: The id of this RemoteProcessGroupStatusDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RemoteProcessGroupStatusDTO.
        The unique ID of the Processor

        :param id: The id of this RemoteProcessGroupStatusDTO.
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this RemoteProcessGroupStatusDTO.
        The name of the remote process group.

        :return: The name of this RemoteProcessGroupStatusDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RemoteProcessGroupStatusDTO.
        The name of the remote process group.

        :param name: The name of this RemoteProcessGroupStatusDTO.
        :type: str
        """

        self._name = name

    @property
    def target_uri(self):
        """
        Gets the target_uri of this RemoteProcessGroupStatusDTO.
        The URI of the target system.

        :return: The target_uri of this RemoteProcessGroupStatusDTO.
        :rtype: str
        """
        return self._target_uri

    @target_uri.setter
    def target_uri(self, target_uri):
        """
        Sets the target_uri of this RemoteProcessGroupStatusDTO.
        The URI of the target system.

        :param target_uri: The target_uri of this RemoteProcessGroupStatusDTO.
        :type: str
        """

        self._target_uri = target_uri

    @property
    def transmission_status(self):
        """
        Gets the transmission_status of this RemoteProcessGroupStatusDTO.
        The transmission status of the remote process group.

        :return: The transmission_status of this RemoteProcessGroupStatusDTO.
        :rtype: str
        """
        return self._transmission_status

    @transmission_status.setter
    def transmission_status(self, transmission_status):
        """
        Sets the transmission_status of this RemoteProcessGroupStatusDTO.
        The transmission status of the remote process group.

        :param transmission_status: The transmission_status of this RemoteProcessGroupStatusDTO.
        :type: str
        """

        self._transmission_status = transmission_status

    @property
    def stats_last_refreshed(self):
        """
        Gets the stats_last_refreshed of this RemoteProcessGroupStatusDTO.
        The time the status for the process group was last refreshed.

        :return: The stats_last_refreshed of this RemoteProcessGroupStatusDTO.
        :rtype: str
        """
        return self._stats_last_refreshed

    @stats_last_refreshed.setter
    def stats_last_refreshed(self, stats_last_refreshed):
        """
        Sets the stats_last_refreshed of this RemoteProcessGroupStatusDTO.
        The time the status for the process group was last refreshed.

        :param stats_last_refreshed: The stats_last_refreshed of this RemoteProcessGroupStatusDTO.
        :type: str
        """

        self._stats_last_refreshed = stats_last_refreshed

    @property
    def validation_status(self):
        """
        Gets the validation_status of this RemoteProcessGroupStatusDTO.
        Indicates whether the component is valid, invalid, or still in the process of validating (i.e., it is unknown whether or not the component is valid)

        :return: The validation_status of this RemoteProcessGroupStatusDTO.
        :rtype: str
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status):
        """
        Sets the validation_status of this RemoteProcessGroupStatusDTO.
        Indicates whether the component is valid, invalid, or still in the process of validating (i.e., it is unknown whether or not the component is valid)

        :param validation_status: The validation_status of this RemoteProcessGroupStatusDTO.
        :type: str
        """
        allowed_values = ["VALID", "INVALID", "VALIDATING"]
        if validation_status not in allowed_values:
            raise ValueError(
                "Invalid value for `validation_status` ({0}), must be one of {1}"
                .format(validation_status, allowed_values)
            )

        self._validation_status = validation_status

    @property
    def aggregate_snapshot(self):
        """
        Gets the aggregate_snapshot of this RemoteProcessGroupStatusDTO.
        A status snapshot that represents the aggregate stats of all nodes in the cluster. If the NiFi instance is a standalone instance, rather than a cluster, this represents the stats of the single instance.

        :return: The aggregate_snapshot of this RemoteProcessGroupStatusDTO.
        :rtype: RemoteProcessGroupStatusSnapshotDTO
        """
        return self._aggregate_snapshot

    @aggregate_snapshot.setter
    def aggregate_snapshot(self, aggregate_snapshot):
        """
        Sets the aggregate_snapshot of this RemoteProcessGroupStatusDTO.
        A status snapshot that represents the aggregate stats of all nodes in the cluster. If the NiFi instance is a standalone instance, rather than a cluster, this represents the stats of the single instance.

        :param aggregate_snapshot: The aggregate_snapshot of this RemoteProcessGroupStatusDTO.
        :type: RemoteProcessGroupStatusSnapshotDTO
        """

        self._aggregate_snapshot = aggregate_snapshot

    @property
    def node_snapshots(self):
        """
        Gets the node_snapshots of this RemoteProcessGroupStatusDTO.
        A status snapshot for each node in the cluster. If the NiFi instance is a standalone instance, rather than a cluster, this may be null.

        :return: The node_snapshots of this RemoteProcessGroupStatusDTO.
        :rtype: list[NodeRemoteProcessGroupStatusSnapshotDTO]
        """
        return self._node_snapshots

    @node_snapshots.setter
    def node_snapshots(self, node_snapshots):
        """
        Sets the node_snapshots of this RemoteProcessGroupStatusDTO.
        A status snapshot for each node in the cluster. If the NiFi instance is a standalone instance, rather than a cluster, this may be null.

        :param node_snapshots: The node_snapshots of this RemoteProcessGroupStatusDTO.
        :type: list[NodeRemoteProcessGroupStatusSnapshotDTO]
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
        if not isinstance(other, RemoteProcessGroupStatusDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
