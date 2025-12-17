# BMXConversation Class Reference

**Inherits from** [BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface Conversation

## Instance Methods

### conversationId

Conversation ID

`- (long long)conversationId`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### editMessage

Edit a message

`- (NSString *)editMessage`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### extension

Extension information of a message

`- (NSString *)extension`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### insertMessageWithMsg:

Insert a message

`- (BMXErrorCode)insertMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
The message

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### insertMessageWithMsg:completion:

Insert a message

`- (void)insertMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### isMuteNotification

Turn off message notifications

`- (BOOL)isMuteNotification`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### lastMsg

The last message

`- (BMXMessage *)lastMsg`

#### Return Value

[BMXMessage](BMXMessage.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### loadMessageWithMsgId:

Get a message by ID

`- (BMXMessage *)loadMessageWithMsgId:(long long)*msgId*`

#### Parameters

_msgId_\
The message ID

#### Return Value

[BMXMessage](BMXMessage.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### loadMessageWithMsgId:completion:

Get a message by ID

`- (void)loadMessageWithMsgId:(long long)*msgId* completion:(void ( ^ ) ( BMXMessage *res , BMXError *aError ))*resBlock*`

#### Parameters

_msgId_\
The message ID

#### Return Value

[BMXMessage](BMXMessage.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### loadMessagesWithRefMsgId:size:arg4:completion:

Get messages from the starting message ID

`- (void)loadMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* arg4:(BMXConversation_Direction)*arg4* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

#### Parameters

_refMsgId_\
Starting message ID

_size_\
Maximum number of messages

_result_\
Message list as result

_Direction_\
Search direction, Up for earlier

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='4' data-2='4' data-3='4' data-4='4' data-5='4' data-6='4' data-7='4' data-8='4' data-9='4' data-10='4' data-11='4' data-12='4' data-13='4' data-14='4' data-15='4' data-16='4' data-17='4' data-18='4' data-19='4' data-20='4' data-21='4' data-22='4' data-23='4' data-24='4' data-25='4' data-26='4' data-27='4' data-28='4' data-29='4' data-30='4' data-31='4' data-32='4' data-33='4' data-34='4' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### loadMessagesWithRefMsgId:size:completion:

Search messages by message ID

`- (void)loadMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

#### Parameters

_size_\
Maximum number of messages

_refTime_\
Starting time

_result_\
Message list as result

_keywords_\
The keywords

_Direction_\
Search direction, Up for earlier

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### loadMessagesWithRefMsgId:size:result:

`- (BMXErrorCode)loadMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### loadMessagesWithRefMsgId:size:result:arg4:

Load messages

`- (BMXErrorCode)loadMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result* arg4:(BMXConversation_Direction)*arg4*`

#### Parameters

_refMsgId_\
First Message Id

_size_\
Maximum number of messages

_result_\
Message list as result

_Direction_\
Search direction, Up for earlier

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='4' data-2='4' data-3='4' data-4='4' data-5='4' data-6='4' data-7='4' data-8='4' data-9='4' data-10='4' data-11='4' data-12='4' data-13='4' data-14='4' data-15='4' data-16='4' data-17='4' data-18='4' data-19='4' data-20='4' data-21='4' data-22='4' data-23='4' data-24='4' data-25='4' data-26='4' data-27='4' data-28='4' data-29='4' data-30='4' data-31='4' data-32='4' data-33='4' data-34='4' data-35='4' data-36='4' data-37='4' data-38='4' data-39='4' data-40='4' data-41='4' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### messageCount

The number of messages

`- (int)messageCount`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### refreshConversation

Force update the total number of messages and unread messages for the conversation

`- (BMXErrorCode)refreshConversation`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### refreshConversationWithCompletion:

Force update the total number of messages and unread messages for the conversation

`- (void)refreshConversationWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### removeAllMessages

Remove all messages in the conversation

`- (BMXErrorCode)removeAllMessages`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### removeAllMessagesWithCompletion:

Remove all messages in the conversation

`- (void)removeAllMessagesWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:

Search messages by keywords

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* arg5:(BMXConversation_Direction)*arg5* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

#### Parameters

_keywords_\
The keywords

_refTime_\
Starting time

_size_\
Maximum number of messages

_result_\
Message list as result

_Direction_\
Search direction, Up for earlier

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Discussion

Deprecated. use searchMessagesByKeyWords instead.

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-54='5' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:completion:

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:result:

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:

Search messages by keywords

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageList *)*result* arg5:(BMXConversation_Direction)*arg5*`

#### Parameters

_keywords_\
The keywords

_refTime_\
Starting time

_size_\
Maximum number of messages

_result_\
Message list as result

_arg5_\
Search direction, Up for earlier

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-54='5' data-55='5' data-56='5' data-57='5' data-58='5' data-59='5' data-60='5' data-61='5' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByTypeWithType:refTime:size:arg5:completion:

Search messages by type

`- (void)searchMessagesByTypeWithType:(BMXMessage_ContentType)*type* refTime:(long long)*refTime* size:(unsigned long)*size* arg5:(BMXConversation_Direction)*arg5* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

#### Parameters

_type_\
The type

_refTime_\
Starting time

_size_\
Maximum number of messages

_result_\
Message list as result

_Direction_\
Search direction, Up for earlier

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByTypeWithType:refTime:size:completion:

`- (void)searchMessagesByTypeWithType:(BMXMessage_ContentType)*type* refTime:(long long)*refTime* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByTypeWithType:refTime:size:result:

`- (BMXErrorCode)searchMessagesByTypeWithType:(BMXMessage_ContentType)*type* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByTypeWithType:refTime:size:result:arg5:

Search messages by type

`- (BMXErrorCode)searchMessagesByTypeWithType:(BMXMessage_ContentType)*type* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageList *)*result* arg5:(BMXConversation_Direction)*arg5*`

#### Parameters

_type_\
The type

_refTime_\
Starting time

_size_\
Maximum number of messages

_result_\
Message list as result

_Direction_\
Search direction, Up for earlier

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setAllMessagesRead

Set all messages as read

`- (BMXErrorCode)setAllMessagesRead`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setAllMessagesReadWithCompletion:

Set all messages as read

`- (void)setAllMessagesReadWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setEditMessage:

Set message in editting

`- (BMXErrorCode)setEditMessage:(NSString *)*editMessage*`

#### Parameters

_editMessage_\
The message content

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setExtension:

Set extension information of messages

`- (BMXErrorCode)setExtension:(NSString *)*ext*`

#### Parameters

_ext_\
The extension information

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setMessagePlayedStatus:status:

Set palyed status of messages

`- (BMXErrorCode)setMessagePlayedStatus:(BMXMessage *)*msg* status:(BOOL)*status*`

#### Parameters

_msg_\
The message

_status_\
Played or not

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setMessagePlayedStatus:status:completion:

Set the palyed status of messages

`- (void)setMessagePlayedStatus:(BMXMessage *)*msg* status:(BOOL)*status* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

_status_\
Played or not

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setMessageReadStatus:status:

Set the read status of messages

`- (BMXErrorCode)setMessageReadStatus:(BMXMessage *)*msg* status:(BOOL)*status*`

#### Parameters

_msg_\
The message

_status_\
Read or not

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setMessageReadStatus:status:completion:

Set the read status of messages

`- (void)setMessageReadStatus:(BMXMessage *)*msg* status:(BOOL)*status* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

_status_\
Read or not

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### type

Conversation type

`- (BMXConversation_Type)type`

#### Return Value

[BMXConversation\_Type](../Constants/BMXConversation_Type.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### unreadNumber

THe number of unread messages

`- (int)unreadNumber`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### updateMessageExtensionWithMsg:

Update the extension information of a message

`- (BMXErrorCode)updateMessageExtensionWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
The message

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### updateMessageExtensionWithMsg:completion:

Update the extension information of a message

`- (void)updateMessageExtensionWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>
```
