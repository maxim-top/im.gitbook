

## 7    群接口

## 7.1  添加群管理员

> POST  /group/admin/add

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| user_list|array[int32]||false|用户id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.2  移除群管理员

> POST  /group/admin/remove

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| user_list|array[int32]||false|用户id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.3  移除群管理员

> DELETE  /group/admin/remove

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| user_list|array[int32]||false|用户id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.4  获取群管理员列表

> GET  /group/admin_list

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
| data|array[object]||false|结果数据|
|⇥ display_name|string||false|成员群名片|
|⇥ join_time|int32||false|成员入群时间|
|⇥ user_id|int32||false|用户id|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.5  根据群id和公告id获取群公告详情

> GET  /group/announcement

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|announcement_id||announcement_id|
|group_id||group_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false||
|⇥ author|int32||false|公告发布者|
|⇥ content|string||false|公告内容|
|⇥ created_at|int32||false|公告发布时间|
|⇥ group_id|int32||false|群id|
|⇥ id|int32||false|公告id|
|⇥ title|string||false|公告标题|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.6  删除公告

> POST  /group/announcement/delete

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|announcement_id||announcement_id|
|group_id||group_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.7  删除公告

> DELETE  /group/announcement/delete

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|announcement_id||announcement_id|
|group_id||group_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.8  编辑群公告

> POST  /group/announcement/edit

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| content|string||false|公告内容|
| group_id|int32||false|群组id|
| title|string||false|公告标题|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false||
|⇥ author|int32||false|公告发布者|
|⇥ content|string||false|公告内容|
|⇥ created_at|int32||false|公告发布时间|
|⇥ group_id|int32||false|群id|
|⇥ id|int32||false|公告id|
|⇥ title|string||false|公告标题|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.9  获取最新一条群公告详情

> GET  /group/announcement/last

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
|⇥ author|int32||false|公告发布者|
|⇥ content|string||false|公告内容|
|⇥ created_at|int32||false|公告发布时间|
|⇥ group_id|int32||false|群id|
|⇥ id|int32||false|公告id|
|⇥ title|string||false|公告标题|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.10 获取群公告列表

> GET  /group/announcement/list

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
| data|array[object]||false|结果数据|
|⇥ author|int32||false|公告发布者|
|⇥ content|string||false|公告内容|
|⇥ created_at|int32||false|公告发布时间|
|⇥ group_id|int32||false|群id|
|⇥ id|int32||false|公告id|
|⇥ title|string||false|公告标题|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.11 获取群申请列表

> POST  /group/application_list

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|cursor||cursor|
|limit||limit|
|version||version|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_list|array[int32]||false|群id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| cursor|string||false|游标，用于翻页|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|
| total|int32||false|总数|
| version|int32||false|版本，目前没用到，留作扩展|


### 接口描述
> 




## 7.12 申请入群

> POST  /group/apply

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| reason|string||false|申请入群原因|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false||
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.13 管理员处理入群申请

> POST  /group/apply/handle

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| approval|boolean||false|审批，bool类型，true为同意，false为拒绝|
| group_id|int32||false|群id|
| user_id|int32||false|用户id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false||
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.14 管理员处理入群申请

> PUT  /group/apply/handle

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| approval|boolean||false|审批，bool类型，true为同意，false为拒绝|
| group_id|int32||false|群id|
| user_id|int32||false|用户id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false||
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.15 将用户禁言

> POST  /group/ban

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| duration|int32||false|禁言时长，单位为分钟|
| group_id|int32||false|群id|
| user_list|array[int32]||false|用户id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.16 获取禁言列表

> GET  /group/banned_list

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|cursor||cursor|
|group_id||group_id|
|limit||limit|
|version||version|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| cursor|string||false|游标，用于翻页|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|
| total|int32||false|总数|
| version|int32||false|版本，目前没用到，留作扩展|


### 接口描述
> 




## 7.17 将用户加入黑名单

> POST  /group/block

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| user_list|array[int32]||false|用户id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.18 获取黑名单列表

> GET  /group/blocked_list

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|cursor||cursor|
|group_id||group_id|
|limit||limit|
|version||version|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| cursor|string||false|游标，用于翻页|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|
| total|int32||false|总数|
| version|int32||false|版本，目前没用到，留作扩展|


### 接口描述
> 




## 7.19 创建群

