
## 3    User action

## 3.1  Set how to validate when adding friend

> POST  /user/authmode

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.2  Set how to validate when adding friend

> PUT  /user/authmode

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.3  Set avatar

> POST  /user/avatar

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| avatar|string||false|Avatar url|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.4  Set avatar

> PUT  /user/avatar

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| avatar|string||false|Avatar url|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.5  Set avatar in batch

> POST  /user/avatar/batch

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| list|array[object]||false||
|⇥ avatar|string||false|Avatar url|
|⇥ user_id|int32||false|User ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|array[object]||false|Result data|
|⇥ reason|string||false|Cause of failure|
|⇥ success|boolean||false|Success or not|
|⇥ user_id|int32||false|User ID|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.6  Set avatar in batch

> PUT  /user/avatar/batch

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| list|array[object]||false||
|⇥ avatar|string||false|Avatar url|
|⇥ user_id|int32||false|User ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|array[object]||false|Result data|
|⇥ reason|string||false|Cause of failure|
|⇥ success|boolean||false|Success or not|
|⇥ user_id|int32||false|User ID|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.7  Bind openid to account. (/app/wechat/bind is recommended for binding; /app/wechat/unbind is recommended for unbinding)

> GET  /user/bind_openid

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|open_id||open_id|
|type||type|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.8  Modify password

> POST  /user/change_password

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| new_password|string||false|new_password New password|
| old_password|string||false|old_password Old password|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.9  Device list

> GET  /user/device/list

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| cursor|string||false|Cursor, no cursor in returned result means the last page has been returned|
| data|array[object]||false|Result data|
|⇥ device_sn|int32||false||
|⇥ platform|int32||false|Device platform,1:ios, 2:android, 3:windows, 4:mac, 5:linux, 6:web|
|⇥ user_agent|string||false||
|⇥ user_id|int32||false|User ID|
| message|string||false|Error information, null means success|
| version|int32||false|Version|


### Interface Description
> 




## 3.10 Delete device

> POST  /user/device/remove

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|device_sn||device_sn|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.11 Delete device

> DELETE  /user/device/remove

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|device_sn||device_sn|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.12 **to-be-translate**

> PUT  /user/disable

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
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.13 Set whether to download thumbnails and files automatically

> POST  /user/download

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.14 Set whether to download thumbnails and files automatically

> PUT  /user/download

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.15 **to-be-translate**

> PUT  /user/enable

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
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.16 Kick specified device

> POST  /user/kick

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|device_sn||No device_sn passed means kicking all devices|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.17 Kick specified device

> PUT  /user/kick

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|device_sn||No device_sn passed means kicking all devices|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.18 Set mobile number

> POST  /user/mobile

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
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.19 Set mobile number

> PUT  /user/mobile

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
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.20 Set nickname

> POST  /user/nickname

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|nick_name||nick_name|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.21 Set nickname

> PUT  /user/nickname

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|nick_name||nick_name|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.22 **to-be-translate**

> GET  /user/online_status

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|**to-be-translate**|
|⇥ online|boolean||false|**to-be-translate**|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.23 Set private extension information

> POST  /user/private

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.24 Set private extension information

> PUT  /user/private

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.25 Get user information

> GET  /user/profile

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|User information|
|⇥ avatar|string||false|Avatar url|
|⇥ description|string||false|Description|
|⇥ email|string||false|Email|
|⇥ mobile|string||false|Mobile number|
|⇥ nick_name|string||false|Nickname|
|⇥ private_info|string||false|Private information, visible only to yourself|
|⇥ public_info|string||false|Public information, visible to both friends and strangers|
|⇥ user_id|int32||false|User ID|
|⇥ username|string||false|Username|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.26 Update user information

> POST  /user/profile

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| description|string||false|Description|
| nick_name|string||false|Nickname|
| private_info|string||false|Private information, visible only to yourself|
| public_info|string||false|Public information, visible to both friends and strangers|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.27 Update user information

> PUT  /user/profile

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| description|string||false|Description|
| nick_name|string||false|Nickname|
| private_info|string||false|Private information, visible only to yourself|
| public_info|string||false|Public information, visible to both friends and strangers|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.28 Update user information in batch

> POST  /user/profile/batch

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| list|array[object]||false||
|⇥ description|string||false|Description|
|⇥ nick_name|string||false|Nickname|
|⇥ private_info|string||false|Private information, visible only to yourself|
|⇥ public_info|string||false|Public information, visible to both friends and strangers|
|⇥ user_id|int32||false|User ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|array[object]||false|Result data|
|⇥ reason|string||false|Cause of failure|
|⇥ success|boolean||false|Success or not|
|⇥ user_id|int32||false|User ID|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.29 Update user information in batch

