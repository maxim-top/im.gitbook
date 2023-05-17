# BMXUserService Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface User Service

## Properties

<a name="//api/name/swigCMemOwn" title="swigCMemOwn"></a>
### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

<a name="//api/name/swigCPtr" title="swigCPtr"></a>
### swigCPtr

`@property (nonatomic) void *swigCPtr`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
### addDelegate:

Add a user service listener

`- (void)addDelegate:(id<BMXUserServiceProtocol>)*aDelegate*`

#### Parameters

*listener*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="addDelegate:" %}{% endlanying_code_snippet %}
```
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXUserServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/bindDeviceWithToken:" title="bindDeviceWithToken:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="addDelegate:delegateQueue:" %}{% endlanying_code_snippet %}
```
### bindDeviceWithToken:

Bind device token

`- (BMXErrorCode)bindDeviceWithToken:(NSString *)*token*`

#### Parameters

*token*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/bindDeviceWithToken:completion:" title="bindDeviceWithToken:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="bindDeviceWithToken:" %}{% endlanying_code_snippet %}
```
### bindDeviceWithToken:completion:

Bind device token

`- (void)bindDeviceWithToken:(NSString *)*token* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*token*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="bindDeviceWithToken:completion:" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/deleteDeviceWithDeviceSn:" title="deleteDeviceWithDeviceSn:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="dealloc" %}{% endlanying_code_snippet %}
```
### deleteDeviceWithDeviceSn:

Delete a device

`- (BMXErrorCode)deleteDeviceWithDeviceSn:(int)*device_sn*`

#### Parameters

*device_sn*  
    Device serial number

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deleteDeviceWithDeviceSn:completion:" title="deleteDeviceWithDeviceSn:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="deleteDeviceWithDeviceSn:" %}{% endlanying_code_snippet %}
```
### deleteDeviceWithDeviceSn:completion:

Delete a device

`- (void)deleteDeviceWithDeviceSn:(int)*device_sn* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*device_sn*  
    Device serial number

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAvatarWithProfile:thumbnail:callback:" title="downloadAvatarWithProfile:thumbnail:callback:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="deleteDeviceWithDeviceSn:completion:" %}{% endlanying_code_snippet %}
```
### downloadAvatarWithProfile:thumbnail:callback:

Download my avatar

`- (BMXErrorCode)downloadAvatarWithProfile:(BMXUserProfile *)*profile* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

*profile*  
    My user profile

*thumbnail*  
    Whether to download my avatar thumbnail

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAvatarWithProfile:thumbnail:callback:completion:" title="downloadAvatarWithProfile:thumbnail:callback:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="downloadAvatarWithProfile:thumbnail:callback:" %}{% endlanying_code_snippet %}
```
### downloadAvatarWithProfile:thumbnail:callback:completion:

Download my avatar

`- (void)downloadAvatarWithProfile:(BMXUserProfile *)*profile* thumbnail:(BOOL)*thumbnail* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*profile*  
    My user profile

*thumbnail*  
    Whether to download my avatar thumbnail

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getDeviceList:" title="getDeviceList:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="downloadAvatarWithProfile:thumbnail:callback:completion:" %}{% endlanying_code_snippet %}
```
### getDeviceList:

Get my deivce list

`- (BMXErrorCode)getDeviceList:(BMXDeviceList *)*deviceList*`

#### Parameters

*deviceList*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getDeviceListWithCompletion:" title="getDeviceListWithCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="getDeviceList:" %}{% endlanying_code_snippet %}
```
### getDeviceListWithCompletion:

Get my deivce list

`- (void)getDeviceListWithCompletion:(void ( ^ ) ( BMXDeviceList *deviceList , BMXError *aError ))*resBlock*`

#### Parameters

*deviceList*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getProfile:completion:" title="getProfile:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="getDeviceListWithCompletion:" %}{% endlanying_code_snippet %}
```
### getProfile:completion:

Get my user profile

`- (void)getProfile:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *aError ))*resBlock*`

#### Parameters

*forceRefresh*  
    From server

*profile*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getProfile:forceRefresh:" title="getProfile:forceRefresh:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="getProfile:completion:" %}{% endlanying_code_snippet %}
```
### getProfile:forceRefresh:

Get my user profile

`- (BMXErrorCode)getProfile:(BMXUserProfile *)*profile* forceRefresh:(BOOL)*forceRefresh*`

#### Parameters

*profile*  

*forceRefresh*  
    From server

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="getProfile:forceRefresh:" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### removeDelegate:

Remove a user service listener

`- (void)removeDelegate:(id<BMXUserServiceProtocol>)*aDelegate*`

#### Parameters

*listener*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAddFriendAuthMode:" title="setAddFriendAuthMode:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="removeDelegate:" %}{% endlanying_code_snippet %}
```
### setAddFriendAuthMode:

