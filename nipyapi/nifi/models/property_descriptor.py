"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class PropertyDescriptor(object):
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
        'allowable_values': 'list[PropertyAllowableValue]',
        'default_value': 'str',
        'required': 'bool',
        'sensitive': 'bool',
        'expression_language_scope': 'str',
        'expression_language_scope_description': 'str',
        'type_provided_by_value': 'DefinedType',
        'valid_regex': 'str',
        'validator': 'str',
        'dynamic': 'bool',
        'resource_definition': 'PropertyResourceDefinition',
        'dependencies': 'list[PropertyDependency]'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'displayName',
        'description': 'description',
        'allowable_values': 'allowableValues',
        'default_value': 'defaultValue',
        'required': 'required',
        'sensitive': 'sensitive',
        'expression_language_scope': 'expressionLanguageScope',
        'expression_language_scope_description': 'expressionLanguageScopeDescription',
        'type_provided_by_value': 'typeProvidedByValue',
        'valid_regex': 'validRegex',
        'validator': 'validator',
        'dynamic': 'dynamic',
        'resource_definition': 'resourceDefinition',
        'dependencies': 'dependencies'
    }

    def __init__(self, name=None, display_name=None, description=None, allowable_values=None, default_value=None, required=None, sensitive=None, expression_language_scope=None, expression_language_scope_description=None, type_provided_by_value=None, valid_regex=None, validator=None, dynamic=None, resource_definition=None, dependencies=None):
        """
        PropertyDescriptor - a model defined in Swagger
        """

        self._name = None
        self._display_name = None
        self._description = None
        self._allowable_values = None
        self._default_value = None
        self._required = None
        self._sensitive = None
        self._expression_language_scope = None
        self._expression_language_scope_description = None
        self._type_provided_by_value = None
        self._valid_regex = None
        self._validator = None
        self._dynamic = None
        self._resource_definition = None
        self._dependencies = None

        self.name = name
        if display_name is not None:
          self.display_name = display_name
        if description is not None:
          self.description = description
        if allowable_values is not None:
          self.allowable_values = allowable_values
        if default_value is not None:
          self.default_value = default_value
        if required is not None:
          self.required = required
        if sensitive is not None:
          self.sensitive = sensitive
        if expression_language_scope is not None:
          self.expression_language_scope = expression_language_scope
        if expression_language_scope_description is not None:
          self.expression_language_scope_description = expression_language_scope_description
        if type_provided_by_value is not None:
          self.type_provided_by_value = type_provided_by_value
        if valid_regex is not None:
          self.valid_regex = valid_regex
        if validator is not None:
          self.validator = validator
        if dynamic is not None:
          self.dynamic = dynamic
        if resource_definition is not None:
          self.resource_definition = resource_definition
        if dependencies is not None:
          self.dependencies = dependencies

    @property
    def name(self):
        """
        Gets the name of this PropertyDescriptor.
        The name of the property key

        :return: The name of this PropertyDescriptor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PropertyDescriptor.
        The name of the property key

        :param name: The name of this PropertyDescriptor.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def display_name(self):
        """
        Gets the display_name of this PropertyDescriptor.
        The display name of the property key, if different from the name

        :return: The display_name of this PropertyDescriptor.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PropertyDescriptor.
        The display name of the property key, if different from the name

        :param display_name: The display_name of this PropertyDescriptor.
        :type: str
        """

        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this PropertyDescriptor.
        The description of what the property does

        :return: The description of this PropertyDescriptor.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PropertyDescriptor.
        The description of what the property does

        :param description: The description of this PropertyDescriptor.
        :type: str
        """

        self._description = description

    @property
    def allowable_values(self):
        """
        Gets the allowable_values of this PropertyDescriptor.
        A list of the allowable values for the property

        :return: The allowable_values of this PropertyDescriptor.
        :rtype: list[PropertyAllowableValue]
        """
        return self._allowable_values

    @allowable_values.setter
    def allowable_values(self, allowable_values):
        """
        Sets the allowable_values of this PropertyDescriptor.
        A list of the allowable values for the property

        :param allowable_values: The allowable_values of this PropertyDescriptor.
        :type: list[PropertyAllowableValue]
        """

        self._allowable_values = allowable_values

    @property
    def default_value(self):
        """
        Gets the default_value of this PropertyDescriptor.
        The default value if a user-set value is not specified

        :return: The default_value of this PropertyDescriptor.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this PropertyDescriptor.
        The default value if a user-set value is not specified

        :param default_value: The default_value of this PropertyDescriptor.
        :type: str
        """

        self._default_value = default_value

    @property
    def required(self):
        """
        Gets the required of this PropertyDescriptor.
        Whether or not  the property is required for the component

        :return: The required of this PropertyDescriptor.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this PropertyDescriptor.
        Whether or not  the property is required for the component

        :param required: The required of this PropertyDescriptor.
        :type: bool
        """

        self._required = required

    @property
    def sensitive(self):
        """
        Gets the sensitive of this PropertyDescriptor.
        Whether or not  the value of the property is considered sensitive (e.g., passwords and keys)

        :return: The sensitive of this PropertyDescriptor.
        :rtype: bool
        """
        return self._sensitive

    @sensitive.setter
    def sensitive(self, sensitive):
        """
        Sets the sensitive of this PropertyDescriptor.
        Whether or not  the value of the property is considered sensitive (e.g., passwords and keys)

        :param sensitive: The sensitive of this PropertyDescriptor.
        :type: bool
        """

        self._sensitive = sensitive

    @property
    def expression_language_scope(self):
        """
        Gets the expression_language_scope of this PropertyDescriptor.
        The scope of expression language supported by this property

        :return: The expression_language_scope of this PropertyDescriptor.
        :rtype: str
        """
        return self._expression_language_scope

    @expression_language_scope.setter
    def expression_language_scope(self, expression_language_scope):
        """
        Sets the expression_language_scope of this PropertyDescriptor.
        The scope of expression language supported by this property

        :param expression_language_scope: The expression_language_scope of this PropertyDescriptor.
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
    def expression_language_scope_description(self):
        """
        Gets the expression_language_scope_description of this PropertyDescriptor.
        The description of the expression language scope supported by this property

        :return: The expression_language_scope_description of this PropertyDescriptor.
        :rtype: str
        """
        return self._expression_language_scope_description

    @expression_language_scope_description.setter
    def expression_language_scope_description(self, expression_language_scope_description):
        """
        Sets the expression_language_scope_description of this PropertyDescriptor.
        The description of the expression language scope supported by this property

        :param expression_language_scope_description: The expression_language_scope_description of this PropertyDescriptor.
        :type: str
        """

        self._expression_language_scope_description = expression_language_scope_description

    @property
    def type_provided_by_value(self):
        """
        Gets the type_provided_by_value of this PropertyDescriptor.
        Indicates that this property is for selecting a controller service of the specified type

        :return: The type_provided_by_value of this PropertyDescriptor.
        :rtype: DefinedType
        """
        return self._type_provided_by_value

    @type_provided_by_value.setter
    def type_provided_by_value(self, type_provided_by_value):
        """
        Sets the type_provided_by_value of this PropertyDescriptor.
        Indicates that this property is for selecting a controller service of the specified type

        :param type_provided_by_value: The type_provided_by_value of this PropertyDescriptor.
        :type: DefinedType
        """

        self._type_provided_by_value = type_provided_by_value

    @property
    def valid_regex(self):
        """
        Gets the valid_regex of this PropertyDescriptor.
        A regular expression that can be used to validate the value of this property

        :return: The valid_regex of this PropertyDescriptor.
        :rtype: str
        """
        return self._valid_regex

    @valid_regex.setter
    def valid_regex(self, valid_regex):
        """
        Sets the valid_regex of this PropertyDescriptor.
        A regular expression that can be used to validate the value of this property

        :param valid_regex: The valid_regex of this PropertyDescriptor.
        :type: str
        """

        self._valid_regex = valid_regex

    @property
    def validator(self):
        """
        Gets the validator of this PropertyDescriptor.
        Name of the validator used for this property descriptor

        :return: The validator of this PropertyDescriptor.
        :rtype: str
        """
        return self._validator

    @validator.setter
    def validator(self, validator):
        """
        Sets the validator of this PropertyDescriptor.
        Name of the validator used for this property descriptor

        :param validator: The validator of this PropertyDescriptor.
        :type: str
        """

        self._validator = validator

    @property
    def dynamic(self):
        """
        Gets the dynamic of this PropertyDescriptor.
        Whether or not the descriptor is for a dynamically added property

        :return: The dynamic of this PropertyDescriptor.
        :rtype: bool
        """
        return self._dynamic

    @dynamic.setter
    def dynamic(self, dynamic):
        """
        Sets the dynamic of this PropertyDescriptor.
        Whether or not the descriptor is for a dynamically added property

        :param dynamic: The dynamic of this PropertyDescriptor.
        :type: bool
        """

        self._dynamic = dynamic

    @property
    def resource_definition(self):
        """
        Gets the resource_definition of this PropertyDescriptor.
        Indicates that this property references external resources

        :return: The resource_definition of this PropertyDescriptor.
        :rtype: PropertyResourceDefinition
        """
        return self._resource_definition

    @resource_definition.setter
    def resource_definition(self, resource_definition):
        """
        Sets the resource_definition of this PropertyDescriptor.
        Indicates that this property references external resources

        :param resource_definition: The resource_definition of this PropertyDescriptor.
        :type: PropertyResourceDefinition
        """

        self._resource_definition = resource_definition

    @property
    def dependencies(self):
        """
        Gets the dependencies of this PropertyDescriptor.
        The dependencies that this property has on other properties

        :return: The dependencies of this PropertyDescriptor.
        :rtype: list[PropertyDependency]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies of this PropertyDescriptor.
        The dependencies that this property has on other properties

        :param dependencies: The dependencies of this PropertyDescriptor.
        :type: list[PropertyDependency]
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
        if not isinstance(other, PropertyDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
