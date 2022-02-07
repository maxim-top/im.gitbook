

## 7    Group interface

## 7.1  Add group Admin

> POST  /group/admin/add

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  user_list| array[int32]| | false| User id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.2  Remove group Admin

> POST  /group/admin/remove

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  user_list| array[int32]| | false| User id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.3  Remove group Admin

> DELETE  /group/admin/remove

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  user_list| array[int32]| | false| User id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.4  Get the list of group Admins

> GET  /group/admin_list

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ display_name| string| | false| Group member profile| 
| ⇥ join_time| int32| | false| Member join time| 
| ⇥ user_id| int32| | false| User id| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.5  Get group announcement details by group id and announcement id

> GET  /group/announcement

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| announcement_id| | announcement_id| 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ author| int32| | false| Announcement publisher| 
| ⇥ content| string| | false| Announcement content| 
| ⇥ created_at| int32| | false| Announcement publish time| 
| ⇥ group_id| int32| | false| Group id| 
| ⇥ id| int32| | false| Announcement id| 
| ⇥ title| string| | false| Announcement tittle| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.6  Delete group announcement

> POST  /group/announcement/delete

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| announcement_id| | announcement_id| 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.7  Delete group announcement

> DELETE  /group/announcement/delete

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| announcement_id| | announcement_id| 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.8  Edit group announcement

> POST  /group/announcement/edit

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  content| string| | false| Announcement content| 
|  group_id| int32| | false| Group id| 
|  title| string| | false| Announcement tittle| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ author| int32| | false| Announcement publisher| 
| ⇥ content| string| | false| Announcement content| 
| ⇥ created_at| int32| | false| Announcement publish time| 
| ⇥ group_id| int32| | false| Group id| 
| ⇥ id| int32| | false| Announcement id| 
| ⇥ title| string| | false| Announcement tittle| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.9  Get the latest group announcement details

> GET  /group/announcement/last

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ author| int32| | false| Announcement publisher| 
| ⇥ content| string| | false| Announcement content| 
| ⇥ created_at| int32| | false| Announcement publish time| 
| ⇥ group_id| int32| | false| Group id| 
| ⇥ id| int32| | false| Announcement id| 
| ⇥ title| string| | false| Announcement tittle| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.10 Get group announcements list

> GET  /group/announcement/list

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ author| int32| | false| Announcement publisher| 
| ⇥ content| string| | false| Announcement content| 
| ⇥ created_at| int32| | false| Announcement publish time| 
| ⇥ group_id| int32| | false| Group id| 
| ⇥ id| int32| | false| Announcement id| 
| ⇥ title| string| | false| Announcement tittle| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.11 Get the list of group membership requests

> POST  /group/application_list

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| cursor| | cursor| 
| limit| | limit| 
| version| | version| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_list| array[int32]| | false| Group id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  cursor| string| | false| Cursor for page turning| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 
|  total| int32| | false| Total| 
|  version| int32| | false| Version, not used at present, reserved for extension| 


### Interface Description
> 




## 7.12 Apply for group membership

> POST  /group/apply

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  reason| string| | false| Reason for membership application| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.13 Admin processes membership application

> POST  /group/apply/handle

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  approval| boolean| | false| Approval, bool type, true for approval, false for rejection| 
|  group_id| int32| | false| Group id| 
|  user_id| int32| | false| User id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.14 Admin processes membership application

> PUT  /group/apply/handle

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  approval| boolean| | false| Approval, bool type, true for approval, false for rejection| 
|  group_id| int32| | false| Group id| 
|  user_id| int32| | false| User id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.15 Ban a user

> POST  /group/ban

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  duration| int32| | false| Duration of banned in minutes| 
|  group_id| int32| | false| Group id| 
|  user_list| array[int32]| | false| User id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.16 Get a list of banned members

> GET  /group/banned_list

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| cursor| | cursor| 
| group_id| | group_id| 
| limit| | limit| 
| version| | version| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  cursor| string| | false| Cursor for page turning| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 
|  total| int32| | false| Total| 
|  version| int32| | false| Version, not used at present, reserved for extension| 


### Interface Description
> 




## 7.17 Blacklist a user

> POST  /group/block

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  user_list| array[int32]| | false| User id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.18 Get backlist

> GET  /group/blocked_list

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| cursor| | cursor| 
| group_id| | group_id| 
| limit| | limit| 
| version| | version| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  cursor| string| | false| Cursor for page turning| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 
|  total| int32| | false| Total| 
|  version| int32| | false| Version, not used at present, reserved for extension| 


