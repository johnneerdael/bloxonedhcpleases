# LeasesLease

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Read-only Field. IP Address in the form \&quot;a.b.c.d\&quot; of the Lease object. This address will be marked as \&quot;leased\&quot; in IPAM while the Lease exists. | [optional] 
**client_id** | **str** | Read-only Field. Client ID. It might be empty. | [optional] 
**ends** | **datetime** | Read-only Field. Time when the Lease will expire. | [optional] 
**fingerprint** | **str** | Read-only Field. String of a fingerprint. | [optional] 
**fingerprint_processed** | **str** | The field indicates if this lease has been fingerprinted yet. | [optional] 
**ha_group** | **str** | The resource identifier. | [optional] 
**hardware** | **str** | Read-only Field. Hardware Address. It consists of six groups of two hex digits in lower-case separated by colons, e.g. \&quot;aa:bb:cc:dd:ee:ff\&quot;. | [optional] 
**host** | **str** | The resource identifier. | [optional] 
**hostname** | **str** | Read-only Field. Client Hostname. It is a fully qualified domain name, consisting of a series of labels separated by dots, e.g. \&quot;www.infoblox.com\&quot;. It might be empty. | [optional] 
**last_updated** | **datetime** | Read-only Field. Time when the Lease was last updated. | [optional] 
**options** | **str** | Read-only data. DHCP options in JSON format. | [optional] 
**space** | **str** | The resource identifier. | [optional] 
**starts** | **datetime** | Read-only Field. Time when the Lease was issued. | [optional] 
**state** | **str** | Read-only Field. The state of the lease and its value could be \&quot;used\&quot; or \&quot;abandoned\&quot;. Leases with a state of deleted are not returned to queries, they are for internal use. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


