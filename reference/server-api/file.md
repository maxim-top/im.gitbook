## 9    文件操作接口

## 9.1  下载头像

> GET  /file/download/avatar

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|image_type||图片类型，1: 原图，2: 缩略图, 3: 封面图|
|object_name||对象名|
|sdk_sign||SDK的签名|
|store_token||文件token|
|thumbnail_strategy||缩略图生成策略, 1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1|

### 响应体
● 200 响应数据格式：JSON


### 接口描述
> 




## 9.2  下载聊天文件

> GET  /file/download/chat

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|file_sign||文件签名|
|format||需要下载的音频文件格式amr/mp3 默认为amr|
|image_type||图片类型，1: 原图，2: 缩略图, 3: 封面图|
|sdk_sign||SDK的签名|
|source||请求来源, miniprogram - 小程序，默认值是 ''|
|store_token||文件token|
|thumbnail_strategy||缩略图生成策略, 1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1|

### 响应体
● 200 响应数据格式：JSON


### 接口描述
> 




## 9.3  获取上传群头像URL

> GET  /file/upload/avatar/group

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|group_id||group_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false||
|⇥ download_url|string||false||
|⇥ oss_body_param|object||false||
|⇥ upload_url|string||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 9.4  获取上传用户头像URL

> GET  /file/upload/avatar/user

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false||
|⇥ download_url|string||false||
|⇥ oss_body_param|object||false||
|⇥ upload_url|string||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 9.5  获取上传聊天文件的URL

> GET  /file/upload/chat

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|file_type||文件类型 100: 普通聊天文件, 101: 语音聊天文件(amr格式),102: 图片聊天文件, 103: 视频聊天文件, 104: 语音聊天文件(mp3格式)200: 普通共享文件, 201: 语音共享文件, 202: 图片共享文件, 203: 视频共享文件|
|to_id||to_id|
|to_type||1: 用户，2: 群组|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false||
|⇥ download_url|string||false||
|⇥ oss_body_param|object||false||
|⇥ upload_url|string||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 9.6  获取聊天文件转发的URL

> GET  /file/upload/forward

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|file_sign||文件签名|
|to_id||to_id|
|to_type||1: 用户，2: 群组|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|string||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 
