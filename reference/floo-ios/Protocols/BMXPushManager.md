# BMXPushManager Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXPushManager.h  

## Overview

推送管理器

## Instance Methods

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
### addDelegate:

`- (void)addDelegate:(id<BMXPushServiceProtocol>)*aDelegate*`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXPushServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/addPushListener:" title="addPushListener:"></a>
### addPushListener:

添加聊天监听者

`- (void)addPushListener:(id<BMXPushServiceProtocol>)*listener*`

#### Parameters

*listener*  
   监听者  

#### Discussion
添加聊天监听者

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/bindDeviceToken:completion:" title="bindDeviceToken:completion:"></a>
### bindDeviceToken:completion:

推送绑定设备token。

`- (void)bindDeviceToken:(NSString *)*deviceToken* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*deviceToken*  
   token 设备的推送token  

*aCompletionBlock*  
   绑定回调  

#### Discussion
推送绑定设备token。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/clearAllNotifications" title="clearAllNotifications"></a>
### clearAllNotifications

用于移除在通知中心显示的所有推送

`- (void)clearAllNotifications`

#### Discussion
用于移除在通知中心显示的所有推送

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/clearNotification:" title="clearNotification:"></a>
### clearNotification:

  用于移除在通知中心显示的指定推送
  iOS 10 以上 支持通过identifier 移除指定推送
  iOS 10 以下 identifier 设置为 0 ，则移除所有推送

`- (void)clearNotification:(NSInteger)*notificationId*`

#### Parameters

*notificationId*  
   如果notificationId 置 0 ，则移除所有推送  

#### Discussion
  用于移除在通知中心显示的指定推送
  iOS 10 以上 支持通过identifier 移除指定推送
  iOS 10 以下 identifier 设置为 0 ，则移除所有推送

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/clearTagsByOperationId:" title="clearTagsByOperationId:"></a>
### clearTagsByOperationId:

清空推送用户的标签。

`- (void)clearTagsByOperationId:(NSString *)*operationId*`

#### Parameters

*operationId*  
   操作id。在回调通知中对应通知提醒。  

#### Discussion
清空推送用户的标签。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/deleteTags:operationId:" title="deleteTags:operationId:"></a>
### deleteTags:operationId:

删除推送用户的标签。

`- (void)deleteTags:(NSArray<NSString*> *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

*tags*  
   要删除用户标签  

*operationId*  
   操作id。在回调通知中对应通知提醒。  

#### Discussion
删除推送用户的标签。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/getCertification" title="getCertification"></a>
### getCertification

获取登陆后服务器返回的推送证书。

`- (void)getCertification`

#### Discussion
获取登陆后服务器返回的推送证书。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/getPushProfileForceRefresh:completion:" title="getPushProfileForceRefresh:completion:"></a>
### getPushProfileForceRefresh:completion:

获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取

`- (void)getPushProfileForceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXPushUserProfile *profile , BMXError *aError ))*aCompletionBlock*`

#### Parameters

*forceRefresh*  
   是否强制从服务器拉取，本地获取失败的情况下会自动从服务器拉取  

*profile*  
   推送用户profile信息，初始传入指向为空的shared_ptr对象，函数返回后从此处获取用户profile信息。  

#### Discussion
获取推送用户详情，如果forceRefresh == true，则强制从服务端拉取

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/getTagsByOperationId:withCompletion:" title="getTagsByOperationId:withCompletion:"></a>
### getTagsByOperationId:withCompletion:

获取推送用户的标签。

`- (void)getTagsByOperationId:(NSString *)*operationId* withCompletion:(void ( ^ ) ( NSArray *tags , BMXError *error ))*aCompletionBlock*`

#### Parameters

*operationId*  
   操作id。在回调通知中对应通知提醒。  

*aCompletionBlock*  
   获取回调  

#### Discussion
获取推送用户的标签。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/getToken" title="getToken"></a>
### getToken

获取登陆后使用的用户token。

`- (void)getToken`

#### Discussion
获取登陆后使用的用户token。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/loadLocalPushMessagesFromMessageId:size:directionType:completion:" title="loadLocalPushMessagesFromMessageId:size:directionType:completion:"></a>
### loadLocalPushMessagesFromMessageId:size:directionType:completion:

加载数据库本地存储的推送消息。如果不指定则从最新消息开始

`- (void)loadLocalPushMessagesFromMessageId:(long long)*reMsgId* size:(NSUInteger)*size* directionType:(BMXPushMessageDirection)*directionType* completion:(void ( ^ ) ( NSArray *messageList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*reMsgId*  
   加载推送消息的起始id  

*size*  
   最大加载消息条数  

*directionType*  
   数据库返回的加载本地推送消息列表  

*aCompletionBlock*  
   加载推送消息的方向，默认是加载更早的消息  

#### Discussion
加载数据库本地存储的推送消息。如果不指定则从最新消息开始

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
### removeDelegate:

`- (void)removeDelegate:(id<BMXPushServiceProtocol>)*aDelegate*`

<a name="//api/name/removePushListener:" title="removePushListener:"></a>
### removePushListener:

移除聊天监听者

`- (void)removePushListener:(id<BMXPushServiceProtocol>)*listener*`

#### Parameters

*listener*  
   监听者  

#### Discussion
移除聊天监听者

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/resume" title="resume"></a>
### resume

恢复推送功能接口。

`- (void)resume`

#### Discussion
恢复推送功能接口。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/sendMessage:" title="sendMessage:"></a>
### sendMessage:

发送推送上行消息，消息状态变化会通过listener通知

`- (void)sendMessage:(NSString *)*message*`

#### Parameters

*message*  
   发送的上行推送消息内容  

#### Discussion
发送推送上行消息，消息状态变化会通过listener通知

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/setBadge:" title="setBadge:"></a>
### setBadge:

设置推送用户的未读角标。

`- (void)setBadge:(int)*count*`

#### Parameters

*count*  
   用户未读角标数  

#### Discussion
设置推送用户的未读角标。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/setPushMode:" title="setPushMode:"></a>
### setPushMode:

设置推送启用状态。默认为使用推送。

`- (void)setPushMode:(BOOL)*enable*`

#### Parameters

*enable*  
   推送的启用状态  

#### Discussion
设置推送启用状态。默认为使用推送。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/setPushTimeStartHour:endHour:" title="setPushTimeStartHour:endHour:"></a>
### setPushTimeStartHour:endHour:

设置允许推送时间。

`- (void)setPushTimeStartHour:(int)*startHour* endHour:(int)*endHour*`

#### Parameters

*startHour*  
   静默允许推送的起始时间小时  

*endHour*  
   静默允许推送的结束时间小时  

#### Discussion
设置允许推送时间。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/setSlienceTimeStartHour:endHour:" title="setSlienceTimeStartHour:endHour:"></a>
### setSlienceTimeStartHour:endHour:

设置推送静默的起始结束时间。

`- (void)setSlienceTimeStartHour:(int)*startHour* endHour:(int)*endHour*`

#### Parameters

*startHour*  
   静默推送的起始时间小时  

*endHour*  
   静默推送的结束时间小时  

#### Discussion
设置推送静默的起始结束时间。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/setTags:operationId:" title="setTags:operationId:"></a>
### setTags:operationId:

设置推送用户的标签。

`- (void)setTags:(NSArray<NSString*> *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

*tags*  
   用户标签  

*operationId*  
   操作id。在回调通知中对应通知提醒。  

#### Discussion
设置推送用户的标签。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/start" title="start"></a>
### start

初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。

`- (void)start`

#### Discussion
初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/startWithAlias:" title="startWithAlias:"></a>
### startWithAlias:

初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。

`- (void)startWithAlias:(NSString *)*alias*`

#### Parameters

*alias*  
   推送初始化使用的当前用户别名  

#### Discussion
初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/startWithAlias:bmxToken:" title="startWithAlias:bmxToken:"></a>
### startWithAlias:bmxToken:

初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。

`- (void)startWithAlias:(NSString *)*alias* bmxToken:(NSString *)*bmxToken*`

#### Parameters

*alias*  
   推送初始化使用的当前用户别名  

*bmxToken*  
   推送初始化的时候App传入的使用的用户的token。  

#### Discussion
初始化推送sdk。在仅使用推送的情况下使用该接口初始化推送sdk。在同时使用IM功能的时候直接在BMXClient调用登陆功能即可。config对象初始化的时候需要传入平台类型和设备id。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/status" title="status"></a>
### status

推送sdk当前的状态。

`- (BMXPushSdkStatus)status`

#### Discussion
推送sdk当前的状态。

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/stop" title="stop"></a>
### stop

停止推送功能接口

`- (void)stop`

#### Discussion
停止推送功能接口

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/unbindAlias:" title="unbindAlias:"></a>
### unbindAlias:

解除用户别名绑定。

`- (void)unbindAlias:(NSString *)*alias*`

#### Parameters

*alias*  
   需要解除绑定的用户别名。  

#### Discussion
解除用户别名绑定。

#### Declared In
* `BMXPushManager.h`

