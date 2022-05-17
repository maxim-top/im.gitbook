# 4 Group interface{#group}

## 4.1 Add group Admin{#post__group_admin_add}

> POST /group/admin/add

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| user_list | array[int64] | true |  | User id list |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ reason | string |  |
|⇥ result | string |  |
|⇥ user_id | int64 |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.2 Remove group Admin{#delete__group_admin_remove}

> DELETE /group/admin/remove

> POST /group/admin/remove

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| user_list | array[int64] | true |  | User id list |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ reason | string |  |
|⇥ result | string |  |
|⇥ user_id | int64 |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.3 Get the list of group Admins{#get__group_admin_list}

> GET /group/admin_list

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | group_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ display_name | string | Group member profile |
|⇥ join_time | int64 | Member join time |
|⇥ user_id | int64 | User id |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.4 Get group announcement details by group id and announcement id{#get__group_announcement}

> GET /group/announcement

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| announcement_id | int64 | true | announcement_id |
| group_id | int64 | true | group_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ author | int64 | Announcement publisher |
|⇥ content | string | Announcement content |
|⇥ created_at | int64 | Announcement publish time |
|⇥ group_id | int64 | Group id |
|⇥ id | int64 | Announcement id |
|⇥ title | string | Announcement tittle |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.5 Delete group announcement{#delete__group_announcement_delete}

> DELETE /group/announcement/delete

> POST /group/announcement/delete

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| announcement_id | int64 | true | announcement_id |
| group_id | int64 | true | group_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.6 Edit group announcement{#post__group_announcement_edit}

> POST /group/announcement/edit

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| content | string | true |  | Announcement content |
| group_id | int64 | true |  | Group id |
| title | string | true |  | Announcement tittle |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ author | int64 | Announcement publisher |
|⇥ content | string | Announcement content |
|⇥ created_at | int64 | Announcement publish time |
|⇥ group_id | int64 | Group id |
|⇥ id | int64 | Announcement id |
|⇥ title | string | Announcement tittle |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.7 Get the latest group announcement details{#get__group_announcement_last}

> GET /group/announcement/last

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | group_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ author | int64 | Announcement publisher |
|⇥ content | string | Announcement content |
|⇥ created_at | int64 | Announcement publish time |
|⇥ group_id | int64 | Group id |
|⇥ id | int64 | Announcement id |
|⇥ title | string | Announcement tittle |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.8 Get group announcements list{#get__group_announcement_list}

> GET /group/announcement/list

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | group_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ author | int64 | Announcement publisher |
|⇥ content | string | Announcement content |
|⇥ created_at | int64 | Announcement publish time |
|⇥ group_id | int64 | Group id |
|⇥ id | int64 | Announcement id |
|⇥ title | string | Announcement tittle |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.9 Get the list of group membership requests{#post__group_application_list}

> POST /group/application_list

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| cursor | string | false | cursor |
| limit | int32 | false | limit |
| version | int64 | false | version |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_list | array[int64] | true |  | Group id list |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| cursor | string | Cursor for page turning |
| data | object | Result data |
| message | string | Error information, null means success |
| total | int64 | Total |
| version | int64 | Version, not used at present, reserved for extension |
#### Interface Description
> 

## 4.10 Apply for group membership{#post__group_apply}

> POST /group/apply

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| reason | string | false |  | Reason for membership application |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ reason | string |  |
|⇥ result | string |  |
|⇥ user_id | int64 |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.11 Admin processes membership application{#put__group_apply_handle}

> PUT /group/apply/handle

> POST /group/apply/handle

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| approval | boolean | true |  | Approval, bool type, true for approval, false for rejection |
| group_id | int64 | true |  | Group id |
| user_id | int64 | true |  | User id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ reason | string |  |
|⇥ result | string |  |
|⇥ user_id | int64 |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.12 Ban a user{#post__group_ban}

> POST /group/ban

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| duration | int64 | true |  | Duration of banned in minutes |
| group_id | int64 | true |  | Group id |
| user_list | array[int64] | true |  | User id list |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ reason | string |  |
|⇥ result | string |  |
|⇥ user_id | int64 |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.13 Get a list of banned members{#get__group_banned_list}

> GET /group/banned_list

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| cursor | string | false | cursor |
| group_id | int64 | true | group_id |
| limit | int32 | false | limit |
| version | int64 | false | version |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| cursor | string | Cursor for page turning |
| data | object | Result data |
| message | string | Error information, null means success |
| total | int64 | Total |
| version | int64 | Version, not used at present, reserved for extension |
#### Interface Description
> 

## 4.14 Blacklist a user{#post__group_block}

> POST /group/block

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| user_list | array[int64] | true |  | User id list |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ reason | string |  |
|⇥ result | string |  |
|⇥ user_id | int64 |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.15 Get backlist{#get__group_blocked_list}

> GET /group/blocked_list

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| cursor | string | false | cursor |
| group_id | int64 | true | group_id |
| limit | int32 | false | limit |
| version | int64 | false | version |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| cursor | string | Cursor for page turning |
| data | object | Result data |
| message | string | Error information, null means success |
| total | int64 | Total |
| version | int64 | Version, not used at present, reserved for extension |
#### Interface Description
> 

## 4.16 Create group{#post__group_create}

> POST /group/create

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| avatar | string | false |  | Group avatar |
| description | string | false |  | Group description |
| name | string | false |  | Group name |
| type | int32 | false |  | Group type: 1 for public group, 0 for private group, 2 for chatroom |
| user_list | array[int64] | false |  | List of user ids invited to join group |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.17 Disband group{#delete__group_destroy}

> DELETE /group/destroy

> POST /group/destroy

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | group_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.18 Update group profile{#put__group_display_name}

> PUT /group/display_name

> POST /group/display_name

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| value | string | true |  | Update content |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.19 Download group file{#get__group_file}

> GET /group/file

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| file_id | int64 | true | file_id |
| group_id | int64 | true | group_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ created_at | int64 |  |
|⇥ file_id | int64 | Shared file id |
|⇥ group_id | int64 | Group id |
|⇥ name | string | Shared file name |
|⇥ size | int64 | Shared file size |
|⇥ type | string | Shared file type |
|⇥ updated_at | int64 |  |
|⇥ uploader | int64 | Shared file uploader |
|⇥ url | string | Shared file url |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.20 Delete group file{#delete__group_file_delete}

> DELETE /group/file/delete

> POST /group/file/delete

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| file_list | array[int64] | true |  | File id list |
| group_id | int64 | true |  | Group id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ file_id | int64 |  |
|⇥ reason | string |  |
|⇥ result | string |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.21 Get the list of group files{#get__group_file_list}

> GET /group/file/list

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | group_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ created_at | int64 |  |
|⇥ file_id | int64 | Shared file id |
|⇥ group_id | int64 | Group id |
|⇥ name | string | Shared file name |
|⇥ size | int64 | Shared file size |
|⇥ type | string | Shared file type |
|⇥ updated_at | int64 |  |
|⇥ uploader | int64 | Shared file uploader |
|⇥ url | string | Shared file url |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.22 Update group file name{#put__group_file_update_name}

> PUT /group/file/update_name

> POST /group/file/update_name

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| file_id | int64 | true |  | File id |
| group_id | int64 | true |  | Group id |
| name | string | true |  | New file name |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.23 Upload group file{#post__group_file_upload}

> POST /group/file/upload

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| name | string | true |  | File name |
| size | int64 | true |  | File size |
| type | string | false |  | File type |
| url | string | true |  | File url |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ created_at | int64 |  |
|⇥ file_id | int64 | Shared file id |
|⇥ group_id | int64 | Group id |
|⇥ name | string | Shared file name |
|⇥ size | int64 | Shared file size |
|⇥ type | string | Shared file type |
|⇥ updated_at | int64 |  |
|⇥ uploader | int64 | Shared file uploader |
|⇥ url | string | Shared file url |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.24 Get group information by group id{#get__group_info}

> GET /group/info

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | group_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ apply_approval | int32 | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests |
|⇥ avatar | string | Group avatar |
|⇥ ban_expire_time | int64 | Expiration time (second), during which only Admins are allowed to send messages, 0 or less than the current time means no banning, -1 means banned permanently |
|⇥ created_at | int64 | Creation time |
|⇥ description | string | Group description |
|⇥ ext | string | Group extension information |
|⇥ group_id | int64 | Group id |
|⇥ history_visible | boolean | History chat visibility settings for new members |
|⇥ member_invite | boolean | Group member invitation settings |
|⇥ member_modify | boolean | Group information modification settings for members |
|⇥ msg_mute_mode | int32 | Group message blocking mode |
|⇥ msg_push_mode | int32 | Push mode of group messages |
|⇥ name | string | Group name |
|⇥ owner_id | int64 | Group Owner id |
|⇥ read_ack | boolean | Group message read function settings |
|⇥ status | int32 | Group state, 0: normal, 1: dissolved |
|⇥ type | int32 | Group type |
|⇥ updated_at | int64 | Update time |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.25 Update group avatar{#put__group_info_avatar}

> PUT /group/info/avatar

> POST /group/info/avatar

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| value | string | true |  | Update content |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.26 Get group information by group id{#post__group_info_batch}

> POST /group/info/batch

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_list | array[int64] | true |  | Group id list |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ apply_approval | int32 | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests |
|⇥ avatar | string |  |
|⇥ capacity | int64 |  |
|⇥ count | int64 |  |
|⇥ group_id | int64 |  |
|⇥ msg_mute_mode | int32 | Group message blocking settings |
|⇥ msg_push_mode | int32 | Group message push settings |
|⇥ name | string |  |
|⇥ owner | int64 |  |
|⇥ status | int32 | Group state, 0: normal, 1: dissolved |
|⇥ type | int32 |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.27 Update group description{#put__group_info_description}

> PUT /group/info/description

> POST /group/info/description

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| value | string | true |  | Update content |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.28 Update extension information{#put__group_info_ext}

> PUT /group/info/ext

> POST /group/info/ext

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| value | string | true |  | Update content |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.29 Update group name{#put__group_info_name}

> PUT /group/info/name

> POST /group/info/name

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| value | string | true |  | Update content |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.30 Get group invitation list{#get__group_invitation_list}

> GET /group/invitation_list

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| cursor | string | false | cursor |
| limit | int32 | false | limit |
| version | int64 | false | version |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| cursor | string | Cursor for page turning |
| data | object | Result data |
| message | string | Error information, null means success |
| total | int64 | Total |
| version | int64 | Version, not used at present, reserved for extension |
#### Interface Description
> 

## 4.31 Invite to group{#post__group_invite}

> POST /group/invite

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| reason | string | false |  | Invitation reason |
| user_list | array[int64] | true |  | Invitee id, List type, multiple users can be invited to a group at one time |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ reason | string |  |
|⇥ result | string |  |
|⇥ user_id | int64 |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.32 Process group invitation by user{#put__group_invite_handle}

> PUT /group/invite/handle

> POST /group/invite/handle

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| approval | boolean | true |  | Approval, bool type, true for approval, false for rejection |
| group_id | int64 | true |  | Group id |
| user_id | int64 | true |  | User id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.33 Kick member out of group{#delete__group_kick}

> DELETE /group/kick

> POST /group/kick

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| user_list | array[int64] | true |  | User id list |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ reason | string |  |
|⇥ result | string |  |
|⇥ user_id | int64 |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.34 Member quit group{#delete__group_leave}

> DELETE /group/leave

> POST /group/leave

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | group_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.35 Get group member list by group id{#get__group_member_list}

> GET /group/member_list

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| cursor | string | false | cursor |
| group_id | int64 | true | group_id |
| limit | int32 | false | limit |
| version | int64 | false | version |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| cursor | string | Cursor for page turning |
| data | array[object] | Result data |
|⇥ display_name | string | Group member profile |
|⇥ join_time | int64 | Member join time |
|⇥ user_id | int64 | User id |
| message | string | Error information, null means success |
| total | int64 | Total |
| version | int64 | Version, not used at present, reserved for extension |
#### Interface Description
> 

## 4.36 Batch retrieval of group member profiles{#post__group_members_display_name}

> POST /group/members/display_name

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| user_list | array[int64] | true |  | User id list |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ display_name | string | Group member profile |
|⇥ join_time | int64 | Member join time |
|⇥ user_id | int64 | User id |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.37 Set group message blocking mode{#put__group_msg_mute_mode}

> PUT /group/msg/mute_mode

> POST /group/msg/mute_mode

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| msg_mute_mode | int32 | true |  | Group message blocking mode: 0: No blocking; 1: Blocking local message notifications; 2: Blocking messages, not receiving messages |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.38 Set group message pushing mode{#put__group_msg_push_mode}

> PUT /group/msg/push_mode

> POST /group/msg/push_mode

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| msg_push_mode | int32 | true |  | Group message push type: 0: Receive all pushes; 1: Do not accept push; 2: Receive Admin and @ pushes; 3. Only receive Admin pushes; 4: Only receive @ pushes |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.39 Get public group list{#get__group_public_list}

> GET /group/public_list

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[int64] | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.40 Group invitation via QR code{#post__group_qrcode_invite}

> POST /group/qrcode/invite

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| qr_info | string | false |  |  |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.41 Get Group invitation QR code{#get__group_qrcode_sign}

> GET /group/qrcode/sign

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | group_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ create_at | int64 | QR code generation time |
|⇥ expire_at | int64 | QR code expiration time |
|⇥ qr_info | string | QR code information |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.42 Get group settings{#get__group_settings}

> GET /group/settings

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Query Param
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true | group_id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ apply_approval | int32 | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests |
|⇥ avatar | string | Group avatar |
|⇥ ban_expire_time | int64 | Expiration time (second), during which only Admins are allowed to send messages, 0 or less than the current time means no banning, -1 means banned permanently |
|⇥ created_at | int64 | Creation time |
|⇥ description | string | Group description |
|⇥ ext | string | Group extension information |
|⇥ group_id | int64 | Group id |
|⇥ history_visible | boolean | History chat visibility settings for new members |
|⇥ member_invite | boolean | Group member invitation settings |
|⇥ member_modify | boolean | Group information modification settings for members |
|⇥ msg_mute_mode | int32 | Group message blocking mode |
|⇥ msg_push_mode | int32 | Push mode of group messages |
|⇥ name | string | Group name |
|⇥ owner_id | int64 | Group Owner id |
|⇥ read_ack | boolean | Group message read function settings |
|⇥ status | int32 | Group state, 0: normal, 1: dissolved |
|⇥ type | int32 | Group type |
|⇥ updated_at | int64 | Update time |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.43 Update group settings - whether to allow member invitations{#put__group_settings_allow_member_invitation}

> PUT /group/settings/allow_member_invitation

> POST /group/settings/allow_member_invitation

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| value | boolean | true |  | Update content |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.44 Update group settings - whether group members can modify group information{#put__group_settings_allow_member_modify}

> PUT /group/settings/allow_member_modify

> POST /group/settings/allow_member_modify

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| value | boolean | true |  | Update content |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.45 Ban all members, only Admins can send messages{#post__group_settings_ban_all}

> POST /group/settings/ban_all

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| duration | int64 | true |  | Duration of banned in minutes |
| group_id | int64 | true |  | Group id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ ban_expire_time | int64 | Expiration time of banning all members |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.46 Update group settings - whether to enable “mark after read”{#put__group_settings_enable_read_ack}

> PUT /group/settings/enable_read_ack

> POST /group/settings/enable_read_ack

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| value | boolean | true |  | Update content |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.47 Update group settings - whether group chat history visible to new members{#put__group_settings_history_visible}

> PUT /group/settings/history_visible

> POST /group/settings/history_visible

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| value | boolean | true |  | Update content |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.48 Update group settings - whether group membership request needs Admin approval{#put__group_settings_require_admin_approval}

> PUT /group/settings/require_admin_approval

> POST /group/settings/require_admin_approval

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| apply_approval | int32 | true |  | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests |
| group_id | int64 | true |  | Group id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.49 Unban all members{#post__group_settings_unban_all}

> POST /group/settings/unban_all

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | boolean | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.50 Transfer of group Owner{#put__group_transfer}

> PUT /group/transfer

> POST /group/transfer

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| new_owner | int64 | true |  | User_id of new group Owner |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | object | Result data |
|⇥ reason | string |  |
|⇥ result | string |  |
|⇥ user_id | int64 |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.51 Remove user from ban list{#post__group_unban}

> POST /group/unban

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| user_list | array[int64] | true |  | User id list |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ reason | string |  |
|⇥ result | string |  |
|⇥ user_id | int64 |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.52 Remove user from blacklist{#delete__group_unblock}

> DELETE /group/unblock

> POST /group/unblock

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Request Body
|  Parameter name |  Data Type | Required  |  Default |  Description |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| group_id | int64 | true |  | Group id |
| user_list | array[int64] | true |  | User id list |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[object] | Result data |
|⇥ reason | string |  |
|⇥ result | string |  |
|⇥ user_id | int64 |  |
| message | string | Error information, null means success |
#### Interface Description
> 

## 4.53 Get the list of groups for the user{#get__group_user_joined}

> GET /group/user_joined

#### Request Header
|  Parameter name |  Data Type | Required |  Description |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | Token |
| app_id | string | true | App ID |
| group_id | int64 | false | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID |
| user_id | int64 | false | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID |

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Description |
|  ------ |  ------ |  ------ |
| code | int32 | Return code, 200 is success |
| data | array[int64] | Result data |
| message | string | Error information, null means success |
#### Interface Description
> 

