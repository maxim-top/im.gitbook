# 5 Message processing{#message}

## 5.1 Send read receipt{#get__message_ack}

> GET /message/ack

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
| conversation_id | int64 | true | conversation_id |
| device_sn | int32 | true | device_sn |
| msg_id | int64 | true | msg_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 5.2 Get the message for the specified session{#get__message_conversation}

> GET /message/conversation

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
| limit | int32 | true | limit |
| msg_id_start | int64 | true | msg_id_start |
| opposite_id | int64 | true | opposite_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ is_last | boolean |  |
|⇥ messages | array[object] |  |
|⇥⇥ attachment | string |  |
|⇥⇥ config | string |  |
|⇥⇥ content | string |  |
|⇥⇥ ctype | string |  |
|⇥⇥ ext | string |  |
|⇥⇥ from_xid | object |  |
|⇥⇥⇥ device_sn | int32 |  |
|⇥⇥⇥ set_device_sn | boolean |  |
|⇥⇥⇥ set_uid | boolean |  |
|⇥⇥⇥ uid | int64 |  |
|⇥⇥ msg_id | int64 |  |
|⇥⇥ set_attachment | boolean |  |
|⇥⇥ set_config | boolean |  |
|⇥⇥ set_content | boolean |  |
|⇥⇥ set_ctype | boolean |  |
|⇥⇥ set_ext | boolean |  |
|⇥⇥ set_from_xid | boolean |  |
|⇥⇥ set_msg_id | boolean |  |
|⇥⇥ set_status | boolean |  |
|⇥⇥ set_timestamp | boolean |  |
|⇥⇥ set_to_xid | boolean |  |
|⇥⇥ status | string |  |
|⇥⇥ timestamp | int64 |  |
|⇥⇥ to_xid | object |  |
|⇥⇥⇥ device_sn | int32 |  |
|⇥⇥⇥ set_device_sn | boolean |  |
|⇥⇥⇥ set_uid | boolean |  |
|⇥⇥⇥ uid | int64 |  |
|⇥ messages_iterator | object |  |
|⇥ messages_size | int32 |  |
|⇥ next_msg_id | int64 |  |
|⇥ set_is_last | boolean |  |
|⇥ set_messages | boolean |  |
|⇥ set_next_msg_id | boolean |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 5.3 Delete the specified session for the user{#delete__message_conversation}

> DELETE /message/conversation

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
| conversation_id | int64 | true | conversation_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 5.4 Send system notification{#put__message_notify}

> PUT /message/notify

> POST /message/notify

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
| attachment | string | false |  |  |
| config | string | false |  |  |
| content | string | false |  |  |
| content_type | int32 | true |  | Message type TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7; |
| ext | string | false |  |  |
| from_user_id | int64 | false |  | Sender's user ID |
| targets | array[int64] | true |  | Receive user ID or group ID |
| transaction_id | int64 | false |  | Request ID, which is used for message deduplication. If two requests with the same transaction_id are received in a short time, the second request will not be executed. No deduplication when request ID is not set. |
| type | int32 | true |  | Target type, 1 - normal user, 2 -- group |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 5.5 Send a message{#put__message_send}

> PUT /message/send

> POST /message/send

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
| attachment | string | false |  |  |
| config | string | false |  |  |
| content | string | false |  |  |
| content_type | int32 | true |  | Message type TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7; |
| ext | string | false |  |  |
| from_user_id | int64 | false |  | Sender's user ID |
| targets | array[int64] | true |  | Receive user ID or group ID |
| transaction_id | int64 | false |  | Request ID, which is used for message deduplication. If two requests with the same transaction_id are received in a short time, the second request will not be executed. No deduplication when request ID is not set. |
| type | int32 | true |  | Target type, 1 - normal user, 2 -- group |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 5.6 Get the list of recent sessions for the specified user{#get__message_unread}

> GET /message/unread

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
| data | array[object] | Result data |
|⇥ conversation_id | object |  |
|⇥⇥ device_sn | int32 |  |
|⇥⇥ set_device_sn | boolean |  |
|⇥⇥ set_uid | boolean |  |
|⇥⇥ uid | int64 |  |
|⇥ num | int32 |  |
|⇥ set_conversation_id | boolean |  |
|⇥ set_num | boolean |  |
| message | string | Error information, null means success |
#### Interface Description
> 

