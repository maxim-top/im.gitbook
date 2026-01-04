# 3 Friend management interface{#roster}

## 3.1 Agree to add friend{#put__roster_accept}

> PUT /roster/accept

> POST /roster/accept

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| user_id | int64 | true | Consent user ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.2 Apply to add friend{#post__roster_apply}

> POST /roster/apply

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
| alias | string | false |  | Name in comment |
| auth_answer | string | false |  | Answer of question |
| reason | string | false |  | Request description |
| user_id | int64 | true |  | Invitee ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.3 Add friends in batch{#post__roster_apply_batch}

> POST /roster/apply/batch

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
|  | array[object] | true | |rosterApplications|
|⇥ alias | string | false |  | Name in comment |
|⇥ reason | string | false |  | Request description |
|⇥ user_id | int64 | true |  | Invitee ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ fails | array[object] | list of failure messages |
|⇥⇥ reason | string | Cause of failure |
|⇥⇥ user_id | int64 | User ID |
|⇥ success | array[int64] | List of successful user IDs |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.4 List of friend requests{#get__roster_apply_list}

> GET /roster/apply/list

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
| cursor | string | false | Cursor: Where to start fetching |
| limit | int32 | false | How many to fetch |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| cursor | string | Cursor, no cursor in returned result means the last page has been returned |
| data | array[object] | Result data |
|⇥ expired_time | int64 | Expiration timestamp(milliseconds) |
|⇥ reason | string | Request description |
|⇥ status | int32 | Status: 0 - waiting for confirmation, 1 - accepted, 2 - rejected |
|⇥ user_id | int64 | User ID that initiate adding friend |
| message | string | Error information, null means success |
| version | int64 | Version |
#### Interface Description
> 

## 3.5 Add to blacklist{#put__roster_block}

> PUT /roster/block

> POST /roster/block

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| user_id | int64 | true | User ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.6 List of blacklists{#get__roster_blocked_list}

> GET /roster/blocked_list

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
| data | array[int64] | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.7 Reject friend request{#put__roster_decline}

> PUT /roster/decline

> POST /roster/decline

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
| reason | string | false |  | Reason for rejection |
| user_id | int64 | true |  | Rejected user ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.8 Delete friend{#delete__roster_delete}

> DELETE /roster/delete

> POST /roster/delete

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| user_id | int64 | true | User ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.9 Update friend extension information{#put__roster_ext}

> PUT /roster/ext

> POST /roster/ext

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
| alias | string | false |  | Name in comment |
| ext | string | false |  | Extension information |
| mute_notification | boolean | false |  | Mute message notification: true - mute message notification, false - do not mute message notification |
| user_id | int64 | true |  | Friend user ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.10 Search for users by ID{#get__roster_id}

> GET /roster/id

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| user_id | int64 | true | User ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ alias | string | Name in comment |
|⇥ auth_mode | int32 | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
|⇥ auth_question | string | Verification question |
|⇥ avatar | string | Avatar |
|⇥ description | string | Description |
|⇥ ext | string | Extension information |
|⇥ mute_notification | boolean | Mute message notification: true - mute message notification, false - do not mute message notification |
|⇥ nick_name | string | Nickname or name |
|⇥ public_info | string | Public information, visible to both friends and strangers |
|⇥ relation | int32 | Relationships: 0 - friend, 1 - deleted friend, 2 - stranger, 3 - blacklist |
|⇥ user_id | int64 | Friend user ID |
|⇥ username | string | Username |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.11 List of friends{#get__roster_list}

> GET /roster/list

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
| cursor | string | false | Cursor:where to start fetching |
| limit | int32 | false | How many to fetch |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| cursor | string | Cursor, no cursor in returned result means the last page has been returned |
| data | array[int64] | Result data |
| message | string | Error information, null means success |
| version | int64 | Version |
#### Interface Description
> 

## 3.12 List of friend details{#post__roster_list}

> POST /roster/list

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
| list | array[int64] | true |  | Friends ID list |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ alias | string | Name in comment |
|⇥ auth_mode | int32 | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
|⇥ auth_question | string | Verification question |
|⇥ avatar | string | Avatar |
|⇥ description | string | Description |
|⇥ ext | string | Extension information |
|⇥ mute_notification | boolean | Mute message notification: true - mute message notification, false - do not mute message notification |
|⇥ nick_name | string | Nickname or name |
|⇥ public_info | string | Public information, visible to both friends and strangers |
|⇥ relation | int32 | Relationships: 0 - friend, 1 - deleted friend, 2 - stranger, 3 - blacklist |
|⇥ user_id | int64 | Friend user ID |
|⇥ username | string | Username |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.13 Whether to allow messaging{#get__roster_may_message}

> GET /roster/may_message

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| roster_id | int64 | true | Friend ID |
| user_id | int64 | true | User ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.14 Search for user by mobile number{#get__roster_mobile}

> GET /roster/mobile

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
| mobile | string | true | Mobile number |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ alias | string | Name in comment |
|⇥ auth_mode | int32 | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
|⇥ auth_question | string | Verification question |
|⇥ avatar | string | Avatar |
|⇥ description | string | Description |
|⇥ ext | string | Extension information |
|⇥ mute_notification | boolean | Mute message notification: true - mute message notification, false - do not mute message notification |
|⇥ nick_name | string | Nickname or name |
|⇥ public_info | string | Public information, visible to both friends and strangers |
|⇥ relation | int32 | Relationships: 0 - friend, 1 - deleted friend, 2 - stranger, 3 - blacklist |
|⇥ user_id | int64 | Friend user ID |
|⇥ username | string | Username |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.15 Search for user by user ID{#get__roster_name}

> GET /roster/name

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
| username | string | true | Username |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ alias | string | Name in comment |
|⇥ auth_mode | int32 | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
|⇥ auth_question | string | Verification question |
|⇥ avatar | string | Avatar |
|⇥ description | string | Description |
|⇥ ext | string | Extension information |
|⇥ mute_notification | boolean | Mute message notification: true - mute message notification, false - do not mute message notification |
|⇥ nick_name | string | Nickname or name |
|⇥ public_info | string | Public information, visible to both friends and strangers |
|⇥ relation | int32 | Relationships: 0 - friend, 1 - deleted friend, 2 - stranger, 3 - blacklist |
|⇥ user_id | int64 | Friend user ID |
|⇥ username | string | Username |
| message | string | Error information, null means success |
#### Interface Description
> 

## 3.16 Remove from blacklist{#delete__roster_unblock}

> DELETE /roster/unblock

> POST /roster/unblock

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| user_id | int64 | true | User ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

