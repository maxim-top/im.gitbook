
## 3    用户操作

## 3.1  设置加好友验证方式

> POST  /user/authmode

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.2  设置加好友验证方式

> PUT  /user/authmode

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.3  设置头像

> POST  /user/avatar

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| avatar|string||false|头像 url|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.4  设置头像

> PUT  /user/avatar

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| avatar|string||false|头像 url|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.5  批量设置头像

> POST  /user/avatar/batch

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| list|array[object]||false||
|⇥ avatar|string||false|头像 url|
|⇥ user_id|int32||false|用户ID|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false|失败原因|
|⇥ success|boolean||false|是否成功|
|⇥ user_id|int32||false|用户ID|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.6  批量设置头像

> PUT  /user/avatar/batch

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| list|array[object]||false||
|⇥ avatar|string||false|头像 url|
|⇥ user_id|int32||false|用户ID|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false|失败原因|
|⇥ success|boolean||false|是否成功|
|⇥ user_id|int32||false|用户ID|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.7  将openid绑定到账号.(绑定建议使用/app/wechat/bind;解绑建议使用/app/wechat/unbind)

> GET  /user/bind_openid

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|open_id||open_id|
|type||type|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.8  修改密码

> POST  /user/change_password

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| new_password|string||false|new_password 新密码|
| old_password|string||false|old_password 旧密码|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.9  设备列表

> GET  /user/device/list

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| cursor|string||false|游标，返回结果中缺失 cursor，表示已经返回最后一页|
| data|array[object]||false|结果数据|
|⇥ device_sn|int32||false||
|⇥ platform|int32||false|设备平台, 1:ios, 2:android, 3:windows, 4:mac, 5:linux, 6:web|
|⇥ user_agent|string||false||
|⇥ user_id|int32||false|用户 ID|
| message|string||false|错误信息，如果成功，该项为null|
| version|int32||false|版本|


### 接口描述
> 




## 3.10 删除device

> POST  /user/device/remove

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|device_sn||device_sn|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.11 删除device

> DELETE  /user/device/remove

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|device_sn||device_sn|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.12 封禁用户

> PUT  /user/disable

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| list|array[int32]||false||

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.13 设置是否自动下载缩略图和文件

> POST  /user/download

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.14 设置是否自动下载缩略图和文件

> PUT  /user/download

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.15 解禁用户

> PUT  /user/enable

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| list|array[int32]||false||

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.16 踢指定设备下线

> POST  /user/kick

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|device_sn||不传device_sn表示踢所有设备|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.17 踢指定设备下线

> PUT  /user/kick

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|device_sn||不传device_sn表示踢所有设备|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.18 设置手机号码

> POST  /user/mobile

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|mobile||mobile|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.19 设置手机号码

> PUT  /user/mobile

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|mobile||mobile|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.20 设置昵称

> POST  /user/nickname

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|nick_name||nick_name|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.21 设置昵称

> PUT  /user/nickname

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|nick_name||nick_name|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.22 查询用户在线状态

> GET  /user/online_status

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|用户在线信息|
|⇥ online|boolean||false|是否在线： true - 在线 ，false - 离线|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.23 设置私有扩展信息

> POST  /user/private

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.24 设置私有扩展信息

> PUT  /user/private

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.25 获取用户信息

> GET  /user/profile

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|用户信息|
|⇥ avatar|string||false|头像 url|
|⇥ description|string||false|描述信息|
|⇥ email|string||false|邮箱|
|⇥ mobile|string||false|手机号码|
|⇥ nick_name|string||false|昵称|
|⇥ private_info|string||false|私有信息，仅自己可见|
|⇥ public_info|string||false|公开信息，好友和陌生人可见|
|⇥ user_id|int32||false|用户ID|
|⇥ username|string||false|用户名|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.26 更新用户信息

> POST  /user/profile

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| description|string||false|描述信息|
| nick_name|string||false|昵称|
| private_info|string||false|私有信息，仅自己可见|
| public_info|string||false|公开信息，好友和陌生人可见|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.27 更新用户信息

> PUT  /user/profile

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| description|string||false|描述信息|
| nick_name|string||false|昵称|
| private_info|string||false|私有信息，仅自己可见|
| public_info|string||false|公开信息，好友和陌生人可见|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.28 批量更新用户信息

> POST  /user/profile/batch

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| list|array[object]||false||
|⇥ description|string||false|描述信息|
|⇥ nick_name|string||false|昵称|
|⇥ private_info|string||false|私有信息，仅自己可见|
|⇥ public_info|string||false|公开信息，好友和陌生人可见|
|⇥ user_id|int32||false|用户ID|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false|失败原因|
|⇥ success|boolean||false|是否成功|
|⇥ user_id|int32||false|用户ID|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.29 批量更新用户信息