> POST  /group/create

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| avatar|string||false|群头像|
| description|string||false|群描述|
| name|string||false|群名称|
| type|int32||false|群类型 1表示公开群，0表示私有群, 2表示聊天室|
| user_list|array[int32]||false|邀请入群的用户id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.20 解散群

> POST  /group/destroy

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
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.21 解散群

> DELETE  /group/destroy

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
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.22 更新群名片

> POST  /group/display_name

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|string||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.23 更新群名片

> PUT  /group/display_name

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|string||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.24 下载群文件

> GET  /group/file

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|file_id||file_id|
|group_id||group_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|群共享文件返回格式|
|⇥ created_at|int32||false||
|⇥ file_id|int32||false|共享文件id|
|⇥ group_id|int32||false|群id|
|⇥ name|string||false|共享文件名称|
|⇥ size|int32||false|共享文件大小|
|⇥ type|string||false|共享文件类型|
|⇥ updated_at|int32||false||
|⇥ uploader|int32||false|共享文件上传者|
|⇥ url|string||false|共享文件url|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.25 删除群文件

> POST  /group/file/delete

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| file_list|array[int32]||false|文件id列表|
| group_id|int32||false|群id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ file_id|int32||false||
|⇥ reason|string||false||
|⇥ result|string||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.26 删除群文件

> DELETE  /group/file/delete

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| file_list|array[int32]||false|文件id列表|
| group_id|int32||false|群id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ file_id|int32||false||
|⇥ reason|string||false||
|⇥ result|string||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.27 获取群文件列表

> GET  /group/file/list

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
| data|array[object]||false|结果数据|
|⇥ created_at|int32||false||
|⇥ file_id|int32||false|共享文件id|
|⇥ group_id|int32||false|群id|
|⇥ name|string||false|共享文件名称|
|⇥ size|int32||false|共享文件大小|
|⇥ type|string||false|共享文件类型|
|⇥ updated_at|int32||false||
|⇥ uploader|int32||false|共享文件上传者|
|⇥ url|string||false|共享文件url|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.28 更新群文件名称

> POST  /group/file/update_name

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| file_id|int32||false|文件id|
| group_id|int32||false|群id|
| name|string||false|文件新名称|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.29 更新群文件名称

> PUT  /group/file/update_name

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| file_id|int32||false|文件id|
| group_id|int32||false|群id|
| name|string||false|文件新名称|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.30 上传群文件

> POST  /group/file/upload

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| name|string||false|文件名称|
| size|int32||false|文件大小|
| type|string||false|文件类型|
| url|string||false|文件url|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|群共享文件返回格式|
|⇥ created_at|int32||false||
|⇥ file_id|int32||false|共享文件id|
|⇥ group_id|int32||false|群id|
|⇥ name|string||false|共享文件名称|
|⇥ size|int32||false|共享文件大小|
|⇥ type|string||false|共享文件类型|
|⇥ updated_at|int32||false||
|⇥ uploader|int32||false|共享文件上传者|
|⇥ url|string||false|共享文件url|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.31 根据group id获取群信息

> GET  /group/info

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
|⇥ apply_approval|int32||false|入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请|
|⇥ avatar|string||false|群头像|
|⇥ ban_expire_time|int32||false|全员禁言过期时间（秒），禁言期间只允许管理员发消息， 为0或小于当前时间表示不禁言, -1表示永久禁言|
|⇥ created_at|int32||false|创建时间|
|⇥ description|string||false|群描述|
|⇥ ext|string||false|群扩展信息|
|⇥ group_id|int32||false|群id|
|⇥ history_visible|boolean||false|新成员可见历史聊天记录设置|
|⇥ member_invite|boolean||false|群成员邀请设置|
|⇥ member_modify|boolean||false|群成员修改群信息设置|
|⇥ msg_mute_mode|int32||false|群消息屏蔽模式|
|⇥ msg_push_mode|int32||false|群消息推送模式|
|⇥ name|string||false|群名称|
|⇥ owner_id|int32||false|群主id|
|⇥ read_ack|boolean||false|群消息已读功能设置|
|⇥ status|int32||false|群状态, 0：正常, 1：已解散|
|⇥ type|int32||false|群类型|
|⇥ updated_at|int32||false|更新时间|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.32 更新群头像

> POST  /group/info/avatar

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|string||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.33 更新群头像

