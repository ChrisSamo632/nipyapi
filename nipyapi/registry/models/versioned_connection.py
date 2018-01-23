# coding: utf-8

"""
    NiFi Registry REST API

    The Rest Api provides an interface to a registry with operations for saving,                                             versioning, reading NiFi flows                                             and components.

    OpenAPI spec version: 0.1.1-SNAPSHOT
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VersionedConnection(object):
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
        'identifier': 'str',
        'name': 'str',
        'comments': 'str',
        'position': 'ThePositionOfAComponentOnTheGraph',
        'source': 'ConnectableComponent',
        'destination': 'ConnectableComponent',
        'label_index': 'int',
        'getz_index': 'int',
        'selected_relationships': 'list[str]',
        'back_pressure_object_threshold': 'int',
        'back_pressure_data_size_threshold': 'str',
        'flow_file_expiration': 'str',
        'prioritizers': 'list[str]',
        'bends': 'list[ThePositionOfAComponentOnTheGraph]',
        'component_type': 'str',
        'group_identifier': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'name': 'name',
        'comments': 'comments',
        'position': 'position',
        'source': 'source',
        'destination': 'destination',
        'label_index': 'labelIndex',
        'getz_index': 'getzIndex',
        'selected_relationships': 'selectedRelationships',
        'back_pressure_object_threshold': 'backPressureObjectThreshold',
        'back_pressure_data_size_threshold': 'backPressureDataSizeThreshold',
        'flow_file_expiration': 'flowFileExpiration',
        'prioritizers': 'prioritizers',
        'bends': 'bends',
        'component_type': 'componentType',
        'group_identifier': 'groupIdentifier'
    }

    def __init__(self, identifier=None, name=None, comments=None, position=None, source=None, destination=None, label_index=None, getz_index=None, selected_relationships=None, back_pressure_object_threshold=None, back_pressure_data_size_threshold=None, flow_file_expiration=None, prioritizers=None, bends=None, component_type=None, group_identifier=None):
        """
        VersionedConnection - a model defined in Swagger
        """

        self._identifier = None
        self._name = None
        self._comments = None
        self._position = None
        self._source = None
        self._destination = None
        self._label_index = None
        self._getz_index = None
        self._selected_relationships = None
        self._back_pressure_object_threshold = None
        self._back_pressure_data_size_threshold = None
        self._flow_file_expiration = None
        self._prioritizers = None
        self._bends = None
        self._component_type = None
        self._group_identifier = None

        if identifier is not None:
          self.identifier = identifier
        if name is not None:
          self.name = name
        if comments is not None:
          self.comments = comments
        if position is not None:
          self.position = position
        if source is not None:
          self.source = source
        if destination is not None:
          self.destination = destination
        if label_index is not None:
          self.label_index = label_index
        if getz_index is not None:
          self.getz_index = getz_index
        if selected_relationships is not None:
          self.selected_relationships = selected_relationships
        if back_pressure_object_threshold is not None:
          self.back_pressure_object_threshold = back_pressure_object_threshold
        if back_pressure_data_size_threshold is not None:
          self.back_pressure_data_size_threshold = back_pressure_data_size_threshold
        if flow_file_expiration is not None:
          self.flow_file_expiration = flow_file_expiration
        if prioritizers is not None:
          self.prioritizers = prioritizers
        if bends is not None:
          self.bends = bends
        if component_type is not None:
          self.component_type = component_type
        if group_identifier is not None:
          self.group_identifier = group_identifier

    @property
    def identifier(self):
        """
        Gets the identifier of this VersionedConnection.
        The component's unique identifier

        :return: The identifier of this VersionedConnection.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this VersionedConnection.
        The component's unique identifier

        :param identifier: The identifier of this VersionedConnection.
        :type: str
        """

        self._identifier = identifier

    @property
    def name(self):
        """
        Gets the name of this VersionedConnection.
        The component's name

        :return: The name of this VersionedConnection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VersionedConnection.
        The component's name

        :param name: The name of this VersionedConnection.
        :type: str
        """

        self._name = name

    @property
    def comments(self):
        """
        Gets the comments of this VersionedConnection.
        The user-supplied comments for the component

        :return: The comments of this VersionedConnection.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this VersionedConnection.
        The user-supplied comments for the component

        :param comments: The comments of this VersionedConnection.
        :type: str
        """

        self._comments = comments

    @property
    def position(self):
        """
        Gets the position of this VersionedConnection.
        The component's position on the graph

        :return: The position of this VersionedConnection.
        :rtype: ThePositionOfAComponentOnTheGraph
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this VersionedConnection.
        The component's position on the graph

        :param position: The position of this VersionedConnection.
        :type: ThePositionOfAComponentOnTheGraph
        """

        self._position = position

    @property
    def source(self):
        """
        Gets the source of this VersionedConnection.
        The source of the connection.

        :return: The source of this VersionedConnection.
        :rtype: ConnectableComponent
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this VersionedConnection.
        The source of the connection.

        :param source: The source of this VersionedConnection.
        :type: ConnectableComponent
        """

        self._source = source

    @property
    def destination(self):
        """
        Gets the destination of this VersionedConnection.
        The destination of the connection.

        :return: The destination of this VersionedConnection.
        :rtype: ConnectableComponent
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this VersionedConnection.
        The destination of the connection.

        :param destination: The destination of this VersionedConnection.
        :type: ConnectableComponent
        """

        self._destination = destination

    @property
    def label_index(self):
        """
        Gets the label_index of this VersionedConnection.
        The index of the bend point where to place the connection label.

        :return: The label_index of this VersionedConnection.
        :rtype: int
        """
        return self._label_index

    @label_index.setter
    def label_index(self, label_index):
        """
        Sets the label_index of this VersionedConnection.
        The index of the bend point where to place the connection label.

        :param label_index: The label_index of this VersionedConnection.
        :type: int
        """

        self._label_index = label_index

    @property
    def getz_index(self):
        """
        Gets the getz_index of this VersionedConnection.
        The z index of the connection.

        :return: The getz_index of this VersionedConnection.
        :rtype: int
        """
        return self._getz_index

    @getz_index.setter
    def getz_index(self, getz_index):
        """
        Sets the getz_index of this VersionedConnection.
        The z index of the connection.

        :param getz_index: The getz_index of this VersionedConnection.
        :type: int
        """

        self._getz_index = getz_index

    @property
    def selected_relationships(self):
        """
        Gets the selected_relationships of this VersionedConnection.
        The selected relationship that comprise the connection.

        :return: The selected_relationships of this VersionedConnection.
        :rtype: list[str]
        """
        return self._selected_relationships

    @selected_relationships.setter
    def selected_relationships(self, selected_relationships):
        """
        Sets the selected_relationships of this VersionedConnection.
        The selected relationship that comprise the connection.

        :param selected_relationships: The selected_relationships of this VersionedConnection.
        :type: list[str]
        """

        self._selected_relationships = selected_relationships

    @property
    def back_pressure_object_threshold(self):
        """
        Gets the back_pressure_object_threshold of this VersionedConnection.
        The object count threshold for determining when back pressure is applied. Updating this value is a passive change in the sense that it won't impact whether existing files over the limit are affected but it does help feeder processors to stop pushing too much into this work queue.

        :return: The back_pressure_object_threshold of this VersionedConnection.
        :rtype: int
        """
        return self._back_pressure_object_threshold

    @back_pressure_object_threshold.setter
    def back_pressure_object_threshold(self, back_pressure_object_threshold):
        """
        Sets the back_pressure_object_threshold of this VersionedConnection.
        The object count threshold for determining when back pressure is applied. Updating this value is a passive change in the sense that it won't impact whether existing files over the limit are affected but it does help feeder processors to stop pushing too much into this work queue.

        :param back_pressure_object_threshold: The back_pressure_object_threshold of this VersionedConnection.
        :type: int
        """

        self._back_pressure_object_threshold = back_pressure_object_threshold

    @property
    def back_pressure_data_size_threshold(self):
        """
        Gets the back_pressure_data_size_threshold of this VersionedConnection.
        The object data size threshold for determining when back pressure is applied. Updating this value is a passive change in the sense that it won't impact whether existing files over the limit are affected but it does help feeder processors to stop pushing too much into this work queue.

        :return: The back_pressure_data_size_threshold of this VersionedConnection.
        :rtype: str
        """
        return self._back_pressure_data_size_threshold

    @back_pressure_data_size_threshold.setter
    def back_pressure_data_size_threshold(self, back_pressure_data_size_threshold):
        """
        Sets the back_pressure_data_size_threshold of this VersionedConnection.
        The object data size threshold for determining when back pressure is applied. Updating this value is a passive change in the sense that it won't impact whether existing files over the limit are affected but it does help feeder processors to stop pushing too much into this work queue.

        :param back_pressure_data_size_threshold: The back_pressure_data_size_threshold of this VersionedConnection.
        :type: str
        """

        self._back_pressure_data_size_threshold = back_pressure_data_size_threshold

    @property
    def flow_file_expiration(self):
        """
        Gets the flow_file_expiration of this VersionedConnection.
        The amount of time a flow file may be in the flow before it will be automatically aged out of the flow. Once a flow file reaches this age it will be terminated from the flow the next time a processor attempts to start work on it.

        :return: The flow_file_expiration of this VersionedConnection.
        :rtype: str
        """
        return self._flow_file_expiration

    @flow_file_expiration.setter
    def flow_file_expiration(self, flow_file_expiration):
        """
        Sets the flow_file_expiration of this VersionedConnection.
        The amount of time a flow file may be in the flow before it will be automatically aged out of the flow. Once a flow file reaches this age it will be terminated from the flow the next time a processor attempts to start work on it.

        :param flow_file_expiration: The flow_file_expiration of this VersionedConnection.
        :type: str
        """

        self._flow_file_expiration = flow_file_expiration

    @property
    def prioritizers(self):
        """
        Gets the prioritizers of this VersionedConnection.
        The comparators used to prioritize the queue.

        :return: The prioritizers of this VersionedConnection.
        :rtype: list[str]
        """
        return self._prioritizers

    @prioritizers.setter
    def prioritizers(self, prioritizers):
        """
        Sets the prioritizers of this VersionedConnection.
        The comparators used to prioritize the queue.

        :param prioritizers: The prioritizers of this VersionedConnection.
        :type: list[str]
        """

        self._prioritizers = prioritizers

    @property
    def bends(self):
        """
        Gets the bends of this VersionedConnection.
        The bend points on the connection.

        :return: The bends of this VersionedConnection.
        :rtype: list[ThePositionOfAComponentOnTheGraph]
        """
        return self._bends

    @bends.setter
    def bends(self, bends):
        """
        Sets the bends of this VersionedConnection.
        The bend points on the connection.

        :param bends: The bends of this VersionedConnection.
        :type: list[ThePositionOfAComponentOnTheGraph]
        """

        self._bends = bends

    @property
    def component_type(self):
        """
        Gets the component_type of this VersionedConnection.

        :return: The component_type of this VersionedConnection.
        :rtype: str
        """
        return self._component_type

    @component_type.setter
    def component_type(self, component_type):
        """
        Sets the component_type of this VersionedConnection.

        :param component_type: The component_type of this VersionedConnection.
        :type: str
        """
        allowed_values = ["CONNECTION", "PROCESSOR", "PROCESS_GROUP", "REMOTE_PROCESS_GROUP", "INPUT_PORT", "OUTPUT_PORT", "REMOTE_INPUT_PORT", "REMOTE_OUTPUT_PORT", "FUNNEL", "LABEL", "CONTROLLER_SERVICE"]
        if component_type not in allowed_values:
            raise ValueError(
                "Invalid value for `component_type` ({0}), must be one of {1}"
                .format(component_type, allowed_values)
            )

        self._component_type = component_type

    @property
    def group_identifier(self):
        """
        Gets the group_identifier of this VersionedConnection.
        The ID of the Process Group that this component belongs to

        :return: The group_identifier of this VersionedConnection.
        :rtype: str
        """
        return self._group_identifier

    @group_identifier.setter
    def group_identifier(self, group_identifier):
        """
        Sets the group_identifier of this VersionedConnection.
        The ID of the Process Group that this component belongs to

        :param group_identifier: The group_identifier of this VersionedConnection.
        :type: str
        """

        self._group_identifier = group_identifier

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
        if not isinstance(other, VersionedConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
