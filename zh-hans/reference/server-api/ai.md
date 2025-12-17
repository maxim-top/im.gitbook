# 8 AI 接口{#ai}

## 8.1 发送消息并获取AI回复{#put\_\_ai\_message\_send}

> PUT /ai/message/send

> POST /ai/message/send

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

| 参数名称           | 类型             | 描述                                                                                                           |
| -------------- | -------------- | ------------------------------------------------------------------------------------------------------------ |
| code           | int32          | 返回码，200是成功                                                                                                   |
| data           | object         | 结果数据                                                                                                         |
| ⇥ messages     | array\[object] | 消息列表                                                                                                         |
| ⇥⇥ attachment  | string         | 消息附件: 消息类型为图片/语音/视频/文件时，此字段会包括文件地址                                                                           |
| ⇥⇥ config      | string         | SDK层使用的扩展字段                                                                                                  |
| ⇥⇥ content     | string         | 消息内容                                                                                                         |
| ⇥⇥ ctype       | string         | 消息内容类型: TEXT - 文本, IMAGE - 图片, AUDIO - 语音, VIDEO - 视频, FILE - 文件, LOCATION - 位置, COMMAND - 自定义， FORWARD 转发消息 |
| ⇥⇥ ext         | string         | 扩展字段                                                                                                         |
| ⇥⇥ from\_xid   | object         | 消息发送者                                                                                                        |
| ⇥⇥⇥ device\_sn | int32          | 设备序号                                                                                                         |
| ⇥⇥⇥ uid        | int64          | 用户ID                                                                                                         |
| ⇥⇥ msg\_id     | int64          | 消息ID                                                                                                         |
| ⇥⇥ timestamp   | int64          | 消息发送时间戳（毫秒）                                                                                                  |
| ⇥⇥ to\_xid     | object         | 消息接收者                                                                                                        |
| ⇥⇥⇥ device\_sn | int32          | 设备序号                                                                                                         |
| ⇥⇥⇥ uid        | int64          | 用户ID                                                                                                         |
| ⇥⇥ type        | string         | 消息类型：CHAT- 单聊 ，GROUPCHAT - 群聊                                                                                |
| message        | string         | 错误信息，如果成功，该项为null                                                                                            |
| #### 接口描述      |                |                                                                                                              |

>
