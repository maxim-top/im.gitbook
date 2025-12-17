# BMXUserService Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface User Service

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### addDelegate:

Add a user service listener

`- (void)addDelegate:(id<BMXUserServiceProtocol>)*aDelegate*`

#### Parameters

_listener_

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

Bind device token

`- (BMXErrorCode)bindDeviceWithToken:(NSString *)*token*`

#### Parameters

_token_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### bindDeviceWithToken:completion:

Bind device token

`- (void)bindDeviceWithToken:(NSString *)*token* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_token_

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

Delete a device

`- (BMXErrorCode)deleteDeviceWithDeviceSn:(int)*device_sn*`

#### Parameters

_device\_sn_\
Device serial number

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### deleteDeviceWithDeviceSn:completion:

Delete a device

`- (void)deleteDeviceWithDeviceSn:(int)*device_sn* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_device\_sn_\
Device serial number

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### downloadAvatarWithProfile:thumbnail:callback:

Download my avatar

`- (BMXErrorCode)downloadAvatarWithProfile:(BMXUserProfile *)*profile* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

_profile_\
My user profile

_thumbnail_\
Whether to download my avatar thumbnail

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### downloadAvatarWithProfile:thumbnail:callback:completion:

Download my avatar

`- (void)downloadAvatarWithProfile:(BMXUserProfile *)*profile* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_profile_\
My user profile

_thumbnail_\
Whether to download my avatar thumbnail

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### getDeviceList:

Get my deivce list

`- (BMXErrorCode)getDeviceList:(BMXDeviceList *)*deviceList*`

#### Parameters

_deviceList_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### getDeviceListWithCompletion:

Get my deivce list

`- (void)getDeviceListWithCompletion:(void ( ^ ) ( BMXDeviceList *deviceList , BMXError *aError ))*resBlock*`

#### Parameters

_deviceList_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### getProfile:completion:

Get my user profile

`- (void)getProfile:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *aError ))*resBlock*`

#### Parameters

_forceRefresh_\
From server

_profile_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### getProfile:forceRefresh:

Get my user profile

`- (BMXErrorCode)getProfile:(BMXUserProfile *)*profile* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

_profile_

_forceRefresh_\
From server

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

Remove a user service listener

`- (void)removeDelegate:(id<BMXUserServiceProtocol>)*aDelegate*`

#### Parameters

_listener_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAddFriendAuthMode:

Set friend authorization mode

`- (BMXErrorCode)setAddFriendAuthMode:(BMXUserProfile_AddFriendAuthMode)*mode*`

#### Parameters

_mode_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAddFriendAuthMode:completion:

Set friend authorization mode

`- (void)setAddFriendAuthMode:(BMXUserProfile_AddFriendAuthMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_mode_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAuthQuestion:

Set friend authorization question

`- (BMXErrorCode)setAuthQuestion:(BMXUserProfileAuthQuestion *)*authQuestion*`

#### Parameters

_authQuestion_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAuthQuestion:completion:

Set friend authorization question

`- (void)setAuthQuestion:(BMXUserProfileAuthQuestion *)*authQuestion* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_authQuestion_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAutoAcceptGroupInvite:

Set whether to accept group invitation automatically

`- (BMXErrorCode)setAutoAcceptGroupInvite:(BOOL)*enable*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAutoAcceptGroupInvite:completion:

Set whether to accept group invitation automatically

`- (void)setAutoAcceptGroupInvite:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAutoDownloadAttachment:

Set whether download attachment automatically

`- (BMXErrorCode)setAutoDownloadAttachment:(BOOL)*enable*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setAutoDownloadAttachment:completion:

Set whether download attachment automatically

`- (void)setAutoDownloadAttachment:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setEnablePush:

Set whether to enable push function

`- (BMXErrorCode)setEnablePush:(BOOL)*enable*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setEnablePush:completion:

Set whether to enable push function

`- (void)setEnablePush:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setEnablePushDetaile:

Set whether to enable push message detail

`- (BMXErrorCode)setEnablePushDetaile:(BOOL)*enable*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setEnablePushDetaile:completion:

Set whether to enable push message detail

`- (void)setEnablePushDetaile:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setNickname:

Set my nickname

`- (BMXErrorCode)setNickname:(NSString *)*nickname*`

#### Parameters

_nickname_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setNickname:completion:

Set my nickname

`- (void)setNickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_nickname_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setNotificationSound:

Set whether to enable sound notification

`- (BMXErrorCode)setNotificationSound:(BOOL)*enable*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setNotificationSound:completion:

Set whether to enable sound notification

`- (void)setNotificationSound:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setNotificationVibrate:

Set whether to enable vibrate notification

`- (BMXErrorCode)setNotificationVibrate:(BOOL)*enable*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setNotificationVibrate:completion:

Set whether to enable vibrate notification

`- (void)setNotificationVibrate:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_enable_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPrivateInfo:

Set private information(Invisible to friends)

`- (BMXErrorCode)setPrivateInfo:(NSString *)*privateInfo*`

#### Parameters

_privateInfo_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPrivateInfo:completion:

Set private information(Invisible to friends)

`- (void)setPrivateInfo:(NSString *)*privateInfo* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_privateInfo_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPublicInfo:

Set public information(Visible to friends)

`- (BMXErrorCode)setPublicInfo:(NSString *)*publicInfo*`

#### Parameters

_publicInfo_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPublicInfo:completion:

Set public information(Visible to friends)

`- (void)setPublicInfo:(NSString *)*publicInfo* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_publicInfo_

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
My nickname

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

_alias_

```
User alias for push
```

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

Set nickname for push

`- (BMXErrorCode)setPushNickname:(NSString *)*nickname*`

#### Parameters

_nickname_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### setPushNickname:completion:

Set nickname for push

`- (void)setPushNickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_nickname_

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### uploadAvatarWithAvatarPath:callback:

Upload my avatar

`- (BMXErrorCode)uploadAvatarWithAvatarPath:(NSString *)*avatarPath* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

_avatarPath_\
Local path of my avatar file

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>

```

### uploadAvatarWithAvatarPath:callback:completion:

Upload my avatar

`- (void)uploadAvatarWithAvatarPath:(NSString *)*avatarPath* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_avatarPath_\
Local path of my avatar file

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXUserService'></div>
```
