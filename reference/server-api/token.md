
## 5    token 接口

## 5.1  通过用户ID和密码取普通用户token

> POST  /token/id

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| device_guid|string||false|设备ID, 如果设置，则返回PushToken|
| password|string||false||
| user_id|int32||false|用户ID，仅用于用户ID登录|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|Token 信息|
|⇥ access_key_secret|string||false|文件密钥|
|⇥ encrypt_type|int32||false|是否启用加密连接|
|⇥ expire|int32||false|过期时间戳|
|⇥ public_key|string||false|公钥|
|⇥ push_token|string||false|推送Token|
|⇥ store_token|string||false|文件token|
|⇥ token|string||false|访问token|
|⇥ user_id|int32||false|用户ID|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 5.2  通过用户名/手机号/邮箱取普通用户token

> POST  /token/login

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| device_guid|string||false|设备ID, 如果设置，则返回PushToken|
| login_name|string||false|登录名，可以是手机号，邮箱，用户名|
| password|string||false||

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|Token 信息|
|⇥ access_key_secret|string||false|文件密钥|
|⇥ encrypt_type|int32||false|是否启用加密连接|
|⇥ expire|int32||false|过期时间戳|
|⇥ public_key|string||false|公钥|
|⇥ push_token|string||false|推送Token|
|⇥ store_token|string||false|文件token|
|⇥ token|string||false|访问token|
|⇥ user_id|int32||false|用户ID|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 5.3  通过用户名和密码取普通用户token

> POST  /token/user

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| device_guid|string||false|设备ID, 如果设置，则返回PushToken|
| name|string||false|用户名，仅用于用户名登录|
| password|string||false||

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|Token 信息|
|⇥ access_key_secret|string||false|文件密钥|
|⇥ encrypt_type|int32||false|是否启用加密连接|
|⇥ expire|int32||false|过期时间戳|
|⇥ public_key|string||false|公钥|
|⇥ push_token|string||false|推送Token|
|⇥ store_token|string||false|文件token|
|⇥ token|string||false|访问token|
|⇥ user_id|int32||false|用户ID|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 


