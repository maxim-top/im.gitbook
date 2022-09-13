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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="conversationDidCreatedConversation:message:" %}{% endlanying_code_snippet %}
```
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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="conversationDidDeletedConversationId:error:" %}{% endlanying_code_snippet %}
```
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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="conversationTotalCountChanged:" %}{% endlanying_code_snippet %}
```
### loadAllConversationDidFinished

List of unread conversations has been loaded

`- (void)loadAllConversationDidFinished`

#### Discussion
List of unread conversations has been loaded

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/messageAttachmentStatusDidChanged:error:percent:" title="messageAttachmentStatusDidChanged:error:percent:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="loadAllConversationDidFinished" %}{% endlanying_code_snippet %}
```
### messageAttachmentStatusDidChanged:error:percent:

Attachment download state changed

`- (void)messageAttachmentStatusDidChanged:(BMXMessageObject *)*message* error:(BMXError *)*error* percent:(int)*percent*`

#### Discussion
Attachment download state changed

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/messageAttachmentUploadProgressChanged:percent:" title="messageAttachmentUploadProgressChanged:percent:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="messageAttachmentStatusDidChanged:error:percent:" %}{% endlanying_code_snippet %}
```
### messageAttachmentUploadProgressChanged:percent:

Attachment upload state changed

`- (void)messageAttachmentUploadProgressChanged:(BMXMessageObject *)*message* percent:(int)*percent*`

#### Discussion
Attachment upload state changed

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/messageRecallStatusDidChanged:error:" title="messageRecallStatusDidChanged:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="messageAttachmentUploadProgressChanged:percent:" %}{% endlanying_code_snippet %}
```
### messageRecallStatusDidChanged:error:

Message recall state changed

`- (void)messageRecallStatusDidChanged:(BMXMessageObject *)*message* error:(BMXError *)*error*`

#### Discussion
Message recall state changed

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/messageStatusChanged:error:" title="messageStatusChanged:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="messageRecallStatusDidChanged:error:" %}{% endlanying_code_snippet %}
```
### messageStatusChanged:error:

Message state changed

`- (void)messageStatusChanged:(BMXMessageObject *)*message* error:(BMXError *)*error*`

#### Discussion
Message state changed

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receiveDeleteMessages:" title="receiveDeleteMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="messageStatusChanged:error:" %}{% endlanying_code_snippet %}
```
### receiveDeleteMessages:

 Message deletions received (delete messages cross devices synchronously)

`- (void)receiveDeleteMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
 Message deletions received (delete messages cross devices synchronously)

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receiveReadAllMessages:" title="receiveReadAllMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receiveDeleteMessages:" %}{% endlanying_code_snippet %}
```
### receiveReadAllMessages:

All received messages are read (all messages are set to read before cross-device synchronization)

`- (void)receiveReadAllMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
All received messages are read (all messages are set to read before cross-device synchronization)

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receiveReadCancelsMessages:" title="receiveReadCancelsMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receiveReadAllMessages:" %}{% endlanying_code_snippet %}
```
### receiveReadCancelsMessages:

Message re-unread received (cross-device synchronization for changing message status into unread)

`- (void)receiveReadCancelsMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
Message re-unread received (cross-device synchronization for changing message status into unread)

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receivedCommandMessages:" title="receivedCommandMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receiveReadCancelsMessages:" %}{% endlanying_code_snippet %}
```
### receivedCommandMessages:

Command received

`- (void)receivedCommandMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
Command received

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receivedDeliverAcks:" title="receivedDeliverAcks:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedCommandMessages:" %}{% endlanying_code_snippet %}
```
### receivedDeliverAcks:

Acknowledgement of message delivered received

`- (void)receivedDeliverAcks:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
Acknowledgement of message delivered received

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receivedMessages:" title="receivedMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedDeliverAcks:" %}{% endlanying_code_snippet %}
```
### receivedMessages:

Messages received

`- (void)receivedMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
Messages received

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receivedReadAcks:" title="receivedReadAcks:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedMessages:" %}{% endlanying_code_snippet %}
```
### receivedReadAcks:

Read acknowledgement of messages received

`- (void)receivedReadAcks:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
Read acknowledgement of messages received

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receivedRecallMessages:" title="receivedRecallMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedReadAcks:" %}{% endlanying_code_snippet %}
```
### receivedRecallMessages:

Canceled messages received

`- (void)receivedRecallMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
Canceled messages received

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/receivedSystemMessages:" title="receivedSystemMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedRecallMessages:" %}{% endlanying_code_snippet %}
```
### receivedSystemMessages:

System notification messages received

`- (void)receivedSystemMessages:(NSArray<BMXMessageObject*> *)*messages*`

#### Discussion
System notification messages received

#### Declared In
* `BMXChatServiceProtocol.h`

<a name="//api/name/retrieveHistoryMessagesConversation:" title="retrieveHistoryMessagesConversation:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedSystemMessages:" %}{% endlanying_code_snippet %}
```
### retrieveHistoryMessagesConversation:

Pull message history

`- (void)retrieveHistoryMessagesConversation:(BMXConversation *)*conversation*`

#### Discussion
Pull message history

#### Declared In
* `BMXChatServiceProtocol.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="retrieveHistoryMessagesConversation:" %}{% endlanying_code_snippet %}
```