> PUT  /user/profile/batch

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| list|array[object]||false||
|⇥ description|string||false|Description|
|⇥ nick_name|string||false|Nickname|
|⇥ private_info|string||false|Private information, visible only to yourself|
|⇥ public_info|string||false|Public information, visible to both friends and strangers|
|⇥ user_id|int32||false|User ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|array[object]||false|Result data|
|⇥ reason|string||false|Cause of failure|
|⇥ success|boolean||false|Success or not|
|⇥ user_id|int32||false|User ID|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.30 Set public extension information

> POST  /user/public

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.31 Set public extension information

> PUT  /user/public

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.32 Set whether to turn off push

> POST  /user/push

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.33 Set whether to turn off push

> PUT  /user/push

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.34 Bind alias

> POST  /user/push/alias

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| alias|string||false|Alias|
| push_token|string||false|Push token|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.35 Set badge

> POST  /user/push/badge

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| badge|int32||false|badge|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.36 Set whether to turn off push details

> POST  /user/push/detail

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.37 Set whether to turn off push details

> PUT  /user/push/detail

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.38 Set push no-disturb time

> POST  /user/push/limit

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|no_push_end_hour||no_push_end_hour|
|no_push_start_hour||no_push_start_hour|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.39 Set push no-disturb time

> PUT  /user/push/limit

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|no_push_end_hour||no_push_end_hour|
|no_push_start_hour||no_push_start_hour|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.40 Set push nickname

> POST  /user/push/nickname

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.41 Set push nickname

> PUT  /user/push/nickname

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.42 Get tag

> GET  /user/push/tag

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|array[string]||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.43 Bind tag

> POST  /user/push/tag

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| tags|array[string]||false||

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.44 Unbind tag

> DELETE  /user/push/tag

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| tags|array[string]||false||

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.45 Delete all tags

> DELETE  /user/push/tag/all

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.46 Register user

> POST  /user/register

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| email|string||false|email|
| mobile|string||false|Mobile number|
| password|string||false||
| username|string||false|Username|
| verification_code|string||false|Verification code, used in combination with mobile phone or email|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|User settings information|
|⇥ auth_answer|string||false|Answer of verification question|
|⇥ auth_mode|int32||false|Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests|
|⇥ auth_question|string||false|Verification question|
|⇥ auto_download|boolean||false|Whether to download automatically|
|⇥ group_confirm|boolean||false|Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed|
|⇥ id|int32||false||
|⇥ no_push|boolean||false|Whether to turn off push|
|⇥ no_push_detail|boolean||false|Whether to push details|
|⇥ no_push_end_hour|int32||false|Start of push no-disturb time|
|⇥ no_push_start_hour|int32||false|End of push no-disturb time|
|⇥ no_sounds|boolean||false|Whether to mute when message received|
|⇥ push_nick_name|string||false|Push nickname|
|⇥ push_token|string||false|Push token|
|⇥ silence_end_time|int32||false|End of push no-reminder time|
|⇥ silence_start_time|int32||false|Start of push no-reminder time|
|⇥ user_id|int32||false|User ID|
|⇥ vibratory|boolean||false|Whether to vibrate when message received|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.47 Register user in batch

> POST  /user/register/batch

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| list|array[object]||false||
|⇥ password|string||false||
|⇥ username|string||false||

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|array[object]||false|Result data|
|⇥ reason|string||false|Cause of failure|
|⇥ success|boolean||false|Success or not|
|⇥ user_id|int32||false|User ID|
|⇥ username|string||false|Username|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.48 Register push user

> POST  /user/register/push

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| alias|string||false|Alias|
| device_guid|string||false|Device ID|
| password|string||false||
| push_token|string||false|Push token|
| sign|string||false|Signature|
| username|string||false||

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|User settings information|
|⇥ auth_answer|string||false|Answer of verification question|
|⇥ auth_mode|int32||false|Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests|
|⇥ auth_question|string||false|Verification question|
|⇥ auto_download|boolean||false|Whether to download automatically|
|⇥ group_confirm|boolean||false|Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed|
|⇥ id|int32||false||
|⇥ no_push|boolean||false|Whether to turn off push|
|⇥ no_push_detail|boolean||false|Whether to push details|
|⇥ no_push_end_hour|int32||false|Start of push no-disturb time|
|⇥ no_push_start_hour|int32||false|End of push no-disturb time|
|⇥ no_sounds|boolean||false|Whether to mute when message received|
|⇥ push_nick_name|string||false|Push nickname|
|⇥ push_token|string||false|Push token|
|⇥ silence_end_time|int32||false|End of push no-reminder time|
|⇥ silence_start_time|int32||false|Start of push no-reminder time|
|⇥ user_id|int32||false|User ID|
|⇥ vibratory|boolean||false|Whether to vibrate when message received|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.49 Register user

