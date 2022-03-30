# 服务端开发指南（API）

本页面供快速集成使用，了解更多请访问[详细文档](../reference/server-api/README.md)

## 入门

### 术语介绍

* app_id

    `app_id`是创建App时，Lanying IM为App生成的唯一标识，是字符串类型。可从console"应用信息"页面获取。
* api_endpoint

    `api_endpoint`是App所在API服务的地址。可从console"应用信息"页面获取。
* access-token

    `access-token`用作权限校验。可在console"Token管理"页面为App生成access-token或选用已有access-token。

### API概述

Lanying IM API服务基于HTTPS安全协议，保证了调用时数据传输的安全性。同时API服务提供访问控制，调用前先需要获取 特有的`access-token`，才有权限操作App下用户、群组等数据。涉及的`access-token`请妥善保存。

调用所有Lanying IM API前，要获取参数`api_endpoint`、`app_id`、`access-token`。 参数`app_id`，`access-token`在请求的Header中使用，未特殊说明的请求Content-Type类型为`application/json`。

调用Lanying IM API的请求的通用示例（请根据具体值替换用`{}`表示的变量）：

```
curl -X {METHOD} '{api_endpoint}/{URI}' \
-H "Content-Type: application/json" \
-H 'access-token: {access-token}' \
-H 'app_id: {app_id}' \
```

### API分类

Lanying IM API主要分为用户API、好友API、群组API、消息API、推送API。

* 用户API

    用户隶属于单个App，是即时通讯的基础。有了用户才能实现好友、群组功能。用户数据分为基本信息和设置信息。 基本信息包括邮箱、手机号、用户名、密码。设置信息包括是否自动下载缩略图和文件、邀请入群是否需要确认等。 总体上讲，用户API主要涉及到其基本信息的更新和用户的设置，相关API以`/user`开头，后面接具体的资源，如获取用户设置API为"GET /user/settings"。
* 好友API

    好友是用户之间的关系，Lanying IM好友设计中用户可为好友设置备注、设置好友消息的通知方式、可申请加好友、拉黑好用等。 好友API提供了好友信息、好友申请、好友列表、好友黑名单列表等相关操作，其API以`/roster`开头。
* 群组API

    群组可以实现多用户通讯。Lanying IM设计中群成员角色分为群主、群管理员、普通群成员，权限等级依次降低，群主拥有群的所有权限，管理员有操作 群成员和修改群信息群设置的权限，根据群设置能普通群成员是否具有修改群信息以及邀请用户加入群组的权限。群成员功能设计有入群邀请、入群申请、 群黑名单、群禁言列表。 主要API包括群组数据操作和群成员操作，群数据操作主要有创建群、解散群、转让群以及群信息、群设置的更新、 群公告操作、群共享文件操作，群成员操作主要有邀请用户入群、管理员处理邀请、用户申请入群、用户处理申请、设置群黑名单、设置群禁言列表、 用户退出群、将用户踢出群等，API以`/group`开头。
* 消息API

    消息相关API是对IM服务的封装，旨在为使用者提供简便方法以实现通讯功能。消息API以`/message`开头。
* 推送API

    推送相关API用于推送通知到设备，其API以`/push`开头。

一般情况下，请求到Lanying IM服务的API如遇业务错误，则返回的http code为200，在response body会返回Lanying IM自定义错误码。 具体错误码的含义见错误码页面。

下面以以下值为例介绍部分关键API，实际请求中请予以替换。

* `app_id`: `welovemaxim`
* `api_endpoint`: `https://api.maximtop.com`
* `access-token`: `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg`

## 用户API

### 注册用户

* API描述

    为指定App注册Lanying IM用户。
* 请求说明

    Http方法: `POST` 资源路径: `/user/register/v2`
* 参数说明
  - Header参数

| 参数      | 描述     | 备注 |
| ------- | ------ | -- |
| app_id | App id | 必填 |

  - Request Body参数

| 参数       | 描述  | 备注                                        |
| -------- | --- | ----------------------------------------- |
| username | 用户名 | 必填，用户名仅支持字母数字下划线组合，且不能是纯数字，不能以maxim、mta开头 |
| password | 密码  | 必填                                        |
* cURL请求示例

    ```
    curl -X POST 'https://api.maximtop.com/user/register/v2' \
    -H "Content-Type: application/json" \
    -H 'app_id: welovemaxim' \
    -d '{ "username": "test_user", "password": "asd"}'
    ```
