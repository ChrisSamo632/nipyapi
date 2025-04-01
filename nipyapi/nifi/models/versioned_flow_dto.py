"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class VersionedFlowDTO(object):
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
        'registry_id': 'str',
        'bucket_id': 'str',
        'flow_id': 'str',
        'flow_name': 'str',
        'description': 'str',
        'comments': 'str',
        'action': 'str'
    }

    attribute_map = {
        'registry_id': 'registryId',
        'bucket_id': 'bucketId',
        'flow_id': 'flowId',
        'flow_name': 'flowName',
        'description': 'description',
        'comments': 'comments',
        'action': 'action'
    }

    def __init__(self, registry_id=None, bucket_id=None, flow_id=None, flow_name=None, description=None, comments=None, action=None):
        """
        VersionedFlowDTO - a model defined in Swagger
        """

        self._registry_id = None
        self._bucket_id = None
        self._flow_id = None
        self._flow_name = None
        self._description = None
        self._comments = None
        self._action = None

        if registry_id is not None:
          self.registry_id = registry_id
        if bucket_id is not None:
          self.bucket_id = bucket_id
        if flow_id is not None:
          self.flow_id = flow_id
        if flow_name is not None:
          self.flow_name = flow_name
        if description is not None:
          self.description = description
        if comments is not None:
          self.comments = comments
        if action is not None:
          self.action = action

    @property
    def registry_id(self):
        """
        Gets the registry_id of this VersionedFlowDTO.
        The ID of the registry that the flow is tracked to

        :return: The registry_id of this VersionedFlowDTO.
        :rtype: str
        """
        return self._registry_id

    @registry_id.setter
    def registry_id(self, registry_id):
        """
        Sets the registry_id of this VersionedFlowDTO.
        The ID of the registry that the flow is tracked to

        :param registry_id: The registry_id of this VersionedFlowDTO.
        :type: str
        """

        self._registry_id = registry_id

    @property
    def bucket_id(self):
        """
        Gets the bucket_id of this VersionedFlowDTO.
        The ID of the bucket where the flow is stored

        :return: The bucket_id of this VersionedFlowDTO.
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """
        Sets the bucket_id of this VersionedFlowDTO.
        The ID of the bucket where the flow is stored

        :param bucket_id: The bucket_id of this VersionedFlowDTO.
        :type: str
        """

        self._bucket_id = bucket_id

    @property
    def flow_id(self):
        """
        Gets the flow_id of this VersionedFlowDTO.
        The ID of the flow

        :return: The flow_id of this VersionedFlowDTO.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        """
        Sets the flow_id of this VersionedFlowDTO.
        The ID of the flow

        :param flow_id: The flow_id of this VersionedFlowDTO.
        :type: str
        """

        self._flow_id = flow_id

    @property
    def flow_name(self):
        """
        Gets the flow_name of this VersionedFlowDTO.
        The name of the flow

        :return: The flow_name of this VersionedFlowDTO.
        :rtype: str
        """
        return self._flow_name

    @flow_name.setter
    def flow_name(self, flow_name):
        """
        Sets the flow_name of this VersionedFlowDTO.
        The name of the flow

        :param flow_name: The flow_name of this VersionedFlowDTO.
        :type: str
        """

        self._flow_name = flow_name

    @property
    def description(self):
        """
        Gets the description of this VersionedFlowDTO.
        A description of the flow

        :return: The description of this VersionedFlowDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this VersionedFlowDTO.
        A description of the flow

        :param description: The description of this VersionedFlowDTO.
        :type: str
        """

        self._description = description

    @property
    def comments(self):
        """
        Gets the comments of this VersionedFlowDTO.
        Comments for the changeset

        :return: The comments of this VersionedFlowDTO.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this VersionedFlowDTO.
        Comments for the changeset

        :param comments: The comments of this VersionedFlowDTO.
        :type: str
        """

        self._comments = comments

    @property
    def action(self):
        """
        Gets the action of this VersionedFlowDTO.
        The action being performed

        :return: The action of this VersionedFlowDTO.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this VersionedFlowDTO.
        The action being performed

        :param action: The action of this VersionedFlowDTO.
        :type: str
        """
        allowed_values = ["COMMIT", "FORCE_COMMIT"]
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"
                .format(action, allowed_values)
            )

        self._action = action

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
        if not isinstance(other, VersionedFlowDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
