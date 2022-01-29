
## 8    Friend management interface

## 8.1  Agree to add friend

> POST  /roster/accept

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|user_id||user_id|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.2  Agree to add friend

> PUT  /roster/accept

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|user_id||user_id|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.3  Apply to add friend

> POST  /roster/apply

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| alias|string||false|Name in comment|
| auth_answer|string||false|Answer of question|
| reason|string||false|Request description|
| user_id|int32||false|Invitee ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.4  Add friends in batch

> POST  /roster/apply/batch

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| alias|string||false|Name in comment|
| reason|string||false|Request description|
| user_id|int32||false|Invitee ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|Returned result for add friends in batch|
|⇥ fails|array[object]||false||
|⇥⇥ reason|string||false|Cause of failure|
|⇥⇥ user_id|int32||false|User ID|
|⇥ success|array[int32]||false||
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.5  List of friend requests

> GET  /roster/apply/list

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|cursor||cursor|
|limit||limit|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| cursor|string||false|Cursor, no cursor in returned result means the last page has been returned|
| data|array[object]||false|Result data|
|⇥ expired_time|int32||false|Expiration time|
|⇥ reason|string||false|Request description|
|⇥ status|int32||false||
|⇥ user_id|int32||false|User ID that initiate adding friend|
| message|string||false|Error information, null means success|
| version|int32||false|Version|


### Interface Description
> 




## 8.6  Add to blacklist

> POST  /roster/block

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|user_id||user_id|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.7  Add to blacklist

> PUT  /roster/block

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|user_id||user_id|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.8  List of blacklists

> GET  /roster/blocked_list

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|array[int32]||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.9  Reject friend request

> POST  /roster/decline

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| reason|string||false|Reason for rejection|
| user_id|int32||false|Rejected user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.10 Reject friend request

> PUT  /roster/decline

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| reason|string||false|Reason for rejection|
| user_id|int32||false|Rejected user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.11 Delete friend

> POST  /roster/delete

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|user_id||user_id|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.12 Delete friend

> DELETE  /roster/delete

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|user_id||user_id|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.13 Update friend extension information

> POST  /roster/ext

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| alias|string||false|Name in comment|
| ext|string||false|Extension information|
| mute_notification|boolean||false|Whether to receive message alert|
| user_id|int32||false|Friend user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.14 Update friend extension information

> PUT  /roster/ext

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| alias|string||false|Name in comment|
| ext|string||false|Extension information|
| mute_notification|boolean||false|Whether to receive message alert|
| user_id|int32||false|Friend user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.15 Search for users by ID

> GET  /roster/id

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|user_id||User ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|List of friends|
|⇥ alias|string||false||
|⇥ auth_mode|int32||false|Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests|
|⇥ auth_question|string||false|Verification question|
|⇥ avatar|string||false|Avatar|
|⇥ description|string||false|Description|
|⇥ ext|string||false||
|⇥ mute_notification|boolean||false||
|⇥ nick_name|string||false|Nickname or name|
|⇥ public_info|string||false|Public information, visible to both friends and strangers|
|⇥ relation|int32||false||
|⇥ user_id|int32||false|Friend user ID|
|⇥ username|string||false|Username|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.16 List of friends

> GET  /roster/list

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|cursor||cursor|
|limit||limit|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| cursor|string||false|Cursor, no cursor in returned result means the last page has been returned|
| data|array[int32]||false|Result data|
| message|string||false|Error information, null means success|
| version|int32||false|Version|


### Interface Description
> 




## 8.17 List of friend details

> POST  /roster/list

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| list|array[int32]||false||

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|array[object]||false|Result data|
|⇥ alias|string||false||
|⇥ auth_mode|int32||false|Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests|
|⇥ auth_question|string||false|Verification question|
|⇥ avatar|string||false|Avatar|
|⇥ description|string||false|Description|
|⇥ ext|string||false||
|⇥ mute_notification|boolean||false||
|⇥ nick_name|string||false|Nickname or name|
|⇥ public_info|string||false|Public information, visible to both friends and strangers|
|⇥ relation|int32||false||
|⇥ user_id|int32||false|Friend user ID|
|⇥ username|string||false|Username|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.18 Whether to allow messaging

> GET  /roster/may_message

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|roster_id||roster_id|
|user_id||user_id|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.19 Search for user by mobile number

> GET  /roster/mobile

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|mobile||mobile|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|List of friends|
|⇥ alias|string||false||
|⇥ auth_mode|int32||false|Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests|
|⇥ auth_question|string||false|Verification question|
|⇥ avatar|string||false|Avatar|
|⇥ description|string||false|Description|
|⇥ ext|string||false||
|⇥ mute_notification|boolean||false||
|⇥ nick_name|string||false|Nickname or name|
|⇥ public_info|string||false|Public information, visible to both friends and strangers|
|⇥ relation|int32||false||
|⇥ user_id|int32||false|Friend user ID|
|⇥ username|string||false|Username|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.20 Search for user by user ID

> GET  /roster/name

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|username||username|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|List of friends|
|⇥ alias|string||false||
|⇥ auth_mode|int32||false|Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests|
|⇥ auth_question|string||false|Verification question|
|⇥ avatar|string||false|Avatar|
|⇥ description|string||false|Description|
|⇥ ext|string||false||
|⇥ mute_notification|boolean||false||
|⇥ nick_name|string||false|Nickname or name|
|⇥ public_info|string||false|Public information, visible to both friends and strangers|
|⇥ relation|int32||false||
|⇥ user_id|int32||false|Friend user ID|
|⇥ username|string||false|Username|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.21 Remove from blacklist

> POST  /roster/unblock

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|user_id||user_id|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 8.22 Remove from blacklist

> DELETE  /roster/unblock

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|user_id||user_id|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




