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
| conversation_id | int64 | false | SessionID |
| device_sn | int32 | false | Device serial number |
| msg_id | int64 | false | MessageID |

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
| limit | int32 | true | How many to fetch |
| msg_id_start | int64 | true | From which message to start pulling forward: use 0 for the latest message |
| opposite_id | int64 | true | SessionID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ is_last | boolean | Whether it is the last message: true - there are no more messages to follow, false - there are more messages to follow |
|⇥ messages | array[object] | Message list |
|⇥⇥ attachment | string | Message attachment: When the message type is image/voice/video/file, this field will include the file url |
|⇥⇥ config | string | Extension fields used by the SDK layer |
|⇥⇥ content | string | Message content |
|⇥⇥ ctype | string | Message Content Type: TEXT - Text, IMAGE - Image, AUDIO - Voice, VIDEO - Video, FILE - File, LOCATION - Location, COMMAND - Custom, FORWARD - Forward Message |
|⇥⇥ ext | string | Extension field |
|⇥⇥ from_xid | object | Message sender |
|⇥⇥⇥ device_sn | int32 | Device serial number |
|⇥⇥⇥ uid | int64 | User ID |
|⇥⇥ msg_id | int64 | MessageID |
|⇥⇥ status | string | Message status: UNREAD - unread, DELIVERED - delivered, READ - read |
|⇥⇥ timestamp | int64 | Message delivery timestamp (milliseconds) |
|⇥⇥ to_xid | object | Message receiver |
|⇥⇥⇥ device_sn | int32 | Device serial number |
|⇥⇥⇥ uid | int64 | User ID |
|⇥ next_msg_id | int64 | the message ID that needs to be set to pull the messages: Set this message ID to msg_id_start of the request parameter to continue to pull the message |
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
| conversation_id | int64 | true | SessionID |

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
| attachment | string | true |  | Attachment: This field needs to be set if the message type is image/voice/video/file.:{"url":"https://xxx"  ,"dName":"1658890327124.amr","fLen":1670,"duration":1}{"url":"https://xxx"  ,"dName":"1646751218948","fLen":508728,"width":828.0,"height":828.0} |
| config | string | false |  | Extension fields used by the SDK |
| content | string | true |  | Message content |
| content_type | int32 | true |  | Message type TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7; |
| ext | string | false |  | Extension field |
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

## 5.5 Revoke message{#put__message_recall}

> PUT /message/recall

> POST /message/recall

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
| conversation_id | int64 | true |  | SessionID |
| msg_id | int64 | true |  | MessageID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 5.6 Send a message{#put__message_send}

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
| attachment | string | true |  | Attachment: This field needs to be set if the message type is image/voice/video/file.:{"url":"https://xxx"  ,"dName":"1658890327124.amr","fLen":1670,"duration":1}{"url":"https://xxx"  ,"dName":"1646751218948","fLen":508728,"width":828.0,"height":828.0} |
| config | string | false |  | Extension fields used by the SDK |
| content | string | true |  | Message content |
| content_type | int32 | true |  | Message type TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7; |
| ext | string | false |  | Extension field |
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

## 5.7 Get the list of recent sessions for the specified user{#get__message_unread}

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
|⇥ conversation_id | object | Conversation info |
|⇥⇥ uid | int64 | SessionID |
|⇥ num | int32 | Unread message-number |
| message | string | Error information, null means success |
#### Interface Description
> 

