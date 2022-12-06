# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.10.1
    Contact: me@ariesclark.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from vrchatapi.configuration import Configuration


class APIHealth(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'ok': 'bool',
        'server_name': 'str',
        'build_version_tag': 'str'
    }

    attribute_map = {
        'ok': 'ok',
        'server_name': 'serverName',
        'build_version_tag': 'buildVersionTag'
    }

    def __init__(self, ok=None, server_name=None, build_version_tag=None, local_vars_configuration=None):  # noqa: E501
        """APIHealth - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._ok = None
        self._server_name = None
        self._build_version_tag = None
        self.discriminator = None

        self.ok = ok
        self.server_name = server_name
        self.build_version_tag = build_version_tag

    @property
    def ok(self):
        """Gets the ok of this APIHealth.  # noqa: E501


        :return: The ok of this APIHealth.  # noqa: E501
        :rtype: bool
        """
        return self._ok

    @ok.setter
    def ok(self, ok):
        """Sets the ok of this APIHealth.


        :param ok: The ok of this APIHealth.  # noqa: E501
        :type ok: bool
        """
        if self.local_vars_configuration.client_side_validation and ok is None:  # noqa: E501
            raise ValueError("Invalid value for `ok`, must not be `None`")  # noqa: E501

        self._ok = ok

    @property
    def server_name(self):
        """Gets the server_name of this APIHealth.  # noqa: E501


        :return: The server_name of this APIHealth.  # noqa: E501
        :rtype: str
        """
        return self._server_name

    @server_name.setter
    def server_name(self, server_name):
        """Sets the server_name of this APIHealth.


        :param server_name: The server_name of this APIHealth.  # noqa: E501
        :type server_name: str
        """
        if self.local_vars_configuration.client_side_validation and server_name is None:  # noqa: E501
            raise ValueError("Invalid value for `server_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                server_name is not None and len(server_name) < 1):
            raise ValueError("Invalid value for `server_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._server_name = server_name

    @property
    def build_version_tag(self):
        """Gets the build_version_tag of this APIHealth.  # noqa: E501


        :return: The build_version_tag of this APIHealth.  # noqa: E501
        :rtype: str
        """
        return self._build_version_tag

    @build_version_tag.setter
    def build_version_tag(self, build_version_tag):
        """Sets the build_version_tag of this APIHealth.


        :param build_version_tag: The build_version_tag of this APIHealth.  # noqa: E501
        :type build_version_tag: str
        """
        if self.local_vars_configuration.client_side_validation and build_version_tag is None:  # noqa: E501
            raise ValueError("Invalid value for `build_version_tag`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                build_version_tag is not None and len(build_version_tag) < 1):
            raise ValueError("Invalid value for `build_version_tag`, length must be greater than or equal to `1`")  # noqa: E501

        self._build_version_tag = build_version_tag

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, APIHealth):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIHealth):
            return True

        return self.to_dict() != other.to_dict()
