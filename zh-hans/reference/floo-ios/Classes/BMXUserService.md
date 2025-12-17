# BMXUserService Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 用户Service

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### addDelegate:

添加用户状态监听者

`- (void)addDelegate:(id<BMXUserServiceProtocol>)*aDelegate*`

#### Parameters

_listener_\
用户状态监听者

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXUserServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### bindDeviceWithToken:

绑定设备推送token

`- (BMXErrorCode)bindDeviceWithToken:(NSString *)*token*`

#### Parameters

_token_\
设备token

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### bindDeviceWithToken:completion:

绑定设备推送token

`- (void)bindDeviceWithToken:(NSString *)*token* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_token_\
设备token

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### deleteDeviceWithDeviceSn:

删除设备

`- (BMXErrorCode)deleteDeviceWithDeviceSn:(int)*device_sn*`

#### Parameters

_device\_sn_\
设备序列号

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### deleteDeviceWithDeviceSn:completion:

删除设备

`- (void)deleteDeviceWithDeviceSn:(int)*device_sn* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_device\_sn_\
设备序列号

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### downloadAvatarWithProfile:thumbnail:callback:

下载头像，默认下载缩略图

`- (BMXErrorCode)downloadAvatarWithProfile:(BMXUserProfile *)*profile* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

_profile_\
用户profile

_thumbnail_\
是否下载缩略图，true下载缩略图，false下载原图

_callback_\
下载回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### downloadAvatarWithProfile:thumbnail:callback:completion:

下载头像，默认下载缩略图

`- (void)downloadAvatarWithProfile:(BMXUserProfile *)*profile* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_profile_\
用户profile

_thumbnail_\
是否下载缩略图，true下载缩略图，false下载原图

_callback_\
下载回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### getDeviceList:

获取设备列表

`- (BMXErrorCode)getDeviceList:(BMXDeviceList *)*deviceList*`

#### Parameters

_deviceList_\
设备列表，传入空列表函数返回后从此处获取返回的设备列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### getDeviceListWithCompletion:

获取设备列表

`- (void)getDeviceListWithCompletion:(void ( ^ ) ( BMXDeviceList *deviceList , BMXError *aError ))*resBlock*`

#### Parameters

_deviceList_\
设备列表，传入空列表函数返回后从此处获取返回的设备列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### getProfile:completion:

获取用户详情，如果forceRefresh == true，则强制从服务端拉取

`- (void)getProfile:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *aError ))*resBlock*`

#### Parameters

_forceRefresh_\
是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取

_profile_\
用户profile信息，初始传入指向为空的shared\_ptr对象，函数返回后从此处获取用户profile信息。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### getProfile:forceRefresh:

获取用户详情，如果forceRefresh == true，则强制从服务端拉取

