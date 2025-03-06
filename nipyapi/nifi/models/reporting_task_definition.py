# coding: utf-8

"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ReportingTaskDefinition(object):
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
        'group': 'str',
        'artifact': 'str',
        'version': 'str',
        'type': 'str',
        'type_description': 'str',
        'build_info': 'BuildInfo',
        'provided_api_implementations': 'list[DefinedType]',
        'tags': 'list[str]',
        'see_also': 'list[str]',
        'deprecated': 'bool',
        'deprecation_reason': 'str',
        'deprecation_alternatives': 'list[str]',
        'restricted': 'bool',
        'restricted_explanation': 'str',
        'explicit_restrictions': 'list[Restriction]',
        'stateful': 'Stateful',
        'system_resource_considerations': 'list[SystemResourceConsideration]',
        'additional_details': 'bool',
        'property_descriptors': 'dict(str, PropertyDescriptor)',
        'supports_dynamic_properties': 'bool',
        'supports_sensitive_dynamic_properties': 'bool',
        'dynamic_properties': 'list[DynamicProperty]',
        'supported_scheduling_strategies': 'list[str]',
        'default_scheduling_strategy': 'str',
        'default_scheduling_period_by_scheduling_strategy': 'dict(str, str)'
    }

    attribute_map = {
        'group': 'group',
        'artifact': 'artifact',
        'version': 'version',
        'type': 'type',
        'type_description': 'typeDescription',
        'build_info': 'buildInfo',
        'provided_api_implementations': 'providedApiImplementations',
        'tags': 'tags',
        'see_also': 'seeAlso',
        'deprecated': 'deprecated',
        'deprecation_reason': 'deprecationReason',
        'deprecation_alternatives': 'deprecationAlternatives',
        'restricted': 'restricted',
        'restricted_explanation': 'restrictedExplanation',
        'explicit_restrictions': 'explicitRestrictions',
        'stateful': 'stateful',
        'system_resource_considerations': 'systemResourceConsiderations',
        'additional_details': 'additionalDetails',
        'property_descriptors': 'propertyDescriptors',
        'supports_dynamic_properties': 'supportsDynamicProperties',
        'supports_sensitive_dynamic_properties': 'supportsSensitiveDynamicProperties',
        'dynamic_properties': 'dynamicProperties',
        'supported_scheduling_strategies': 'supportedSchedulingStrategies',
        'default_scheduling_strategy': 'defaultSchedulingStrategy',
        'default_scheduling_period_by_scheduling_strategy': 'defaultSchedulingPeriodBySchedulingStrategy'
    }

    def __init__(self, group=None, artifact=None, version=None, type=None, type_description=None, build_info=None, provided_api_implementations=None, tags=None, see_also=None, deprecated=None, deprecation_reason=None, deprecation_alternatives=None, restricted=None, restricted_explanation=None, explicit_restrictions=None, stateful=None, system_resource_considerations=None, additional_details=None, property_descriptors=None, supports_dynamic_properties=None, supports_sensitive_dynamic_properties=None, dynamic_properties=None, supported_scheduling_strategies=None, default_scheduling_strategy=None, default_scheduling_period_by_scheduling_strategy=None):
        """
        ReportingTaskDefinition - a model defined in Swagger
        """

        self._group = None
        self._artifact = None
        self._version = None
        self._type = None
        self._type_description = None
        self._build_info = None
        self._provided_api_implementations = None
        self._tags = None
        self._see_also = None
        self._deprecated = None
        self._deprecation_reason = None
        self._deprecation_alternatives = None
        self._restricted = None
        self._restricted_explanation = None
        self._explicit_restrictions = None
        self._stateful = None
        self._system_resource_considerations = None
        self._additional_details = None
        self._property_descriptors = None
        self._supports_dynamic_properties = None
        self._supports_sensitive_dynamic_properties = None
        self._dynamic_properties = None
        self._supported_scheduling_strategies = None
        self._default_scheduling_strategy = None
        self._default_scheduling_period_by_scheduling_strategy = None

        if group is not None:
          self.group = group
        if artifact is not None:
          self.artifact = artifact
        if version is not None:
          self.version = version
        self.type = type
        if type_description is not None:
          self.type_description = type_description
        if build_info is not None:
          self.build_info = build_info
        if provided_api_implementations is not None:
          self.provided_api_implementations = provided_api_implementations
        if tags is not None:
          self.tags = tags
        if see_also is not None:
          self.see_also = see_also
        if deprecated is not None:
          self.deprecated = deprecated
        if deprecation_reason is not None:
          self.deprecation_reason = deprecation_reason
        if deprecation_alternatives is not None:
          self.deprecation_alternatives = deprecation_alternatives
        if restricted is not None:
          self.restricted = restricted
        if restricted_explanation is not None:
          self.restricted_explanation = restricted_explanation
        if explicit_restrictions is not None:
          self.explicit_restrictions = explicit_restrictions
        if stateful is not None:
          self.stateful = stateful
        if system_resource_considerations is not None:
          self.system_resource_considerations = system_resource_considerations
        if additional_details is not None:
          self.additional_details = additional_details
        if property_descriptors is not None:
          self.property_descriptors = property_descriptors
        if supports_dynamic_properties is not None:
          self.supports_dynamic_properties = supports_dynamic_properties
        if supports_sensitive_dynamic_properties is not None:
          self.supports_sensitive_dynamic_properties = supports_sensitive_dynamic_properties
        if dynamic_properties is not None:
          self.dynamic_properties = dynamic_properties
        if supported_scheduling_strategies is not None:
          self.supported_scheduling_strategies = supported_scheduling_strategies
        if default_scheduling_strategy is not None:
          self.default_scheduling_strategy = default_scheduling_strategy
        if default_scheduling_period_by_scheduling_strategy is not None:
          self.default_scheduling_period_by_scheduling_strategy = default_scheduling_period_by_scheduling_strategy

    @property
    def group(self):
        """
        Gets the group of this ReportingTaskDefinition.
        The group name of the bundle that provides the referenced type.

        :return: The group of this ReportingTaskDefinition.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this ReportingTaskDefinition.
        The group name of the bundle that provides the referenced type.

        :param group: The group of this ReportingTaskDefinition.
        :type: str
        """

        self._group = group

    @property
    def artifact(self):
        """
        Gets the artifact of this ReportingTaskDefinition.
        The artifact name of the bundle that provides the referenced type.

        :return: The artifact of this ReportingTaskDefinition.
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """
        Sets the artifact of this ReportingTaskDefinition.
        The artifact name of the bundle that provides the referenced type.

        :param artifact: The artifact of this ReportingTaskDefinition.
        :type: str
        """

        self._artifact = artifact

    @property
    def version(self):
        """
        Gets the version of this ReportingTaskDefinition.
        The version of the bundle that provides the referenced type.

        :return: The version of this ReportingTaskDefinition.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this ReportingTaskDefinition.
        The version of the bundle that provides the referenced type.

        :param version: The version of this ReportingTaskDefinition.
        :type: str
        """

        self._version = version

    @property
    def type(self):
        """
        Gets the type of this ReportingTaskDefinition.
        The fully-qualified class type

        :return: The type of this ReportingTaskDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ReportingTaskDefinition.
        The fully-qualified class type

        :param type: The type of this ReportingTaskDefinition.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def type_description(self):
        """
        Gets the type_description of this ReportingTaskDefinition.
        The description of the type.

        :return: The type_description of this ReportingTaskDefinition.
        :rtype: str
        """
        return self._type_description

    @type_description.setter
    def type_description(self, type_description):
        """
        Sets the type_description of this ReportingTaskDefinition.
        The description of the type.

        :param type_description: The type_description of this ReportingTaskDefinition.
        :type: str
        """

        self._type_description = type_description

    @property
    def build_info(self):
        """
        Gets the build_info of this ReportingTaskDefinition.
        The build metadata for this component

        :return: The build_info of this ReportingTaskDefinition.
        :rtype: BuildInfo
        """
        return self._build_info

    @build_info.setter
    def build_info(self, build_info):
        """
        Sets the build_info of this ReportingTaskDefinition.
        The build metadata for this component

        :param build_info: The build_info of this ReportingTaskDefinition.
        :type: BuildInfo
        """

        self._build_info = build_info

    @property
    def provided_api_implementations(self):
        """
        Gets the provided_api_implementations of this ReportingTaskDefinition.
        If this type represents a provider for an interface, this lists the APIs it implements

        :return: The provided_api_implementations of this ReportingTaskDefinition.
        :rtype: list[DefinedType]
        """
        return self._provided_api_implementations

    @provided_api_implementations.setter
    def provided_api_implementations(self, provided_api_implementations):
        """
        Sets the provided_api_implementations of this ReportingTaskDefinition.
        If this type represents a provider for an interface, this lists the APIs it implements

        :param provided_api_implementations: The provided_api_implementations of this ReportingTaskDefinition.
        :type: list[DefinedType]
        """

        self._provided_api_implementations = provided_api_implementations

    @property
    def tags(self):
        """
        Gets the tags of this ReportingTaskDefinition.
        The tags associated with this type

        :return: The tags of this ReportingTaskDefinition.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ReportingTaskDefinition.
        The tags associated with this type

        :param tags: The tags of this ReportingTaskDefinition.
        :type: list[str]
        """

        self._tags = tags

    @property
    def see_also(self):
        """
        Gets the see_also of this ReportingTaskDefinition.
        The names of other component types that may be related

        :return: The see_also of this ReportingTaskDefinition.
        :rtype: list[str]
        """
        return self._see_also

    @see_also.setter
    def see_also(self, see_also):
        """
        Sets the see_also of this ReportingTaskDefinition.
        The names of other component types that may be related

        :param see_also: The see_also of this ReportingTaskDefinition.
        :type: list[str]
        """

        self._see_also = see_also

    @property
    def deprecated(self):
        """
        Gets the deprecated of this ReportingTaskDefinition.
        Whether or not the component has been deprecated

        :return: The deprecated of this ReportingTaskDefinition.
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """
        Sets the deprecated of this ReportingTaskDefinition.
        Whether or not the component has been deprecated

        :param deprecated: The deprecated of this ReportingTaskDefinition.
        :type: bool
        """

        self._deprecated = deprecated

    @property
    def deprecation_reason(self):
        """
        Gets the deprecation_reason of this ReportingTaskDefinition.
        If this component has been deprecated, this optional field can be used to provide an explanation

        :return: The deprecation_reason of this ReportingTaskDefinition.
        :rtype: str
        """
        return self._deprecation_reason

    @deprecation_reason.setter
    def deprecation_reason(self, deprecation_reason):
        """
        Sets the deprecation_reason of this ReportingTaskDefinition.
        If this component has been deprecated, this optional field can be used to provide an explanation

        :param deprecation_reason: The deprecation_reason of this ReportingTaskDefinition.
        :type: str
        """

        self._deprecation_reason = deprecation_reason

    @property
    def deprecation_alternatives(self):
        """
        Gets the deprecation_alternatives of this ReportingTaskDefinition.
        If this component has been deprecated, this optional field provides alternatives to use

        :return: The deprecation_alternatives of this ReportingTaskDefinition.
        :rtype: list[str]
        """
        return self._deprecation_alternatives

    @deprecation_alternatives.setter
    def deprecation_alternatives(self, deprecation_alternatives):
        """
        Sets the deprecation_alternatives of this ReportingTaskDefinition.
        If this component has been deprecated, this optional field provides alternatives to use

        :param deprecation_alternatives: The deprecation_alternatives of this ReportingTaskDefinition.
        :type: list[str]
        """

        self._deprecation_alternatives = deprecation_alternatives

    @property
    def restricted(self):
        """
        Gets the restricted of this ReportingTaskDefinition.
        Whether or not the component has a general restriction

        :return: The restricted of this ReportingTaskDefinition.
        :rtype: bool
        """
        return self._restricted

    @restricted.setter
    def restricted(self, restricted):
        """
        Sets the restricted of this ReportingTaskDefinition.
        Whether or not the component has a general restriction

        :param restricted: The restricted of this ReportingTaskDefinition.
        :type: bool
        """

        self._restricted = restricted

    @property
    def restricted_explanation(self):
        """
        Gets the restricted_explanation of this ReportingTaskDefinition.
        An optional description of the general restriction

        :return: The restricted_explanation of this ReportingTaskDefinition.
        :rtype: str
        """
        return self._restricted_explanation

    @restricted_explanation.setter
    def restricted_explanation(self, restricted_explanation):
        """
        Sets the restricted_explanation of this ReportingTaskDefinition.
        An optional description of the general restriction

        :param restricted_explanation: The restricted_explanation of this ReportingTaskDefinition.
        :type: str
        """

        self._restricted_explanation = restricted_explanation

    @property
    def explicit_restrictions(self):
        """
        Gets the explicit_restrictions of this ReportingTaskDefinition.
        Explicit restrictions that indicate a require permission to use the component

        :return: The explicit_restrictions of this ReportingTaskDefinition.
        :rtype: list[Restriction]
        """
        return self._explicit_restrictions

    @explicit_restrictions.setter
    def explicit_restrictions(self, explicit_restrictions):
        """
        Sets the explicit_restrictions of this ReportingTaskDefinition.
        Explicit restrictions that indicate a require permission to use the component

        :param explicit_restrictions: The explicit_restrictions of this ReportingTaskDefinition.
        :type: list[Restriction]
        """

        self._explicit_restrictions = explicit_restrictions

    @property
    def stateful(self):
        """
        Gets the stateful of this ReportingTaskDefinition.
        Indicates if the component stores state

        :return: The stateful of this ReportingTaskDefinition.
        :rtype: Stateful
        """
        return self._stateful

    @stateful.setter
    def stateful(self, stateful):
        """
        Sets the stateful of this ReportingTaskDefinition.
        Indicates if the component stores state

        :param stateful: The stateful of this ReportingTaskDefinition.
        :type: Stateful
        """

        self._stateful = stateful

    @property
    def system_resource_considerations(self):
        """
        Gets the system_resource_considerations of this ReportingTaskDefinition.
        The system resource considerations for the given component

        :return: The system_resource_considerations of this ReportingTaskDefinition.
        :rtype: list[SystemResourceConsideration]
        """
        return self._system_resource_considerations

    @system_resource_considerations.setter
    def system_resource_considerations(self, system_resource_considerations):
        """
        Sets the system_resource_considerations of this ReportingTaskDefinition.
        The system resource considerations for the given component

        :param system_resource_considerations: The system_resource_considerations of this ReportingTaskDefinition.
        :type: list[SystemResourceConsideration]
        """

        self._system_resource_considerations = system_resource_considerations

    @property
    def additional_details(self):
        """
        Gets the additional_details of this ReportingTaskDefinition.
        Indicates if the component has additional details documentation

        :return: The additional_details of this ReportingTaskDefinition.
        :rtype: bool
        """
        return self._additional_details

    @additional_details.setter
    def additional_details(self, additional_details):
        """
        Sets the additional_details of this ReportingTaskDefinition.
        Indicates if the component has additional details documentation

        :param additional_details: The additional_details of this ReportingTaskDefinition.
        :type: bool
        """

        self._additional_details = additional_details

    @property
    def property_descriptors(self):
        """
        Gets the property_descriptors of this ReportingTaskDefinition.
        Descriptions of configuration properties applicable to this component.

        :return: The property_descriptors of this ReportingTaskDefinition.
        :rtype: dict(str, PropertyDescriptor)
        """
        return self._property_descriptors

    @property_descriptors.setter
    def property_descriptors(self, property_descriptors):
        """
        Sets the property_descriptors of this ReportingTaskDefinition.
        Descriptions of configuration properties applicable to this component.

        :param property_descriptors: The property_descriptors of this ReportingTaskDefinition.
        :type: dict(str, PropertyDescriptor)
        """

        self._property_descriptors = property_descriptors

    @property
    def supports_dynamic_properties(self):
        """
        Gets the supports_dynamic_properties of this ReportingTaskDefinition.
        Whether or not this component makes use of dynamic (user-set) properties.

        :return: The supports_dynamic_properties of this ReportingTaskDefinition.
        :rtype: bool
        """
        return self._supports_dynamic_properties

    @supports_dynamic_properties.setter
    def supports_dynamic_properties(self, supports_dynamic_properties):
        """
        Sets the supports_dynamic_properties of this ReportingTaskDefinition.
        Whether or not this component makes use of dynamic (user-set) properties.

        :param supports_dynamic_properties: The supports_dynamic_properties of this ReportingTaskDefinition.
        :type: bool
        """

        self._supports_dynamic_properties = supports_dynamic_properties

    @property
    def supports_sensitive_dynamic_properties(self):
        """
        Gets the supports_sensitive_dynamic_properties of this ReportingTaskDefinition.
        Whether or not this component makes use of sensitive dynamic (user-set) properties.

        :return: The supports_sensitive_dynamic_properties of this ReportingTaskDefinition.
        :rtype: bool
        """
        return self._supports_sensitive_dynamic_properties

    @supports_sensitive_dynamic_properties.setter
    def supports_sensitive_dynamic_properties(self, supports_sensitive_dynamic_properties):
        """
        Sets the supports_sensitive_dynamic_properties of this ReportingTaskDefinition.
        Whether or not this component makes use of sensitive dynamic (user-set) properties.

        :param supports_sensitive_dynamic_properties: The supports_sensitive_dynamic_properties of this ReportingTaskDefinition.
        :type: bool
        """

        self._supports_sensitive_dynamic_properties = supports_sensitive_dynamic_properties

    @property
    def dynamic_properties(self):
        """
        Gets the dynamic_properties of this ReportingTaskDefinition.
        Describes the dynamic properties supported by this component

        :return: The dynamic_properties of this ReportingTaskDefinition.
        :rtype: list[DynamicProperty]
        """
        return self._dynamic_properties

    @dynamic_properties.setter
    def dynamic_properties(self, dynamic_properties):
        """
        Sets the dynamic_properties of this ReportingTaskDefinition.
        Describes the dynamic properties supported by this component

        :param dynamic_properties: The dynamic_properties of this ReportingTaskDefinition.
        :type: list[DynamicProperty]
        """

        self._dynamic_properties = dynamic_properties

    @property
    def supported_scheduling_strategies(self):
        """
        Gets the supported_scheduling_strategies of this ReportingTaskDefinition.
        The supported scheduling strategies, such as TIME_DRIVER or CRON.

        :return: The supported_scheduling_strategies of this ReportingTaskDefinition.
        :rtype: list[str]
        """
        return self._supported_scheduling_strategies

    @supported_scheduling_strategies.setter
    def supported_scheduling_strategies(self, supported_scheduling_strategies):
        """
        Sets the supported_scheduling_strategies of this ReportingTaskDefinition.
        The supported scheduling strategies, such as TIME_DRIVER or CRON.

        :param supported_scheduling_strategies: The supported_scheduling_strategies of this ReportingTaskDefinition.
        :type: list[str]
        """

        self._supported_scheduling_strategies = supported_scheduling_strategies

    @property
    def default_scheduling_strategy(self):
        """
        Gets the default_scheduling_strategy of this ReportingTaskDefinition.
        The default scheduling strategy for the reporting task.

        :return: The default_scheduling_strategy of this ReportingTaskDefinition.
        :rtype: str
        """
        return self._default_scheduling_strategy

    @default_scheduling_strategy.setter
    def default_scheduling_strategy(self, default_scheduling_strategy):
        """
        Sets the default_scheduling_strategy of this ReportingTaskDefinition.
        The default scheduling strategy for the reporting task.

        :param default_scheduling_strategy: The default_scheduling_strategy of this ReportingTaskDefinition.
        :type: str
        """

        self._default_scheduling_strategy = default_scheduling_strategy

    @property
    def default_scheduling_period_by_scheduling_strategy(self):
        """
        Gets the default_scheduling_period_by_scheduling_strategy of this ReportingTaskDefinition.
        The default scheduling period for each scheduling strategy. The scheduling period is expected to be a time period, such as \"30 sec\".

        :return: The default_scheduling_period_by_scheduling_strategy of this ReportingTaskDefinition.
        :rtype: dict(str, str)
        """
        return self._default_scheduling_period_by_scheduling_strategy

    @default_scheduling_period_by_scheduling_strategy.setter
    def default_scheduling_period_by_scheduling_strategy(self, default_scheduling_period_by_scheduling_strategy):
        """
        Sets the default_scheduling_period_by_scheduling_strategy of this ReportingTaskDefinition.
        The default scheduling period for each scheduling strategy. The scheduling period is expected to be a time period, such as \"30 sec\".

        :param default_scheduling_period_by_scheduling_strategy: The default_scheduling_period_by_scheduling_strategy of this ReportingTaskDefinition.
        :type: dict(str, str)
        """

        self._default_scheduling_period_by_scheduling_strategy = default_scheduling_period_by_scheduling_strategy

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
        if not isinstance(other, ReportingTaskDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