Set friend authorization mode

`- (BMXErrorCode)setAddFriendAuthMode:(BMXUserProfile_AddFriendAuthMode)*mode*`

#### Parameters

*mode*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAddFriendAuthMode:completion:" title="setAddFriendAuthMode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setAddFriendAuthMode:" %}{% endlanying_code_snippet %}
```
### setAddFriendAuthMode:completion:

Set friend authorization mode

`- (void)setAddFriendAuthMode:(BMXUserProfile_AddFriendAuthMode)*mode* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*mode*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAuthQuestion:" title="setAuthQuestion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setAddFriendAuthMode:completion:" %}{% endlanying_code_snippet %}
```
### setAuthQuestion:

Set friend authorization question

`- (BMXErrorCode)setAuthQuestion:(BMXUserProfileAuthQuestion *)*authQuestion*`

#### Parameters

*authQuestion*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAuthQuestion:completion:" title="setAuthQuestion:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setAuthQuestion:" %}{% endlanying_code_snippet %}
```
### setAuthQuestion:completion:

Set friend authorization question

`- (void)setAuthQuestion:(BMXUserProfileAuthQuestion *)*authQuestion* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*authQuestion*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAutoAcceptGroupInvite:" title="setAutoAcceptGroupInvite:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setAuthQuestion:completion:" %}{% endlanying_code_snippet %}
```
### setAutoAcceptGroupInvite:

Set whether to accept group invitation automatically

`- (BMXErrorCode)setAutoAcceptGroupInvite:(BOOL)*enable*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAutoAcceptGroupInvite:completion:" title="setAutoAcceptGroupInvite:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setAutoAcceptGroupInvite:" %}{% endlanying_code_snippet %}
```
### setAutoAcceptGroupInvite:completion:

Set whether to accept group invitation automatically

`- (void)setAutoAcceptGroupInvite:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAutoDownloadAttachment:" title="setAutoDownloadAttachment:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setAutoAcceptGroupInvite:completion:" %}{% endlanying_code_snippet %}
```
### setAutoDownloadAttachment:

Set whether download attachment automatically

`- (BMXErrorCode)setAutoDownloadAttachment:(BOOL)*enable*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAutoDownloadAttachment:completion:" title="setAutoDownloadAttachment:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setAutoDownloadAttachment:" %}{% endlanying_code_snippet %}
```
### setAutoDownloadAttachment:completion:

Set whether download attachment automatically

`- (void)setAutoDownloadAttachment:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setEnablePush:" title="setEnablePush:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setAutoDownloadAttachment:completion:" %}{% endlanying_code_snippet %}
```
### setEnablePush:

Set whether to enable push function

`- (BMXErrorCode)setEnablePush:(BOOL)*enable*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setEnablePush:completion:" title="setEnablePush:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setEnablePush:" %}{% endlanying_code_snippet %}
```
### setEnablePush:completion:

Set whether to enable push function

`- (void)setEnablePush:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setEnablePushDetaile:" title="setEnablePushDetaile:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setEnablePush:completion:" %}{% endlanying_code_snippet %}
```
### setEnablePushDetaile:

Set whether to enable push message detail

`- (BMXErrorCode)setEnablePushDetaile:(BOOL)*enable*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setEnablePushDetaile:completion:" title="setEnablePushDetaile:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setEnablePushDetaile:" %}{% endlanying_code_snippet %}
```
### setEnablePushDetaile:completion:

Set whether to enable push message detail

`- (void)setEnablePushDetaile:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setNickname:" title="setNickname:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setEnablePushDetaile:completion:" %}{% endlanying_code_snippet %}
```
### setNickname:

Set my nickname

`- (BMXErrorCode)setNickname:(NSString *)*nickname*`

#### Parameters

