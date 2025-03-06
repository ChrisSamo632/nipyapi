# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ModelProperty(object):
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
        'controller_service_definition': 'ControllerServiceDefinition',
        'allowable_values': 'list[AllowableValue]',
        'required': 'bool',
        'sensitive': 'bool',
        'expression_language_supported': 'bool',
        'expression_language_scope': 'str',
        'dynamically_modifies_classpath': 'bool',
        'dynamic': 'bool',
        'dependencies': 'list[Dependency]',
        'resource_definition': 'ResourceDefinition'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'displayName',
        'description': 'description',
        'default_value': 'defaultValue',
        'controller_service_definition': 'controllerServiceDefinition',
        'allowable_values': 'allowableValues',
        'required': 'required',
        'sensitive': 'sensitive',
        'expression_language_supported': 'expressionLanguageSupported',
        'expression_language_scope': 'expressionLanguageScope',
        'dynamically_modifies_classpath': 'dynamicallyModifiesClasspath',
        'dynamic': 'dynamic',
        'dependencies': 'dependencies',
        'resource_definition': 'resourceDefinition'
    }

    def __init__(self, name=None, display_name=None, description=None, default_value=None, controller_service_definition=None, allowable_values=None, required=None, sensitive=None, expression_language_supported=None, expression_language_scope=None, dynamically_modifies_classpath=None, dynamic=None, dependencies=None, resource_definition=None):
        """
        ModelProperty - a model defined in Swagger
        """

        self._name = None
        self._display_name = None
        self._description = None
        self._default_value = None
        self._controller_service_definition = None
        self._allowable_values = None
        self._required = None
        self._sensitive = None
        self._expression_language_supported = None
        self._expression_language_scope = None
        self._dynamically_modifies_classpath = None
        self._dynamic = None
        self._dependencies = None
        self._resource_definition = None

        if name is not None:
          self.name = name
        if display_name is not None:
          self.display_name = display_name
        if description is not None:
          self.description = description
        if default_value is not None:
          self.default_value = default_value
        if controller_service_definition is not None:
          self.controller_service_definition = controller_service_definition
        if allowable_values is not None:
          self.allowable_values = allowable_values
        if required is not None:
          self.required = required
        if sensitive is not None:
          self.sensitive = sensitive
        if expression_language_supported is not None:
          self.expression_language_supported = expression_language_supported
        if expression_language_scope is not None:
          self.expression_language_scope = expression_language_scope
        if dynamically_modifies_classpath is not None:
          self.dynamically_modifies_classpath = dynamically_modifies_classpath
        if dynamic is not None:
          self.dynamic = dynamic
        if dependencies is not None:
          self.dependencies = dependencies
        if resource_definition is not None:
          self.resource_definition = resource_definition

    @property
    def name(self):
        """
        Gets the name of this ModelProperty.
        The name of the property

        :return: The name of this ModelProperty.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ModelProperty.
        The name of the property

        :param name: The name of this ModelProperty.
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this ModelProperty.
        The display name

        :return: The display_name of this ModelProperty.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ModelProperty.
        The display name

        :param display_name: The display_name of this ModelProperty.
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this ModelProperty.
        The description

        :return: The description of this ModelProperty.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ModelProperty.
        The description

        :param description: The description of this ModelProperty.
        :type: str
        """

        self._description = description

    @property
    def default_value(self):
        """
        Gets the default_value of this ModelProperty.
        The default value

        :return: The default_value of this ModelProperty.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this ModelProperty.
        The default value

        :param default_value: The default_value of this ModelProperty.
        :type: str
        """

        self._default_value = default_value

    @property
    def controller_service_definition(self):
        """
        Gets the controller_service_definition of this ModelProperty.
        The controller service required by this property, or null if none is required

        :return: The controller_service_definition of this ModelProperty.
        :rtype: ControllerServiceDefinition
        """
        return self._controller_service_definition

    @controller_service_definition.setter
    def controller_service_definition(self, controller_service_definition):
        """
        Sets the controller_service_definition of this ModelProperty.
        The controller service required by this property, or null if none is required

        :param controller_service_definition: The controller_service_definition of this ModelProperty.
        :type: ControllerServiceDefinition
        """

        self._controller_service_definition = controller_service_definition

    @property
    def allowable_values(self):
        """
        Gets the allowable_values of this ModelProperty.
        The allowable values for this property

        :return: The allowable_values of this ModelProperty.
        :rtype: list[AllowableValue]
        """
        return self._allowable_values

    @allowable_values.setter
    def allowable_values(self, allowable_values):
        """
        Sets the allowable_values of this ModelProperty.
        The allowable values for this property

        :param allowable_values: The allowable_values of this ModelProperty.
        :type: list[AllowableValue]
        """

        self._allowable_values = allowable_values

    @property
    def required(self):
        """
        Gets the required of this ModelProperty.
        Whether or not the property is required

        :return: The required of this ModelProperty.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this ModelProperty.
        Whether or not the property is required

        :param required: The required of this ModelProperty.
        :type: bool
        """

        self._required = required

    @property
    def sensitive(self):
        """
        Gets the sensitive of this ModelProperty.
        Whether or not the property is sensitive

        :return: The sensitive of this ModelProperty.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """
        Sets the sensitive of this ModelProperty.
        Whether or not the property is sensitive

        :param sensitive: The sensitive of this ModelProperty.
        :type: bool
        """

        self._sensitive = sensitive

    @property
    def expression_language_supported(self):
        """
        Gets the expression_language_supported of this ModelProperty.
        Whether or not expression language is supported

        :return: The expression_language_supported of this ModelProperty.
        :rtype: bool
        """
        return self._expression_language_supported

    @expression_language_supported.setter
    def expression_language_supported(self, expression_language_supported):
        """
        Sets the expression_language_supported of this ModelProperty.
        Whether or not expression language is supported

        :param expression_language_supported: The expression_language_supported of this ModelProperty.
        :type: bool
        """

        self._expression_language_supported = expression_language_supported

    @property
    def expression_language_scope(self):
        """
        Gets the expression_language_scope of this ModelProperty.
        The scope of expression language support

        :return: The expression_language_scope of this ModelProperty.
        :rtype: str
        """
        return self._expression_language_scope

    @expression_language_scope.setter
    def expression_language_scope(self, expression_language_scope):
        """
        Sets the expression_language_scope of this ModelProperty.
        The scope of expression language support

        :param expression_language_scope: The expression_language_scope of this ModelProperty.
        :type: str
        """
        allowed_values = ["NONE", "VARIABLE_REGISTRY", "FLOWFILE_ATTRIBUTES"]
        if expression_language_scope not in allowed_values:
            raise ValueError(
                "Invalid value for `expression_language_scope` ({0}), must be one of {1}"
                .format(expression_language_scope, allowed_values)
            )

        self._expression_language_scope = expression_language_scope

    @property
    def dynamically_modifies_classpath(self):
        """
        Gets the dynamically_modifies_classpath of this ModelProperty.
        Whether or not the processor dynamically modifies the classpath

        :return: The dynamically_modifies_classpath of this ModelProperty.
        :rtype: bool
        """
        return self._dynamically_modifies_classpath

    @dynamically_modifies_classpath.setter
    def dynamically_modifies_classpath(self, dynamically_modifies_classpath):
        """
        Sets the dynamically_modifies_classpath of this ModelProperty.
        Whether or not the processor dynamically modifies the classpath

        :param dynamically_modifies_classpath: The dynamically_modifies_classpath of this ModelProperty.
        :type: bool
        """

        self._dynamically_modifies_classpath = dynamically_modifies_classpath

    @property
    def dynamic(self):
        """
        Gets the dynamic of this ModelProperty.
        Whether or not the processor is dynamic

        :return: The dynamic of this ModelProperty.
        :rtype: bool
        """
        return self._dynamic

    @dynamic.setter
    def dynamic(self, dynamic):
        """
        Sets the dynamic of this ModelProperty.
        Whether or not the processor is dynamic

        :param dynamic: The dynamic of this ModelProperty.
        :type: bool
        """

        self._dynamic = dynamic

    @property
    def dependencies(self):
        """
        Gets the dependencies of this ModelProperty.
        The properties that this property depends on

        :return: The dependencies of this ModelProperty.
        :rtype: list[Dependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies of this ModelProperty.
        The properties that this property depends on

        :param dependencies: The dependencies of this ModelProperty.
        :type: list[Dependency]
        """

        self._dependencies = dependencies

    @property
    def resource_definition(self):
        """
        Gets the resource_definition of this ModelProperty.
        The optional resource definition

        :return: The resource_definition of this ModelProperty.
        :rtype: ResourceDefinition
        """
        return self._resource_definition

    @resource_definition.setter
    def resource_definition(self, resource_definition):
        """
        Sets the resource_definition of this ModelProperty.
        The optional resource definition

        :param resource_definition: The resource_definition of this ModelProperty.
        :type: ResourceDefinition
        """

        self._resource_definition = resource_definition

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
        if not isinstance(other, ModelProperty):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
