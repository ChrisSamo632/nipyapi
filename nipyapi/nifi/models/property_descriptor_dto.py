"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class PropertyDescriptorDTO(object):
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
        'display_name': 'str',
        'description': 'str',
        'default_value': 'str',
        'allowable_values': 'list[AllowableValueEntity]',
        'required': 'bool',
        'sensitive': 'bool',
        'dynamic': 'bool',
        'supports_el': 'bool',
        'expression_language_scope': 'str',
        'identifies_controller_service': 'str',
        'identifies_controller_service_bundle': 'BundleDTO',
        'dependencies': 'list[PropertyDependencyDTO]'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'displayName',
        'description': 'description',
        'default_value': 'defaultValue',
        'allowable_values': 'allowableValues',
        'required': 'required',
        'sensitive': 'sensitive',
        'dynamic': 'dynamic',
        'supports_el': 'supportsEl',
        'expression_language_scope': 'expressionLanguageScope',
        'identifies_controller_service': 'identifiesControllerService',
        'identifies_controller_service_bundle': 'identifiesControllerServiceBundle',
        'dependencies': 'dependencies'
    }

    def __init__(self, name=None, display_name=None, description=None, default_value=None, allowable_values=None, required=None, sensitive=None, dynamic=None, supports_el=None, expression_language_scope=None, identifies_controller_service=None, identifies_controller_service_bundle=None, dependencies=None):
        """
        PropertyDescriptorDTO - a model defined in Swagger
        """

        self._name = None
        self._display_name = None
        self._description = None
        self._default_value = None
        self._allowable_values = None
        self._required = None
        self._sensitive = None
        self._dynamic = None
        self._supports_el = None
        self._expression_language_scope = None
        self._identifies_controller_service = None
        self._identifies_controller_service_bundle = None
        self._dependencies = None

        if name is not None:
          self.name = name
        if display_name is not None:
          self.display_name = display_name
        if description is not None:
          self.description = description
        if default_value is not None:
          self.default_value = default_value
        if allowable_values is not None:
          self.allowable_values = allowable_values
        if required is not None:
          self.required = required
        if sensitive is not None:
          self.sensitive = sensitive
        if dynamic is not None:
          self.dynamic = dynamic
        if supports_el is not None:
          self.supports_el = supports_el
        if expression_language_scope is not None:
          self.expression_language_scope = expression_language_scope
        if identifies_controller_service is not None:
          self.identifies_controller_service = identifies_controller_service
        if identifies_controller_service_bundle is not None:
          self.identifies_controller_service_bundle = identifies_controller_service_bundle
        if dependencies is not None:
          self.dependencies = dependencies

    @property
    def name(self):
        """
        Gets the name of this PropertyDescriptorDTO.
        The name for the property.

        :return: The name of this PropertyDescriptorDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PropertyDescriptorDTO.
        The name for the property.

        :param name: The name of this PropertyDescriptorDTO.
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this PropertyDescriptorDTO.
        The human readable name for the property.

        :return: The display_name of this PropertyDescriptorDTO.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PropertyDescriptorDTO.
        The human readable name for the property.

        :param display_name: The display_name of this PropertyDescriptorDTO.
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this PropertyDescriptorDTO.
        The description for the property. Used to relay additional details to a user or provide a mechanism of documenting intent.

        :return: The description of this PropertyDescriptorDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PropertyDescriptorDTO.
        The description for the property. Used to relay additional details to a user or provide a mechanism of documenting intent.

        :param description: The description of this PropertyDescriptorDTO.
        :type: str
        """

        self._description = description

    @property
    def default_value(self):
        """
        Gets the default_value of this PropertyDescriptorDTO.
        The default value for the property.

        :return: The default_value of this PropertyDescriptorDTO.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this PropertyDescriptorDTO.
        The default value for the property.

        :param default_value: The default_value of this PropertyDescriptorDTO.
        :type: str
        """

        self._default_value = default_value

    @property
    def allowable_values(self):
        """
        Gets the allowable_values of this PropertyDescriptorDTO.
        Allowable values for the property. If empty then the allowed values are not constrained.

        :return: The allowable_values of this PropertyDescriptorDTO.
        :rtype: list[AllowableValueEntity]
        """
        return self._allowable_values

    @allowable_values.setter
    def allowable_values(self, allowable_values):
        """
        Sets the allowable_values of this PropertyDescriptorDTO.
        Allowable values for the property. If empty then the allowed values are not constrained.

        :param allowable_values: The allowable_values of this PropertyDescriptorDTO.
        :type: list[AllowableValueEntity]
        """

        self._allowable_values = allowable_values

    @property
    def required(self):
        """
        Gets the required of this PropertyDescriptorDTO.
        Whether the property is required.

        :return: The required of this PropertyDescriptorDTO.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this PropertyDescriptorDTO.
        Whether the property is required.

        :param required: The required of this PropertyDescriptorDTO.
        :type: bool
        """

        self._required = required

    @property
    def sensitive(self):
        """
        Gets the sensitive of this PropertyDescriptorDTO.
        Whether the property is sensitive and protected whenever stored or represented.

        :return: The sensitive of this PropertyDescriptorDTO.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """
        Sets the sensitive of this PropertyDescriptorDTO.
        Whether the property is sensitive and protected whenever stored or represented.

        :param sensitive: The sensitive of this PropertyDescriptorDTO.
        :type: bool
        """

        self._sensitive = sensitive

    @property
    def dynamic(self):
        """
        Gets the dynamic of this PropertyDescriptorDTO.
        Whether the property is dynamic (user-defined).

        :return: The dynamic of this PropertyDescriptorDTO.
        :rtype: bool
        """
        return self._dynamic

    @dynamic.setter
    def dynamic(self, dynamic):
        """
        Sets the dynamic of this PropertyDescriptorDTO.
        Whether the property is dynamic (user-defined).

        :param dynamic: The dynamic of this PropertyDescriptorDTO.
        :type: bool
        """

        self._dynamic = dynamic

    @property
    def supports_el(self):
        """
        Gets the supports_el of this PropertyDescriptorDTO.
        Whether the property supports expression language.

        :return: The supports_el of this PropertyDescriptorDTO.
        :rtype: bool
        """
        return self._supports_el

    @supports_el.setter
    def supports_el(self, supports_el):
        """
        Sets the supports_el of this PropertyDescriptorDTO.
        Whether the property supports expression language.

        :param supports_el: The supports_el of this PropertyDescriptorDTO.
        :type: bool
        """

        self._supports_el = supports_el

    @property
    def expression_language_scope(self):
        """
        Gets the expression_language_scope of this PropertyDescriptorDTO.
        Scope of the Expression Language evaluation for the property.

        :return: The expression_language_scope of this PropertyDescriptorDTO.
        :rtype: str
        """
        return self._expression_language_scope

    @expression_language_scope.setter
    def expression_language_scope(self, expression_language_scope):
        """
        Sets the expression_language_scope of this PropertyDescriptorDTO.
        Scope of the Expression Language evaluation for the property.

        :param expression_language_scope: The expression_language_scope of this PropertyDescriptorDTO.
        :type: str
        """

        self._expression_language_scope = expression_language_scope

    @property
    def identifies_controller_service(self):
        """
        Gets the identifies_controller_service of this PropertyDescriptorDTO.
        If the property identifies a controller service this returns the fully qualified type.

        :return: The identifies_controller_service of this PropertyDescriptorDTO.
        :rtype: str
        """
        return self._identifies_controller_service

    @identifies_controller_service.setter
    def identifies_controller_service(self, identifies_controller_service):
        """
        Sets the identifies_controller_service of this PropertyDescriptorDTO.
        If the property identifies a controller service this returns the fully qualified type.

        :param identifies_controller_service: The identifies_controller_service of this PropertyDescriptorDTO.
        :type: str
        """

        self._identifies_controller_service = identifies_controller_service

    @property
    def identifies_controller_service_bundle(self):
        """
        Gets the identifies_controller_service_bundle of this PropertyDescriptorDTO.
        If the property identifies a controller service this returns the bundle of the type, null otherwise.

        :return: The identifies_controller_service_bundle of this PropertyDescriptorDTO.
        :rtype: BundleDTO
        """
        return self._identifies_controller_service_bundle

    @identifies_controller_service_bundle.setter
    def identifies_controller_service_bundle(self, identifies_controller_service_bundle):
        """
        Sets the identifies_controller_service_bundle of this PropertyDescriptorDTO.
        If the property identifies a controller service this returns the bundle of the type, null otherwise.

        :param identifies_controller_service_bundle: The identifies_controller_service_bundle of this PropertyDescriptorDTO.
        :type: BundleDTO
        """

        self._identifies_controller_service_bundle = identifies_controller_service_bundle

    @property
    def dependencies(self):
        """
        Gets the dependencies of this PropertyDescriptorDTO.
        A list of dependencies that must be met in order for this Property to be relevant. If any of these dependencies is not met, the property described by this Property Descriptor is not relevant.

        :return: The dependencies of this PropertyDescriptorDTO.
        :rtype: list[PropertyDependencyDTO]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies of this PropertyDescriptorDTO.
        A list of dependencies that must be met in order for this Property to be relevant. If any of these dependencies is not met, the property described by this Property Descriptor is not relevant.

        :param dependencies: The dependencies of this PropertyDescriptorDTO.
        :type: list[PropertyDependencyDTO]
        """

        self._dependencies = dependencies

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
        if not isinstance(other, PropertyDescriptorDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
