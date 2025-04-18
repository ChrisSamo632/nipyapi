"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 1.28.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class BuildInfo(object):
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
        'build_tool': 'str',
        'build_flags': 'str',
        'build_branch': 'str',
        'build_tag': 'str',
        'build_revision': 'str',
        'built': 'int',
        'built_by': 'str'
    }

    attribute_map = {
        'build_tool': 'buildTool',
        'build_flags': 'buildFlags',
        'build_branch': 'buildBranch',
        'build_tag': 'buildTag',
        'build_revision': 'buildRevision',
        'built': 'built',
        'built_by': 'builtBy'
    }

    def __init__(self, build_tool=None, build_flags=None, build_branch=None, build_tag=None, build_revision=None, built=None, built_by=None):
        """
        BuildInfo - a model defined in Swagger
        """

        self._build_tool = None
        self._build_flags = None
        self._build_branch = None
        self._build_tag = None
        self._build_revision = None
        self._built = None
        self._built_by = None

        if build_tool is not None:
          self.build_tool = build_tool
        if build_flags is not None:
          self.build_flags = build_flags
        if build_branch is not None:
          self.build_branch = build_branch
        if build_tag is not None:
          self.build_tag = build_tag
        if build_revision is not None:
          self.build_revision = build_revision
        if built is not None:
          self.built = built
        if built_by is not None:
          self.built_by = built_by

    @property
    def build_tool(self):
        """
        Gets the build_tool of this BuildInfo.
        The tool used to build the version of the bundle

        :return: The build_tool of this BuildInfo.
        :rtype: str
        """
        return self._build_tool

    @build_tool.setter
    def build_tool(self, build_tool):
        """
        Sets the build_tool of this BuildInfo.
        The tool used to build the version of the bundle

        :param build_tool: The build_tool of this BuildInfo.
        :type: str
        """

        self._build_tool = build_tool

    @property
    def build_flags(self):
        """
        Gets the build_flags of this BuildInfo.
        The flags used to build the version of the bundle

        :return: The build_flags of this BuildInfo.
        :rtype: str
        """
        return self._build_flags

    @build_flags.setter
    def build_flags(self, build_flags):
        """
        Sets the build_flags of this BuildInfo.
        The flags used to build the version of the bundle

        :param build_flags: The build_flags of this BuildInfo.
        :type: str
        """

        self._build_flags = build_flags

    @property
    def build_branch(self):
        """
        Gets the build_branch of this BuildInfo.
        The branch used to build the version of the bundle

        :return: The build_branch of this BuildInfo.
        :rtype: str
        """
        return self._build_branch

    @build_branch.setter
    def build_branch(self, build_branch):
        """
        Sets the build_branch of this BuildInfo.
        The branch used to build the version of the bundle

        :param build_branch: The build_branch of this BuildInfo.
        :type: str
        """

        self._build_branch = build_branch

    @property
    def build_tag(self):
        """
        Gets the build_tag of this BuildInfo.
        The tag used to build the version of the bundle

        :return: The build_tag of this BuildInfo.
        :rtype: str
        """
        return self._build_tag

    @build_tag.setter
    def build_tag(self, build_tag):
        """
        Sets the build_tag of this BuildInfo.
        The tag used to build the version of the bundle

        :param build_tag: The build_tag of this BuildInfo.
        :type: str
        """

        self._build_tag = build_tag

    @property
    def build_revision(self):
        """
        Gets the build_revision of this BuildInfo.
        The revision used to build the version of the bundle

        :return: The build_revision of this BuildInfo.
        :rtype: str
        """
        return self._build_revision

    @build_revision.setter
    def build_revision(self, build_revision):
        """
        Sets the build_revision of this BuildInfo.
        The revision used to build the version of the bundle

        :param build_revision: The build_revision of this BuildInfo.
        :type: str
        """

        self._build_revision = build_revision

    @property
    def built(self):
        """
        Gets the built of this BuildInfo.
        The timestamp the version of the bundle was built

        :return: The built of this BuildInfo.
        :rtype: int
        """
        return self._built

    @built.setter
    def built(self, built):
        """
        Sets the built of this BuildInfo.
        The timestamp the version of the bundle was built

        :param built: The built of this BuildInfo.
        :type: int
        """

        self._built = built

    @property
    def built_by(self):
        """
        Gets the built_by of this BuildInfo.
        The identity of the user that performed the build

        :return: The built_by of this BuildInfo.
        :rtype: str
        """
        return self._built_by

    @built_by.setter
    def built_by(self, built_by):
        """
        Sets the built_by of this BuildInfo.
        The identity of the user that performed the build

        :param built_by: The built_by of this BuildInfo.
        :type: str
        """

        self._built_by = built_by

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
        if not isinstance(other, BuildInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
