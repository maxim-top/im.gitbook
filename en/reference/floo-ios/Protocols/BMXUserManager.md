# BMXUserManager Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXUserManager.h  

## Instance Methods

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
### addDelegate:

`- (void)addDelegate:(id<BMXUserServiceProtocol>)*aDelegate*`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="addDelegate:" %}{% endlanying_code_snippet %}
```
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXUserServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/bindDevice:completion:" title="bindDevice:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="addDelegate:delegateQueue:" %}{% endlanying_code_snippet %}
```
### bindDevice:completion:

Binding device push token

`- (void)bindDevice:(NSString *)*token* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Binding device push token

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/deleteDeviceByDeviceSN:completion:" title="deleteDeviceByDeviceSN:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="bindDevice:completion:" %}{% endlanying_code_snippet %}
```
### deleteDeviceByDeviceSN:completion:

Delete device

`- (void)deleteDeviceByDeviceSN:(NSInteger)*deviceSN* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Delete device

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/downloadAvatarWithProfile:thumbnail:progress:completion:" title="downloadAvatarWithProfile:thumbnail:progress:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="deleteDeviceByDeviceSN:completion:" %}{% endlanying_code_snippet %}
```
### downloadAvatarWithProfile:thumbnail:progress:completion:

Download avatar

`- (void)downloadAvatarWithProfile:(BMXUserProfile *)*profile* thumbnail:(BOOL)*thumbnail* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgress* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *error ))*aCompletion*`

#### Parameters

*profile*  
   User information  

*aProgress*  
   Download progress  

*aCompletion*  
   Callback  

#### Discussion
Download avatar

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/getDeviceListCompletion:" title="getDeviceListCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="downloadAvatarWithProfile:thumbnail:progress:completion:" %}{% endlanying_code_snippet %}
```
### getDeviceListCompletion:

Get device list

`- (void)getDeviceListCompletion:(void ( ^ ) ( BMXError *error , NSArray *deviceList ))*aCompletionBlock*`

#### Discussion
Get device list

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/getProfileForceRefresh:completion:" title="getProfileForceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="getDeviceListCompletion:" %}{% endlanying_code_snippet %}
```
### getProfileForceRefresh:completion:

Get user details

`- (void)getProfileForceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *aError ))*aCompletionBlock*`

#### Discussion
Get user details

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="getProfileForceRefresh:completion:" %}{% endlanying_code_snippet %}
```
### removeDelegate:

`- (void)removeDelegate:(id<BMXUserServiceProtocol>)*aDelegate*`

<a name="//api/name/setAddFriendAuthMode:completion:" title="setAddFriendAuthMode:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="removeDelegate:" %}{% endlanying_code_snippet %}
```
### setAddFriendAuthMode:completion:

Set method to validate when adding friend

`- (void)setAddFriendAuthMode:(BMXAddFriendAuthMode)*addFriendAuthMode* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*addFriendAuthMode*  
   BMXAddFriendAuthMode  

#### Discussion
Set method to validate when adding friend

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setAuthQuestion:completion:" title="setAuthQuestion:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setAddFriendAuthMode:completion:" %}{% endlanying_code_snippet %}
```
### setAuthQuestion:completion:

Set friend authentication questions

`- (void)setAuthQuestion:(BMXAuthQuestion *)*authQuestion* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*authQuestion*  
   BMXAuthQuestion  

#### Discussion
Set friend authentication questions

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setAutoAcceptGroupInvite:completion:" title="setAutoAcceptGroupInvite:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setAuthQuestion:completion:" %}{% endlanying_code_snippet %}
```
### setAutoAcceptGroupInvite:completion:

Set whether to automatically accept group invitations

`- (void)setAutoAcceptGroupInvite:(BOOL)*autoAcceptGroupInvite* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*autoAcceptGroupInvite*  
   BOOL  

#### Discussion
Set whether to automatically accept group invitations

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setAutoDownloadAttachment:completion:" title="setAutoDownloadAttachment:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setAutoAcceptGroupInvite:completion:" %}{% endlanying_code_snippet %}
```
### setAutoDownloadAttachment:completion:

Set whether to automatically download thumbnail and voice attachment

`- (void)setAutoDownloadAttachment:(BOOL)*autoDownloadAttachment* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*autoDownloadAttachment*  
   BOOL  

#### Discussion
Set whether to automatically download thumbnail and voice attachment

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setEnablePushDetail:completion:" title="setEnablePushDetail:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setAutoDownloadAttachment:completion:" %}{% endlanying_code_snippet %}
```
### setEnablePushDetail:completion:

Set whether to push details

`- (void)setEnablePushDetail:(BOOL)*enablePushDetail* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*enablePushDetail*  
   BOOL  

#### Discussion
Set whether to push details

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setEnablePushStatus:completion:" title="setEnablePushStatus:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setEnablePushDetail:completion:" %}{% endlanying_code_snippet %}
```
### setEnablePushStatus:completion:

Set whether push is allowed

`- (void)setEnablePushStatus:(BOOL)*enablePushStatus* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*enablePushStatus*  
   BOOL  

#### Discussion
Set whether push is allowed

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setNickname:completion:" title="setNickname:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setEnablePushStatus:completion:" %}{% endlanying_code_snippet %}
```
### setNickname:completion:

Set nickname

`- (void)setNickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Set nickname

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setNotificationSound:completion:" title="setNotificationSound:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setNickname:completion:" %}{% endlanying_code_snippet %}
```
### setNotificationSound:completion:

Set whether a new message is audibly alerted

`- (void)setNotificationSound:(BOOL)*notificationSound* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*notificationSound*  
   BOO  

#### Discussion
Set whether a new message is audibly alerted

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setNotificationVibrate:completion:" title="setNotificationVibrate:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setNotificationSound:completion:" %}{% endlanying_code_snippet %}
```
### setNotificationVibrate:completion:

Set whether a new message is alerted in vibration

`- (void)setNotificationVibrate:(BOOL)*notificationVibrate* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*notificationVibrate*  
   BOOL  

#### Discussion
Set whether a new message is alerted in vibration

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setPrivateInfo:completion:" title="setPrivateInfo:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setNotificationVibrate:completion:" %}{% endlanying_code_snippet %}
```
### setPrivateInfo:completion:

Set private extension information

`- (void)setPrivateInfo:(NSString *)*privateInfo* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*privateInfo*  
   string  

#### Discussion
Set private extension information

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setPublicInfo:completion:" title="setPublicInfo:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setPrivateInfo:completion:" %}{% endlanying_code_snippet %}
```
### setPublicInfo:completion:

Set public extension information

`- (void)setPublicInfo:(NSString *)*publicInfo* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*publicInfo*  
   string  

#### Discussion
Set public extension information

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setsetPushNickname:completion:" title="setsetPushNickname:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setPublicInfo:completion:" %}{% endlanying_code_snippet %}
```
### setsetPushNickname:completion:

Set push nickname

`- (void)setsetPushNickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Set push nickname

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/uploadAvatarWithData:progress:" title="uploadAvatarWithData:progress:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setsetPushNickname:completion:" %}{% endlanying_code_snippet %}
```
### uploadAvatarWithData:progress:

Upload avatar

`- (void)uploadAvatarWithData:(NSData *)*avatarData* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgressBlock*`

#### Parameters

*avatarData*  
   Avatar  

*aProgressBlock*  
   Upload progress  

#### Discussion
Upload avatar

#### Declared In
* `BMXUserManager.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="uploadAvatarWithData:progress:" %}{% endlanying_code_snippet %}
```
