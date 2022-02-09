# BMXConversation Class Reference

  **Inherits from** NSObject  
  **Declared in** BMXConversation.h  

## Properties

<a name="//api/name/conversationId" title="conversationId"></a>
### conversationId

Session Id

`@property (nonatomic, assign, readonly) long long conversationId`

#### Discussion
Session Id

#### Declared In
* `BMXConversation.h`

<a name="//api/name/editMessage" title="editMessage"></a>
### editMessage

Edit message

`@property (nonatomic, copy) NSString *editMessage`

#### Discussion
Edit message

#### Declared In
* `BMXConversation.h`

<a name="//api/name/extensionJson" title="extensionJson"></a>
### extensionJson

Extension information

`@property (nonatomic, copy) NSString *extensionJson`

#### Discussion
Extension information

#### Declared In
* `BMXConversation.h`

<a name="//api/name/isMuteNotication" title="isMuteNotication"></a>
### isMuteNotication

Whether the user is alerted to the message, without which the session total unread-number does not count this session.

`@property (nonatomic, assign) BOOL isMuteNotication`

#### Discussion
Whether the user is alerted to the message, without which the session total unread-number does not count this session.

#### Declared In
* `BMXConversation.h`

<a name="//api/name/lastMessage" title="lastMessage"></a>
### lastMessage

Latest message

`@property (nonatomic, strong, readonly) BMXMessageObject *lastMessage`

#### Discussion
Latest message

#### Declared In
* `BMXConversation.h`

<a name="//api/name/messageCount" title="messageCount"></a>
### messageCount

Number of all messages in session

`@property (nonatomic, assign, readonly) NSInteger messageCount`

#### Discussion
Number of all messages in session

#### Declared In
* `BMXConversation.h`

<a name="//api/name/type" title="type"></a>
### type

Session type

`@property (nonatomic, assign, readonly) BMXConversationType type`

#### Discussion
Session type

#### Declared In
* `BMXConversation.h`

<a name="//api/name/unreadNumber" title="unreadNumber"></a>
### unreadNumber

Number of unread messages

`@property (nonatomic, assign, readonly) NSInteger unreadNumber`

#### Discussion
Number of unread messages

#### Declared In
* `BMXConversation.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/insertMessage:completion:" title="insertMessage:completion:"></a>
### insertMessage:completion:

Insert a message

`- (void)insertMessage:(BMXMessageObject *)*msg* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*msg*  
   message  

*aCompletionBlock*  
   Result  

#### Discussion
Insert a message

#### Declared In
* `BMXConversation.h`

<a name="//api/name/loadMessage:completion:" title="loadMessage:completion:"></a>
### loadMessage:completion:

Read a message

`- (void)loadMessage:(long long)*msgId* completion:(void ( ^ ) ( BMXMessageObject *message ))*aCompletionBlock*`

#### Parameters

*msgId*  
   msgId  

*aCompletionBlock*  
   Result  

#### Discussion
Read a message

#### Declared In
* `BMXConversation.h`

<a name="//api/name/loadMessageFromMessageId:size:completion:" title="loadMessageFromMessageId:size:completion:"></a>
### loadMessageFromMessageId:size:completion:

Load messages, starting from the reference message to load earlier messages; starting from the latest message if not specified

`- (void)loadMessageFromMessageId:(long long)*reMsgId* size:(NSUInteger)*size* completion:(void ( ^ ) ( NSArray *messageList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*reMsgId*  
   Reference message Id  

*size*  
   size  

*aCompletionBlock*  
   Result:MessageList  

#### Discussion
Load messages, starting from the reference message to load earlier messages; starting from the latest message if not specified

#### Declared In
* `BMXConversation.h`

<a name="//api/name/removeAllMessagescompletion:" title="removeAllMessagescompletion:"></a>
### removeAllMessagescompletion:

Delete all messages in sesstion

`- (void)removeAllMessagescompletion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*aCompletionBlock*  
   Result  

#### Discussion
Delete all messages in sesstion

#### Declared In
* `BMXConversation.h`

<a name="//api/name/searchMessagesByKeyWords:refTime:size:directionType:completion:" title="searchMessagesByKeyWords:refTime:size:directionType:completion:"></a>
### searchMessagesByKeyWords:refTime:size:directionType:completion:

Search for messages, starting with latest if not specified

`- (void)searchMessagesByKeyWords:(NSString *)*keywords* refTime:(NSTimeInterval)*refTime* size:(NSUInteger)*size* directionType:(BMXMessageDirection)*directionType* completion:(void ( ^ ) ( NSArray<BMXMessageObject*> *messageList , BMXError *error ))*aCompletionBlock*`

#### Discussion
Search for messages, starting with latest if not specified

#### Declared In
* `BMXConversation.h`

<a name="//api/name/searchMessagesBycontentType:refTime:size:directionType:completion:" title="searchMessagesBycontentType:refTime:size:directionType:completion:"></a>
### searchMessagesBycontentType:refTime:size:directionType:completion:

Search for messages by type, starting with latest if not specified

`- (void)searchMessagesBycontentType:(BMXContentType)*contentType* refTime:(NSTimeInterval)*refTime* size:(NSUInteger)*size* directionType:(BMXMessageDirection)*directionType* completion:(void ( ^ ) ( NSArray<BMXMessageObject*> *messageList , BMXError *error ))*aCompletionBlock*`

#### Discussion
Search for messages by type, starting with latest if not specified

#### Declared In
* `BMXConversation.h`

<a name="//api/name/setAllMessagesReadCompletion:" title="setAllMessagesReadCompletion:"></a>
### setAllMessagesReadCompletion:

Set all messages to read, update number of unread messages

`- (void)setAllMessagesReadCompletion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
Set all messages to read, update number of unread messages

#### Declared In
* `BMXConversation.h`

<a name="//api/name/setMessagePlayedStatus:status:completion:" title="setMessagePlayedStatus:status:completion:"></a>
### setMessagePlayedStatus:status:completion:

Set message playback state (valid only for voice/video messages)

`- (void)setMessagePlayedStatus:(BMXMessageObject *)*message* status:(bool)*status* completion:(void ( ^ ) ( BMXMessageObject *aMessage , BMXError *error ))*aCompletionBlock*`

#### Parameters

*message*  
   message  

*status*  
   Playback state  

*aCompletionBlock*  
   Result  

#### Discussion
Set message playback state (valid only for voice/video messages)

#### Declared In
* `BMXConversation.h`

<a name="//api/name/setMessageReadStatus:status:completion:" title="setMessageReadStatus:status:completion:"></a>
### setMessageReadStatus:status:completion:

Set message unread state, update the number of unread messages locally

`- (void)setMessageReadStatus:(BMXMessageObject *)*message* status:(BOOL)*status* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*message*  
   message  

*status*  
   Read or unread  

*aCompletionBlock*  
   Result  

#### Discussion
Set message unread state, update the number of unread messages locally

#### Declared In
* `BMXConversation.h`

<a name="//api/name/updateMessageExtension:completion:" title="updateMessageExtension:completion:"></a>
### updateMessageExtension:completion:

Update the extend field info of a database-stored message

`- (void)updateMessageExtension:(BMXMessageObject *)*message* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*message*  
   The message that needs to change the extension information when the msg section has updated its extension field  

*aCompletionBlock*  
   Update result  

#### Discussion
Update the extend field info of a database-stored message

#### Declared In
* `BMXConversation.h`

