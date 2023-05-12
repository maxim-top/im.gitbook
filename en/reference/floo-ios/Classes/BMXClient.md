# BMXClient Class Reference

  **Inherits from** <a href="../Classes/BMXNetworkListener.md">BMXNetworkListener</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Client instance

## Properties

<a name="//api/name/chatService" title="chatService"></a>
### chatService

`@property (nonatomic, strong, readonly) BMXChatService *chatService`

<a name="//api/name/groupService" title="groupService"></a>
### groupService

`@property (nonatomic, strong, readonly) BMXGroupService *groupService`

<a name="//api/name/pushService" title="pushService"></a>
### pushService

`@property (nonatomic, strong, readonly) BMXPushService *pushService`

<a name="//api/name/rosterService" title="rosterService"></a>
### rosterService

`@property (nonatomic, strong, readonly) BMXRosterService *rosterService`

<a name="//api/name/rtcService" title="rtcService"></a>
### rtcService

`@property (nonatomic, strong, readonly) BMXRTCService *rtcService`

<a name="//api/name/userService" title="userService"></a>
### userService

`@property (nonatomic, strong, readonly) BMXUserService *userService`

<a title="Class Methods" name="class_methods"></a>
## Class Methods

<a name="//api/name/createWithConfig:" title="createWithConfig:"></a>
### createWithConfig:

Create a BMXClient

`+ (BMXClient *)createWithConfig:(BMXSDKConfig *)*config*`

#### Parameters

*config*  
   <a href="../Classes/BMXSDKConfig.md">BMXSDKConfig</a> SDK config created

#### Return Value
BMXClient

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sharedClient" title="sharedClient"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createWithConfig:" %}{% endlanying_code_snippet %}
```
### sharedClient

`+ (instancetype)sharedClient`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/changeAppIdWithAppId:" title="changeAppIdWithAppId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="sharedClient" %}{% endlanying_code_snippet %}
```
### changeAppIdWithAppId:

`- (BMXErrorCode)changeAppIdWithAppId:(NSString *)*appId*`

<a name="//api/name/changeAppIdWithAppId:appSecret:" title="changeAppIdWithAppId:appSecret:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="changeAppIdWithAppId:" %}{% endlanying_code_snippet %}
```
### changeAppIdWithAppId:appSecret:

Change appId，also works on appId in BMXConfig

`- (BMXErrorCode)changeAppIdWithAppId:(NSString *)*appId* appSecret:(NSString *)*appSecret*`

#### Parameters

*appId*  
   The new appId  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/changeAppIdWithAppId:appSecret:completion:" title="changeAppIdWithAppId:appSecret:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="changeAppIdWithAppId:appSecret:" %}{% endlanying_code_snippet %}
```
### changeAppIdWithAppId:appSecret:completion:

Change appId，also works on appId in BMXConfig

`- (void)changeAppIdWithAppId:(NSString *)*appId* appSecret:(NSString *)*appSecret* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*appId*  
   The new appId

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/changeAppIdWithAppId:completion:" title="changeAppIdWithAppId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="changeAppIdWithAppId:appSecret:completion:" %}{% endlanying_code_snippet %}
```
### changeAppIdWithAppId:completion:

`- (void)changeAppIdWithAppId:(NSString *)*appId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

<a name="//api/name/connectStatus" title="connectStatus"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="changeAppIdWithAppId:completion:" %}{% endlanying_code_snippet %}
```
### connectStatus

Get connection status to the server

`- (BMXConnectStatus)connectStatus`

#### Return Value
<a href="../Constants/BMXConnectStatus.md">BMXConnectStatus</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="connectStatus" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/deleteAccountWithPassword:" title="deleteAccountWithPassword:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### deleteAccountWithPassword:

Delete my account

`- (BMXErrorCode)deleteAccountWithPassword:(NSString *)*password*`

#### Parameters

*password*  
   The password for my account  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deleteAccountWithPassword:completion:" title="deleteAccountWithPassword:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="deleteAccountWithPassword:" %}{% endlanying_code_snippet %}
```
### deleteAccountWithPassword:completion:

Delete my account

`- (void)deleteAccountWithPassword:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*password*  
   The password for my account

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/disconnect" title="disconnect"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="deleteAccountWithPassword:completion:" %}{% endlanying_code_snippet %}
```
### disconnect

Disconnect from the server

`- (void)disconnect`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/disconnectWithCompletion:" title="disconnectWithCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="disconnect" %}{% endlanying_code_snippet %}
```
### disconnectWithCompletion:

Disconnect from the server

