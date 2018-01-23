# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.5.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProcessGroupEntity(object):
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
        'revision': 'RevisionDTO',
        'id': 'str',
        'uri': 'str',
        'position': 'PositionDTO',
        'permissions': 'PermissionsDTO',
        'bulletins': 'list[BulletinEntity]',
        'component': 'ProcessGroupDTO',
        'status': 'ProcessGroupStatusDTO',
        'versioned_flow_snapshot': 'VersionedFlowSnapshot',
        'running_count': 'int',
        'stopped_count': 'int',
        'invalid_count': 'int',
        'disabled_count': 'int',
        'active_remote_port_count': 'int',
        'inactive_remote_port_count': 'int',
        'versioned_flow_state': 'str',
        'up_to_date_count': 'int',
        'locally_modified_count': 'int',
        'stale_count': 'int',
        'locally_modified_and_stale_count': 'int',
        'sync_failure_count': 'int',
        'input_port_count': 'int',
        'output_port_count': 'int'
    }

    attribute_map = {
        'revision': 'revision',
        'id': 'id',
        'uri': 'uri',
        'position': 'position',
        'permissions': 'permissions',
        'bulletins': 'bulletins',
        'component': 'component',
        'status': 'status',
        'versioned_flow_snapshot': 'versionedFlowSnapshot',
        'running_count': 'runningCount',
        'stopped_count': 'stoppedCount',
        'invalid_count': 'invalidCount',
        'disabled_count': 'disabledCount',
        'active_remote_port_count': 'activeRemotePortCount',
        'inactive_remote_port_count': 'inactiveRemotePortCount',
        'versioned_flow_state': 'versionedFlowState',
        'up_to_date_count': 'upToDateCount',
        'locally_modified_count': 'locallyModifiedCount',
        'stale_count': 'staleCount',
        'locally_modified_and_stale_count': 'locallyModifiedAndStaleCount',
        'sync_failure_count': 'syncFailureCount',
        'input_port_count': 'inputPortCount',
        'output_port_count': 'outputPortCount'
    }

    def __init__(self, revision=None, id=None, uri=None, position=None, permissions=None, bulletins=None, component=None, status=None, versioned_flow_snapshot=None, running_count=None, stopped_count=None, invalid_count=None, disabled_count=None, active_remote_port_count=None, inactive_remote_port_count=None, versioned_flow_state=None, up_to_date_count=None, locally_modified_count=None, stale_count=None, locally_modified_and_stale_count=None, sync_failure_count=None, input_port_count=None, output_port_count=None):
        """
        ProcessGroupEntity - a model defined in Swagger
        """

        self._revision = None
        self._id = None
        self._uri = None
        self._position = None
        self._permissions = None
        self._bulletins = None
        self._component = None
        self._status = None
        self._versioned_flow_snapshot = None
        self._running_count = None
        self._stopped_count = None
        self._invalid_count = None
        self._disabled_count = None
        self._active_remote_port_count = None
        self._inactive_remote_port_count = None
        self._versioned_flow_state = None
        self._up_to_date_count = None
        self._locally_modified_count = None
        self._stale_count = None
        self._locally_modified_and_stale_count = None
        self._sync_failure_count = None
        self._input_port_count = None
        self._output_port_count = None

        if revision is not None:
          self.revision = revision
        if id is not None:
          self.id = id
        if uri is not None:
          self.uri = uri
        if position is not None:
          self.position = position
        if permissions is not None:
          self.permissions = permissions
        if bulletins is not None:
          self.bulletins = bulletins
        if component is not None:
          self.component = component
        if status is not None:
          self.status = status
        if versioned_flow_snapshot is not None:
          self.versioned_flow_snapshot = versioned_flow_snapshot
        if running_count is not None:
          self.running_count = running_count
        if stopped_count is not None:
          self.stopped_count = stopped_count
        if invalid_count is not None:
          self.invalid_count = invalid_count
        if disabled_count is not None:
          self.disabled_count = disabled_count
        if active_remote_port_count is not None:
          self.active_remote_port_count = active_remote_port_count
        if inactive_remote_port_count is not None:
          self.inactive_remote_port_count = inactive_remote_port_count
        if versioned_flow_state is not None:
          self.versioned_flow_state = versioned_flow_state
        if up_to_date_count is not None:
          self.up_to_date_count = up_to_date_count
        if locally_modified_count is not None:
          self.locally_modified_count = locally_modified_count
        if stale_count is not None:
          self.stale_count = stale_count
        if locally_modified_and_stale_count is not None:
          self.locally_modified_and_stale_count = locally_modified_and_stale_count
        if sync_failure_count is not None:
          self.sync_failure_count = sync_failure_count
        if input_port_count is not None:
          self.input_port_count = input_port_count
        if output_port_count is not None:
          self.output_port_count = output_port_count

    @property
    def revision(self):
        """
        Gets the revision of this ProcessGroupEntity.
        The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses.

        :return: The revision of this ProcessGroupEntity.
        :rtype: RevisionDTO
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """
        Sets the revision of this ProcessGroupEntity.
        The revision for this request/response. The revision is required for any mutable flow requests and is included in all responses.

        :param revision: The revision of this ProcessGroupEntity.
        :type: RevisionDTO
        """

        self._revision = revision

    @property
    def id(self):
        """
        Gets the id of this ProcessGroupEntity.
        The id of the component.

        :return: The id of this ProcessGroupEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProcessGroupEntity.
        The id of the component.

        :param id: The id of this ProcessGroupEntity.
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """
        Gets the uri of this ProcessGroupEntity.
        The URI for futures requests to the component.

        :return: The uri of this ProcessGroupEntity.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this ProcessGroupEntity.
        The URI for futures requests to the component.

        :param uri: The uri of this ProcessGroupEntity.
        :type: str
        """

        self._uri = uri

    @property
    def position(self):
        """
        Gets the position of this ProcessGroupEntity.
        The position of this component in the UI if applicable.

        :return: The position of this ProcessGroupEntity.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ProcessGroupEntity.
        The position of this component in the UI if applicable.

        :param position: The position of this ProcessGroupEntity.
        :type: PositionDTO
        """

        self._position = position

    @property
    def permissions(self):
        """
        Gets the permissions of this ProcessGroupEntity.
        The permissions for this component.

        :return: The permissions of this ProcessGroupEntity.
        :rtype: PermissionsDTO
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """
        Sets the permissions of this ProcessGroupEntity.
        The permissions for this component.

        :param permissions: The permissions of this ProcessGroupEntity.
        :type: PermissionsDTO
        """

        self._permissions = permissions

    @property
    def bulletins(self):
        """
        Gets the bulletins of this ProcessGroupEntity.
        The bulletins for this component.

        :return: The bulletins of this ProcessGroupEntity.
        :rtype: list[BulletinEntity]
        """
        return self._bulletins

    @bulletins.setter
    def bulletins(self, bulletins):
        """
        Sets the bulletins of this ProcessGroupEntity.
        The bulletins for this component.

        :param bulletins: The bulletins of this ProcessGroupEntity.
        :type: list[BulletinEntity]
        """

        self._bulletins = bulletins

    @property
    def component(self):
        """
        Gets the component of this ProcessGroupEntity.

        :return: The component of this ProcessGroupEntity.
        :rtype: ProcessGroupDTO
        """
        return self._component

    @component.setter
    def component(self, component):
        """
        Sets the component of this ProcessGroupEntity.

        :param component: The component of this ProcessGroupEntity.
        :type: ProcessGroupDTO
        """

        self._component = component

    @property
    def status(self):
        """
        Gets the status of this ProcessGroupEntity.
        The status of the process group.

        :return: The status of this ProcessGroupEntity.
        :rtype: ProcessGroupStatusDTO
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ProcessGroupEntity.
        The status of the process group.

        :param status: The status of this ProcessGroupEntity.
        :type: ProcessGroupStatusDTO
        """

        self._status = status

    @property
    def versioned_flow_snapshot(self):
        """
        Gets the versioned_flow_snapshot of this ProcessGroupEntity.
        Returns the Versioned Flow that describes the contents of the Versioned Flow to be imported

        :return: The versioned_flow_snapshot of this ProcessGroupEntity.
        :rtype: VersionedFlowSnapshot
        """
        return self._versioned_flow_snapshot

    @versioned_flow_snapshot.setter
    def versioned_flow_snapshot(self, versioned_flow_snapshot):
        """
        Sets the versioned_flow_snapshot of this ProcessGroupEntity.
        Returns the Versioned Flow that describes the contents of the Versioned Flow to be imported

        :param versioned_flow_snapshot: The versioned_flow_snapshot of this ProcessGroupEntity.
        :type: VersionedFlowSnapshot
        """

        self._versioned_flow_snapshot = versioned_flow_snapshot

    @property
    def running_count(self):
        """
        Gets the running_count of this ProcessGroupEntity.
        The number of running components in this process group.

        :return: The running_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._running_count

    @running_count.setter
    def running_count(self, running_count):
        """
        Sets the running_count of this ProcessGroupEntity.
        The number of running components in this process group.

        :param running_count: The running_count of this ProcessGroupEntity.
        :type: int
        """

        self._running_count = running_count

    @property
    def stopped_count(self):
        """
        Gets the stopped_count of this ProcessGroupEntity.
        The number of stopped components in the process group.

        :return: The stopped_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._stopped_count

    @stopped_count.setter
    def stopped_count(self, stopped_count):
        """
        Sets the stopped_count of this ProcessGroupEntity.
        The number of stopped components in the process group.

        :param stopped_count: The stopped_count of this ProcessGroupEntity.
        :type: int
        """

        self._stopped_count = stopped_count

    @property
    def invalid_count(self):
        """
        Gets the invalid_count of this ProcessGroupEntity.
        The number of invalid components in the process group.

        :return: The invalid_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._invalid_count

    @invalid_count.setter
    def invalid_count(self, invalid_count):
        """
        Sets the invalid_count of this ProcessGroupEntity.
        The number of invalid components in the process group.

        :param invalid_count: The invalid_count of this ProcessGroupEntity.
        :type: int
        """

        self._invalid_count = invalid_count

    @property
    def disabled_count(self):
        """
        Gets the disabled_count of this ProcessGroupEntity.
        The number of disabled components in the process group.

        :return: The disabled_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._disabled_count

    @disabled_count.setter
    def disabled_count(self, disabled_count):
        """
        Sets the disabled_count of this ProcessGroupEntity.
        The number of disabled components in the process group.

        :param disabled_count: The disabled_count of this ProcessGroupEntity.
        :type: int
        """

        self._disabled_count = disabled_count

    @property
    def active_remote_port_count(self):
        """
        Gets the active_remote_port_count of this ProcessGroupEntity.
        The number of active remote ports in the process group.

        :return: The active_remote_port_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._active_remote_port_count

    @active_remote_port_count.setter
    def active_remote_port_count(self, active_remote_port_count):
        """
        Sets the active_remote_port_count of this ProcessGroupEntity.
        The number of active remote ports in the process group.

        :param active_remote_port_count: The active_remote_port_count of this ProcessGroupEntity.
        :type: int
        """

        self._active_remote_port_count = active_remote_port_count

    @property
    def inactive_remote_port_count(self):
        """
        Gets the inactive_remote_port_count of this ProcessGroupEntity.
        The number of inactive remote ports in the process group.

        :return: The inactive_remote_port_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._inactive_remote_port_count

    @inactive_remote_port_count.setter
    def inactive_remote_port_count(self, inactive_remote_port_count):
        """
        Sets the inactive_remote_port_count of this ProcessGroupEntity.
        The number of inactive remote ports in the process group.

        :param inactive_remote_port_count: The inactive_remote_port_count of this ProcessGroupEntity.
        :type: int
        """

        self._inactive_remote_port_count = inactive_remote_port_count

    @property
    def versioned_flow_state(self):
        """
        Gets the versioned_flow_state of this ProcessGroupEntity.
        The current state of the Process Group, as it relates to the Versioned Flow

        :return: The versioned_flow_state of this ProcessGroupEntity.
        :rtype: str
        """
        return self._versioned_flow_state

    @versioned_flow_state.setter
    def versioned_flow_state(self, versioned_flow_state):
        """
        Sets the versioned_flow_state of this ProcessGroupEntity.
        The current state of the Process Group, as it relates to the Versioned Flow

        :param versioned_flow_state: The versioned_flow_state of this ProcessGroupEntity.
        :type: str
        """
        allowed_values = ["LOCALLY_MODIFIED_DESCENDANT", "LOCALLY_MODIFIED", "STALE", "LOCALLY_MODIFIED_AND_STALE", "UP_TO_DATE"]
        if versioned_flow_state not in allowed_values:
            raise ValueError(
                "Invalid value for `versioned_flow_state` ({0}), must be one of {1}"
                .format(versioned_flow_state, allowed_values)
            )

        self._versioned_flow_state = versioned_flow_state

    @property
    def up_to_date_count(self):
        """
        Gets the up_to_date_count of this ProcessGroupEntity.
        The number of up to date versioned process groups in the process group.

        :return: The up_to_date_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._up_to_date_count

    @up_to_date_count.setter
    def up_to_date_count(self, up_to_date_count):
        """
        Sets the up_to_date_count of this ProcessGroupEntity.
        The number of up to date versioned process groups in the process group.

        :param up_to_date_count: The up_to_date_count of this ProcessGroupEntity.
        :type: int
        """

        self._up_to_date_count = up_to_date_count

    @property
    def locally_modified_count(self):
        """
        Gets the locally_modified_count of this ProcessGroupEntity.
        The number of locally modified versioned process groups in the process group.

        :return: The locally_modified_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._locally_modified_count

    @locally_modified_count.setter
    def locally_modified_count(self, locally_modified_count):
        """
        Sets the locally_modified_count of this ProcessGroupEntity.
        The number of locally modified versioned process groups in the process group.

        :param locally_modified_count: The locally_modified_count of this ProcessGroupEntity.
        :type: int
        """

        self._locally_modified_count = locally_modified_count

    @property
    def stale_count(self):
        """
        Gets the stale_count of this ProcessGroupEntity.
        The number of stale versioned process groups in the process group.

        :return: The stale_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._stale_count

    @stale_count.setter
    def stale_count(self, stale_count):
        """
        Sets the stale_count of this ProcessGroupEntity.
        The number of stale versioned process groups in the process group.

        :param stale_count: The stale_count of this ProcessGroupEntity.
        :type: int
        """

        self._stale_count = stale_count

    @property
    def locally_modified_and_stale_count(self):
        """
        Gets the locally_modified_and_stale_count of this ProcessGroupEntity.
        The number of locally modified and stale versioned process groups in the process group.

        :return: The locally_modified_and_stale_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._locally_modified_and_stale_count

    @locally_modified_and_stale_count.setter
    def locally_modified_and_stale_count(self, locally_modified_and_stale_count):
        """
        Sets the locally_modified_and_stale_count of this ProcessGroupEntity.
        The number of locally modified and stale versioned process groups in the process group.

        :param locally_modified_and_stale_count: The locally_modified_and_stale_count of this ProcessGroupEntity.
        :type: int
        """

        self._locally_modified_and_stale_count = locally_modified_and_stale_count

    @property
    def sync_failure_count(self):
        """
        Gets the sync_failure_count of this ProcessGroupEntity.
        The number of versioned process groups in the process group that are unable to sync to a registry.

        :return: The sync_failure_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._sync_failure_count

    @sync_failure_count.setter
    def sync_failure_count(self, sync_failure_count):
        """
        Sets the sync_failure_count of this ProcessGroupEntity.
        The number of versioned process groups in the process group that are unable to sync to a registry.

        :param sync_failure_count: The sync_failure_count of this ProcessGroupEntity.
        :type: int
        """

        self._sync_failure_count = sync_failure_count

    @property
    def input_port_count(self):
        """
        Gets the input_port_count of this ProcessGroupEntity.
        The number of input ports in the process group.

        :return: The input_port_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._input_port_count

    @input_port_count.setter
    def input_port_count(self, input_port_count):
        """
        Sets the input_port_count of this ProcessGroupEntity.
        The number of input ports in the process group.

        :param input_port_count: The input_port_count of this ProcessGroupEntity.
        :type: int
        """

        self._input_port_count = input_port_count

    @property
    def output_port_count(self):
        """
        Gets the output_port_count of this ProcessGroupEntity.
        The number of output ports in the process group.

        :return: The output_port_count of this ProcessGroupEntity.
        :rtype: int
        """
        return self._output_port_count

    @output_port_count.setter
    def output_port_count(self, output_port_count):
        """
        Sets the output_port_count of this ProcessGroupEntity.
        The number of output ports in the process group.

        :param output_port_count: The output_port_count of this ProcessGroupEntity.
        :type: int
        """

        self._output_port_count = output_port_count

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
        if not isinstance(other, ProcessGroupEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
