# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.11.1
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


class Instance(object):
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
        'active': 'bool',
        'can_request_invite': 'bool',
        'capacity': 'int',
        'client_number': 'str',
        'full': 'bool',
        'id': 'str',
        'instance_id': 'str',
        'location': 'str',
        'n_users': 'int',
        'name': 'str',
        'owner_id': 'str',
        'permanent': 'bool',
        'photon_region': 'Region',
        'platforms': 'InstancePlatforms',
        'region': 'Region',
        'secure_name': 'str',
        'short_name': 'str',
        'tags': 'list[str]',
        'type': 'InstanceType',
        'world_id': 'str',
        'hidden': 'str',
        'friends': 'str',
        'private': 'str'
    }

    attribute_map = {
        'active': 'active',
        'can_request_invite': 'canRequestInvite',
        'capacity': 'capacity',
        'client_number': 'clientNumber',
        'full': 'full',
        'id': 'id',
        'instance_id': 'instanceId',
        'location': 'location',
        'n_users': 'n_users',
        'name': 'name',
        'owner_id': 'ownerId',
        'permanent': 'permanent',
        'photon_region': 'photonRegion',
        'platforms': 'platforms',
        'region': 'region',
        'secure_name': 'secureName',
        'short_name': 'shortName',
        'tags': 'tags',
        'type': 'type',
        'world_id': 'worldId',
        'hidden': 'hidden',
        'friends': 'friends',
        'private': 'private'
    }

    def __init__(self, active=True, can_request_invite=True, capacity=None, client_number=None, full=False, id=None, instance_id=None, location=None, n_users=None, name=None, owner_id=None, permanent=False, photon_region=None, platforms=None, region=None, secure_name=None, short_name=None, tags=None, type=None, world_id=None, hidden=None, friends=None, private=None, local_vars_configuration=None):  # noqa: E501
        """Instance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._active = None
        self._can_request_invite = None
        self._capacity = None
        self._client_number = None
        self._full = None
        self._id = None
        self._instance_id = None
        self._location = None
        self._n_users = None
        self._name = None
        self._owner_id = None
        self._permanent = None
        self._photon_region = None
        self._platforms = None
        self._region = None
        self._secure_name = None
        self._short_name = None
        self._tags = None
        self._type = None
        self._world_id = None
        self._hidden = None
        self._friends = None
        self._private = None
        self.discriminator = None

        self.active = active
        self.can_request_invite = can_request_invite
        self.capacity = capacity
        self.client_number = client_number
        self.full = full
        self.id = id
        self.instance_id = instance_id
        self.location = location
        self.n_users = n_users
        self.name = name
        if owner_id is not None:
            self.owner_id = owner_id
        self.permanent = permanent
        self.photon_region = photon_region
        self.platforms = platforms
        self.region = region
        self.secure_name = secure_name
        if short_name is not None:
            self.short_name = short_name
        self.tags = tags
        self.type = type
        self.world_id = world_id
        if hidden is not None:
            self.hidden = hidden
        if friends is not None:
            self.friends = friends
        if private is not None:
            self.private = private

    @property
    def active(self):
        """Gets the active of this Instance.  # noqa: E501


        :return: The active of this Instance.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Instance.


        :param active: The active of this Instance.  # noqa: E501
        :type active: bool
        """
        if self.local_vars_configuration.client_side_validation and active is None:  # noqa: E501
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def can_request_invite(self):
        """Gets the can_request_invite of this Instance.  # noqa: E501


        :return: The can_request_invite of this Instance.  # noqa: E501
        :rtype: bool
        """
        return self._can_request_invite

    @can_request_invite.setter
    def can_request_invite(self, can_request_invite):
        """Sets the can_request_invite of this Instance.


        :param can_request_invite: The can_request_invite of this Instance.  # noqa: E501
        :type can_request_invite: bool
        """
        if self.local_vars_configuration.client_side_validation and can_request_invite is None:  # noqa: E501
            raise ValueError("Invalid value for `can_request_invite`, must not be `None`")  # noqa: E501

        self._can_request_invite = can_request_invite

    @property
    def capacity(self):
        """Gets the capacity of this Instance.  # noqa: E501


        :return: The capacity of this Instance.  # noqa: E501
        :rtype: int
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this Instance.


        :param capacity: The capacity of this Instance.  # noqa: E501
        :type capacity: int
        """
        if self.local_vars_configuration.client_side_validation and capacity is None:  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                capacity is not None and capacity < 0):  # noqa: E501
            raise ValueError("Invalid value for `capacity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._capacity = capacity

    @property
    def client_number(self):
        """Gets the client_number of this Instance.  # noqa: E501

        Always returns \"unknown\".  # noqa: E501

        :return: The client_number of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._client_number

    @client_number.setter
    def client_number(self, client_number):
        """Sets the client_number of this Instance.

        Always returns \"unknown\".  # noqa: E501

        :param client_number: The client_number of this Instance.  # noqa: E501
        :type client_number: str
        """
        if self.local_vars_configuration.client_side_validation and client_number is None:  # noqa: E501
            raise ValueError("Invalid value for `client_number`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                client_number is not None and len(client_number) < 1):
            raise ValueError("Invalid value for `client_number`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_number = client_number

    @property
    def full(self):
        """Gets the full of this Instance.  # noqa: E501


        :return: The full of this Instance.  # noqa: E501
        :rtype: bool
        """
        return self._full

    @full.setter
    def full(self, full):
        """Sets the full of this Instance.


        :param full: The full of this Instance.  # noqa: E501
        :type full: bool
        """
        if self.local_vars_configuration.client_side_validation and full is None:  # noqa: E501
            raise ValueError("Invalid value for `full`, must not be `None`")  # noqa: E501

        self._full = full

    @property
    def id(self):
        """Gets the id of this Instance.  # noqa: E501

        InstanceID can be \"offline\" on User profiles if you are not friends with that user and \"private\" if you are friends and user is in private instance.  # noqa: E501

        :return: The id of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Instance.

        InstanceID can be \"offline\" on User profiles if you are not friends with that user and \"private\" if you are friends and user is in private instance.  # noqa: E501

        :param id: The id of this Instance.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'(private|offline|(wrld|wld)_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}:(\d+)(~region\(([\w]+)\))?(~([\w]+)\(usr_([\w-]+)\)((\~canRequestInvite)?)(~region\(([\w].+)\))?~nonce\((.+)\))?)', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/(private|offline|(wrld|wld)_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}:(\d+)(~region\(([\w]+)\))?(~([\w]+)\(usr_([\w-]+)\)((\~canRequestInvite)?)(~region\(([\w].+)\))?~nonce\((.+)\))?)/`")  # noqa: E501

        self._id = id

    @property
    def instance_id(self):
        """Gets the instance_id of this Instance.  # noqa: E501


        :return: The instance_id of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this Instance.


        :param instance_id: The instance_id of this Instance.  # noqa: E501
        :type instance_id: str
        """
        if self.local_vars_configuration.client_side_validation and instance_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                instance_id is not None and len(instance_id) < 1):
            raise ValueError("Invalid value for `instance_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def location(self):
        """Gets the location of this Instance.  # noqa: E501

        InstanceID can be \"offline\" on User profiles if you are not friends with that user and \"private\" if you are friends and user is in private instance.  # noqa: E501

        :return: The location of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Instance.

        InstanceID can be \"offline\" on User profiles if you are not friends with that user and \"private\" if you are friends and user is in private instance.  # noqa: E501

        :param location: The location of this Instance.  # noqa: E501
        :type location: str
        """
        if self.local_vars_configuration.client_side_validation and location is None:  # noqa: E501
            raise ValueError("Invalid value for `location`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                location is not None and not re.search(r'(private|offline|(wrld|wld)_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}:(\d+)(~region\(([\w]+)\))?(~([\w]+)\(usr_([\w-]+)\)((\~canRequestInvite)?)(~region\(([\w].+)\))?~nonce\((.+)\))?)', location)):  # noqa: E501
            raise ValueError(r"Invalid value for `location`, must be a follow pattern or equal to `/(private|offline|(wrld|wld)_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}:(\d+)(~region\(([\w]+)\))?(~([\w]+)\(usr_([\w-]+)\)((\~canRequestInvite)?)(~region\(([\w].+)\))?~nonce\((.+)\))?)/`")  # noqa: E501

        self._location = location

    @property
    def n_users(self):
        """Gets the n_users of this Instance.  # noqa: E501


        :return: The n_users of this Instance.  # noqa: E501
        :rtype: int
        """
        return self._n_users

    @n_users.setter
    def n_users(self, n_users):
        """Sets the n_users of this Instance.


        :param n_users: The n_users of this Instance.  # noqa: E501
        :type n_users: int
        """
        if self.local_vars_configuration.client_side_validation and n_users is None:  # noqa: E501
            raise ValueError("Invalid value for `n_users`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                n_users is not None and n_users < 0):  # noqa: E501
            raise ValueError("Invalid value for `n_users`, must be a value greater than or equal to `0`")  # noqa: E501

        self._n_users = n_users

    @property
    def name(self):
        """Gets the name of this Instance.  # noqa: E501


        :return: The name of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Instance.


        :param name: The name of this Instance.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def owner_id(self):
        """Gets the owner_id of this Instance.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The owner_id of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this Instance.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param owner_id: The owner_id of this Instance.  # noqa: E501
        :type owner_id: str
        """

        self._owner_id = owner_id

    @property
    def permanent(self):
        """Gets the permanent of this Instance.  # noqa: E501


        :return: The permanent of this Instance.  # noqa: E501
        :rtype: bool
        """
        return self._permanent

    @permanent.setter
    def permanent(self, permanent):
        """Sets the permanent of this Instance.


        :param permanent: The permanent of this Instance.  # noqa: E501
        :type permanent: bool
        """
        if self.local_vars_configuration.client_side_validation and permanent is None:  # noqa: E501
            raise ValueError("Invalid value for `permanent`, must not be `None`")  # noqa: E501

        self._permanent = permanent

    @property
    def photon_region(self):
        """Gets the photon_region of this Instance.  # noqa: E501


        :return: The photon_region of this Instance.  # noqa: E501
        :rtype: Region
        """
        return self._photon_region

    @photon_region.setter
    def photon_region(self, photon_region):
        """Sets the photon_region of this Instance.


        :param photon_region: The photon_region of this Instance.  # noqa: E501
        :type photon_region: Region
        """
        if self.local_vars_configuration.client_side_validation and photon_region is None:  # noqa: E501
            raise ValueError("Invalid value for `photon_region`, must not be `None`")  # noqa: E501

        self._photon_region = photon_region

    @property
    def platforms(self):
        """Gets the platforms of this Instance.  # noqa: E501


        :return: The platforms of this Instance.  # noqa: E501
        :rtype: InstancePlatforms
        """
        return self._platforms

    @platforms.setter
    def platforms(self, platforms):
        """Sets the platforms of this Instance.


        :param platforms: The platforms of this Instance.  # noqa: E501
        :type platforms: InstancePlatforms
        """
        if self.local_vars_configuration.client_side_validation and platforms is None:  # noqa: E501
            raise ValueError("Invalid value for `platforms`, must not be `None`")  # noqa: E501

        self._platforms = platforms

    @property
    def region(self):
        """Gets the region of this Instance.  # noqa: E501


        :return: The region of this Instance.  # noqa: E501
        :rtype: Region
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Instance.


        :param region: The region of this Instance.  # noqa: E501
        :type region: Region
        """
        if self.local_vars_configuration.client_side_validation and region is None:  # noqa: E501
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def secure_name(self):
        """Gets the secure_name of this Instance.  # noqa: E501


        :return: The secure_name of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._secure_name

    @secure_name.setter
    def secure_name(self, secure_name):
        """Sets the secure_name of this Instance.


        :param secure_name: The secure_name of this Instance.  # noqa: E501
        :type secure_name: str
        """
        if self.local_vars_configuration.client_side_validation and secure_name is None:  # noqa: E501
            raise ValueError("Invalid value for `secure_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                secure_name is not None and len(secure_name) < 1):
            raise ValueError("Invalid value for `secure_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._secure_name = secure_name

    @property
    def short_name(self):
        """Gets the short_name of this Instance.  # noqa: E501


        :return: The short_name of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this Instance.


        :param short_name: The short_name of this Instance.  # noqa: E501
        :type short_name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                short_name is not None and len(short_name) < 1):
            raise ValueError("Invalid value for `short_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._short_name = short_name

    @property
    def tags(self):
        """Gets the tags of this Instance.  # noqa: E501

        The tags array on Instances usually contain the language tags of the people in the instance.   # noqa: E501

        :return: The tags of this Instance.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Instance.

        The tags array on Instances usually contain the language tags of the people in the instance.   # noqa: E501

        :param tags: The tags of this Instance.  # noqa: E501
        :type tags: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def type(self):
        """Gets the type of this Instance.  # noqa: E501


        :return: The type of this Instance.  # noqa: E501
        :rtype: InstanceType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Instance.


        :param type: The type of this Instance.  # noqa: E501
        :type type: InstanceType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def world_id(self):
        """Gets the world_id of this Instance.  # noqa: E501

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :return: The world_id of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._world_id

    @world_id.setter
    def world_id(self, world_id):
        """Sets the world_id of this Instance.

        WorldID be \"offline\" on User profiles if you are not friends with that user.  # noqa: E501

        :param world_id: The world_id of this Instance.  # noqa: E501
        :type world_id: str
        """
        if self.local_vars_configuration.client_side_validation and world_id is None:  # noqa: E501
            raise ValueError("Invalid value for `world_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                world_id is not None and not re.search(r'(^$|offline|(wrld|wld)_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})', world_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `world_id`, must be a follow pattern or equal to `/(^$|offline|(wrld|wld)_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})/`")  # noqa: E501

        self._world_id = world_id

    @property
    def hidden(self):
        """Gets the hidden of this Instance.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The hidden of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Instance.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param hidden: The hidden of this Instance.  # noqa: E501
        :type hidden: str
        """

        self._hidden = hidden

    @property
    def friends(self):
        """Gets the friends of this Instance.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The friends of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._friends

    @friends.setter
    def friends(self, friends):
        """Sets the friends of this Instance.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param friends: The friends of this Instance.  # noqa: E501
        :type friends: str
        """

        self._friends = friends

    @property
    def private(self):
        """Gets the private of this Instance.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The private of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this Instance.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param private: The private of this Instance.  # noqa: E501
        :type private: str
        """

        self._private = private

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
        if not isinstance(other, Instance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Instance):
            return True

        return self.to_dict() != other.to_dict()
