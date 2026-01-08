# 5 消息处理{#message}

## 5.1 发送已读回执{#get__message_ack}

> GET /message/ack

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| conversation_id | int64 | false | 会话ID |
| device_sn | int32 | false | 设备序号 |
| msg_id | int64 | false | 消息ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 5.2 广播消息{#post__message_broadcast}

> POST /message/broadcast

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| attachment | string | false |  |  |
| config | string | false |  |  |
| content | string | false |  |  |
| content_type | int32 | true |  | 消息类型 TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6; |
| ext | string | false |  |  |
| type | int32 | true |  | 目标类型，1 - 普通用户 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ send_num | int64 | 发送数量 |
|⇥ success | boolean | 是否成功 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 5.3 取指定会话的消息{#get__message_conversation}

> GET /message/conversation

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| limit | int32 | true | 最多拉取多少条 |
| msg_id_start | int64 | true | 从哪条消息开始向前拉取：传0表示最新的一条消息 |
| opposite_id | int64 | true | 会话ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ is_last | boolean | 是否是最后一条消息: true - 表示后面没有消息了， false - 后面还有消息 |
|⇥ messages | array[object] | 消息列表 |
|⇥⇥ attachment | string | 消息附件: 消息类型为图片/语音/视频/文件时，此字段会包括文件地址 |
|⇥⇥ config | string | SDK层使用的扩展字段 |
|⇥⇥ content | string | 消息内容 |
|⇥⇥ ctype | string | 消息内容类型: TEXT - 文本, IMAGE - 图片, AUDIO - 语音, VIDEO - 视频, FILE - 文件, LOCATION - 位置, COMMAND - 自定义， FORWARD 转发消息 |
|⇥⇥ ext | string | 扩展字段 |
|⇥⇥ from_xid | object | 消息发送者 |
|⇥⇥⇥ device_sn | int32 | 设备序号 |
|⇥⇥⇥ uid | int64 | 用户ID |
|⇥⇥ msg_id | int64 | 消息ID |
|⇥⇥ status | string | 消息状态：UNREAD- 未读 ，DELIVERED - 已投递 ， READ - 已读 |
|⇥⇥ timestamp | int64 | 消息发送时间戳（毫秒） |
|⇥⇥ to_xid | object | 消息接收者 |
|⇥⇥⇥ device_sn | int32 | 设备序号 |
|⇥⇥⇥ uid | int64 | 用户ID |
|⇥ next_msg_id | int64 | 继续拉取需要设置的消息ID, 将此消息ID设置到请求参数的msg_id_start即可继续拉取消息 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 5.4 删除用户的指定会话{#delete__message_conversation}

> DELETE /message/conversation

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| conversation_id | int64 | true | 会话ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 5.5 发送系统通知{#put__message_notify}

> PUT /message/notify

> POST /message/notify

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| attachment | string | false |  | 附件：如果消息类型为图片/语音/视频/文件时需要设置此字段。格式如:{"url":"https://xxx"  ,"dName":"1658890327124.amr","fLen":1670,"duration":1}{"url":"https://xxx"  ,"dName":"1646751218948","fLen":508728,"width":828.0,"height":828.0} |
| config | string | false |  | SDK使用的扩展字段 |
| content | string | true |  | 消息内容 |
| content_type | int32 | true |  | 消息类型 TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7;<br>    READ_ACK  = 9;<br>    RECALL    = 10;<br>    APPEND    = 11;<br>    REPLACE   = 12; |
| ext | string | false |  | 扩展字段 |
| from_user_id | int64 | false |  | 发送者的用户ID |
| online_only | boolean | false |  | 是否只发给在线用户(默认为false)： true - 只发给在线用户； false - 发给在线和离线用户 |
| related_mid | int64 | false |  | 消息操作相关的消息ID： 如何消息类型为READ_ACK/RECALL时需要设置此字段，表示已读或撤回的消息ID |
| targets | array[int64] | true |  | 接收用户ID或群ID |
| transaction_id | int64 | false |  | 请求ID，用于消息去重， 如果短时间内收到2个相同transaction_id的请求，第二次请求不会被执行。 如果不设置就不会被去重 |
| type | int32 | true |  | 目标类型，1 - 普通用户，2 - 群组 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
| msg_ids | array[int64] | 消息ID列表：当前只有消息接收者数量为1时才会返回消息ID |
#### 接口描述
> 

## 5.6 撤回消息{#put__message_recall}

> PUT /message/recall

> POST /message/recall

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| conversation_id | int64 | true |  | 会话ID |
| msg_id | int64 | true |  | 消息ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 5.7 发送消息{#put__message_send}

> PUT /message/send

> POST /message/send

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| attachment | string | false |  | 附件：如果消息类型为图片/语音/视频/文件时需要设置此字段。格式如:{"url":"https://xxx"  ,"dName":"1658890327124.amr","fLen":1670,"duration":1}{"url":"https://xxx"  ,"dName":"1646751218948","fLen":508728,"width":828.0,"height":828.0} |
| config | string | false |  | SDK使用的扩展字段 |
| content | string | true |  | 消息内容 |
| content_type | int32 | true |  | 消息类型 TEXT      = 0;<br>    IMAGE     = 1;<br>    AUDIO     = 2;<br>    VIDEO     = 3;<br>    FILE      = 4;<br>    LOCATION  = 5;<br>    COMMAND   = 6;<br>    FORWARD   = 7;<br>    READ_ACK  = 9;<br>    RECALL    = 10;<br>    APPEND    = 11;<br>    REPLACE   = 12; |
| ext | string | false |  | 扩展字段 |
| from_user_id | int64 | false |  | 发送者的用户ID |
| online_only | boolean | false |  | 是否只发给在线用户(默认为false)： true - 只发给在线用户； false - 发给在线和离线用户 |
| related_mid | int64 | false |  | 消息操作相关的消息ID： 如何消息类型为READ_ACK/RECALL时需要设置此字段，表示已读或撤回的消息ID |
| targets | array[int64] | true |  | 接收用户ID或群ID |
| transaction_id | int64 | false |  | 请求ID，用于消息去重， 如果短时间内收到2个相同transaction_id的请求，第二次请求不会被执行。 如果不设置就不会被去重 |
| type | int32 | true |  | 目标类型，1 - 普通用户，2 - 群组 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
| msg_ids | array[int64] | 消息ID列表：当前只有消息接收者数量为1时才会返回消息ID |
#### 接口描述
> 

## 5.8 取指定用户的最近会话列表{#get__message_unread}

> GET /message/unread

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ conversation_id | object | 会话信息 |
|⇥⇥ uid | int64 | 会话ID |
|⇥ num | int32 | 未读消息数 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

