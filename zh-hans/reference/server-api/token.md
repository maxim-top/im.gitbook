# 2 token 接口{#token}

## 2.1 通过用户ID和密码取普通用户token{#post\_\_token\_id}

> POST /token/id

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称         | 数据类型   | 必填    | 默认值 | 描述                      |
| ------------ | ------ | ----- | --- | ----------------------- |
| device\_guid | string | false |     | 设备ID, 如果设置，则返回PushToken |
| password     | string | true  |     | 密码                      |
| user\_id     | int64  | true  |     | 用户ID，仅用于用户ID登录          |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称                  | 类型     | 描述                            |
| --------------------- | ------ | ----------------------------- |
| code                  | int32  | 返回码，200是成功                    |
| data                  | object | 结果数据                          |
| ⇥ access\_key\_secret | string | 文件密钥                          |
| ⇥ encrypt\_type       | int32  | 是否启用加密连接                      |
| ⇥ expire              | int64  | 过期时间戳                         |
| ⇥ public\_key         | string | 公钥                            |
| ⇥ push\_token         | string | 推送Token                       |
| ⇥ store\_token        | string | 文件token                       |
| ⇥ token               | string | 访问token, 即调用API时的access-token |
| ⇥ user\_id            | int64  | 用户ID                          |
| message               | string | 错误信息，如果成功，该项为null             |
| #### 接口描述             |        |                               |

>

## 2.2 通过用户名/手机号/邮箱取普通用户token{#post\_\_token\_login}

> POST /token/login

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称         | 数据类型   | 必填    | 默认值 | 描述                      |
| ------------ | ------ | ----- | --- | ----------------------- |
| device\_guid | string | false |     | 设备ID, 如果设置，则返回PushToken |
| login\_name  | string | true  |     | 登录名，可以是手机号，邮箱，用户名       |
| password     | string | true  |     | 密码                      |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称                  | 类型     | 描述                            |
| --------------------- | ------ | ----------------------------- |
| code                  | int32  | 返回码，200是成功                    |
| data                  | object | 结果数据                          |
| ⇥ access\_key\_secret | string | 文件密钥                          |
| ⇥ encrypt\_type       | int32  | 是否启用加密连接                      |
| ⇥ expire              | int64  | 过期时间戳                         |
| ⇥ public\_key         | string | 公钥                            |
| ⇥ push\_token         | string | 推送Token                       |
| ⇥ store\_token        | string | 文件token                       |
| ⇥ token               | string | 访问token, 即调用API时的access-token |
| ⇥ user\_id            | int64  | 用户ID                          |
| message               | string | 错误信息，如果成功，该项为null             |
| #### 接口描述             |        |                               |

>

## 2.3 通过用户名和密码取普通用户token{#post\_\_token\_user}

> POST /token/user

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称         | 数据类型   | 必填    | 默认值 | 描述                      |
| ------------ | ------ | ----- | --- | ----------------------- |
| device\_guid | string | false |     | 设备ID, 如果设置，则返回PushToken |
| name         | string | true  |     | 用户名，仅用于用户名登录            |
| password     | string | true  |     | 密码                      |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称                  | 类型     | 描述                            |
| --------------------- | ------ | ----------------------------- |
| code                  | int32  | 返回码，200是成功                    |
| data                  | object | 结果数据                          |
| ⇥ access\_key\_secret | string | 文件密钥                          |
| ⇥ encrypt\_type       | int32  | 是否启用加密连接                      |
| ⇥ expire              | int64  | 过期时间戳                         |
| ⇥ public\_key         | string | 公钥                            |
| ⇥ push\_token         | string | 推送Token                       |
| ⇥ store\_token        | string | 文件token                       |
| ⇥ token               | string | 访问token, 即调用API时的access-token |
| ⇥ user\_id            | int64  | 用户ID                          |
| message               | string | 错误信息，如果成功，该项为null             |
| #### 接口描述             |        |                               |

>
