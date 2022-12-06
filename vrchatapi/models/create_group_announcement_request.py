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


class CreateGroupAnnouncementRequest(object):
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
        'title': 'str',
        'text': 'str',
        'image_id': 'str',
        'send_notification': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'text': 'text',
        'image_id': 'imageId',
        'send_notification': 'sendNotification'
    }

    def __init__(self, title=None, text=None, image_id=None, send_notification=False, local_vars_configuration=None):  # noqa: E501
        """CreateGroupAnnouncementRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._text = None
        self._image_id = None
        self._send_notification = None
        self.discriminator = None

        self.title = title
        if text is not None:
            self.text = text
        if image_id is not None:
            self.image_id = image_id
        if send_notification is not None:
            self.send_notification = send_notification

    @property
    def title(self):
        """Gets the title of this CreateGroupAnnouncementRequest.  # noqa: E501

        Announcement title  # noqa: E501

        :return: The title of this CreateGroupAnnouncementRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateGroupAnnouncementRequest.

        Announcement title  # noqa: E501

        :param title: The title of this CreateGroupAnnouncementRequest.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) < 1):
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def text(self):
        """Gets the text of this CreateGroupAnnouncementRequest.  # noqa: E501

        Announcement text  # noqa: E501

        :return: The text of this CreateGroupAnnouncementRequest.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CreateGroupAnnouncementRequest.

        Announcement text  # noqa: E501

        :param text: The text of this CreateGroupAnnouncementRequest.  # noqa: E501
        :type text: str
        """
        if (self.local_vars_configuration.client_side_validation and
                text is not None and len(text) < 1):
            raise ValueError("Invalid value for `text`, length must be greater than or equal to `1`")  # noqa: E501

        self._text = text

    @property
    def image_id(self):
        """Gets the image_id of this CreateGroupAnnouncementRequest.  # noqa: E501


        :return: The image_id of this CreateGroupAnnouncementRequest.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this CreateGroupAnnouncementRequest.


        :param image_id: The image_id of this CreateGroupAnnouncementRequest.  # noqa: E501
        :type image_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                image_id is not None and not re.search(r'file_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}', image_id)):  # noqa: E501
            raise ValueError(r"Invalid value for `image_id`, must be a follow pattern or equal to `/file_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}/`")  # noqa: E501

        self._image_id = image_id

    @property
    def send_notification(self):
        """Gets the send_notification of this CreateGroupAnnouncementRequest.  # noqa: E501

        Send notification to group members.  # noqa: E501

        :return: The send_notification of this CreateGroupAnnouncementRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_notification

    @send_notification.setter
    def send_notification(self, send_notification):
        """Sets the send_notification of this CreateGroupAnnouncementRequest.

        Send notification to group members.  # noqa: E501

        :param send_notification: The send_notification of this CreateGroupAnnouncementRequest.  # noqa: E501
        :type send_notification: bool
        """

        self._send_notification = send_notification

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
        if not isinstance(other, CreateGroupAnnouncementRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateGroupAnnouncementRequest):
            return True

        return self.to_dict() != other.to_dict()
