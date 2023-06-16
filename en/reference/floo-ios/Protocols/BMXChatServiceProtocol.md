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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="conversationDidCreatedConversation:message:" %}{% endlanying_code_snippet %}
```
### conversationDidDeletedConversationId:error:

Conversation deleted

`- (void)conversationDidDeletedConversationId:(NSInteger)*conversationId* error:(BMXError *)*error*`

#### Parameters

*conversationId*  

*error*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/conversationTotalCountChanged:" title="conversationTotalCountChanged:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="conversationDidDeletedConversationId:error:" %}{% endlanying_code_snippet %}
```
### conversationTotalCountChanged:

Conversation unread message count changed

`- (void)conversationTotalCountChanged:(NSInteger)*unreadCount*`

#### Parameters

*unreadCount*  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/loadAllConversationDidFinished" title="loadAllConversationDidFinished"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="conversationTotalCountChanged:" %}{% endlanying_code_snippet %}
```
### loadAllConversationDidFinished

All conversations loaded

`- (void)loadAllConversationDidFinished`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageAttachmentStatusDidChanged:error:percent:" title="messageAttachmentStatusDidChanged:error:percent:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="loadAllConversationDidFinished" %}{% endlanying_code_snippet %}
```
### messageAttachmentStatusDidChanged:error:percent:

Message attachment download status changed

`- (void)messageAttachmentStatusDidChanged:(BMXMessage *)*message* error:(BMXError *)*error* percent:(int)*percent*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageAttachmentUploadProgressChanged:percent:" title="messageAttachmentUploadProgressChanged:percent:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="messageAttachmentStatusDidChanged:error:percent:" %}{% endlanying_code_snippet %}
```
### messageAttachmentUploadProgressChanged:percent:

Message attachment upload status changed

`- (void)messageAttachmentUploadProgressChanged:(BMXMessage *)*message* percent:(int)*percent*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageRecallStatusDidChanged:error:" title="messageRecallStatusDidChanged:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="messageAttachmentUploadProgressChanged:percent:" %}{% endlanying_code_snippet %}
```
### messageRecallStatusDidChanged:error:

Message recall status changed

`- (void)messageRecallStatusDidChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageStatusChanged:error:" title="messageStatusChanged:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="messageRecallStatusDidChanged:error:" %}{% endlanying_code_snippet %}
```
### messageStatusChanged:error:

Message sending status changed

`- (void)messageStatusChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receiveDeleteMessages:" title="receiveDeleteMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="messageStatusChanged:error:" %}{% endlanying_code_snippet %}
```
### receiveDeleteMessages:

Receive messages deleted

`- (void)receiveDeleteMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receiveReadAllMessages:" title="receiveReadAllMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receiveDeleteMessages:" %}{% endlanying_code_snippet %}
```
### receiveReadAllMessages:

Receive all messages have been read

`- (void)receiveReadAllMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receiveReadCancelsMessages:" title="receiveReadCancelsMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receiveReadAllMessages:" %}{% endlanying_code_snippet %}
```
### receiveReadCancelsMessages:

Receive messages have been set as unread

`- (void)receiveReadCancelsMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedCommandMessages:" title="receivedCommandMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receiveReadCancelsMessages:" %}{% endlanying_code_snippet %}
```
### receivedCommandMessages:

Receive command messages

`- (void)receivedCommandMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedDeliverAcks:" title="receivedDeliverAcks:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedCommandMessages:" %}{% endlanying_code_snippet %}
```
### receivedDeliverAcks:

Recieve delivery ACKs

`- (void)receivedDeliverAcks:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedMessages:" title="receivedMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedDeliverAcks:" %}{% endlanying_code_snippet %}
```
### receivedMessages:

Receive messages

`- (void)receivedMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedReadAcks:" title="receivedReadAcks:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedMessages:" %}{% endlanying_code_snippet %}
```
### receivedReadAcks:

Receive read ACKs

`- (void)receivedReadAcks:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedRecallMessages:" title="receivedRecallMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedReadAcks:" %}{% endlanying_code_snippet %}
```
### receivedRecallMessages:

Receive recalled messages

`- (void)receivedRecallMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedSystemMessages:" title="receivedSystemMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedRecallMessages:" %}{% endlanying_code_snippet %}
```
### receivedSystemMessages:

Receive system messages

`- (void)receivedSystemMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In
* `floo_proxy.h`

<a name="//api/name/retrieveHistoryMessagesConversation:" title="retrieveHistoryMessagesConversation:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedSystemMessages:" %}{% endlanying_code_snippet %}
```
### retrieveHistoryMessagesConversation:

Retrieve history messages of a conversation

`- (void)retrieveHistoryMessagesConversation:(BMXConversation *)*conversation*`

#### Discussion

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="retrieveHistoryMessagesConversation:" %}{% endlanying_code_snippet %}
```
