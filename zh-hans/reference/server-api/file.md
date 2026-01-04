# 6 文件操作接口{#file}

## 6.1 下载头像{#get__file_download_avatar}

> GET /file/download/avatar

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
| h | double | false | 图片高 |
| image_type | int32 | false | 图片类型，1: 原图，2: 缩略图, 3: 封面图 |
| object_name | string | true | 对象名 |
| sdk_sign | string | false | SDK的签名 |
| store_token | string | false | 文件token |
| thumbnail_strategy | int32 | false | 缩略图生成策略, 1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1 |
| w | double | false | 图片宽 |

#### 响应体
● 200 响应数据格式：JSON

#### 接口描述
> 

## 6.2 下载聊天文件{#get__file_download_chat}

> GET /file/download/chat

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
| file_sign | string | true | 文件签名 |
| format | string | false | 需要下载的音频文件格式amr/mp3 默认为amr |
| h | double | false | 图片高 |
| image_type | int32 | false | 图片类型，1: 原图，2: 缩略图, 3: 封面图 |
| sdk_sign | string | false | SDK的签名 |
| source | string | false | 请求来源, miniprogram - 小程序，默认值是 '' |
| store_token | string | false | 文件token |
| thumbnail_strategy | int32 | false | 缩略图生成策略, 1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1 |
| w | double | false | 图片宽 |

#### 响应体
● 200 响应数据格式：JSON

#### 接口描述
> 

## 6.3 获取上传群头像URL{#get__file_upload_avatar_group}

> GET /file/upload/avatar/group

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | group_id |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ download_url | string | 下载地址 |
|⇥ oss_body_param | object | 上传时需要设置的OSS参数 |
|⇥ upload_method | string | 上传方式: POST/PUT |
|⇥ upload_url | string | 上传地址 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 6.4 获取上传用户头像URL{#get__file_upload_avatar_user}

> GET /file/upload/avatar/user

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
| data | object | 结果数据 |
|⇥ download_url | string | 下载地址 |
|⇥ oss_body_param | object | 上传时需要设置的OSS参数 |
|⇥ upload_method | string | 上传方式: POST/PUT |
|⇥ upload_url | string | 上传地址 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 6.5 获取上传聊天文件的URL{#get__file_upload_chat}

> GET /file/upload/chat

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
| file_type | int32 | true | 文件类型 100: 普通聊天文件, 101: 语音聊天文件(amr格式),102: 图片聊天文件, 103: 视频聊天文件, 104: 语音聊天文件(mp3格式)200: 普通共享文件, 201: 语音共享文件, 202: 图片共享文件, 203: 视频共享文件 |
| to_id | int64 | true | to_id |
| to_type | int32 | false | 1: 用户，2: 群组 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ download_url | string | 下载地址 |
|⇥ oss_body_param | object | 上传时需要设置的OSS参数 |
|⇥ upload_method | string | 上传方式: POST/PUT |
|⇥ upload_url | string | 上传地址 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 6.6 获取聊天文件转发的URL{#get__file_upload_forward}

> GET /file/upload/forward

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
| file_sign | string | true | 文件签名 |
| to_id | int64 | true | to_id |
| to_type | int32 | false | 1: 用户，2: 群组 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | string | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

