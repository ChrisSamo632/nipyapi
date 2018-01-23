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


class RemoteProcessGroupStatusSnapshotDTO(object):
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
        'target_uri': 'str',
        'transmission_status': 'str',
        'active_thread_count': 'int',
        'flow_files_sent': 'int',
        'bytes_sent': 'int',
        'sent': 'str',
        'flow_files_received': 'int',
        'bytes_received': 'int',
        'received': 'str'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'groupId',
        'name': 'name',
        'target_uri': 'targetUri',
        'transmission_status': 'transmissionStatus',
        'active_thread_count': 'activeThreadCount',
        'flow_files_sent': 'flowFilesSent',
        'bytes_sent': 'bytesSent',
        'sent': 'sent',
        'flow_files_received': 'flowFilesReceived',
        'bytes_received': 'bytesReceived',
        'received': 'received'
    }

    def __init__(self, id=None, group_id=None, name=None, target_uri=None, transmission_status=None, active_thread_count=None, flow_files_sent=None, bytes_sent=None, sent=None, flow_files_received=None, bytes_received=None, received=None):
        """
        RemoteProcessGroupStatusSnapshotDTO - a model defined in Swagger
        """

        self._id = None
        self._group_id = None
        self._name = None
        self._target_uri = None
        self._transmission_status = None
        self._active_thread_count = None
        self._flow_files_sent = None
        self._bytes_sent = None
        self._sent = None
        self._flow_files_received = None
        self._bytes_received = None
        self._received = None

        if id is not None:
          self.id = id
        if group_id is not None:
          self.group_id = group_id
        if name is not None:
          self.name = name
        if target_uri is not None:
          self.target_uri = target_uri
        if transmission_status is not None:
          self.transmission_status = transmission_status
        if active_thread_count is not None:
          self.active_thread_count = active_thread_count
        if flow_files_sent is not None:
          self.flow_files_sent = flow_files_sent
        if bytes_sent is not None:
          self.bytes_sent = bytes_sent
        if sent is not None:
          self.sent = sent
        if flow_files_received is not None:
          self.flow_files_received = flow_files_received
        if bytes_received is not None:
          self.bytes_received = bytes_received
        if received is not None:
          self.received = received

    @property
    def id(self):
        """
        Gets the id of this RemoteProcessGroupStatusSnapshotDTO.
        The id of the remote process group.

        :return: The id of this RemoteProcessGroupStatusSnapshotDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RemoteProcessGroupStatusSnapshotDTO.
        The id of the remote process group.

        :param id: The id of this RemoteProcessGroupStatusSnapshotDTO.
        :type: str
        """

        self._id = id

    @property
    def group_id(self):
        """
        Gets the group_id of this RemoteProcessGroupStatusSnapshotDTO.
        The id of the parent process group the remote process group resides in.

        :return: The group_id of this RemoteProcessGroupStatusSnapshotDTO.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this RemoteProcessGroupStatusSnapshotDTO.
        The id of the parent process group the remote process group resides in.

        :param group_id: The group_id of this RemoteProcessGroupStatusSnapshotDTO.
        :type: str
        """

        self._group_id = group_id

    @property
    def name(self):
        """
        Gets the name of this RemoteProcessGroupStatusSnapshotDTO.
        The name of the remote process group.

        :return: The name of this RemoteProcessGroupStatusSnapshotDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RemoteProcessGroupStatusSnapshotDTO.
        The name of the remote process group.

        :param name: The name of this RemoteProcessGroupStatusSnapshotDTO.
        :type: str
        """

        self._name = name

    @property
    def target_uri(self):
        """
        Gets the target_uri of this RemoteProcessGroupStatusSnapshotDTO.
        The URI of the target system.

        :return: The target_uri of this RemoteProcessGroupStatusSnapshotDTO.
        :rtype: str
        """
        return self._target_uri

    @target_uri.setter
    def target_uri(self, target_uri):
        """
        Sets the target_uri of this RemoteProcessGroupStatusSnapshotDTO.
        The URI of the target system.

        :param target_uri: The target_uri of this RemoteProcessGroupStatusSnapshotDTO.
        :type: str
        """

        self._target_uri = target_uri

    @property
    def transmission_status(self):
        """
        Gets the transmission_status of this RemoteProcessGroupStatusSnapshotDTO.
        The transmission status of the remote process group.

        :return: The transmission_status of this RemoteProcessGroupStatusSnapshotDTO.
        :rtype: str
        """
        return self._transmission_status

    @transmission_status.setter
    def transmission_status(self, transmission_status):
        """
        Sets the transmission_status of this RemoteProcessGroupStatusSnapshotDTO.
        The transmission status of the remote process group.

        :param transmission_status: The transmission_status of this RemoteProcessGroupStatusSnapshotDTO.
        :type: str
        """

        self._transmission_status = transmission_status

    @property
    def active_thread_count(self):
        """
        Gets the active_thread_count of this RemoteProcessGroupStatusSnapshotDTO.
        The number of active threads for the remote process group.

        :return: The active_thread_count of this RemoteProcessGroupStatusSnapshotDTO.
        :rtype: int
        """
        return self._active_thread_count

    @active_thread_count.setter
    def active_thread_count(self, active_thread_count):
        """
        Sets the active_thread_count of this RemoteProcessGroupStatusSnapshotDTO.
        The number of active threads for the remote process group.

        :param active_thread_count: The active_thread_count of this RemoteProcessGroupStatusSnapshotDTO.
        :type: int
        """

        self._active_thread_count = active_thread_count

    @property
    def flow_files_sent(self):
        """
        Gets the flow_files_sent of this RemoteProcessGroupStatusSnapshotDTO.
        The number of FlowFiles sent to the remote process group in the last 5 minutes.

        :return: The flow_files_sent of this RemoteProcessGroupStatusSnapshotDTO.
        :rtype: int
        """
        return self._flow_files_sent

    @flow_files_sent.setter
    def flow_files_sent(self, flow_files_sent):
        """
        Sets the flow_files_sent of this RemoteProcessGroupStatusSnapshotDTO.
        The number of FlowFiles sent to the remote process group in the last 5 minutes.

        :param flow_files_sent: The flow_files_sent of this RemoteProcessGroupStatusSnapshotDTO.
        :type: int
        """

        self._flow_files_sent = flow_files_sent

    @property
    def bytes_sent(self):
        """
        Gets the bytes_sent of this RemoteProcessGroupStatusSnapshotDTO.
        The size of the FlowFiles sent to the remote process group in the last 5 minutes.

        :return: The bytes_sent of this RemoteProcessGroupStatusSnapshotDTO.
        :rtype: int
        """
        return self._bytes_sent

    @bytes_sent.setter
    def bytes_sent(self, bytes_sent):
        """
        Sets the bytes_sent of this RemoteProcessGroupStatusSnapshotDTO.
        The size of the FlowFiles sent to the remote process group in the last 5 minutes.

        :param bytes_sent: The bytes_sent of this RemoteProcessGroupStatusSnapshotDTO.
        :type: int
        """

        self._bytes_sent = bytes_sent

    @property
    def sent(self):
        """
        Gets the sent of this RemoteProcessGroupStatusSnapshotDTO.
        The count/size of the flowfiles sent to the remote process group in the last 5 minutes.

        :return: The sent of this RemoteProcessGroupStatusSnapshotDTO.
        :rtype: str
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """
        Sets the sent of this RemoteProcessGroupStatusSnapshotDTO.
        The count/size of the flowfiles sent to the remote process group in the last 5 minutes.

        :param sent: The sent of this RemoteProcessGroupStatusSnapshotDTO.
        :type: str
        """

        self._sent = sent

    @property
    def flow_files_received(self):
        """
        Gets the flow_files_received of this RemoteProcessGroupStatusSnapshotDTO.
        The number of FlowFiles received from the remote process group in the last 5 minutes.

        :return: The flow_files_received of this RemoteProcessGroupStatusSnapshotDTO.
        :rtype: int
        """
        return self._flow_files_received

    @flow_files_received.setter
    def flow_files_received(self, flow_files_received):
        """
        Sets the flow_files_received of this RemoteProcessGroupStatusSnapshotDTO.
        The number of FlowFiles received from the remote process group in the last 5 minutes.

        :param flow_files_received: The flow_files_received of this RemoteProcessGroupStatusSnapshotDTO.
        :type: int
        """

        self._flow_files_received = flow_files_received

    @property
    def bytes_received(self):
        """
        Gets the bytes_received of this RemoteProcessGroupStatusSnapshotDTO.
        The size of the FlowFiles received from the remote process group in the last 5 minutes.

        :return: The bytes_received of this RemoteProcessGroupStatusSnapshotDTO.
        :rtype: int
        """
        return self._bytes_received

    @bytes_received.setter
    def bytes_received(self, bytes_received):
        """
        Sets the bytes_received of this RemoteProcessGroupStatusSnapshotDTO.
        The size of the FlowFiles received from the remote process group in the last 5 minutes.

        :param bytes_received: The bytes_received of this RemoteProcessGroupStatusSnapshotDTO.
        :type: int
        """

        self._bytes_received = bytes_received

    @property
    def received(self):
        """
        Gets the received of this RemoteProcessGroupStatusSnapshotDTO.
        The count/size of the flowfiles received from the remote process group in the last 5 minutes.

        :return: The received of this RemoteProcessGroupStatusSnapshotDTO.
        :rtype: str
        """
        return self._received

    @received.setter
    def received(self, received):
        """
        Sets the received of this RemoteProcessGroupStatusSnapshotDTO.
        The count/size of the flowfiles received from the remote process group in the last 5 minutes.

        :param received: The received of this RemoteProcessGroupStatusSnapshotDTO.
        :type: str
        """

        self._received = received

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
        if not isinstance(other, RemoteProcessGroupStatusSnapshotDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
