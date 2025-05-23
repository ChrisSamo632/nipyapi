"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class UpdateControllerServiceReferenceRequestEntity(object):
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
        'referencing_component_revisions': 'dict(str, RevisionDTO)',
        'disconnected_node_acknowledged': 'bool',
        'ui_only': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'state': 'state',
        'referencing_component_revisions': 'referencingComponentRevisions',
        'disconnected_node_acknowledged': 'disconnectedNodeAcknowledged',
        'ui_only': 'uiOnly'
    }

    def __init__(self, id=None, state=None, referencing_component_revisions=None, disconnected_node_acknowledged=None, ui_only=None):
        """
        UpdateControllerServiceReferenceRequestEntity - a model defined in Swagger
        """

        self._id = None
        self._state = None
        self._referencing_component_revisions = None
        self._disconnected_node_acknowledged = None
        self._ui_only = None

        if id is not None:
          self.id = id
        if state is not None:
          self.state = state
        if referencing_component_revisions is not None:
          self.referencing_component_revisions = referencing_component_revisions
        if disconnected_node_acknowledged is not None:
          self.disconnected_node_acknowledged = disconnected_node_acknowledged
        if ui_only is not None:
          self.ui_only = ui_only

    @property
    def id(self):
        """
        Gets the id of this UpdateControllerServiceReferenceRequestEntity.
        The identifier of the Controller Service.

        :return: The id of this UpdateControllerServiceReferenceRequestEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UpdateControllerServiceReferenceRequestEntity.
        The identifier of the Controller Service.

        :param id: The id of this UpdateControllerServiceReferenceRequestEntity.
        :type: str
        """

        self._id = id

    @property
    def state(self):
        """
        Gets the state of this UpdateControllerServiceReferenceRequestEntity.
        The new state of the references for the controller service.

        :return: The state of this UpdateControllerServiceReferenceRequestEntity.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this UpdateControllerServiceReferenceRequestEntity.
        The new state of the references for the controller service.

        :param state: The state of this UpdateControllerServiceReferenceRequestEntity.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "RUNNING", "STOPPED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def referencing_component_revisions(self):
        """
        Gets the referencing_component_revisions of this UpdateControllerServiceReferenceRequestEntity.
        The revisions for all referencing components.

        :return: The referencing_component_revisions of this UpdateControllerServiceReferenceRequestEntity.
        :rtype: dict(str, RevisionDTO)
        """
        return self._referencing_component_revisions

    @referencing_component_revisions.setter
    def referencing_component_revisions(self, referencing_component_revisions):
        """
        Sets the referencing_component_revisions of this UpdateControllerServiceReferenceRequestEntity.
        The revisions for all referencing components.

        :param referencing_component_revisions: The referencing_component_revisions of this UpdateControllerServiceReferenceRequestEntity.
        :type: dict(str, RevisionDTO)
        """

        self._referencing_component_revisions = referencing_component_revisions

    @property
    def disconnected_node_acknowledged(self):
        """
        Gets the disconnected_node_acknowledged of this UpdateControllerServiceReferenceRequestEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :return: The disconnected_node_acknowledged of this UpdateControllerServiceReferenceRequestEntity.
        :rtype: bool
        """
        return self._disconnected_node_acknowledged

    @disconnected_node_acknowledged.setter
    def disconnected_node_acknowledged(self, disconnected_node_acknowledged):
        """
        Sets the disconnected_node_acknowledged of this UpdateControllerServiceReferenceRequestEntity.
        Acknowledges that this node is disconnected to allow for mutable requests to proceed.

        :param disconnected_node_acknowledged: The disconnected_node_acknowledged of this UpdateControllerServiceReferenceRequestEntity.
        :type: bool
        """

        self._disconnected_node_acknowledged = disconnected_node_acknowledged

    @property
    def ui_only(self):
        """
        Gets the ui_only of this UpdateControllerServiceReferenceRequestEntity.
        Indicates whether or not the response should only include fields necessary for rendering the NiFi User Interface. As such, when this value is set to true, some fields may be returned as null values, and the selected fields may change at any time without notice. As a result, this value should not be set to true by any client other than the UI.

        :return: The ui_only of this UpdateControllerServiceReferenceRequestEntity.
        :rtype: bool
        """
        return self._ui_only

    @ui_only.setter
    def ui_only(self, ui_only):
        """
        Sets the ui_only of this UpdateControllerServiceReferenceRequestEntity.
        Indicates whether or not the response should only include fields necessary for rendering the NiFi User Interface. As such, when this value is set to true, some fields may be returned as null values, and the selected fields may change at any time without notice. As a result, this value should not be set to true by any client other than the UI.

        :param ui_only: The ui_only of this UpdateControllerServiceReferenceRequestEntity.
        :type: bool
        """

        self._ui_only = ui_only

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
        if not isinstance(other, UpdateControllerServiceReferenceRequestEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