* 返回结果示例

    ```
    {
    	"code": 200,
    	"data": {
    		"user_id": 2302128618880,
    		"auto_download": false,
    		"group_confirm": false,
    		"no_sounds": false,
    		"no_push": false,
    		"vibratory": false,
    		"no_push_detail": false,
    		"auth_mode": 0,
    		"no_push_start_hour": 0,
    		"no_push_end_hour": 0
    	}
    }
    ```

## 好友API

### 添加好友

* API描述

    为指定用户添加好友。
* 请求说明

    Http方法: `POST` 资源路径: `/user/add_roster`
* 参数说明
  - Header参数

| 参数           | 描述          | 备注 |
| ------------ | ----------- | -- |
| app_id      | APP ID      | 必填 |
| access-token | token       | 必填 |
| user_id     | 添加方user_id | 必填 |
  - Request Body参数

| 参数   | 描述             | 备注 |
| ---- | -------------- | -- |
| list | 被添加方user_id列表 | 必填 |
* cURL请求示例

    ```
    curl -X POST 'https://api.maximtop.com/user/add_roster' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -H 'user_id: 2302128618880' \
    -d '{ "list": [2199040544848, 2199040544992]}'
    ```
* 返回结果示例

    ```
    {
    	"code": 200,
    	"data": true
    }
    ```

### 获取好友列表

* API描述

    获取指定用户的好友列表。
* 请求说明

    Http方法: `GET` 资源路径: `/user/rosters`
* 参数说明
  - Header参数

| 参数           | 描述           | 备注 |
| ------------ | ------------ | -- |
| app_id      | APP ID       | 必填 |
| access-token | token        | 必填 |
| user_id     | 当前用户user_id | 必填 |
  - Request Body参数

      无
* cURL请求示例

    ```
    curl -X GET 'https://api.maximtop.com/user/rosters' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -H 'user_id: 2302128618880'
    ```
* 返回结果示例

    ```
    {
    	"code": 200,
    	"data": [{
    		"user_id": 2199040544848,
    		"name": "a"
    	}, {
    		"user_id": 2199040544992,
    		"name": "b"
    	}]
    }
    ```

## 群组API

### 创建群

* API描述

    以指定用户为群主创建群组。
* 请求说明

    Http方法: `POST` 资源路径: `/group/create`
* 参数说明
  - Header参数

| 参数           | 描述         | 备注 |
| ------------ | ---------- | -- |
| app_id      | APP ID     | 必填 |
| access-token | token      | 必填 |
| user_id     | 群主user_id | 必填 |
  - Request Body参数

| 参数          | 描述  | 备注 |
| ----------- | --- | -- |
| name        | 群名称 | 必填 |
| description | 群描述 | 可选 |
* cURL请求示例

    ```
    curl -X POST 'https://api.maximtop.com/group/create' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -H 'user_id: 2302128618880' \
    -d '{ "name": "g001", "description": "test-group"}'
    ```
* 返回结果示例

    ```
    {
    	"code": 200,
    	"data": {
    		"name": "g001",
    		"status": 0,
    		"description": "test-group",
    		"type": 0,
    		"group_id": 2306414607729,
    		"owner_id": 2302128618880,
    		"created_at": 1569615417000,
    		"updated_at": 1569615417000,
    		"member_invite": true,
    		"apply_approval": 1,
    		"read_ack": false,
    		"history_visible": false,
    		"member_modify": false
    	}
    }
    ```

### 邀请用户加群

* API描述

    以指定用户为群主邀请用户加入群组。
* 请求说明

    Http方法: `POST` 资源路径: `/group/invite`
* 参数说明
  - Header参数

| 参数           | 描述         | 备注 |
| ------------ | ---------- | -- |
| app_id      | APP ID     | 必填 |
| access-token | token      | 必填 |
| user_id     | 群主user_id | 必填 |
  - Request Body参数

| 参数         | 描述     | 备注 |
| ---------- | ------ | -- |
| group_id  | 群id    | 必填 |
| user_list | 用户id列表 | 必填 |
* cURL请求示例

    ```
    curl -X POST 'https://api.maximtop.com/group/invite' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -H 'user_id: 2302128618880' \
    -d '{ "group_id": 2306414607729, "user_list": [2199040544848, 2199040544992]}'
    ```
