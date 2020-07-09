# bloxonedhcpleases.LeaseCommandApi

All URIs are relative to *https://csp.infoblox.com/api/ddi/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lease_command_create**](LeaseCommandApi.md#lease_command_create) | **POST** /dhcp/lease_command | Create the LeaseCommand object.


# **lease_command_create**
> LeasesCreateLeaseCommandResponse lease_command_create(body)

Create the LeaseCommand object.

Use this method to create a LeaseCommand object. The LeaseCommand object is for performing an action on a lease.

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
api_instance = bloxonedhcpleases.LeaseCommandApi(bloxonedhcpleases.ApiClient(configuration))
body = bloxonedhcpleases.LeasesLeaseCommand() # LeasesLeaseCommand | 

try:
    # Create the LeaseCommand object.
    api_response = api_instance.lease_command_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaseCommandApi->lease_command_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeasesLeaseCommand**](LeasesLeaseCommand.md)|  | 

### Return type

[**LeasesCreateLeaseCommandResponse**](LeasesCreateLeaseCommandResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

