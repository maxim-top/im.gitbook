# BMXUserManager Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXUserManager.h  

## Instance Methods

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
### addDelegate:

`- (void)addDelegate:(id<BMXUserServiceProtocol>)*aDelegate*`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXUserServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/bindDevice:completion:" title="bindDevice:completion:"></a>
### bindDevice:completion:

Binding device push token

`- (void)bindDevice:(NSString *)*token* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Binding device push token

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/deleteDeviceByDeviceSN:completion:" title="deleteDeviceByDeviceSN:completion:"></a>
### deleteDeviceByDeviceSN:completion:

Delete device

`- (void)deleteDeviceByDeviceSN:(NSInteger)*deviceSN* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Delete device

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/downloadAvatarWithProfile:thumbnail:progress:completion:" title="downloadAvatarWithProfile:thumbnail:progress:completion:"></a>
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
### getDeviceListCompletion:

Get device list

`- (void)getDeviceListCompletion:(void ( ^ ) ( BMXError *error , NSArray *deviceList ))*aCompletionBlock*`

#### Discussion
Get device list

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/getProfileForceRefresh:completion:" title="getProfileForceRefresh:completion:"></a>
### getProfileForceRefresh:completion:

Get user details

`- (void)getProfileForceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *aError ))*aCompletionBlock*`

#### Discussion
Get user details

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
### removeDelegate:

`- (void)removeDelegate:(id<BMXUserServiceProtocol>)*aDelegate*`

<a name="//api/name/setAddFriendAuthMode:completion:" title="setAddFriendAuthMode:completion:"></a>
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
### setNickname:completion:

Set nickname

`- (void)setNickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Set nickname

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setNotificationSound:completion:" title="setNotificationSound:completion:"></a>
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
### setsetPushNickname:completion:

Set push nickname

`- (void)setsetPushNickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Set push nickname

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/uploadAvatarWithData:progress:" title="uploadAvatarWithData:progress:"></a>
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