* 返回结果示例

    ```
    {
    	"code": 200,
    	"data": [{
    		"result": "success",
    		"user_id": 2199040544848
    	}, {
    		"result": "success",
    		"user_id": 2199040544992
    	}]
    }
    ```

### 获取群成员列表

* API描述

    获取群成员列表，支持分页。 分页由limit和cursor字段控制，limit是每页的大小，cursor是游标。 **cursor**：取第某页数据后若还有成员数据，会返回cursor字段，传cursor字段会取游标的下一页数据。
* 请求说明

    Http方法: `GET` 资源路径: `/group/member_list`
* 参数说明
  - Header参数

| 参数           | 描述         | 备注 |
| ------------ | ---------- | -- |
| app_id      | APP ID     | 必填 |
| access-token | token      | 必填 |
| user_id     | 群主user_id | 必填 |
  * 查询参数参数

| 参数        | 描述       | 备注        |
| --------- | -------- | --------- |
| group_id | 群id      | 必填        |
| cursor    | 分页游标     | 可选，默认取第一页 |
| limit     | 单次获取成员数量 | 可选，默认1000 |
* cURL请求示例

    ```
    curl -X GET 'https://api.maximtop.com/group/member_list?group_id=2306414607729&limit=50' \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -H 'user_id: 2302128618880'
    ```
* 返回结果示例

    ```
    {
    	"code": 200,
    	"data": [{
    		"user_id": 2302128618880,
    		"join_time": 1569615417000
    	}, {
    		"user_id": 2199040544848,
    		"join_time": 1569615490000
    	}, {
    		"user_id": 2199040544992,
    		"join_time": 1569615490000
    	}],
    	"version": 1569586735861
    }
    ```

### 解散群

* API描述

    解散群组。
* 请求说明

    Http方法: `DELETE` 资源路径: `/group/destroy`
* 参数说明
  - Header参数

| 参数           | 描述         | 备注 |
| ------------ | ---------- | -- |
| app_id      | APP ID     | 必填 |
| access-token | token      | 必填 |
| user_id     | 群主user_id | 必填 |
* cURL请求示例

    ```
    curl -X DELETE 'https://api.maximtop.com/group/destroy?group_id=2306414607729' \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -H 'user_id: 2302128618880'
    ```
* 返回结果示例

    ```
    {
    	"code": 200,
    	"data": true
    }
    ```

## 发送消息API

### 管理员发送单聊文本消息

* API描述

    给指定目标发送消息，可以批量发给群或用户。 指定目标用targets字段表示，列表类型，列表中id只能为用户id或群id的一种，两者不能混合发送。
* 请求说明

    Http方法: `POST` 资源路径: `/message/send`
* 参数说明
  - Header参数

| 参数           | 描述     | 备注 |
| ------------ | ------ | -- |
| app_id      | APP ID | 必填 |
| access-token | token  | 必填 |
  - Request Body参数

| 参数            | 描述            | 备注 |
| ------------- | ------------- | -- |
| targets       | 目标id列表        | 必填 |
| type          | 目标类型,1:单聊2:群聊 | 必填 |
| content_type | 消息内容类型,0:文本消息 | 必填 |
| ext           | 扩展字段          | 可选 |
* cURL请求示例

    ```
    curl -X POST 'https://api.maximtop.com/message/send' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -d '{"targets":[2302128618880],"type":1,"content":"hello","content_type":0}'
    ```
* 返回结果示例

    ```
    {
        "code": 200,
        "data": true
    }
    ```

## 推送API

### 管理员发送推送通知

* API描述

    给指定目标发送通知，可以推送给APP下的所有人，也可以按标签/别名/PushToken/用户ID来推送。
* 请求说明

    Http方法: `POST` 资源路径: `/push/notify`
* 参数说明：
  - Header参数

    | 参数           | 描述     | 备注 |
    | ------------ | ------ | -- |
    | app_id      | APP ID | 必填 |
    | access-token | token  | 必填 |

  * Request Body主要参数

| 参数       | 描述    | 备注 |
| -------- | ----- | -- |
| audience | 推送目标  | 必填 |
| message  | 推送消息体 | 必填 |
  * audience：推送目标。类型为字符串或JSONObject:

      ```
      "all", 表示发给所有设备
      {"tag":["tag1","tag2"]} 表示发给标签为tag1或tag2的设备
      {"alias":["alias1","alias2"]} 表示发给别名为alias1或alias2的设备
      {"user_id":[111,222]} 表示发给用户ID为111或222的设备
      {"push_token":["push_token1","push_token2"]} 表示发给PushToken为push_token1或push_token2的设备
      使用标签/别名/用户ID/pushToken推送时，列表长度不能超过500
      ```
  * message:推送消息体, 主要字段如下，全部字段请参考API详细文档

