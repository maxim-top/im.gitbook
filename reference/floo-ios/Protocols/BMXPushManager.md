# BMXPushManager Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXPushManager.h  

## Overview

Push manager

## Instance Methods

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
### addDelegate:

`- (void)addDelegate:(id<BMXPushServiceProtocol>)*aDelegate*`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXPushServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/addPushListener:" title="addPushListener:"></a>
### addPushListener:

Add chat listener

`- (void)addPushListener:(id<BMXPushServiceProtocol>)*listener*`

#### Parameters

*listener*  
   Listener  

#### Discussion
Add chat listener

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/bindDeviceToken:completion:" title="bindDeviceToken:completion:"></a>
### bindDeviceToken:completion:

Push binding device token.

`- (void)bindDeviceToken:(NSString *)*deviceToken* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*deviceToken*  
   token device's push token  

*aCompletionBlock*  
   Bind callback  

#### Discussion
Push binding device token.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/clearAllNotifications" title="clearAllNotifications"></a>
### clearAllNotifications

Used to remove all pushes displayed in Notification

`- (void)clearAllNotifications`

#### Discussion
Used to remove all pushes displayed in Notification

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/clearNotification:" title="clearNotification:"></a>
### clearNotification:

  Used to remove the specified push displayed in Notification
  iOS 10 and over support to remove specified push by identifier
  For iOS 10 and earlier versions, remove all pushes if identifier is set to 0

`- (void)clearNotification:(NSInteger)*notificationId*`

#### Parameters

*notificationId*  
   If notificationId is set to 0, remove all pushes  

#### Discussion
  Used to remove the specified push displayed in Notification
  iOS 10 and over support to remove specified push by identifier
  For iOS 10 and earlier versions, remove all pushes if identifier is set to 0

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/clearTagsByOperationId:" title="clearTagsByOperationId:"></a>
### clearTagsByOperationId:

Clear tags of the push user.

`- (void)clearTagsByOperationId:(NSString *)*operationId*`

#### Parameters

*operationId*  
   Operation id. Corresponding notification reminder in callback notification.  

#### Discussion
Clear tags of the push user.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/deleteTags:operationId:" title="deleteTags:operationId:"></a>
### deleteTags:operationId:

Delete tags of the push user.

`- (void)deleteTags:(NSArray<NSString*> *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

*tags*  
   User tag to delete  

*operationId*  
   Operation id. Corresponding notification reminder in callback notification.  

#### Discussion
Delete tags of the push user.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/getCertification" title="getCertification"></a>
### getCertification

Get push certificate returned by server after login.

`- (void)getCertification`

#### Discussion
Get push certificate returned by server after login.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/getPushProfileForceRefresh:completion:" title="getPushProfileForceRefresh:completion:"></a>
### getPushProfileForceRefresh:completion:

Get push user details, force pull from server-side if forceRefresh == true

`- (void)getPushProfileForceRefresh:(BOOL)*forceRefresh* completion:(void ( ^ ) ( BMXPushUserProfile *profile , BMXError *aError ))*aCompletionBlock*`

#### Parameters

*forceRefresh*  
   Whether to force pull from server, automatically if local fetch failed  

*profile*
   Push user profile information, initially passing in a pointing-to-empty shared_ptr object, fetch the user profile information here after function returned.

#### Discussion
Get push user details, force pull from server-side if forceRefresh == true

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/getTagsByOperationId:withCompletion:" title="getTagsByOperationId:withCompletion:"></a>
### getTagsByOperationId:withCompletion:

Get tags of the push user.

`- (void)getTagsByOperationId:(NSString *)*operationId* withCompletion:(void ( ^ ) ( NSArray *tags , BMXError *error ))*aCompletionBlock*`

#### Parameters

*operationId*  
   Operation id. Corresponding notification reminder in callback notification.  

*aCompletionBlock*  
   Get callback  

#### Discussion
Get tags of the push user.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/getToken" title="getToken"></a>
### getToken

Get user token to use after login.

`- (void)getToken`

#### Discussion
Get user token to use after login.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/loadLocalPushMessagesFromMessageId:size:directionType:completion:" title="loadLocalPushMessagesFromMessageId:size:directionType:completion:"></a>
### loadLocalPushMessagesFromMessageId:size:directionType:completion:

Load push message stored locally in database. Start with latest message if not specified

`- (void)loadLocalPushMessagesFromMessageId:(long long)*reMsgId* size:(NSUInteger)*size* directionType:(BMXPushMessageDirection)*directionType* completion:(void ( ^ ) ( NSArray *messageList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*reMsgId*  
   Start id for loading pushes  

*size*  
   Maximum number of loaded messages  

*directionType*  
   List of loaded local pushes returned by database  

*aCompletionBlock*  
   Direction of loading pushes, default to load earlier messages  

#### Discussion
Load push message stored locally in database. Start with latest message if not specified

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
### removeDelegate:

`- (void)removeDelegate:(id<BMXPushServiceProtocol>)*aDelegate*`

<a name="//api/name/removePushListener:" title="removePushListener:"></a>
### removePushListener:

Remove chat listener

`- (void)removePushListener:(id<BMXPushServiceProtocol>)*listener*`

#### Parameters

*listener*  
   Listener  

#### Discussion
Remove chat listener

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/resume" title="resume"></a>
### resume

Restore push feature interface.

`- (void)resume`

#### Discussion
Restore push feature interface.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/sendMessage:" title="sendMessage:"></a>
### sendMessage:

Send a push uplink message and notify the listener of a change in message status

`- (void)sendMessage:(NSString *)*message*`

#### Parameters

*message*  
   Sent uplink push content  

#### Discussion
Send a push uplink message and notify the listener of a change in message status

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/setBadge:" title="setBadge:"></a>
### setBadge:

Set unread badge for push user.

`- (void)setBadge:(int)*count*`

#### Parameters

*count*  
   Unread badge count of user  

#### Discussion
Set unread badge for push user.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/setPushMode:" title="setPushMode:"></a>
### setPushMode:

Set push enabled state. Default enabled.

`- (void)setPushMode:(BOOL)*enable*`

#### Parameters

*enable*  
   Enabled state of push  

#### Discussion
Set push enabled state. Default enabled.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/setPushTimeStartHour:endHour:" title="setPushTimeStartHour:endHour:"></a>
### setPushTimeStartHour:endHour:

Set allowed push time.

`- (void)setPushTimeStartHour:(int)*startHour* endHour:(int)*endHour*`

#### Parameters

*startHour*  
   Start time for allowed silent push (hour)  

*endHour*  
   End time for allowed silent push (hour)  

#### Discussion
Set allowed push time.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/setSlienceTimeStartHour:endHour:" title="setSlienceTimeStartHour:endHour:"></a>
### setSlienceTimeStartHour:endHour:

Set the start and end time of silent push.

`- (void)setSlienceTimeStartHour:(int)*startHour* endHour:(int)*endHour*`

#### Parameters

*startHour*  
   Start time for silent push (hour)  

*endHour*  
   End time for silent push (hour)  

#### Discussion
Set the start and end time of silent push.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/setTags:operationId:" title="setTags:operationId:"></a>
### setTags:operationId:

Set tags of push user.

`- (void)setTags:(NSArray<NSString*> *)*tags* operationId:(NSString *)*operationId*`

#### Parameters

*tags*  
   User tag  

*operationId*  
   Operation id. Corresponding notification reminder in callback notification.  

#### Discussion
Set tags of push user.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/start" title="start"></a>
### start

Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.

`- (void)start`

#### Discussion
Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/startWithAlias:" title="startWithAlias:"></a>
### startWithAlias:

Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.

`- (void)startWithAlias:(NSString *)*alias*`

#### Parameters

*alias*  
   Current user alias used for push initialization  

#### Discussion
Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/startWithAlias:bmxToken:" title="startWithAlias:bmxToken:"></a>
### startWithAlias:bmxToken:

Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.

`- (void)startWithAlias:(NSString *)*alias* bmxToken:(NSString *)*bmxToken*`

#### Parameters

*alias*  
   Current user alias used for push initialization  

*bmxToken*  
   User token passed in by App when push initialization.  

#### Discussion
Initialize push sdk. Use this interface to initialize the push sdk in the case of using push only. When using IM features at the same time, call login function directly in BMXClient. The config object initializes by passing in the platform type and device id.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/status" title="status"></a>
### status

Push the current state of sdk.

`- (BMXPushSdkStatus)status`

#### Discussion
Push the current state of sdk.

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/stop" title="stop"></a>
### stop

Function interface for stop push

`- (void)stop`

#### Discussion
Function interface for stop push

#### Declared In
* `BMXPushManager.h`

<a name="//api/name/unbindAlias:" title="unbindAlias:"></a>
### unbindAlias:

Unbind user alias.

`- (void)unbindAlias:(NSString *)*alias*`

#### Parameters

*alias*  
   The user alias that needs to be unbound.  

#### Discussion
Unbind user alias.

#### Declared In
* `BMXPushManager.h`

