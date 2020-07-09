# bloxonedhcpleases.GlobalLeaseApi

All URIs are relative to *https://csp.infoblox.com/api/ddi/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**global_lease_read**](GlobalLeaseApi.md#global_lease_read) | **GET** /dhcp/global_lease | Read the Global Lease object.
[**global_lease_read2**](GlobalLeaseApi.md#global_lease_read2) | **GET** /dhcp/global_lease/{id} | Read the Global Lease object.
[**global_lease_update**](GlobalLeaseApi.md#global_lease_update) | **PATCH** /dhcp/global_lease/{id} | 


# **global_lease_read**
> LeasesReadGlobalLeaseResponse global_lease_read(fields=fields)

Read the Global Lease object.

Use this method to read the Global Lease configuration object.

### Example
```python
from __future__ import print_function
import time
import bloxonedhcpleases
from bloxonedhcpleases.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonedhcpleases.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonedhcpleases.GlobalLeaseApi(bloxonedhcpleases.ApiClient(configuration))
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read the Global Lease object.
    api_response = api_instance.global_lease_read(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalLeaseApi->global_lease_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**LeasesReadGlobalLeaseResponse**](LeasesReadGlobalLeaseResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_lease_read2**
> LeasesReadGlobalLeaseResponse global_lease_read2(id, fields=fields)

Read the Global Lease object.

Use this method to read the Global Lease configuration object.

### Example
```python
from __future__ import print_function
import time
import bloxonedhcpleases
from bloxonedhcpleases.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonedhcpleases.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonedhcpleases.GlobalLeaseApi(bloxonedhcpleases.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
fields = 'fields_example' # str |   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         (optional)

try:
    # Read the Global Lease object.
    api_response = api_instance.global_lease_read2(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalLeaseApi->global_lease_read2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **fields** | **str**|   A collection of response resources can be transformed by specifying a set of JSON tags to be returned. For a “flat” resource, the tag name is straightforward. If field selection is allowed on non-flat hierarchical resources, the service should implement a qualified naming scheme such as dot-qualification to reference data down the hierarchy. If a resource does not have the specified tag, the tag does not appear in the output resource.  Specify this parameter as a comma-separated list of JSON tag names.         | [optional] 

### Return type

[**LeasesReadGlobalLeaseResponse**](LeasesReadGlobalLeaseResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **global_lease_update**
> LeasesUpdateGlobalLeaseResponse global_lease_update(id, body)



### Example
```python
from __future__ import print_function
import time
import bloxonedhcpleases
from bloxonedhcpleases.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = bloxonedhcpleases.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = bloxonedhcpleases.GlobalLeaseApi(bloxonedhcpleases.ApiClient(configuration))
id = 'id_example' # str | An application specific resource identity of a resource
body = bloxonedhcpleases.LeasesGlobalLease() # LeasesGlobalLease | 

try:
    api_response = api_instance.global_lease_update(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GlobalLeaseApi->global_lease_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An application specific resource identity of a resource | 
 **body** | [**LeasesGlobalLease**](LeasesGlobalLease.md)|  | 

### Return type

[**LeasesUpdateGlobalLeaseResponse**](LeasesUpdateGlobalLeaseResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

