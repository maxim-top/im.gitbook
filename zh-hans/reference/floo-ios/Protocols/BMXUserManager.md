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

绑定设备推送token

`- (void)bindDevice:(NSString *)*token* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
绑定设备推送token

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/deleteDeviceByDeviceSN:completion:" title="deleteDeviceByDeviceSN:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="bindDevice:completion:" %}{% endlanying_code_snippet %}
```
### deleteDeviceByDeviceSN:completion:

删除设备

`- (void)deleteDeviceByDeviceSN:(NSInteger)*deviceSN* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
删除设备

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/downloadAvatarWithProfile:thumbnail:progress:completion:" title="downloadAvatarWithProfile:thumbnail:progress:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="deleteDeviceByDeviceSN:completion:" %}{% endlanying_code_snippet %}
```
### downloadAvatarWithProfile:thumbnail:progress:completion:

下载头像

`- (void)downloadAvatarWithProfile:(BMXUserProfile *)*profile* thumbnail:(BOOL)*thumbnail* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgress* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *error ))*aCompletion*`

#### Parameters

*profile*  
   用户信息  

*aProgress*  
   下载进度  

*aCompletion*  
   回调  

#### Discussion
下载头像

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/getDeviceListCompletion:" title="getDeviceListCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="downloadAvatarWithProfile:thumbnail:progress:completion:" %}{% endlanying_code_snippet %}
```
### getDeviceListCompletion:

获取设备列表

`- (void)getDeviceListCompletion:(void ( ^ ) ( BMXError *error , NSArray *deviceList ))*aCompletionBlock*`

#### Discussion
获取设备列表

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/getProfileForceRefresh:completion:" title="getProfileForceRefresh:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="getDeviceListCompletion:" %}{% endlanying_code_snippet %}
```
### getProfileForceRefresh:completion:

获取用户详情

`- (void)getProfileForceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXUserProfile *profile , BMXError *aError ))*aCompletionBlock*`

#### Discussion
获取用户详情

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

设置加好友验证方式

`- (void)setAddFriendAuthMode:(BMXAddFriendAuthMode)*addFriendAuthMode* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*addFriendAuthMode*  
   BMXAddFriendAuthMode  

#### Discussion
设置加好友验证方式

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setAuthQuestion:completion:" title="setAuthQuestion:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setAddFriendAuthMode:completion:" %}{% endlanying_code_snippet %}
```
### setAuthQuestion:completion:

设置加好友验证问题

`- (void)setAuthQuestion:(BMXAuthQuestion *)*authQuestion* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*authQuestion*  
   BMXAuthQuestion  

#### Discussion
设置加好友验证问题

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setAutoAcceptGroupInvite:completion:" title="setAutoAcceptGroupInvite:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setAuthQuestion:completion:" %}{% endlanying_code_snippet %}
```
### setAutoAcceptGroupInvite:completion:

设置是否自动同意入群邀请

`- (void)setAutoAcceptGroupInvite:(BOOL)*autoAcceptGroupInvite* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*autoAcceptGroupInvite*  
   BOOL  

#### Discussion
设置是否自动同意入群邀请

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setAutoDownloadAttachment:completion:" title="setAutoDownloadAttachment:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setAutoAcceptGroupInvite:completion:" %}{% endlanying_code_snippet %}
```
### setAutoDownloadAttachment:completion:

设置是否自动缩略图和语音附件

`- (void)setAutoDownloadAttachment:(BOOL)*autoDownloadAttachment* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*autoDownloadAttachment*  
   BOOL  

#### Discussion
设置是否自动缩略图和语音附件

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setEnablePushDetail:completion:" title="setEnablePushDetail:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setAutoDownloadAttachment:completion:" %}{% endlanying_code_snippet %}
```
### setEnablePushDetail:completion:

设置是否推送详情

`- (void)setEnablePushDetail:(BOOL)*enablePushDetail* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*enablePushDetail*  
   BOOL  

#### Discussion
设置是否推送详情

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setEnablePushStatus:completion:" title="setEnablePushStatus:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setEnablePushDetail:completion:" %}{% endlanying_code_snippet %}
```
### setEnablePushStatus:completion:

设置是否允许推送

`- (void)setEnablePushStatus:(BOOL)*enablePushStatus* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*enablePushStatus*  
   BOOL  

#### Discussion
设置是否允许推送

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setNickname:completion:" title="setNickname:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setEnablePushStatus:completion:" %}{% endlanying_code_snippet %}
```
### setNickname:completion:

设置昵称

`- (void)setNickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
设置昵称

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setNotificationSound:completion:" title="setNotificationSound:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setNickname:completion:" %}{% endlanying_code_snippet %}
```
### setNotificationSound:completion:

设置收到新消息是否声音提醒

`- (void)setNotificationSound:(BOOL)*notificationSound* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*notificationSound*  
   BOO  

#### Discussion
设置收到新消息是否声音提醒

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setNotificationVibrate:completion:" title="setNotificationVibrate:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setNotificationSound:completion:" %}{% endlanying_code_snippet %}
```
### setNotificationVibrate:completion:

设置收到新消息是否震动

`- (void)setNotificationVibrate:(BOOL)*notificationVibrate* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*notificationVibrate*  
   BOOL  

#### Discussion
设置收到新消息是否震动

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setPrivateInfo:completion:" title="setPrivateInfo:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setNotificationVibrate:completion:" %}{% endlanying_code_snippet %}
```
### setPrivateInfo:completion:

设置私有扩展信息

`- (void)setPrivateInfo:(NSString *)*privateInfo* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*privateInfo*  
   string  

#### Discussion
设置私有扩展信息

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setPublicInfo:completion:" title="setPublicInfo:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setPrivateInfo:completion:" %}{% endlanying_code_snippet %}
```
### setPublicInfo:completion:

设置公开扩展信息

`- (void)setPublicInfo:(NSString *)*publicInfo* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*publicInfo*  
   string  

#### Discussion
设置公开扩展信息

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/setsetPushNickname:completion:" title="setsetPushNickname:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setPublicInfo:completion:" %}{% endlanying_code_snippet %}
```
### setsetPushNickname:completion:

设置推送昵称

`- (void)setsetPushNickname:(NSString *)*nickname* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
设置推送昵称

#### Declared In
* `BMXUserManager.h`

<a name="//api/name/uploadAvatarWithData:progress:" title="uploadAvatarWithData:progress:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="setsetPushNickname:completion:" %}{% endlanying_code_snippet %}
```
### uploadAvatarWithData:progress:

上传头像

`- (void)uploadAvatarWithData:(NSData *)*avatarData* progress:(void ( ^ ) ( int progress , BMXError *error ))*aProgressBlock*`

#### Parameters

*avatarData*  
   头像  

*aProgressBlock*  
   上传进度  

#### Discussion
上传头像

#### Declared In
* `BMXUserManager.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXUserManager",function="uploadAvatarWithData:progress:" %}{% endlanying_code_snippet %}
```
