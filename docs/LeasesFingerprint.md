# LeasesFingerprint

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_class** | **str** | The resource identifier. | [optional] 
**comment** | **str** | Comment of the fingerprint if any. | [optional] 
**defined_by** | **str** | If this fingerprint was defined by the user or if it was defined by Infoblox. | [optional] 
**id** | **str** | The resource identifier. | [optional] 
**inheritance_sources** | [**LeasesFingerprintInheritance**](LeasesFingerprintInheritance.md) | Inheritance implementation for share_fingerprint field. | [optional] 
**name** | **str** | Name of the fingerprint. | [optional] 
**rules** | [**list[LeasesFingerprintRule]**](LeasesFingerprintRule.md) |  | [optional] 
**share_fingerprint** | **bool** | If this fingerprint should be shared with Infoblox.  This only makes sense for custom fingerprints. The default for custom fingerprints is \&quot;shared\&quot; or true. The value could be inherited from dhcp/global_lease. | [optional] 
**tags** | [**TypesJSONValue**](TypesJSONValue.md) | Tagging specifics. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