> PUT  /user/profile/batch

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| list|array[object]||false||
|⇥ description|string||false|描述信息|
|⇥ nick_name|string||false|昵称|
|⇥ private_info|string||false|私有信息，仅自己可见|
|⇥ public_info|string||false|公开信息，好友和陌生人可见|
|⇥ user_id|int32||false|用户ID|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false|失败原因|
|⇥ success|boolean||false|是否成功|
|⇥ user_id|int32||false|用户ID|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.30 设置公开扩展信息

> POST  /user/public

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.31 设置公开扩展信息

> PUT  /user/public

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.32 设置是否关闭推送

> POST  /user/push

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.33 设置是否关闭推送

> PUT  /user/push

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.34 绑定别名

> POST  /user/push/alias

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| alias|string||false|别名|
| push_token|string||false|推送token|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.35 设置badge

> POST  /user/push/badge

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| badge|int32||false|badge|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.36 设置是否关闭推送详情

> POST  /user/push/detail

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.37 设置是否关闭推送详情

> PUT  /user/push/detail

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.38 设置推送免打扰时间

> POST  /user/push/limit

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|no_push_end_hour||no_push_end_hour|
|no_push_start_hour||no_push_start_hour|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.39 设置推送免打扰时间

> PUT  /user/push/limit

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|no_push_end_hour||no_push_end_hour|
|no_push_start_hour||no_push_start_hour|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.40 设置推送昵称

> POST  /user/push/nickname

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.41 设置推送昵称

> PUT  /user/push/nickname

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.42 获取标签

> GET  /user/push/tag

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[string]||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.43 绑定标签

> POST  /user/push/tag

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| tags|array[string]||false||

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.44 解绑标签

> DELETE  /user/push/tag

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| tags|array[string]||false||

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.45 删除所有标签

> DELETE  /user/push/tag/all

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.46 注册用户

> POST  /user/register

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| email|string||false|email|
| mobile|string||false|手机号码|
| password|string||false||
| username|string||false|用户名|
| verification_code|string||false|验证码，结合手机或邮箱使用|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|用户设置信息|
|⇥ auth_answer|string||false|验证问题答案|
|⇥ auth_mode|int32||false|验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请|
|⇥ auth_question|string||false|验证问题|
|⇥ auto_download|boolean||false|是否自动下载|
|⇥ group_confirm|boolean||false|邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请|
|⇥ id|int32||false||
|⇥ no_push|boolean||false|是否关闭推送消息|
|⇥ no_push_detail|boolean||false|是否推送详情|
|⇥ no_push_end_hour|int32||false|推送免打扰结束时间|
|⇥ no_push_start_hour|int32||false|推送免打扰开始时间|
|⇥ no_sounds|boolean||false|收到消息时是否静音|
|⇥ push_nick_name|string||false|推送昵称|
|⇥ push_token|string||false|推送token|
|⇥ silence_end_time|int32||false|推送不提醒结束时间|
|⇥ silence_start_time|int32||false|推送不提醒开始时间|
|⇥ user_id|int32||false|用户ID|
|⇥ vibratory|boolean||false|收到消息时否振动|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.47 批量注册用户

> POST  /user/register/batch

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| list|array[object]||false||
|⇥ password|string||false||
|⇥ username|string||false||

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false|失败原因|
|⇥ success|boolean||false|是否成功|
|⇥ user_id|int32||false|用户ID|
|⇥ username|string||false|用户名|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.48 注册推送用户

> POST  /user/register/push

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| alias|string||false|别名|
| device_guid|string||false|设备ID|
| password|string||false||
| push_token|string||false|推送token|
| sign|string||false|签名|
| username|string||false||

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|用户设置信息|
|⇥ auth_answer|string||false|验证问题答案|
|⇥ auth_mode|int32||false|验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请|
|⇥ auth_question|string||false|验证问题|
|⇥ auto_download|boolean||false|是否自动下载|
|⇥ group_confirm|boolean||false|邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请|
|⇥ id|int32||false||
|⇥ no_push|boolean||false|是否关闭推送消息|
|⇥ no_push_detail|boolean||false|是否推送详情|
|⇥ no_push_end_hour|int32||false|推送免打扰结束时间|
|⇥ no_push_start_hour|int32||false|推送免打扰开始时间|
|⇥ no_sounds|boolean||false|收到消息时是否静音|
|⇥ push_nick_name|string||false|推送昵称|
|⇥ push_token|string||false|推送token|
|⇥ silence_end_time|int32||false|推送不提醒结束时间|
|⇥ silence_start_time|int32||false|推送不提醒开始时间|
|⇥ user_id|int32||false|用户ID|
|⇥ vibratory|boolean||false|收到消息时否振动|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.49 注册用户

