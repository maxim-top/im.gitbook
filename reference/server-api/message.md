

## 6    Message processing

## 6.1  Send read receipt

> GET  /message/ack

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| 
| app_id| | App ID| 
| group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| 
| user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| conversation_id| | conversation_id| 
| device_sn| | device_sn| 
| msg_id| | msg_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 6.2  Get the message for the specified conversation

> GET  /message/conversation

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| 
| app_id| | App ID| 
| group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| 
| user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| limit| | limit| 
| msg_id_start| | msg_id_start| 
| opposite_id| | opposite_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ is_last| boolean| | false| | 
| ⇥ messages| array[object]| | false| | 
| ⇥⇥ attachment| string| | false| | 
| ⇥⇥ config| string| | false| | 
| ⇥⇥ content| string| | false| | 
| ⇥⇥ ctype| string| | false| | 
| ⇥⇥ ext| string| | false| | 
| ⇥⇥ from_xid| object| | false| | 
| ⇥⇥⇥ device_sn| int32| | false| | 
| ⇥⇥⇥ set_device_sn| boolean| | false| | 
| ⇥⇥⇥ set_uid| boolean| | false| | 
| ⇥⇥⇥ uid| int32| | false| | 
| ⇥⇥ msg_id| int32| | false| | 
| ⇥⇥ set_attachment| boolean| | false| | 
| ⇥⇥ set_config| boolean| | false| | 
| ⇥⇥ set_content| boolean| | false| | 
| ⇥⇥ set_ctype| boolean| | false| | 
| ⇥⇥ set_ext| boolean| | false| | 
| ⇥⇥ set_from_xid| boolean| | false| | 
| ⇥⇥ set_msg_id| boolean| | false| | 
| ⇥⇥ set_status| boolean| | false| | 
| ⇥⇥ set_timestamp| boolean| | false| | 
| ⇥⇥ set_to_xid| boolean| | false| | 
| ⇥⇥ status| string| | false| | 
| ⇥⇥ timestamp| int32| | false| | 
| ⇥⇥ to_xid| object| | false| | 
| ⇥⇥⇥ device_sn| int32| | false| | 
| ⇥⇥⇥ set_device_sn| boolean| | false| | 
| ⇥⇥⇥ set_uid| boolean| | false| | 
| ⇥⇥⇥ uid| int32| | false| | 
| ⇥ messages_iterator| object| | false| | 
| ⇥ messages_size| int32| | false| | 
| ⇥ next_msg_id| int32| | false| | 
| ⇥ set_is_last| boolean| | false| | 
| ⇥ set_messages| boolean| | false| | 
| ⇥ set_next_msg_id| boolean| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 6.3  Delete the specified conversation for the user

> DELETE  /message/conversation

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| 
| app_id| | App ID| 
| group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| 
| user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| conversation_id| | conversation_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 6.4  Send system notification

> POST  /message/notify

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| 
| app_id| | App ID| 
| group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| 
| user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  attachment| string| | false| | 
|  config| string| | false| | 
|  content| string| | false| | 
|  content_type| int32| | false| Message type TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7;| 
|  ext| string| | false| | 
|  from_user_id| int32| | false| Sender's user ID| 
|  targets| array[int32]| | false| Receive user ID or group ID| 
|  transaction_id| int32| | false| Request ID, which is used for message deduplication. If two requests with the same transaction_id are received in a short time, the second request will not be executed. No deduplication when request ID is not set.| 
|  type| int32| | false| Target type, 1 - normal user, 2 -- group| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 6.5  Send system notification

> PUT  /message/notify

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| 
| app_id| | App ID| 
| group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| 
| user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  attachment| string| | false| | 
|  config| string| | false| | 
|  content| string| | false| | 
|  content_type| int32| | false| Message type TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7;| 
|  ext| string| | false| | 
|  from_user_id| int32| | false| Sender's user ID| 
|  targets| array[int32]| | false| Receive user ID or group ID| 
|  transaction_id| int32| | false| Request ID, which is used for message deduplication. If two requests with the same transaction_id are received in a short time, the second request will not be executed. No deduplication when request ID is not set.| 
|  type| int32| | false| Target type, 1 - normal user, 2 -- group| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 6.6  Send a message

> POST  /message/send

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| 
| app_id| | App ID| 
| group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| 
| user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  attachment| string| | false| | 
|  config| string| | false| | 
|  content| string| | false| | 
|  content_type| int32| | false| Message type TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7;| 
|  ext| string| | false| | 
|  from_user_id| int32| | false| Sender's user ID| 
|  targets| array[int32]| | false| Receive user ID or group ID| 
|  transaction_id| int32| | false| Request ID, which is used for message deduplication. If two requests with the same transaction_id are received in a short time, the second request will not be executed. No deduplication when request ID is not set.| 
|  type| int32| | false| Target type, 1 - normal user, 2 -- group| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 6.7  Send a message

> PUT  /message/send

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| 
| app_id| | App ID| 
| group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| 
| user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  attachment| string| | false| | 
|  config| string| | false| | 
|  content| string| | false| | 
|  content_type| int32| | false| Message type TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7;| 
|  ext| string| | false| | 
|  from_user_id| int32| | false| Sender's user ID| 
|  targets| array[int32]| | false| Receive user ID or group ID| 
|  transaction_id| int32| | false| Request ID, which is used for message deduplication. If two requests with the same transaction_id are received in a short time, the second request will not be executed. No deduplication when request ID is not set.| 
|  type| int32| | false| Target type, 1 - normal user, 2 -- group| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 6.8  Get the list of recent conversations for the specified user

> GET  /message/unread

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| 
| app_id| | App ID| 
| group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| 
| user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ conversation_id| object| | false| | 
| ⇥⇥ device_sn| int32| | false| | 
| ⇥⇥ set_device_sn| boolean| | false| | 
| ⇥⇥ set_uid| boolean| | false| | 
| ⇥⇥ uid| int32| | false| | 
| ⇥ num| int32| | false| | 
| ⇥ set_conversation_id| boolean| | false| | 
| ⇥ set_num| boolean| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 


