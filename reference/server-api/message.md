

## 6    消息处理

## 6.1  发送已读回执

> GET  /message/ack

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|conversation_id||conversation_id|
|device_sn||device_sn|
|msg_id||msg_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 6.2  取指定会话的消息

> GET  /message/conversation

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|limit||limit|
|msg_id_start||msg_id_start|
|opposite_id||opposite_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false||
|⇥ is_last|boolean||false||
|⇥ messages|array[object]||false||
|⇥⇥ attachment|string||false||
|⇥⇥ config|string||false||
|⇥⇥ content|string||false||
|⇥⇥ ctype|string||false||
|⇥⇥ ext|string||false||
|⇥⇥ from_xid|object||false||
|⇥⇥⇥ device_sn|int32||false||
|⇥⇥⇥ set_device_sn|boolean||false||
|⇥⇥⇥ set_uid|boolean||false||
|⇥⇥⇥ uid|int32||false||
|⇥⇥ msg_id|int32||false||
|⇥⇥ set_attachment|boolean||false||
|⇥⇥ set_config|boolean||false||
|⇥⇥ set_content|boolean||false||
|⇥⇥ set_ctype|boolean||false||
|⇥⇥ set_ext|boolean||false||
|⇥⇥ set_from_xid|boolean||false||
|⇥⇥ set_msg_id|boolean||false||
|⇥⇥ set_status|boolean||false||
|⇥⇥ set_timestamp|boolean||false||
|⇥⇥ set_to_xid|boolean||false||
|⇥⇥ status|string||false||
|⇥⇥ timestamp|int32||false||
|⇥⇥ to_xid|object||false||
|⇥⇥⇥ device_sn|int32||false||
|⇥⇥⇥ set_device_sn|boolean||false||
|⇥⇥⇥ set_uid|boolean||false||
|⇥⇥⇥ uid|int32||false||
|⇥ messages_iterator|object||false||
|⇥ messages_size|int32||false||
|⇥ next_msg_id|int32||false||
|⇥ set_is_last|boolean||false||
|⇥ set_messages|boolean||false||
|⇥ set_next_msg_id|boolean||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 6.3  删除用户的指定会话

> DELETE  /message/conversation

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|conversation_id||conversation_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 6.4  发送系统通知

> POST  /message/notify

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| attachment|string||false||
| config|string||false||
| content|string||false||
| content_type|int32||false|消息类型 TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7;|
| ext|string||false||
| from_user_id|int32||false|发送者的用户ID|
| targets|array[int32]||false|接收用户ID或群ID|
| transaction_id|int32||false|请求ID，用于消息去重， 如果短时间内收到2个相同transaction_id的请求，第二次请求不会被执行。 如果不设置就不会被去重|
| type|int32||false|目标类型，1 - 普通用户，2 - 群组|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 6.5  发送系统通知

> PUT  /message/notify

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| attachment|string||false||
| config|string||false||
| content|string||false||
| content_type|int32||false|消息类型 TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7;|
| ext|string||false||
| from_user_id|int32||false|发送者的用户ID|
| targets|array[int32]||false|接收用户ID或群ID|
| transaction_id|int32||false|请求ID，用于消息去重， 如果短时间内收到2个相同transaction_id的请求，第二次请求不会被执行。 如果不设置就不会被去重|
| type|int32||false|目标类型，1 - 普通用户，2 - 群组|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 6.6  发送消息

> POST  /message/send

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| attachment|string||false||
| config|string||false||
| content|string||false||
| content_type|int32||false|消息类型 TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7;|
| ext|string||false||
| from_user_id|int32||false|发送者的用户ID|
| targets|array[int32]||false|接收用户ID或群ID|
| transaction_id|int32||false|请求ID，用于消息去重， 如果短时间内收到2个相同transaction_id的请求，第二次请求不会被执行。 如果不设置就不会被去重|
| type|int32||false|目标类型，1 - 普通用户，2 - 群组|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 6.7  发送消息

> PUT  /message/send

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| attachment|string||false||
| config|string||false||
| content|string||false||
| content_type|int32||false|消息类型 TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7;|
| ext|string||false||
| from_user_id|int32||false|发送者的用户ID|
| targets|array[int32]||false|接收用户ID或群ID|
| transaction_id|int32||false|请求ID，用于消息去重， 如果短时间内收到2个相同transaction_id的请求，第二次请求不会被执行。 如果不设置就不会被去重|
| type|int32||false|目标类型，1 - 普通用户，2 - 群组|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 6.8  取指定用户的最近会话列表

> GET  /message/unread

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ conversation_id|object||false||
|⇥⇥ device_sn|int32||false||
|⇥⇥ set_device_sn|boolean||false||
|⇥⇥ set_uid|boolean||false||
|⇥⇥ uid|int32||false||
|⇥ num|int32||false||
|⇥ set_conversation_id|boolean||false||
|⇥ set_num|boolean||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 


