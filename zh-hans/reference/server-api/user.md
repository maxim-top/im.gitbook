# 1 用户操作{#user}

## 1.1 设置加好友验证方式{#put__user_authmode}

> PUT /user/authmode

> POST /user/authmode

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
| value | int32 | true | value |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.2 设置头像{#put__user_avatar}

> PUT /user/avatar

> POST /user/avatar

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
| avatar | string | true |  | 头像 url |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.3 批量设置头像{#put__user_avatar_batch}

> PUT /user/avatar/batch

> POST /user/avatar/batch

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
| list | array[object] | false |  |  |
|⇥ avatar | string | true |  | 头像 url |
|⇥ user_id | int64 | false |  | 用户ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ reason | string | 失败原因 |
|⇥ success | boolean | 是否成功 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.4 修改密码{#post__user_change_password}

> POST /user/change_password

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
| new_password | string | false |  | new_password 新密码 |
| old_password | string | false |  | old_password 旧密码 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.5 设备列表{#get__user_device_list}

> GET /user/device/list

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
| cursor | string | 游标，返回结果中缺失 cursor，表示已经返回最后一页 |
| data | array[object] | 结果数据 |
|⇥ device_sn | int32 |  |
|⇥ platform | int32 | 设备平台, 1:ios, 2:android, 3:windows, 4:mac, 5:linux, 6:web |
|⇥ user_agent | string |  |
|⇥ user_id | int64 | 用户 ID |
| message | string | 错误信息，如果成功，该项为null |
| version | int64 | 版本 |
#### 接口描述
> 

## 1.6 删除device{#delete__user_device_remove}

> DELETE /user/device/remove

> POST /user/device/remove

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
| device_sn | int32 | true | device_sn |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.7 封禁用户{#put__user_disable}

> PUT /user/disable

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
| list | array[int64] | false |  |  |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.8 设置是否自动下载缩略图和文件{#put__user_download}

> PUT /user/download

> POST /user/download

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
| value | boolean | true | value |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.9 解禁用户{#put__user_enable}

> PUT /user/enable

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
| list | array[int64] | false |  |  |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.10 踢指定设备下线{#put__user_kick}

> PUT /user/kick

> POST /user/kick

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
| device_sn | int32 | false | 不传device_sn表示踢所有设备 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.11 列出APP下所有用户{#get__user_list}

> GET /user/list

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
| page_num | int32 | false | page_num |
| page_size | int32 | false | page_size |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ status | int32 | 0-激活，1-禁用 |
|⇥ user_id | int64 |  |
|⇥ username | string |  |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.12 设置手机号码{#put__user_mobile}

> PUT /user/mobile

> POST /user/mobile

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
| mobile | string | true | mobile |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.13 设置昵称{#put__user_nickname}

> PUT /user/nickname

> POST /user/nickname

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
| nick_name | string | true | nick_name |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.14 查询用户在线状态{#get__user_online_status}

> GET /user/online_status

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
|⇥ online | boolean | 是否在线： true - 在线 ，false - 离线 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.15 设置私有扩展信息{#put__user_private}

> PUT /user/private

> POST /user/private

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
|  | string | true |  |  |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.16 获取用户信息{#get__user_profile}

> GET /user/profile

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
|⇥ avatar | string | 头像 url |
|⇥ description | string | 描述信息 |
|⇥ email | string | 邮箱 |
|⇥ mobile | string | 手机号码 |
|⇥ nick_name | string | 昵称 |
|⇥ private_info | string | 私有信息，仅自己可见 |
|⇥ public_info | string | 公开信息，好友和陌生人可见 |
|⇥ user_id | int64 | 用户ID |
|⇥ username | string | 用户名 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.17 更新用户信息{#put__user_profile}

> PUT /user/profile

> POST /user/profile

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
| description | string | false |  | 描述信息 |
| nick_name | string | false |  | 昵称 |
| private_info | string | false |  | 私有信息，仅自己可见 |
| public_info | string | false |  | 公开信息，好友和陌生人可见 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.18 批量更新用户信息{#put__user_profile_batch}

> PUT /user/profile/batch

> POST /user/profile/batch

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
| list | array[object] | false |  |  |
|⇥ description | string | false |  | 描述信息 |
|⇥ nick_name | string | false |  | 昵称 |
|⇥ private_info | string | false |  | 私有信息，仅自己可见 |
|⇥ public_info | string | false |  | 公开信息，好友和陌生人可见 |
|⇥ user_id | int64 | false |  | 用户ID |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ reason | string | 失败原因 |
|⇥ success | boolean | 是否成功 |
|⇥ user_id | int64 | 用户ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.19 设置公开扩展信息{#put__user_public}

> PUT /user/public

> POST /user/public

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
|  | string | true |  |  |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.20 设置是否关闭推送{#put__user_push}

> PUT /user/push

> POST /user/push

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
| value | boolean | true | value |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.21 绑定别名{#post__user_push_alias}

> POST /user/push/alias

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
| alias | string | true |  | 别名 |
| push_token | string | false |  | 推送token |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.22 设置badge{#post__user_push_badge}

> POST /user/push/badge

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
| badge | int32 | true |  | badge |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.23 设置是否关闭推送详情{#put__user_push_detail}

> PUT /user/push/detail

> POST /user/push/detail

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
| value | boolean | true | value |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.24 设置推送免打扰时间{#put__user_push_limit}

> PUT /user/push/limit

> POST /user/push/limit

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
| no_push_end_hour | int32 | true | no_push_end_hour |
| no_push_start_hour | int32 | true | no_push_start_hour |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.25 设置推送昵称{#put__user_push_nickname}

> PUT /user/push/nickname

> POST /user/push/nickname

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
| value | string | true | value |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.26 解绑标签{#delete__user_push_tag}

> DELETE /user/push/tag

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
| tags | array[string] | false |  |  |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.27 获取标签{#get__user_push_tag}

> GET /user/push/tag

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
| data | array[string] | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.28 绑定标签{#post__user_push_tag}

> POST /user/push/tag

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
| tags | array[string] | false |  |  |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.29 删除所有标签{#delete__user_push_tag_all}

> DELETE /user/push/tag/all

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
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.30 批量注册用户{#post__user_register_batch}

> POST /user/register/batch

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
| list | array[object] | false |  |  |
|⇥ password | string | true |  |  |
|⇥ username | string | true |  |  |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ reason | string | 失败原因 |
|⇥ success | boolean | 是否成功 |
|⇥ user_id | int64 | 用户ID |
|⇥ username | string | 用户名 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.31 注册推送用户{#post__user_register_push}

> POST /user/register/push

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
| alias | string | false |  | 别名 |
| device_guid | string | false |  | 设备ID |
| password | string | true |  |  |
| push_token | string | false |  | 推送token |
| sign | string | false |  | 签名 |
| username | string | true |  |  |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ auth_answer | string | 验证问题答案 |
|⇥ auth_mode | int32 | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |
|⇥ auth_question | string | 验证问题 |
|⇥ auto_download | boolean | 是否自动下载 |
|⇥ group_confirm | boolean | 邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请 |
|⇥ id | int64 |  |
|⇥ no_push | boolean | 是否关闭推送消息 |
|⇥ no_push_detail | boolean | 是否推送详情 |
|⇥ no_push_end_hour | int32 | 推送免打扰结束时间 |
|⇥ no_push_start_hour | int32 | 推送免打扰开始时间 |
|⇥ no_sounds | boolean | 收到消息时是否静音 |
|⇥ push_nick_name | string | 推送昵称 |
|⇥ push_token | string | 推送token |
|⇥ silence_end_time | int32 | 推送不提醒结束时间 |
|⇥ silence_start_time | int32 | 推送不提醒开始时间 |
|⇥ user_id | int64 | 用户ID |
|⇥ vibratory | boolean | 收到消息时否振动 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.32 注册用户{#post__user_register_v2}

> POST /user/register/v2

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
| password | string | true |  |  |
| username | string | true |  |  |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ auth_answer | string | 验证问题答案 |
|⇥ auth_mode | int32 | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |
|⇥ auth_question | string | 验证问题 |
|⇥ auto_download | boolean | 是否自动下载 |
|⇥ group_confirm | boolean | 邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请 |
|⇥ id | int64 |  |
|⇥ no_push | boolean | 是否关闭推送消息 |
|⇥ no_push_detail | boolean | 是否推送详情 |
|⇥ no_push_end_hour | int32 | 推送免打扰结束时间 |
|⇥ no_push_start_hour | int32 | 推送免打扰开始时间 |
|⇥ no_sounds | boolean | 收到消息时是否静音 |
|⇥ push_nick_name | string | 推送昵称 |
|⇥ push_token | string | 推送token |
|⇥ silence_end_time | int32 | 推送不提醒结束时间 |
|⇥ silence_start_time | int32 | 推送不提醒开始时间 |
|⇥ user_id | int64 | 用户ID |
|⇥ vibratory | boolean | 收到消息时否振动 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.33 获取用户设置{#get__user_settings}

> GET /user/settings

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
|⇥ auth_answer | string | 验证问题答案 |
|⇥ auth_mode | int32 | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |
|⇥ auth_question | string | 验证问题 |
|⇥ auto_download | boolean | 是否自动下载 |
|⇥ group_confirm | boolean | 邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请 |
|⇥ id | int64 |  |
|⇥ no_push | boolean | 是否关闭推送消息 |
|⇥ no_push_detail | boolean | 是否推送详情 |
|⇥ no_push_end_hour | int32 | 推送免打扰结束时间 |
|⇥ no_push_start_hour | int32 | 推送免打扰开始时间 |
|⇥ no_sounds | boolean | 收到消息时是否静音 |
|⇥ push_nick_name | string | 推送昵称 |
|⇥ push_token | string | 推送token |
|⇥ silence_end_time | int32 | 推送不提醒结束时间 |
|⇥ silence_start_time | int32 | 推送不提醒开始时间 |
|⇥ user_id | int64 | 用户ID |
|⇥ vibratory | boolean | 收到消息时否振动 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.34 修改用户设置{#put__user_settings}

> PUT /user/settings

> POST /user/settings

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
| auth_answer | string | false |  | 验证问题答案 |
| auth_mode | int32 | false |  | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |
| auth_question | string | false |  | 验证问题 |
| auto_download | boolean | false |  | 是否自动下载 |
| group_confirm | boolean | false |  | 邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请 |
| id | int64 | false |  |  |
| no_push | boolean | false |  | 是否关闭推送消息 |
| no_push_detail | boolean | false |  | 是否推送详情 |
| no_push_end_hour | int32 | false |  | 推送免打扰结束时间 |
| no_push_start_hour | int32 | false |  | 推送免打扰开始时间 |
| no_sounds | boolean | false |  | 收到消息时是否静音 |
| push_nick_name | string | false |  | 推送昵称 |
| push_token | string | false |  | 推送token |
| silence_end_time | int32 | false |  | 推送不提醒结束时间 |
| silence_start_time | int32 | false |  | 推送不提醒开始时间 |
| user_id | int64 | true |  | 用户ID |
| vibratory | boolean | false |  | 收到消息时否振动 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.35 设置新消息是否关闭声音提醒{#put__user_sounds}

> PUT /user/sounds

> POST /user/sounds

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
| value | boolean | true | value |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.36 绑定token{#put__user_token_bind}

> PUT /user/token/bind

> POST /user/token/bind

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
| device_sn | int32 | true |  | 设备SN |
| device_token | string | true |  | device token |
| notifier_name | string | true |  | 证书名称 |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.37 解绑token{#delete__user_token_unbind}

> DELETE /user/token/unbind

> POST /user/token/unbind

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
| deviceSn | int32 | true | deviceSn |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.38 修改用户名{#put__user_username}

> PUT /user/username

> POST /user/username

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
| username | string | true | username |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 1.39 设置新消息是否振动{#put__user_vibratory}

> PUT /user/vibratory

> POST /user/vibratory

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
| value | boolean | true | value |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | boolean | 结果数据 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

