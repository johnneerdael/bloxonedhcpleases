# LeasesLeaseCommand

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Required Field. IP Address in the form \&quot;a.b.c.d\&quot; within the IP space specified by &#39;space&#39; field. | 
**command** | **str** | The command to perform on the lease. It can have one of the following values: [clear]. The followings are descriptions for each commnd type: command          | description ---------------- | -------------------------------- clear            | Removes the lease defined by (space, address) from the DHCP server(s). This will NOT affect the client that issued the lease. | 
**space** | **str** | The resource identifier. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


