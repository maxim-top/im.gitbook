# Server-side（server api）Quick integration指南

This page is for quick integration, visit [detailed documentation](https://maximtop.com/docs/api)

## Getting started

### Terminology introduction

*   app\_id

    `app_id`is the unique identity that MaxIM generates for App when it is created and is of string type. Available from "Application Information" page in Console.
*   api\_endpoint

    `api_endpoint`is the address of the API service where the app resides. Available from "Application Information" page in Console.
*   access-token

    `access-token`is used for permission verification. You can generate access-token for App or select existing access-token from “Token Management” page in Console.

### API profile

MaxIM API service is based on the HTTPS security protocol, which ensures the security of data transfer when invoked. At the same time, MaxIM API service provides access control, and it is necessary to obtain the unique`access-token`to operate users, groups and other data under App legally. Involved`access-token`shall be kept properly.

Before calling any MaxIM API, please get parameter first`api_endpoint`、`app_id`、`access-token`. Parameter`app_id`，`access-token`will be used in the header of request, and unspecified request Content-Type type is`application/json`。

a generic example of the request that calls MaxIM API (please replace the variable represented by`{}`with a specified value):

```
curl -X {METHOD} '{api_endpoint}/{URI}' \
-H "Content-Type: application/json" \
-H 'access-token: {access-token}' \
-H 'app_id: {app_id}' \
```

### API classification

MaxIM API is mainly divided into user API, friend API, group API, message API and push API.

*   User API

    Users belong to a single App, which is the foundation of instant messaging. Only with users can we realize the functions of friends and groups. User data is divided into basic information and setting information. Basic information includes email address, mobile number, username and password. Setting information includes whether to download thumbnails and files automatically, whether to confirm the invitation to join group, etc. Generally speaking, the user API mainly involves the update of its basic information and user settings, and the related API starts with`/user`, followed by specific resources, ex. “GET /user/settings” to get user settings API.
*   Friend API

    Friend is the relationship between users. In MaxIM friendship design, users can set remarks for friends, set the notification method of friend messages, apply for adding friends, and blacklist a friend. Friend API provides friend information, friend application, friend list, friend blacklist and other related operations, and its API starts with`/roster`.
*   Group API

    Groups enable multi-user communication. In MaxIM design, the roles of group members are divided into group Owners, group Admins and group Members, and the authority levels are lowered in turn. The group Owners have all the permissions of the group, while the Admins have the permissions to operate group members and modify group information settings. According to group settings, ordinary group Members may have or not have the permissions to modify group information and invite users to join group. The functional design of group membership includes invitation to join group, application to join group, set group blacklist and group ban list. The main APIs include group data operations and group member operations. Group data operations mainly include create group, dissolve group, transfer group Owner, update group information and group settings, group announcement operation, group shared file operation; and group member operations mainly include invite user to join group, Admin process invitation, user apply to join group, user process application, set group blacklist, set group ban list, user quit group, kick user out of group, etc. APIs start with`/group`.
*   Message API

    Message APIs are encapsulations of IM services designed to provide an easy way for messaging. Message APIs start with`/message`.
*   PushAPI

    Push相关API用于Push通知到设备，其API以`/push`.

In general, the API requested to MaxIM service will return an http code of 200 in case of a business error, and a MaxIM custom error code will be returned in the response body. See the Error Code page for the specific meaning of error code.

Some of the key APIs are demonstrated with the following values, which should be replaced in your actual request.

* `app_id`: `welovemaxim`
* `api_endpoint`: `https://api.maximtop.com`
* `access-token`: `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg`

## User API

### Register user

*   API description

    Register a MaxIM user for the specified App.
*   Request description

    Http method: `POST` Resource path: `/user/register/v2`
*   Parameter description

    * Header parameter

    | Parameter      | Description     | Comment |
    | ------- | ------ | -- |
    | app\_id | App id | Required |

    * Request Body parameter

    | Parameter       | Description  | Comment                                        |
    | -------- | --- | ----------------------------------------- |
    | username | Username | Required, username supports only alphanumeric and underscore combinations, and cannot be pure numbers nor begin with maxim, mta |
    | password | Password  | Required                                        |
*   cURL request example

    ```
    curl -X POST 'https://api.maximtop.com/user/register/v2' \
    -H "Content-Type: application/json" \
    -H 'app_id: welovemaxim' \
    -d '{ "username": "test_user", "password": "asd"}'
    ```
*   Returned result example

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

## Friend API

### Add friend

*   API description

    Add friend for specified user.
*   Request description

    Http method: `POST` Resource path: `/user/add_roster`
* Parameter description
  *   Header parameter

      | Parameter           | Description          | Comment |
      | ------------ | ----------- | -- |
      | app\_id      | APP ID      | Required |
      | access-token | token       | Required |
      | user\_id     | user\_id of adding party | Required |
  *   Request Body parameter

      | Parameter   | Description             | Comment |
      | ---- | -------------- | -- |
      | list | user\_id list of added party | Required |
*   cURL request example

    ```
    curl -X POST 'https://api.maximtop.com/user/add_roster' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -H 'user_id: 2302128618880' \
    -d '{ "list": [2199040544848, 2199040544992]}'
    ```
*   Returned result example

    ```
    {
    	"code": 200,
    	"data": true
    }
    ```

### Get friend list

*   API description

    Get friend list of the specified user.
*   Request description

    Http method: `GET` Resource path: `/user/rosters`
* Parameter description
  *   Header parameter

      | Parameter           | Description           | Comment |
      | ------------ | ------------ | -- |
      | app\_id      | APP ID       | Required |
      | access-token | token        | Required |
      | user\_id     | user\_id of current user | Required |
  *   Request Body parameter

      None
*   cURL request example

    ```
    curl -X GET 'https://api.maximtop.com/user/rosters' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -H 'user_id: 2302128618880'
    ```
*   Returned result example

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

## Group API

### Create group

*   API description

    Create a group with the specified user as group Owner.
*   Request description

    Http method: `POST` Resource path: `/group/create`
* Parameter description
  *   Header parameter

      | Parameter           | Description         | Comment |
      | ------------ | ---------- | -- |
      | app\_id      | APP ID     | Required |
      | access-token | token      | Required |
      | user\_id     | user\_id of group Owner | Required |
  *   Request Body parameter

      | Parameter          | Description  | Comment |
      | ----------- | --- | -- |
      | name        | Group name | Required |
      | description | Group description | Optional |
*   cURL request example

    ```
    curl -X POST 'https://api.maximtop.com/group/create' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -H 'user_id: 2302128618880' \
    -d '{ "name": "g001", "description": "test-group"}'
    ```
*   Returned result example

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

### Invite user to join group

*   API description

    Invite user to join the group with the specified user as group Owner.
*   Request description

    Http method: `POST` Resource path: `/group/invite`
* Parameter description
  *   Header parameter

      | Parameter           | Description         | Comment |
      | ------------ | ---------- | -- |
      | app\_id      | APP ID     | Required |
      | access-token | token      | Required |
      | user\_id     | user\_id of group Owner | Required |
  *   Request Body parameter

      | Parameter         | Description     | Comment |
      | ---------- | ------ | -- |
      | group\_id  | Group id    | Required |
      | user\_list | User id list | Required |
*   cURL request example

    ```
    curl -X POST 'https://api.maximtop.com/group/invite' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -H 'user_id: 2302128618880' \
    -d '{ "group_id": 2306414607729, "user_list": [2199040544848, 2199040544992]}'
    ```
*   Returned result example

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

### Get group member list

*   API description

    Get group member list, can be in pages. Pages are controlled by limit and cursor fields, limit for page size, cursor as the name suggest. **cursor**：If there is still member data left after fetching data on a certain page, it will return cursor field for fetching data from the next page of the cursor.
*   Request description

    Http method: `GET` Resource path: `/group/member_list`
* Parameter description
  *   Header parameter

      | Parameter           | Description         | Comment |
      | ------------ | ---------- | -- |
      | app\_id      | APP ID     | Required |
      | access-token | token      | Required |
      | user\_id     | user\_id of group Owner | Required |
  *   Query parameter

      | Parameter        | Description       | Comment        |
      | --------- | -------- | --------- |
      | group\_id | Group id      | Required        |
      | cursor    | Paged cursor     | Optional, default the first page |
      | limit     | Number of members to fetch at once | Optional, default 1,000 |
*   cURL request example

    ```
    curl -X GET 'https://api.maximtop.com/group/member_list?group_id=2306414607729&limit=50' \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -H 'user_id: 2302128618880'
    ```
*   Returned result example

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

### Disband group

*   API description

    Dissolve group.
*   Request description

    Http method: `DELETE` Resource path: `/group/destroy`
* Parameter description
  *   Header parameter

      | Parameter           | Description         | Comment |
      | ------------ | ---------- | -- |
      | app\_id      | APP ID     | Required |
      | access-token | token      | Required |
      | user\_id     | user\_id of group Owner | Required |
*   cURL request example

    ```
    curl -X DELETE 'https://api.maximtop.com/group/destroy?group_id=2306414607729' \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -H 'user_id: 2302128618880'
    ```
*   Returned result example

    ```
    {
    	"code": 200,
    	"data": true
    }
    ```

## Send message API

### Admin send single chat text-message

*   API description

    Send message to a specified destination, which can be sent in batches to groups or users. The specified destination is represented by targets field, list type and ids in list can only be one of user/group ids, and the both types cannot be mixed.
*   Request description

    Http method: `POST` Resource path: `/message/send`
* Parameter description
  *   Header parameter

      | Parameter           | Description     | Comment |
      | ------------ | ------ | -- |
      | app\_id      | APP ID | Required |
      | access-token | token  | Required |
  *   Request Body parameter

      | Parameter            | Description            | Comment |
      | ------------- | ------------- | -- |
      | targets       | List of target ids        | Required |
      | type          | Target type, 1: Single chat 2: Group chat | Required |
      | content\_type | Message content type, 0: text-message | Required |
      | ext           | Extension field          | Optional |
*   cURL request example

    ```
    curl -X POST 'https://api.maximtop.com/message/send' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -d '{"targets":[2302128618880],"type":1,"content":"hello","content_type":0}'
    ```
*   Returned result example

    ```
    {
        "code": 200,
        "data": true
    }
    ```

## PushAPI

### 管理员SendPush通知

*   API description

    给指定目标Send通知，可以Push给APP下的所有人，也可以按标签/Alias/PushToken/User ID来Push。
*   Request description

    Http method: `POST` Resource path: `/push/notify`
* Parameter description：
  *   Header parameter

      | Parameter           | Description     | Comment |
      | ------------ | ------ | -- |
      | app\_id      | APP ID | Required |
      | access-token | token  | Required |
  *   Request Body主要Parameter

      | Parameter       | Description    | Comment |
      | -------- | ----- | -- |
      | audience | Push目标  | Required |
      | message  | Message body pushed | Required |
  *   audience：Push目标。Class型为字符串或JSONObject:

      ```
      "all", means push to all devices
      {"tag":["tag1","tag2"]} means push to devices labeled tag1 or tag2
      {"alias":["alias1","alias2"]} means push to devices with alias1 or alias2
      {"user_id":[111,222]} means push to devices with user ID 111 or 222
      {"push_token":["push_token1","push_token2"]} means push to devices with PushToken push_token1 or push_token2
      List length cannot exceed 500 when pushed with tag/alias/user ID/pushToken
      ```
  *   message:Message body pushed, 主要Field如下，全部Field请参考API Details

      | Parameter              | Description   | Comment                                          |
      | --------------- | ---- | ------------------------------------------- |
      | type            | 通知Class型 | Optional，text - 文本，image - Image， cmd - 透传Message。默认为text |
      | title           | 通知标题 | Optional                                          |
      | body            | 通知Content | Optional                                          |
      | attachment\_url | AttachmentAddress | Optional,Image/音频/视频的URLAddress。                          |
      | ext             | Extension field | Optional，Class型为JSONObject                            |
*   cURL request example

    ```
    Push文本给APP下所有设备：
    curl -X POST 'https://api.maximtop.com/push/notify' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -d '{"audience": "all","message": {"type": "text","title": "this is push title","body": "this is push body"}}'
    ```

    ```
    PushImage给push_token为token1或token2的设备:
    curl -X POST 'https://api.maximtop.com/push/notify' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -d '{"audience": {"push_token":["token1","token2"]},"message": {"type": "image","title": "this is push title","body": "this is push body","attachment_url": "https://xxx.com/images/1.jpg"}}'
    ```

    ```
    Push透传Message给标签为beijing或shanghai的所有设备，透传Message不会展示到通知栏上:
    curl -X POST 'https://api.maximtop.com/push/notify' \
    -H "Content-Type: application/json" \
    -H 'access-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJhcHAiOiJkcGJkdmVrZmVjYm8iLCJzdWIiOiIyMCIsImNsdXN0ZXIiOjAsInJvbGUiOjIsImlhdCI6MTU2Nzk5NzQwOH0.U-iFpEwprrkf-mFkhHN_CWmF5nkBbRQLTjttN4Qlkzw3ET1Zke9OZdjutm90KSyDs9jjYvUSAGGsWVjLmDZlkg' \
    -H 'app_id: welovemaxim' \
    -d '{"audience": {"tag":["beijing","shanghai"]},"message": {"type": "cmd","title": "this is push title","body": "this is push body","ext": {"key1": 12345, "key2": "xxx" }}}'
    ```
*   Returned result example

    ```
    {
        "code": 200,
        "data": true
    }
    ```

## Appendix

### Error code description

* 1xxxx indicates an issue related to user/friend system
* 2xxxx indicates an issue related to group system
* 3xxxx indicates an issue related to license

| Error code   | Description                      |
| ----- | ----------------------- |
| 10000 | User does not exist                   |
| 10001 | Incorrect verification code                  |
| 10002 | Incorrect request parameter                 |
| 10003 | Missing access-token parameter in header |
| 10004 | User already exists                   |
| 10005 | User already exists in friend list                |
| 10006 | User already exists in blacklist                |
| 10007 | Friend does not exist or expired             |
| 10008 | Invalid access-token in header   |
| 10009 | oss exception                   |
| 10010 | User has no permission                   |
| 10011 | user\_id bound             |
| 10012 | User rejected friend request                |
| 12001 | 上传PushImage到XiaomiPlatform失败           |
| 12002 | PushImageFile size需小于1M           |
| 12003 | 上传PushImage到OPPOPlatform失败         |
| 12004 | Push的ImageAddressNone法Download Center             |
| 12005 | Push目标列表的长度不能超过500        |
| 12006 | 没有开通PushFeatures                |
| 20000 | Server database exception                |
| 20001 | Group does not exist                   |
| 20002 | The user is not a group member                 |
| 20003 | msg\_push\_mode value is illegal     |
| 20004 | Group Owner cannot quit the group directly               |
| 20005 | Group transfer error: Assignee is not a group member          |
| 20006 | Group in repair mode                |
| 20007 | Number of groups in App exceeds limit                |
| 20008 | Number of user-created groups exceeds limit              |
| 20009 | Number of user-joined groups exceeds limit              |
| 20010 | Number of group members exceeds limit                   |
| 20011 | This operation needs group member permission               |
| 20012 | This operation needs group Admin permission              |
| 20013 | This oeration needs group Owner permission                |
| 20014 | Application of membership expired or processed             |
| 20015 | Invitation of membership expired or processed             |
| 20016 | Times of user’s kicked-out exceeds limit, can no longer join group       |
| 20017 | User is already a group member                |
| 20018 | User is already blacklisted               |
| 20020 | Group announcement does not exist                  |
| 20021 | Group announcement disabled by Admin               |
| 20022 | Group shared file does not exist                |
| 20023 | No permission to operate group shared file              |
| 20024 | Group invitation QR Code is illegal               |
| 20025 | Group invitation QR Code has expired               |
| 30021 | Invalid MaxIM License         |
| 30022 | Expired MaxIM License        |
| 30023 | MaxIM License limit exceeded       |
| 40000 | app\_id does not exist              |
