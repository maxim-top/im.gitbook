# 1 User action{#user}

## 1.1 Set how to validate when adding friend{#put__user_authmode}

> PUT /user/authmode

> POST /user/authmode

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| value | int32 | true | value |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.2 Set avatar{#put__user_avatar}

> PUT /user/avatar

> POST /user/avatar

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| avatar | string | true |  | Avatar url |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.3 Set avatar in batch{#put__user_avatar_batch}

> PUT /user/avatar/batch

> POST /user/avatar/batch

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| list | array[object] | false |  |  |
|⇥ avatar | string | true |  | Avatar url |
|⇥ user_id | int64 | false |  | User ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ reason | string | Cause of failure |
|⇥ success | boolean | Success or not |
|⇥ user_id | int64 | User ID |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.4 Modify password{#post__user_change_password}

> POST /user/change_password

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| new_password | string | false |  | new_password New password |
| old_password | string | false |  | old_password Old password |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.5 Device list{#get__user_device_list}

> GET /user/device/list

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| cursor | string | Cursor, no cursor in returned result means the last page has been returned |
| data | array[object] | Result data |
|⇥ device_sn | int32 |  |
|⇥ platform | int32 | Device platform,1:ios, 2:android, 3:windows, 4:mac, 5:linux, 6:web |
|⇥ user_agent | string |  |
|⇥ user_id | int64 | User ID |
| message | string | Error information, null means success |
| version | int64 | Version |
#### Interface Description
> 

## 1.6 Delete device{#delete__user_device_remove}

> DELETE /user/device/remove

> POST /user/device/remove

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| device_sn | int32 | true | device_sn |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.7 Banned user{#put__user_disable}

> PUT /user/disable

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| list | array[int64] | false |  |  |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.8 Set whether to download thumbnails and files automatically{#put__user_download}

> PUT /user/download

> POST /user/download

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| value | boolean | true | value |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.9 Unbanned user{#put__user_enable}

> PUT /user/enable

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| list | array[int64] | false |  |  |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.10 Kick specified device{#put__user_kick}

> PUT /user/kick

> POST /user/kick

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| device_sn | int32 | false | No device_sn passed means kicking all devices |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.11 List all users in the APP{#get__user_list}

> GET /user/list

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| page_num | int32 | false | page_num |
| page_size | int32 | false | page_size |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ status | int32 | 0-normal,1-forbidden |
|⇥ user_id | int64 |  |
|⇥ username | string |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.12 Set mobile number{#put__user_mobile}

> PUT /user/mobile

> POST /user/mobile

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| mobile | string | true | mobile |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.13 Set nickname{#put__user_nickname}

> PUT /user/nickname

> POST /user/nickname

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| nick_name | string | true | nick_name |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.14 Query user online status{#get__user_online_status}

> GET /user/online_status

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ online | boolean | Online or not: true - online, false - offline |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.15 Set private extension information{#put__user_private}

> PUT /user/private

> POST /user/private

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
|  | string | true |  |  |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.16 Get user information{#get__user_profile}

> GET /user/profile

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ avatar | string | Avatar url |
|⇥ description | string | Description |
|⇥ email | string | Email |
|⇥ mobile | string | Mobile number |
|⇥ nick_name | string | Nickname |
|⇥ private_info | string | Private information, visible only to yourself |
|⇥ public_info | string | Public information, visible to both friends and strangers |
|⇥ user_id | int64 | User ID |
|⇥ username | string | Username |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.17 Update user information{#put__user_profile}

> PUT /user/profile

> POST /user/profile

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| description | string | false |  | Description |
| nick_name | string | false |  | Nickname |
| private_info | string | false |  | Private information, visible only to yourself |
| public_info | string | false |  | Public information, visible to both friends and strangers |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.18 Update user information in batch{#put__user_profile_batch}

> PUT /user/profile/batch

> POST /user/profile/batch

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| list | array[object] | false |  |  |
|⇥ description | string | false |  | Description |
|⇥ nick_name | string | false |  | Nickname |
|⇥ private_info | string | false |  | Private information, visible only to yourself |
|⇥ public_info | string | false |  | Public information, visible to both friends and strangers |
|⇥ user_id | int64 | false |  | User ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ reason | string | Cause of failure |
|⇥ success | boolean | Success or not |
|⇥ user_id | int64 | User ID |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.19 Set public extension information{#put__user_public}

> PUT /user/public

> POST /user/public

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
|  | string | true |  |  |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.20 Set whether to turn off push{#put__user_push}

> PUT /user/push

> POST /user/push

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| value | boolean | true | value |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.21 Bind alias{#post__user_push_alias}

> POST /user/push/alias

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| alias | string | true |  | Alias |
| push_token | string | false |  | Push token |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.22 Set badge{#post__user_push_badge}

> POST /user/push/badge

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| badge | int32 | true |  | badge |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.23 Set whether to turn off push details{#put__user_push_detail}

> PUT /user/push/detail

> POST /user/push/detail

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| value | boolean | true | value |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.24 Set push no-disturb time{#put__user_push_limit}

> PUT /user/push/limit

> POST /user/push/limit

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| no_push_end_hour | int32 | true | no_push_end_hour |
| no_push_start_hour | int32 | true | no_push_start_hour |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.25 Set push nickname{#put__user_push_nickname}

> PUT /user/push/nickname

> POST /user/push/nickname

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| value | string | true | value |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.26 Get tag{#get__user_push_tag}

> GET /user/push/tag

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[string] | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.27 Bind tag{#post__user_push_tag}

> POST /user/push/tag

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| tags | array[string] | false |  |  |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.28 Unbind tag{#delete__user_push_tag}

> DELETE /user/push/tag

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| tags | array[string] | false |  |  |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.29 Delete all tags{#delete__user_push_tag_all}

> DELETE /user/push/tag/all

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.30 Register user in batch{#post__user_register_batch}

> POST /user/register/batch

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| list | array[object] | false |  |  |
|⇥ password | string | true |  |  |
|⇥ username | string | true |  |  |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ reason | string | Cause of failure |
|⇥ success | boolean | Success or not |
|⇥ user_id | int64 | User ID |
|⇥ username | string | Username |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.31 Register push user{#post__user_register_push}

> POST /user/register/push

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| alias | string | false |  | Alias |
| device_guid | string | false |  | Device ID |
| password | string | true |  |  |
| push_token | string | false |  | Push token |
| sign | string | false |  | Signature |
| username | string | true |  |  |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ auth_answer | string | Answer of verification question |
|⇥ auth_mode | int32 | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
|⇥ auth_question | string | Verification question |
|⇥ auto_download | boolean | Whether to download automatically |
|⇥ group_confirm | boolean | Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed |
|⇥ id | int64 |  |
|⇥ no_push | boolean | Whether to turn off push |
|⇥ no_push_detail | boolean | Whether to push details |
|⇥ no_push_end_hour | int32 | Start of push no-disturb time |
|⇥ no_push_start_hour | int32 | End of push no-disturb time |
|⇥ no_sounds | boolean | Whether to mute when message received |
|⇥ push_nick_name | string | Push nickname |
|⇥ push_token | string | Push token |
|⇥ silence_end_time | int32 | End of push no-reminder time |
|⇥ silence_start_time | int32 | Start of push no-reminder time |
|⇥ user_id | int64 | User ID |
|⇥ vibratory | boolean | Whether to vibrate when message received |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.32 Register user{#post__user_register_v2}

> POST /user/register/v2

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| password | string | true |  |  |
| username | string | true |  |  |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ auth_answer | string | Answer of verification question |
|⇥ auth_mode | int32 | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
|⇥ auth_question | string | Verification question |
|⇥ auto_download | boolean | Whether to download automatically |
|⇥ group_confirm | boolean | Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed |
|⇥ id | int64 |  |
|⇥ no_push | boolean | Whether to turn off push |
|⇥ no_push_detail | boolean | Whether to push details |
|⇥ no_push_end_hour | int32 | Start of push no-disturb time |
|⇥ no_push_start_hour | int32 | End of push no-disturb time |
|⇥ no_sounds | boolean | Whether to mute when message received |
|⇥ push_nick_name | string | Push nickname |
|⇥ push_token | string | Push token |
|⇥ silence_end_time | int32 | End of push no-reminder time |
|⇥ silence_start_time | int32 | Start of push no-reminder time |
|⇥ user_id | int64 | User ID |
|⇥ vibratory | boolean | Whether to vibrate when message received |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.33 Get user settings{#get__user_settings}

> GET /user/settings

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ auth_answer | string | Answer of verification question |
|⇥ auth_mode | int32 | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
|⇥ auth_question | string | Verification question |
|⇥ auto_download | boolean | Whether to download automatically |
|⇥ group_confirm | boolean | Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed |
|⇥ id | int64 |  |
|⇥ no_push | boolean | Whether to turn off push |
|⇥ no_push_detail | boolean | Whether to push details |
|⇥ no_push_end_hour | int32 | Start of push no-disturb time |
|⇥ no_push_start_hour | int32 | End of push no-disturb time |
|⇥ no_sounds | boolean | Whether to mute when message received |
|⇥ push_nick_name | string | Push nickname |
|⇥ push_token | string | Push token |
|⇥ silence_end_time | int32 | End of push no-reminder time |
|⇥ silence_start_time | int32 | Start of push no-reminder time |
|⇥ user_id | int64 | User ID |
|⇥ vibratory | boolean | Whether to vibrate when message received |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.34 Modify user settings{#put__user_settings}

> PUT /user/settings

> POST /user/settings

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| auth_answer | string | false |  | Answer of verification question |
| auth_mode | int32 | false |  | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
| auth_question | string | false |  | Verification question |
| auto_download | boolean | false |  | Whether to download automatically |
| group_confirm | boolean | false |  | Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed |
| id | int64 | false |  |  |
| no_push | boolean | false |  | Whether to turn off push |
| no_push_detail | boolean | false |  | Whether to push details |
| no_push_end_hour | int32 | false |  | Start of push no-disturb time |
| no_push_start_hour | int32 | false |  | End of push no-disturb time |
| no_sounds | boolean | false |  | Whether to mute when message received |
| push_nick_name | string | false |  | Push nickname |
| push_token | string | false |  | Push token |
| silence_end_time | int32 | false |  | End of push no-reminder time |
| silence_start_time | int32 | false |  | Start of push no-reminder time |
| user_id | int64 | true |  | User ID |
| vibratory | boolean | false |  | Whether to vibrate when message received |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.35 Set whether to mute sound alert for new message{#put__user_sounds}

> PUT /user/sounds

> POST /user/sounds

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| value | boolean | true | value |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.36 Bind token{#put__user_token_bind}

> PUT /user/token/bind

> POST /user/token/bind

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| device_sn | int32 | true |  | Device SN |
| device_token | string | true |  | device token |
| notifier_name | string | true |  | Certificate name |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.37 Unbind token{#delete__user_token_unbind}

> DELETE /user/token/unbind

> POST /user/token/unbind

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| deviceSn | int32 | true | deviceSn |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.38 Modify username{#put__user_username}

> PUT /user/username

> POST /user/username

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| username | string | true | username |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 1.39 Set whether to vibrate alert for new message{#put__user_vibratory}

> PUT /user/vibratory

> POST /user/vibratory

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| value | boolean | true | value |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

