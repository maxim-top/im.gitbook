# BMXChatServiceProtocol Protocol Reference

**Conforms to** NSObject\
**Declared in** floo\_proxy.h

## Overview

@protocol Chat service listener

## Instance Methods

### conversationDidCreatedConversation:message:

Conversation created

`- (void)conversationDidCreatedConversation:(BMXConversation *)*conversation* message:(BMXMessage *)*message*`

#### Parameters

_conversation_

_message_

```
The latest message
```

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### conversationDidDeletedConversationId:error:

Conversation deleted

`- (void)conversationDidDeletedConversationId:(NSInteger)*conversationId* error:(BMXError *)*error*`

#### Parameters

_conversationId_

_error_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### conversationTotalCountChanged:

Conversation unread message count changed

`- (void)conversationTotalCountChanged:(NSInteger)*unreadCount*`

#### Parameters

_unreadCount_

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### loadAllConversationDidFinished

All conversations loaded

`- (void)loadAllConversationDidFinished`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### messageAttachmentStatusDidChanged:error:percent:

Message attachment download status changed

`- (void)messageAttachmentStatusDidChanged:(BMXMessage *)*message* error:(BMXError *)*error* percent:(int)*percent*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### messageAttachmentUploadProgressChanged:percent:

Message attachment upload status changed

`- (void)messageAttachmentUploadProgressChanged:(BMXMessage *)*message* percent:(int)*percent*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### messageRecallStatusDidChanged:error:

Message recall status changed

`- (void)messageRecallStatusDidChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### messageStatusChanged:error:

Message sending status changed

`- (void)messageStatusChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### receiveDeleteMessages:

Receive messages deleted

`- (void)receiveDeleteMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### receiveReadAllMessages:

Receive all messages have been read

`- (void)receiveReadAllMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### receiveReadCancelsMessages:

Receive messages have been set as unread

`- (void)receiveReadCancelsMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### receivedCommandMessages:

Receive command messages

`- (void)receivedCommandMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### receivedDeliverAcks:

Recieve delivery ACKs

`- (void)receivedDeliverAcks:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### receivedMessages:

Receive messages

`- (void)receivedMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### receivedReadAcks:

Receive read ACKs

`- (void)receivedReadAcks:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### receivedRecallMessages:

Receive recalled messages

`- (void)receivedRecallMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### receivedSystemMessages:

Receive system messages

`- (void)receivedSystemMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>

```

### retrieveHistoryMessagesConversation:

Retrieve history messages of a conversation

`- (void)retrieveHistoryMessagesConversation:(BMXConversation *)*conversation*`

#### Discussion

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatServiceProtocol'></div>
```
