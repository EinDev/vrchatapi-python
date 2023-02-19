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


class GroupAnnouncement(object):
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
        'group_id': 'str',
        'author_id': 'str',
        'title': 'str',
        'text': 'str',
        'image_id': 'str',
        'image_url': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'groupId',
        'author_id': 'authorId',
        'title': 'title',
        'text': 'text',
        'image_id': 'imageId',
        'image_url': 'imageUrl',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, group_id=None, author_id=None, title=None, text=None, image_id=None, image_url=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """GroupAnnouncement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._group_id = None
        self._author_id = None
        self._title = None
        self._text = None
        self._image_id = None
        self._image_url = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if group_id is not None:
            self.group_id = group_id
        if author_id is not None:
            self.author_id = author_id
        self.title = title
        self.text = text
        if image_id is not None:
            self.image_id = image_id
        self.image_url = image_url
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this GroupAnnouncement.  # noqa: E501


        :return: The id of this GroupAnnouncement.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupAnnouncement.


        :param id: The id of this GroupAnnouncement.  # noqa: E501
        :type id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                id is not None and not re.search(r'gpos_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', id)):  # noqa: E501
            raise ValueError(r"Invalid value for `id`, must be a follow pattern or equal to `/gpos_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._id = id

    @property
    def group_id(self):
        """Gets the group_id of this GroupAnnouncement.  # noqa: E501


        :return: The group_id of this GroupAnnouncement.  # noqa: E501
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GroupAnnouncement.


        :param group_id: The group_id of this GroupAnnouncement.  # noqa: E501
        :type group_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                group_id is not None and not re.search(r'grp_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', group_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `group_id`, must be a follow pattern or equal to `/grp_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._group_id = group_id

    @property
    def author_id(self):
        """Gets the author_id of this GroupAnnouncement.  # noqa: E501

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :return: The author_id of this GroupAnnouncement.  # noqa: E501
        :rtype: str
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id):
        """Sets the author_id of this GroupAnnouncement.

        A users unique ID, usually in the form of `usr_c1644b5b-3ca4-45b4-97c6-a2a0de70d469`. Legacy players can have old IDs in the form of `8JoV9XEdpo`. The ID can never be changed.  # noqa: E501

        :param author_id: The author_id of this GroupAnnouncement.  # noqa: E501
        :type author_id: str
        """

        self._author_id = author_id

    @property
    def title(self):
        """Gets the title of this GroupAnnouncement.  # noqa: E501


        :return: The title of this GroupAnnouncement.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GroupAnnouncement.


        :param title: The title of this GroupAnnouncement.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def text(self):
        """Gets the text of this GroupAnnouncement.  # noqa: E501


        :return: The text of this GroupAnnouncement.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this GroupAnnouncement.


        :param text: The text of this GroupAnnouncement.  # noqa: E501
        :type text: str
        """

        self._text = text

    @property
    def image_id(self):
        """Gets the image_id of this GroupAnnouncement.  # noqa: E501


        :return: The image_id of this GroupAnnouncement.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this GroupAnnouncement.


        :param image_id: The image_id of this GroupAnnouncement.  # noqa: E501
        :type image_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                image_id is not None and not re.search(r'file_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', image_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `image_id`, must be a follow pattern or equal to `/file_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._image_id = image_id

    @property
    def image_url(self):
        """Gets the image_url of this GroupAnnouncement.  # noqa: E501


        :return: The image_url of this GroupAnnouncement.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this GroupAnnouncement.


        :param image_url: The image_url of this GroupAnnouncement.  # noqa: E501
        :type image_url: str
        """

        self._image_url = image_url

    @property
    def created_at(self):
        """Gets the created_at of this GroupAnnouncement.  # noqa: E501


        :return: The created_at of this GroupAnnouncement.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GroupAnnouncement.


        :param created_at: The created_at of this GroupAnnouncement.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this GroupAnnouncement.  # noqa: E501


        :return: The updated_at of this GroupAnnouncement.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GroupAnnouncement.


        :param updated_at: The updated_at of this GroupAnnouncement.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

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
        if not isinstance(other, GroupAnnouncement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GroupAnnouncement):
            return True

        return self.to_dict() != other.to_dict()
