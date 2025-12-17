# 1 User action{#user}

## 1.1 Set how to validate when adding friend{#put\_\_user\_authmode}

> PUT /user/authmode

> POST /user/authmode

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                                                                                                                                                                                                               |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| value          | int32     | true     | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.2 Set avatar{#put\_\_user\_avatar}

> PUT /user/avatar

> POST /user/avatar

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
| avatar         | string    | true     |         | Avatar url  |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.3 Set avatar in batch{#put\_\_user\_avatar\_batch}

> PUT /user/avatar/batch

> POST /user/avatar/batch

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type      | Required | Default | Description |
| -------------- | -------------- | -------- | ------- | ----------- |
| list           | array\[object] | false    |         |             |
| ⇥ avatar       | string         | true     |         | Avatar url  |
| ⇥ user\_id     | int64          | true     |         | User ID     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ reason                   | string         | Cause of failure                      |
| ⇥ success                  | boolean        | Success or not                        |
| ⇥ user\_id                 | int64          | User ID                               |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 1.4 Modify password{#post\_\_user\_change\_password}

> POST /user/change\_password

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description  |
| -------------- | --------- | -------- | ------- | ------------ |
| new\_password  | string    | true     |         | New password |
| old\_password  | string    | true     |         | Old password |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.5 Administrator change password{#post\_\_user\_change\_password\_admin}

> POST /user/change\_password\_admin

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
| password       | string    | true     |         | Password    |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.6 Delete users{#delete\_\_user\_delete}

> DELETE /user/delete

> POST /user/delete

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description                                                                                                                   |
| -------------- | --------- | -------- | ------- | ----------------------------------------------------------------------------------------------------------------------------- |
| password       | string    | false    |         | User password: if it is a user TOKEN, this field needs to be set; if it is an administrator TOKEN, it does not need to be set |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.7 Device list{#get\_\_user\_device\_list}

> GET /user/device/list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                                                                |
| -------------------------- | -------------- | -------------------------------------------------------------------------- |
| code                       | int32          | Return code, 200 is success                                                |
| cursor                     | string         | Cursor, no cursor in returned result means the last page has been returned |
| data                       | array\[object] | Result data                                                                |
| ⇥ device\_sn               | int32          | Device serial number                                                       |
| ⇥ platform                 | int32          | Device platform,1:ios, 2:android, 3:windows, 4:mac, 5:linux, 6:web         |
| ⇥ user\_agent              | string         | Device information                                                         |
| ⇥ user\_id                 | int64          | User ID                                                                    |
| message                    | string         | Error information, null means success                                      |
| version                    | int64          | Version                                                                    |
| #### Interface Description |                |                                                                            |

>

## 1.8 Delete device{#delete\_\_user\_device\_remove}

> DELETE /user/device/remove

> POST /user/device/remove

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description          |
| -------------- | --------- | -------- | -------------------- |
| device\_sn     | int32     | true     | Device serial number |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.9 Banned user{#put\_\_user\_disable}

> PUT /user/disable

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description      |
| -------------- | ------------- | -------- | ------- | ---------------- |
| list           | array\[int64] | true     |         | List of user IDs |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.10 Set whether to download thumbnails and files automatically{#put\_\_user\_download}

> PUT /user/download

> POST /user/download

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                                                          |
| -------------- | --------- | -------- | -------------------------------------------------------------------- |
| value          | boolean   | true     | Whether to automatically download thumbnails: true - yes, false - no |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.11 Unbanned user{#put\_\_user\_enable}

> PUT /user/enable

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type     | Required | Default | Description      |
| -------------- | ------------- | -------- | ------- | ---------------- |
| list           | array\[int64] | true     |         | List of user IDs |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.12 Kick specified device{#put\_\_user\_kick}

> PUT /user/kick

> POST /user/kick

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                                         |
| -------------- | --------- | -------- | --------------------------------------------------- |
| device\_sn     | int32     | false    | Device serial number:Not set means kick all devices |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.13 List all users under the APP{#get\_\_user\_list}

> GET /user/list

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                                        |
| -------------- | --------- | -------- | -------------------------------------------------- |
| page\_num      | int32     | false    | Number of pages:must be greater than0,default is 1 |
| page\_size     | int32     | false    | Size per page:50 per page by default               |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ status                   | int32          | 0-normal, 1-ban                       |
| ⇥ user\_id                 | int64          | User ID                               |
| ⇥ username                 | string         | Username                              |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 1.14 Set mobile number{#put\_\_user\_mobile}

> PUT /user/mobile

> POST /user/mobile

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

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.15 Set nickname{#put\_\_user\_nickname}

> PUT /user/nickname

> POST /user/nickname

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
| nick\_name     | string    | true     | Nickname    |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.16 Query user online status{#get\_\_user\_online\_status}

> GET /user/online\_status

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                                   |
| -------------------------- | ------- | --------------------------------------------- |
| code                       | int32   | Return code, 200 is success                   |
| data                       | object  | Result data                                   |
| ⇥ online                   | boolean | Online or not: true - online, false - offline |
| message                    | string  | Error information, null means success         |
| #### Interface Description |         |                                               |

>

## 1.17 Set private extension information{#put\_\_user\_private}

> PUT /user/private

> POST /user/private

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
|                | string    | true     |         | Private extension information |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.18 Get user information{#get\_\_user\_profile}

> GET /user/profile

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                                               |
| -------------------------- | ------ | --------------------------------------------------------- |
| code                       | int32  | Return code, 200 is success                               |
| data                       | object | Result data                                               |
| ⇥ avatar                   | string | Avatar url                                                |
| ⇥ description              | string | Description                                               |
| ⇥ email                    | string | Email                                                     |
| ⇥ mobile                   | string | Mobile number                                             |
| ⇥ nick\_name               | string | Nickname                                                  |
| ⇥ private\_info            | string | Private information, visible only to yourself             |
| ⇥ public\_info             | string | Public information, visible to both friends and strangers |
| ⇥ user\_id                 | int64  | User ID                                                   |
| ⇥ username                 | string | Username                                                  |
| message                    | string | Error information, null means success                     |
| #### Interface Description |        |                                                           |

>

## 1.19 Update user information{#put\_\_user\_profile}

> PUT /user/profile

> POST /user/profile

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description                                               |
| -------------- | --------- | -------- | ------- | --------------------------------------------------------- |
| description    | string    | false    |         | Description                                               |
| nick\_name     | string    | false    |         | Nickname                                                  |
| private\_info  | string    | false    |         | Private information, visible only to yourself             |
| public\_info   | string    | false    |         | Public information, visible to both friends and strangers |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.20 Update user information in batch{#put\_\_user\_profile\_batch}

> PUT /user/profile/batch

> POST /user/profile/batch

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name  | Data Type      | Required | Default | Description                                               |
| --------------- | -------------- | -------- | ------- | --------------------------------------------------------- |
| list            | array\[object] | false    |         |                                                           |
| ⇥ description   | string         | false    |         | Description                                               |
| ⇥ nick\_name    | string         | false    |         | Nickname                                                  |
| ⇥ private\_info | string         | false    |         | Private information, visible only to yourself             |
| ⇥ public\_info  | string         | false    |         | Public information, visible to both friends and strangers |
| ⇥ user\_id      | int64          | false    |         | User ID                                                   |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ reason                   | string         | Cause of failure                      |
| ⇥ success                  | boolean        | Success or not                        |
| ⇥ user\_id                 | int64          | User ID                               |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 1.21 Set public extension information{#put\_\_user\_public}

> PUT /user/public

> POST /user/public

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description                  |
| -------------- | --------- | -------- | ------- | ---------------------------- |
|                | string    | true     |         | Public extension information |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.22 Set whether to turn off push{#put\_\_user\_push}

> PUT /user/push

> POST /user/push

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                                                      |
| -------------- | --------- | -------- | ---------------------------------------------------------------- |
| value          | boolean   | true     | Whether to close push: true - close push, false - not close push |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.23 Bind alias{#post\_\_user\_push\_alias}

> POST /user/push/alias

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
| alias          | string    | true     |         | Alias       |
| push\_token    | string    | false    |         | Push token  |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.24 Set badge{#post\_\_user\_push\_badge}

> POST /user/push/badge

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
| badge          | int32     | true     |         | badge       |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.25 Set whether to turn off push details{#put\_\_user\_push\_detail}

> PUT /user/push/detail

> POST /user/push/detail

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                                                                                 |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------- |
| value          | boolean   | true     | Whether to close push details: true - close push details, false - do not close push details |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.26 Set push no-disturb time{#put\_\_user\_push\_limit}

> PUT /user/push/limit

> POST /user/push/limit

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name        | Data Type | Required | Description               |
| --------------------- | --------- | -------- | ------------------------- |
| no\_push\_end\_hour   | int32     | true     | Push DND end hour(0-23)   |
| no\_push\_start\_hour | int32     | true     | Push DND start hour(0-23) |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.27 Set push nickname{#put\_\_user\_push\_nickname}

> PUT /user/push/nickname

> POST /user/push/nickname

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
| value          | string    | true     | Push nickname |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.28 Get tag{#get\_\_user\_push\_tag}

> GET /user/push/tag

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[string] | Result data                           |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 1.29 Bind tag{#post\_\_user\_push\_tag}

> POST /user/push/tag

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type      | Required | Default | Description  |
| -------------- | -------------- | -------- | ------- | ------------ |
| tags           | array\[string] | true     |         | List of tags |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.30 Unbind tag{#delete\_\_user\_push\_tag}

> DELETE /user/push/tag

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type      | Required | Default | Description  |
| -------------- | -------------- | -------- | ------- | ------------ |
| tags           | array\[string] | true     |         | List of tags |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.31 Delete all tags{#delete\_\_user\_push\_tag\_all}

> DELETE /user/push/tag/all

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.32 Register user in batch{#post\_\_user\_register\_batch}

> POST /user/register/batch

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type      | Required | Default | Description |
| -------------- | -------------- | -------- | ------- | ----------- |
| list           | array\[object] | false    |         |             |
| ⇥ password     | string         | true     |         | Password    |
| ⇥ username     | string         | true     |         | Username    |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type           | Description                           |
| -------------------------- | -------------- | ------------------------------------- |
| code                       | int32          | Return code, 200 is success           |
| data                       | array\[object] | Result data                           |
| ⇥ reason                   | string         | Cause of failure                      |
| ⇥ success                  | boolean        | Success or not                        |
| ⇥ user\_id                 | int64          | User ID                               |
| ⇥ username                 | string         | Username                              |
| message                    | string         | Error information, null means success |
| #### Interface Description |                |                                       |

>

## 1.33 Register push user{#post\_\_user\_register\_push}

> POST /user/register/push

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
| alias          | string    | false    |         | Alias       |
| device\_guid   | string    | false    |         | Device ID   |
| password       | string    | true     |         | Password    |
| push\_token    | string    | false    |         | Push token  |
| sign           | string    | false    |         | Signature   |
| username       | string    | true     |         | Username    |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                                                                                                                                                                                                               |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                       | int32   | Return code, 200 is success                                                                                                                                                                                               |
| data                       | object  | Result data                                                                                                                                                                                                               |
| ⇥ auth\_answer             | string  | Answer of verification question                                                                                                                                                                                           |
| ⇥ auth\_mode               | int32   | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
| ⇥ auth\_question           | string  | Verification question                                                                                                                                                                                                     |
| ⇥ auto\_download           | boolean | Whether to automatically download: true - automatic download, false - no automatic download                                                                                                                               |
| ⇥ group\_confirm           | boolean | Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed                                                                                 |
| ⇥ id                       | int64   |                                                                                                                                                                                                                           |
| ⇥ no\_push                 | boolean | Whether to turn off push messages: true - turn off push messages, false - do not turn off push messages                                                                                                                   |
| ⇥ no\_push\_detail         | boolean | Whether to push details: true - push details, false - don't push details                                                                                                                                                  |
| ⇥ no\_push\_end\_hour      | int32   | Start of push no-disturb time(Hour 0-23)                                                                                                                                                                                  |
| ⇥ no\_push\_start\_hour    | int32   | End of push no-disturb time(Hour 0-23)                                                                                                                                                                                    |
| ⇥ no\_sounds               | boolean | Whether to mute when a message is received: true - mute, false - not mute                                                                                                                                                 |
| ⇥ push\_nick\_name         | string  | Push nickname                                                                                                                                                                                                             |
| ⇥ push\_token              | string  | Push token                                                                                                                                                                                                                |
| ⇥ silence\_end\_time       | int32   | End of push no-reminder time(Hour 0-23)                                                                                                                                                                                   |
| ⇥ silence\_start\_time     | int32   | Start of push no-reminder time(Hour 0-23)                                                                                                                                                                                 |
| ⇥ user\_id                 | int64   | User ID                                                                                                                                                                                                                   |
| ⇥ vibratory                | boolean | Whether to vibrate when a message is received: true - vibrate, false - not vibrate                                                                                                                                        |
| message                    | string  | Error information, null means success                                                                                                                                                                                     |
| #### Interface Description |         |                                                                                                                                                                                                                           |

>

## 1.34 Register user{#post\_\_user\_register\_v2}

> POST /user/register/v2

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
| password       | string    | true     |         | Password    |
| username       | string    | true     |         | Username    |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                                                                                                                                                                                                               |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                       | int32   | Return code, 200 is success                                                                                                                                                                                               |
| data                       | object  | Result data                                                                                                                                                                                                               |
| ⇥ auth\_answer             | string  | Answer of verification question                                                                                                                                                                                           |
| ⇥ auth\_mode               | int32   | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
| ⇥ auth\_question           | string  | Verification question                                                                                                                                                                                                     |
| ⇥ auto\_download           | boolean | Whether to automatically download: true - automatic download, false - no automatic download                                                                                                                               |
| ⇥ group\_confirm           | boolean | Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed                                                                                 |
| ⇥ id                       | int64   |                                                                                                                                                                                                                           |
| ⇥ no\_push                 | boolean | Whether to turn off push messages: true - turn off push messages, false - do not turn off push messages                                                                                                                   |
| ⇥ no\_push\_detail         | boolean | Whether to push details: true - push details, false - don't push details                                                                                                                                                  |
| ⇥ no\_push\_end\_hour      | int32   | Start of push no-disturb time(Hour 0-23)                                                                                                                                                                                  |
| ⇥ no\_push\_start\_hour    | int32   | End of push no-disturb time(Hour 0-23)                                                                                                                                                                                    |
| ⇥ no\_sounds               | boolean | Whether to mute when a message is received: true - mute, false - not mute                                                                                                                                                 |
| ⇥ push\_nick\_name         | string  | Push nickname                                                                                                                                                                                                             |
| ⇥ push\_token              | string  | Push token                                                                                                                                                                                                                |
| ⇥ silence\_end\_time       | int32   | End of push no-reminder time(Hour 0-23)                                                                                                                                                                                   |
| ⇥ silence\_start\_time     | int32   | Start of push no-reminder time(Hour 0-23)                                                                                                                                                                                 |
| ⇥ user\_id                 | int64   | User ID                                                                                                                                                                                                                   |
| ⇥ vibratory                | boolean | Whether to vibrate when a message is received: true - vibrate, false - not vibrate                                                                                                                                        |
| message                    | string  | Error information, null means success                                                                                                                                                                                     |
| #### Interface Description |         |                                                                                                                                                                                                                           |

>

## 1.35 Get user settings{#get\_\_user\_settings}

> GET /user/settings

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                                                                                                                                                                                                               |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| code                       | int32   | Return code, 200 is success                                                                                                                                                                                               |
| data                       | object  | Result data                                                                                                                                                                                                               |
| ⇥ auth\_answer             | string  | Answer of verification question                                                                                                                                                                                           |
| ⇥ auth\_mode               | int32   | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
| ⇥ auth\_question           | string  | Verification question                                                                                                                                                                                                     |
| ⇥ auto\_download           | boolean | Whether to automatically download: true - automatic download, false - no automatic download                                                                                                                               |
| ⇥ group\_confirm           | boolean | Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed                                                                                 |
| ⇥ id                       | int64   |                                                                                                                                                                                                                           |
| ⇥ no\_push                 | boolean | Whether to turn off push messages: true - turn off push messages, false - do not turn off push messages                                                                                                                   |
| ⇥ no\_push\_detail         | boolean | Whether to push details: true - push details, false - don't push details                                                                                                                                                  |
| ⇥ no\_push\_end\_hour      | int32   | Start of push no-disturb time(Hour 0-23)                                                                                                                                                                                  |
| ⇥ no\_push\_start\_hour    | int32   | End of push no-disturb time(Hour 0-23)                                                                                                                                                                                    |
| ⇥ no\_sounds               | boolean | Whether to mute when a message is received: true - mute, false - not mute                                                                                                                                                 |
| ⇥ push\_nick\_name         | string  | Push nickname                                                                                                                                                                                                             |
| ⇥ push\_token              | string  | Push token                                                                                                                                                                                                                |
| ⇥ silence\_end\_time       | int32   | End of push no-reminder time(Hour 0-23)                                                                                                                                                                                   |
| ⇥ silence\_start\_time     | int32   | Start of push no-reminder time(Hour 0-23)                                                                                                                                                                                 |
| ⇥ user\_id                 | int64   | User ID                                                                                                                                                                                                                   |
| ⇥ vibratory                | boolean | Whether to vibrate when a message is received: true - vibrate, false - not vibrate                                                                                                                                        |
| message                    | string  | Error information, null means success                                                                                                                                                                                     |
| #### Interface Description |         |                                                                                                                                                                                                                           |

>

## 1.36 Modify user settings{#put\_\_user\_settings}

> PUT /user/settings

> POST /user/settings

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name        | Data Type | Required | Default | Description                                                                                                                                                                                                               |
| --------------------- | --------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| auth\_answer          | string    | false    |         | Answer of verification question                                                                                                                                                                                           |
| auth\_mode            | int32     | false    |         | Verification method: 0 - No verification, anyone can be added as a friend; 1 - consent is required to be added as a friend; 2 - answer questions correctly to be added as a friend; 3 - reject all adding friend requests |
| auth\_question        | string    | false    |         | Verification question                                                                                                                                                                                                     |
| auto\_download        | boolean   | false    |         | Whether to automatically download: true - automatic download, false - no automatic download                                                                                                                               |
| group\_confirm        | boolean   | false    |         | Whether user consent is required when inviting to join group: true - user consent is required, false - invitation is automatically agreed                                                                                 |
| id                    | int64     | false    |         |                                                                                                                                                                                                                           |
| no\_push              | boolean   | false    |         | Whether to turn off push messages: true - turn off push messages, false - do not turn off push messages                                                                                                                   |
| no\_push\_detail      | boolean   | false    |         | Whether to push details: true - push details, false - don't push details                                                                                                                                                  |
| no\_push\_end\_hour   | int32     | false    |         | Start of push no-disturb time(Hour 0-23)                                                                                                                                                                                  |
| no\_push\_start\_hour | int32     | false    |         | End of push no-disturb time(Hour 0-23)                                                                                                                                                                                    |
| no\_sounds            | boolean   | false    |         | Whether to mute when a message is received: true - mute, false - not mute                                                                                                                                                 |
| push\_nick\_name      | string    | false    |         | Push nickname                                                                                                                                                                                                             |
| push\_token           | string    | false    |         | Push token                                                                                                                                                                                                                |
| silence\_end\_time    | int32     | false    |         | End of push no-reminder time(Hour 0-23)                                                                                                                                                                                   |
| silence\_start\_time  | int32     | false    |         | Start of push no-reminder time(Hour 0-23)                                                                                                                                                                                 |
| user\_id              | int64     | true     |         | User ID                                                                                                                                                                                                                   |
| vibratory             | boolean   | false    |         | Whether to vibrate when a message is received: true - vibrate, false - not vibrate                                                                                                                                        |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.37 Set whether to mute sound alert for new message{#put\_\_user\_sounds}

> PUT /user/sounds

> POST /user/sounds

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                                                                                                            |
| -------------- | --------- | -------- | ---------------------------------------------------------------------------------------------------------------------- |
| value          | boolean   | true     | Whether to turn off the sound reminder: true - turn off the sound reminder, false - do not turn off the sound reminder |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.38 Bind token{#put\_\_user\_token\_bind}

> PUT /user/token/bind

> POST /user/token/bind

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
| device\_sn     | int32     | true     |         | Device serial number |
| device\_token  | string    | true     |         | device token         |
| notifier\_name | string    | true     |         | Certificate name     |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.39 Unbind token{#delete\_\_user\_token\_unbind}

> DELETE /user/token/unbind

> POST /user/token/unbind

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description          |
| -------------- | --------- | -------- | -------------------- |
| deviceSn       | int32     | true     | Device serial number |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                           |
| -------------------------- | ------ | ------------------------------------- |
| code                       | int32  | Return code, 200 is success           |
| data                       | object | Result data                           |
| message                    | string | Error information, null means success |
| #### Interface Description |        |                                       |

>

## 1.40 Modify username{#put\_\_user\_username}

> PUT /user/username

> POST /user/username

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

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>

## 1.41 Set whether to vibrate alert for new message{#put\_\_user\_vibratory}

> PUT /user/vibratory

> POST /user/vibratory

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param

| Parameter name | Data Type | Required | Description                                          |
| -------------- | --------- | -------- | ---------------------------------------------------- |
| value          | boolean   | true     | Whether to vibrate: true-vibrate, false-no vibration |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type    | Description                           |
| -------------------------- | ------- | ------------------------------------- |
| code                       | int32   | Return code, 200 is success           |
| data                       | boolean | Result data                           |
| message                    | string  | Error information, null means success |
| #### Interface Description |         |                                       |

>