`- (void)disconnectWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fastSignInByIdWithUid:password:" title="fastSignInByIdWithUid:password:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="disconnectWithCompletion:" %}{% endlanying_code_snippet %}
```
### fastSignInByIdWithUid:password:

Fast login by user ID (A successful login required)

`- (BMXErrorCode)fastSignInByIdWithUid:(long long)*uid* password:(NSString *)*password*`

#### Parameters

*uid*  
   The user ID  

*password*  
   The password  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fastSignInByIdWithUid:password:completion:" title="fastSignInByIdWithUid:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="fastSignInByIdWithUid:password:" %}{% endlanying_code_snippet %}
```
### fastSignInByIdWithUid:password:completion:

Fast login by user ID (A successful login required)

`- (void)fastSignInByIdWithUid:(long long)*uid* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*uid*  
   The user ID

*password*  
   The password

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fastSignInByNameWithName:password:" title="fastSignInByNameWithName:password:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="fastSignInByIdWithUid:password:completion:" %}{% endlanying_code_snippet %}
```
### fastSignInByNameWithName:password:

Fast login by username (A successful login required)

`- (BMXErrorCode)fastSignInByNameWithName:(NSString *)*name* password:(NSString *)*password*`

#### Parameters

*name*  
   The username

*password*  
   The password

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fastSignInByNameWithName:password:completion:" title="fastSignInByNameWithName:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="fastSignInByNameWithName:password:" %}{% endlanying_code_snippet %}
```
### fastSignInByNameWithName:password:completion:

Fast login by username (A successful login required)

`- (void)fastSignInByNameWithName:(NSString *)*name* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*name*  
   The username  

*password*  
   The password

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getSDKConfig" title="getSDKConfig"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="fastSignInByNameWithName:password:completion:" %}{% endlanying_code_snippet %}
```
### getSDKConfig

Get SDK config

`- (BMXSDKConfig *)getSDKConfig`

#### Return Value
<a href="../Classes/BMXSDKConfig.md">BMXSDKConfig</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initializeServerConfigWithIsLocal:" title="initializeServerConfigWithIsLocal:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getSDKConfig" %}{% endlanying_code_snippet %}
```
### initializeServerConfigWithIsLocal:

Initialize server config to accelerate login speed

`- (BMXErrorCode)initializeServerConfigWithIsLocal:(BOOL)*isLocal*`

#### Parameters

*isLocal*  
   true for loading from local file, or downloading from server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initializeServerConfigWithIsLocal:completion:" title="initializeServerConfigWithIsLocal:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initializeServerConfigWithIsLocal:" %}{% endlanying_code_snippet %}
```
### initializeServerConfigWithIsLocal:completion:

Initialize server config to accelerate login speed

`- (void)initializeServerConfigWithIsLocal:(BOOL)*isLocal* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*isLocal*  
   true for loading from local file, or downloading from server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onNetworkChangedWithType:reconnect:" title="onNetworkChangedWithType:reconnect:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initializeServerConfigWithIsLocal:completion:" %}{% endlanying_code_snippet %}
```
### onNetworkChangedWithType:reconnect:

Send network status change events to SDK

`- (void)onNetworkChangedWithType:(BMXNetworkType)*type* reconnect:(BOOL)*reconnect*`

#### Parameters

*type*  
   New network type  

*reconnect*  
   Need to reconnect or not

#### Declared In
* `floo_proxy.h`

<a name="//api/name/reconnect" title="reconnect"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="onNetworkChangedWithType:reconnect:" %}{% endlanying_code_snippet %}
```
### reconnect

Enforce reconnection

`- (void)reconnect`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/reconnectWithCompletion:" title="reconnectWithCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="reconnect" %}{% endlanying_code_snippet %}
```
### reconnectWithCompletion:

Enforce reconnection

`- (void)reconnectWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sendMessageWithMsg:" title="sendMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="reconnectWithCompletion:" %}{% endlanying_code_snippet %}
```
### sendMessageWithMsg:

Send a message

`- (void)sendMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sendMessageWithMsg:completion:" title="sendMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="sendMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### sendMessageWithMsg:completion:

Send a message

`- (void)sendMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signInByIdWithArg1:password:" title="signInByIdWithArg1:password:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="sendMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### signInByIdWithArg1:password:

Sign in by username

`- (BMXErrorCode)signInByIdWithArg1:(long long)*arg1* password:(NSString *)*password*`

#### Parameters

*password*  
   The password 

