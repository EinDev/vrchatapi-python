# vrchatapi.InviteApi

All URIs are relative to *https://api.vrchat.cloud/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invite_message**](InviteApi.md#get_invite_message) | **GET** /message/{userId}/message/{messageId} | Get Invite Messages
[**get_invite_messages**](InviteApi.md#get_invite_messages) | **GET** /message/{userId}/message | List Invite Messages
[**reset_invite_message**](InviteApi.md#reset_invite_message) | **DELETE** /message/{userId}/message/{messageId} | Reset Invite Message
[**update_invite_message**](InviteApi.md#update_invite_message) | **PUT** /message/{userId}/message/{messageId} | Update Invite Message


# **get_invite_message**
> InviteMessage get_invite_message(user_id, message_id)

Get Invite Messages

Returns a single Invite Message. This returns the exact same information but less than `getInviteMessages`. Admin Credentials are required to view messages of other users!

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import invite_api
from vrchatapi.model.inline_response400 import InlineResponse400
from vrchatapi.model.invite_message import InviteMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invite_api.InviteApi(api_client)
    user_id = "userId_example" # str | 
    message_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get Invite Messages
        api_response = api_instance.get_invite_message(user_id, message_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->get_invite_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **message_id** | **int**|  |

### Return type

[**InviteMessage**](InviteMessage.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single InviteMessage object. |  -  |
**400** | Error response when trying to update an Invite Message with invalid slot number. |  -  |
**401** | Error response due to missing authorization to perform that action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invite_messages**
> [InviteMessage] get_invite_messages(user_id)

List Invite Messages

Returns a list of all that users Invite Messages. Admin Credentials are required to view messages of other users!

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import invite_api
from vrchatapi.model.inline_response400 import InlineResponse400
from vrchatapi.model.invite_message import InviteMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invite_api.InviteApi(api_client)
    user_id = "userId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # List Invite Messages
        api_response = api_instance.get_invite_messages(user_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->get_invite_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |

### Return type

[**[InviteMessage]**](InviteMessage.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of InviteMessage objects. |  -  |
**400** | Error response when trying to update an Invite Message with invalid slot number. |  -  |
**401** | Error response due to missing authorization to perform that action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_invite_message**
> [InviteMessage] reset_invite_message(user_id, message_id)

Reset Invite Message

Resets a single Invite Message back to it's original message, and then returns a list of all of them. Admin Credentials are required to update messages of other users!  Resetting a message respects the rate-limit, but resetting it does not set the rate-limit to 60 like when editing it. It is possible to edit it right after resetting it. Trying to edit a message before the cooldown timer expires results in a 429 Too Fast Error.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import invite_api
from vrchatapi.model.inline_response400 import InlineResponse400
from vrchatapi.model.invite_message import InviteMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invite_api.InviteApi(api_client)
    user_id = "userId_example" # str | 
    message_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Reset Invite Message
        api_response = api_instance.reset_invite_message(user_id, message_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->reset_invite_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **message_id** | **int**|  |

### Return type

[**[InviteMessage]**](InviteMessage.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of InviteMessage objects. |  -  |
**400** | Error response when trying to update an Invite Message with invalid slot number. |  -  |
**401** | Error response due to missing authorization to perform that action. |  -  |
**429** | Error response when trying to update an Invite Message before the cooldown has expired. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invite_message**
> [InviteMessage] update_invite_message(user_id, message_id)

Update Invite Message

Updates a single Invite Message and then returns a list of all of them. Admin Credentials are required to update messages of other users!  Updating a message automatically sets the cooldown timer to 60 minutes. Trying to edit a message before the cooldown timer expires results in a 429 Too Fast Error.

### Example

* Api Key Authentication (apiKeyCookie):
* Api Key Authentication (authCookie):
```python
import time
import vrchatapi
from vrchatapi.api import invite_api
from vrchatapi.model.inline_response400 import InlineResponse400
from vrchatapi.model.invite_message import InviteMessage
from pprint import pprint
# Defining the host is optional and defaults to https://api.vrchat.cloud/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = vrchatapi.Configuration(
    host = "https://api.vrchat.cloud/api/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyCookie
configuration.api_key['apiKeyCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyCookie'] = 'Bearer'

# Configure API key authorization: authCookie
configuration.api_key['authCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with vrchatapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = invite_api.InviteApi(api_client)
    user_id = "userId_example" # str | 
    message_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Update Invite Message
        api_response = api_instance.update_invite_message(user_id, message_id)
        pprint(api_response)
    except vrchatapi.ApiException as e:
        print("Exception when calling InviteApi->update_invite_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  |
 **message_id** | **int**|  |

### Return type

[**[InviteMessage]**](InviteMessage.md)

### Authorization

[apiKeyCookie](../README.md#apiKeyCookie), [authCookie](../README.md#authCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of InviteMessage objects. |  -  |
**400** | Error response when trying to update an Invite Message with invalid slot number. |  -  |
**401** | Error response due to missing authorization to perform that action. |  -  |
**429** | Error response when trying to update an Invite Message before the cooldown has expired. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