### Interface Description
> 




## 7.19 Create group

> POST  /group/create

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  avatar| string| | false| Group avatar| 
|  description| string| | false| Group description| 
|  name| string| | false| Group name| 
|  type| int32| | false| Group type: 1 for public group, 0 for private group, 2 for chatroom| 
|  user_list| array[int32]| | false| List of user ids invited to join group| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.20 Disband group

> POST  /group/destroy

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.21 Disband group

> DELETE  /group/destroy

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.22 Update group profile

> POST  /group/display_name

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| string| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.23 Update group profile

> PUT  /group/display_name

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| string| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.24 Download group file

> GET  /group/file

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| file_id| | file_id| 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Returned format of group shared files| 
| ⇥ created_at| int32| | false| | 
| ⇥ file_id| int32| | false| Shared file id| 
| ⇥ group_id| int32| | false| Group id| 
| ⇥ name| string| | false| Shared file name| 
| ⇥ size| int32| | false| Shared file size| 
| ⇥ type| string| | false| Shared file type| 
| ⇥ updated_at| int32| | false| | 
| ⇥ uploader| int32| | false| Shared file uploader| 
| ⇥ url| string| | false| Shared file url| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.25 Delete group file

> POST  /group/file/delete

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  file_list| array[int32]| | false| File id list| 
|  group_id| int32| | false| Group id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ file_id| int32| | false| | 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.26 Delete group file

> DELETE  /group/file/delete

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  file_list| array[int32]| | false| File id list| 
|  group_id| int32| | false| Group id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ file_id| int32| | false| | 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.27 Get the list of group files

> GET  /group/file/list

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ created_at| int32| | false| | 
| ⇥ file_id| int32| | false| Shared file id| 
| ⇥ group_id| int32| | false| Group id| 
| ⇥ name| string| | false| Shared file name| 
| ⇥ size| int32| | false| Shared file size| 
| ⇥ type| string| | false| Shared file type| 
| ⇥ updated_at| int32| | false| | 
| ⇥ uploader| int32| | false| Shared file uploader| 
| ⇥ url| string| | false| Shared file url| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.28 Update group file name

> POST  /group/file/update_name

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  file_id| int32| | false| File id| 
|  group_id| int32| | false| Group id| 
|  name| string| | false| New file name| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.29 Update group file name

> PUT  /group/file/update_name

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  file_id| int32| | false| File id| 
|  group_id| int32| | false| Group id| 
|  name| string| | false| New file name| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.30 Upload group file

> POST  /group/file/upload

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  name| string| | false| File name| 
|  size| int32| | false| File size| 
|  type| string| | false| File type| 
|  url| string| | false| File url| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Returned format of group shared files| 
| ⇥ created_at| int32| | false| | 
| ⇥ file_id| int32| | false| Shared file id| 
| ⇥ group_id| int32| | false| Group id| 
| ⇥ name| string| | false| Shared file name| 
| ⇥ size| int32| | false| Shared file size| 
| ⇥ type| string| | false| Shared file type| 
| ⇥ updated_at| int32| | false| | 
| ⇥ uploader| int32| | false| Shared file uploader| 
| ⇥ url| string| | false| Shared file url| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.31 Get group information by group id

> GET  /group/info

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ apply_approval| int32| | false| Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests| 
| ⇥ avatar| string| | false| Group avatar| 
| ⇥ ban_expire_time| int32| | false| Expiration time (second), during which only Admins are allowed to send messages, 0 or less than the current time means no banning, -1 means banned permanently| 
| ⇥ created_at| int32| | false| Creation time| 
| ⇥ description| string| | false| Group description| 
| ⇥ ext| string| | false| Group extension information| 
| ⇥ group_id| int32| | false| Group id| 
| ⇥ history_visible| boolean| | false| History chat visibility settings for new members| 
| ⇥ member_invite| boolean| | false| Group member invitation settings| 
| ⇥ member_modify| boolean| | false| Group information modification settings for members| 
| ⇥ msg_mute_mode| int32| | false| Group message blocking mode| 
| ⇥ msg_push_mode| int32| | false| Push mode of group messages| 
| ⇥ name| string| | false| Group name| 
| ⇥ owner_id| int32| | false| Group Owner id| 
| ⇥ read_ack| boolean| | false| Group message read function settings| 
| ⇥ status| int32| | false| Group state, 0: normal, 1: dissolved| 
| ⇥ type| int32| | false| Group type| 
| ⇥ updated_at| int32| | false| Update time| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.32 Update group avatar

