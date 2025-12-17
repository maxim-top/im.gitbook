# 4 Group interface{#group}

## 4.1 Add group Admin{#post\_\_group\_admin\_add}

> POST /group/admin/add

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description  |
| -------------- | ------------- | -------- | ------- | ------------ |
| group\_id      | int64         | true     |         | Group id     |
| user\_list     | array\[int64] | true     |         | User id list |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ reason                   | string         | Error message                         |
| ⇥ result                   | string         | Operation result: success/fail        |
| ⇥ user\_id                 | int64          | User ID                               |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 4.2 Remove group Admin{#delete\_\_group\_admin\_remove}

> DELETE /group/admin/remove

> POST /group/admin/remove

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description  |
| -------------- | ------------- | -------- | ------- | ------------ |
| group\_id      | int64         | true     |         | Group id     |
| user\_list     | array\[int64] | true     |         | User id list |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ reason                   | string         | Error message                         |
| ⇥ result                   | string         | Operation result: success/fail        |
| ⇥ user\_id                 | int64          | User ID                               |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 4.3 Get the list of group Admins{#get\_\_group\_admin\_list}

> GET /group/admin\_list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| group\_id      | int64     | true     | GroupID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ display\_name            | string         | Group member profile                  |
| ⇥ expired\_time            | int64          | BanExpiration time(milliseconds)      |
| ⇥ join\_time               | int64          | Member join time(milliseconds)        |
| ⇥ user\_id                 | int64          | User id                               |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 4.4 Get group announcement details by group id and announcement id{#get\_\_group\_announcement}

> GET /group/announcement

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name   | Data Type | Required | Description     |
| ---------------- | --------- | -------- | --------------- |
| announcement\_id | int64     | true     | Announcement ID |
| group\_id        | int64     | true     | GroupID         |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                             |
| -------------------------- | ------ | --------------------------------------- |
| code                       | int32  | Return code, 200 is success             |
| data                       | object | Result data                             |
| ⇥ author                   | int64  | Announcement publisher                  |
| ⇥ content                  | string | Announcement content                    |
| ⇥ created\_at              | int64  | Announcement publish time(milliseconds) |
| ⇥ group\_id                | int64  | Group id                                |
| ⇥ id                       | int64  | Announcement id                         |
| ⇥ title                    | string | Announcement tittle                     |
| message                    | string | Error information, null means success   |
| #### Interface Description |        |                                         |

>

## 4.5 Delete group announcement{#delete\_\_group\_announcement\_delete}

> DELETE /group/announcement/delete

> POST /group/announcement/delete

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name   | Data Type | Required | Description     |
| ---------------- | --------- | -------- | --------------- |
| announcement\_id | int64     | true     | Announcement ID |
| group\_id        | int64     | true     | GroupID         |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                           |
| -------------------------- | ------ | ------------------------------------- |
| code                       | int32  | Return code, 200 is success           |
| data                       | object | Result data                           |
| message                    | string | Error information, null means success |
| #### Interface Description |        |                                       |

>

## 4.6 Edit group announcement{#post\_\_group\_announcement\_edit}

> POST /group/announcement/edit

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description          |
| -------------- | --------- | -------- | ------- | -------------------- |
| content        | string    | true     |         | Announcement content |
| group\_id      | int64     | true     |         | Group id             |
| title          | string    | true     |         | Announcement tittle  |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                             |
| -------------------------- | ------ | --------------------------------------- |
| code                       | int32  | Return code, 200 is success             |
| data                       | object | Result data                             |
| ⇥ author                   | int64  | Announcement publisher                  |
| ⇥ content                  | string | Announcement content                    |
| ⇥ created\_at              | int64  | Announcement publish time(milliseconds) |
| ⇥ group\_id                | int64  | Group id                                |
| ⇥ id                       | int64  | Announcement id                         |
| ⇥ title                    | string | Announcement tittle                     |
| message                    | string | Error information, null means success   |
| #### Interface Description |        |                                         |

>

## 4.7 Get the latest group announcement details{#get\_\_group\_announcement\_last}

> GET /group/announcement/last

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| group\_id      | int64     | true     | GroupID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                             |
| -------------------------- | ------ | --------------------------------------- |
| code                       | int32  | Return code, 200 is success             |
| data                       | object | Result data                             |
| ⇥ author                   | int64  | Announcement publisher                  |
| ⇥ content                  | string | Announcement content                    |
| ⇥ created\_at              | int64  | Announcement publish time(milliseconds) |
| ⇥ group\_id                | int64  | Group id                                |
| ⇥ id                       | int64  | Announcement id                         |
| ⇥ title                    | string | Announcement tittle                     |
| message                    | string | Error information, null means success   |
| #### Interface Description |        |                                         |

>

## 4.8 Get group announcements list{#get\_\_group\_announcement\_list}

> GET /group/announcement/list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| group\_id      | int64     | true     | GroupID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                             |
| -------------------------- | -------------- | --------------------------------------- |
| code                       | int32          | Return code, 200 is success             |
| data                       | array\[object] | Result data                             |
| ⇥ author                   | int64          | Announcement publisher                  |
| ⇥ content                  | string         | Announcement content                    |
| ⇥ created\_at              | int64          | Announcement publish time(milliseconds) |
| ⇥ group\_id                | int64          | Group id                                |
| ⇥ id                       | int64          | Announcement id                         |
| ⇥ title                    | string         | Announcement tittle                     |
| message                    | string         | Error information, null means success   |
| #### Interface Description |                |                                         |

>

## 4.9 Get the list of group membership requests{#post\_\_group\_application\_list}

> POST /group/application\_list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                     |
| -------------- | --------- | -------- | ------------------------------- |
| cursor         | string    | false    | Cursor: where to start fetching |
| limit          | int32     | false    | How many to fetch               |
| version        | int64     | false    | Version                         |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description   |
| -------------- | ------------- | -------- | ------- | ------------- |
| group\_list    | array\[int64] | true     |         | Group id list |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                                          |
| -------------------------- | -------------- | ---------------------------------------------------- |
| code                       | int32          | Return code, 200 is success                          |
| cursor                     | string         | Cursor for page turning                              |
| data                       | array\[object] | Result data                                          |
| ⇥ applicant\_id            | int64          | Applicant's User ID                                  |
| ⇥ expired\_time            | int64          | Application Expiration Timestamp(milliseconds)       |
| ⇥ group\_id                | int64          | GroupID                                              |
| ⇥ reason                   | string         | Reason                                               |
| ⇥ status                   | int32          | Status: 0 - Pending, 1 - Agreed, 2 - Rejected        |
| message                    | string         | Error information, null means success                |
| total                      | int64          | Total                                                |
| version                    | int64          | Version, not used at present, reserved for extension |
| #### Interface Description |                |                                                      |

>

## 4.10 Apply for group membership{#post\_\_group\_apply}

> POST /group/apply

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description                       |
| -------------- | --------- | -------- | ------- | --------------------------------- |
| group\_id      | int64     | true     |         | Group id                          |
| reason         | string    | false    |         | Reason for membership application |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                           |
| -------------------------- | ------ | ------------------------------------- |
| code                       | int32  | Return code, 200 is success           |
| data                       | object | Result data                           |
| ⇥ reason                   | string | Error message                         |
| ⇥ result                   | string | Operation result: success/fail        |
| ⇥ user\_id                 | int64  | User ID                               |
| message                    | string | Error information, null means success |
| #### Interface Description |        |                                       |

>

## 4.11 Admin processes membership application{#put\_\_group\_apply\_handle}

> PUT /group/apply/handle

> POST /group/apply/handle

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description                                                 |
| -------------- | --------- | -------- | ------- | ----------------------------------------------------------- |
| approval       | boolean   | true     |         | Approval, bool type, true for approval, false for rejection |
| group\_id      | int64     | true     |         | Group id                                                    |
| user\_id       | int64     | true     |         | User id                                                     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                           |
| -------------------------- | ------ | ------------------------------------- |
| code                       | int32  | Return code, 200 is success           |
| data                       | object | Result data                           |
| ⇥ reason                   | string | Error message                         |
| ⇥ result                   | string | Operation result: success/fail        |
| ⇥ user\_id                 | int64  | User ID                               |
| message                    | string | Error information, null means success |
| #### Interface Description |        |                                       |

>

## 4.12 Ban a user{#post\_\_group\_ban}

> POST /group/ban

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description                   |
| -------------- | ------------- | -------- | ------- | ----------------------------- |
| duration       | int64         | true     |         | Duration of banned in minutes |
| group\_id      | int64         | true     |         | Group id                      |
| user\_list     | array\[int64] | true     |         | User id list                  |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ reason                   | string         | Error message                         |
| ⇥ result                   | string         | Operation result: success/fail        |
| ⇥ user\_id                 | int64          | User ID                               |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 4.13 Get a list of banned members{#get\_\_group\_banned\_list}

> GET /group/banned\_list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                    |
| -------------- | --------- | -------- | ------------------------------ |
| cursor         | string    | false    | Cursor:where to start fetching |
| group\_id      | int64     | true     | GroupID                        |
| limit          | int32     | false    | How many to fetch              |
| version        | int64     | false    | Version                        |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                                          |
| -------------------------- | -------------- | ---------------------------------------------------- |
| code                       | int32          | Return code, 200 is success                          |
| cursor                     | string         | Cursor for page turning                              |
| data                       | array\[object] | Result data                                          |
| ⇥ display\_name            | string         | Group member profile                                 |
| ⇥ expired\_time            | int64          | BanExpiration time(milliseconds)                     |
| ⇥ join\_time               | int64          | Member join time(milliseconds)                       |
| ⇥ user\_id                 | int64          | User id                                              |
| message                    | string         | Error information, null means success                |
| total                      | int64          | Total                                                |
| version                    | int64          | Version, not used at present, reserved for extension |
| #### Interface Description |                |                                                      |

>

## 4.14 Blacklist a user{#post\_\_group\_block}

> POST /group/block

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description  |
| -------------- | ------------- | -------- | ------- | ------------ |
| group\_id      | int64         | true     |         | Group id     |
| user\_list     | array\[int64] | true     |         | User id list |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ reason                   | string         | Error message                         |
| ⇥ result                   | string         | Operation result: success/fail        |
| ⇥ user\_id                 | int64          | User ID                               |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 4.15 Get backlist{#get\_\_group\_blocked\_list}

> GET /group/blocked\_list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                    |
| -------------- | --------- | -------- | ------------------------------ |
| cursor         | string    | false    | Cursor:where to start fetching |
| group\_id      | int64     | true     | GroupID                        |
| limit          | int32     | false    | How many to fetch              |
| version        | int64     | false    | Version                        |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                                          |
| -------------------------- | -------------- | ---------------------------------------------------- |
| code                       | int32          | Return code, 200 is success                          |
| cursor                     | string         | Cursor for page turning                              |
| data                       | array\[object] | Result data                                          |
| ⇥ created\_at              | string         | Creation time                                        |
| ⇥ group\_id                | int64          | GroupID                                              |
| ⇥ user\_id                 | int64          | User ID                                              |
| message                    | string         | Error information, null means success                |
| total                      | int64          | Total                                                |
| version                    | int64          | Version, not used at present, reserved for extension |
| #### Interface Description |                |                                                      |

>

## 4.16 Create group{#post\_\_group\_create}

> POST /group/create

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description                                 |
| -------------- | ------------- | -------- | ------- | ------------------------------------------- |
| avatar         | string        | false    |         | Group avatar                                |
| description    | string        | false    |         | Group description                           |
| name           | string        | false    |         | Group name                                  |
| type           | int32         | false    |         | Group type: 0 - private group, 2 - chatroom |
| user\_list     | array\[int64] | false    |         | List of user ids invited to join group      |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                                                                                                                                                                                             |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                       | int32   | Return code, 200 is success                                                                                                                                                                             |
| data                       | object  | Result data                                                                                                                                                                                             |
| ⇥ apply\_approval          | int32   | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests                                                                                         |
| ⇥ avatar                   | string  | Group avatar                                                                                                                                                                                            |
| ⇥ ban\_expire\_time        | int64   | Expiration time (second), during which only Admins are allowed to send messages, 0 or less than the current time means no banning, -1 means banned permanently                                          |
| ⇥ capacity                 | int64   | GroupCapacity                                                                                                                                                                                           |
| ⇥ count                    | int64   | Current count of group member                                                                                                                                                                           |
| ⇥ created\_at              | int64   | Creation time(milliseconds)                                                                                                                                                                             |
| ⇥ description              | string  | Group description                                                                                                                                                                                       |
| ⇥ ext                      | string  | Group extension information                                                                                                                                                                             |
| ⇥ group\_id                | int64   | Group id                                                                                                                                                                                                |
| ⇥ history\_visible         | boolean | History chat visibility settings for new members: true - New members can see chat history, false - New members invisible chat history                                                                   |
| ⇥ member\_invite           | boolean | Whether to allow group members to invite others into the group: true - Group members are allowed to invite others into the group, false - Group members are not allowed to invite others into the group |
| ⇥ member\_modify           | boolean | Group members modify group information settings: true - Allow group members to modify group information, false - Do not allow group members to modify group information                                 |
| ⇥ msg\_mute\_mode          | int32   | Group message blocking mode: 0 - not blocking, 1 - blocking local message notifications, 2 - blocking messages, not receiving messages                                                                  |
| ⇥ msg\_push\_mode          | int32   | Group message push mode: 0 - receive all pushes, 1 - not accept pushes, 2 - receive admin and @message pushes, 3 - only receive admin pushes, 4 - only receive @message pushes                          |
| ⇥ name                     | string  | Group name                                                                                                                                                                                              |
| ⇥ owner\_id                | int64   | Group Owner id                                                                                                                                                                                          |
| ⇥ read\_ack                | boolean | Whether to enable the read function of group messages: true - enable the read function of group messages, false - disable the read function of group messages                                           |
| ⇥ status                   | int32   | Group state, 0: normal, 1: dissolved                                                                                                                                                                    |
| ⇥ type                     | int32   | Group type: 0 - private group, 2 - chatroom                                                                                                                                                             |
| ⇥ updated\_at              | int64   | Update time(milliseconds)                                                                                                                                                                               |
| message                    | string  | Error information, null means success                                                                                                                                                                   |
| #### Interface Description |         |                                                                                                                                                                                                         |

>

## 4.17 Disband group{#delete\_\_group\_destroy}

> DELETE /group/destroy

> POST /group/destroy

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| group\_id      | int64     | true     | GroupID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.18 Update group profile{#put\_\_group\_display\_name}

> PUT /group/display\_name

> POST /group/display\_name

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description    |
| -------------- | --------- | -------- | ------- | -------------- |
| group\_id      | int64     | true     |         | Group id       |
| value          | string    | true     |         | Update content |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.19 Download group file{#get\_\_group\_file}

> GET /group/file

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| file\_id       | int64     | true     | FileID      |
| group\_id      | int64     | true     | GroupID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                           |
| -------------------------- | ------ | ------------------------------------- |
| code                       | int32  | Return code, 200 is success           |
| data                       | object | Result data                           |
| ⇥ created\_at              | int64  | Creation time(milliseconds)           |
| ⇥ file\_id                 | int64  | Shared file id                        |
| ⇥ group\_id                | int64  | Group id                              |
| ⇥ name                     | string | Shared file name                      |
| ⇥ size                     | int64  | Shared file size                      |
| ⇥ type                     | string | Shared file type                      |
| ⇥ updated\_at              | int64  | Update time(milliseconds)             |
| ⇥ uploader                 | int64  | Shared file uploader                  |
| ⇥ url                      | string | Shared file url                       |
| message                    | string | Error information, null means success |
| #### Interface Description |        |                                       |

>

## 4.20 Delete group file{#delete\_\_group\_file\_delete}

> DELETE /group/file/delete

> POST /group/file/delete

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description  |
| -------------- | ------------- | -------- | ------- | ------------ |
| file\_list     | array\[int64] | true     |         | File id list |
| group\_id      | int64         | true     |         | Group id     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ file\_id                 | int64          | FileID                                |
| ⇥ reason                   | string         | Reason                                |
| ⇥ result                   | string         | Result: success/fail                  |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 4.21 Get the list of group files{#get\_\_group\_file\_list}

> GET /group/file/list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| group\_id      | int64     | true     | GroupID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ created\_at              | int64          | Creation time(milliseconds)           |
| ⇥ file\_id                 | int64          | Shared file id                        |
| ⇥ group\_id                | int64          | Group id                              |
| ⇥ name                     | string         | Shared file name                      |
| ⇥ size                     | int64          | Shared file size                      |
| ⇥ type                     | string         | Shared file type                      |
| ⇥ updated\_at              | int64          | Update time(milliseconds)             |
| ⇥ uploader                 | int64          | Shared file uploader                  |
| ⇥ url                      | string         | Shared file url                       |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 4.22 Update group file name{#put\_\_group\_file\_update\_name}

> PUT /group/file/update\_name

> POST /group/file/update\_name

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description   |
| -------------- | --------- | -------- | ------- | ------------- |
| file\_id       | int64     | true     |         | File id       |
| group\_id      | int64     | true     |         | Group id      |
| name           | string    | true     |         | New file name |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.23 Upload group file{#post\_\_group\_file\_upload}

> POST /group/file/upload

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description |
| -------------- | --------- | -------- | ------- | ----------- |
| group\_id      | int64     | true     |         | Group id    |
| name           | string    | true     |         | File name   |
| size           | int64     | true     |         | File size   |
| type           | string    | false    |         | File type   |
| url            | string    | true     |         | File url    |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                           |
| -------------------------- | ------ | ------------------------------------- |
| code                       | int32  | Return code, 200 is success           |
| data                       | object | Result data                           |
| ⇥ created\_at              | int64  | Creation time(milliseconds)           |
| ⇥ file\_id                 | int64  | Shared file id                        |
| ⇥ group\_id                | int64  | Group id                              |
| ⇥ name                     | string | Shared file name                      |
| ⇥ size                     | int64  | Shared file size                      |
| ⇥ type                     | string | Shared file type                      |
| ⇥ updated\_at              | int64  | Update time(milliseconds)             |
| ⇥ uploader                 | int64  | Shared file uploader                  |
| ⇥ url                      | string | Shared file url                       |
| message                    | string | Error information, null means success |
| #### Interface Description |        |                                       |

>

## 4.24 Get group information by group id{#get\_\_group\_info}

> GET /group/info

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| group\_id      | int64     | true     | GroupID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                                                                                                                                                                                             |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                       | int32   | Return code, 200 is success                                                                                                                                                                             |
| data                       | object  | Result data                                                                                                                                                                                             |
| ⇥ apply\_approval          | int32   | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests                                                                                         |
| ⇥ avatar                   | string  | Group avatar                                                                                                                                                                                            |
| ⇥ ban\_expire\_time        | int64   | Expiration time (second), during which only Admins are allowed to send messages, 0 or less than the current time means no banning, -1 means banned permanently                                          |
| ⇥ capacity                 | int64   | GroupCapacity                                                                                                                                                                                           |
| ⇥ count                    | int64   | Current count of group member                                                                                                                                                                           |
| ⇥ created\_at              | int64   | Creation time(milliseconds)                                                                                                                                                                             |
| ⇥ description              | string  | Group description                                                                                                                                                                                       |
| ⇥ ext                      | string  | Group extension information                                                                                                                                                                             |
| ⇥ group\_id                | int64   | Group id                                                                                                                                                                                                |
| ⇥ history\_visible         | boolean | History chat visibility settings for new members: true - New members can see chat history, false - New members invisible chat history                                                                   |
| ⇥ member\_invite           | boolean | Whether to allow group members to invite others into the group: true - Group members are allowed to invite others into the group, false - Group members are not allowed to invite others into the group |
| ⇥ member\_modify           | boolean | Group members modify group information settings: true - Allow group members to modify group information, false - Do not allow group members to modify group information                                 |
| ⇥ msg\_mute\_mode          | int32   | Group message blocking mode: 0 - not blocking, 1 - blocking local message notifications, 2 - blocking messages, not receiving messages                                                                  |
| ⇥ msg\_push\_mode          | int32   | Group message push mode: 0 - receive all pushes, 1 - not accept pushes, 2 - receive admin and @message pushes, 3 - only receive admin pushes, 4 - only receive @message pushes                          |
| ⇥ name                     | string  | Group name                                                                                                                                                                                              |
| ⇥ owner\_id                | int64   | Group Owner id                                                                                                                                                                                          |
| ⇥ read\_ack                | boolean | Whether to enable the read function of group messages: true - enable the read function of group messages, false - disable the read function of group messages                                           |
| ⇥ status                   | int32   | Group state, 0: normal, 1: dissolved                                                                                                                                                                    |
| ⇥ type                     | int32   | Group type: 0 - private group, 2 - chatroom                                                                                                                                                             |
| ⇥ updated\_at              | int64   | Update time(milliseconds)                                                                                                                                                                               |
| message                    | string  | Error information, null means success                                                                                                                                                                   |
| #### Interface Description |         |                                                                                                                                                                                                         |

>

## 4.25 Update group avatar{#put\_\_group\_info\_avatar}

> PUT /group/info/avatar

> POST /group/info/avatar

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description    |
| -------------- | --------- | -------- | ------- | -------------- |
| group\_id      | int64     | true     |         | Group id       |
| value          | string    | true     |         | Update content |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.26 Get group information by group id{#post\_\_group\_info\_batch}

> POST /group/info/batch

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description   |
| -------------- | ------------- | -------- | ------- | ------------- |
| group\_list    | array\[int64] | true     |         | Group id list |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                                                                                                                                                                    |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| code                       | int32          | Return code, 200 is success                                                                                                                                                    |
| data                       | array\[object] | Result data                                                                                                                                                                    |
| ⇥ apply\_approval          | int32          | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests                                                                |
| ⇥ avatar                   | string         | Group avatar                                                                                                                                                                   |
| ⇥ capacity                 | int64          | GroupCapacity                                                                                                                                                                  |
| ⇥ count                    | int64          | Current count of group member                                                                                                                                                  |
| ⇥ group\_id                | int64          | GroupID                                                                                                                                                                        |
| ⇥ msg\_mute\_mode          | int32          | Group message blocking mode: 0 - not blocking, 1 - blocking local message notifications, 2 - blocking messages, not receiving messages                                         |
| ⇥ msg\_push\_mode          | int32          | Group message push mode: 0 - receive all pushes, 1 - not accept pushes, 2 - receive admin and @message pushes, 3 - only receive admin pushes, 4 - only receive @message pushes |
| ⇥ name                     | string         | Group name                                                                                                                                                                     |
| ⇥ owner                    | int64          | Group Owner id                                                                                                                                                                 |
| ⇥ status                   | int32          | Group state, 0: normal, 1: dissolved                                                                                                                                           |
| ⇥ type                     | int32          | Group type: 0 - private group, 2 - chatroom                                                                                                                                    |
| message                    | string         | Error information, null means success                                                                                                                                          |
| #### Interface Description |                |                                                                                                                                                                                |

>

## 4.27 Update group description{#put\_\_group\_info\_description}

> PUT /group/info/description

> POST /group/info/description

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description    |
| -------------- | --------- | -------- | ------- | -------------- |
| group\_id      | int64     | true     |         | Group id       |
| value          | string    | true     |         | Update content |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.28 Update extension information{#put\_\_group\_info\_ext}

> PUT /group/info/ext

> POST /group/info/ext

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description    |
| -------------- | --------- | -------- | ------- | -------------- |
| group\_id      | int64     | true     |         | Group id       |
| value          | string    | true     |         | Update content |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.29 Update group name{#put\_\_group\_info\_name}

> PUT /group/info/name

> POST /group/info/name

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description    |
| -------------- | --------- | -------- | ------- | -------------- |
| group\_id      | int64     | true     |         | Group id       |
| value          | string    | true     |         | Update content |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.30 Get group invitation list{#get\_\_group\_invitation\_list}

> GET /group/invitation\_list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                     |
| -------------- | --------- | -------- | ------------------------------- |
| cursor         | string    | false    | Cursor: where to start fetching |
| limit          | int32     | false    | How many to fetch               |
| version        | int64     | false    | Version                         |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                                             |
| -------------------------- | -------------- | ------------------------------------------------------- |
| code                       | int32          | Return code, 200 is success                             |
| cursor                     | string         | Cursor for page turning                                 |
| data                       | array\[object] | Result data                                             |
| ⇥ expired\_time            | int64          | Expiration timestamp(milliseconds)                      |
| ⇥ group\_id                | int64          | GroupID                                                 |
| ⇥ invitee\_id              | int64          | Invitee ID                                              |
| ⇥ inviter\_id              | int64          | Inviter ID                                              |
| ⇥ reason                   | string         | Reason                                                  |
| ⇥ status                   | int32          | Status: 0 - Pending, 1 - User agreed, 2 - User rejected |
| ⇥ updated\_at              | string         | Update time                                             |
| message                    | string         | Error information, null means success                   |
| total                      | int64          | Total                                                   |
| version                    | int64          | Version, not used at present, reserved for extension    |
| #### Interface Description |                |                                                         |

>

## 4.31 Invite to group{#post\_\_group\_invite}

> POST /group/invite

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description                                                                 |
| -------------- | ------------- | -------- | ------- | --------------------------------------------------------------------------- |
| group\_id      | int64         | true     |         | Group id                                                                    |
| reason         | string        | false    |         | Invitation reason                                                           |
| user\_list     | array\[int64] | true     |         | Invitee id, List type, multiple users can be invited to a group at one time |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ reason                   | string         | Error message                         |
| ⇥ result                   | string         | Operation result: success/fail        |
| ⇥ user\_id                 | int64          | User ID                               |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 4.32 Process group invitation by user{#put\_\_group\_invite\_handle}

> PUT /group/invite/handle

> POST /group/invite/handle

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description                                                 |
| -------------- | --------- | -------- | ------- | ----------------------------------------------------------- |
| approval       | boolean   | true     |         | Approval, bool type, true for approval, false for rejection |
| group\_id      | int64     | true     |         | Group id                                                    |
| user\_id       | int64     | true     |         | User id                                                     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.33 Kick member out of group{#delete\_\_group\_kick}

> DELETE /group/kick

> POST /group/kick

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description  |
| -------------- | ------------- | -------- | ------- | ------------ |
| group\_id      | int64         | true     |         | Group id     |
| user\_list     | array\[int64] | true     |         | User id list |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ reason                   | string         | Error message                         |
| ⇥ result                   | string         | Operation result: success/fail        |
| ⇥ user\_id                 | int64          | User ID                               |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 4.34 Member quit group{#delete\_\_group\_leave}

> DELETE /group/leave

> POST /group/leave

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| group\_id      | int64     | true     | GroupID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.35 Get group member list by group id{#get\_\_group\_member\_list}

> GET /group/member\_list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                    |
| -------------- | --------- | -------- | ------------------------------ |
| cursor         | string    | false    | Cursor:where to start fetching |
| group\_id      | int64     | true     | GroupID                        |
| limit          | int32     | false    | How many to fetch              |
| version        | int64     | false    | Version                        |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                                          |
| -------------------------- | -------------- | ---------------------------------------------------- |
| code                       | int32          | Return code, 200 is success                          |
| cursor                     | string         | Cursor for page turning                              |
| data                       | array\[object] | Result data                                          |
| ⇥ display\_name            | string         | Group member profile                                 |
| ⇥ expired\_time            | int64          | BanExpiration time(milliseconds)                     |
| ⇥ join\_time               | int64          | Member join time(milliseconds)                       |
| ⇥ user\_id                 | int64          | User id                                              |
| message                    | string         | Error information, null means success                |
| total                      | int64          | Total                                                |
| version                    | int64          | Version, not used at present, reserved for extension |
| #### Interface Description |                |                                                      |

>

## 4.36 Batch retrieval of group member profiles{#post\_\_group\_members\_display\_name}

> POST /group/members/display\_name

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description  |
| -------------- | ------------- | -------- | ------- | ------------ |
| group\_id      | int64         | true     |         | Group id     |
| user\_list     | array\[int64] | true     |         | User id list |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ display\_name            | string         | Group member profile                  |
| ⇥ expired\_time            | int64          | BanExpiration time(milliseconds)      |
| ⇥ join\_time               | int64          | Member join time(milliseconds)        |
| ⇥ user\_id                 | int64          | User id                               |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 4.37 Set group message blocking mode{#put\_\_group\_msg\_mute\_mode}

> PUT /group/msg/mute\_mode

> POST /group/msg/mute\_mode

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name  | Data Type | Required | Default | Description                                                                                                            |
| --------------- | --------- | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------- |
| group\_id       | int64     | true     |         | Group id                                                                                                               |
| msg\_mute\_mode | int32     | true     |         | Group message blocking mode: 0 - No blocking1 - Block local message notification2 - Block message, no message received |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                           |
| -------------------------- | ------ | ------------------------------------- |
| code                       | int32  | Return code, 200 is success           |
| data                       | object | Result data                           |
| message                    | string | Error information, null means success |
| #### Interface Description |        |                                       |

>

## 4.38 Set group message pushing mode{#put\_\_group\_msg\_push\_mode}

> PUT /group/msg/push\_mode

> POST /group/msg/push\_mode

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name  | Data Type | Required | Default | Description                                                                                                                                                  |
| --------------- | --------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| group\_id       | int64     | true     |         | Group id                                                                                                                                                     |
| msg\_push\_mode | int32     | true     |         | Group message push type: 0: Receive all pushes; 1: Do not accept push; 2: Receive Admin and @ pushes; 3. Only receive Admin pushes; 4: Only receive @ pushes |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                           |
| -------------------------- | ------ | ------------------------------------- |
| code                       | int32  | Return code, 200 is success           |
| data                       | object | Result data                           |
| message                    | string | Error information, null means success |
| #### Interface Description |        |                                       |

>

## 4.39 Get public group list(Deprecated){#get\_\_group\_public\_list}

> GET /group/public\_list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type          | Description                           |
| -------------------------- | ------------- | ------------------------------------- |
| code                       | int32         | Return code, 200 is success           |
| data                       | array\[int64] | Result data                           |
| message                    | string        | Error information, null means success |
| #### Interface Description |               |                                       |

>

## 4.40 Group invitation via QR code{#post\_\_group\_qrcode\_invite}

> POST /group/qrcode/invite

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description                                                      |
| -------------- | --------- | -------- | ------- | ---------------------------------------------------------------- |
| qr\_info       | string    | true     |         | QR code information:It can be obtained by GET /group/qrcode/sign |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                           |
| -------------------------- | ------ | ------------------------------------- |
| code                       | int32  | Return code, 200 is success           |
| data                       | object | Result data                           |
| message                    | string | Error information, null means success |
| #### Interface Description |        |                                       |

>

## 4.41 Get Group invitation QR code{#get\_\_group\_qrcode\_sign}

> GET /group/qrcode/sign

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| group\_id      | int64     | true     | GroupID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                           |
| -------------------------- | ------ | ------------------------------------- |
| code                       | int32  | Return code, 200 is success           |
| data                       | object | Result data                           |
| ⇥ create\_at               | int64  | QR code generation time(milliseconds) |
| ⇥ expire\_at               | int64  | QR code expiration time(milliseconds) |
| ⇥ qr\_info                 | string | QR code information                   |
| message                    | string | Error information, null means success |
| #### Interface Description |        |                                       |

>

## 4.42 Get group settings{#get\_\_group\_settings}

> GET /group/settings

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| group\_id      | int64     | true     | GroupID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                                                                                                                                                                                             |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                       | int32   | Return code, 200 is success                                                                                                                                                                             |
| data                       | object  | Result data                                                                                                                                                                                             |
| ⇥ apply\_approval          | int32   | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests                                                                                         |
| ⇥ avatar                   | string  | Group avatar                                                                                                                                                                                            |
| ⇥ ban\_expire\_time        | int64   | Expiration time (second), during which only Admins are allowed to send messages, 0 or less than the current time means no banning, -1 means banned permanently                                          |
| ⇥ capacity                 | int64   | GroupCapacity                                                                                                                                                                                           |
| ⇥ count                    | int64   | Current count of group member                                                                                                                                                                           |
| ⇥ created\_at              | int64   | Creation time(milliseconds)                                                                                                                                                                             |
| ⇥ description              | string  | Group description                                                                                                                                                                                       |
| ⇥ ext                      | string  | Group extension information                                                                                                                                                                             |
| ⇥ group\_id                | int64   | Group id                                                                                                                                                                                                |
| ⇥ history\_visible         | boolean | History chat visibility settings for new members: true - New members can see chat history, false - New members invisible chat history                                                                   |
| ⇥ member\_invite           | boolean | Whether to allow group members to invite others into the group: true - Group members are allowed to invite others into the group, false - Group members are not allowed to invite others into the group |
| ⇥ member\_modify           | boolean | Group members modify group information settings: true - Allow group members to modify group information, false - Do not allow group members to modify group information                                 |
| ⇥ msg\_mute\_mode          | int32   | Group message blocking mode: 0 - not blocking, 1 - blocking local message notifications, 2 - blocking messages, not receiving messages                                                                  |
| ⇥ msg\_push\_mode          | int32   | Group message push mode: 0 - receive all pushes, 1 - not accept pushes, 2 - receive admin and @message pushes, 3 - only receive admin pushes, 4 - only receive @message pushes                          |
| ⇥ name                     | string  | Group name                                                                                                                                                                                              |
| ⇥ owner\_id                | int64   | Group Owner id                                                                                                                                                                                          |
| ⇥ read\_ack                | boolean | Whether to enable the read function of group messages: true - enable the read function of group messages, false - disable the read function of group messages                                           |
| ⇥ status                   | int32   | Group state, 0: normal, 1: dissolved                                                                                                                                                                    |
| ⇥ type                     | int32   | Group type: 0 - private group, 2 - chatroom                                                                                                                                                             |
| ⇥ updated\_at              | int64   | Update time(milliseconds)                                                                                                                                                                               |
| message                    | string  | Error information, null means success                                                                                                                                                                   |
| #### Interface Description |         |                                                                                                                                                                                                         |

>

## 4.43 Update group settings - whether to allow member invitations{#put\_\_group\_settings\_allow\_member\_invitation}

> PUT /group/settings/allow\_member\_invitation

> POST /group/settings/allow\_member\_invitation

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description    |
| -------------- | --------- | -------- | ------- | -------------- |
| group\_id      | int64     | true     |         | Group id       |
| value          | boolean   | true     |         | Update content |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.44 Update group settings - whether group members can modify group information{#put\_\_group\_settings\_allow\_member\_modify}

> PUT /group/settings/allow\_member\_modify

> POST /group/settings/allow\_member\_modify

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description    |
| -------------- | --------- | -------- | ------- | -------------- |
| group\_id      | int64     | true     |         | Group id       |
| value          | boolean   | true     |         | Update content |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.45 Ban all members, only Admins can send messages{#post\_\_group\_settings\_ban\_all}

> POST /group/settings/ban\_all

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description                   |
| -------------- | --------- | -------- | ------- | ----------------------------- |
| duration       | int64     | true     |         | Duration of banned in minutes |
| group\_id      | int64     | true     |         | Group id                      |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                                                                                                                                                    |
| -------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                       | int32  | Return code, 200 is success                                                                                                                                    |
| data                       | object | Result data                                                                                                                                                    |
| ⇥ ban\_expire\_time        | int64  | Expiration time (second), during which only Admins are allowed to send messages, 0 or less than the current time means no banning, -1 means banned permanently |
| message                    | string | Error information, null means success                                                                                                                          |
| #### Interface Description |        |                                                                                                                                                                |

>

## 4.46 Update group settings - whether to enable “mark after read”{#put\_\_group\_settings\_enable\_read\_ack}

> PUT /group/settings/enable\_read\_ack

> POST /group/settings/enable\_read\_ack

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description    |
| -------------- | --------- | -------- | ------- | -------------- |
| group\_id      | int64     | true     |         | Group id       |
| value          | boolean   | true     |         | Update content |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.47 Update group settings - whether group chat history visible to new members{#put\_\_group\_settings\_history\_visible}

> PUT /group/settings/history\_visible

> POST /group/settings/history\_visible

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description    |
| -------------- | --------- | -------- | ------- | -------------- |
| group\_id      | int64     | true     |         | Group id       |
| value          | boolean   | true     |         | Update content |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.48 Update group settings - whether group membership request needs Admin approval{#put\_\_group\_settings\_require\_admin\_approval}

> PUT /group/settings/require\_admin\_approval

> POST /group/settings/require\_admin\_approval

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name  | Data Type | Required | Default | Description                                                                                                     |
| --------------- | --------- | -------- | ------- | --------------------------------------------------------------------------------------------------------------- |
| apply\_approval | int32     | true     |         | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests |
| group\_id       | int64     | true     |         | Group id                                                                                                        |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.49 Unban all members{#post\_\_group\_settings\_unban\_all}

> POST /group/settings/unban\_all

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description |
| -------------- | --------- | -------- | ------- | ----------- |
| group\_id      | int64     | true     |         | Group id    |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 4.50 Transfer of group Owner{#put\_\_group\_transfer}

> PUT /group/transfer

> POST /group/transfer

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description                 |
| -------------- | --------- | -------- | ------- | --------------------------- |
| group\_id      | int64     | true     |         | Group id                    |
| new\_owner     | int64     | true     |         | User\_id of new group Owner |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                           |
| -------------------------- | ------ | ------------------------------------- |
| code                       | int32  | Return code, 200 is success           |
| data                       | object | Result data                           |
| ⇥ reason                   | string | Error message                         |
| ⇥ result                   | string | Operation result: success/fail        |
| ⇥ user\_id                 | int64  | User ID                               |
| message                    | string | Error information, null means success |
| #### Interface Description |        |                                       |

>

## 4.51 Remove user from ban list{#post\_\_group\_unban}

> POST /group/unban

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description  |
| -------------- | ------------- | -------- | ------- | ------------ |
| group\_id      | int64         | true     |         | Group id     |
| user\_list     | array\[int64] | true     |         | User id list |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ reason                   | string         | Error message                         |
| ⇥ result                   | string         | Operation result: success/fail        |
| ⇥ user\_id                 | int64          | User ID                               |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 4.52 Remove user from blacklist{#delete\_\_group\_unblock}

> DELETE /group/unblock

> POST /group/unblock

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description  |
| -------------- | ------------- | -------- | ------- | ------------ |
| group\_id      | int64         | true     |         | Group id     |
| user\_list     | array\[int64] | true     |         | User id list |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ reason                   | string         | Error message                         |
| ⇥ result                   | string         | Operation result: success/fail        |
| ⇥ user\_id                 | int64          | User ID                               |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 4.53 Get the list of groups for the user{#get\_\_group\_user\_joined}

> GET /group/user\_joined

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type          | Description                           |
| -------------------------- | ------------- | ------------------------------------- |
| code                       | int32         | Return code, 200 is success           |
| data                       | array\[int64] | Result data                           |
| message                    | string        | Error information, null means success |
| #### Interface Description |               |                                       |

>
