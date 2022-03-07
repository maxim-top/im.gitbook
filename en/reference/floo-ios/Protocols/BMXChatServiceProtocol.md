# BMXChatServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXChatServiceProtocol.h  

## Instance Methods

<a name="//api/name/conversationDidCreatedConversation:message:" title="conversationDidCreatedConversation:message:"></a>
### conversationDidCreatedConversation:message:

New conversation locally created

`- (void)conversationDidCreatedConversation:(BMXConversation *)*conversation* message:(BMXMessageObject *)*message*`

#### Parameters

*conversation*  
   Newly created local conversation  

*message*  
   Latest message for conversation, return for existing, empty for no existing  

#### Discussion
New conversation locally created

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/conversationDidDeletedConversationId:error:" title="conversationDidDeletedConversationId:error:"></a>
### conversationDidDeletedConversationId:error:

 Delete a conversation

`- (void)conversationDidDeletedConversationId:(NSInteger)*conversationId* error:(BMXError *)*error*`

#### Parameters

*conversationId*  
   Deleted local conversation id  

*error*  
   State error code  

#### Discussion
 Delete a conversation

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/conversationTotalCountChanged:" title="conversationTotalCountChanged:"></a>
### conversationTotalCountChanged:

Update total number of unread messages

`- (void)conversationTotalCountChanged:(NSInteger)*unreadCount*`

#### Parameters

*unreadCount*  
   Number of unreads  

#### Discussion
Update total number of unread messages

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/loadAllConversationDidFinished" title="loadAllConversationDidFinished"></a>
### loadAllConversationDidFinished

List of unread conversations has been loaded

`- (void)loadAllConversationDidFinished`

#### Discussion
List of unread conversations has been loaded

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/messageAttachmentStatusDidChanged:error:percent:" title="messageAttachmentStatusDidChanged:error:percent:"></a>
### messageAttachmentStatusDidChanged:error:percent:

Attachment download state changed

`- (void)messageAttachmentStatusDidChanged:(BMXMessageObject *)*message* error:(BMXError *)*error* percent:(int)*percent*`

#### Discussion
Attachment download state changed

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/messageAttachmentUploadProgressChanged:percent:" title="messageAttachmentUploadProgressChanged:percent:"></a>
### messageAttachmentUploadProgressChanged:percent:

Attachment upload state changed

`- (void)messageAttachmentUploadProgressChanged:(BMXMessageObject *)*message* percent:(int)*percent*`

#### Discussion
Attachment upload state changed

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/messageRecallStatusDidChanged:error:" title="messageRecallStatusDidChanged:error:"></a>
### messageRecallStatusDidChanged:error:

Message recall state changed

`- (void)messageRecallStatusDidChanged:(BMXMessageObject *)*message* error:(BMXError *)*error*`

#### Discussion
Message recall state changed

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/messageStatusChanged:error:" title="messageStatusChanged:error:"></a>
### messageStatusChanged:error:

Message state changed

`- (void)messageStatusChanged:(BMXMessageObject *)*message* error:(BMXError *)*error*`

#### Discussion
Message state changed

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receiveDeleteMessages:" title="receiveDeleteMessages:"></a>
### receiveDeleteMessages:

 Message deletions received (delete messages cross devices synchronously)

`- (void)receiveDeleteMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
 Message deletions received (delete messages cross devices synchronously)

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receiveReadAllMessages:" title="receiveReadAllMessages:"></a>
### receiveReadAllMessages:

All received messages are read (all messages are set to read before cross-device synchronization)

`- (void)receiveReadAllMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
All received messages are read (all messages are set to read before cross-device synchronization)

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receiveReadCancelsMessages:" title="receiveReadCancelsMessages:"></a>
### receiveReadCancelsMessages:

Message re-unread received (cross-device synchronization for changing message status into unread)

`- (void)receiveReadCancelsMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
Message re-unread received (cross-device synchronization for changing message status into unread)

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receivedCommandMessages:" title="receivedCommandMessages:"></a>
### receivedCommandMessages:

Command received

`- (void)receivedCommandMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
Command received

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receivedDeliverAcks:" title="receivedDeliverAcks:"></a>
### receivedDeliverAcks:

Acknowledgement of message delivered received

`- (void)receivedDeliverAcks:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
Acknowledgement of message delivered received

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receivedMessages:" title="receivedMessages:"></a>
### receivedMessages:

Messages received

`- (void)receivedMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
Messages received

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receivedReadAcks:" title="receivedReadAcks:"></a>
### receivedReadAcks:

Read acknowledgement of messages received

`- (void)receivedReadAcks:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
Read acknowledgement of messages received

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receivedRecallMessages:" title="receivedRecallMessages:"></a>
### receivedRecallMessages:

Canceled messages received

`- (void)receivedRecallMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
Canceled messages received

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receivedSystemMessages:" title="receivedSystemMessages:"></a>
### receivedSystemMessages:

System notification messages received

`- (void)receivedSystemMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
System notification messages received

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/retrieveHistoryMessagesConversation:" title="retrieveHistoryMessagesConversation:"></a>
### retrieveHistoryMessagesConversation:

Pull message history

`- (void)retrieveHistoryMessagesConversation:(BMXConversation *)*conversation*`

#### Discussion
Pull message history

#### Declared In
* `BMXChatServiceProtocol.h`