> POST  /group/info/avatar

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| string| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.33 Update group avatar

> PUT  /group/info/avatar

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| string| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.34 Get group information by group id

> POST  /group/info/batch

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_list| array[int32]| | false| Group id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ apply_approval| int32| | false| Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests| 
| ⇥ avatar| string| | false| | 
| ⇥ capacity| int32| | false| | 
| ⇥ count| int32| | false| | 
| ⇥ group_id| int32| | false| | 
| ⇥ msg_mute_mode| int32| | false| Group message blocking settings| 
| ⇥ msg_push_mode| int32| | false| Group message push settings| 
| ⇥ name| string| | false| | 
| ⇥ owner| int32| | false| | 
| ⇥ status| int32| | false| Group state, 0: normal, 1: dissolved| 
| ⇥ type| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.35 Update group description

> POST  /group/info/description

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| string| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.36 Update group description

> PUT  /group/info/description

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| string| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.37 Update extension information

> POST  /group/info/ext

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| string| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.38 Update extension information

> PUT  /group/info/ext

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| string| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.39 Update group name

> POST  /group/info/name

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| string| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.40 Update group name

> PUT  /group/info/name

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| string| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.41 Get group invitation list

> GET  /group/invitation_list

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| cursor| | cursor| 
| limit| | limit| 
| version| | version| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  cursor| string| | false| Cursor for page turning| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 
|  total| int32| | false| Total| 
|  version| int32| | false| Version, not used at present, reserved for extension| 


### Interface Description
> 




## 7.42 Invite to group

> POST  /group/invite

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  reason| string| | false| Invitation reason| 
|  user_list| array[int32]| | false| Invitee id, List type, multiple users can be invited to a group at one time| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.43 Process group invitation by user

> POST  /group/invite/handle

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  approval| boolean| | false| Approval, bool type, true for approval, false for rejection| 
|  group_id| int32| | false| Group id| 
|  user_id| int32| | false| User id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.44 Process group invitation by user

> PUT  /group/invite/handle

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  approval| boolean| | false| Approval, bool type, true for approval, false for rejection| 
|  group_id| int32| | false| Group id| 
|  user_id| int32| | false| User id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.45 Kick member out of group

> POST  /group/kick

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  user_list| array[int32]| | false| User id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.46 Kick member out of group

> DELETE  /group/kick

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  user_list| array[int32]| | false| User id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.47 Member quit group

> POST  /group/leave

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.48 Member quit group

> DELETE  /group/leave

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.49 Get group member list by group id

> GET  /group/member_list

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| cursor| | cursor| 
| group_id| | group_id| 
| limit| | limit| 
| version| | version| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  cursor| string| | false| Cursor for page turning| 
|  data| array[object]| | false| Result data| 
| ⇥ display_name| string| | false| Group member profile| 
| ⇥ join_time| int32| | false| Member join time| 
| ⇥ user_id| int32| | false| User id| 
|  message| string| | false| Error information, null means success| 
|  total| int32| | false| Total| 
|  version| int32| | false| Version, not used at present, reserved for extension| 


### Interface Description
> 




## 7.50 Batch retrieval of group member profiles

> POST  /group/members/display_name

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  user_list| array[int32]| | false| User id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ display_name| string| | false| Group member profile| 
| ⇥ join_time| int32| | false| Member join time| 
| ⇥ user_id| int32| | false| User id| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.51 Set group message blocking mode

> POST  /group/msg/mute_mode

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  msg_mute_mode| int32| | false| Group message blocking mode: 0: No blocking; 1: Blocking local message notifications; 2: Blocking messages, not receiving messages| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.52 Set group message blocking mode

> PUT  /group/msg/mute_mode

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  msg_mute_mode| int32| | false| Group message blocking mode: 0: No blocking; 1: Blocking local message notifications; 2: Blocking messages, not receiving messages| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.53 Set group message pushing mode

> POST  /group/msg/push_mode

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  msg_push_mode| int32| | false| Group message push type: 0: Receive all pushes; 1: Do not accept push; 2: Receive Admin and @ pushes; 3. Only receive Admin pushes; 4: Only receive @ pushes| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.54 Set group message pushing mode

> PUT  /group/msg/push_mode

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  msg_push_mode| int32| | false| Group message push type: 0: Receive all pushes; 1: Do not accept push; 2: Receive Admin and @ pushes; 3. Only receive Admin pushes; 4: Only receive @ pushes| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.55 Get public group list