> POST  /user/register/v2

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| password|string||false||
| username|string||false||

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|User settings information|
|⇥ auth_answer|string||false|Answer of verification question|
|⇥ auth_mode|int32||false|Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests|
|⇥ auth_question|string||false|Verification question|
|⇥ auto_download|boolean||false|Whether to download automatically|
|⇥ group_confirm|boolean||false|Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed|
|⇥ id|int32||false||
|⇥ no_push|boolean||false|Whether to turn off push|
|⇥ no_push_detail|boolean||false|Whether to push details|
|⇥ no_push_end_hour|int32||false|Start of push no-disturb time|
|⇥ no_push_start_hour|int32||false|End of push no-disturb time|
|⇥ no_sounds|boolean||false|Whether to mute when message received|
|⇥ push_nick_name|string||false|Push nickname|
|⇥ push_token|string||false|Push token|
|⇥ silence_end_time|int32||false|End of push no-reminder time|
|⇥ silence_start_time|int32||false|Start of push no-reminder time|
|⇥ user_id|int32||false|User ID|
|⇥ vibratory|boolean||false|Whether to vibrate when message received|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.50 Get user settings

> GET  /user/settings

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|User settings information|
|⇥ auth_answer|string||false|Answer of verification question|
|⇥ auth_mode|int32||false|Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests|
|⇥ auth_question|string||false|Verification question|
|⇥ auto_download|boolean||false|Whether to download automatically|
|⇥ group_confirm|boolean||false|Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed|
|⇥ id|int32||false||
|⇥ no_push|boolean||false|Whether to turn off push|
|⇥ no_push_detail|boolean||false|Whether to push details|
|⇥ no_push_end_hour|int32||false|Start of push no-disturb time|
|⇥ no_push_start_hour|int32||false|End of push no-disturb time|
|⇥ no_sounds|boolean||false|Whether to mute when message received|
|⇥ push_nick_name|string||false|Push nickname|
|⇥ push_token|string||false|Push token|
|⇥ silence_end_time|int32||false|End of push no-reminder time|
|⇥ silence_start_time|int32||false|Start of push no-reminder time|
|⇥ user_id|int32||false|User ID|
|⇥ vibratory|boolean||false|Whether to vibrate when message received|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.51 Modify user settings

> POST  /user/settings

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| auth_answer|string||false|Answer of verification question|
| auth_mode|int32||false|Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests|
| auth_question|string||false|Verification question|
| auto_download|boolean||false|Whether to download automatically|
| group_confirm|boolean||false|Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed|
| id|int32||false||
| no_push|boolean||false|Whether to turn off push|
| no_push_detail|boolean||false|Whether to push details|
| no_push_end_hour|int32||false|Start of push no-disturb time|
| no_push_start_hour|int32||false|End of push no-disturb time|
| no_sounds|boolean||false|Whether to mute when message received|
| push_nick_name|string||false|Push nickname|
| push_token|string||false|Push token|
| silence_end_time|int32||false|End of push no-reminder time|
| silence_start_time|int32||false|Start of push no-reminder time|
| user_id|int32||false|User ID|
| vibratory|boolean||false|Whether to vibrate when message received|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.52 Modify user settings

> PUT  /user/settings

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| auth_answer|string||false|Answer of verification question|
| auth_mode|int32||false|Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests|
| auth_question|string||false|Verification question|
| auto_download|boolean||false|Whether to download automatically|
| group_confirm|boolean||false|Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed|
| id|int32||false||
| no_push|boolean||false|Whether to turn off push|
| no_push_detail|boolean||false|Whether to push details|
| no_push_end_hour|int32||false|Start of push no-disturb time|
| no_push_start_hour|int32||false|End of push no-disturb time|
| no_sounds|boolean||false|Whether to mute when message received|
| push_nick_name|string||false|Push nickname|
| push_token|string||false|Push token|
| silence_end_time|int32||false|End of push no-reminder time|
| silence_start_time|int32||false|Start of push no-reminder time|
| user_id|int32||false|User ID|
| vibratory|boolean||false|Whether to vibrate when message received|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.53 Set whether to mute sound alert for new message

> POST  /user/sounds

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.54 Set whether to mute sound alert for new message

> PUT  /user/sounds

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.55 Bind token

> POST  /user/token/bind

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| device_sn|int32||false|Device SN|
| device_token|string||false|device token|
| notifier_name|string||false|Certificate name|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.56 Bind token

> PUT  /user/token/bind

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| device_sn|int32||false|Device SN|
| device_token|string||false|device token|
| notifier_name|string||false|Certificate name|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.57 Unbind token

> POST  /user/token/unbind

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|deviceSn||deviceSn|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.58 Unbind token

> DELETE  /user/token/unbind

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|deviceSn||deviceSn|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.59 Modify username

> POST  /user/username

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
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.60 Modify username

> PUT  /user/username

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
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.61 Set whether to vibrate alert for new message

> POST  /user/vibratory

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 3.62 Set whether to vibrate alert for new message

> PUT  /user/vibratory

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|value||value|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|boolean||false|Result data|
| message|string||false|Error information, null means success|


### Interface Description
> 



