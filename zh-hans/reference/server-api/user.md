# 1 用户操作{#user}

## 1.1 设置加好友验证方式{#put\_\_user\_authmode}

> PUT /user/authmode

> POST /user/authmode

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称  | 数据类型  | 必填   | 描述                                                                          |
| ----- | ----- | ---- | --------------------------------------------------------------------------- |
| value | int32 | true | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.2 设置头像{#put\_\_user\_avatar}

> PUT /user/avatar

> POST /user/avatar

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称   | 数据类型   | 必填   | 默认值 | 描述     |
| ------ | ------ | ---- | --- | ------ |
| avatar | string | true |     | 头像 url |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.3 批量设置头像{#put\_\_user\_avatar\_batch}

> PUT /user/avatar/batch

> POST /user/avatar/batch

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称       | 数据类型           | 必填    | 默认值 | 描述     |
| ---------- | -------------- | ----- | --- | ------ |
| list       | array\[object] | false |     |        |
| ⇥ avatar   | string         | true  |     | 头像 url |
| ⇥ user\_id | int64          | true  |     | 用户ID   |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称       | 类型             | 描述                |
| ---------- | -------------- | ----------------- |
| code       | int32          | 返回码，200是成功        |
| data       | array\[object] | 结果数据              |
| ⇥ reason   | string         | 失败原因              |
| ⇥ success  | boolean        | 是否成功              |
| ⇥ user\_id | int64          | 用户ID              |
| message    | string         | 错误信息，如果成功，该项为null |
| #### 接口描述  |                |                   |

>

## 1.4 修改密码{#post\_\_user\_change\_password}

> POST /user/change\_password

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称          | 数据类型   | 必填   | 默认值 | 描述  |
| ------------- | ------ | ---- | --- | --- |
| new\_password | string | true |     | 新密码 |
| old\_password | string | true |     | 旧密码 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.5 管理员修改密码{#post\_\_user\_change\_password\_admin}

> POST /user/change\_password\_admin

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称     | 数据类型   | 必填   | 默认值 | 描述 |
| -------- | ------ | ---- | --- | -- |
| password | string | true |     | 密码 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.6 删除用户{#delete\_\_user\_delete}

> DELETE /user/delete

> POST /user/delete

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称     | 数据类型   | 必填    | 默认值 | 描述                                       |
| -------- | ------ | ----- | --- | ---------------------------------------- |
| password | string | false |     | 用户密码：如果是用户TOKEN,需要设置此字段；如果是管理员TOKEN则不需设置 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.7 设备列表{#get\_\_user\_device\_list}

> GET /user/device/list

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称          | 类型             | 描述                                                       |
| ------------- | -------------- | -------------------------------------------------------- |
| code          | int32          | 返回码，200是成功                                               |
| cursor        | string         | 游标，返回结果中缺失 cursor，表示已经返回最后一页                             |
| data          | array\[object] | 结果数据                                                     |
| ⇥ device\_sn  | int32          | 设备序号                                                     |
| ⇥ platform    | int32          | 设备平台, 1:ios, 2:android, 3:windows, 4:mac, 5:linux, 6:web |
| ⇥ user\_agent | string         | 设备信息                                                     |
| ⇥ user\_id    | int64          | 用户 ID                                                    |
| message       | string         | 错误信息，如果成功，该项为null                                        |
| version       | int64          | 版本                                                       |
| #### 接口描述     |                |                                                          |

>

## 1.8 删除device{#delete\_\_user\_device\_remove}

> DELETE /user/device/remove

> POST /user/device/remove

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称       | 数据类型  | 必填   | 描述   |
| ---------- | ----- | ---- | ---- |
| device\_sn | int32 | true | 设备序号 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.9 封禁用户{#put\_\_user\_disable}

> PUT /user/disable

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称 | 数据类型          | 必填   | 默认值 | 描述     |
| ---- | ------------- | ---- | --- | ------ |
| list | array\[int64] | true |     | 用户ID列表 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.10 设置是否自动下载缩略图和文件{#put\_\_user\_download}

> PUT /user/download

> POST /user/download

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称  | 数据类型    | 必填   | 描述                                |
| ----- | ------- | ---- | --------------------------------- |
| value | boolean | true | 是否自动下载缩略图和文件： true - 是， false - 否 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.11 解禁用户{#put\_\_user\_enable}

> PUT /user/enable

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称 | 数据类型          | 必填   | 默认值 | 描述     |
| ---- | ------------- | ---- | --- | ------ |
| list | array\[int64] | true |     | 用户ID列表 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.12 踢指定设备下线{#put\_\_user\_kick}

> PUT /user/kick

> POST /user/kick

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称       | 数据类型  | 必填    | 描述              |
| ---------- | ----- | ----- | --------------- |
| device\_sn | int32 | false | 设备序号：不设置表示踢所有设备 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.13 列出APP下所有用户{#get\_\_user\_list}

> GET /user/list

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称       | 数据类型  | 必填    | 描述            |
| ---------- | ----- | ----- | ------------- |
| page\_num  | int32 | false | 页数：必须大于0，默认为1 |
| page\_size | int32 | false | 每页大小：默认每页50条  |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称       | 类型             | 描述                |
| ---------- | -------------- | ----------------- |
| code       | int32          | 返回码，200是成功        |
| data       | array\[object] | 结果数据              |
| ⇥ status   | int32          | 0-正常，1-封禁         |
| ⇥ user\_id | int64          | 用户ID              |
| ⇥ username | string         | 用户名               |
| message    | string         | 错误信息，如果成功，该项为null |
| #### 接口描述  |                |                   |

>

## 1.14 设置手机号码{#put\_\_user\_mobile}

> PUT /user/mobile

> POST /user/mobile

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称   | 数据类型   | 必填   | 描述   |
| ------ | ------ | ---- | ---- |
| mobile | string | true | 手机号码 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.15 设置昵称{#put\_\_user\_nickname}

> PUT /user/nickname

> POST /user/nickname

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称       | 数据类型   | 必填   | 描述 |
| ---------- | ------ | ---- | -- |
| nick\_name | string | true | 昵称 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.16 查询用户在线状态{#get\_\_user\_online\_status}

> GET /user/online\_status

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                          |
| --------- | ------- | --------------------------- |
| code      | int32   | 返回码，200是成功                  |
| data      | object  | 结果数据                        |
| ⇥ online  | boolean | 是否在线： true - 在线 ，false - 离线 |
| message   | string  | 错误信息，如果成功，该项为null           |
| #### 接口描述 |         |                             |

>

## 1.17 设置私有扩展信息{#put\_\_user\_private}

> PUT /user/private

> POST /user/private

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称 | 数据类型   | 必填   | 默认值 | 描述     |
| ---- | ------ | ---- | --- | ------ |
|      | string | true |     | 私有扩展信息 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.18 获取用户信息{#get\_\_user\_profile}

> GET /user/profile

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称            | 类型     | 描述                |
| --------------- | ------ | ----------------- |
| code            | int32  | 返回码，200是成功        |
| data            | object | 结果数据              |
| ⇥ avatar        | string | 头像 url            |
| ⇥ description   | string | 描述信息              |
| ⇥ email         | string | 邮箱                |
| ⇥ mobile        | string | 手机号码              |
| ⇥ nick\_name    | string | 昵称                |
| ⇥ private\_info | string | 私有信息，仅自己可见        |
| ⇥ public\_info  | string | 公开信息，好友和陌生人可见     |
| ⇥ user\_id      | int64  | 用户ID              |
| ⇥ username      | string | 用户名               |
| message         | string | 错误信息，如果成功，该项为null |
| #### 接口描述       |        |                   |

>

## 1.19 更新用户信息{#put\_\_user\_profile}

> PUT /user/profile

> POST /user/profile

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称          | 数据类型   | 必填    | 默认值 | 描述            |
| ------------- | ------ | ----- | --- | ------------- |
| description   | string | false |     | 描述信息          |
| nick\_name    | string | false |     | 昵称            |
| private\_info | string | false |     | 私有信息，仅自己可见    |
| public\_info  | string | false |     | 公开信息，好友和陌生人可见 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.20 批量更新用户信息{#put\_\_user\_profile\_batch}

> PUT /user/profile/batch

> POST /user/profile/batch

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称            | 数据类型           | 必填    | 默认值 | 描述            |
| --------------- | -------------- | ----- | --- | ------------- |
| list            | array\[object] | false |     |               |
| ⇥ description   | string         | false |     | 描述信息          |
| ⇥ nick\_name    | string         | false |     | 昵称            |
| ⇥ private\_info | string         | false |     | 私有信息，仅自己可见    |
| ⇥ public\_info  | string         | false |     | 公开信息，好友和陌生人可见 |
| ⇥ user\_id      | int64          | false |     | 用户ID          |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称       | 类型             | 描述                |
| ---------- | -------------- | ----------------- |
| code       | int32          | 返回码，200是成功        |
| data       | array\[object] | 结果数据              |
| ⇥ reason   | string         | 失败原因              |
| ⇥ success  | boolean        | 是否成功              |
| ⇥ user\_id | int64          | 用户ID              |
| message    | string         | 错误信息，如果成功，该项为null |
| #### 接口描述  |                |                   |

>

## 1.21 设置公开扩展信息{#put\_\_user\_public}

> PUT /user/public

> POST /user/public

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称 | 数据类型   | 必填   | 默认值 | 描述     |
| ---- | ------ | ---- | --- | ------ |
|      | string | true |     | 公开扩展信息 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.22 设置是否关闭推送{#put\_\_user\_push}

> PUT /user/push

> POST /user/push

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称  | 数据类型    | 必填   | 描述                                 |
| ----- | ------- | ---- | ---------------------------------- |
| value | boolean | true | 是否关闭推送： true - 关闭推送， false - 不关闭推送 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.23 绑定别名{#post\_\_user\_push\_alias}

> POST /user/push/alias

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称        | 数据类型   | 必填    | 默认值 | 描述      |
| ----------- | ------ | ----- | --- | ------- |
| alias       | string | true  |     | 别名      |
| push\_token | string | false |     | 推送token |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.24 设置badge{#post\_\_user\_push\_badge}

> POST /user/push/badge

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称  | 数据类型  | 必填   | 默认值 | 描述    |
| ----- | ----- | ---- | --- | ----- |
| badge | int32 | true |     | badge |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.25 设置是否关闭推送详情{#put\_\_user\_push\_detail}

> PUT /user/push/detail

> POST /user/push/detail

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称  | 数据类型    | 必填   | 描述                                       |
| ----- | ------- | ---- | ---------------------------------------- |
| value | boolean | true | 是否关闭推送详情: true - 关闭推送详情, false - 不关闭推送详情 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.26 设置推送免打扰时间{#put\_\_user\_push\_limit}

> PUT /user/push/limit

> POST /user/push/limit

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称                  | 数据类型  | 必填   | 描述               |
| --------------------- | ----- | ---- | ---------------- |
| no\_push\_end\_hour   | int32 | true | 推送免打扰结束的小时（0-23） |
| no\_push\_start\_hour | int32 | true | 推送免打扰开始的小时（0-23） |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.27 设置推送昵称{#put\_\_user\_push\_nickname}

> PUT /user/push/nickname

> POST /user/push/nickname

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称  | 数据类型   | 必填   | 描述   |
| ----- | ------ | ---- | ---- |
| value | string | true | 推送昵称 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.28 获取标签{#get\_\_user\_push\_tag}

> GET /user/push/tag

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型             | 描述                |
| --------- | -------------- | ----------------- |
| code      | int32          | 返回码，200是成功        |
| data      | array\[string] | 结果数据              |
| message   | string         | 错误信息，如果成功，该项为null |
| #### 接口描述 |                |                   |

>

## 1.29 绑定标签{#post\_\_user\_push\_tag}

> POST /user/push/tag

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称 | 数据类型           | 必填   | 默认值 | 描述   |
| ---- | -------------- | ---- | --- | ---- |
| tags | array\[string] | true |     | 标签列表 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.30 解绑标签{#delete\_\_user\_push\_tag}

> DELETE /user/push/tag

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称 | 数据类型           | 必填   | 默认值 | 描述   |
| ---- | -------------- | ---- | --- | ---- |
| tags | array\[string] | true |     | 标签列表 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.31 删除所有标签{#delete\_\_user\_push\_tag\_all}

> DELETE /user/push/tag/all

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.32 批量注册用户{#post\_\_user\_register\_batch}

> POST /user/register/batch

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称       | 数据类型           | 必填    | 默认值 | 描述  |
| ---------- | -------------- | ----- | --- | --- |
| list       | array\[object] | false |     |     |
| ⇥ password | string         | true  |     | 密码  |
| ⇥ username | string         | true  |     | 用户名 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称       | 类型             | 描述                |
| ---------- | -------------- | ----------------- |
| code       | int32          | 返回码，200是成功        |
| data       | array\[object] | 结果数据              |
| ⇥ reason   | string         | 失败原因              |
| ⇥ success  | boolean        | 是否成功              |
| ⇥ user\_id | int64          | 用户ID              |
| ⇥ username | string         | 用户名               |
| message    | string         | 错误信息，如果成功，该项为null |
| #### 接口描述  |                |                   |

>

## 1.33 注册推送用户{#post\_\_user\_register\_push}

> POST /user/register/push

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称         | 数据类型   | 必填    | 默认值 | 描述      |
| ------------ | ------ | ----- | --- | ------- |
| alias        | string | false |     | 别名      |
| device\_guid | string | false |     | 设备ID    |
| password     | string | true  |     | 密码      |
| push\_token  | string | false |     | 推送token |
| sign         | string | false |     | 签名      |
| username     | string | true  |     | 用户名     |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称                    | 类型      | 描述                                                                          |
| ----------------------- | ------- | --------------------------------------------------------------------------- |
| code                    | int32   | 返回码，200是成功                                                                  |
| data                    | object  | 结果数据                                                                        |
| ⇥ auth\_answer          | string  | 验证问题答案                                                                      |
| ⇥ auth\_mode            | int32   | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |
| ⇥ auth\_question        | string  | 验证问题                                                                        |
| ⇥ auto\_download        | boolean | 是否自动下载: true - 自动下载, false - 不自动下载                                          |
| ⇥ group\_confirm        | boolean | 邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请                            |
| ⇥ id                    | int64   |                                                                             |
| ⇥ no\_push              | boolean | 是否关闭推送消息: true - 关闭推送消息, false - 不关闭推送消息                                    |
| ⇥ no\_push\_detail      | boolean | 是否推送详情: true - 推送详情, false - 不推送详情                                          |
| ⇥ no\_push\_end\_hour   | int32   | 推送免打扰结束时间（小时 0-23）                                                          |
| ⇥ no\_push\_start\_hour | int32   | 推送免打扰开始时间（小时 0-23）                                                          |
| ⇥ no\_sounds            | boolean | 收到消息时是否静音: true - 静音, false - 不静音                                           |
| ⇥ push\_nick\_name      | string  | 推送昵称                                                                        |
| ⇥ push\_token           | string  | 推送token                                                                     |
| ⇥ silence\_end\_time    | int32   | 推送不提醒结束时间（小时 0-23）                                                          |
| ⇥ silence\_start\_time  | int32   | 推送不提醒开始时间（小时 0-23）                                                          |
| ⇥ user\_id              | int64   | 用户ID                                                                        |
| ⇥ vibratory             | boolean | 收到消息时否振动: true - 振动， false - 不振动                                            |
| message                 | string  | 错误信息，如果成功，该项为null                                                           |
| #### 接口描述               |         |                                                                             |

>

## 1.34 注册用户{#post\_\_user\_register\_v2}

> POST /user/register/v2

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称     | 数据类型   | 必填   | 默认值 | 描述  |
| -------- | ------ | ---- | --- | --- |
| password | string | true |     | 密码  |
| username | string | true |     | 用户名 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称                    | 类型      | 描述                                                                          |
| ----------------------- | ------- | --------------------------------------------------------------------------- |
| code                    | int32   | 返回码，200是成功                                                                  |
| data                    | object  | 结果数据                                                                        |
| ⇥ auth\_answer          | string  | 验证问题答案                                                                      |
| ⇥ auth\_mode            | int32   | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |
| ⇥ auth\_question        | string  | 验证问题                                                                        |
| ⇥ auto\_download        | boolean | 是否自动下载: true - 自动下载, false - 不自动下载                                          |
| ⇥ group\_confirm        | boolean | 邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请                            |
| ⇥ id                    | int64   |                                                                             |
| ⇥ no\_push              | boolean | 是否关闭推送消息: true - 关闭推送消息, false - 不关闭推送消息                                    |
| ⇥ no\_push\_detail      | boolean | 是否推送详情: true - 推送详情, false - 不推送详情                                          |
| ⇥ no\_push\_end\_hour   | int32   | 推送免打扰结束时间（小时 0-23）                                                          |
| ⇥ no\_push\_start\_hour | int32   | 推送免打扰开始时间（小时 0-23）                                                          |
| ⇥ no\_sounds            | boolean | 收到消息时是否静音: true - 静音, false - 不静音                                           |
| ⇥ push\_nick\_name      | string  | 推送昵称                                                                        |
| ⇥ push\_token           | string  | 推送token                                                                     |
| ⇥ silence\_end\_time    | int32   | 推送不提醒结束时间（小时 0-23）                                                          |
| ⇥ silence\_start\_time  | int32   | 推送不提醒开始时间（小时 0-23）                                                          |
| ⇥ user\_id              | int64   | 用户ID                                                                        |
| ⇥ vibratory             | boolean | 收到消息时否振动: true - 振动， false - 不振动                                            |
| message                 | string  | 错误信息，如果成功，该项为null                                                           |
| #### 接口描述               |         |                                                                             |

>

## 1.35 获取用户设置{#get\_\_user\_settings}

> GET /user/settings

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称                    | 类型      | 描述                                                                          |
| ----------------------- | ------- | --------------------------------------------------------------------------- |
| code                    | int32   | 返回码，200是成功                                                                  |
| data                    | object  | 结果数据                                                                        |
| ⇥ auth\_answer          | string  | 验证问题答案                                                                      |
| ⇥ auth\_mode            | int32   | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |
| ⇥ auth\_question        | string  | 验证问题                                                                        |
| ⇥ auto\_download        | boolean | 是否自动下载: true - 自动下载, false - 不自动下载                                          |
| ⇥ group\_confirm        | boolean | 邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请                            |
| ⇥ id                    | int64   |                                                                             |
| ⇥ no\_push              | boolean | 是否关闭推送消息: true - 关闭推送消息, false - 不关闭推送消息                                    |
| ⇥ no\_push\_detail      | boolean | 是否推送详情: true - 推送详情, false - 不推送详情                                          |
| ⇥ no\_push\_end\_hour   | int32   | 推送免打扰结束时间（小时 0-23）                                                          |
| ⇥ no\_push\_start\_hour | int32   | 推送免打扰开始时间（小时 0-23）                                                          |
| ⇥ no\_sounds            | boolean | 收到消息时是否静音: true - 静音, false - 不静音                                           |
| ⇥ push\_nick\_name      | string  | 推送昵称                                                                        |
| ⇥ push\_token           | string  | 推送token                                                                     |
| ⇥ silence\_end\_time    | int32   | 推送不提醒结束时间（小时 0-23）                                                          |
| ⇥ silence\_start\_time  | int32   | 推送不提醒开始时间（小时 0-23）                                                          |
| ⇥ user\_id              | int64   | 用户ID                                                                        |
| ⇥ vibratory             | boolean | 收到消息时否振动: true - 振动， false - 不振动                                            |
| message                 | string  | 错误信息，如果成功，该项为null                                                           |
| #### 接口描述               |         |                                                                             |

>

## 1.36 修改用户设置{#put\_\_user\_settings}

> PUT /user/settings

> POST /user/settings

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称                  | 数据类型    | 必填    | 默认值 | 描述                                                                          |
| --------------------- | ------- | ----- | --- | --------------------------------------------------------------------------- |
| auth\_answer          | string  | false |     | 验证问题答案                                                                      |
| auth\_mode            | int32   | false |     | 验证方式, 0 - 无需验证，任何人可以加为好友, 1 - 需要同意方可加为好友, 2 - 需要回答问题正确方可加为好友, 3 - 拒绝所有加好友申请 |
| auth\_question        | string  | false |     | 验证问题                                                                        |
| auto\_download        | boolean | false |     | 是否自动下载: true - 自动下载, false - 不自动下载                                          |
| group\_confirm        | boolean | false |     | 邀请入群时是否需要用户确认: true - 需要用户同意才可加入， false - 自动同意邀请                            |
| id                    | int64   | false |     |                                                                             |
| no\_push              | boolean | false |     | 是否关闭推送消息: true - 关闭推送消息, false - 不关闭推送消息                                    |
| no\_push\_detail      | boolean | false |     | 是否推送详情: true - 推送详情, false - 不推送详情                                          |
| no\_push\_end\_hour   | int32   | false |     | 推送免打扰结束时间（小时 0-23）                                                          |
| no\_push\_start\_hour | int32   | false |     | 推送免打扰开始时间（小时 0-23）                                                          |
| no\_sounds            | boolean | false |     | 收到消息时是否静音: true - 静音, false - 不静音                                           |
| push\_nick\_name      | string  | false |     | 推送昵称                                                                        |
| push\_token           | string  | false |     | 推送token                                                                     |
| silence\_end\_time    | int32   | false |     | 推送不提醒结束时间（小时 0-23）                                                          |
| silence\_start\_time  | int32   | false |     | 推送不提醒开始时间（小时 0-23）                                                          |
| user\_id              | int64   | true  |     | 用户ID                                                                        |
| vibratory             | boolean | false |     | 收到消息时否振动: true - 振动， false - 不振动                                            |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.37 设置新消息是否关闭声音提醒{#put\_\_user\_sounds}

> PUT /user/sounds

> POST /user/sounds

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称  | 数据类型    | 必填   | 描述                                       |
| ----- | ------- | ---- | ---------------------------------------- |
| value | boolean | true | 是否关闭声音提醒: true - 关闭声音提醒, false - 不关闭声音提醒 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.38 绑定token{#put\_\_user\_token\_bind}

> PUT /user/token/bind

> POST /user/token/bind

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求体(Request Body)

| 参数名称           | 数据类型   | 必填   | 默认值 | 描述           |
| -------------- | ------ | ---- | --- | ------------ |
| device\_sn     | int32  | true |     | 设备序号         |
| device\_token  | string | true |     | device token |
| notifier\_name | string | true |     | 证书名称         |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.39 解绑token{#delete\_\_user\_token\_unbind}

> DELETE /user/token/unbind

> POST /user/token/unbind

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称     | 数据类型  | 必填   | 描述   |
| -------- | ----- | ---- | ---- |
| deviceSn | int32 | true | 设备序号 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型     | 描述                |
| --------- | ------ | ----------------- |
| code      | int32  | 返回码，200是成功        |
| data      | object | 结果数据              |
| message   | string | 错误信息，如果成功，该项为null |
| #### 接口描述 |        |                   |

>

## 1.40 修改用户名{#put\_\_user\_username}

> PUT /user/username

> POST /user/username

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称     | 数据类型   | 必填   | 描述  |
| -------- | ------ | ---- | --- |
| username | string | true | 用户名 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>

## 1.41 设置新消息是否振动{#put\_\_user\_vibratory}

> PUT /user/vibratory

> POST /user/vibratory

#### 请求头

| 参数名称         | 数据类型   | 必填    | 描述                                                   |
| ------------ | ------ | ----- | ---------------------------------------------------- |
| access-token | string | false | 令牌                                                   |
| app\_id      | string | true  | 应用ID                                                 |
| group\_id    | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user\_id     | int64  | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口   |

#### 请求参数(Query Param)

| 参数名称  | 数据类型    | 必填   | 描述                       |
| ----- | ------- | ---- | ------------------------ |
| value | boolean | true | 是否振动： true-振动, false-不振动 |

#### 响应体

● 200 响应数据格式：JSON

| 参数名称      | 类型      | 描述                |
| --------- | ------- | ----------------- |
| code      | int32   | 返回码，200是成功        |
| data      | boolean | 结果数据              |
| message   | string  | 错误信息，如果成功，该项为null |
| #### 接口描述 |         |                   |

>
