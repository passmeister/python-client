# swagger_client.PassApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_or_update_pass**](PassApi.md#create_or_update_pass) | **POST** /pass | This method creates or (if the pass id already exists) updates a pass, so you don&#39;t have to track ids and creation status of your passes.
[**delete_pass**](PassApi.md#delete_pass) | **DELETE** /pass | Delete pass by pass id.
[**get_pass**](PassApi.md#get_pass) | **GET** /pass | Get pass information by pass id.
[**pass_list**](PassApi.md#pass_list) | **GET** /pass/list | Retrieve the list of active pass ids for a given pass type.
[**pass_sync**](PassApi.md#pass_sync) | **POST** /pass/sync | Send updates to all active passes for a given pass type.


# **create_or_update_pass**
> create_or_update_pass(pass_type_id, pass_id=pass_id)

This method creates or (if the pass id already exists) updates a pass, so you don't have to track ids and creation status of your passes.

This method creates or (if the pass id already exists) updates a pass, so you don't have to track ids and creation status of your passes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PassApi()
pass_type_id = NULL # object | your pass type id, for example P963493 (Urban Fitness)
pass_id = NULL # object | id of the pass (provided by you when creating the pass or automatically set by passmeister) (optional)

try:
    # This method creates or (if the pass id already exists) updates a pass, so you don't have to track ids and creation status of your passes.
    api_instance.create_or_update_pass(pass_type_id, pass_id=pass_id)
except ApiException as e:
    print("Exception when calling PassApi->create_or_update_pass: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pass_type_id** | [**object**](.md)| your pass type id, for example P963493 (Urban Fitness) | 
 **pass_id** | [**object**](.md)| id of the pass (provided by you when creating the pass or automatically set by passmeister) | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pass**
> delete_pass(pass_type_id, pass_id)

Delete pass by pass id.

Delete pass by pass id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PassApi()
pass_type_id = NULL # object | your pass type id, for example P963493 (Urban Fitness)
pass_id = NULL # object | id of the pass

try:
    # Delete pass by pass id.
    api_instance.delete_pass(pass_type_id, pass_id)
except ApiException as e:
    print("Exception when calling PassApi->delete_pass: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pass_type_id** | [**object**](.md)| your pass type id, for example P963493 (Urban Fitness) | 
 **pass_id** | [**object**](.md)| id of the pass | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pass**
> get_pass(pass_type_id, pass_id)

Get pass information by pass id.

Get pass information by pass id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PassApi()
pass_type_id = NULL # object | your pass type id, for example P963493 (Urban Fitness)
pass_id = NULL # object | id of the pass

try:
    # Get pass information by pass id.
    api_instance.get_pass(pass_type_id, pass_id)
except ApiException as e:
    print("Exception when calling PassApi->get_pass: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pass_type_id** | [**object**](.md)| your pass type id, for example P963493 (Urban Fitness) | 
 **pass_id** | [**object**](.md)| id of the pass | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pass_list**
> pass_list(pass_type_id, page=page, limit=limit)

Retrieve the list of active pass ids for a given pass type.

Retrieve the list of active pass ids for a given pass type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PassApi()
pass_type_id = NULL # object | your pass type id, for example P963493 (Urban Fitness)
page = NULL # object |  (optional)
limit = NULL # object |  (optional)

try:
    # Retrieve the list of active pass ids for a given pass type.
    api_instance.pass_list(pass_type_id, page=page, limit=limit)
except ApiException as e:
    print("Exception when calling PassApi->pass_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pass_type_id** | [**object**](.md)| your pass type id, for example P963493 (Urban Fitness) | 
 **page** | [**object**](.md)|  | [optional] 
 **limit** | [**object**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pass_sync**
> pass_sync(pass_type_id)

Send updates to all active passes for a given pass type.

For example: you changed the pass type layout and now you want to update all installed passes. (The API call only confirms the scheduling of the updates, actual updating of passes on your customers devices can take a while.)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PassApi()
pass_type_id = NULL # object | your pass type id, for example P963493 (Urban Fitness)

try:
    # Send updates to all active passes for a given pass type.
    api_instance.pass_sync(pass_type_id)
except ApiException as e:
    print("Exception when calling PassApi->pass_sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pass_type_id** | [**object**](.md)| your pass type id, for example P963493 (Urban Fitness) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

