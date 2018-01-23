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


class ProcessGroupFlowDTO(object):
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
        'uri': 'str',
        'parent_group_id': 'str',
        'breadcrumb': 'FlowBreadcrumbEntity',
        'flow': 'FlowDTO',
        'last_refreshed': 'str'
    }

    attribute_map = {
        'id': 'id',
        'uri': 'uri',
        'parent_group_id': 'parentGroupId',
        'breadcrumb': 'breadcrumb',
        'flow': 'flow',
        'last_refreshed': 'lastRefreshed'
    }

    def __init__(self, id=None, uri=None, parent_group_id=None, breadcrumb=None, flow=None, last_refreshed=None):
        """
        ProcessGroupFlowDTO - a model defined in Swagger
        """

        self._id = None
        self._uri = None
        self._parent_group_id = None
        self._breadcrumb = None
        self._flow = None
        self._last_refreshed = None

        if id is not None:
          self.id = id
        if uri is not None:
          self.uri = uri
        if parent_group_id is not None:
          self.parent_group_id = parent_group_id
        if breadcrumb is not None:
          self.breadcrumb = breadcrumb
        if flow is not None:
          self.flow = flow
        if last_refreshed is not None:
          self.last_refreshed = last_refreshed

    @property
    def id(self):
        """
        Gets the id of this ProcessGroupFlowDTO.
        The id of the component.

        :return: The id of this ProcessGroupFlowDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProcessGroupFlowDTO.
        The id of the component.

        :param id: The id of this ProcessGroupFlowDTO.
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """
        Gets the uri of this ProcessGroupFlowDTO.
        The URI for futures requests to the component.

        :return: The uri of this ProcessGroupFlowDTO.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this ProcessGroupFlowDTO.
        The URI for futures requests to the component.

        :param uri: The uri of this ProcessGroupFlowDTO.
        :type: str
        """

        self._uri = uri

    @property
    def parent_group_id(self):
        """
        Gets the parent_group_id of this ProcessGroupFlowDTO.
        The id of parent process group of this component if applicable.

        :return: The parent_group_id of this ProcessGroupFlowDTO.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """
        Sets the parent_group_id of this ProcessGroupFlowDTO.
        The id of parent process group of this component if applicable.

        :param parent_group_id: The parent_group_id of this ProcessGroupFlowDTO.
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def breadcrumb(self):
        """
        Gets the breadcrumb of this ProcessGroupFlowDTO.
        The breadcrumb of the process group.

        :return: The breadcrumb of this ProcessGroupFlowDTO.
        :rtype: FlowBreadcrumbEntity
        """
        return self._breadcrumb

    @breadcrumb.setter
    def breadcrumb(self, breadcrumb):
        """
        Sets the breadcrumb of this ProcessGroupFlowDTO.
        The breadcrumb of the process group.

        :param breadcrumb: The breadcrumb of this ProcessGroupFlowDTO.
        :type: FlowBreadcrumbEntity
        """

        self._breadcrumb = breadcrumb

    @property
    def flow(self):
        """
        Gets the flow of this ProcessGroupFlowDTO.
        The flow structure starting at this Process Group.

        :return: The flow of this ProcessGroupFlowDTO.
        :rtype: FlowDTO
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """
        Sets the flow of this ProcessGroupFlowDTO.
        The flow structure starting at this Process Group.

        :param flow: The flow of this ProcessGroupFlowDTO.
        :type: FlowDTO
        """

        self._flow = flow

    @property
    def last_refreshed(self):
        """
        Gets the last_refreshed of this ProcessGroupFlowDTO.
        The time the flow for the process group was last refreshed.

        :return: The last_refreshed of this ProcessGroupFlowDTO.
        :rtype: str
        """
        return self._last_refreshed

    @last_refreshed.setter
    def last_refreshed(self, last_refreshed):
        """
        Sets the last_refreshed of this ProcessGroupFlowDTO.
        The time the flow for the process group was last refreshed.

        :param last_refreshed: The last_refreshed of this ProcessGroupFlowDTO.
        :type: str
        """

        self._last_refreshed = last_refreshed

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
        if not isinstance(other, ProcessGroupFlowDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
