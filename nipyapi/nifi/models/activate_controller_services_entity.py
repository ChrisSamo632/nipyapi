"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class ActivateControllerServicesEntity(object):
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
        'state': 'str',
        'components': 'dict(str, RevisionDTO)',
        'disconnected_node_acknowledged': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'components': 'components',
        'disconnected_node_acknowledged': 'disconnectedNodeAcknowledged'
    }

    def __init__(self, id=None, state=None, components=None, disconnected_node_acknowledged=None):
        """
        ActivateControllerServicesEntity - a model defined in Swagger
        """

        self._id = None
        self._state = None
        self._components = None
        self._disconnected_node_acknowledged = None

        if id is not None:
          self.id = id
        if state is not None:
          self.state = state
        if components is not None:
          self.components = components
        if disconnected_node_acknowledged is not None:
          self.disconnected_node_acknowledged = disconnected_node_acknowledged

    @property
    def id(self):
        """
        Gets the id of this ActivateControllerServicesEntity.
        The id of the ProcessGroup

        :return: The id of this ActivateControllerServicesEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ActivateControllerServicesEntity.
        The id of the ProcessGroup

        :param id: The id of this ActivateControllerServicesEntity.
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """
        Gets the state of this ActivateControllerServicesEntity.
        The desired state of the descendant components

        :return: The state of this ActivateControllerServicesEntity.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ActivateControllerServicesEntity.
        The desired state of the descendant components

        :param state: The state of this ActivateControllerServicesEntity.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def components(self):
        """
        Gets the components of this ActivateControllerServicesEntity.
        Optional services to schedule. If not specified, all authorized descendant controller services will be used.

        :return: The components of this ActivateControllerServicesEntity.
        :rtype: dict(str, RevisionDTO)
        """
        return self._components

    @components.setter
    def components(self, components):
        """
        Sets the components of this ActivateControllerServicesEntity.
        Optional services to schedule. If not specified, all authorized descendant controller services will be used.

        :param components: The components of this ActivateControllerServicesEntity.
        :type: dict(str, RevisionDTO)
        """

        self._components = components

    @property
    def disconnected_node_acknowledged(self):
        """
        Gets the disconnected_node_acknowledged of this ActivateControllerServicesEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :return: The disconnected_node_acknowledged of this ActivateControllerServicesEntity.
        :rtype: bool
        """
        return self._disconnected_node_acknowledged

    @disconnected_node_acknowledged.setter
    def disconnected_node_acknowledged(self, disconnected_node_acknowledged):
        """
        Sets the disconnected_node_acknowledged of this ActivateControllerServicesEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :param disconnected_node_acknowledged: The disconnected_node_acknowledged of this ActivateControllerServicesEntity.
        :type: bool
        """

        self._disconnected_node_acknowledged = disconnected_node_acknowledged

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
        if not isinstance(other, ActivateControllerServicesEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
