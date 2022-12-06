# coding: utf-8

"""
    VRChat API Documentation


    The version of the OpenAPI document: 1.10.1
    Contact: me@ariesclark.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from vrchatapi.api_client import ApiClient
from vrchatapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class NotificationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def accept_friend_request(self, notification_id, **kwargs):  # noqa: E501
        """Accept Friend Request  # noqa: E501

        Accept a friend request by notification `frq_` ID. Friend requests can be found using the NotificationsAPI `getNotifications` by filtering of type `friendRequest`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.accept_friend_request(notification_id, async_req=True)
        >>> result = thread.get()

        :param notification_id: Must be a valid notification ID. (required)
        :type notification_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Success
        """
        kwargs['_return_http_data_only'] = True
        return self.accept_friend_request_with_http_info(notification_id, **kwargs)  # noqa: E501

    def accept_friend_request_with_http_info(self, notification_id, **kwargs):  # noqa: E501
        """Accept Friend Request  # noqa: E501

        Accept a friend request by notification `frq_` ID. Friend requests can be found using the NotificationsAPI `getNotifications` by filtering of type `friendRequest`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.accept_friend_request_with_http_info(notification_id, async_req=True)
        >>> result = thread.get()

        :param notification_id: Must be a valid notification ID. (required)
        :type notification_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Success, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'notification_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method accept_friend_request" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'notification_id' is set
        if self.api_client.client_side_validation and local_var_params.get('notification_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `notification_id` when calling `accept_friend_request`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'notification_id' in local_var_params:
            path_params['notificationId'] = local_var_params['notification_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyCookie', 'authCookie']  # noqa: E501

        response_types_map = {
            200: "Success",
            401: "Error",
            404: "Error",
        }

        return self.api_client.call_api(
            '/auth/user/notifications/{notificationId}/accept', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def clear_notifications(self, **kwargs):  # noqa: E501
        """Clear All Notifications  # noqa: E501

        Clear **all** notifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clear_notifications(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Success
        """
        kwargs['_return_http_data_only'] = True
        return self.clear_notifications_with_http_info(**kwargs)  # noqa: E501

    def clear_notifications_with_http_info(self, **kwargs):  # noqa: E501
        """Clear All Notifications  # noqa: E501

        Clear **all** notifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clear_notifications_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Success, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clear_notifications" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyCookie', 'authCookie']  # noqa: E501

        response_types_map = {
            200: "Success",
            401: "Error",
        }

        return self.api_client.call_api(
            '/auth/user/notifications/clear', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def delete_notification(self, notification_id, **kwargs):  # noqa: E501
        """Delete Notification  # noqa: E501

        Delete a notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_notification(notification_id, async_req=True)
        >>> result = thread.get()

        :param notification_id: Must be a valid notification ID. (required)
        :type notification_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Notification
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_notification_with_http_info(notification_id, **kwargs)  # noqa: E501

    def delete_notification_with_http_info(self, notification_id, **kwargs):  # noqa: E501
        """Delete Notification  # noqa: E501

        Delete a notification.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_notification_with_http_info(notification_id, async_req=True)
        >>> result = thread.get()

        :param notification_id: Must be a valid notification ID. (required)
        :type notification_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Notification, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'notification_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_notification" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'notification_id' is set
        if self.api_client.client_side_validation and local_var_params.get('notification_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `notification_id` when calling `delete_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'notification_id' in local_var_params:
            path_params['notificationId'] = local_var_params['notification_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyCookie', 'authCookie']  # noqa: E501

        response_types_map = {
            200: "Notification",
            401: "Error",
        }

        return self.api_client.call_api(
            '/auth/user/notifications/{notificationId}/hide', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_notifications(self, **kwargs):  # noqa: E501
        """List Notifications  # noqa: E501

        Retrieve all of the current user's notifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_notifications(async_req=True)
        >>> result = thread.get()

        :param type: Only send notifications of this type (can use `all` for all). This parameter no longer does anything, and is deprecated.
        :type type: str
        :param sent: Return notifications sent by the user. Must be false or omitted.
        :type sent: bool
        :param hidden: Whether to return hidden or non-hidden notifications. True only allowed on type `friendRequest`.
        :type hidden: bool
        :param after: Only return notifications sent after this Date. Ignored if type is `friendRequest`.
        :type after: str
        :param n: The number of objects to return.
        :type n: int
        :param offset: A zero-based offset from the default object sorting from where search results start.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: list[Notification]
        """
        kwargs['_return_http_data_only'] = True
        return self.get_notifications_with_http_info(**kwargs)  # noqa: E501

    def get_notifications_with_http_info(self, **kwargs):  # noqa: E501
        """List Notifications  # noqa: E501

        Retrieve all of the current user's notifications.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_notifications_with_http_info(async_req=True)
        >>> result = thread.get()

        :param type: Only send notifications of this type (can use `all` for all). This parameter no longer does anything, and is deprecated.
        :type type: str
        :param sent: Return notifications sent by the user. Must be false or omitted.
        :type sent: bool
        :param hidden: Whether to return hidden or non-hidden notifications. True only allowed on type `friendRequest`.
        :type hidden: bool
        :param after: Only return notifications sent after this Date. Ignored if type is `friendRequest`.
        :type after: str
        :param n: The number of objects to return.
        :type n: int
        :param offset: A zero-based offset from the default object sorting from where search results start.
        :type offset: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(list[Notification], status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'type',
            'sent',
            'hidden',
            'after',
            'n',
            'offset'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notifications" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'n' in local_var_params and local_var_params['n'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `n` when calling `get_notifications`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and 'n' in local_var_params and local_var_params['n'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `n` when calling `get_notifications`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `offset` when calling `get_notifications`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get('type') is not None:  # noqa: E501
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if local_var_params.get('sent') is not None:  # noqa: E501
            query_params.append(('sent', local_var_params['sent']))  # noqa: E501
        if local_var_params.get('hidden') is not None:  # noqa: E501
            query_params.append(('hidden', local_var_params['hidden']))  # noqa: E501
        if local_var_params.get('after') is not None:  # noqa: E501
            query_params.append(('after', local_var_params['after']))  # noqa: E501
        if local_var_params.get('n') is not None:  # noqa: E501
            query_params.append(('n', local_var_params['n']))  # noqa: E501
        if local_var_params.get('offset') is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyCookie', 'authCookie']  # noqa: E501

        response_types_map = {
            200: "list[Notification]",
            401: "Error",
        }

        return self.api_client.call_api(
            '/auth/user/notifications', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def mark_notification_as_read(self, notification_id, **kwargs):  # noqa: E501
        """Mark Notification As Read  # noqa: E501

        Mark a notification as seen.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mark_notification_as_read(notification_id, async_req=True)
        >>> result = thread.get()

        :param notification_id: Must be a valid notification ID. (required)
        :type notification_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: Notification
        """
        kwargs['_return_http_data_only'] = True
        return self.mark_notification_as_read_with_http_info(notification_id, **kwargs)  # noqa: E501

    def mark_notification_as_read_with_http_info(self, notification_id, **kwargs):  # noqa: E501
        """Mark Notification As Read  # noqa: E501

        Mark a notification as seen.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.mark_notification_as_read_with_http_info(notification_id, async_req=True)
        >>> result = thread.get()

        :param notification_id: Must be a valid notification ID. (required)
        :type notification_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(Notification, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'notification_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mark_notification_as_read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'notification_id' is set
        if self.api_client.client_side_validation and local_var_params.get('notification_id') is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `notification_id` when calling `mark_notification_as_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'notification_id' in local_var_params:
            path_params['notificationId'] = local_var_params['notification_id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyCookie', 'authCookie']  # noqa: E501

        response_types_map = {
            200: "Notification",
            401: "Error",
        }

        return self.api_client.call_api(
            '/auth/user/notifications/{notificationId}/see', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