*name*  
   THe username

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signInByIdWithArg1:password:completion:" title="signInByIdWithArg1:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signInByIdWithArg1:password:" %}{% endlanying_code_snippet %}
```
### signInByIdWithArg1:password:completion:

Sign in by user ID

`- (void)signInByIdWithArg1:(long long)*arg1* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*password*  
   The password

*int64_t*  
   The user ID  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signInByNameWithName:password:" title="signInByNameWithName:password:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signInByIdWithArg1:password:completion:" %}{% endlanying_code_snippet %}
```
### signInByNameWithName:password:

Sign in by username

`- (BMXErrorCode)signInByNameWithName:(NSString *)*name* password:(NSString *)*password*`

#### Parameters

*name*  
   The username  

*password*  
   The password 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signInByNameWithName:password:completion:" title="signInByNameWithName:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signInByNameWithName:password:" %}{% endlanying_code_snippet %}
```
### signInByNameWithName:password:completion:

Sign in by username

`- (void)signInByNameWithName:(NSString *)*name* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*name*  
   The username 

*password*  
   The password  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signInStatus" title="signInStatus"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signInByNameWithName:password:completion:" %}{% endlanying_code_snippet %}
```
### signInStatus

Get login status

`- (BMXSignInStatus)signInStatus`

#### Return Value
<a href="../Constants/BMXSignInStatus.md">BMXSignInStatus</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signOut" title="signOut"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signInStatus" %}{% endlanying_code_snippet %}
```
### signOut

`- (BMXErrorCode)signOut`

<a name="//api/name/signOutWithCompletion:" title="signOutWithCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signOut" %}{% endlanying_code_snippet %}
```
### signOutWithCompletion:

`- (void)signOutWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

<a name="//api/name/signOutWithUid:" title="signOutWithUid:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signOutWithCompletion:" %}{% endlanying_code_snippet %}
```
### signOutWithUid:

`- (BMXErrorCode)signOutWithUid:(long long)*uid*`

<a name="//api/name/signOutWithUid:completion:" title="signOutWithUid:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signOutWithUid:" %}{% endlanying_code_snippet %}
```
### signOutWithUid:completion:

`- (void)signOutWithUid:(long long)*uid* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

<a name="//api/name/signOutWithUid:ignoreUnbindDevice:" title="signOutWithUid:ignoreUnbindDevice:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signOutWithUid:completion:" %}{% endlanying_code_snippet %}
```
### signOutWithUid:ignoreUnbindDevice:

Sign out

`- (BMXErrorCode)signOutWithUid:(long long)*uid* ignoreUnbindDevice:(BOOL)*ignoreUnbindDevice*`

#### Parameters

*uid*  
   My user ID  

*ignoreUnbindDevice*  
   Ignore unbinding device on sign out

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signOutWithUid:ignoreUnbindDevice:completion:" title="signOutWithUid:ignoreUnbindDevice:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signOutWithUid:ignoreUnbindDevice:" %}{% endlanying_code_snippet %}
```
### signOutWithUid:ignoreUnbindDevice:completion:

Sign out

`- (void)signOutWithUid:(long long)*uid* ignoreUnbindDevice:(BOOL)*ignoreUnbindDevice* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*uid*  
   My user ID    

*ignoreUnbindDevice*  
   Ignore unbinding device on sign out

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signUpNewUserWithUsername:password:bmxUserProfilePtr:" title="signUpNewUserWithUsername:password:bmxUserProfilePtr:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signOutWithUid:ignoreUnbindDevice:completion:" %}{% endlanying_code_snippet %}
```
### signUpNewUserWithUsername:password:bmxUserProfilePtr:

Sign up a new account

`- (BMXErrorCode)signUpNewUserWithUsername:(NSString *)*username* password:(NSString *)*password* bmxUserProfilePtr:(BMXUserProfile *)*bmxUserProfilePtr*`

#### Parameters

*username*  
   The username

*password*  
   The password

*bmxUserProfilePtr*  
   Profile of the new user

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signUpNewUserWithUsername:password:completion:" title="signUpNewUserWithUsername:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signUpNewUserWithUsername:password:bmxUserProfilePtr:" %}{% endlanying_code_snippet %}
```
### signUpNewUserWithUsername:password:completion:

Sign up a new account

`- (void)signUpNewUserWithUsername:(NSString *)*username* password:(NSString *)*password* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *aError ))*resBlock*`

#### Parameters

*username*  
   The username  

*password*  
   The password

*bmxUserProfilePtr*  
   Profile of the new user

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="signUpNewUserWithUsername:password:completion:" %}{% endlanying_code_snippet %}
```
