# 5 消息处理{#message}

## 5.1 发送已读回执{#get\_\_message\_ack}

> GET /message/ack

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称             | 数据类型  | 必填    | 描述   |
| ---------------- | ----- | ----- | ---- |
| conversation\_id | int64 | false | 会话ID |
| device\_sn       | int32 | false | 设备序号 |
| msg\_id          | int64 | false | 消息ID |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 5.2 取指定会话的消息{#get\_\_message\_conversation}

> GET /message/conversation

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称           | 数据类型  | 必填   | 描述                      |
| -------------- | ----- | ---- | ----------------------- |
| limit          | int32 | true | 最多拉取多少条                 |
| msg\_id\_start | int64 | true | 从哪条消息开始向前拉取：传0表示最新的一条消息 |
| opposite\_id   | int64 | true | 会话ID                    |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称            | 类型             | 描述                                                                                                           |
| --------------- | -------------- | ------------------------------------------------------------------------------------------------------------ |
| code            | int32          | 返回码，200是成功                                                                                                   |
| data            | object         | 结果数据                                                                                                         |
| ⇥ is\_last      | boolean        | 是否是最后一条消息: true - 表示后面没有消息了， false - 后面还有消息                                                                  |
| ⇥ messages      | array\[object] | 消息列表                                                                                                         |
| ⇥⇥ attachment   | string         | 消息附件: 消息类型为图片/语音/视频/文件时，此字段会包括文件地址                                                                           |
| ⇥⇥ config       | string         | SDK层使用的扩展字段                                                                                                  |
| ⇥⇥ content      | string         | 消息内容                                                                                                         |
| ⇥⇥ ctype        | string         | 消息内容类型: TEXT - 文本, IMAGE - 图片, AUDIO - 语音, VIDEO - 视频, FILE - 文件, LOCATION - 位置, COMMAND - 自定义， FORWARD 转发消息 |
| ⇥⇥ ext          | string         | 扩展字段                                                                                                         |
| ⇥⇥ from\_xid    | object         | 消息发送者                                                                                                        |
| ⇥⇥⇥ device\_sn  | int32          | 设备序号                                                                                                         |
| ⇥⇥⇥ uid         | int64          | 用户ID                                                                                                         |
| ⇥⇥ msg\_id      | int64          | 消息ID                                                                                                         |
| ⇥⇥ status       | string         | 消息状态：UNREAD- 未读 ，DELIVERED - 已投递 ， READ - 已读                                                                 |
| ⇥⇥ timestamp    | int64          | 消息发送时间戳（毫秒）                                                                                                  |
| ⇥⇥ to\_xid      | object         | 消息接收者                                                                                                        |
| ⇥⇥⇥ device\_sn  | int32          | 设备序号                                                                                                         |
| ⇥⇥⇥ uid         | int64          | 用户ID                                                                                                         |
| ⇥ next\_msg\_id | int64          | 继续拉取需要设置的消息ID, 将此消息ID设置到请求参数的msg\_id\_start即可继续拉取消息                                                          |
| message         | string         | 错误信息，如果成功，该项为null                                                                                            |
| #### 接口描述       |                |                                                                                                              |

>

## 5.3 删除用户的指定会话{#delete\_\_message\_conversation}

> DELETE /message/conversation

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称             | 数据类型  | 必填   | 描述   |
| ---------------- | ----- | ---- | ---- |
| conversation\_id | int64 | true | 会话ID |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 5.4 发送系统通知{#put\_\_message\_notify}

> PUT /message/notify

> POST /message/notify

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称            | 数据类型          | 必填    | 默认值 | 描述                                                                                                                                                                                                     |
| --------------- | ------------- | ----- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| attachment      | string        | true  |     | 附件：如果消息类型为图片/语音/视频/文件时需要设置此字段。格式如:{"url":"https://xxx" ,"dName":"1658890327124.amr","fLen":1670,"duration":1}{"url":"https://xxx" ,"dName":"1646751218948","fLen":508728,"width":828.0,"height":828.0} |
| config          | string        | false |     | SDK使用的扩展字段                                                                                                                                                                                             |
| content         | string        | true  |     | 消息内容                                                                                                                                                                                                   |
| content\_type   | int32         | true  |     | <p>消息类型 TEXT = 0;<br>IMAGE = 1;<br>AUDIO = 2;<br>VIDEO = 3;<br>FILE = 4;<br>LOCATION = 5;<br>COMMAND = 6;<br>FORWARD = 7;<br>READ_ACK = 9;<br>RECALL = 10;<br>APPEND = 11;<br>REPLACE = 12;</p>        |
| ext             | string        | false |     | 扩展字段                                                                                                                                                                                                   |
| from\_user\_id  | int64         | false |     | 发送者的用户ID                                                                                                                                                                                               |
| online\_only    | boolean       | false |     | 是否只发给在线用户(默认为false)： true - 只发给在线用户； false - 发给在线和离线用户                                                                                                                                                 |
| related\_mid    | int64         | false |     | 消息操作相关的消息ID： 如何消息类型为READ\_ACK/RECALL时需要设置此字段，表示已读或撤回的消息ID                                                                                                                                              |
| targets         | array\[int64] | true  |     | 接收用户ID或群ID                                                                                                                                                                                             |
| transaction\_id | int64         | false |     | 请求ID，用于消息去重， 如果短时间内收到2个相同transaction\_id的请求，第二次请求不会被执行。 如果不设置就不会被去重                                                                                                                                    |
| type            | int32         | true  |     | 目标类型，1 - 普通用户，2 - 群组                                                                                                                                                                                   |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型            | 描述                            |
| --------- | ------------- | ----------------------------- |
| code      | int32         | 返回码，200是成功                    |
| data      | boolean       | 结果数据                          |
| message   | string        | 错误信息，如果成功，该项为null             |
| msg\_ids  | array\[int64] | 消息ID列表：当前只有消息接收者数量为1时才会返回消息ID |
| #### 接口描述 |               |                               |

>

## 5.5 撤回消息{#put\_\_message\_recall}

> PUT /message/recall

> POST /message/recall

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称             | 数据类型  | 必填   | 默认值 | 描述   |
| ---------------- | ----- | ---- | --- | ---- |
| conversation\_id | int64 | true |     | 会话ID |
| msg\_id          | int64 | true |     | 消息ID |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 5.6 发送消息{#put\_\_message\_send}

> PUT /message/send

> POST /message/send

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称            | 数据类型          | 必填    | 默认值 | 描述                                                                                                                                                                                                     |
| --------------- | ------------- | ----- | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| attachment      | string        | true  |     | 附件：如果消息类型为图片/语音/视频/文件时需要设置此字段。格式如:{"url":"https://xxx" ,"dName":"1658890327124.amr","fLen":1670,"duration":1}{"url":"https://xxx" ,"dName":"1646751218948","fLen":508728,"width":828.0,"height":828.0} |
| config          | string        | false |     | SDK使用的扩展字段                                                                                                                                                                                             |
| content         | string        | true  |     | 消息内容                                                                                                                                                                                                   |
| content\_type   | int32         | true  |     | <p>消息类型 TEXT = 0;<br>IMAGE = 1;<br>AUDIO = 2;<br>VIDEO = 3;<br>FILE = 4;<br>LOCATION = 5;<br>COMMAND = 6;<br>FORWARD = 7;<br>READ_ACK = 9;<br>RECALL = 10;<br>APPEND = 11;<br>REPLACE = 12;</p>        |
| ext             | string        | false |     | 扩展字段                                                                                                                                                                                                   |
| from\_user\_id  | int64         | false |     | 发送者的用户ID                                                                                                                                                                                               |
| online\_only    | boolean       | false |     | 是否只发给在线用户(默认为false)： true - 只发给在线用户； false - 发给在线和离线用户                                                                                                                                                 |
| related\_mid    | int64         | false |     | 消息操作相关的消息ID： 如何消息类型为READ\_ACK/RECALL时需要设置此字段，表示已读或撤回的消息ID                                                                                                                                              |
| targets         | array\[int64] | true  |     | 接收用户ID或群ID                                                                                                                                                                                             |
| transaction\_id | int64         | false |     | 请求ID，用于消息去重， 如果短时间内收到2个相同transaction\_id的请求，第二次请求不会被执行。 如果不设置就不会被去重                                                                                                                                    |
| type            | int32         | true  |     | 目标类型，1 - 普通用户，2 - 群组                                                                                                                                                                                   |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型            | 描述                            |
| --------- | ------------- | ----------------------------- |
| code      | int32         | 返回码，200是成功                    |
| data      | boolean       | 结果数据                          |
| message   | string        | 错误信息，如果成功，该项为null             |
| msg\_ids  | array\[int64] | 消息ID列表：当前只有消息接收者数量为1时才会返回消息ID |
| #### 接口描述 |               |                               |

>

## 5.7 取指定用户的最近会话列表{#get\_\_message\_unread}

> GET /message/unread

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称               | 类型             | 描述                |
| ------------------ | -------------- | ----------------- |
| code               | int32          | 返回码，200是成功        |
| data               | array\[object] | 结果数据              |
| ⇥ conversation\_id | object         | 会话信息              |
| ⇥⇥ uid             | int64          | 会话ID              |
| ⇥ num              | int32          | 未读消息数             |
| message            | string         | 错误信息，如果成功，该项为null |
| #### 接口描述          |                |                   |

>