`- (BMXErrorCode)getProfile:(BMXUserProfile *)*profile* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_profile_\
用户profile信息，初始传入指向为空的shared\_ptr对象，函数返回后从此处获取用户profile信息。

_forceRefresh_\
是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### removeDelegate:

移除用户状态监听者

`- (void)removeDelegate:(id<BMXUserServiceProtocol>)*aDelegate*`

#### Parameters

_listener_\
用户状态监听者

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAddFriendAuthMode:

设置加好友验证方式

`- (BMXErrorCode)setAddFriendAuthMode:(BMXUserProfile_AddFriendAuthMode)*mode*`

#### Parameters

_mode_\
加好友验证方式

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAddFriendAuthMode:completion:

设置加好友验证方式

`- (void)setAddFriendAuthMode:(BMXUserProfile_AddFriendAuthMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_mode_\
加好友验证方式

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAuthQuestion:

设置加好友验证问题

`- (BMXErrorCode)setAuthQuestion:(BMXUserProfileAuthQuestion *)*authQuestion*`

#### Parameters

_authQuestion_\
加好友验证问题

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAuthQuestion:completion:

设置加好友验证问题

`- (void)setAuthQuestion:(BMXUserProfileAuthQuestion *)*authQuestion* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_authQuestion_\
加好友验证问题

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAutoAcceptGroupInvite:

设置是否自动同意入群邀请

`- (BMXErrorCode)setAutoAcceptGroupInvite:(BOOL)*enable*`

#### Parameters

_enable_\
是否自动同意入群邀请，true同意，false不同意

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAutoAcceptGroupInvite:completion:

设置是否自动同意入群邀请

`- (void)setAutoAcceptGroupInvite:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_enable_\
是否自动同意入群邀请，true同意，false不同意

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAutoDownloadAttachment:

设置是否自动缩略图和语音附件

`- (BMXErrorCode)setAutoDownloadAttachment:(BOOL)*enable*`

#### Parameters

_enable_\
是否自动缩略图和语音附件，true自动下载，false不会自动下载

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAutoDownloadAttachment:completion:

设置是否自动缩略图和语音附件

`- (void)setAutoDownloadAttachment:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_enable_\
是否自动缩略图和语音附件，true自动下载，false不会自动下载

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setEnablePush:

设置是否允许推送

`- (BMXErrorCode)setEnablePush:(BOOL)*enable*`

#### Parameters

_enable_\
是否允许推送，true推送，false不推送

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setEnablePush:completion:

设置是否允许推送

`- (void)setEnablePush:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_enable_\
是否允许推送，true推送，false不推送

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setEnablePushDetaile:

设置是否推送详情

`- (BMXErrorCode)setEnablePushDetaile:(BOOL)*enable*`

#### Parameters

_enable_\
是否推送详情，true推送，false不推送

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setEnablePushDetaile:completion:

设置是否推送详情

`- (void)setEnablePushDetaile:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_enable_\
是否推送详情，true推送，false不推送

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setNickname:

设置昵称

`- (BMXErrorCode)setNickname:(NSString *)*nickname*`

#### Parameters

_nickname_\
用户昵称

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setNickname:completion:

设置昵称

`- (void)setNickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_nickname_\
用户昵称

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setNotificationSound:

设置收到新消息是否声音提醒

`- (BMXErrorCode)setNotificationSound:(BOOL)*enable*`

#### Parameters

_enable_\
收到新消息是否声音提醒，true提醒，false不提醒

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setNotificationSound:completion:

设置收到新消息是否声音提醒

`- (void)setNotificationSound:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_enable_\
收到新消息是否声音提醒，true提醒，false不提醒

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setNotificationVibrate:

设置收到新消息是否震动

`- (BMXErrorCode)setNotificationVibrate:(BOOL)*enable*`

#### Parameters

_enable_\
收到新消息是否震动，true震动，false不震动

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setNotificationVibrate:completion:

设置收到新消息是否震动

`- (void)setNotificationVibrate:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_enable_\
收到新消息是否震动，true震动，false不震动

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPrivateInfo:

设置私有扩展信息

`- (BMXErrorCode)setPrivateInfo:(NSString *)*privateInfo*`

#### Parameters

_privateInfo_\
私有扩展信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPrivateInfo:completion:

设置私有扩展信息

`- (void)setPrivateInfo:(NSString *)*privateInfo* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_privateInfo_\
私有扩展信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPublicInfo:

设置公开扩展信息

`- (BMXErrorCode)setPublicInfo:(NSString *)*publicInfo*`

#### Parameters

_publicInfo_\
公开扩展信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPublicInfo:completion:

设置公开扩展信息

`- (void)setPublicInfo:(NSString *)*publicInfo* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_publicInfo_\
公开扩展信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPushAlias:bmxPushToken:

@brief

`- (BMXErrorCode)setPushAlias:(NSString *)*alias* bmxPushToken:(NSString *)*bmxPushToken*`

#### Parameters

_nickname_\
推送昵称

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Discussion

@brief

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPushAlias:bmxPushToken:completion:

@brief

`- (void)setPushAlias:(NSString *)*alias* bmxPushToken:(NSString *)*bmxPushToken* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_nickname_\
推送昵称

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Discussion

@brief

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPushNickname:

设置推送昵称

`- (BMXErrorCode)setPushNickname:(NSString *)*nickname*`

#### Parameters

_nickname_\
推送昵称

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPushNickname:completion:

设置推送昵称

`- (void)setPushNickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_nickname_\
推送昵称

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### uploadAvatarWithAvatarPath:callback:

上传头像

`- (BMXErrorCode)uploadAvatarWithAvatarPath:(NSString *)*avatarPath* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

_avatarPath_\
上传头像的本地地址

_callback_\
上传回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### uploadAvatarWithAvatarPath:callback:completion:

上传头像

`- (void)uploadAvatarWithAvatarPath:(NSString *)*avatarPath* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_avatarPath_\
上传头像的本地地址

_callback_\
上传回调函数

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>
```
