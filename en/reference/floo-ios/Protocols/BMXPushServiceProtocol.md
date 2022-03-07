# BMXPushServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXPushServiceProtocol.h  

## Instance Methods

<a name="//api/name/certRetrieved:" title="certRetrieved:"></a>
### certRetrieved:

Get push certificate after push initialization.

`- (void)certRetrieved:(NSString *)*certification*`

#### Parameters

*certification*  
   Push certificate  

#### Discussion
Get push certificate after push initialization.

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/clearedTags:" title="clearedTags:"></a>
### clearedTags:

Clear callback of user push success.

`- (void)clearedTags:(NSString *)*operationId*`

#### Parameters

*operationId*  
   Operation id  

#### Discussion
Clear callback of user push success.

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/deleteTagsDidFinished:" title="deleteTagsDidFinished:"></a>
### deleteTagsDidFinished:

Delete callback for succeeded tag of user push.

`- (void)deleteTagsDidFinished:(NSString *)*operationId*`

#### Parameters

*operationId*  
   Operation id  

#### Discussion
Delete callback for succeeded tag of user push.

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/getTagsDidFinished:" title="getTagsDidFinished:"></a>
### getTagsDidFinished:

Get callback for succeeded tag of user push.

`- (void)getTagsDidFinished:(NSString *)*operationId*`

#### Parameters

*operationId*  
   Operation id  

#### Discussion
Get callback for succeeded tag of user push.

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/pushMessageStatusChanged:error:" title="pushMessageStatusChanged:error:"></a>
### pushMessageStatusChanged:error:

Send notification of push uplink message status change.

`- (void)pushMessageStatusChanged:(BMXMessageObject *)*message* error:(BMXError *)*error*`

#### Parameters

*message*  
   Uplink message with state change  

*error*  
   State error code  

#### Discussion
Send notification of push uplink message status change.

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/pushStartDidFinished:" title="pushStartDidFinished:"></a>
### pushStartDidFinished:

Notification of push initialization complete.

`- (void)pushStartDidFinished:(NSString *)*bmxToken*`

#### Parameters

*bmxToken*  
   bmxToken  

#### Discussion
Notification of push initialization complete.

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/pushStartDidStopped" title="pushStartDidStopped"></a>
### pushStartDidStopped

Notification of push feature stop.

`- (void)pushStartDidStopped`

#### Discussion
Notification of push feature stop.

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/receivedPush:" title="receivedPush:"></a>
### receivedPush:

New push notification received

`- (void)receivedPush:(NSArray<BMXMessageObject*> *)*messages*`

#### Parameters

*messages*  
   Push notification list  

#### Discussion
New push notification received

#### Declared In
* `BMXPushServiceProtocol.h`

<a name="//api/name/setTagsDidFinished:" title="setTagsDidFinished:"></a>
### setTagsDidFinished:

Set callback for succeeded tag of user push.

`- (void)setTagsDidFinished:(NSString *)*operationId*`

#### Parameters

*operationId*  
   Operation id  

#### Discussion
Set callback for succeeded tag of user push.

#### Declared In
* `BMXPushServiceProtocol.h`

