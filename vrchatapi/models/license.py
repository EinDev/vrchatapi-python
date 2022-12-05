# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.10.0
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


class License(object):
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
        'for_id': 'str',
        'for_type': 'LicenseType',
        'for_name': 'str',
        'for_action': 'LicenseAction'
    }

    attribute_map = {
        'for_id': 'forId',
        'for_type': 'forType',
        'for_name': 'forName',
        'for_action': 'forAction'
    }

    def __init__(self, for_id=None, for_type=None, for_name=None, for_action=None, local_vars_configuration=None):  # noqa: E501
        """License - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._for_id = None
        self._for_type = None
        self._for_name = None
        self._for_action = None
        self.discriminator = None

        self.for_id = for_id
        self.for_type = for_type
        self.for_name = for_name
        self.for_action = for_action

    @property
    def for_id(self):
        """Gets the for_id of this License.  # noqa: E501

        Either a AvatarID, LicenseGroupID, PermissionID or ProductID. This depends on the `forType` field.  # noqa: E501

        :return: The for_id of this License.  # noqa: E501
        :rtype: str
        """
        return self._for_id

    @for_id.setter
    def for_id(self, for_id):
        """Sets the for_id of this License.

        Either a AvatarID, LicenseGroupID, PermissionID or ProductID. This depends on the `forType` field.  # noqa: E501

        :param for_id: The for_id of this License.  # noqa: E501
        :type for_id: str
        """
        if self.local_vars_configuration.client_side_validation and for_id is None:  # noqa: E501
            raise ValueError("Invalid value for `for_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                for_id is not None and len(for_id) < 1):
            raise ValueError("Invalid value for `for_id`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                for_id is not None and not re.search(r'(avtr|lgrp|prms|prod)_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', for_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `for_id`, must be a follow pattern or equal to `/(avtr|lgrp|prms|prod)_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._for_id = for_id

    @property
    def for_type(self):
        """Gets the for_type of this License.  # noqa: E501


        :return: The for_type of this License.  # noqa: E501
        :rtype: LicenseType
        """
        return self._for_type

    @for_type.setter
    def for_type(self, for_type):
        """Sets the for_type of this License.


        :param for_type: The for_type of this License.  # noqa: E501
        :type for_type: LicenseType
        """
        if self.local_vars_configuration.client_side_validation and for_type is None:  # noqa: E501
            raise ValueError("Invalid value for `for_type`, must not be `None`")  # noqa: E501

        self._for_type = for_type

    @property
    def for_name(self):
        """Gets the for_name of this License.  # noqa: E501


        :return: The for_name of this License.  # noqa: E501
        :rtype: str
        """
        return self._for_name

    @for_name.setter
    def for_name(self, for_name):
        """Sets the for_name of this License.


        :param for_name: The for_name of this License.  # noqa: E501
        :type for_name: str
        """
        if self.local_vars_configuration.client_side_validation and for_name is None:  # noqa: E501
            raise ValueError("Invalid value for `for_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                for_name is not None and len(for_name) < 1):
            raise ValueError("Invalid value for `for_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._for_name = for_name

    @property
    def for_action(self):
        """Gets the for_action of this License.  # noqa: E501


        :return: The for_action of this License.  # noqa: E501
        :rtype: LicenseAction
        """
        return self._for_action

    @for_action.setter
    def for_action(self, for_action):
        """Sets the for_action of this License.


        :param for_action: The for_action of this License.  # noqa: E501
        :type for_action: LicenseAction
        """
        if self.local_vars_configuration.client_side_validation and for_action is None:  # noqa: E501
            raise ValueError("Invalid value for `for_action`, must not be `None`")  # noqa: E501

        self._for_action = for_action

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
        if not isinstance(other, License):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, License):
            return True

        return self.to_dict() != other.to_dict()
