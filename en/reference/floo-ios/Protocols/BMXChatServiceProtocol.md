# BMXChatServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@protocol Chat service listener

## Instance Methods

<a name="//api/name/conversationDidCreatedConversation:message:" title="conversationDidCreatedConversation:message:"></a>
### conversationDidCreatedConversation:message:

Conversation created

`- (void)conversationDidCreatedConversation:(BMXConversation *)*conversation* message:(BMXMessage *)*message*`

#### Parameters

*conversation*  

*message*  

    The latest message

#### Declared In
* `floo_proxy.h`

<a name="//api/name/conversationDidDeletedConversationId:error:" title="conversationDidDeletedConversationId:error:"></a>
### conversationDidDeletedConversationId:error:

Conversation deleted

`- (void)conversationDidDeletedConversationId:(NSInteger)*conversationId* error:(BMXError *)*error*`

#### Parameters

*conversationId*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/conversationTotalCountChanged:" title="conversationTotalCountChanged:"></a>
### conversationTotalCountChanged:

Conversation unread message count changed

`- (void)conversationTotalCountChanged:(NSInteger)*unreadCount*`

#### Parameters

*unreadCount*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/loadAllConversationDidFinished" title="loadAllConversationDidFinished"></a>
### loadAllConversationDidFinished

All conversations loaded

`- (void)loadAllConversationDidFinished`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageAttachmentStatusDidChanged:error:percent:" title="messageAttachmentStatusDidChanged:error:percent:"></a>
### messageAttachmentStatusDidChanged:error:percent:

Message attachment download status changed

`- (void)messageAttachmentStatusDidChanged:(BMXMessage *)*message* error:(BMXError *)*error* percent:(int)*percent*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageAttachmentUploadProgressChanged:percent:" title="messageAttachmentUploadProgressChanged:percent:"></a>
### messageAttachmentUploadProgressChanged:percent:

Message attachment upload status changed

`- (void)messageAttachmentUploadProgressChanged:(BMXMessage *)*message* percent:(int)*percent*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageRecallStatusDidChanged:error:" title="messageRecallStatusDidChanged:error:"></a>
### messageRecallStatusDidChanged:error:

Message recall status changed

`- (void)messageRecallStatusDidChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageStatusChanged:error:" title="messageStatusChanged:error:"></a>
### messageStatusChanged:error:

Message sending status changed

`- (void)messageStatusChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receiveDeleteMessages:" title="receiveDeleteMessages:"></a>
### receiveDeleteMessages:

Receive messages deleted

`- (void)receiveDeleteMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receiveReadAllMessages:" title="receiveReadAllMessages:"></a>
### receiveReadAllMessages:

Receive all messages have been read

`- (void)receiveReadAllMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receiveReadCancelsMessages:" title="receiveReadCancelsMessages:"></a>
### receiveReadCancelsMessages:

Receive messages have been set as unread

`- (void)receiveReadCancelsMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedCommandMessages:" title="receivedCommandMessages:"></a>
### receivedCommandMessages:

Receive command messages

`- (void)receivedCommandMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedDeliverAcks:" title="receivedDeliverAcks:"></a>
### receivedDeliverAcks:

Recieve delivery ACKs

`- (void)receivedDeliverAcks:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedMessages:" title="receivedMessages:"></a>
### receivedMessages:

Receive messages

`- (void)receivedMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedReadAcks:" title="receivedReadAcks:"></a>
### receivedReadAcks:

Receive read ACKs

`- (void)receivedReadAcks:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedRecallMessages:" title="receivedRecallMessages:"></a>
### receivedRecallMessages:

Receive recalled messages

`- (void)receivedRecallMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedSystemMessages:" title="receivedSystemMessages:"></a>
### receivedSystemMessages:

Receive system messages

`- (void)receivedSystemMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/retrieveHistoryMessagesConversation:" title="retrieveHistoryMessagesConversation:"></a>
### retrieveHistoryMessagesConversation:

Retrieve history messages of a conversation

`- (void)retrieveHistoryMessagesConversation:(BMXConversation *)*conversation*`

#### Discussion

#### Declared In
* `floo_proxy.h`

