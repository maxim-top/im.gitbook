# 3 好友管理接口{#roster}

## 3.1 同意好友申请{#put__roster_accept}

> PUT /roster/accept

> POST /roster/accept

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| user_id | int64 | true | 被同意的用户ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 3.2 申请加好友{#post__roster_apply}

> POST /roster/apply

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
| alias | string | false |  | 备注名称 |
| auth_answer | string | false |  | 问题答案 |
| reason | string | false |  | 申请描述 |
| user_id | int64 | true |  | 被申请用户 ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 3.3 批量添加好友{#post__roster_apply_batch}

> POST /roster/apply/batch

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
|  | array[object] | true | |rosterApplications|
|⇥ alias | string | false |  | 备注名称 |
|⇥ reason | string | false |  | 申请描述 |
|⇥ user_id | int64 | true |  | 被申请用户 ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ fails | array[object] | 失败信息列表 |
|⇥⇥ reason | string | 失败原因 |
|⇥⇥ user_id | int64 | 用户ID |
|⇥ success | array[int64] | 成功的用户ID列表 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 3.4 好友申请列表{#get__roster_apply_list}

> GET /roster/apply/list

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
| cursor | string | false | 游标: 从哪开始拉取 |
| limit | int32 | false | 最多拉取多少条 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| cursor | string | 游标，返回结果中缺失 cursor，表示已经返回最后一页 |
| data | array[object] | 结果数据 |
|⇥ expired_time | int64 | 过期时间戳(毫秒) |
|⇥ reason | string | 申请描述 |
|⇥ status | int32 | 状态:  0 - 等待确认, 1 - 接受, 2 - 拒绝 |
|⇥ user_id | int64 | 发起加好友申请的用户ID |
| message | string | 错误信息，如果成功，该项为null |
| version | int64 | 版本 |
#### 接口描述
> 

## 3.5 添加黑名单{#put__roster_block}

> PUT /roster/block

> POST /roster/block

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| user_id | int64 | true | 用户ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 3.6 黑名单列表{#get__roster_blocked_list}

> GET /roster/blocked_list

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

## 3.7 拒绝好友申请{#put__roster_decline}

> PUT /roster/decline

> POST /roster/decline

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
| reason | string | false |  | 拒绝的原因 |
| user_id | int64 | true |  | 拒绝的用户ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 3.8 删除好友{#delete__roster_delete}

> DELETE /roster/delete

> POST /roster/delete

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| user_id | int64 | true | 用户ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 3.9 更新好友扩展信息{#put__roster_ext}

> PUT /roster/ext

> POST /roster/ext

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
| alias | string | false |  | 备注名称 |
| ext | string | false |  | 扩展信息 |
| mute_notification | boolean | false |  | 是否消息免打扰: true - 消息免打扰, false - 不消息免打扰 |
| user_id | int64 | true |  | 好友用户ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 3.10 用ID搜索用户{#get__roster_id}

> GET /roster/id

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| user_id | int64 | true | 用户ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ alias | string | 备注名称 |
|⇥ auth_mode | int32 | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |
|⇥ auth_question | string | 验证问题 |
|⇥ avatar | string | 头像 |
|⇥ description | string | 描述信息 |
|⇥ ext | string | 扩展信息 |
|⇥ mute_notification | boolean | 是否消息免打扰: true - 消息免打扰, false - 不消息免打扰 |
|⇥ nick_name | string | 昵称或名称 |
|⇥ public_info | string | 公开信息，好友和陌生人可见 |
|⇥ relation | int32 | 关系: 0 - 好友, 1 - 被删除的好友, 2 - 陌生人, 3 - 黑名单 |
|⇥ user_id | int64 | 好友用户ID |
|⇥ username | string | 用户名 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 3.11 好友列表{#get__roster_list}

> GET /roster/list

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
| cursor | string | false | 游标：从哪开始取 |
| limit | int32 | false | 最多取多少条 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| cursor | string | 游标，返回结果中缺失 cursor，表示已经返回最后一页 |
| data | array[int64] | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
| version | int64 | 版本 |
#### 接口描述
> 

## 3.12 好友详情列表{#post__roster_list}

> POST /roster/list

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
| list | array[int64] | true |  | 好友ID列表 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ alias | string | 备注名称 |
|⇥ auth_mode | int32 | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |
|⇥ auth_question | string | 验证问题 |
|⇥ avatar | string | 头像 |
|⇥ description | string | 描述信息 |
|⇥ ext | string | 扩展信息 |
|⇥ mute_notification | boolean | 是否消息免打扰: true - 消息免打扰, false - 不消息免打扰 |
|⇥ nick_name | string | 昵称或名称 |
|⇥ public_info | string | 公开信息，好友和陌生人可见 |
|⇥ relation | int32 | 关系: 0 - 好友, 1 - 被删除的好友, 2 - 陌生人, 3 - 黑名单 |
|⇥ user_id | int64 | 好友用户ID |
|⇥ username | string | 用户名 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 3.13 是否允许发消息{#get__roster_may_message}

> GET /roster/may_message

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| roster_id | int64 | true | 好友ID |
| user_id | int64 | true | 用户ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 3.14 用手机号搜索用户{#get__roster_mobile}

> GET /roster/mobile

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
| mobile | string | true | 手机号 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ alias | string | 备注名称 |
|⇥ auth_mode | int32 | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |
|⇥ auth_question | string | 验证问题 |
|⇥ avatar | string | 头像 |
|⇥ description | string | 描述信息 |
|⇥ ext | string | 扩展信息 |
|⇥ mute_notification | boolean | 是否消息免打扰: true - 消息免打扰, false - 不消息免打扰 |
|⇥ nick_name | string | 昵称或名称 |
|⇥ public_info | string | 公开信息，好友和陌生人可见 |
|⇥ relation | int32 | 关系: 0 - 好友, 1 - 被删除的好友, 2 - 陌生人, 3 - 黑名单 |
|⇥ user_id | int64 | 好友用户ID |
|⇥ username | string | 用户名 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 3.15 用用户名搜索用户{#get__roster_name}

> GET /roster/name

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
| username | string | true | 用户名 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ alias | string | 备注名称 |
|⇥ auth_mode | int32 | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |
|⇥ auth_question | string | 验证问题 |
|⇥ avatar | string | 头像 |
|⇥ description | string | 描述信息 |
|⇥ ext | string | 扩展信息 |
|⇥ mute_notification | boolean | 是否消息免打扰: true - 消息免打扰, false - 不消息免打扰 |
|⇥ nick_name | string | 昵称或名称 |
|⇥ public_info | string | 公开信息，好友和陌生人可见 |
|⇥ relation | int32 | 关系: 0 - 好友, 1 - 被删除的好友, 2 - 陌生人, 3 - 黑名单 |
|⇥ user_id | int64 | 好友用户ID |
|⇥ username | string | 用户名 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 3.16 从黑名单移除{#delete__roster_unblock}

> DELETE /roster/unblock

> POST /roster/unblock

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| user_id | int64 | true | 用户ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

