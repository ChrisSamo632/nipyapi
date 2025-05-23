"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class ActionDTO(object):
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
        'id': 'int',
        'user_identity': 'str',
        'timestamp': 'str',
        'source_id': 'str',
        'source_name': 'str',
        'source_type': 'str',
        'component_details': 'ComponentDetailsDTO',
        'operation': 'str',
        'action_details': 'ActionDetailsDTO'
    }

    attribute_map = {
        'id': 'id',
        'user_identity': 'userIdentity',
        'timestamp': 'timestamp',
        'source_id': 'sourceId',
        'source_name': 'sourceName',
        'source_type': 'sourceType',
        'component_details': 'componentDetails',
        'operation': 'operation',
        'action_details': 'actionDetails'
    }

    def __init__(self, id=None, user_identity=None, timestamp=None, source_id=None, source_name=None, source_type=None, component_details=None, operation=None, action_details=None):
        """
        ActionDTO - a model defined in Swagger
        """

        self._id = None
        self._user_identity = None
        self._timestamp = None
        self._source_id = None
        self._source_name = None
        self._source_type = None
        self._component_details = None
        self._operation = None
        self._action_details = None

        if id is not None:
          self.id = id
        if user_identity is not None:
          self.user_identity = user_identity
        if timestamp is not None:
          self.timestamp = timestamp
        if source_id is not None:
          self.source_id = source_id
        if source_name is not None:
          self.source_name = source_name
        if source_type is not None:
          self.source_type = source_type
        if component_details is not None:
          self.component_details = component_details
        if operation is not None:
          self.operation = operation
        if action_details is not None:
          self.action_details = action_details

    @property
    def id(self):
        """
        Gets the id of this ActionDTO.
        The action id.

        :return: The id of this ActionDTO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ActionDTO.
        The action id.

        :param id: The id of this ActionDTO.
        :type: int
        """

        self._id = id

    @property
    def user_identity(self):
        """
        Gets the user_identity of this ActionDTO.
        The identity of the user that performed the action.

        :return: The user_identity of this ActionDTO.
        :rtype: str
        """
        return self._user_identity

    @user_identity.setter
    def user_identity(self, user_identity):
        """
        Sets the user_identity of this ActionDTO.
        The identity of the user that performed the action.

        :param user_identity: The user_identity of this ActionDTO.
        :type: str
        """

        self._user_identity = user_identity

    @property
    def timestamp(self):
        """
        Gets the timestamp of this ActionDTO.
        The timestamp of the action.

        :return: The timestamp of this ActionDTO.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this ActionDTO.
        The timestamp of the action.

        :param timestamp: The timestamp of this ActionDTO.
        :type: str
        """

        self._timestamp = timestamp

    @property
    def source_id(self):
        """
        Gets the source_id of this ActionDTO.
        The id of the source component.

        :return: The source_id of this ActionDTO.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this ActionDTO.
        The id of the source component.

        :param source_id: The source_id of this ActionDTO.
        :type: str
        """

        self._source_id = source_id

    @property
    def source_name(self):
        """
        Gets the source_name of this ActionDTO.
        The name of the source component.

        :return: The source_name of this ActionDTO.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this ActionDTO.
        The name of the source component.

        :param source_name: The source_name of this ActionDTO.
        :type: str
        """

        self._source_name = source_name

    @property
    def source_type(self):
        """
        Gets the source_type of this ActionDTO.
        The type of the source component.

        :return: The source_type of this ActionDTO.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this ActionDTO.
        The type of the source component.

        :param source_type: The source_type of this ActionDTO.
        :type: str
        """

        self._source_type = source_type

    @property
    def component_details(self):
        """
        Gets the component_details of this ActionDTO.
        The details of the source component.

        :return: The component_details of this ActionDTO.
        :rtype: ComponentDetailsDTO
        """
        return self._component_details

    @component_details.setter
    def component_details(self, component_details):
        """
        Sets the component_details of this ActionDTO.
        The details of the source component.

        :param component_details: The component_details of this ActionDTO.
        :type: ComponentDetailsDTO
        """

        self._component_details = component_details

    @property
    def operation(self):
        """
        Gets the operation of this ActionDTO.
        The operation that was performed.

        :return: The operation of this ActionDTO.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this ActionDTO.
        The operation that was performed.

        :param operation: The operation of this ActionDTO.
        :type: str
        """

        self._operation = operation

    @property
    def action_details(self):
        """
        Gets the action_details of this ActionDTO.
        The details of the action.

        :return: The action_details of this ActionDTO.
        :rtype: ActionDetailsDTO
        """
        return self._action_details

    @action_details.setter
    def action_details(self, action_details):
        """
        Sets the action_details of this ActionDTO.
        The details of the action.

        :param action_details: The action_details of this ActionDTO.
        :type: ActionDetailsDTO
        """

        self._action_details = action_details

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
        if not isinstance(other, ActionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
