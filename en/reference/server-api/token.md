
## 5    token interface

## 5.1  Get ordinary user token by user ID and password

> POST  /token/id

#### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| 
| app_id| | App ID| 
| group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| 
| user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

#### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  device_guid| string| | false| Device ID, if set, returns PushToken| 
|  password| string| | false| | 
|  user_id| int32| | false| User ID, for login by user ID only| 

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Token information| 
| ⇥ access_key_secret| string| | false| File key| 
| ⇥ encrypt_type| int32| | false| Whether to enable encrypted connection| 
| ⇥ expire| int32| | false| Expiration timestamp| 
| ⇥ public_key| string| | false| Public key| 
| ⇥ push_token| string| | false| Push Token| 
| ⇥ store_token| string| | false| File token| 
| ⇥ token| string| | false| Access token| 
| ⇥ user_id| int32| | false| User ID| 
|  message| string| | false| Error information, null means success| 


#### Interface Description
> 




## 5.2  Get ordinary user token by username/mobile number/email

> POST  /token/login

#### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| 
| app_id| | App ID| 
| group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| 
| user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

#### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  device_guid| string| | false| Device ID, if set, returns PushToken| 
|  login_name| string| | false| Login name, which can be mobile number, email, username| 
|  password| string| | false| | 

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Token information| 
| ⇥ access_key_secret| string| | false| File key| 
| ⇥ encrypt_type| int32| | false| Whether to enable encrypted connection| 
| ⇥ expire| int32| | false| Expiration timestamp| 
| ⇥ public_key| string| | false| Public key| 
| ⇥ push_token| string| | false| Push Token| 
| ⇥ store_token| string| | false| File token| 
| ⇥ token| string| | false| Access token| 
| ⇥ user_id| int32| | false| User ID| 
|  message| string| | false| Error information, null means success| 


#### Interface Description
> 




## 5.3  Get ordinary user token by username and password

> POST  /token/user

#### Request Header
|  Parameter name |  Default |  Description | 
|  ------ |  ------ |  ------ | 
| access-token| | Token| 
| app_id| | App ID| 
| group_id| | This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID| 
| user_id| | This field can be set only if access-token is a user token, means call this interface as a group member for this user ID| 

#### Request Body
|  Parameter name |  Data Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  device_guid| string| | false| Device ID, if set, returns PushToken| 
|  name| string| | false| Username, for login by username only| 
|  password| string| | false| | 

#### Response Body
● 200 Response data format:JSON

|  Parameter name |  Type |  Default |  Not null |  Description | 
|  ------ |  ------ |  ------ |  ------ |  ------ | 
|  code| int32| | false| Return code, 200 is success| 
|  data| object| | false| Token information| 
| ⇥ access_key_secret| string| | false| File key| 
| ⇥ encrypt_type| int32| | false| Whether to enable encrypted connection| 
| ⇥ expire| int32| | false| Expiration timestamp| 
| ⇥ public_key| string| | false| Public key| 
| ⇥ push_token| string| | false| Push Token| 
| ⇥ store_token| string| | false| File token| 
| ⇥ token| string| | false| Access token| 
| ⇥ user_id| int32| | false| User ID| 
|  message| string| | false| Error information, null means success| 


#### Interface Description
> 


