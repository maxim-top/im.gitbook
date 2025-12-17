# BMXClient Class Reference

**Inherits from** [BMXNetworkListener](BMXNetworkListener.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 客户端实例

## Properties

### chatService

`@property (nonatomic, strong, readonly) BMXChatService *chatService`

### groupService

`@property (nonatomic, strong, readonly) BMXGroupService *groupService`

### pushService

`@property (nonatomic, strong, readonly) BMXPushService *pushService`

### rosterService

`@property (nonatomic, strong, readonly) BMXRosterService *rosterService`

### rtcService

`@property (nonatomic, strong, readonly) BMXRTCService *rtcService`

### userService

`@property (nonatomic, strong, readonly) BMXUserService *userService`

## Class Methods

### createWithConfig:

创建BMXClient

`+ (BMXClient *)createWithConfig:(BMXSDKConfig *)*config*`

#### Parameters

_config_\
客户端本地已经创建好的[BMXSDKConfig](BMXSDKConfig.md) SDK配置对象

#### Return Value

BMXClient

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### sharedClient

`+ (instancetype)sharedClient`

## Instance Methods

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### changeAppIdWithAppId:

`- (BMXErrorCode)changeAppIdWithAppId:(NSString *)*appId*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### changeAppIdWithAppId:appSecret:

更改SDK的appId，本操作会同时更新BMXConfig中的appId。

`- (BMXErrorCode)changeAppIdWithAppId:(NSString *)*appId* appSecret:(NSString *)*appSecret*`

#### Parameters

_appId_\
新变更的appId

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### changeAppIdWithAppId:appSecret:completion:

更改SDK的appId，本操作会同时更新BMXConfig中的appId。

`- (void)changeAppIdWithAppId:(NSString *)*appId* appSecret:(NSString *)*appSecret* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_appId_\
新变更的appId

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### changeAppIdWithAppId:completion:

`- (void)changeAppIdWithAppId:(NSString *)*appId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### connectStatus

获取当前和服务器的连接状态

`- (BMXConnectStatus)connectStatus`

#### Return Value

[BMXConnectStatus](../Constants/BMXConnectStatus.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### deleteAccountWithPassword:

删除账号

`- (BMXErrorCode)deleteAccountWithPassword:(NSString *)*password*`

#### Parameters

_password_\
密码

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### deleteAccountWithPassword:completion:

删除账号

`- (void)deleteAccountWithPassword:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_password_\
密码

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### disconnect

断开网络连接

`- (void)disconnect`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### disconnectWithCompletion:

断开网络连接

`- (void)disconnectWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### fastSignInByIdWithUid:password:

通过用户ID快速登录（要求之前成功登录过，登录速度较快）

`- (BMXErrorCode)fastSignInByIdWithUid:(long long)*uid* password:(NSString *)*password*`

#### Parameters

_uid_\
用户id

_password_\
用户密码(用于sdk在内部token到期时自动更新用户token)

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### fastSignInByIdWithUid:password:completion:

通过用户ID快速登录（要求之前成功登录过，登录速度较快）

`- (void)fastSignInByIdWithUid:(long long)*uid* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_uid_\
用户id

_password_\
用户密码(用于sdk在内部token到期时自动更新用户token)

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### fastSignInByNameWithName:password:

通过用户名快速登录（要求之前成功登录过，登录速度较快）

`- (BMXErrorCode)fastSignInByNameWithName:(NSString *)*name* password:(NSString *)*password*`

#### Parameters

_name_\
用户名

_password_\
用户密码(用于sdk在内部token到期时自动更新用户token)

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### fastSignInByNameWithName:password:completion:

通过用户名快速登录（要求之前成功登录过，登录速度较快）

`- (void)fastSignInByNameWithName:(NSString *)*name* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_name_\
用户名

_password_\
用户密码(用于sdk在内部token到期时自动更新用户token)

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### getSDKConfig

获取SDK设置

`- (BMXSDKConfig *)getSDKConfig`

#### Return Value

[BMXSDKConfig](BMXSDKConfig.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### initializeServerConfigWithIsLocal:

获取app的服务器网络配置，在初始化SDK之后登陆之前调用，可以提前获取服务器配置加快登陆速度。

`- (BMXErrorCode)initializeServerConfigWithIsLocal:(BOOL)*isLocal*`

#### Parameters

_isLocal_\
为true则使用本地缓存的dns配置，为false则从服务器获取最新的配置。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### initializeServerConfigWithIsLocal:completion:

获取app的服务器网络配置，在初始化SDK之后登陆之前调用，可以提前获取服务器配置加快登陆速度。

`- (void)initializeServerConfigWithIsLocal:(BOOL)*isLocal* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_isLocal_\
为true则使用本地缓存的dns配置，为false则从服务器获取最新的配置。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### onNetworkChangedWithType:reconnect:

处理网络状态发送变化

`- (void)onNetworkChangedWithType:(BMXNetworkType)*type* reconnect:(BOOL)*reconnect*`

#### Parameters

_type_\
变化后的网络类型

_reconnect_\
网络是否需要重连

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### reconnect

强制重新连接

`- (void)reconnect`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### reconnectWithCompletion:

强制重新连接

`- (void)reconnectWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### sendMessageWithMsg:

发送消息，消息状态变化会通过listener通知，在发送群组消息且指定的群组为开启群组已读回执的情况下， 该接口会自动获取群成员列表id并且填充到message config中去，无需客户端自己进行群组成员列表的填充操作。

`- (void)sendMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
发送的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### sendMessageWithMsg:completion:

发送消息，消息状态变化会通过listener通知，在发送群组消息且指定的群组为开启群组已读回执的情况下， 该接口会自动获取群成员列表id并且填充到message config中去，无需客户端自己进行群组成员列表的填充操作。

`- (void)sendMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
发送的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signInByIdWithArg1:password:

通过用户名登录

`- (BMXErrorCode)signInByIdWithArg1:(long long)*arg1* password:(NSString *)*password*`

#### Parameters

_password_\
用户密码

_name_\
用户名

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='1' data-2='1' data-3='1' data-4='1' data-5='1' data-6='1' data-7='1' data-8='1' data-9='1' data-10='1' data-11='1' data-12='1' data-13='1' data-14='1' data-15='1' data-16='1' data-17='1' data-18='1' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signInByIdWithArg1:password:completion:

通过用户ID登录

`- (void)signInByIdWithArg1:(long long)*arg1* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_password_\
用户密码

_int64\_t_\
用户id

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='1' data-2='1' data-3='1' data-4='1' data-5='1' data-6='1' data-7='1' data-8='1' data-9='1' data-10='1' data-11='1' data-12='1' data-13='1' data-14='1' data-15='1' data-16='1' data-17='1' data-18='1' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signInByNameWithName:password:

通过用户名登录

`- (BMXErrorCode)signInByNameWithName:(NSString *)*name* password:(NSString *)*password*`

#### Parameters

_name_\
用户名

_password_\
用户密码

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signInByNameWithName:password:completion:

通过用户名登录

`- (void)signInByNameWithName:(NSString *)*name* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_name_\
用户名

_password_\
用户密码

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signInStatus

获取当前的登录状态

`- (BMXSignInStatus)signInStatus`

#### Return Value

[BMXSignInStatus](../Constants/BMXSignInStatus.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signOut

`- (BMXErrorCode)signOut`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signOutWithCompletion:

`- (void)signOutWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signOutWithUid:

`- (BMXErrorCode)signOutWithUid:(long long)*uid*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signOutWithUid:completion:

`- (void)signOutWithUid:(long long)*uid* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signOutWithUid:ignoreUnbindDevice:

退出登录

`- (BMXErrorCode)signOutWithUid:(long long)*uid* ignoreUnbindDevice:(BOOL)*ignoreUnbindDevice*`

#### Parameters

_uid_\
退出用户的uid（默认输入0则退出当前登陆用户）

_ignoreUnbindDevice_\
用户退出时是否忽略解绑定设备操作。对应某些服务器不可访问的情况下忽略服务器解绑定设备操作直接强制退出时设置为true

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signOutWithUid:ignoreUnbindDevice:completion:

退出登录

`- (void)signOutWithUid:(long long)*uid* ignoreUnbindDevice:(BOOL)*ignoreUnbindDevice* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_uid_\
退出用户的uid（默认输入0则退出当前登陆用户）

_ignoreUnbindDevice_\
用户退出时是否忽略解绑定设备操作。对应某些服务器不可访问的情况下忽略服务器解绑定设备操作直接强制退出时设置为true

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signUpNewUserWithUsername:password:bmxUserProfilePtr:

注册新用户，username和password是必填参数

`- (BMXErrorCode)signUpNewUserWithUsername:(NSString *)*username* password:(NSString *)*password* bmxUserProfilePtr:(BMXUserProfile *)*bmxUserProfilePtr*`

#### Parameters

_username_\
用户名

_password_\
用户密码

_bmxUserProfilePtr_\
注册成功后从该函数处获取新注册用户的Profile信息，初始传入指向为空的shared\_ptr对象即可。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signUpNewUserWithUsername:password:completion:

注册新用户，username和password是必填参数

`- (void)signUpNewUserWithUsername:(NSString *)*username* password:(NSString *)*password* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *aError ))*resBlock*`

#### Parameters

_username_\
用户名

_password_\
用户密码

_bmxUserProfilePtr_\
注册成功后从该函数处获取新注册用户的Profile信息，初始传入指向为空的shared\_ptr对象即可。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>
```