> GET  /group/public_list

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[int32]| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.56 Group invitation via QR code

> POST  /group/qrcode/invite

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  qr_info| string| | false| | 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.57 Get Group invitation QR code

> GET  /group/qrcode/sign

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ create_at| int32| | false| QR code generation time| 
| ⇥ expire_at| int32| | false| QR code expiration time| 
| ⇥ qr_info| string| | false| QR code information| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.58 Get group settings

> GET  /group/settings

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Query Param
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| group_id| | group_id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ apply_approval| int32| | false| Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests| 
| ⇥ avatar| string| | false| Group avatar| 
| ⇥ ban_expire_time| int32| | false| Expiration time (second), during which only Admins are allowed to send messages, 0 or less than the current time means no banning, -1 means banned permanently| 
| ⇥ created_at| int32| | false| Creation time| 
| ⇥ description| string| | false| Group description| 
| ⇥ ext| string| | false| Group extension information| 
| ⇥ group_id| int32| | false| Group id| 
| ⇥ history_visible| boolean| | false| History chat visibility settings for new members| 
| ⇥ member_invite| boolean| | false| Group member invitation settings| 
| ⇥ member_modify| boolean| | false| Group information modification settings for members| 
| ⇥ msg_mute_mode| int32| | false| Group message blocking mode| 
| ⇥ msg_push_mode| int32| | false| Push mode of group messages| 
| ⇥ name| string| | false| Group name| 
| ⇥ owner_id| int32| | false| Group Owner id| 
| ⇥ read_ack| boolean| | false| Group message read function settings| 
| ⇥ status| int32| | false| Group state, 0: normal, 1: dissolved| 
| ⇥ type| int32| | false| Group type| 
| ⇥ updated_at| int32| | false| Update time| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.59 Update group settings - whether to allow member invitations

> POST  /group/settings/allow_member_invitation

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| boolean| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.60 Update group settings - whether to allow member invitations

> PUT  /group/settings/allow_member_invitation

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| boolean| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.61 Update group settings - whether group members can modify group information

> POST  /group/settings/allow_member_modify

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| boolean| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.62 Update group settings - whether group members can modify group information

> PUT  /group/settings/allow_member_modify

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| boolean| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.63 Ban all members, only Admins can send messages

> POST  /group/settings/ban_all

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  duration| int32| | false| Duration of banned in minutes| 
|  group_id| int32| | false| Group id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ ban_expire_time| int32| | false| Expiration time of banning all members| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.64 Update group settings - whether to enable “mark after read”

> POST  /group/settings/enable_read_ack

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| boolean| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.65 Update group settings - whether to enable “mark after read”

> PUT  /group/settings/enable_read_ack

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| boolean| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.66 Update group settings - whether group chat history visible to new members

> POST  /group/settings/history_visible

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| boolean| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.67 Update group settings - whether group chat history visible to new members

> PUT  /group/settings/history_visible

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  value| boolean| | false| Update content| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.68 Update group settings - whether group membership request needs Admin approval

> POST  /group/settings/require_admin_approval

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  apply_approval| int32| | false| Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests| 
|  group_id| int32| | false| Group id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.69 Update group settings - whether group membership request needs Admin approval

> PUT  /group/settings/require_admin_approval

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  apply_approval| int32| | false| Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests| 
|  group_id| int32| | false| Group id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.70 Unban all members

> POST  /group/settings/unban_all

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| boolean| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.71 Transfer of group Owner

> POST  /group/transfer

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  new_owner| int32| | false| User_id of new group Owner| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.72 Transfer of group Owner

> PUT  /group/transfer

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  new_owner| int32| | false| User_id of new group Owner| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| | 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.73 Remove user from ban list

> POST  /group/unban

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  user_list| array[int32]| | false| User id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.74 Remove user from blacklist

> POST  /group/unblock

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  user_list| array[int32]| | false| User id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.75 Remove user from blacklist

> DELETE  /group/unblock

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  group_id| int32| | false| Group id| 
|  user_list| array[int32]| | false| User id list| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[object]| | false| Result data| 
| ⇥ reason| string| | false| | 
| ⇥ result| string| | false| | 
| ⇥ user_id| int32| | false| | 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 




## 7.76 Get the list of groups for the user

> GET  /group/user_joined

### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| | app_id| | App ID| | group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| | user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

### Response Body
● 200 Response data format:JSON
|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| array[int32]| | false| Result data| 
|  message| string| | false| Error information, null means success| 


### Interface Description
> 



