# BMXClient Class Reference

**Inherits from** [BMXNetworkListener](BMXNetworkListener.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface Client instance

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

Create a BMXClient

`+ (BMXClient *)createWithConfig:(BMXSDKConfig *)*config*`

#### Parameters

_config_\
[BMXSDKConfig](BMXSDKConfig.md) SDK config created

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

Change appId，also works on appId in BMXConfig

`- (BMXErrorCode)changeAppIdWithAppId:(NSString *)*appId* appSecret:(NSString *)*appSecret*`

#### Parameters

_appId_\
The new appId

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### changeAppIdWithAppId:appSecret:completion:

Change appId，also works on appId in BMXConfig

`- (void)changeAppIdWithAppId:(NSString *)*appId* appSecret:(NSString *)*appSecret* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_appId_\
The new appId

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

Get connection status to the server

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

Delete my account

`- (BMXErrorCode)deleteAccountWithPassword:(NSString *)*password*`

#### Parameters

_password_\
The password for my account

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### deleteAccountWithPassword:completion:

Delete my account

`- (void)deleteAccountWithPassword:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_password_\
The password for my account

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### disconnect

Disconnect from the server

`- (void)disconnect`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### disconnectWithCompletion:

Disconnect from the server

`- (void)disconnectWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### fastSignInByIdWithUid:password:

Fast login by user ID (A successful login required)

`- (BMXErrorCode)fastSignInByIdWithUid:(long long)*uid* password:(NSString *)*password*`

#### Parameters

_uid_\
The user ID

_password_\
The password

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### fastSignInByIdWithUid:password:completion:

Fast login by user ID (A successful login required)

`- (void)fastSignInByIdWithUid:(long long)*uid* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_uid_\
The user ID

_password_\
The password

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### fastSignInByNameWithName:password:

Fast login by username (A successful login required)

`- (BMXErrorCode)fastSignInByNameWithName:(NSString *)*name* password:(NSString *)*password*`

#### Parameters

_name_\
The username

_password_\
The password

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### fastSignInByNameWithName:password:completion:

Fast login by username (A successful login required)

`- (void)fastSignInByNameWithName:(NSString *)*name* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_name_\
The username

_password_\
The password

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### getSDKConfig

Get SDK config

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

Initialize server config to accelerate login speed

`- (BMXErrorCode)initializeServerConfigWithIsLocal:(BOOL)*isLocal*`

#### Parameters

_isLocal_\
true for loading from local file, or downloading from server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### initializeServerConfigWithIsLocal:completion:

Initialize server config to accelerate login speed

`- (void)initializeServerConfigWithIsLocal:(BOOL)*isLocal* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_isLocal_\
true for loading from local file, or downloading from server

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### onNetworkChangedWithType:reconnect:

Send network status change events to SDK

`- (void)onNetworkChangedWithType:(BMXNetworkType)*type* reconnect:(BOOL)*reconnect*`

#### Parameters

_type_\
New network type

_reconnect_\
Need to reconnect or not

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### reconnect

Enforce reconnection

`- (void)reconnect`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### reconnectWithCompletion:

Enforce reconnection

`- (void)reconnectWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### sendMessageWithMsg:

Send a message

`- (void)sendMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### sendMessageWithMsg:completion:

Send a message

`- (void)sendMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signInByIdWithArg1:password:

Sign in by username

`- (BMXErrorCode)signInByIdWithArg1:(long long)*arg1* password:(NSString *)*password*`

#### Parameters

_password_\
The password

_name_\
THe username

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='1' data-2='1' data-3='1' data-4='1' data-5='1' data-6='1' data-7='1' data-8='1' data-9='1' data-10='1' data-11='1' data-12='1' data-13='1' data-14='1' data-15='1' data-16='1' data-17='1' data-18='1' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signInByIdWithArg1:password:completion:

Sign in by user ID

`- (void)signInByIdWithArg1:(long long)*arg1* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_password_\
The password

_int64\_t_\
The user ID

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='1' data-2='1' data-3='1' data-4='1' data-5='1' data-6='1' data-7='1' data-8='1' data-9='1' data-10='1' data-11='1' data-12='1' data-13='1' data-14='1' data-15='1' data-16='1' data-17='1' data-18='1' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signInByNameWithName:password:

Sign in by username

`- (BMXErrorCode)signInByNameWithName:(NSString *)*name* password:(NSString *)*password*`

#### Parameters

_name_\
The username

_password_\
The password

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signInByNameWithName:password:completion:

Sign in by username

`- (void)signInByNameWithName:(NSString *)*name* password:(NSString *)*password* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_name_\
The username

_password_\
The password

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signInStatus

Get login status

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

Sign out

`- (BMXErrorCode)signOutWithUid:(long long)*uid* ignoreUnbindDevice:(BOOL)*ignoreUnbindDevice*`

#### Parameters

_uid_\
My user ID

_ignoreUnbindDevice_\
Ignore unbinding device on sign out

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signOutWithUid:ignoreUnbindDevice:completion:

Sign out

`- (void)signOutWithUid:(long long)*uid* ignoreUnbindDevice:(BOOL)*ignoreUnbindDevice* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_uid_\
My user ID

_ignoreUnbindDevice_\
Ignore unbinding device on sign out

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signUpNewUserWithUsername:password:bmxUserProfilePtr:

Sign up a new account

`- (BMXErrorCode)signUpNewUserWithUsername:(NSString *)*username* password:(NSString *)*password* bmxUserProfilePtr:(BMXUserProfile *)*bmxUserProfilePtr*`

#### Parameters

_username_\
The username

_password_\
The password

_bmxUserProfilePtr_\
Profile of the new user

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>

```

### signUpNewUserWithUsername:password:completion:

Sign up a new account

`- (void)signUpNewUserWithUsername:(NSString *)*username* password:(NSString *)*password* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *aError ))*resBlock*`

#### Parameters

_username_\
The username

_password_\
The password

_bmxUserProfilePtr_\
Profile of the new user

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXClient'></div>
```
