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


class SubmitReplayRequestEntity(object):
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
        'event_id': 'int',
        'cluster_node_id': 'str'
    }

    attribute_map = {
        'event_id': 'eventId',
        'cluster_node_id': 'clusterNodeId'
    }

    def __init__(self, event_id=None, cluster_node_id=None):
        """
        SubmitReplayRequestEntity - a model defined in Swagger
        """

        self._event_id = None
        self._cluster_node_id = None

        if event_id is not None:
          self.event_id = event_id
        if cluster_node_id is not None:
          self.cluster_node_id = cluster_node_id

    @property
    def event_id(self):
        """
        Gets the event_id of this SubmitReplayRequestEntity.
        The event identifier

        :return: The event_id of this SubmitReplayRequestEntity.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """
        Sets the event_id of this SubmitReplayRequestEntity.
        The event identifier

        :param event_id: The event_id of this SubmitReplayRequestEntity.
        :type: int
        """

        self._event_id = event_id

    @property
    def cluster_node_id(self):
        """
        Gets the cluster_node_id of this SubmitReplayRequestEntity.
        The identifier of the node where to submit the replay request.

        :return: The cluster_node_id of this SubmitReplayRequestEntity.
        :rtype: str
        """
        return self._cluster_node_id

    @cluster_node_id.setter
    def cluster_node_id(self, cluster_node_id):
        """
        Sets the cluster_node_id of this SubmitReplayRequestEntity.
        The identifier of the node where to submit the replay request.

        :param cluster_node_id: The cluster_node_id of this SubmitReplayRequestEntity.
        :type: str
        """

        self._cluster_node_id = cluster_node_id

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
        if not isinstance(other, SubmitReplayRequestEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
