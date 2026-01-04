# BMXClient Class Reference

  **Inherits from** <a href="../Classes/BMXNetworkListener.md">BMXNetworkListener</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 客户端实例

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

创建BMXClient

`+ (BMXClient *)createWithConfig:(BMXSDKConfig *)*config*`

#### Parameters

*config*  
   客户端本地已经创建好的<a href="../Classes/BMXSDKConfig.md">BMXSDKConfig</a> SDK配置对象  

#### Return Value
BMXClient

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sharedClient" title="sharedClient"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="createWithConfig:" %}{% endlanying_code_snippet %}
```
### sharedClient

`+ (instancetype)sharedClient`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/changeAppIdWithAppId:" title="changeAppIdWithAppId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="sharedClient" %}{% endlanying_code_snippet %}
```
### changeAppIdWithAppId:

`- (BMXErrorCode)changeAppIdWithAppId:(NSString *)*appId*`

<a name="//api/name/changeAppIdWithAppId:appSecret:" title="changeAppIdWithAppId:appSecret:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="changeAppIdWithAppId:" %}{% endlanying_code_snippet %}
```
### changeAppIdWithAppId:appSecret:

更改SDK的appId，本操作会同时更新BMXConfig中的appId。

`- (BMXErrorCode)changeAppIdWithAppId:(NSString *)*appId* appSecret:(NSString *)*appSecret*`

#### Parameters

*appId*  
   新变更的appId  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/changeAppIdWithAppId:appSecret:completion:" title="changeAppIdWithAppId:appSecret:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="changeAppIdWithAppId:appSecret:" %}{% endlanying_code_snippet %}
```
### changeAppIdWithAppId:appSecret:completion:

更改SDK的appId，本操作会同时更新BMXConfig中的appId。

`- (void)changeAppIdWithAppId:(NSString *)*appId* appSecret:(NSString *)*appSecret* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*appId*  
   新变更的appId  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/changeAppIdWithAppId:completion:" title="changeAppIdWithAppId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="changeAppIdWithAppId:appSecret:completion:" %}{% endlanying_code_snippet %}
```
### changeAppIdWithAppId:completion:

`- (void)changeAppIdWithAppId:(NSString *)*appId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

<a name="//api/name/connectStatus" title="connectStatus"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="changeAppIdWithAppId:completion:" %}{% endlanying_code_snippet %}
```
### connectStatus

获取当前和服务器的连接状态

`- (BMXConnectStatus)connectStatus`

#### Return Value
<a href="../Constants/BMXConnectStatus.md">BMXConnectStatus</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="connectStatus" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/deleteAccountWithPassword:" title="deleteAccountWithPassword:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="dealloc" %}{% endlanying_code_snippet %}
```
### deleteAccountWithPassword:

删除账号

`- (BMXErrorCode)deleteAccountWithPassword:(NSString *)*password*`

#### Parameters

*password*  
   密码  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deleteAccountWithPassword:completion:" title="deleteAccountWithPassword:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="deleteAccountWithPassword:" %}{% endlanying_code_snippet %}
```
### deleteAccountWithPassword:completion:

删除账号

`- (void)deleteAccountWithPassword:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*password*  
   密码  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/disconnect" title="disconnect"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="deleteAccountWithPassword:completion:" %}{% endlanying_code_snippet %}
```
### disconnect

断开网络连接

`- (void)disconnect`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/disconnectWithCompletion:" title="disconnectWithCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="disconnect" %}{% endlanying_code_snippet %}
```
### disconnectWithCompletion:

断开网络连接

`- (void)disconnectWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fastSignInByIdWithUid:password:" title="fastSignInByIdWithUid:password:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="disconnectWithCompletion:" %}{% endlanying_code_snippet %}
```
### fastSignInByIdWithUid:password:

通过用户ID快速登录（要求之前成功登录过，登录速度较快）

`- (BMXErrorCode)fastSignInByIdWithUid:(long long)*uid* password:(NSString *)*password*`

#### Parameters

*uid*  
   用户id  

*password*  
   用户密码(用于sdk在内部token到期时自动更新用户token)  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fastSignInByIdWithUid:password:completion:" title="fastSignInByIdWithUid:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="fastSignInByIdWithUid:password:" %}{% endlanying_code_snippet %}
```
### fastSignInByIdWithUid:password:completion:

通过用户ID快速登录（要求之前成功登录过，登录速度较快）

`- (void)fastSignInByIdWithUid:(long long)*uid* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*uid*  
   用户id  

*password*  
   用户密码(用于sdk在内部token到期时自动更新用户token)  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fastSignInByNameWithName:password:" title="fastSignInByNameWithName:password:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="fastSignInByIdWithUid:password:completion:" %}{% endlanying_code_snippet %}
```
### fastSignInByNameWithName:password:

通过用户名快速登录（要求之前成功登录过，登录速度较快）

`- (BMXErrorCode)fastSignInByNameWithName:(NSString *)*name* password:(NSString *)*password*`

#### Parameters

*name*  
   用户名  

*password*  
   用户密码(用于sdk在内部token到期时自动更新用户token)  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fastSignInByNameWithName:password:completion:" title="fastSignInByNameWithName:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="fastSignInByNameWithName:password:" %}{% endlanying_code_snippet %}
```
### fastSignInByNameWithName:password:completion:

通过用户名快速登录（要求之前成功登录过，登录速度较快）

`- (void)fastSignInByNameWithName:(NSString *)*name* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*name*  
   用户名  

*password*  
   用户密码(用于sdk在内部token到期时自动更新用户token)  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getSDKConfig" title="getSDKConfig"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="fastSignInByNameWithName:password:completion:" %}{% endlanying_code_snippet %}
```
### getSDKConfig

获取SDK设置

`- (BMXSDKConfig *)getSDKConfig`

#### Return Value
<a href="../Classes/BMXSDKConfig.md">BMXSDKConfig</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initializeServerConfigWithIsLocal:" title="initializeServerConfigWithIsLocal:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="getSDKConfig" %}{% endlanying_code_snippet %}
```
### initializeServerConfigWithIsLocal:

获取app的服务器网络配置，在初始化SDK之后登陆之前调用，可以提前获取服务器配置加快登陆速度。

`- (BMXErrorCode)initializeServerConfigWithIsLocal:(BOOL)*isLocal*`

#### Parameters

*isLocal*  
   为true则使用本地缓存的dns配置，为false则从服务器获取最新的配置。  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initializeServerConfigWithIsLocal:completion:" title="initializeServerConfigWithIsLocal:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="initializeServerConfigWithIsLocal:" %}{% endlanying_code_snippet %}
```
### initializeServerConfigWithIsLocal:completion:

获取app的服务器网络配置，在初始化SDK之后登陆之前调用，可以提前获取服务器配置加快登陆速度。

`- (void)initializeServerConfigWithIsLocal:(BOOL)*isLocal* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*isLocal*  
   为true则使用本地缓存的dns配置，为false则从服务器获取最新的配置。  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/onNetworkChangedWithType:reconnect:" title="onNetworkChangedWithType:reconnect:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="initializeServerConfigWithIsLocal:completion:" %}{% endlanying_code_snippet %}
```
### onNetworkChangedWithType:reconnect:

处理网络状态发送变化

`- (void)onNetworkChangedWithType:(BMXNetworkType)*type* reconnect:(BOOL)*reconnect*`

#### Parameters

*type*  
   变化后的网络类型  

*reconnect*  
   网络是否需要重连  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/reconnect" title="reconnect"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="onNetworkChangedWithType:reconnect:" %}{% endlanying_code_snippet %}
```
### reconnect

强制重新连接

`- (void)reconnect`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/reconnectWithCompletion:" title="reconnectWithCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="reconnect" %}{% endlanying_code_snippet %}
```
### reconnectWithCompletion:

强制重新连接

`- (void)reconnectWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sendMessageWithMsg:" title="sendMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="reconnectWithCompletion:" %}{% endlanying_code_snippet %}
```
### sendMessageWithMsg:

发送消息，消息状态变化会通过listener通知，在发送群组消息且指定的群组为开启群组已读回执的情况下，
该接口会自动获取群成员列表id并且填充到message config中去，无需客户端自己进行群组成员列表的填充操作。

`- (void)sendMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   发送的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sendMessageWithMsg:completion:" title="sendMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="sendMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### sendMessageWithMsg:completion:

发送消息，消息状态变化会通过listener通知，在发送群组消息且指定的群组为开启群组已读回执的情况下，
该接口会自动获取群成员列表id并且填充到message config中去，无需客户端自己进行群组成员列表的填充操作。

`- (void)sendMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   发送的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signInByIdWithArg1:password:" title="signInByIdWithArg1:password:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="sendMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### signInByIdWithArg1:password:

通过用户名登录

`- (BMXErrorCode)signInByIdWithArg1:(long long)*arg1* password:(NSString *)*password*`

#### Parameters

*password*  
   用户密码  

*name*  
   用户名  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signInByIdWithArg1:password:completion:" title="signInByIdWithArg1:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signInByIdWithArg1:password:" %}{% endlanying_code_snippet %}
```
### signInByIdWithArg1:password:completion:

通过用户ID登录

`- (void)signInByIdWithArg1:(long long)*arg1* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*password*  
   用户密码  

*int64_t*  
   用户id  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signInByNameWithName:password:" title="signInByNameWithName:password:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signInByIdWithArg1:password:completion:" %}{% endlanying_code_snippet %}
```
### signInByNameWithName:password:

通过用户名登录

`- (BMXErrorCode)signInByNameWithName:(NSString *)*name* password:(NSString *)*password*`

#### Parameters

*name*  
   用户名  

*password*  
   用户密码  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signInByNameWithName:password:completion:" title="signInByNameWithName:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signInByNameWithName:password:" %}{% endlanying_code_snippet %}
```
### signInByNameWithName:password:completion:

通过用户名登录

`- (void)signInByNameWithName:(NSString *)*name* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*name*  
   用户名  

*password*  
   用户密码  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signInStatus" title="signInStatus"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signInByNameWithName:password:completion:" %}{% endlanying_code_snippet %}
```
### signInStatus

获取当前的登录状态

`- (BMXSignInStatus)signInStatus`

#### Return Value
<a href="../Constants/BMXSignInStatus.md">BMXSignInStatus</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signOut" title="signOut"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signInStatus" %}{% endlanying_code_snippet %}
```
### signOut

`- (BMXErrorCode)signOut`

<a name="//api/name/signOutWithCompletion:" title="signOutWithCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signOut" %}{% endlanying_code_snippet %}
```
### signOutWithCompletion:

`- (void)signOutWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

<a name="//api/name/signOutWithUid:" title="signOutWithUid:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signOutWithCompletion:" %}{% endlanying_code_snippet %}
```
### signOutWithUid:

`- (BMXErrorCode)signOutWithUid:(long long)*uid*`

<a name="//api/name/signOutWithUid:completion:" title="signOutWithUid:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signOutWithUid:" %}{% endlanying_code_snippet %}
```
### signOutWithUid:completion:

`- (void)signOutWithUid:(long long)*uid* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

<a name="//api/name/signOutWithUid:ignoreUnbindDevice:" title="signOutWithUid:ignoreUnbindDevice:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signOutWithUid:completion:" %}{% endlanying_code_snippet %}
```
### signOutWithUid:ignoreUnbindDevice:

退出登录

`- (BMXErrorCode)signOutWithUid:(long long)*uid* ignoreUnbindDevice:(BOOL)*ignoreUnbindDevice*`

#### Parameters

*uid*  
   退出用户的uid（默认输入0则退出当前登陆用户）  

*ignoreUnbindDevice*  
   用户退出时是否忽略解绑定设备操作。对应某些服务器不可访问的情况下忽略服务器解绑定设备操作直接强制退出时设置为true  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signOutWithUid:ignoreUnbindDevice:completion:" title="signOutWithUid:ignoreUnbindDevice:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signOutWithUid:ignoreUnbindDevice:" %}{% endlanying_code_snippet %}
```
### signOutWithUid:ignoreUnbindDevice:completion:

退出登录

`- (void)signOutWithUid:(long long)*uid* ignoreUnbindDevice:(BOOL)*ignoreUnbindDevice* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*uid*  
   退出用户的uid（默认输入0则退出当前登陆用户）  

*ignoreUnbindDevice*  
   用户退出时是否忽略解绑定设备操作。对应某些服务器不可访问的情况下忽略服务器解绑定设备操作直接强制退出时设置为true  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signUpNewUserWithUsername:password:bmxUserProfilePtr:" title="signUpNewUserWithUsername:password:bmxUserProfilePtr:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signOutWithUid:ignoreUnbindDevice:completion:" %}{% endlanying_code_snippet %}
```
### signUpNewUserWithUsername:password:bmxUserProfilePtr:

注册新用户，username和password是必填参数

`- (BMXErrorCode)signUpNewUserWithUsername:(NSString *)*username* password:(NSString *)*password* bmxUserProfilePtr:(BMXUserProfile *)*bmxUserProfilePtr*`

#### Parameters

*username*  
   用户名  

*password*  
   用户密码  

*bmxUserProfilePtr*  
   注册成功后从该函数处获取新注册用户的Profile信息，初始传入指向为空的shared_ptr对象即可。  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/signUpNewUserWithUsername:password:completion:" title="signUpNewUserWithUsername:password:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signUpNewUserWithUsername:password:bmxUserProfilePtr:" %}{% endlanying_code_snippet %}
```
### signUpNewUserWithUsername:password:completion:

注册新用户，username和password是必填参数

`- (void)signUpNewUserWithUsername:(NSString *)*username* password:(NSString *)*password* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *aError ))*resBlock*`

#### Parameters

*username*  
   用户名  

*password*  
   用户密码  

*bmxUserProfilePtr*  
   注册成功后从该函数处获取新注册用户的Profile信息，初始传入指向为空的shared_ptr对象即可。  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXClient",function="signUpNewUserWithUsername:password:completion:" %}{% endlanying_code_snippet %}
```