> PUT  /group/info/avatar

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|string||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.34 根据group id获取群信息

> POST  /group/info/batch

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_list|array[int32]||false|群id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ apply_approval|int32||false|入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请|
|⇥ avatar|string||false||
|⇥ capacity|int32||false||
|⇥ count|int32||false||
|⇥ group_id|int32||false||
|⇥ msg_mute_mode|int32||false|群消息屏蔽设置|
|⇥ msg_push_mode|int32||false|群消息推送设置|
|⇥ name|string||false||
|⇥ owner|int32||false||
|⇥ status|int32||false|群状态, 0：正常, 1：已解散|
|⇥ type|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.35 更新群描述

> POST  /group/info/description

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|string||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.36 更新群描述

> PUT  /group/info/description

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|string||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.37 更新扩展信息

> POST  /group/info/ext

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|string||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.38 更新扩展信息

> PUT  /group/info/ext

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|string||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.39 更新群名称

> POST  /group/info/name

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|string||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.40 更新群名称

> PUT  /group/info/name

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|string||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.41 获取群邀请列表

> GET  /group/invitation_list

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|cursor||cursor|
|limit||limit|
|version||version|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| cursor|string||false|游标，用于翻页|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|
| total|int32||false|总数|
| version|int32||false|版本，目前没用到，留作扩展|


### 接口描述
> 




## 7.42 邀请入群

> POST  /group/invite

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| reason|string||false|邀请理由|
| user_list|array[int32]||false|受邀请者id，List类型，单次可邀请多个用户入群|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.43 用户处理入群邀请

> POST  /group/invite/handle

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| approval|boolean||false|审批，bool类型，true为同意，false为拒绝|
| group_id|int32||false|群id|
| user_id|int32||false|用户id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.44 用户处理入群邀请

> PUT  /group/invite/handle

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| approval|boolean||false|审批，bool类型，true为同意，false为拒绝|
| group_id|int32||false|群id|
| user_id|int32||false|用户id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.45 将成员踢出群

> POST  /group/kick

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| user_list|array[int32]||false|用户id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.46 将成员踢出群

> DELETE  /group/kick

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| user_list|array[int32]||false|用户id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.47 成员退出群

> POST  /group/leave

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
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.48 成员退出群

> DELETE  /group/leave

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
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.49 根据group id获取群成员列表

> GET  /group/member_list

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求参数(Query Param)
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|cursor||cursor|
|group_id||group_id|
|limit||limit|
|version||version|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| cursor|string||false|游标，用于翻页|
| data|array[object]||false|结果数据|
|⇥ display_name|string||false|成员群名片|
|⇥ join_time|int32||false|成员入群时间|
|⇥ user_id|int32||false|用户id|
| message|string||false|错误信息，如果成功，该项为null|
| total|int32||false|总数|
| version|int32||false|版本，目前没用到，留作扩展|


### 接口描述
> 




## 7.50 批量获取群成员的群名片

> POST  /group/members/display_name

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| user_list|array[int32]||false|用户id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ display_name|string||false|成员群名片|
|⇥ join_time|int32||false|成员入群时间|
|⇥ user_id|int32||false|用户id|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.51 设置群消息屏蔽模式

> POST  /group/msg/mute_mode

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| msg_mute_mode|int32||false|群消息屏蔽模式： 0 不屏蔽1 屏蔽本地消息通知2 屏蔽消息，不接收消息|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.52 设置群消息屏蔽模式

> PUT  /group/msg/mute_mode

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| msg_mute_mode|int32||false|群消息屏蔽模式： 0 不屏蔽1 屏蔽本地消息通知2 屏蔽消息，不接收消息|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.53 设置群消息推送模式

> POST  /group/msg/push_mode

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| msg_push_mode|int32||false|群消息推送类型： 0:接收所有推送;1:不接受推送;2:接收管理员和@消息推送;3:只接收管理员消息推送;4:只接收@消息推送|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.54 设置群消息推送模式

> PUT  /group/msg/push_mode

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| msg_push_mode|int32||false|群消息推送类型： 0:接收所有推送;1:不接受推送;2:接收管理员和@消息推送;3:只接收管理员消息推送;4:只接收@消息推送|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.55 获取公开群列表

> GET  /group/public_list

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




## 7.56 二维码邀请入群

> POST  /group/qrcode/invite

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| qr_info|string||false||

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.57 获取群邀请二维码信息