| 参数              | 描述   | 备注                                          |
| --------------- | ---- | ------------------------------------------- |
| type            | 通知类型 | 可选，text - 文本，image - 图片， cmd - 透传消息。默认为text |
| title           | 通知标题 | 可选                                          |
| body            | 通知内容 | 可选                                          |
| attachment_url | 附件地址 | 可选,图片/音频/视频的URL地址。                          |
| ext             | 扩展字段 | 可选，类型为JSONObject                            |
* cURL请求示例

    ```
    推送文本给APP下所有设备：
    curl -X POST 'https://api.maximtop.com/push/notify' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -d '{"audience": "all","message": {"type": "text","title": "this is push title","body": "this is push body"}}'
    ```

    ```
    推送图片给push_token为token1或token2的设备:
    curl -X POST 'https://api.maximtop.com/push/notify' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -d '{"audience": {"push_token":["token1","token2"]},"message": {"type": "image","title": "this is push title","body": "this is push body","attachment_url": "https://xxx.com/images/1.jpg"}}'
    ```

    ```
    推送透传消息给标签为beijing或shanghai的所有设备，透传消息不会展示到通知栏上:
    curl -X POST 'https://api.maximtop.com/push/notify' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -d '{"audience": {"tag":["beijing","shanghai"]},"message": {"type": "cmd","title": "this is push title","body": "this is push body","ext": {"key1": 12345, "key2": "xxx" }}}'
    ```
* 返回结果示例

    ```
    {
        "code": 200,
        "data": true
    }
    ```

## 附录

### 错误码说明

* 1xxxx表示用户/好友体系问题
* 2xxxx表示群组体系问题
* 3xxxx表示license问题

| 错误码   | 描述                      |
| ----- | ----------------------- |
| 10000 | 用户不存在                   |
| 10001 | 验证码不正确                  |
| 10002 | 请求参数不正确                 |
| 10003 | header中缺少access-token参数 |
| 10004 | 用户已存在                   |
| 10005 | 用户已在好友列表                |
| 10006 | 用户在黑名单列表                |
| 10007 | 好友申请不存在或已过期             |
| 10008 | header中access-token无效   |
| 10009 | oss异常                   |
| 10010 | 用户无权限                   |
| 10011 | user_id已绑定             |
| 10012 | 用户拒绝好友申请                |
| 12001 | 上传推送图片到小米平台失败           |
| 12002 | 推送图片文件大小需小于1M           |
| 12003 | 上传推送图片到OPPO平台失败         |
| 12004 | 推送的图片地址无法下载             |
| 12005 | 推送目标列表的长度不能超过500        |
| 12006 | 没有开通推送功能                |
| 20000 | 服务器数据库异常                |
| 20001 | 群组不存在                   |
| 20002 | 用户不是群成员                 |
| 20003 | msg_push_mode值不合法     |
| 20004 | 群主不能直接离开群               |
| 20005 | 转让群异常：被转让人非群成员          |
| 20006 | 群组处于修复模式                |
| 20007 | App群数量超限                |
| 20008 | 用户创建的群数量超限              |
| 20009 | 用户加入的群数量超限              |
| 20010 | 群人数超限                   |
| 20011 | 操作需要群成员权限               |
| 20012 | 操作需要群管理员权限              |
| 20013 | 操作需要群主权限                |
| 20014 | 入群申请已过期或已处理             |
| 20015 | 入群邀请已过期或已处理             |
| 20016 | 用户被踢出群次数超限，不能再加入群       |
| 20017 | 用户已经是群成员                |
| 20018 | 用户在群黑名单列表               |
| 20020 | 群公告不存在                  |
| 20021 | 群公告被管理员禁用               |
| 20022 | 群共享文件不存在                |
| 20023 | 无权限操作群共享文件              |
| 20024 | 群邀请二维码不合法               |
| 20025 | 群邀请二维码已过期               |
| 30021 | Lanying IM License无效         |
| 30022 | Lanying IM License已过期        |
| 30023 | 超出Lanying IM License限制       |
| 40000 | app_id不存在              |
