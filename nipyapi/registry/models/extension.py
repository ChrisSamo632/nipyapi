"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class Extension(object):
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
        'name': 'str',
        'type': 'str',
        'deprecation_notice': 'DeprecationNotice',
        'description': 'str',
        'tags': 'list[str]',
        'properties': 'list[ModelProperty]',
        'supports_sensitive_dynamic_properties': 'bool',
        'dynamic_properties': 'list[DynamicProperty]',
        'relationships': 'list[Relationship]',
        'dynamic_relationship': 'DynamicRelationship',
        'reads_attributes': 'list[Attribute]',
        'writes_attributes': 'list[Attribute]',
        'stateful': 'Stateful',
        'restricted': 'Restricted',
        'input_requirement': 'str',
        'system_resource_considerations': 'list[SystemResourceConsideration]',
        'see_also': 'list[str]',
        'provided_service_apis': 'list[ProvidedServiceAPI]',
        'default_settings': 'DefaultSettings',
        'default_schedule': 'DefaultSchedule',
        'trigger_serially': 'bool',
        'trigger_when_empty': 'bool',
        'trigger_when_any_destination_available': 'bool',
        'supports_batching': 'bool',
        'event_driven': 'bool',
        'primary_node_only': 'bool',
        'side_effect_free': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'deprecation_notice': 'deprecationNotice',
        'description': 'description',
        'tags': 'tags',
        'properties': 'properties',
        'supports_sensitive_dynamic_properties': 'supportsSensitiveDynamicProperties',
        'dynamic_properties': 'dynamicProperties',
        'relationships': 'relationships',
        'dynamic_relationship': 'dynamicRelationship',
        'reads_attributes': 'readsAttributes',
        'writes_attributes': 'writesAttributes',
        'stateful': 'stateful',
        'restricted': 'restricted',
        'input_requirement': 'inputRequirement',
        'system_resource_considerations': 'systemResourceConsiderations',
        'see_also': 'seeAlso',
        'provided_service_apis': 'providedServiceAPIs',
        'default_settings': 'defaultSettings',
        'default_schedule': 'defaultSchedule',
        'trigger_serially': 'triggerSerially',
        'trigger_when_empty': 'triggerWhenEmpty',
        'trigger_when_any_destination_available': 'triggerWhenAnyDestinationAvailable',
        'supports_batching': 'supportsBatching',
        'event_driven': 'eventDriven',
        'primary_node_only': 'primaryNodeOnly',
        'side_effect_free': 'sideEffectFree'
    }

    def __init__(self, name=None, type=None, deprecation_notice=None, description=None, tags=None, properties=None, supports_sensitive_dynamic_properties=None, dynamic_properties=None, relationships=None, dynamic_relationship=None, reads_attributes=None, writes_attributes=None, stateful=None, restricted=None, input_requirement=None, system_resource_considerations=None, see_also=None, provided_service_apis=None, default_settings=None, default_schedule=None, trigger_serially=None, trigger_when_empty=None, trigger_when_any_destination_available=None, supports_batching=None, event_driven=None, primary_node_only=None, side_effect_free=None):
        """
        Extension - a model defined in Swagger
        """

        self._name = None
        self._type = None
        self._deprecation_notice = None
        self._description = None
        self._tags = None
        self._properties = None
        self._supports_sensitive_dynamic_properties = None
        self._dynamic_properties = None
        self._relationships = None
        self._dynamic_relationship = None
        self._reads_attributes = None
        self._writes_attributes = None
        self._stateful = None
        self._restricted = None
        self._input_requirement = None
        self._system_resource_considerations = None
        self._see_also = None
        self._provided_service_apis = None
        self._default_settings = None
        self._default_schedule = None
        self._trigger_serially = None
        self._trigger_when_empty = None
        self._trigger_when_any_destination_available = None
        self._supports_batching = None
        self._event_driven = None
        self._primary_node_only = None
        self._side_effect_free = None

        if name is not None:
          self.name = name
        if type is not None:
          self.type = type
        if deprecation_notice is not None:
          self.deprecation_notice = deprecation_notice
        if description is not None:
          self.description = description
        if tags is not None:
          self.tags = tags
        if properties is not None:
          self.properties = properties
        if supports_sensitive_dynamic_properties is not None:
          self.supports_sensitive_dynamic_properties = supports_sensitive_dynamic_properties
        if dynamic_properties is not None:
          self.dynamic_properties = dynamic_properties
        if relationships is not None:
          self.relationships = relationships
        if dynamic_relationship is not None:
          self.dynamic_relationship = dynamic_relationship
        if reads_attributes is not None:
          self.reads_attributes = reads_attributes
        if writes_attributes is not None:
          self.writes_attributes = writes_attributes
        if stateful is not None:
          self.stateful = stateful
        if restricted is not None:
          self.restricted = restricted
        if input_requirement is not None:
          self.input_requirement = input_requirement
        if system_resource_considerations is not None:
          self.system_resource_considerations = system_resource_considerations
        if see_also is not None:
          self.see_also = see_also
        if provided_service_apis is not None:
          self.provided_service_apis = provided_service_apis
        if default_settings is not None:
          self.default_settings = default_settings
        if default_schedule is not None:
          self.default_schedule = default_schedule
        if trigger_serially is not None:
          self.trigger_serially = trigger_serially
        if trigger_when_empty is not None:
          self.trigger_when_empty = trigger_when_empty
        if trigger_when_any_destination_available is not None:
          self.trigger_when_any_destination_available = trigger_when_any_destination_available
        if supports_batching is not None:
          self.supports_batching = supports_batching
        if event_driven is not None:
          self.event_driven = event_driven
        if primary_node_only is not None:
          self.primary_node_only = primary_node_only
        if side_effect_free is not None:
          self.side_effect_free = side_effect_free

    @property
    def name(self):
        """
        Gets the name of this Extension.
        The name of the extension

        :return: The name of this Extension.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Extension.
        The name of the extension

        :param name: The name of this Extension.
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """
        Gets the type of this Extension.
        The type of the extension

        :return: The type of this Extension.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Extension.
        The type of the extension

        :param type: The type of this Extension.
        :type: str
        """
        allowed_values = ["PROCESSOR", "CONTROLLER_SERVICE", "REPORTING_TASK"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def deprecation_notice(self):
        """
        Gets the deprecation_notice of this Extension.
        The deprecation notice of the extension

        :return: The deprecation_notice of this Extension.
        :rtype: DeprecationNotice
        """
        return self._deprecation_notice

    @deprecation_notice.setter
    def deprecation_notice(self, deprecation_notice):
        """
        Sets the deprecation_notice of this Extension.
        The deprecation notice of the extension

        :param deprecation_notice: The deprecation_notice of this Extension.
        :type: DeprecationNotice
        """

        self._deprecation_notice = deprecation_notice

    @property
    def description(self):
        """
        Gets the description of this Extension.
        The description of the extension

        :return: The description of this Extension.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Extension.
        The description of the extension

        :param description: The description of this Extension.
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """
        Gets the tags of this Extension.
        The tags of the extension

        :return: The tags of this Extension.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Extension.
        The tags of the extension

        :param tags: The tags of this Extension.
        :type: list[str]
        """

        self._tags = tags

    @property
    def properties(self):
        """
        Gets the properties of this Extension.
        The properties of the extension

        :return: The properties of this Extension.
        :rtype: list[ModelProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this Extension.
        The properties of the extension

        :param properties: The properties of this Extension.
        :type: list[ModelProperty]
        """

        self._properties = properties

    @property
    def supports_sensitive_dynamic_properties(self):
        """
        Gets the supports_sensitive_dynamic_properties of this Extension.

        :return: The supports_sensitive_dynamic_properties of this Extension.
        :rtype: bool
        """
        return self._supports_sensitive_dynamic_properties

    @supports_sensitive_dynamic_properties.setter
    def supports_sensitive_dynamic_properties(self, supports_sensitive_dynamic_properties):
        """
        Sets the supports_sensitive_dynamic_properties of this Extension.

        :param supports_sensitive_dynamic_properties: The supports_sensitive_dynamic_properties of this Extension.
        :type: bool
        """

        self._supports_sensitive_dynamic_properties = supports_sensitive_dynamic_properties

    @property
    def dynamic_properties(self):
        """
        Gets the dynamic_properties of this Extension.
        The dynamic properties of the extension

        :return: The dynamic_properties of this Extension.
        :rtype: list[DynamicProperty]
        """
        return self._dynamic_properties

    @dynamic_properties.setter
    def dynamic_properties(self, dynamic_properties):
        """
        Sets the dynamic_properties of this Extension.
        The dynamic properties of the extension

        :param dynamic_properties: The dynamic_properties of this Extension.
        :type: list[DynamicProperty]
        """

        self._dynamic_properties = dynamic_properties

    @property
    def relationships(self):
        """
        Gets the relationships of this Extension.
        The relationships of the extension

        :return: The relationships of this Extension.
        :rtype: list[Relationship]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """
        Sets the relationships of this Extension.
        The relationships of the extension

        :param relationships: The relationships of this Extension.
        :type: list[Relationship]
        """

        self._relationships = relationships

    @property
    def dynamic_relationship(self):
        """
        Gets the dynamic_relationship of this Extension.
        The dynamic relationships of the extension

        :return: The dynamic_relationship of this Extension.
        :rtype: DynamicRelationship
        """
        return self._dynamic_relationship

    @dynamic_relationship.setter
    def dynamic_relationship(self, dynamic_relationship):
        """
        Sets the dynamic_relationship of this Extension.
        The dynamic relationships of the extension

        :param dynamic_relationship: The dynamic_relationship of this Extension.
        :type: DynamicRelationship
        """

        self._dynamic_relationship = dynamic_relationship

    @property
    def reads_attributes(self):
        """
        Gets the reads_attributes of this Extension.
        The attributes read from flow files by the extension

        :return: The reads_attributes of this Extension.
        :rtype: list[Attribute]
        """
        return self._reads_attributes

    @reads_attributes.setter
    def reads_attributes(self, reads_attributes):
        """
        Sets the reads_attributes of this Extension.
        The attributes read from flow files by the extension

        :param reads_attributes: The reads_attributes of this Extension.
        :type: list[Attribute]
        """

        self._reads_attributes = reads_attributes

    @property
    def writes_attributes(self):
        """
        Gets the writes_attributes of this Extension.
        The attributes written to flow files by the extension

        :return: The writes_attributes of this Extension.
        :rtype: list[Attribute]
        """
        return self._writes_attributes

    @writes_attributes.setter
    def writes_attributes(self, writes_attributes):
        """
        Sets the writes_attributes of this Extension.
        The attributes written to flow files by the extension

        :param writes_attributes: The writes_attributes of this Extension.
        :type: list[Attribute]
        """

        self._writes_attributes = writes_attributes

    @property
    def stateful(self):
        """
        Gets the stateful of this Extension.
        The information about how the extension stores state

        :return: The stateful of this Extension.
        :rtype: Stateful
        """
        return self._stateful

    @stateful.setter
    def stateful(self, stateful):
        """
        Sets the stateful of this Extension.
        The information about how the extension stores state

        :param stateful: The stateful of this Extension.
        :type: Stateful
        """

        self._stateful = stateful

    @property
    def restricted(self):
        """
        Gets the restricted of this Extension.
        The restrictions of the extension

        :return: The restricted of this Extension.
        :rtype: Restricted
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """
        Sets the restricted of this Extension.
        The restrictions of the extension

        :param restricted: The restricted of this Extension.
        :type: Restricted
        """

        self._restricted = restricted

    @property
    def input_requirement(self):
        """
        Gets the input_requirement of this Extension.
        The input requirement of the extension

        :return: The input_requirement of this Extension.
        :rtype: str
        """
        return self._input_requirement

    @input_requirement.setter
    def input_requirement(self, input_requirement):
        """
        Sets the input_requirement of this Extension.
        The input requirement of the extension

        :param input_requirement: The input_requirement of this Extension.
        :type: str
        """
        allowed_values = ["INPUT_REQUIRED", "INPUT_ALLOWED", "INPUT_FORBIDDEN"]
        if input_requirement not in allowed_values:
            raise ValueError(
                "Invalid value for `input_requirement` ({0}), must be one of {1}"
                .format(input_requirement, allowed_values)
            )

        self._input_requirement = input_requirement

    @property
    def system_resource_considerations(self):
        """
        Gets the system_resource_considerations of this Extension.
        The resource considerations of the extension

        :return: The system_resource_considerations of this Extension.
        :rtype: list[SystemResourceConsideration]
        """
        return self._system_resource_considerations

    @system_resource_considerations.setter
    def system_resource_considerations(self, system_resource_considerations):
        """
        Sets the system_resource_considerations of this Extension.
        The resource considerations of the extension

        :param system_resource_considerations: The system_resource_considerations of this Extension.
        :type: list[SystemResourceConsideration]
        """

        self._system_resource_considerations = system_resource_considerations

    @property
    def see_also(self):
        """
        Gets the see_also of this Extension.
        The names of other extensions to see

        :return: The see_also of this Extension.
        :rtype: list[str]
        """
        return self._see_also

    @see_also.setter
    def see_also(self, see_also):
        """
        Sets the see_also of this Extension.
        The names of other extensions to see

        :param see_also: The see_also of this Extension.
        :type: list[str]
        """

        self._see_also = see_also

    @property
    def provided_service_apis(self):
        """
        Gets the provided_service_apis of this Extension.
        The service APIs provided by this extension

        :return: The provided_service_apis of this Extension.
        :rtype: list[ProvidedServiceAPI]
        """
        return self._provided_service_apis

    @provided_service_apis.setter
    def provided_service_apis(self, provided_service_apis):
        """
        Sets the provided_service_apis of this Extension.
        The service APIs provided by this extension

        :param provided_service_apis: The provided_service_apis of this Extension.
        :type: list[ProvidedServiceAPI]
        """

        self._provided_service_apis = provided_service_apis

    @property
    def default_settings(self):
        """
        Gets the default_settings of this Extension.
        The default settings for a processor

        :return: The default_settings of this Extension.
        :rtype: DefaultSettings
        """
        return self._default_settings

    @default_settings.setter
    def default_settings(self, default_settings):
        """
        Sets the default_settings of this Extension.
        The default settings for a processor

        :param default_settings: The default_settings of this Extension.
        :type: DefaultSettings
        """

        self._default_settings = default_settings

    @property
    def default_schedule(self):
        """
        Gets the default_schedule of this Extension.
        The default schedule for a processor reporting task

        :return: The default_schedule of this Extension.
        :rtype: DefaultSchedule
        """
        return self._default_schedule

    @default_schedule.setter
    def default_schedule(self, default_schedule):
        """
        Sets the default_schedule of this Extension.
        The default schedule for a processor reporting task

        :param default_schedule: The default_schedule of this Extension.
        :type: DefaultSchedule
        """

        self._default_schedule = default_schedule

    @property
    def trigger_serially(self):
        """
        Gets the trigger_serially of this Extension.
        Indicates that a processor should be triggered serially

        :return: The trigger_serially of this Extension.
        :rtype: bool
        """
        return self._trigger_serially

    @trigger_serially.setter
    def trigger_serially(self, trigger_serially):
        """
        Sets the trigger_serially of this Extension.
        Indicates that a processor should be triggered serially

        :param trigger_serially: The trigger_serially of this Extension.
        :type: bool
        """

        self._trigger_serially = trigger_serially

    @property
    def trigger_when_empty(self):
        """
        Gets the trigger_when_empty of this Extension.
        Indicates that a processor should be triggered when the incoming queues are empty

        :return: The trigger_when_empty of this Extension.
        :rtype: bool
        """
        return self._trigger_when_empty

    @trigger_when_empty.setter
    def trigger_when_empty(self, trigger_when_empty):
        """
        Sets the trigger_when_empty of this Extension.
        Indicates that a processor should be triggered when the incoming queues are empty

        :param trigger_when_empty: The trigger_when_empty of this Extension.
        :type: bool
        """

        self._trigger_when_empty = trigger_when_empty

    @property
    def trigger_when_any_destination_available(self):
        """
        Gets the trigger_when_any_destination_available of this Extension.
        Indicates that a processor should be triggered when any destinations have space for flow files

        :return: The trigger_when_any_destination_available of this Extension.
        :rtype: bool
        """
        return self._trigger_when_any_destination_available

    @trigger_when_any_destination_available.setter
    def trigger_when_any_destination_available(self, trigger_when_any_destination_available):
        """
        Sets the trigger_when_any_destination_available of this Extension.
        Indicates that a processor should be triggered when any destinations have space for flow files

        :param trigger_when_any_destination_available: The trigger_when_any_destination_available of this Extension.
        :type: bool
        """

        self._trigger_when_any_destination_available = trigger_when_any_destination_available

    @property
    def supports_batching(self):
        """
        Gets the supports_batching of this Extension.
        Indicates that a processor supports batching

        :return: The supports_batching of this Extension.
        :rtype: bool
        """
        return self._supports_batching

    @supports_batching.setter
    def supports_batching(self, supports_batching):
        """
        Sets the supports_batching of this Extension.
        Indicates that a processor supports batching

        :param supports_batching: The supports_batching of this Extension.
        :type: bool
        """

        self._supports_batching = supports_batching

    @property
    def event_driven(self):
        """
        Gets the event_driven of this Extension.
        Indicates that a processor supports event driven scheduling

        :return: The event_driven of this Extension.
        :rtype: bool
        """
        return self._event_driven

    @event_driven.setter
    def event_driven(self, event_driven):
        """
        Sets the event_driven of this Extension.
        Indicates that a processor supports event driven scheduling

        :param event_driven: The event_driven of this Extension.
        :type: bool
        """

        self._event_driven = event_driven

    @property
    def primary_node_only(self):
        """
        Gets the primary_node_only of this Extension.
        Indicates that a processor should be scheduled only on the primary node

        :return: The primary_node_only of this Extension.
        :rtype: bool
        """
        return self._primary_node_only

    @primary_node_only.setter
    def primary_node_only(self, primary_node_only):
        """
        Sets the primary_node_only of this Extension.
        Indicates that a processor should be scheduled only on the primary node

        :param primary_node_only: The primary_node_only of this Extension.
        :type: bool
        """

        self._primary_node_only = primary_node_only

    @property
    def side_effect_free(self):
        """
        Gets the side_effect_free of this Extension.
        Indicates that a processor is side effect free

        :return: The side_effect_free of this Extension.
        :rtype: bool
        """
        return self._side_effect_free

    @side_effect_free.setter
    def side_effect_free(self, side_effect_free):
        """
        Sets the side_effect_free of this Extension.
        Indicates that a processor is side effect free

        :param side_effect_free: The side_effect_free of this Extension.
        :type: bool
        """

        self._side_effect_free = side_effect_free

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
        if not isinstance(other, Extension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