> GET  /group/qrcode/sign

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
|⇥ create_at|int32||false|二维码生成时间|
|⇥ expire_at|int32||false|二维码过期时间|
|⇥ qr_info|string||false|二维码信息|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.58 获取群设置

> GET  /group/settings

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
|⇥ apply_approval|int32||false|入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请|
|⇥ avatar|string||false|群头像|
|⇥ ban_expire_time|int32||false|全员禁言过期时间（秒），禁言期间只允许管理员发消息， 为0或小于当前时间表示不禁言, -1表示永久禁言|
|⇥ created_at|int32||false|创建时间|
|⇥ description|string||false|群描述|
|⇥ ext|string||false|群扩展信息|
|⇥ group_id|int32||false|群id|
|⇥ history_visible|boolean||false|新成员可见历史聊天记录设置|
|⇥ member_invite|boolean||false|群成员邀请设置|
|⇥ member_modify|boolean||false|群成员修改群信息设置|
|⇥ msg_mute_mode|int32||false|群消息屏蔽模式|
|⇥ msg_push_mode|int32||false|群消息推送模式|
|⇥ name|string||false|群名称|
|⇥ owner_id|int32||false|群主id|
|⇥ read_ack|boolean||false|群消息已读功能设置|
|⇥ status|int32||false|群状态, 0：正常, 1：已解散|
|⇥ type|int32||false|群类型|
|⇥ updated_at|int32||false|更新时间|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.59 更新群设置--是否允许成员邀请

> POST  /group/settings/allow_member_invitation

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|boolean||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.60 更新群设置--是否允许成员邀请

> PUT  /group/settings/allow_member_invitation

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|boolean||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.61 更新群设置--群成员是否可修改群信息

> POST  /group/settings/allow_member_modify

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|boolean||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.62 更新群设置--群成员是否可修改群信息

> PUT  /group/settings/allow_member_modify

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|boolean||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.63 全员禁言，只允许管理员发消息

> POST  /group/settings/ban_all

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| duration|int32||false|禁言时长，单位为分钟|
| group_id|int32||false|群id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false||
|⇥ ban_expire_time|int32||false|全员禁言过期时间|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.64 更新群设置--是否开启群消息已读功能

> POST  /group/settings/enable_read_ack

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|boolean||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.65 更新群设置--是否开启群消息已读功能

> PUT  /group/settings/enable_read_ack

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|boolean||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.66 更新群设置--新成员是否可见群历史聊天记录

> POST  /group/settings/history_visible

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|boolean||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.67 更新群设置--新成员是否可见群历史聊天记录

> PUT  /group/settings/history_visible

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| value|boolean||false|更新内容|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.68 更新群设置--群申请是否需要管理员审批

> POST  /group/settings/require_admin_approval

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| apply_approval|int32||false|入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请|
| group_id|int32||false|群id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.69 更新群设置--群申请是否需要管理员审批

> PUT  /group/settings/require_admin_approval

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| apply_approval|int32||false|入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请|
| group_id|int32||false|群id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.70 取消全员禁言

> POST  /group/settings/unban_all

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|boolean||false|结果数据|
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.71 转让群

> POST  /group/transfer

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| new_owner|int32||false|新群主的user_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false||
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.72 转让群

> PUT  /group/transfer

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| new_owner|int32||false|新群主的user_id|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|object||false||
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.73 从禁言列表移除用户

> POST  /group/unban

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| user_list|array[int32]||false|用户id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.74 从黑名单移除用户

> POST  /group/unblock

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| user_list|array[int32]||false|用户id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.75 从黑名单移除用户

> DELETE  /group/unblock

### 请求头
| 参数名称 | 默认值 | 描述 |
| ------ | ------ | ------ |
|access-token||令牌||app_id||应用ID||group_id||仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口||user_id||仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口|

### 请求体(Request Body)
| 参数名称 | 数据类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| group_id|int32||false|群id|
| user_list|array[int32]||false|用户id列表|

### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 默认值 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|返回码，200是成功|
| data|array[object]||false|结果数据|
|⇥ reason|string||false||
|⇥ result|string||false||
|⇥ user_id|int32||false||
| message|string||false|错误信息，如果成功，该项为null|


### 接口描述
> 




## 7.76 获取用户的群组列表

> GET  /group/user_joined

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



