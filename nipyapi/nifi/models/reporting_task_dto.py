"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class ReportingTaskDTO(object):
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
        'type': 'str',
        'bundle': 'BundleDTO',
        'state': 'str',
        'comments': 'str',
        'persists_state': 'bool',
        'restricted': 'bool',
        'deprecated': 'bool',
        'multiple_versions_available': 'bool',
        'supports_sensitive_dynamic_properties': 'bool',
        'scheduling_period': 'str',
        'scheduling_strategy': 'str',
        'default_scheduling_period': 'dict(str, str)',
        'properties': 'dict(str, str)',
        'descriptors': 'dict(str, PropertyDescriptorDTO)',
        'sensitive_dynamic_property_names': 'list[str]',
        'custom_ui_url': 'str',
        'annotation_data': 'str',
        'validation_errors': 'list[str]',
        'validation_status': 'str',
        'active_thread_count': 'int',
        'extension_missing': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'versioned_component_id': 'versionedComponentId',
        'parent_group_id': 'parentGroupId',
        'position': 'position',
        'name': 'name',
        'type': 'type',
        'bundle': 'bundle',
        'state': 'state',
        'comments': 'comments',
        'persists_state': 'persistsState',
        'restricted': 'restricted',
        'deprecated': 'deprecated',
        'multiple_versions_available': 'multipleVersionsAvailable',
        'supports_sensitive_dynamic_properties': 'supportsSensitiveDynamicProperties',
        'scheduling_period': 'schedulingPeriod',
        'scheduling_strategy': 'schedulingStrategy',
        'default_scheduling_period': 'defaultSchedulingPeriod',
        'properties': 'properties',
        'descriptors': 'descriptors',
        'sensitive_dynamic_property_names': 'sensitiveDynamicPropertyNames',
        'custom_ui_url': 'customUiUrl',
        'annotation_data': 'annotationData',
        'validation_errors': 'validationErrors',
        'validation_status': 'validationStatus',
        'active_thread_count': 'activeThreadCount',
        'extension_missing': 'extensionMissing'
    }

    def __init__(self, id=None, versioned_component_id=None, parent_group_id=None, position=None, name=None, type=None, bundle=None, state=None, comments=None, persists_state=None, restricted=None, deprecated=None, multiple_versions_available=None, supports_sensitive_dynamic_properties=None, scheduling_period=None, scheduling_strategy=None, default_scheduling_period=None, properties=None, descriptors=None, sensitive_dynamic_property_names=None, custom_ui_url=None, annotation_data=None, validation_errors=None, validation_status=None, active_thread_count=None, extension_missing=None):
        """
        ReportingTaskDTO - a model defined in Swagger
        """

        self._id = None
        self._versioned_component_id = None
        self._parent_group_id = None
        self._position = None
        self._name = None
        self._type = None
        self._bundle = None
        self._state = None
        self._comments = None
        self._persists_state = None
        self._restricted = None
        self._deprecated = None
        self._multiple_versions_available = None
        self._supports_sensitive_dynamic_properties = None
        self._scheduling_period = None
        self._scheduling_strategy = None
        self._default_scheduling_period = None
        self._properties = None
        self._descriptors = None
        self._sensitive_dynamic_property_names = None
        self._custom_ui_url = None
        self._annotation_data = None
        self._validation_errors = None
        self._validation_status = None
        self._active_thread_count = None
        self._extension_missing = None

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
        if type is not None:
          self.type = type
        if bundle is not None:
          self.bundle = bundle
        if state is not None:
          self.state = state
        if comments is not None:
          self.comments = comments
        if persists_state is not None:
          self.persists_state = persists_state
        if restricted is not None:
          self.restricted = restricted
        if deprecated is not None:
          self.deprecated = deprecated
        if multiple_versions_available is not None:
          self.multiple_versions_available = multiple_versions_available
        if supports_sensitive_dynamic_properties is not None:
          self.supports_sensitive_dynamic_properties = supports_sensitive_dynamic_properties
        if scheduling_period is not None:
          self.scheduling_period = scheduling_period
        if scheduling_strategy is not None:
          self.scheduling_strategy = scheduling_strategy
        if default_scheduling_period is not None:
          self.default_scheduling_period = default_scheduling_period
        if properties is not None:
          self.properties = properties
        if descriptors is not None:
          self.descriptors = descriptors
        if sensitive_dynamic_property_names is not None:
          self.sensitive_dynamic_property_names = sensitive_dynamic_property_names
        if custom_ui_url is not None:
          self.custom_ui_url = custom_ui_url
        if annotation_data is not None:
          self.annotation_data = annotation_data
        if validation_errors is not None:
          self.validation_errors = validation_errors
        if validation_status is not None:
          self.validation_status = validation_status
        if active_thread_count is not None:
          self.active_thread_count = active_thread_count
        if extension_missing is not None:
          self.extension_missing = extension_missing

    @property
    def id(self):
        """
        Gets the id of this ReportingTaskDTO.
        The id of the component.

        :return: The id of this ReportingTaskDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ReportingTaskDTO.
        The id of the component.

        :param id: The id of this ReportingTaskDTO.
        :type: str
        """

        self._id = id

    @property
    def versioned_component_id(self):
        """
        Gets the versioned_component_id of this ReportingTaskDTO.
        The ID of the corresponding component that is under version control

        :return: The versioned_component_id of this ReportingTaskDTO.
        :rtype: str
        """
        return self._versioned_component_id

    @versioned_component_id.setter
    def versioned_component_id(self, versioned_component_id):
        """
        Sets the versioned_component_id of this ReportingTaskDTO.
        The ID of the corresponding component that is under version control

        :param versioned_component_id: The versioned_component_id of this ReportingTaskDTO.
        :type: str
        """

        self._versioned_component_id = versioned_component_id

    @property
    def parent_group_id(self):
        """
        Gets the parent_group_id of this ReportingTaskDTO.
        The id of parent process group of this component if applicable.

        :return: The parent_group_id of this ReportingTaskDTO.
        :rtype: str
        """
        return self._parent_group_id

    @parent_group_id.setter
    def parent_group_id(self, parent_group_id):
        """
        Sets the parent_group_id of this ReportingTaskDTO.
        The id of parent process group of this component if applicable.

        :param parent_group_id: The parent_group_id of this ReportingTaskDTO.
        :type: str
        """

        self._parent_group_id = parent_group_id

    @property
    def position(self):
        """
        Gets the position of this ReportingTaskDTO.
        The position of this component in the UI if applicable.

        :return: The position of this ReportingTaskDTO.
        :rtype: PositionDTO
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ReportingTaskDTO.
        The position of this component in the UI if applicable.

        :param position: The position of this ReportingTaskDTO.
        :type: PositionDTO
        """

        self._position = position

    @property
    def name(self):
        """
        Gets the name of this ReportingTaskDTO.
        The name of the reporting task.

        :return: The name of this ReportingTaskDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReportingTaskDTO.
        The name of the reporting task.

        :param name: The name of this ReportingTaskDTO.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this ReportingTaskDTO.
        The fully qualified type of the reporting task.

        :return: The type of this ReportingTaskDTO.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ReportingTaskDTO.
        The fully qualified type of the reporting task.

        :param type: The type of this ReportingTaskDTO.
        :type: str
        """

        self._type = type

    @property
    def bundle(self):
        """
        Gets the bundle of this ReportingTaskDTO.
        The details of the artifact that bundled this reporting task type.

        :return: The bundle of this ReportingTaskDTO.
        :rtype: BundleDTO
        """
        return self._bundle

    @bundle.setter
    def bundle(self, bundle):
        """
        Sets the bundle of this ReportingTaskDTO.
        The details of the artifact that bundled this reporting task type.

        :param bundle: The bundle of this ReportingTaskDTO.
        :type: BundleDTO
        """

        self._bundle = bundle

    @property
    def state(self):
        """
        Gets the state of this ReportingTaskDTO.
        The state of the reporting task.

        :return: The state of this ReportingTaskDTO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ReportingTaskDTO.
        The state of the reporting task.

        :param state: The state of this ReportingTaskDTO.
        :type: str
        """
        allowed_values = ["RUNNING", "STOPPED", "DISABLED"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def comments(self):
        """
        Gets the comments of this ReportingTaskDTO.
        The comments of the reporting task.

        :return: The comments of this ReportingTaskDTO.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this ReportingTaskDTO.
        The comments of the reporting task.

        :param comments: The comments of this ReportingTaskDTO.
        :type: str
        """

        self._comments = comments

    @property
    def persists_state(self):
        """
        Gets the persists_state of this ReportingTaskDTO.
        Whether the reporting task persists state.

        :return: The persists_state of this ReportingTaskDTO.
        :rtype: bool
        """
        return self._persists_state

    @persists_state.setter
    def persists_state(self, persists_state):
        """
        Sets the persists_state of this ReportingTaskDTO.
        Whether the reporting task persists state.

        :param persists_state: The persists_state of this ReportingTaskDTO.
        :type: bool
        """

        self._persists_state = persists_state

    @property
    def restricted(self):
        """
        Gets the restricted of this ReportingTaskDTO.
        Whether the reporting task requires elevated privileges.

        :return: The restricted of this ReportingTaskDTO.
        :rtype: bool
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """
        Sets the restricted of this ReportingTaskDTO.
        Whether the reporting task requires elevated privileges.

        :param restricted: The restricted of this ReportingTaskDTO.
        :type: bool
        """

        self._restricted = restricted

    @property
    def deprecated(self):
        """
        Gets the deprecated of this ReportingTaskDTO.
        Whether the reporting task has been deprecated.

        :return: The deprecated of this ReportingTaskDTO.
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """
        Sets the deprecated of this ReportingTaskDTO.
        Whether the reporting task has been deprecated.

        :param deprecated: The deprecated of this ReportingTaskDTO.
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def multiple_versions_available(self):
        """
        Gets the multiple_versions_available of this ReportingTaskDTO.
        Whether the reporting task has multiple versions available.

        :return: The multiple_versions_available of this ReportingTaskDTO.
        :rtype: bool
        """
        return self._multiple_versions_available

    @multiple_versions_available.setter
    def multiple_versions_available(self, multiple_versions_available):
        """
        Sets the multiple_versions_available of this ReportingTaskDTO.
        Whether the reporting task has multiple versions available.

        :param multiple_versions_available: The multiple_versions_available of this ReportingTaskDTO.
        :type: bool
        """

        self._multiple_versions_available = multiple_versions_available

    @property
    def supports_sensitive_dynamic_properties(self):
        """
        Gets the supports_sensitive_dynamic_properties of this ReportingTaskDTO.
        Whether the reporting task supports sensitive dynamic properties.

        :return: The supports_sensitive_dynamic_properties of this ReportingTaskDTO.
        :rtype: bool
        """
        return self._supports_sensitive_dynamic_properties

    @supports_sensitive_dynamic_properties.setter
    def supports_sensitive_dynamic_properties(self, supports_sensitive_dynamic_properties):
        """
        Sets the supports_sensitive_dynamic_properties of this ReportingTaskDTO.
        Whether the reporting task supports sensitive dynamic properties.

        :param supports_sensitive_dynamic_properties: The supports_sensitive_dynamic_properties of this ReportingTaskDTO.
        :type: bool
        """

        self._supports_sensitive_dynamic_properties = supports_sensitive_dynamic_properties

    @property
    def scheduling_period(self):
        """
        Gets the scheduling_period of this ReportingTaskDTO.
        The frequency with which to schedule the reporting task. The format of the value will depend on the value of the schedulingStrategy.

        :return: The scheduling_period of this ReportingTaskDTO.
        :rtype: str
        """
        return self._scheduling_period

    @scheduling_period.setter
    def scheduling_period(self, scheduling_period):
        """
        Sets the scheduling_period of this ReportingTaskDTO.
        The frequency with which to schedule the reporting task. The format of the value will depend on the value of the schedulingStrategy.

        :param scheduling_period: The scheduling_period of this ReportingTaskDTO.
        :type: str
        """

        self._scheduling_period = scheduling_period

    @property
    def scheduling_strategy(self):
        """
        Gets the scheduling_strategy of this ReportingTaskDTO.
        The scheduling strategy that determines how the schedulingPeriod value should be interpreted.

        :return: The scheduling_strategy of this ReportingTaskDTO.
        :rtype: str
        """
        return self._scheduling_strategy

    @scheduling_strategy.setter
    def scheduling_strategy(self, scheduling_strategy):
        """
        Sets the scheduling_strategy of this ReportingTaskDTO.
        The scheduling strategy that determines how the schedulingPeriod value should be interpreted.

        :param scheduling_strategy: The scheduling_strategy of this ReportingTaskDTO.
        :type: str
        """

        self._scheduling_strategy = scheduling_strategy

    @property
    def default_scheduling_period(self):
        """
        Gets the default_scheduling_period of this ReportingTaskDTO.
        The default scheduling period for the different scheduling strategies.

        :return: The default_scheduling_period of this ReportingTaskDTO.
        :rtype: dict(str, str)
        """
        return self._default_scheduling_period

    @default_scheduling_period.setter
    def default_scheduling_period(self, default_scheduling_period):
        """
        Sets the default_scheduling_period of this ReportingTaskDTO.
        The default scheduling period for the different scheduling strategies.

        :param default_scheduling_period: The default_scheduling_period of this ReportingTaskDTO.
        :type: dict(str, str)
        """

        self._default_scheduling_period = default_scheduling_period

    @property
    def properties(self):
        """
        Gets the properties of this ReportingTaskDTO.
        The properties of the reporting task.

        :return: The properties of this ReportingTaskDTO.
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this ReportingTaskDTO.
        The properties of the reporting task.

        :param properties: The properties of this ReportingTaskDTO.
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def descriptors(self):
        """
        Gets the descriptors of this ReportingTaskDTO.
        The descriptors for the reporting tasks properties.

        :return: The descriptors of this ReportingTaskDTO.
        :rtype: dict(str, PropertyDescriptorDTO)
        """
        return self._descriptors

    @descriptors.setter
    def descriptors(self, descriptors):
        """
        Sets the descriptors of this ReportingTaskDTO.
        The descriptors for the reporting tasks properties.

        :param descriptors: The descriptors of this ReportingTaskDTO.
        :type: dict(str, PropertyDescriptorDTO)
        """

        self._descriptors = descriptors

    @property
    def sensitive_dynamic_property_names(self):
        """
        Gets the sensitive_dynamic_property_names of this ReportingTaskDTO.
        Set of sensitive dynamic property names

        :return: The sensitive_dynamic_property_names of this ReportingTaskDTO.
        :rtype: list[str]
        """
        return self._sensitive_dynamic_property_names

    @sensitive_dynamic_property_names.setter
    def sensitive_dynamic_property_names(self, sensitive_dynamic_property_names):
        """
        Sets the sensitive_dynamic_property_names of this ReportingTaskDTO.
        Set of sensitive dynamic property names

        :param sensitive_dynamic_property_names: The sensitive_dynamic_property_names of this ReportingTaskDTO.
        :type: list[str]
        """

        self._sensitive_dynamic_property_names = sensitive_dynamic_property_names

    @property
    def custom_ui_url(self):
        """
        Gets the custom_ui_url of this ReportingTaskDTO.
        The URL for the custom configuration UI for the reporting task.

        :return: The custom_ui_url of this ReportingTaskDTO.
        :rtype: str
        """
        return self._custom_ui_url

    @custom_ui_url.setter
    def custom_ui_url(self, custom_ui_url):
        """
        Sets the custom_ui_url of this ReportingTaskDTO.
        The URL for the custom configuration UI for the reporting task.

        :param custom_ui_url: The custom_ui_url of this ReportingTaskDTO.
        :type: str
        """

        self._custom_ui_url = custom_ui_url

    @property
    def annotation_data(self):
        """
        Gets the annotation_data of this ReportingTaskDTO.
        The annotation data for the repoting task. This is how the custom UI relays configuration to the reporting task.

        :return: The annotation_data of this ReportingTaskDTO.
        :rtype: str
        """
        return self._annotation_data

    @annotation_data.setter
    def annotation_data(self, annotation_data):
        """
        Sets the annotation_data of this ReportingTaskDTO.
        The annotation data for the repoting task. This is how the custom UI relays configuration to the reporting task.

        :param annotation_data: The annotation_data of this ReportingTaskDTO.
        :type: str
        """

        self._annotation_data = annotation_data

    @property
    def validation_errors(self):
        """
        Gets the validation_errors of this ReportingTaskDTO.
        Gets the validation errors from the reporting task. These validation errors represent the problems with the reporting task that must be resolved before it can be scheduled to run.

        :return: The validation_errors of this ReportingTaskDTO.
        :rtype: list[str]
        """
        return self._validation_errors

    @validation_errors.setter
    def validation_errors(self, validation_errors):
        """
        Sets the validation_errors of this ReportingTaskDTO.
        Gets the validation errors from the reporting task. These validation errors represent the problems with the reporting task that must be resolved before it can be scheduled to run.

        :param validation_errors: The validation_errors of this ReportingTaskDTO.
        :type: list[str]
        """

        self._validation_errors = validation_errors

    @property
    def validation_status(self):
        """
        Gets the validation_status of this ReportingTaskDTO.
        Indicates whether the Reporting Task is valid, invalid, or still in the process of validating (i.e., it is unknown whether or not the Reporting Task is valid)

        :return: The validation_status of this ReportingTaskDTO.
        :rtype: str
        """
        return self._validation_status

    @validation_status.setter
    def validation_status(self, validation_status):
        """
        Sets the validation_status of this ReportingTaskDTO.
        Indicates whether the Reporting Task is valid, invalid, or still in the process of validating (i.e., it is unknown whether or not the Reporting Task is valid)

        :param validation_status: The validation_status of this ReportingTaskDTO.
        :type: str
        """
        allowed_values = ["VALID", "INVALID", "VALIDATING"]
        if validation_status not in allowed_values:
            raise ValueError(
                "Invalid value for `validation_status` ({0}), must be one of {1}"
                .format(validation_status, allowed_values)
            )

        self._validation_status = validation_status

    @property
    def active_thread_count(self):
        """
        Gets the active_thread_count of this ReportingTaskDTO.
        The number of active threads for the reporting task.

        :return: The active_thread_count of this ReportingTaskDTO.
        :rtype: int
        """
        return self._active_thread_count

    @active_thread_count.setter
    def active_thread_count(self, active_thread_count):
        """
        Sets the active_thread_count of this ReportingTaskDTO.
        The number of active threads for the reporting task.

        :param active_thread_count: The active_thread_count of this ReportingTaskDTO.
        :type: int
        """

        self._active_thread_count = active_thread_count

    @property
    def extension_missing(self):
        """
        Gets the extension_missing of this ReportingTaskDTO.
        Whether the underlying extension is missing.

        :return: The extension_missing of this ReportingTaskDTO.
        :rtype: bool
        """
        return self._extension_missing

    @extension_missing.setter
    def extension_missing(self, extension_missing):
        """
        Sets the extension_missing of this ReportingTaskDTO.
        Whether the underlying extension is missing.

        :param extension_missing: The extension_missing of this ReportingTaskDTO.
        :type: bool
        """

        self._extension_missing = extension_missing

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
        if not isinstance(other, ReportingTaskDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
