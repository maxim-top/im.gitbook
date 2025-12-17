# 2 token interface{#token}

## 2.1 Get ordinary user token by user ID and password{#post\_\_token\_id}

> POST /token/id

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description                          |
| -------------- | --------- | -------- | ------- | ------------------------------------ |
| device\_guid   | string    | false    |         | Device ID, if set, returns PushToken |
| password       | string    | true     |         | Password                             |
| user\_id       | int64     | true     |         | User ID, for login by user ID only   |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                                         |
| -------------------------- | ------ | --------------------------------------------------- |
| code                       | int32  | Return code, 200 is success                         |
| data                       | object | Result data                                         |
| ⇥ access\_key\_secret      | string | File key                                            |
| ⇥ encrypt\_type            | int32  | Whether to enable encrypted connection              |
| ⇥ expire                   | int64  | Expiration timestamp                                |
| ⇥ public\_key              | string | Public key                                          |
| ⇥ push\_token              | string | Push Token                                          |
| ⇥ store\_token             | string | File token                                          |
| ⇥ token                    | string | Access token, The access-token when calling the API |
| ⇥ user\_id                 | int64  | User ID                                             |
| message                    | string | Error information, null means success               |
| #### Interface Description |        |                                                     |

>

## 2.2 Get ordinary user token by username/mobile number/email{#post\_\_token\_login}

> POST /token/login

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description                                             |
| -------------- | --------- | -------- | ------- | ------------------------------------------------------- |
| device\_guid   | string    | false    |         | Device ID, if set, returns PushToken                    |
| login\_name    | string    | true     |         | Login name, which can be mobile number, email, username |
| password       | string    | true     |         | Password                                                |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                                         |
| -------------------------- | ------ | --------------------------------------------------- |
| code                       | int32  | Return code, 200 is success                         |
| data                       | object | Result data                                         |
| ⇥ access\_key\_secret      | string | File key                                            |
| ⇥ encrypt\_type            | int32  | Whether to enable encrypted connection              |
| ⇥ expire                   | int64  | Expiration timestamp                                |
| ⇥ public\_key              | string | Public key                                          |
| ⇥ push\_token              | string | Push Token                                          |
| ⇥ store\_token             | string | File token                                          |
| ⇥ token                    | string | Access token, The access-token when calling the API |
| ⇥ user\_id                 | int64  | User ID                                             |
| message                    | string | Error information, null means success               |
| #### Interface Description |        |                                                     |

>

## 2.3 Get ordinary user token by username and password{#post\_\_token\_user}

> POST /token/user

#### Request Header

| Parameter name | Data Type | Required | Description                                                                                                              |
| -------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| access-token   | string    | false    | Token                                                                                                                    |
| app\_id        | string    | true     | App ID                                                                                                                   |
| group\_id      | int64     | false    | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID    |
| user\_id       | int64     | false    | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body

| Parameter name | Data Type | Required | Default | Description                          |
| -------------- | --------- | -------- | ------- | ------------------------------------ |
| device\_guid   | string    | false    |         | Device ID, if set, returns PushToken |
| name           | string    | true     |         | Username, for login by username only |
| password       | string    | true     |         | Password                             |

#### Response Body

● 200 Response data format:JSON

| Parameter name             | Type   | Description                                         |
| -------------------------- | ------ | --------------------------------------------------- |
| code                       | int32  | Return code, 200 is success                         |
| data                       | object | Result data                                         |
| ⇥ access\_key\_secret      | string | File key                                            |
| ⇥ encrypt\_type            | int32  | Whether to enable encrypted connection              |
| ⇥ expire                   | int64  | Expiration timestamp                                |
| ⇥ public\_key              | string | Public key                                          |
| ⇥ push\_token              | string | Push Token                                          |
| ⇥ store\_token             | string | File token                                          |
| ⇥ token                    | string | Access token, The access-token when calling the API |
| ⇥ user\_id                 | int64  | User ID                                             |
| message                    | string | Error information, null means success               |
| #### Interface Description |        |                                                     |

>
