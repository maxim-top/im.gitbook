
## 8    好友管理接口

## 8.1  同意好友申请

> POST  /roster/accept

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|user_id||user_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.2  同意好友申请

> PUT  /roster/accept

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|user_id||user_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.3  申请加好友

> POST  /roster/apply

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| alias|string||false|备注名称|
| auth_answer|string||false|问题答案|
| reason|string||false|申请描述|
| user_id|int32||false|被申请用户 ID|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.4  批量添加好友

> POST  /roster/apply/batch

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| alias|string||false|备注名称|
| reason|string||false|申请描述|
| user_id|int32||false|被申请用户 ID|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|批量添加好友返回结果|
|⇥ fails|array[object]||false||
|⇥⇥ reason|string||false|失败原因|
|⇥⇥ user_id|int32||false|用户ID|
|⇥ success|array[int32]||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.5  好友申请列表

> GET  /roster/apply/list

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|cursor||cursor|
|limit||limit|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| cursor|string||false|游标，返回结果中缺失 cursor，表示已经返回最后一页|
| data|array[object]||false|结果数据|
|⇥ expired_time|int32||false|过期时间|
|⇥ reason|string||false|申请描述|
|⇥ status|int32||false||
|⇥ user_id|int32||false|发起加好友申请的用户ID|
| message|string||false|错误信息，如果成功，该项为null|
| version|int32||false|版本|


### 接口描述
> 




## 8.6  添加黑名单

> POST  /roster/block

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|user_id||user_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.7  添加黑名单

> PUT  /roster/block

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|user_id||user_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.8  黑名单列表

> GET  /roster/blocked_list

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[int32]||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.9  拒绝好友申请

> POST  /roster/decline

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| reason|string||false|拒绝的原因|
| user_id|int32||false|拒绝的用户ID|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.10 拒绝好友申请

> PUT  /roster/decline

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| reason|string||false|拒绝的原因|
| user_id|int32||false|拒绝的用户ID|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.11 删除好友

> POST  /roster/delete

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|user_id||user_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.12 删除好友

> DELETE  /roster/delete

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|user_id||user_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.13 更新好友扩展信息

> POST  /roster/ext

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| alias|string||false|备注名称|
| ext|string||false|扩展信息|
| mute_notification|boolean||false|是否接收消息提醒|
| user_id|int32||false|好友用户ID|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.14 更新好友扩展信息

> PUT  /roster/ext

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| alias|string||false|备注名称|
| ext|string||false|扩展信息|
| mute_notification|boolean||false|是否接收消息提醒|
| user_id|int32||false|好友用户ID|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.15 用ID搜索用户

> GET  /roster/id

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|user_id||用户ID|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|好友列表|
|⇥ alias|string||false||
|⇥ auth_mode|int32||false|验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请|
|⇥ auth_question|string||false|验证问题|
|⇥ avatar|string||false|头像|
|⇥ description|string||false|描述信息|
|⇥ ext|string||false||
|⇥ mute_notification|boolean||false||
|⇥ nick_name|string||false|昵称或名称|
|⇥ public_info|string||false|公开信息，好友和陌生人可见|
|⇥ relation|int32||false||
|⇥ user_id|int32||false|好友用户ID|
|⇥ username|string||false|用户名|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.16 好友列表

> GET  /roster/list

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|cursor||cursor|
|limit||limit|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| cursor|string||false|游标，返回结果中缺失 cursor，表示已经返回最后一页|
| data|array[int32]||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|
| version|int32||false|版本|


### 接口描述
> 




## 8.17 好友详情列表

> POST  /roster/list

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
| data|array[object]||false|结果数据|
|⇥ alias|string||false||
|⇥ auth_mode|int32||false|验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请|
|⇥ auth_question|string||false|验证问题|
|⇥ avatar|string||false|头像|
|⇥ description|string||false|描述信息|
|⇥ ext|string||false||
|⇥ mute_notification|boolean||false||
|⇥ nick_name|string||false|昵称或名称|
|⇥ public_info|string||false|公开信息，好友和陌生人可见|
|⇥ relation|int32||false||
|⇥ user_id|int32||false|好友用户ID|
|⇥ username|string||false|用户名|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.18 是否允许发消息

> GET  /roster/may_message

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|roster_id||roster_id|
|user_id||user_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.19 用手机号搜索用户

> GET  /roster/mobile

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
| data|object||false|好友列表|
|⇥ alias|string||false||
|⇥ auth_mode|int32||false|验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请|
|⇥ auth_question|string||false|验证问题|
|⇥ avatar|string||false|头像|
|⇥ description|string||false|描述信息|
|⇥ ext|string||false||
|⇥ mute_notification|boolean||false||
|⇥ nick_name|string||false|昵称或名称|
|⇥ public_info|string||false|公开信息，好友和陌生人可见|
|⇥ relation|int32||false||
|⇥ user_id|int32||false|好友用户ID|
|⇥ username|string||false|用户名|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.20 用用户名搜索用户

> GET  /roster/name

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
| data|object||false|好友列表|
|⇥ alias|string||false||
|⇥ auth_mode|int32||false|验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请|
|⇥ auth_question|string||false|验证问题|
|⇥ avatar|string||false|头像|
|⇥ description|string||false|描述信息|
|⇥ ext|string||false||
|⇥ mute_notification|boolean||false||
|⇥ nick_name|string||false|昵称或名称|
|⇥ public_info|string||false|公开信息，好友和陌生人可见|
|⇥ relation|int32||false||
|⇥ user_id|int32||false|好友用户ID|
|⇥ username|string||false|用户名|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.21 从黑名单移除

> POST  /roster/unblock

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|user_id||user_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 8.22 从黑名单移除

> DELETE  /roster/unblock

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|user_id||user_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




