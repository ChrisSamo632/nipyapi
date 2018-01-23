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


class ProcessGroupDTO(object):
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
        'versioned_component_id': 'str',
        'parent_group_id': 'str',
        'position': 'PositionDTO',
        'name': 'str',
        'comments': 'str',
        'variables': 'dict(str, str)',
        'version_control_information': 'VersionControlInformationDTO',
        'running_count': 'int',
        'stopped_count': 'int',
        'invalid_count': 'int',
        'disabled_count': 'int',
        'active_remote_port_count': 'int',
        'inactive_remote_port_count': 'int',
        'up_to_date_count': 'int',
        'locally_modified_count': 'int',
        'stale_count': 'int',
        'locally_modified_and_stale_count': 'int',
        'sync_failure_count': 'int',
        'input_port_count': 'int',
        'output_port_count': 'int',
        'contents': 'FlowSnippetDTO'
    }

    attribute_map = {
        'id': 'id',
        'versioned_component_id': 'versionedComponentId',
        'parent_group_id': 'parentGroupId',
        'position': 'position',
        'name': 'name',
        'comments': 'comments',
        'variables': 'variables',
        'version_control_information': 'versionControlInformation',
        'running_count': 'runningCount',
        'stopped_count': 'stoppedCount',
        'invalid_count': 'invalidCount',
        'disabled_count': 'disabledCount',
        'active_remote_port_count': 'activeRemotePortCount',
        'inactive_remote_port_count': 'inactiveRemotePortCount',
        'up_to_date_count': 'upToDateCount',
        'locally_modified_count': 'locallyModifiedCount',
        'stale_count': 'staleCount',
        'locally_modified_and_stale_count': 'locallyModifiedAndStaleCount',
        'sync_failure_count': 'syncFailureCount',
        'input_port_count': 'inputPortCount',
        'output_port_count': 'outputPortCount',
        'contents': 'contents'
    }

    def __init__(self, id=None, versioned_component_id=None, parent_group_id=None, position=None, name=None, comments=None, variables=None, version_control_information=None, running_count=None, stopped_count=None, invalid_count=None, disabled_count=None, active_remote_port_count=None, inactive_remote_port_count=None, up_to_date_count=None, locally_modified_count=None, stale_count=None, locally_modified_and_stale_count=None, sync_failure_count=None, input_port_count=None, output_port_count=None, contents=None):
        """
        ProcessGroupDTO - a model defined in Swagger
        """

        self._id = None
        self._versioned_component_id = None
        self._parent_group_id = None
        self._position = None
        self._name = None
        self._comments = None
        self._variables = None
        self._version_control_information = None
        self._running_count = None
        self._stopped_count = None
        self._invalid_count = None
        self._disabled_count = None
        self._active_remote_port_count = None
        self._inactive_remote_port_count = None
        self._up_to_date_count = None
        self._locally_modified_count = None
        self._stale_count = None
        self._locally_modified_and_stale_count = None
        self._sync_failure_count = None
        self._input_port_count = None
        self._output_port_count = None
        self._contents = None

        if id is not None:
          self.id = id
        if versioned_component_id is not None:
          self.versioned_component_id = versioned_component_id
        if parent_group_id is not None:
          self.parent_group_id = parent_group_id
        if position is not None:
          self.position = position
        if name is not None:
          self.name = name
        if comments is not None:
          self.comments = comments
        if variables is not None:
          self.variables = variables
        if version_control_information is not None:
          self.version_control_information = version_control_information
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
        if contents is not None:
          self.contents = contents

    @property
    def id(self):
        """
        Gets the id of this ProcessGroupDTO.
        The id of the component.

        :return: The id of this ProcessGroupDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProcessGroupDTO.
        The id of the component.

        :param id: The id of this ProcessGroupDTO.
        :type: str
        """

        self._id = id

    @property
    def versioned_component_id(self):
        """
        Gets the versioned_component_id of this ProcessGroupDTO.
        The ID of the corresponding component that is under version control

        :return: The versioned_component_id of this ProcessGroupDTO.
        :rtype: str
        """
        return self._versioned_component_id

    @versioned_component_id.setter
    def versioned_component_id(self, versioned_component_id):
        """
        Sets the versioned_component_id of this ProcessGroupDTO.
        The ID of the corresponding component that is under version control

        :param versioned_component_id: The versioned_component_id of this ProcessGroupDTO.
        :type: str
        """

        self._versioned_component_id = versioned_component_id

    @property
    def parent_group_id(self):
        """
        Gets the parent_group_id of this ProcessGroupDTO.
        The id of parent process group of this component if applicable.

        :return: The parent_group_id of this ProcessGroupDTO.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """
        Sets the parent_group_id of this ProcessGroupDTO.
        The id of parent process group of this component if applicable.

        :param parent_group_id: The parent_group_id of this ProcessGroupDTO.
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def position(self):
        """
        Gets the position of this ProcessGroupDTO.
        The position of this component in the UI if applicable.

        :return: The position of this ProcessGroupDTO.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ProcessGroupDTO.
        The position of this component in the UI if applicable.

        :param position: The position of this ProcessGroupDTO.
        :type: PositionDTO
        """

        self._position = position

    @property
    def name(self):
        """
        Gets the name of this ProcessGroupDTO.
        The name of the process group.

        :return: The name of this ProcessGroupDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProcessGroupDTO.
        The name of the process group.

        :param name: The name of this ProcessGroupDTO.
        :type: str
        """

        self._name = name

    @property
    def comments(self):
        """
        Gets the comments of this ProcessGroupDTO.
        The comments for the process group.

        :return: The comments of this ProcessGroupDTO.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this ProcessGroupDTO.
        The comments for the process group.

        :param comments: The comments of this ProcessGroupDTO.
        :type: str
        """

        self._comments = comments

    @property
    def variables(self):
        """
        Gets the variables of this ProcessGroupDTO.
        The variables that are configured for the Process Group. Note that this map contains only those variables that are defined on this Process Group and not any variables that are defined in the parent Process Group, etc. I.e., this Map will not contain all variables that are accessible by components in this Process Group by rather only the variables that are defined for this Process Group itself.

        :return: The variables of this ProcessGroupDTO.
        :rtype: dict(str, str)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """
        Sets the variables of this ProcessGroupDTO.
        The variables that are configured for the Process Group. Note that this map contains only those variables that are defined on this Process Group and not any variables that are defined in the parent Process Group, etc. I.e., this Map will not contain all variables that are accessible by components in this Process Group by rather only the variables that are defined for this Process Group itself.

        :param variables: The variables of this ProcessGroupDTO.
        :type: dict(str, str)
        """

        self._variables = variables

    @property
    def version_control_information(self):
        """
        Gets the version_control_information of this ProcessGroupDTO.
        The Version Control information that indicates which Flow Registry, and where in the Flow Registry, this Process Group is tracking to; or null if this Process Group is not under version control

        :return: The version_control_information of this ProcessGroupDTO.
        :rtype: VersionControlInformationDTO
        """
        return self._version_control_information

    @version_control_information.setter
    def version_control_information(self, version_control_information):
        """
        Sets the version_control_information of this ProcessGroupDTO.
        The Version Control information that indicates which Flow Registry, and where in the Flow Registry, this Process Group is tracking to; or null if this Process Group is not under version control

        :param version_control_information: The version_control_information of this ProcessGroupDTO.
        :type: VersionControlInformationDTO
        """

        self._version_control_information = version_control_information

    @property
    def running_count(self):
        """
        Gets the running_count of this ProcessGroupDTO.
        The number of running components in this process group.

        :return: The running_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._running_count

    @running_count.setter
    def running_count(self, running_count):
        """
        Sets the running_count of this ProcessGroupDTO.
        The number of running components in this process group.

        :param running_count: The running_count of this ProcessGroupDTO.
        :type: int
        """

        self._running_count = running_count

    @property
    def stopped_count(self):
        """
        Gets the stopped_count of this ProcessGroupDTO.
        The number of stopped components in the process group.

        :return: The stopped_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._stopped_count

    @stopped_count.setter
    def stopped_count(self, stopped_count):
        """
        Sets the stopped_count of this ProcessGroupDTO.
        The number of stopped components in the process group.

        :param stopped_count: The stopped_count of this ProcessGroupDTO.
        :type: int
        """

        self._stopped_count = stopped_count

    @property
    def invalid_count(self):
        """
        Gets the invalid_count of this ProcessGroupDTO.
        The number of invalid components in the process group.

        :return: The invalid_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._invalid_count

    @invalid_count.setter
    def invalid_count(self, invalid_count):
        """
        Sets the invalid_count of this ProcessGroupDTO.
        The number of invalid components in the process group.

        :param invalid_count: The invalid_count of this ProcessGroupDTO.
        :type: int
        """

        self._invalid_count = invalid_count

    @property
    def disabled_count(self):
        """
        Gets the disabled_count of this ProcessGroupDTO.
        The number of disabled components in the process group.

        :return: The disabled_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._disabled_count

    @disabled_count.setter
    def disabled_count(self, disabled_count):
        """
        Sets the disabled_count of this ProcessGroupDTO.
        The number of disabled components in the process group.

        :param disabled_count: The disabled_count of this ProcessGroupDTO.
        :type: int
        """

        self._disabled_count = disabled_count

    @property
    def active_remote_port_count(self):
        """
        Gets the active_remote_port_count of this ProcessGroupDTO.
        The number of active remote ports in the process group.

        :return: The active_remote_port_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._active_remote_port_count

    @active_remote_port_count.setter
    def active_remote_port_count(self, active_remote_port_count):
        """
        Sets the active_remote_port_count of this ProcessGroupDTO.
        The number of active remote ports in the process group.

        :param active_remote_port_count: The active_remote_port_count of this ProcessGroupDTO.
        :type: int
        """

        self._active_remote_port_count = active_remote_port_count

    @property
    def inactive_remote_port_count(self):
        """
        Gets the inactive_remote_port_count of this ProcessGroupDTO.
        The number of inactive remote ports in the process group.

        :return: The inactive_remote_port_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._inactive_remote_port_count

    @inactive_remote_port_count.setter
    def inactive_remote_port_count(self, inactive_remote_port_count):
        """
        Sets the inactive_remote_port_count of this ProcessGroupDTO.
        The number of inactive remote ports in the process group.

        :param inactive_remote_port_count: The inactive_remote_port_count of this ProcessGroupDTO.
        :type: int
        """

        self._inactive_remote_port_count = inactive_remote_port_count

    @property
    def up_to_date_count(self):
        """
        Gets the up_to_date_count of this ProcessGroupDTO.
        The number of up to date versioned process groups in the process group.

        :return: The up_to_date_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._up_to_date_count

    @up_to_date_count.setter
    def up_to_date_count(self, up_to_date_count):
        """
        Sets the up_to_date_count of this ProcessGroupDTO.
        The number of up to date versioned process groups in the process group.

        :param up_to_date_count: The up_to_date_count of this ProcessGroupDTO.
        :type: int
        """

        self._up_to_date_count = up_to_date_count

    @property
    def locally_modified_count(self):
        """
        Gets the locally_modified_count of this ProcessGroupDTO.
        The number of locally modified versioned process groups in the process group.

        :return: The locally_modified_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._locally_modified_count

    @locally_modified_count.setter
    def locally_modified_count(self, locally_modified_count):
        """
        Sets the locally_modified_count of this ProcessGroupDTO.
        The number of locally modified versioned process groups in the process group.

        :param locally_modified_count: The locally_modified_count of this ProcessGroupDTO.
        :type: int
        """

        self._locally_modified_count = locally_modified_count

    @property
    def stale_count(self):
        """
        Gets the stale_count of this ProcessGroupDTO.
        The number of stale versioned process groups in the process group.

        :return: The stale_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._stale_count

    @stale_count.setter
    def stale_count(self, stale_count):
        """
        Sets the stale_count of this ProcessGroupDTO.
        The number of stale versioned process groups in the process group.

        :param stale_count: The stale_count of this ProcessGroupDTO.
        :type: int
        """

        self._stale_count = stale_count

    @property
    def locally_modified_and_stale_count(self):
        """
        Gets the locally_modified_and_stale_count of this ProcessGroupDTO.
        The number of locally modified and stale versioned process groups in the process group.

        :return: The locally_modified_and_stale_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._locally_modified_and_stale_count

    @locally_modified_and_stale_count.setter
    def locally_modified_and_stale_count(self, locally_modified_and_stale_count):
        """
        Sets the locally_modified_and_stale_count of this ProcessGroupDTO.
        The number of locally modified and stale versioned process groups in the process group.

        :param locally_modified_and_stale_count: The locally_modified_and_stale_count of this ProcessGroupDTO.
        :type: int
        """

        self._locally_modified_and_stale_count = locally_modified_and_stale_count

    @property
    def sync_failure_count(self):
        """
        Gets the sync_failure_count of this ProcessGroupDTO.
        The number of versioned process groups in the process group that are unable to sync to a registry.

        :return: The sync_failure_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._sync_failure_count

    @sync_failure_count.setter
    def sync_failure_count(self, sync_failure_count):
        """
        Sets the sync_failure_count of this ProcessGroupDTO.
        The number of versioned process groups in the process group that are unable to sync to a registry.

        :param sync_failure_count: The sync_failure_count of this ProcessGroupDTO.
        :type: int
        """

        self._sync_failure_count = sync_failure_count

    @property
    def input_port_count(self):
        """
        Gets the input_port_count of this ProcessGroupDTO.
        The number of input ports in the process group.

        :return: The input_port_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._input_port_count

    @input_port_count.setter
    def input_port_count(self, input_port_count):
        """
        Sets the input_port_count of this ProcessGroupDTO.
        The number of input ports in the process group.

        :param input_port_count: The input_port_count of this ProcessGroupDTO.
        :type: int
        """

        self._input_port_count = input_port_count

    @property
    def output_port_count(self):
        """
        Gets the output_port_count of this ProcessGroupDTO.
        The number of output ports in the process group.

        :return: The output_port_count of this ProcessGroupDTO.
        :rtype: int
        """
        return self._output_port_count

    @output_port_count.setter
    def output_port_count(self, output_port_count):
        """
        Sets the output_port_count of this ProcessGroupDTO.
        The number of output ports in the process group.

        :param output_port_count: The output_port_count of this ProcessGroupDTO.
        :type: int
        """

        self._output_port_count = output_port_count

    @property
    def contents(self):
        """
        Gets the contents of this ProcessGroupDTO.
        The contents of this process group.

        :return: The contents of this ProcessGroupDTO.
        :rtype: FlowSnippetDTO
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """
        Sets the contents of this ProcessGroupDTO.
        The contents of this process group.

        :param contents: The contents of this ProcessGroupDTO.
        :type: FlowSnippetDTO
        """

        self._contents = contents

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
        if not isinstance(other, ProcessGroupDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
