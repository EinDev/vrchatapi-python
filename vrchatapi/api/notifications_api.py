"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.7.5
    Contact: me@ariesclark.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from vrchatapi.api_client import ApiClient, Endpoint as _Endpoint
from vrchatapi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from vrchatapi.model.error import Error
from vrchatapi.model.notification import Notification
from vrchatapi.model.success import Success


class NotificationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.accept_friend_request_endpoint = _Endpoint(
            settings={
                'response_type': (Success,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/auth/user/notifications/{notificationId}/accept',
                'operation_id': 'accept_friend_request',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'notification_id',
                ],
                'required': [
                    'notification_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'notification_id':
                        (str,),
                },
                'attribute_map': {
                    'notification_id': 'notificationId',
                },
                'location_map': {
                    'notification_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.clear_notifications_endpoint = _Endpoint(
            settings={
                'response_type': (Success,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/auth/user/notifications/clear',
                'operation_id': 'clear_notifications',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.delete_notification_endpoint = _Endpoint(
            settings={
                'response_type': (Notification,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/auth/user/notifications/{notificationId}/hide',
                'operation_id': 'delete_notification',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'notification_id',
                ],
                'required': [
                    'notification_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'notification_id':
                        (str,),
                },
                'attribute_map': {
                    'notification_id': 'notificationId',
                },
                'location_map': {
                    'notification_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_notifications_endpoint = _Endpoint(
            settings={
                'response_type': ([Notification],),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/auth/user/notifications',
                'operation_id': 'get_notifications',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'type',
                    'sent',
                    'hidden',
                    'after',
                    'n',
                    'offset',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'n',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('n',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                    ('offset',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'type':
                        (str,),
                    'sent':
                        (bool,),
                    'hidden':
                        (bool,),
                    'after':
                        (str,),
                    'n':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'type': 'type',
                    'sent': 'sent',
                    'hidden': 'hidden',
                    'after': 'after',
                    'n': 'n',
                    'offset': 'offset',
                },
                'location_map': {
                    'type': 'query',
                    'sent': 'query',
                    'hidden': 'query',
                    'after': 'query',
                    'n': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.mark_notification_as_read_endpoint = _Endpoint(
            settings={
                'response_type': (Notification,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/auth/user/notifications/{notificationId}/see',
                'operation_id': 'mark_notification_as_read',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'notification_id',
                ],
                'required': [
                    'notification_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'notification_id':
                        (str,),
                },
                'attribute_map': {
                    'notification_id': 'notificationId',
                },
                'location_map': {
                    'notification_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def accept_friend_request(
        self,
        notification_id,
        **kwargs
    ):
        """Accept Friend Request  # noqa: E501

        Accept a friend request by notification `frq_` ID. Friend requests can be found using the NotificationsAPI `getNotifications` by filtering of type `friendRequest`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.accept_friend_request(notification_id, async_req=True)
        >>> result = thread.get()

        Args:
            notification_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Success
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['notification_id'] = \
            notification_id
        return self.accept_friend_request_endpoint.call_with_http_info(**kwargs)

    def clear_notifications(
        self,
        **kwargs
    ):
        """Clear All Notifications  # noqa: E501

        Clear **all** notifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clear_notifications(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Success
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.clear_notifications_endpoint.call_with_http_info(**kwargs)

    def delete_notification(
        self,
        notification_id,
        **kwargs
    ):
        """Delete Notification  # noqa: E501

        Delete a notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_notification(notification_id, async_req=True)
        >>> result = thread.get()

        Args:
            notification_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Notification
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['notification_id'] = \
            notification_id
        return self.delete_notification_endpoint.call_with_http_info(**kwargs)

    def get_notifications(
        self,
        **kwargs
    ):
        """List Notifications  # noqa: E501

        Retrieve all of the current user's notifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_notifications(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            type (str): Only send notifications of this type (can use `all` for all).. [optional]
            sent (bool): Return notifications sent by the user. Must be false or omitted.. [optional]
            hidden (bool): Whether to return hidden or non-hidden notifications. True only allowed on type `friendRequest`.. [optional]
            after (str): Only return notifications sent after this Date. Ignored if type is `friendRequest`.. [optional]
            n (int): The number of objects to return.. [optional] if omitted the server will use the default value of 60
            offset (int): A zero-based offset from the default object sorting from where search results start.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [Notification]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.get_notifications_endpoint.call_with_http_info(**kwargs)

    def mark_notification_as_read(
        self,
        notification_id,
        **kwargs
    ):
        """Mark Notification As Read  # noqa: E501

        Mark a notification as seen.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mark_notification_as_read(notification_id, async_req=True)
        >>> result = thread.get()

        Args:
            notification_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Notification
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['notification_id'] = \
            notification_id
        return self.mark_notification_as_read_endpoint.call_with_http_info(**kwargs)