> POST  /user/register/v2

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| password|string||false||
| username|string||false||

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|用户设置信息|
|⇥ auth_answer|string||false|验证问题答案|
|⇥ auth_mode|int32||false|验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请|
|⇥ auth_question|string||false|验证问题|
|⇥ auto_download|boolean||false|是否自动下载|
|⇥ group_confirm|boolean||false|邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请|
|⇥ id|int32||false||
|⇥ no_push|boolean||false|是否关闭推送消息|
|⇥ no_push_detail|boolean||false|是否推送详情|
|⇥ no_push_end_hour|int32||false|推送免打扰结束时间|
|⇥ no_push_start_hour|int32||false|推送免打扰开始时间|
|⇥ no_sounds|boolean||false|收到消息时是否静音|
|⇥ push_nick_name|string||false|推送昵称|
|⇥ push_token|string||false|推送token|
|⇥ silence_end_time|int32||false|推送不提醒结束时间|
|⇥ silence_start_time|int32||false|推送不提醒开始时间|
|⇥ user_id|int32||false|用户ID|
|⇥ vibratory|boolean||false|收到消息时否振动|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.50 获取用户设置

> GET  /user/settings

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|用户设置信息|
|⇥ auth_answer|string||false|验证问题答案|
|⇥ auth_mode|int32||false|验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请|
|⇥ auth_question|string||false|验证问题|
|⇥ auto_download|boolean||false|是否自动下载|
|⇥ group_confirm|boolean||false|邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请|
|⇥ id|int32||false||
|⇥ no_push|boolean||false|是否关闭推送消息|
|⇥ no_push_detail|boolean||false|是否推送详情|
|⇥ no_push_end_hour|int32||false|推送免打扰结束时间|
|⇥ no_push_start_hour|int32||false|推送免打扰开始时间|
|⇥ no_sounds|boolean||false|收到消息时是否静音|
|⇥ push_nick_name|string||false|推送昵称|
|⇥ push_token|string||false|推送token|
|⇥ silence_end_time|int32||false|推送不提醒结束时间|
|⇥ silence_start_time|int32||false|推送不提醒开始时间|
|⇥ user_id|int32||false|用户ID|
|⇥ vibratory|boolean||false|收到消息时否振动|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.51 修改用户设置

> POST  /user/settings

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| auth_answer|string||false|验证问题答案|
| auth_mode|int32||false|验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请|
| auth_question|string||false|验证问题|
| auto_download|boolean||false|是否自动下载|
| group_confirm|boolean||false|邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请|
| id|int32||false||
| no_push|boolean||false|是否关闭推送消息|
| no_push_detail|boolean||false|是否推送详情|
| no_push_end_hour|int32||false|推送免打扰结束时间|
| no_push_start_hour|int32||false|推送免打扰开始时间|
| no_sounds|boolean||false|收到消息时是否静音|
| push_nick_name|string||false|推送昵称|
| push_token|string||false|推送token|
| silence_end_time|int32||false|推送不提醒结束时间|
| silence_start_time|int32||false|推送不提醒开始时间|
| user_id|int32||false|用户ID|
| vibratory|boolean||false|收到消息时否振动|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.52 修改用户设置

> PUT  /user/settings

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| auth_answer|string||false|验证问题答案|
| auth_mode|int32||false|验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请|
| auth_question|string||false|验证问题|
| auto_download|boolean||false|是否自动下载|
| group_confirm|boolean||false|邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请|
| id|int32||false||
| no_push|boolean||false|是否关闭推送消息|
| no_push_detail|boolean||false|是否推送详情|
| no_push_end_hour|int32||false|推送免打扰结束时间|
| no_push_start_hour|int32||false|推送免打扰开始时间|
| no_sounds|boolean||false|收到消息时是否静音|
| push_nick_name|string||false|推送昵称|
| push_token|string||false|推送token|
| silence_end_time|int32||false|推送不提醒结束时间|
| silence_start_time|int32||false|推送不提醒开始时间|
| user_id|int32||false|用户ID|
| vibratory|boolean||false|收到消息时否振动|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.53 设置新消息是否关闭声音提醒

> POST  /user/sounds

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.54 设置新消息是否关闭声音提醒

> PUT  /user/sounds

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.55 绑定token

> POST  /user/token/bind

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| device_sn|int32||false|设备SN|
| device_token|string||false|device token|
| notifier_name|string||false|证书名称|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.56 绑定token

> PUT  /user/token/bind

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| device_sn|int32||false|设备SN|
| device_token|string||false|device token|
| notifier_name|string||false|证书名称|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.57 解绑token

> POST  /user/token/unbind

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|deviceSn||deviceSn|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.58 解绑token

> DELETE  /user/token/unbind

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|deviceSn||deviceSn|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.59 修改用户名

> POST  /user/username

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|username||username|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.60 修改用户名

> PUT  /user/username

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|username||username|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.61 设置新消息是否振动

> POST  /user/vibratory

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 3.62 设置新消息是否振动

> PUT  /user/vibratory

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|value||value|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 



