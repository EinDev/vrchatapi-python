"""
    VRChat API Documentation

    ![VRChat API Banner](https://vrchatapi.github.io/assets/img/api_banner_1500x400.png)  # Welcome to the VRChat API  Before we begin, we would like to state this is a **COMMUNITY DRIVEN PROJECT**. This means that everything you read on here was written by the community itself and is **not** officially supported by VRChat. The documentation is provided \"AS IS\", and any action you take towards VRChat is completely your own responsibility.  The documentation and additional libraries SHALL ONLY be used for applications interacting with VRChat's API in accordance with their [Terms of Service](https://github.com/VRChatAPI), and MUST NOT be used for modifying the client, \"avatar ripping\", or other illegal activities. Malicious usage or spamming the API may result in account termination. Certain parts of the API are also more sensitive than others, for example moderation, so please tread extra carefully and read the warnings when present.  ![Tupper Policy on API](https://i.imgur.com/yLlW7Ok.png)  Finally, use of the API using applications other than the approved methods (website, VRChat application, Unity SDK) is not officially supported. VRChat provides no guarantee or support for external applications using the API. Access to API endpoints may break **at any time, without notice**. Therefore, please **do not ping** VRChat Staff in the VRChat Discord if you are having API problems, as they do not provide API support. We will make a best effort in keeping this documentation and associated language libraries up to date, but things might be outdated or missing. If you find that something is no longer valid, please contact us on Discord or [create an issue](https://github.com/vrchatapi/specification/issues) and tell us so we can fix it.  # Getting Started  The VRChat API can be used to programmatically retrieve or update information regarding your profile, friends, avatars, worlds and more. The API consists of two parts, \"Photon\" which is only used in-game, and the \"Web API\" which is used by both the game and the website. This documentation focuses only on the Web API.  The API is designed around the REST ideology, providing semi-simple and usually predictable URIs to access and modify objects. Requests support standard HTTP methods like GET, PUT, POST, and DELETE and standard status codes. Response bodies are always UTF-8 encoded JSON objects, unless explicitly documented otherwise.  <div class=\"callout callout-error\">   <strong>🛑 Warning! Do not touch Photon!</strong><br>   Photon is only used by the in-game client and should <b>not</b> be touched. Doing so may result in permanent account termination. </div>  <div class=\"callout callout-info\">   <strong>ℹ️ API Key and Authentication</strong><br>   The API Key has always been the same and is currently <code>JlE5Jldo5Jibnk5O5hTx6XVqsJu4WJ26</code>.   Read <a href=\"#tag--authentication\">Authentication</a> for how to log in. </div>  # Using the API  For simply exploring what the API can do it is strongly recommended to download [Insomnia](https://insomnia.rest/download), a free and open-source API client that's great for sending requests to the API in an orderly fashion. Insomnia allows you to send data in the format that's required for VRChat's API. It is also possible to try out the API in your browser, by first logging in at [vrchat.com/home](https://vrchat.com/home/) and then going to [vrchat.com/api/1/auth/user](https://vrchat.com/api/1/auth/user), but the information will be much harder to work with.  For more permanent operation such as software development it is instead recommended to use one of the existing language SDKs. This community project maintains API libraries in several languages, which allows you to interact with the API with simple function calls rather than having to implement the HTTP protocol yourself. Most of these libraries are automatically generated from the API specification, sometimes with additional helpful wrapper code to make usage easier. This allows them to be almost automatically updated and expanded upon as soon as a new feature is introduced in the specification itself. The libraries can be found on [GitHub](https://github.com/vrchatapi) or following:  * [NodeJS (JavaScript)](https://www.npmjs.com/package/vrchat) * [Dart](https://pub.dev/packages/vrchat_dart) * [Rust](https://crates.io/crates/vrchatapi) * [C#](https://github.com/vrchatapi/vrchatapi-csharp) * [Python](https://github.com/vrchatapi/VRChatPython)  # Pagination  Most endpoints enforce pagination, meaning they will only return 10 entries by default, and never more than 100.<br> Using both the limit and offset parameters allows you to easily paginate through a large number of objects.  | Query Parameter | Type | Description | | ----------|--|------- | | `limit` | integer  | The number of objects to return. This value often defaults to 10. Highest limit is always 100.| | `offset` | integer  | A zero-based offset from the default object sorting.|  If a request returns fewer objects than the `limit` parameter, there are no more items available to return.  # Contribution  Do you want to get involved in the documentation effort? Do you want to help improve one of the language API libraries? This project is an [OPEN Open Source Project](https://openopensource.org)! This means that individuals making significant and valuable contributions are given commit-access to the project. It also means we are very open and welcoming of new people making contributions, unlike some more guarded open-source projects.  [![Discord](https://img.shields.io/static/v1?label=vrchatapi&message=discord&color=blueviolet&style=for-the-badge)](https://discord.gg/qjZE9C9fkB)  # noqa: E501

    The version of the OpenAPI document: 1.1.2
    Contact: me@ruby.js.org
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
from vrchatapi.model.file import File
from vrchatapi.model.inline_object3 import InlineObject3
from vrchatapi.model.inline_object4 import InlineObject4
from vrchatapi.model.inline_object5 import InlineObject5
from vrchatapi.model.inline_response2004 import InlineResponse2004
from vrchatapi.model.inline_response2005 import InlineResponse2005
from vrchatapi.model.success import Success


class FilesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_file(
            self,
            **kwargs
        ):
            """Create File  # noqa: E501

            Creates a new File object  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_file(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                inline_object3 (InlineObject3): [optional]
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
                File
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
            return self.call_with_http_info(**kwargs)

        self.create_file = _Endpoint(
            settings={
                'response_type': (File,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/file',
                'operation_id': 'create_file',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'inline_object3',
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
                    'inline_object3':
                        (InlineObject3,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'inline_object3': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_file
        )

        def __create_file_version(
            self,
            file_id,
            **kwargs
        ):
            """Create File Version  # noqa: E501

            Creates a new FileVersion. Once a Version has been created, proceed to the `/file/{fileId}/{versionId}/file/start` endpoint to start a file upload.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_file_version(file_id, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str):

            Keyword Args:
                inline_object4 (InlineObject4): [optional]
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
                File
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
            kwargs['file_id'] = \
                file_id
            return self.call_with_http_info(**kwargs)

        self.create_file_version = _Endpoint(
            settings={
                'response_type': (File,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/file/{fileId}',
                'operation_id': 'create_file_version',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'inline_object4',
                ],
                'required': [
                    'file_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'file_id',
                ]
            },
            root_map={
                'validations': {
                    ('file_id',): {

                        'regex': {
                            'pattern': r'file_[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'file_id':
                        (str,),
                    'inline_object4':
                        (InlineObject4,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                },
                'location_map': {
                    'file_id': 'path',
                    'inline_object4': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__create_file_version
        )

        def __delete_file(
            self,
            file_id,
            **kwargs
        ):
            """Delete File  # noqa: E501

            Deletes a File object.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_file(file_id, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str):

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
            kwargs['file_id'] = \
                file_id
            return self.call_with_http_info(**kwargs)

        self.delete_file = _Endpoint(
            settings={
                'response_type': (Success,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/file/{fileId}',
                'operation_id': 'delete_file',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                ],
                'required': [
                    'file_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'file_id',
                ]
            },
            root_map={
                'validations': {
                    ('file_id',): {

                        'regex': {
                            'pattern': r'file_[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'file_id':
                        (str,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                },
                'location_map': {
                    'file_id': 'path',
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
            api_client=api_client,
            callable=__delete_file
        )

        def __delete_file_version(
            self,
            file_id,
            version_id,
            **kwargs
        ):
            """Delete File Version  # noqa: E501

            Delete a specific version of a file. You can only delete the latest version.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_file_version(file_id, version_id, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str):
                version_id (int):

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
                File
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
            kwargs['file_id'] = \
                file_id
            kwargs['version_id'] = \
                version_id
            return self.call_with_http_info(**kwargs)

        self.delete_file_version = _Endpoint(
            settings={
                'response_type': (File,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/file/{fileId}/{versionId}',
                'operation_id': 'delete_file_version',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'version_id',
                ],
                'required': [
                    'file_id',
                    'version_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'file_id',
                    'version_id',
                ]
            },
            root_map={
                'validations': {
                    ('file_id',): {

                        'regex': {
                            'pattern': r'file_[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}',  # noqa: E501
                        },
                    },
                    ('version_id',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'file_id':
                        (str,),
                    'version_id':
                        (int,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                    'version_id': 'versionId',
                },
                'location_map': {
                    'file_id': 'path',
                    'version_id': 'path',
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
            api_client=api_client,
            callable=__delete_file_version
        )

        def __download_file_version(
            self,
            file_id,
            version_id,
            **kwargs
        ):
            """Download File Version  # noqa: E501

            Downloads the file with the provided version number.  **Version Note:** Version 0 is always when the file was created. The real data is usually always located in version 1 and up.  **Extension Note:** Files are not guaranteed to have a file extensions. UnityPackage files tends to have it, images through this endpoint do not. You are responsible for appending file extension from the `extension` field when neccesary.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.download_file_version(file_id, version_id, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str):
                version_id (int):

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
                None
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
            kwargs['file_id'] = \
                file_id
            kwargs['version_id'] = \
                version_id
            return self.call_with_http_info(**kwargs)

        self.download_file_version = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/file/{fileId}/{versionId}',
                'operation_id': 'download_file_version',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'version_id',
                ],
                'required': [
                    'file_id',
                    'version_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'file_id',
                    'version_id',
                ]
            },
            root_map={
                'validations': {
                    ('file_id',): {

                        'regex': {
                            'pattern': r'file_[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}',  # noqa: E501
                        },
                    },
                    ('version_id',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'file_id':
                        (str,),
                    'version_id':
                        (int,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                    'version_id': 'versionId',
                },
                'location_map': {
                    'file_id': 'path',
                    'version_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__download_file_version
        )

        def __finish_file_data_upload(
            self,
            file_id,
            version_id,
            file_type,
            **kwargs
        ):
            """Finish FileData Upload  # noqa: E501

            Finish an upload of a FileData. This will mark it as \"complete\". After uploading the `file` for Avatars and Worlds you then have to upload a `signature` file.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.finish_file_data_upload(file_id, version_id, file_type, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str):
                version_id (int):
                file_type (str):

            Keyword Args:
                inline_object5 (InlineObject5): [optional]
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
                File
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
            kwargs['file_id'] = \
                file_id
            kwargs['version_id'] = \
                version_id
            kwargs['file_type'] = \
                file_type
            return self.call_with_http_info(**kwargs)

        self.finish_file_data_upload = _Endpoint(
            settings={
                'response_type': (File,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/file/{fileId}/{versionId}/{fileType}/finish',
                'operation_id': 'finish_file_data_upload',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'version_id',
                    'file_type',
                    'inline_object5',
                ],
                'required': [
                    'file_id',
                    'version_id',
                    'file_type',
                ],
                'nullable': [
                ],
                'enum': [
                    'file_type',
                ],
                'validation': [
                    'file_id',
                    'version_id',
                ]
            },
            root_map={
                'validations': {
                    ('file_id',): {

                        'regex': {
                            'pattern': r'file_[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}',  # noqa: E501
                        },
                    },
                    ('version_id',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('file_type',): {

                        "FILE": "file",
                        "SIGNATURE": "signature",
                        "DELTA": "delta"
                    },
                },
                'openapi_types': {
                    'file_id':
                        (str,),
                    'version_id':
                        (int,),
                    'file_type':
                        (str,),
                    'inline_object5':
                        (InlineObject5,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                    'version_id': 'versionId',
                    'file_type': 'fileType',
                },
                'location_map': {
                    'file_id': 'path',
                    'version_id': 'path',
                    'file_type': 'path',
                    'inline_object5': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__finish_file_data_upload
        )

        def __get_file(
            self,
            file_id,
            **kwargs
        ):
            """Show File  # noqa: E501

            Shows general information about the \"File\" object. Each File can have several \"Version\"'s, and each Version can have multiple real files or \"Data\" blobs.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_file(file_id, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str):

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
                File
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
            kwargs['file_id'] = \
                file_id
            return self.call_with_http_info(**kwargs)

        self.get_file = _Endpoint(
            settings={
                'response_type': (File,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/file/{fileId}',
                'operation_id': 'get_file',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                ],
                'required': [
                    'file_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'file_id',
                ]
            },
            root_map={
                'validations': {
                    ('file_id',): {

                        'regex': {
                            'pattern': r'file_[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'file_id':
                        (str,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                },
                'location_map': {
                    'file_id': 'path',
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
            api_client=api_client,
            callable=__get_file
        )

        def __get_file_data_upload_status(
            self,
            file_id,
            version_id,
            file_type,
            **kwargs
        ):
            """Check FileData Upload Status  # noqa: E501

            Retrieves the upload status for file upload. Can currently only be accessed when `status` is `waiting`. Trying to access it on a file version already uploaded currently times out.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_file_data_upload_status(file_id, version_id, file_type, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str):
                version_id (int):
                file_type (str):

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
                InlineResponse2004
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
            kwargs['file_id'] = \
                file_id
            kwargs['version_id'] = \
                version_id
            kwargs['file_type'] = \
                file_type
            return self.call_with_http_info(**kwargs)

        self.get_file_data_upload_status = _Endpoint(
            settings={
                'response_type': (InlineResponse2004,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/file/{fileId}/{versionId}/{fileType}/status',
                'operation_id': 'get_file_data_upload_status',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'version_id',
                    'file_type',
                ],
                'required': [
                    'file_id',
                    'version_id',
                    'file_type',
                ],
                'nullable': [
                ],
                'enum': [
                    'file_type',
                ],
                'validation': [
                    'file_id',
                    'version_id',
                ]
            },
            root_map={
                'validations': {
                    ('file_id',): {

                        'regex': {
                            'pattern': r'file_[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}',  # noqa: E501
                        },
                    },
                    ('version_id',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('file_type',): {

                        "FILE": "file",
                        "SIGNATURE": "signature",
                        "DELTA": "delta"
                    },
                },
                'openapi_types': {
                    'file_id':
                        (str,),
                    'version_id':
                        (int,),
                    'file_type':
                        (str,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                    'version_id': 'versionId',
                    'file_type': 'fileType',
                },
                'location_map': {
                    'file_id': 'path',
                    'version_id': 'path',
                    'file_type': 'path',
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
            api_client=api_client,
            callable=__get_file_data_upload_status
        )

        def __get_files(
            self,
            **kwargs
        ):
            """List Files  # noqa: E501

            Returns a list of files  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_files(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                tag (str): Tag, for example \"icon\" or \"gallery\", not included by default.. [optional]
                user_id (str): UserID, will always generate a 500 permission error.. [optional]
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
                [File]
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
            return self.call_with_http_info(**kwargs)

        self.get_files = _Endpoint(
            settings={
                'response_type': ([File],),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/files',
                'operation_id': 'get_files',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'tag',
                    'user_id',
                    'n',
                    'offset',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'tag',
                    'n',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('tag',): {

                        'min_length': 1,
                    },
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
                    'tag':
                        (str,),
                    'user_id':
                        (str,),
                    'n':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'tag': 'tag',
                    'user_id': 'userId',
                    'n': 'n',
                    'offset': 'offset',
                },
                'location_map': {
                    'tag': 'query',
                    'user_id': 'query',
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
            api_client=api_client,
            callable=__get_files
        )

        def __start_file_data_upload(
            self,
            file_id,
            version_id,
            file_type,
            part_number,
            **kwargs
        ):
            """Start FileData Upload  # noqa: E501

            Starts an upload of a specific FilePart. This endpoint will return an AWS URL which you can PUT data to. You need to call this and receive a new AWS API URL for each `partNumber`. Please see AWS's REST documentation on \"PUT Object to S3\" on how to upload. Once all parts has been uploaded, proceed to `/finish` endpoint.  **Note:** `nextPartNumber` seems like it is always ignored. Despite it returning 0, first partNumber is always 1.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.start_file_data_upload(file_id, version_id, file_type, part_number, async_req=True)
            >>> result = thread.get()

            Args:
                file_id (str):
                version_id (int):
                file_type (str):
                part_number (int):

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
                InlineResponse2005
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
            kwargs['file_id'] = \
                file_id
            kwargs['version_id'] = \
                version_id
            kwargs['file_type'] = \
                file_type
            kwargs['part_number'] = \
                part_number
            return self.call_with_http_info(**kwargs)

        self.start_file_data_upload = _Endpoint(
            settings={
                'response_type': (InlineResponse2005,),
                'auth': [
                    'apiKeyCookie',
                    'authCookie'
                ],
                'endpoint_path': '/file/{fileId}/{versionId}/{fileType}/start',
                'operation_id': 'start_file_data_upload',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'version_id',
                    'file_type',
                    'part_number',
                ],
                'required': [
                    'file_id',
                    'version_id',
                    'file_type',
                    'part_number',
                ],
                'nullable': [
                ],
                'enum': [
                    'file_type',
                ],
                'validation': [
                    'file_id',
                    'version_id',
                    'part_number',
                ]
            },
            root_map={
                'validations': {
                    ('file_id',): {

                        'regex': {
                            'pattern': r'file_[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}',  # noqa: E501
                        },
                    },
                    ('version_id',): {

                        'inclusive_minimum': 1,
                    },
                    ('part_number',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                    ('file_type',): {

                        "FILE": "file",
                        "SIGNATURE": "signature",
                        "DELTA": "delta"
                    },
                },
                'openapi_types': {
                    'file_id':
                        (str,),
                    'version_id':
                        (int,),
                    'file_type':
                        (str,),
                    'part_number':
                        (int,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                    'version_id': 'versionId',
                    'file_type': 'fileType',
                    'part_number': 'partNumber',
                },
                'location_map': {
                    'file_id': 'path',
                    'version_id': 'path',
                    'file_type': 'path',
                    'part_number': 'query',
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
            api_client=api_client,
            callable=__start_file_data_upload
        )