*nickname*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setNickname:completion:" title="setNickname:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setNickname:" %}{% endlanying_code_snippet %}
```
### setNickname:completion:

Set my nickname

`- (void)setNickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*nickname*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setNotificationSound:" title="setNotificationSound:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setNickname:completion:" %}{% endlanying_code_snippet %}
```
### setNotificationSound:

Set whether to enable sound notification

`- (BMXErrorCode)setNotificationSound:(BOOL)*enable*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setNotificationSound:completion:" title="setNotificationSound:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setNotificationSound:" %}{% endlanying_code_snippet %}
```
### setNotificationSound:completion:

Set whether to enable sound notification

`- (void)setNotificationSound:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setNotificationVibrate:" title="setNotificationVibrate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setNotificationSound:completion:" %}{% endlanying_code_snippet %}
```
### setNotificationVibrate:

Set whether to enable vibrate notification

`- (BMXErrorCode)setNotificationVibrate:(BOOL)*enable*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setNotificationVibrate:completion:" title="setNotificationVibrate:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setNotificationVibrate:" %}{% endlanying_code_snippet %}
```
### setNotificationVibrate:completion:

Set whether to enable vibrate notification

`- (void)setNotificationVibrate:(BOOL)*enable* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*enable*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPrivateInfo:" title="setPrivateInfo:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setNotificationVibrate:completion:" %}{% endlanying_code_snippet %}
```
### setPrivateInfo:

Set private information(Invisible to friends)

`- (BMXErrorCode)setPrivateInfo:(NSString *)*privateInfo*`

#### Parameters

*privateInfo*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPrivateInfo:completion:" title="setPrivateInfo:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setPrivateInfo:" %}{% endlanying_code_snippet %}
```
### setPrivateInfo:completion:

Set private information(Invisible to friends)

`- (void)setPrivateInfo:(NSString *)*privateInfo* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*privateInfo*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPublicInfo:" title="setPublicInfo:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setPrivateInfo:completion:" %}{% endlanying_code_snippet %}
```
### setPublicInfo:

Set public information(Visible to friends)

`- (BMXErrorCode)setPublicInfo:(NSString *)*publicInfo*`

#### Parameters

*publicInfo*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPublicInfo:completion:" title="setPublicInfo:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setPublicInfo:" %}{% endlanying_code_snippet %}
```
### setPublicInfo:completion:

Set public information(Visible to friends)

`- (void)setPublicInfo:(NSString *)*publicInfo* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*publicInfo*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushAlias:bmxPushToken:" title="setPushAlias:bmxPushToken:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setPublicInfo:completion:" %}{% endlanying_code_snippet %}
```
### setPushAlias:bmxPushToken:

@brief

`- (BMXErrorCode)setPushAlias:(NSString *)*alias* bmxPushToken:(NSString *)*bmxPushToken*`

#### Parameters

*nickname*  
    My nickname

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Discussion
@brief

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushAlias:bmxPushToken:completion:" title="setPushAlias:bmxPushToken:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setPushAlias:bmxPushToken:" %}{% endlanying_code_snippet %}
```
### setPushAlias:bmxPushToken:completion:

@brief

`- (void)setPushAlias:(NSString *)*alias* bmxPushToken:(NSString *)*bmxPushToken* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*alias*  

    User alias for push

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Discussion
@brief

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushNickname:" title="setPushNickname:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setPushAlias:bmxPushToken:completion:" %}{% endlanying_code_snippet %}
```
### setPushNickname:

Set nickname for push

`- (BMXErrorCode)setPushNickname:(NSString *)*nickname*`

#### Parameters

*nickname*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushNickname:completion:" title="setPushNickname:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setPushNickname:" %}{% endlanying_code_snippet %}
```
### setPushNickname:completion:

Set nickname for push

`- (void)setPushNickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*nickname*  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/uploadAvatarWithAvatarPath:callback:" title="uploadAvatarWithAvatarPath:callback:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="setPushNickname:completion:" %}{% endlanying_code_snippet %}
```
### uploadAvatarWithAvatarPath:callback:

Upload my avatar

`- (BMXErrorCode)uploadAvatarWithAvatarPath:(NSString *)*avatarPath* callback:(void ( ^ ) ( int progress ))*callback*`

#### Parameters

*avatarPath*  
    Local path of my avatar file

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/uploadAvatarWithAvatarPath:callback:completion:" title="uploadAvatarWithAvatarPath:callback:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="uploadAvatarWithAvatarPath:callback:" %}{% endlanying_code_snippet %}
```
### uploadAvatarWithAvatarPath:callback:completion:

Upload my avatar

`- (void)uploadAvatarWithAvatarPath:(NSString *)*avatarPath* callback:(void ( ^ ) ( int progress ))*callback* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*avatarPath*  
    Local path of my avatar file

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserService",function="uploadAvatarWithAvatarPath:callback:completion:" %}{% endlanying_code_snippet %}
```
