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


class Transaction(object):
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
        'id': 'str',
        'status': 'TransactionStatus',
        'subscription': 'Subscription',
        'sandbox': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'steam': 'TransactionSteamInfo',
        'agreement': 'TransactionAgreement',
        'error': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'subscription': 'subscription',
        'sandbox': 'sandbox',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'steam': 'steam',
        'agreement': 'agreement',
        'error': 'error'
    }

    def __init__(self, id=None, status=None, subscription=None, sandbox=False, created_at=None, updated_at=None, steam=None, agreement=None, error=None, local_vars_configuration=None):  # noqa: E501
        """Transaction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._status = None
        self._subscription = None
        self._sandbox = None
        self._created_at = None
        self._updated_at = None
        self._steam = None
        self._agreement = None
        self._error = None
        self.discriminator = None

        self.id = id
        self.status = status
        self.subscription = subscription
        self.sandbox = sandbox
        self.created_at = created_at
        self.updated_at = updated_at
        if steam is not None:
            self.steam = steam
        if agreement is not None:
            self.agreement = agreement
        self.error = error

    @property
    def id(self):
        """Gets the id of this Transaction.  # noqa: E501


        :return: The id of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Transaction.


        :param id: The id of this Transaction.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'txn_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/txn_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._id = id

    @property
    def status(self):
        """Gets the status of this Transaction.  # noqa: E501


        :return: The status of this Transaction.  # noqa: E501
        :rtype: TransactionStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Transaction.


        :param status: The status of this Transaction.  # noqa: E501
        :type status: TransactionStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def subscription(self):
        """Gets the subscription of this Transaction.  # noqa: E501


        :return: The subscription of this Transaction.  # noqa: E501
        :rtype: Subscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this Transaction.


        :param subscription: The subscription of this Transaction.  # noqa: E501
        :type subscription: Subscription
        """
        if self.local_vars_configuration.client_side_validation and subscription is None:  # noqa: E501
            raise ValueError("Invalid value for `subscription`, must not be `None`")  # noqa: E501

        self._subscription = subscription

    @property
    def sandbox(self):
        """Gets the sandbox of this Transaction.  # noqa: E501


        :return: The sandbox of this Transaction.  # noqa: E501
        :rtype: bool
        """
        return self._sandbox

    @sandbox.setter
    def sandbox(self, sandbox):
        """Sets the sandbox of this Transaction.


        :param sandbox: The sandbox of this Transaction.  # noqa: E501
        :type sandbox: bool
        """
        if self.local_vars_configuration.client_side_validation and sandbox is None:  # noqa: E501
            raise ValueError("Invalid value for `sandbox`, must not be `None`")  # noqa: E501

        self._sandbox = sandbox

    @property
    def created_at(self):
        """Gets the created_at of this Transaction.  # noqa: E501


        :return: The created_at of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Transaction.


        :param created_at: The created_at of this Transaction.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Transaction.  # noqa: E501


        :return: The updated_at of this Transaction.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Transaction.


        :param updated_at: The updated_at of this Transaction.  # noqa: E501
        :type updated_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def steam(self):
        """Gets the steam of this Transaction.  # noqa: E501


        :return: The steam of this Transaction.  # noqa: E501
        :rtype: TransactionSteamInfo
        """
        return self._steam

    @steam.setter
    def steam(self, steam):
        """Sets the steam of this Transaction.


        :param steam: The steam of this Transaction.  # noqa: E501
        :type steam: TransactionSteamInfo
        """

        self._steam = steam

    @property
    def agreement(self):
        """Gets the agreement of this Transaction.  # noqa: E501


        :return: The agreement of this Transaction.  # noqa: E501
        :rtype: TransactionAgreement
        """
        return self._agreement

    @agreement.setter
    def agreement(self, agreement):
        """Sets the agreement of this Transaction.


        :param agreement: The agreement of this Transaction.  # noqa: E501
        :type agreement: TransactionAgreement
        """

        self._agreement = agreement

    @property
    def error(self):
        """Gets the error of this Transaction.  # noqa: E501


        :return: The error of this Transaction.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Transaction.


        :param error: The error of this Transaction.  # noqa: E501
        :type error: str
        """
        if self.local_vars_configuration.client_side_validation and error is None:  # noqa: E501
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

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
        if not isinstance(other, Transaction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transaction):
            return True

        return self.to_dict() != other.to_dict()
