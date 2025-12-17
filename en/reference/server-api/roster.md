# 3 Friend management interface{#roster}

## 3.1 Agree to add friend{#put\_\_roster\_accept}

> PUT /roster/accept

> POST /roster/accept

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                           |
| -------------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------- |
| access-token   | string    | false    | Token                                                                                                                 |
| app\_id        | string    | true     | App ID                                                                                                                |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |

#### Query Param

| Parameter name | Data Type | Required | Description     |
| -------------- | --------- | -------- | --------------- |
| user\_id       | int64     | true     | Consent user ID |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 3.2 Apply to add friend{#post\_\_roster\_apply}

> POST /roster/apply

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description         |
| -------------- | --------- | -------- | ------- | ------------------- |
| alias          | string    | false    |         | Name in comment     |
| auth\_answer   | string    | false    |         | Answer of question  |
| reason         | string    | false    |         | Request description |
| user\_id       | int64     | true     |         | Invitee ID          |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 3.3 Add friends in batch{#post\_\_roster\_apply\_batch}

> POST /roster/apply/batch

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type      | Required | Default | Description         |
| -------------- | -------------- | -------- | ------- | ------------------- |
|                | array\[object] | true     |         | rosterApplications  |
| ⇥ alias        | string         | false    |         | Name in comment     |
| ⇥ reason       | string         | false    |         | Request description |
| ⇥ user\_id     | int64          | true     |         | Invitee ID          |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | object         | Result data                           |
| ⇥ fails                    | array\[object] | list of failure messages              |
| ⇥⇥ reason                  | string         | Cause of failure                      |
| ⇥⇥ user\_id                | int64          | User ID                               |
| ⇥ success                  | array\[int64]  | List of successful user IDs           |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 3.4 List of friend requests{#get\_\_roster\_apply\_list}

> GET /roster/apply/list

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
| cursor         | string    | false    | Cursor: Where to start fetching |
| limit          | int32     | false    | How many to fetch               |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                                                                |
| -------------------------- | -------------- | -------------------------------------------------------------------------- |
| code                       | int32          | Return code, 200 is success                                                |
| cursor                     | string         | Cursor, no cursor in returned result means the last page has been returned |
| data                       | array\[object] | Result data                                                                |
| ⇥ expired\_time            | int64          | Expiration timestamp(milliseconds)                                         |
| ⇥ reason                   | string         | Request description                                                        |
| ⇥ status                   | int32          | Status: 0 - waiting for confirmation, 1 - accepted, 2 - rejected           |
| ⇥ user\_id                 | int64          | User ID that initiate adding friend                                        |
| message                    | string         | Error information, null means success                                      |
| version                    | int64          | Version                                                                    |
| #### Interface Description |                |                                                                            |

>

## 3.5 Add to blacklist{#put\_\_roster\_block}

> PUT /roster/block

> POST /roster/block

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                           |
| -------------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------- |
| access-token   | string    | false    | Token                                                                                                                 |
| app\_id        | string    | true     | App ID                                                                                                                |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| user\_id       | int64     | true     | User ID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 3.6 List of blacklists{#get\_\_roster\_blocked\_list}

> GET /roster/blocked\_list

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

## 3.7 Reject friend request{#put\_\_roster\_decline}

> PUT /roster/decline

> POST /roster/decline

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
| reason         | string    | false    |         | Reason for rejection |
| user\_id       | int64     | true     |         | Rejected user ID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 3.8 Delete friend{#delete\_\_roster\_delete}

> DELETE /roster/delete

> POST /roster/delete

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                           |
| -------------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------- |
| access-token   | string    | false    | Token                                                                                                                 |
| app\_id        | string    | true     | App ID                                                                                                                |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| user\_id       | int64     | true     | User ID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 3.9 Update friend extension information{#put\_\_roster\_ext}

> PUT /roster/ext

> POST /roster/ext

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name     | Data Type | Required | Default | Description                                                                                           |
| ------------------ | --------- | -------- | ------- | ----------------------------------------------------------------------------------------------------- |
| alias              | string    | false    |         | Name in comment                                                                                       |
| ext                | string    | false    |         | Extension information                                                                                 |
| mute\_notification | boolean   | false    |         | Mute message notification: true - mute message notification, false - do not mute message notification |
| user\_id           | int64     | true     |         | Friend user ID                                                                                        |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 3.10 Search for users by ID{#get\_\_roster\_id}

> GET /roster/id

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                           |
| -------------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------- |
| access-token   | string    | false    | Token                                                                                                                 |
| app\_id        | string    | true     | App ID                                                                                                                |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| user\_id       | int64     | true     | User ID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                                                                                                                                                                                                               |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                       | int32   | Return code, 200 is success                                                                                                                                                                                               |
| data                       | object  | Result data                                                                                                                                                                                                               |
| ⇥ alias                    | string  | Name in comment                                                                                                                                                                                                           |
| ⇥ auth\_mode               | int32   | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
| ⇥ auth\_question           | string  | Verification question                                                                                                                                                                                                     |
| ⇥ avatar                   | string  | Avatar                                                                                                                                                                                                                    |
| ⇥ description              | string  | Description                                                                                                                                                                                                               |
| ⇥ ext                      | string  | Extension information                                                                                                                                                                                                     |
| ⇥ mute\_notification       | boolean | Mute message notification: true - mute message notification, false - do not mute message notification                                                                                                                     |
| ⇥ nick\_name               | string  | Nickname or name                                                                                                                                                                                                          |
| ⇥ public\_info             | string  | Public information, visible to both friends and strangers                                                                                                                                                                 |
| ⇥ relation                 | int32   | Relationships: 0 - friend, 1 - deleted friend, 2 - stranger, 3 - blacklist                                                                                                                                                |
| ⇥ user\_id                 | int64   | Friend user ID                                                                                                                                                                                                            |
| ⇥ username                 | string  | Username                                                                                                                                                                                                                  |
| message                    | string  | Error information, null means success                                                                                                                                                                                     |
| #### Interface Description |         |                                                                                                                                                                                                                           |

>

## 3.11 List of friends{#get\_\_roster\_list}

> GET /roster/list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                    |
| -------------- | --------- | -------- | ------------------------------ |
| cursor         | string    | false    | Cursor:where to start fetching |
| limit          | int32     | false    | How many to fetch              |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type          | Description                                                                |
| -------------------------- | ------------- | -------------------------------------------------------------------------- |
| code                       | int32         | Return code, 200 is success                                                |
| cursor                     | string        | Cursor, no cursor in returned result means the last page has been returned |
| data                       | array\[int64] | Result data                                                                |
| message                    | string        | Error information, null means success                                      |
| version                    | int64         | Version                                                                    |
| #### Interface Description |               |                                                                            |

>

## 3.12 List of friend details{#post\_\_roster\_list}

> POST /roster/list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description     |
| -------------- | ------------- | -------- | ------- | --------------- |
| list           | array\[int64] | true     |         | Friends ID list |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                                                                                                                                                                                                               |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                       | int32          | Return code, 200 is success                                                                                                                                                                                               |
| data                       | array\[object] | Result data                                                                                                                                                                                                               |
| ⇥ alias                    | string         | Name in comment                                                                                                                                                                                                           |
| ⇥ auth\_mode               | int32          | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
| ⇥ auth\_question           | string         | Verification question                                                                                                                                                                                                     |
| ⇥ avatar                   | string         | Avatar                                                                                                                                                                                                                    |
| ⇥ description              | string         | Description                                                                                                                                                                                                               |
| ⇥ ext                      | string         | Extension information                                                                                                                                                                                                     |
| ⇥ mute\_notification       | boolean        | Mute message notification: true - mute message notification, false - do not mute message notification                                                                                                                     |
| ⇥ nick\_name               | string         | Nickname or name                                                                                                                                                                                                          |
| ⇥ public\_info             | string         | Public information, visible to both friends and strangers                                                                                                                                                                 |
| ⇥ relation                 | int32          | Relationships: 0 - friend, 1 - deleted friend, 2 - stranger, 3 - blacklist                                                                                                                                                |
| ⇥ user\_id                 | int64          | Friend user ID                                                                                                                                                                                                            |
| ⇥ username                 | string         | Username                                                                                                                                                                                                                  |
| message                    | string         | Error information, null means success                                                                                                                                                                                     |
| #### Interface Description |                |                                                                                                                                                                                                                           |

>

## 3.13 Whether to allow messaging{#get\_\_roster\_may\_message}

> GET /roster/may\_message

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                           |
| -------------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------- |
| access-token   | string    | false    | Token                                                                                                                 |
| app\_id        | string    | true     | App ID                                                                                                                |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| roster\_id     | int64     | true     | Friend ID   |
| user\_id       | int64     | true     | User ID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 3.14 Search for user by mobile number{#get\_\_roster\_mobile}

> GET /roster/mobile

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description   |
| -------------- | --------- | -------- | ------------- |
| mobile         | string    | true     | Mobile number |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                                                                                                                                                                                                               |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                       | int32   | Return code, 200 is success                                                                                                                                                                                               |
| data                       | object  | Result data                                                                                                                                                                                                               |
| ⇥ alias                    | string  | Name in comment                                                                                                                                                                                                           |
| ⇥ auth\_mode               | int32   | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
| ⇥ auth\_question           | string  | Verification question                                                                                                                                                                                                     |
| ⇥ avatar                   | string  | Avatar                                                                                                                                                                                                                    |
| ⇥ description              | string  | Description                                                                                                                                                                                                               |
| ⇥ ext                      | string  | Extension information                                                                                                                                                                                                     |
| ⇥ mute\_notification       | boolean | Mute message notification: true - mute message notification, false - do not mute message notification                                                                                                                     |
| ⇥ nick\_name               | string  | Nickname or name                                                                                                                                                                                                          |
| ⇥ public\_info             | string  | Public information, visible to both friends and strangers                                                                                                                                                                 |
| ⇥ relation                 | int32   | Relationships: 0 - friend, 1 - deleted friend, 2 - stranger, 3 - blacklist                                                                                                                                                |
| ⇥ user\_id                 | int64   | Friend user ID                                                                                                                                                                                                            |
| ⇥ username                 | string  | Username                                                                                                                                                                                                                  |
| message                    | string  | Error information, null means success                                                                                                                                                                                     |
| #### Interface Description |         |                                                                                                                                                                                                                           |

>

## 3.15 Search for user by user ID{#get\_\_roster\_name}

> GET /roster/name

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| username       | string    | true     | Username    |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                                                                                                                                                                                                               |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                       | int32   | Return code, 200 is success                                                                                                                                                                                               |
| data                       | object  | Result data                                                                                                                                                                                                               |
| ⇥ alias                    | string  | Name in comment                                                                                                                                                                                                           |
| ⇥ auth\_mode               | int32   | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
| ⇥ auth\_question           | string  | Verification question                                                                                                                                                                                                     |
| ⇥ avatar                   | string  | Avatar                                                                                                                                                                                                                    |
| ⇥ description              | string  | Description                                                                                                                                                                                                               |
| ⇥ ext                      | string  | Extension information                                                                                                                                                                                                     |
| ⇥ mute\_notification       | boolean | Mute message notification: true - mute message notification, false - do not mute message notification                                                                                                                     |
| ⇥ nick\_name               | string  | Nickname or name                                                                                                                                                                                                          |
| ⇥ public\_info             | string  | Public information, visible to both friends and strangers                                                                                                                                                                 |
| ⇥ relation                 | int32   | Relationships: 0 - friend, 1 - deleted friend, 2 - stranger, 3 - blacklist                                                                                                                                                |
| ⇥ user\_id                 | int64   | Friend user ID                                                                                                                                                                                                            |
| ⇥ username                 | string  | Username                                                                                                                                                                                                                  |
| message                    | string  | Error information, null means success                                                                                                                                                                                     |
| #### Interface Description |         |                                                                                                                                                                                                                           |

>

## 3.16 Remove from blacklist{#delete\_\_roster\_unblock}

> DELETE /roster/unblock

> POST /roster/unblock

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                           |
| -------------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------- |
| access-token   | string    | false    | Token                                                                                                                 |
| app\_id        | string    | true     | App ID                                                                                                                |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |

#### Query Param

| Parameter name | Data Type | Required | Description |
| -------------- | --------- | -------- | ----------- |
| user\_id       | int64     | true     | User ID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>
