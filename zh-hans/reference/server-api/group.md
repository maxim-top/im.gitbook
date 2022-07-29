# 4 群接口{#group}

## 4.1 添加群管理员{#post__group_admin_add}

> POST /group/admin/add

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| user_list | array[int64] | true |  | 用户id列表 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ reason | string | 错误信息 |
|⇥ result | string | 操作结果： success - 成功, fail - 失败 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.2 移除群管理员{#delete__group_admin_remove}

> DELETE /group/admin/remove

> POST /group/admin/remove

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| user_list | array[int64] | true |  | 用户id列表 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ reason | string | 错误信息 |
|⇥ result | string | 操作结果： success - 成功, fail - 失败 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.3 获取群管理员列表{#get__group_admin_list}

> GET /group/admin_list

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | 群组ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ display_name | string | 成员群名片 |
|⇥ expired_time | int64 | 禁言过期时间(毫秒) |
|⇥ join_time | int64 | 成员入群时间戳(毫秒) |
|⇥ user_id | int64 | 用户id |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.4 根据群id和公告id获取群公告详情{#get__group_announcement}

> GET /group/announcement

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| announcement_id | int64 | true | 公告ID |
| group_id | int64 | true | 群组ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ author | int64 | 公告发布者 |
|⇥ content | string | 公告内容 |
|⇥ created_at | int64 | 公告发布时间(毫秒) |
|⇥ group_id | int64 | 群id |
|⇥ id | int64 | 公告id |
|⇥ title | string | 公告标题 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.5 删除公告{#delete__group_announcement_delete}

> DELETE /group/announcement/delete

> POST /group/announcement/delete

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| announcement_id | int64 | true | 公告ID |
| group_id | int64 | true | 群组ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.6 编辑群公告{#post__group_announcement_edit}

> POST /group/announcement/edit

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| content | string | true |  | 公告内容 |
| group_id | int64 | true |  | 群组id |
| title | string | true |  | 公告标题 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ author | int64 | 公告发布者 |
|⇥ content | string | 公告内容 |
|⇥ created_at | int64 | 公告发布时间(毫秒) |
|⇥ group_id | int64 | 群id |
|⇥ id | int64 | 公告id |
|⇥ title | string | 公告标题 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.7 获取最新一条群公告详情{#get__group_announcement_last}

> GET /group/announcement/last

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | 群组ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ author | int64 | 公告发布者 |
|⇥ content | string | 公告内容 |
|⇥ created_at | int64 | 公告发布时间(毫秒) |
|⇥ group_id | int64 | 群id |
|⇥ id | int64 | 公告id |
|⇥ title | string | 公告标题 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.8 获取群公告列表{#get__group_announcement_list}

> GET /group/announcement/list

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | 群组ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ author | int64 | 公告发布者 |
|⇥ content | string | 公告内容 |
|⇥ created_at | int64 | 公告发布时间(毫秒) |
|⇥ group_id | int64 | 群id |
|⇥ id | int64 | 公告id |
|⇥ title | string | 公告标题 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.9 获取群申请列表{#post__group_application_list}

> POST /group/application_list

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
| cursor | string | false | 游标: 从哪开始取 |
| limit | int32 | false | 最多取多少条 |
| version | int64 | false | 版本号 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_list | array[int64] | true |  | 群id列表 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| cursor | string | 游标，用于翻页 |
| data | array[object] | 结果数据 |
|⇥ applicant_id | int64 | 申请者的用户ID |
|⇥ expired_time | int64 | 申请过期时间戳（毫秒） |
|⇥ group_id | int64 | 群组ID |
|⇥ reason | string | 原因 |
|⇥ status | int32 | 状态： 0 - 待处理，1 - 同意，2 - 拒绝 |
| message | string | 错误信息，如果成功，该项为null |
| total | int64 | 总数 |
| version | int64 | 版本，目前没用到，留作扩展 |
#### 接口描述
> 

## 4.10 申请入群{#post__group_apply}

> POST /group/apply

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| reason | string | false |  | 申请入群原因 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ reason | string | 错误信息 |
|⇥ result | string | 操作结果： success - 成功, fail - 失败 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.11 管理员处理入群申请{#put__group_apply_handle}

> PUT /group/apply/handle

> POST /group/apply/handle

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| approval | boolean | true |  | 审批，bool类型，true为同意，false为拒绝 |
| group_id | int64 | true |  | 群id |
| user_id | int64 | true |  | 用户id |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ reason | string | 错误信息 |
|⇥ result | string | 操作结果： success - 成功, fail - 失败 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.12 将用户禁言{#post__group_ban}

> POST /group/ban

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| duration | int64 | true |  | 禁言时长，单位为分钟 |
| group_id | int64 | true |  | 群id |
| user_list | array[int64] | true |  | 用户id列表 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ reason | string | 错误信息 |
|⇥ result | string | 操作结果： success - 成功, fail - 失败 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.13 获取禁言列表{#get__group_banned_list}

> GET /group/banned_list

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| cursor | string | false | 游标：从哪开始取 |
| group_id | int64 | true | 群组ID |
| limit | int32 | false | 取多少条 |
| version | int64 | false | 版本 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| cursor | string | 游标，用于翻页 |
| data | array[object] | 结果数据 |
|⇥ display_name | string | 成员群名片 |
|⇥ expired_time | int64 | 禁言过期时间(毫秒) |
|⇥ join_time | int64 | 成员入群时间戳(毫秒) |
|⇥ user_id | int64 | 用户id |
| message | string | 错误信息，如果成功，该项为null |
| total | int64 | 总数 |
| version | int64 | 版本，目前没用到，留作扩展 |
#### 接口描述
> 

## 4.14 将用户加入黑名单{#post__group_block}

> POST /group/block

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| user_list | array[int64] | true |  | 用户id列表 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ reason | string | 错误信息 |
|⇥ result | string | 操作结果： success - 成功, fail - 失败 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.15 获取黑名单列表{#get__group_blocked_list}

> GET /group/blocked_list

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| cursor | string | false | 游标：从哪开始取 |
| group_id | int64 | true | 群组ID |
| limit | int32 | false | 取多少条 |
| version | int64 | false | 版本 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| cursor | string | 游标，用于翻页 |
| data | array[object] | 结果数据 |
|⇥ created_at | string | 创建时间 |
|⇥ group_id | int64 | 群组ID |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
| total | int64 | 总数 |
| version | int64 | 版本，目前没用到，留作扩展 |
#### 接口描述
> 

## 4.16 创建群{#post__group_create}

> POST /group/create

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| avatar | string | false |  | 群头像 |
| description | string | false |  | 群描述 |
| name | string | false |  | 群名称 |
| type | int32 | false |  | 群类型 0表示私有群, 2表示聊天室 |
| user_list | array[int64] | false |  | 邀请入群的用户id列表 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.17 解散群{#delete__group_destroy}

> DELETE /group/destroy

> POST /group/destroy

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | 群组ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.18 更新群名片{#put__group_display_name}

> PUT /group/display_name

> POST /group/display_name

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| value | string | true |  | 更新内容 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.19 下载群文件{#get__group_file}

> GET /group/file

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| file_id | int64 | true | 文件ID |
| group_id | int64 | true | 群组ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ created_at | int64 | 创建时间戳(毫秒) |
|⇥ file_id | int64 | 共享文件id |
|⇥ group_id | int64 | 群id |
|⇥ name | string | 共享文件名称 |
|⇥ size | int64 | 共享文件大小 |
|⇥ type | string | 共享文件类型 |
|⇥ updated_at | int64 | 更新时间戳(毫秒) |
|⇥ uploader | int64 | 共享文件上传者 |
|⇥ url | string | 共享文件url |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.20 删除群文件{#delete__group_file_delete}

> DELETE /group/file/delete

> POST /group/file/delete

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| file_list | array[int64] | true |  | 文件id列表 |
| group_id | int64 | true |  | 群id |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ file_id | int64 | 文件ID |
|⇥ reason | string | 原因 |
|⇥ result | string | 结果： success - 成功, fail - 失败 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.21 获取群文件列表{#get__group_file_list}

> GET /group/file/list

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | 群组ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ created_at | int64 | 创建时间戳(毫秒) |
|⇥ file_id | int64 | 共享文件id |
|⇥ group_id | int64 | 群id |
|⇥ name | string | 共享文件名称 |
|⇥ size | int64 | 共享文件大小 |
|⇥ type | string | 共享文件类型 |
|⇥ updated_at | int64 | 更新时间戳(毫秒) |
|⇥ uploader | int64 | 共享文件上传者 |
|⇥ url | string | 共享文件url |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.22 更新群文件名称{#put__group_file_update_name}

> PUT /group/file/update_name

> POST /group/file/update_name

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| file_id | int64 | true |  | 文件id |
| group_id | int64 | true |  | 群id |
| name | string | true |  | 文件新名称 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.23 上传群文件{#post__group_file_upload}

> POST /group/file/upload

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| name | string | true |  | 文件名称 |
| size | int64 | true |  | 文件大小 |
| type | string | false |  | 文件类型 |
| url | string | true |  | 文件url |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ created_at | int64 | 创建时间戳(毫秒) |
|⇥ file_id | int64 | 共享文件id |
|⇥ group_id | int64 | 群id |
|⇥ name | string | 共享文件名称 |
|⇥ size | int64 | 共享文件大小 |
|⇥ type | string | 共享文件类型 |
|⇥ updated_at | int64 | 更新时间戳(毫秒) |
|⇥ uploader | int64 | 共享文件上传者 |
|⇥ url | string | 共享文件url |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.24 根据group id获取群信息{#get__group_info}

> GET /group/info

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | 群组ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ apply_approval | int32 | 入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请 |
|⇥ avatar | string | 群头像 |
|⇥ ban_expire_time | int64 | 全员禁言过期时间（秒），禁言期间只允许管理员发消息， 为0或小于当前时间表示不禁言, -1表示永久禁言 |
|⇥ capacity | int64 | 群容量 |
|⇥ count | int64 | 当前人数 |
|⇥ created_at | int64 | 创建时间(毫秒） |
|⇥ description | string | 群描述 |
|⇥ ext | string | 群扩展信息 |
|⇥ group_id | int64 | 群id |
|⇥ history_visible | boolean | 新成员可见历史聊天记录设置： true - 新成员可见历史聊天记录， false - 新成员不可见历史聊天记录 |
|⇥ member_invite | boolean | 是否允许群成员邀请其他人入群: true - 群成员允许邀请其他人入群， false - 群成员不允许邀请其他人入群 |
|⇥ member_modify | boolean | 群成员修改群信息设置： true - 允许群成员修改群信息， false - 不允许群成员修改群信息 |
|⇥ msg_mute_mode | int32 | 群消息屏蔽模式：0 - 表示不屏蔽， 1 - 表示屏蔽本地消息通知， 2 - 表示屏蔽消息，不接收消息 |
|⇥ msg_push_mode | int32 | 群消息推送模式：0 - 接收所有推送， 1 - 不接受推送， 2 - 接收管理员和@消息推送， 3 - 只接收管理员消息推送，4 - 只接收@消息推送 |
|⇥ name | string | 群名称 |
|⇥ owner_id | int64 | 群主id |
|⇥ read_ack | boolean | 是否开启群消息已读功能设置：true - 开启群消息已读功能， false - 不开启群消息已读功能 |
|⇥ status | int32 | 群状态, 0：正常, 1：已解散 |
|⇥ type | int32 | 群类型： 0 - 表示私有群, 2 - 表示聊天室 |
|⇥ updated_at | int64 | 更新时间（毫秒） |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.25 更新群头像{#put__group_info_avatar}

> PUT /group/info/avatar

> POST /group/info/avatar

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| value | string | true |  | 更新内容 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.26 根据group id获取群信息{#post__group_info_batch}

> POST /group/info/batch

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_list | array[int64] | true |  | 群id列表 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ apply_approval | int32 | 入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请 |
|⇥ avatar | string | 群头像 |
|⇥ capacity | int64 | 群容量 |
|⇥ count | int64 | 当前人数 |
|⇥ group_id | int64 | 群组ID |
|⇥ msg_mute_mode | int32 | 群消息屏蔽模式：0 - 表示不屏蔽， 1 - 表示屏蔽本地消息通知， 2 - 表示屏蔽消息，不接收消息 |
|⇥ msg_push_mode | int32 | 群消息推送模式：0 - 接收所有推送， 1 - 不接受推送， 2 - 接收管理员和@消息推送， 3 - 只接收管理员消息推送，4 - 只接收@消息推送 |
|⇥ name | string | 群名称 |
|⇥ owner | int64 | 群主id |
|⇥ status | int32 | 群状态, 0：正常, 1：已解散 |
|⇥ type | int32 | 群类型： 0 - 表示私有群, 2 - 表示聊天室 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.27 更新群描述{#put__group_info_description}

> PUT /group/info/description

> POST /group/info/description

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| value | string | true |  | 更新内容 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.28 更新扩展信息{#put__group_info_ext}

> PUT /group/info/ext

> POST /group/info/ext

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| value | string | true |  | 更新内容 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.29 更新群名称{#put__group_info_name}

> PUT /group/info/name

> POST /group/info/name

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| value | string | true |  | 更新内容 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.30 获取群邀请列表{#get__group_invitation_list}

> GET /group/invitation_list

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
| cursor | string | false | 游标: 从哪开始取 |
| limit | int32 | false | 最多取多少条 |
| version | int64 | false | 版本号 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| cursor | string | 游标，用于翻页 |
| data | array[object] | 结果数据 |
|⇥ expired_time | int64 | 过期时间戳（毫秒） |
|⇥ group_id | int64 | 群组ID |
|⇥ invitee_id | int64 | 被邀请者ID |
|⇥ inviter_id | int64 | 邀请者ID |
|⇥ reason | string | 原因 |
|⇥ status | int32 | 状态： 0 - 待处理，1 - 用户同意，2 - 用户拒绝 |
|⇥ updated_at | string | 更新时间 |
| message | string | 错误信息，如果成功，该项为null |
| total | int64 | 总数 |
| version | int64 | 版本，目前没用到，留作扩展 |
#### 接口描述
> 

## 4.31 邀请入群{#post__group_invite}

> POST /group/invite

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| reason | string | false |  | 邀请理由 |
| user_list | array[int64] | true |  | 受邀请者id，List类型，单次可邀请多个用户入群 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ reason | string | 错误信息 |
|⇥ result | string | 操作结果： success - 成功, fail - 失败 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.32 用户处理入群邀请{#put__group_invite_handle}

> PUT /group/invite/handle

> POST /group/invite/handle

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| approval | boolean | true |  | 审批，bool类型，true为同意，false为拒绝 |
| group_id | int64 | true |  | 群id |
| user_id | int64 | true |  | 用户id |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.33 将成员踢出群{#delete__group_kick}

> DELETE /group/kick

> POST /group/kick

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| user_list | array[int64] | true |  | 用户id列表 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ reason | string | 错误信息 |
|⇥ result | string | 操作结果： success - 成功, fail - 失败 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.34 成员退出群{#delete__group_leave}

> DELETE /group/leave

> POST /group/leave

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | 群组ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.35 根据group id获取群成员列表{#get__group_member_list}

> GET /group/member_list

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| cursor | string | false | 游标：从哪开始取 |
| group_id | int64 | true | 群组ID |
| limit | int32 | false | 取多少条 |
| version | int64 | false | 版本 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| cursor | string | 游标，用于翻页 |
| data | array[object] | 结果数据 |
|⇥ display_name | string | 成员群名片 |
|⇥ expired_time | int64 | 禁言过期时间(毫秒) |
|⇥ join_time | int64 | 成员入群时间戳(毫秒) |
|⇥ user_id | int64 | 用户id |
| message | string | 错误信息，如果成功，该项为null |
| total | int64 | 总数 |
| version | int64 | 版本，目前没用到，留作扩展 |
#### 接口描述
> 

## 4.36 批量获取群成员的群名片{#post__group_members_display_name}

> POST /group/members/display_name

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| user_list | array[int64] | true |  | 用户id列表 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ display_name | string | 成员群名片 |
|⇥ expired_time | int64 | 禁言过期时间(毫秒) |
|⇥ join_time | int64 | 成员入群时间戳(毫秒) |
|⇥ user_id | int64 | 用户id |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.37 设置群消息屏蔽模式{#put__group_msg_mute_mode}

> PUT /group/msg/mute_mode

> POST /group/msg/mute_mode

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| msg_mute_mode | int32 | true |  | 群消息屏蔽模式： 0 - 不屏蔽1 - 屏蔽本地消息通知2 - 屏蔽消息，不接收消息 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.38 设置群消息推送模式{#put__group_msg_push_mode}

> PUT /group/msg/push_mode

> POST /group/msg/push_mode

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| msg_push_mode | int32 | true |  | 群消息推送类型： 0:接收所有推送;1:不接受推送;2:接收管理员和@消息推送;3:只接收管理员消息推送;4:只接收@消息推送 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.39 获取公开群列表(已废弃){#get__group_public_list}

> GET /group/public_list

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
| data | array[int64] | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.40 二维码邀请入群{#post__group_qrcode_invite}

> POST /group/qrcode/invite

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| qr_info | string | true |  | 二维码信息：可以通过GET /group/qrcode/sign获取 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.41 获取群邀请二维码信息{#get__group_qrcode_sign}

> GET /group/qrcode/sign

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | 群组ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ create_at | int64 | 二维码生成时间（毫秒） |
|⇥ expire_at | int64 | 二维码过期时间（毫秒） |
|⇥ qr_info | string | 二维码信息 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.42 获取群设置{#get__group_settings}

> GET /group/settings

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | 群组ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ apply_approval | int32 | 入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请 |
|⇥ avatar | string | 群头像 |
|⇥ ban_expire_time | int64 | 全员禁言过期时间（秒），禁言期间只允许管理员发消息， 为0或小于当前时间表示不禁言, -1表示永久禁言 |
|⇥ capacity | int64 | 群容量 |
|⇥ count | int64 | 当前人数 |
|⇥ created_at | int64 | 创建时间(毫秒） |
|⇥ description | string | 群描述 |
|⇥ ext | string | 群扩展信息 |
|⇥ group_id | int64 | 群id |
|⇥ history_visible | boolean | 新成员可见历史聊天记录设置： true - 新成员可见历史聊天记录， false - 新成员不可见历史聊天记录 |
|⇥ member_invite | boolean | 是否允许群成员邀请其他人入群: true - 群成员允许邀请其他人入群， false - 群成员不允许邀请其他人入群 |
|⇥ member_modify | boolean | 群成员修改群信息设置： true - 允许群成员修改群信息， false - 不允许群成员修改群信息 |
|⇥ msg_mute_mode | int32 | 群消息屏蔽模式：0 - 表示不屏蔽， 1 - 表示屏蔽本地消息通知， 2 - 表示屏蔽消息，不接收消息 |
|⇥ msg_push_mode | int32 | 群消息推送模式：0 - 接收所有推送， 1 - 不接受推送， 2 - 接收管理员和@消息推送， 3 - 只接收管理员消息推送，4 - 只接收@消息推送 |
|⇥ name | string | 群名称 |
|⇥ owner_id | int64 | 群主id |
|⇥ read_ack | boolean | 是否开启群消息已读功能设置：true - 开启群消息已读功能， false - 不开启群消息已读功能 |
|⇥ status | int32 | 群状态, 0：正常, 1：已解散 |
|⇥ type | int32 | 群类型： 0 - 表示私有群, 2 - 表示聊天室 |
|⇥ updated_at | int64 | 更新时间（毫秒） |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.43 更新群设置--是否允许成员邀请{#put__group_settings_allow_member_invitation}

> PUT /group/settings/allow_member_invitation

> POST /group/settings/allow_member_invitation

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| value | boolean | true |  | 更新内容 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.44 更新群设置--群成员是否可修改群信息{#put__group_settings_allow_member_modify}

> PUT /group/settings/allow_member_modify

> POST /group/settings/allow_member_modify

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| value | boolean | true |  | 更新内容 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.45 全员禁言，只允许管理员发消息{#post__group_settings_ban_all}

> POST /group/settings/ban_all

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| duration | int64 | true |  | 禁言时长，单位为分钟 |
| group_id | int64 | true |  | 群id |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ ban_expire_time | int64 | 全员禁言过期时间（秒），禁言期间只允许管理员发消息， 为0或小于当前时间表示不禁言, -1表示永久禁言 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.46 更新群设置--是否开启群消息已读功能{#put__group_settings_enable_read_ack}

> PUT /group/settings/enable_read_ack

> POST /group/settings/enable_read_ack

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| value | boolean | true |  | 更新内容 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.47 更新群设置--新成员是否可见群历史聊天记录{#put__group_settings_history_visible}

> PUT /group/settings/history_visible

> POST /group/settings/history_visible

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| value | boolean | true |  | 更新内容 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.48 更新群设置--群申请是否需要管理员审批{#put__group_settings_require_admin_approval}

> PUT /group/settings/require_admin_approval

> POST /group/settings/require_admin_approval

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| apply_approval | int32 | true |  | 入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请 |
| group_id | int64 | true |  | 群id |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.49 取消全员禁言{#post__group_settings_unban_all}

> POST /group/settings/unban_all

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.50 转让群{#put__group_transfer}

> PUT /group/transfer

> POST /group/transfer

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| new_owner | int64 | true |  | 新群主的user_id |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ reason | string | 错误信息 |
|⇥ result | string | 操作结果： success - 成功, fail - 失败 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.51 从禁言列表移除用户{#post__group_unban}

> POST /group/unban

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| user_list | array[int64] | true |  | 用户id列表 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ reason | string | 错误信息 |
|⇥ result | string | 操作结果： success - 成功, fail - 失败 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.52 从黑名单移除用户{#delete__group_unblock}

> DELETE /group/unblock

> POST /group/unblock

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | 群id |
| user_list | array[int64] | true |  | 用户id列表 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ reason | string | 错误信息 |
|⇥ result | string | 操作结果： success - 成功, fail - 失败 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 4.53 获取用户的群组列表{#get__group_user_joined}

> GET /group/user_joined

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
| data | array[int64] | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

