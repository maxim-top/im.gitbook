# 6 文件操作接口{#file}

## 6.1 下载头像{#get\_\_file\_download\_avatar}

> GET /file/download/avatar

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称                | 数据类型   | 必填    | 描述                                        |
| ------------------- | ------ | ----- | ----------------------------------------- |
| h                   | double | false | 图片高                                       |
| image\_type         | int32  | false | 图片类型，1: 原图，2: 缩略图, 3: 封面图                 |
| object\_name        | string | true  | 对象名                                       |
| sdk\_sign           | string | false | SDK的签名                                    |
| store\_token        | string | false | 文件token                                   |
| thumbnail\_strategy | int32  | false | 缩略图生成策略, 1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1 |
| w                   | double | false | 图片宽                                       |

#### 响应体

● 200 响应数据格式：JSON

#### 接口描述

>

## 6.2 下载聊天文件{#get\_\_file\_download\_chat}

> GET /file/download/chat

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称                | 数据类型   | 必填    | 描述                                        |
| ------------------- | ------ | ----- | ----------------------------------------- |
| file\_sign          | string | true  | 文件签名                                      |
| format              | string | false | 需要下载的音频文件格式amr/mp3 默认为amr                 |
| h                   | double | false | 图片高                                       |
| image\_type         | int32  | false | 图片类型，1: 原图，2: 缩略图, 3: 封面图                 |
| sdk\_sign           | string | false | SDK的签名                                    |
| source              | string | false | 请求来源, miniprogram - 小程序，默认值是 ''           |
| store\_token        | string | false | 文件token                                   |
| thumbnail\_strategy | int32  | false | 缩略图生成策略, 1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1 |
| w                   | double | false | 图片宽                                       |

#### 响应体

● 200 响应数据格式：JSON

#### 接口描述

>

## 6.3 获取上传群头像URL{#get\_\_file\_upload\_avatar\_group}

> GET /file/upload/avatar/group

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                 |
| ------------ | ------ | ----- | -------------------------------------------------- |
| access-token | string | false | 令牌                                                 |
| app\_id      | string | true  | 应用ID                                               |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)

| 参数名称      | 数据类型  | 必填   | 描述        |
| --------- | ----- | ---- | --------- |
| group\_id | int64 | true | group\_id |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称               | 类型     | 描述                |
| ------------------ | ------ | ----------------- |
| code               | int32  | 返回码，200是成功        |
| data               | object | 结果数据              |
| ⇥ download\_url    | string | 下载地址              |
| ⇥ oss\_body\_param | object | 上传时需要设置的OSS参数     |
| ⇥ upload\_method   | string | 上传方式: POST/PUT    |
| ⇥ upload\_url      | string | 上传地址              |
| message            | string | 错误信息，如果成功，该项为null |
| #### 接口描述          |        |                   |

>

## 6.4 获取上传用户头像URL{#get\_\_file\_upload\_avatar\_user}

> GET /file/upload/avatar/user

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称               | 类型     | 描述                |
| ------------------ | ------ | ----------------- |
| code               | int32  | 返回码，200是成功        |
| data               | object | 结果数据              |
| ⇥ download\_url    | string | 下载地址              |
| ⇥ oss\_body\_param | object | 上传时需要设置的OSS参数     |
| ⇥ upload\_method   | string | 上传方式: POST/PUT    |
| ⇥ upload\_url      | string | 上传地址              |
| message            | string | 错误信息，如果成功，该项为null |
| #### 接口描述          |        |                   |

>

## 6.5 获取上传聊天文件的URL{#get\_\_file\_upload\_chat}

> GET /file/upload/chat

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称       | 数据类型  | 必填    | 描述                                                                                                                                  |
| ---------- | ----- | ----- | ----------------------------------------------------------------------------------------------------------------------------------- |
| file\_type | int32 | true  | 文件类型 100: 普通聊天文件, 101: 语音聊天文件(amr格式),102: 图片聊天文件, 103: 视频聊天文件, 104: 语音聊天文件(mp3格式)200: 普通共享文件, 201: 语音共享文件, 202: 图片共享文件, 203: 视频共享文件 |
| to\_id     | int64 | true  | to\_id                                                                                                                              |
| to\_type   | int32 | false | 1: 用户，2: 群组                                                                                                                         |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称               | 类型     | 描述                |
| ------------------ | ------ | ----------------- |
| code               | int32  | 返回码，200是成功        |
| data               | object | 结果数据              |
| ⇥ download\_url    | string | 下载地址              |
| ⇥ oss\_body\_param | object | 上传时需要设置的OSS参数     |
| ⇥ upload\_method   | string | 上传方式: POST/PUT    |
| ⇥ upload\_url      | string | 上传地址              |
| message            | string | 错误信息，如果成功，该项为null |
| #### 接口描述          |        |                   |

>

## 6.6 获取聊天文件转发的URL{#get\_\_file\_upload\_forward}

> GET /file/upload/forward

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称       | 数据类型   | 必填    | 描述          |
| ---------- | ------ | ----- | ----------- |
| file\_sign | string | true  | 文件签名        |
| to\_id     | int64  | true  | to\_id      |
| to\_type   | int32  | false | 1: 用户，2: 群组 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型     | 描述                |
| --------- | ------ | ----------------- |
| code      | int32  | 返回码，200是成功        |
| data      | string | 结果数据              |
| message   | string | 错误信息，如果成功，该项为null |
| #### 接口描述 |        |                   |

>
