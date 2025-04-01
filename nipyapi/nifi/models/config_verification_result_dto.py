"""
    NiFi Rest API

    The Rest API provides programmatic access to command and control a NiFi instance in real time. Start and                                             stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class ConfigVerificationResultDTO(object):
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
        'outcome': 'str',
        'verification_step_name': 'str',
        'explanation': 'str'
    }

    attribute_map = {
        'outcome': 'outcome',
        'verification_step_name': 'verificationStepName',
        'explanation': 'explanation'
    }

    def __init__(self, outcome=None, verification_step_name=None, explanation=None):
        """
        ConfigVerificationResultDTO - a model defined in Swagger
        """

        self._outcome = None
        self._verification_step_name = None
        self._explanation = None

        if outcome is not None:
          self.outcome = outcome
        if verification_step_name is not None:
          self.verification_step_name = verification_step_name
        if explanation is not None:
          self.explanation = explanation

    @property
    def outcome(self):
        """
        Gets the outcome of this ConfigVerificationResultDTO.
        The outcome of the verification

        :return: The outcome of this ConfigVerificationResultDTO.
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """
        Sets the outcome of this ConfigVerificationResultDTO.
        The outcome of the verification

        :param outcome: The outcome of this ConfigVerificationResultDTO.
        :type: str
        """
        allowed_values = ["SUCCESSFUL", "FAILED", "SKIPPED"]
        if outcome not in allowed_values:
            raise ValueError(
                "Invalid value for `outcome` ({0}), must be one of {1}"
                .format(outcome, allowed_values)
            )

        self._outcome = outcome

    @property
    def verification_step_name(self):
        """
        Gets the verification_step_name of this ConfigVerificationResultDTO.
        The name of the verification step

        :return: The verification_step_name of this ConfigVerificationResultDTO.
        :rtype: str
        """
        return self._verification_step_name

    @verification_step_name.setter
    def verification_step_name(self, verification_step_name):
        """
        Sets the verification_step_name of this ConfigVerificationResultDTO.
        The name of the verification step

        :param verification_step_name: The verification_step_name of this ConfigVerificationResultDTO.
        :type: str
        """

        self._verification_step_name = verification_step_name

    @property
    def explanation(self):
        """
        Gets the explanation of this ConfigVerificationResultDTO.
        An explanation of why the step was or was not successful

        :return: The explanation of this ConfigVerificationResultDTO.
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """
        Sets the explanation of this ConfigVerificationResultDTO.
        An explanation of why the step was or was not successful

        :param explanation: The explanation of this ConfigVerificationResultDTO.
        :type: str
        """

        self._explanation = explanation

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
        if not isinstance(other, ConfigVerificationResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
