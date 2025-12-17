# BMXMessage Class Reference

**Inherits from** [BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface Message

## Class Methods

### createCommandMessageWithFrom:to:type:conversationId:content:

Create a COMMAND message to send

`+ (BMXMessage *)createCommandMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content*`

#### Parameters

_from_\
Message sender

_to_\
Message receiver

_type_\
Message type

_conversationId_\
Conversation ID

_content_\
Message content

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createCommandMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:

Create a COMMAND message received

`+ (BMXMessage *)createCommandMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

_msgId_\
Message ID

_from_\
Message sender

_to_\
Message receiver

_type_\
Message type

_conversationId_\
Conversation ID

_content_\
Message content

_serverTimestamp_\
Message timestamp on server

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createForwardMessageWithMsg:from:to:type:conversationId:

Create a message to forward

`+ (BMXMessage *)createForwardMessageWithMsg:(BMXMessage *)*msg* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId*`

#### Parameters

_msg_\
Message to be forward

_from_\
Message sender

_to_\
Message receiver

_type_\
Message type

_conversationId_\
Conversation ID

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createMessageWithFrom:to:type:conversationId:attachment:

Create a message with an attachment

`+ (BMXMessage *)createMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* attachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

_from_\
Message sender

_to_\
Message receiver

_type_\
Message type

_conversationId_\
Conversation ID

_attachment_\
The attachment

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createMessageWithFrom:to:type:conversationId:content:

Create a text message

`+ (BMXMessage *)createMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content*`

#### Parameters

_from_\
Message sender

_to_\
Message receiver

_type_\
Message type

_conversationId_\
Conversation ID

_content_\
Message content

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createMessageWithMsgId:from:to:type:conversationId:attachment:serverTimestamp:

Create a received message

`+ (BMXMessage *)createMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* attachment:(BMXMessageAttachment *)*attachment* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

_msgId_\
Message ID

_from_\
Message sender

_to_\
Message receiver

_type_\
Message type

_conversationId_\
Conversation ID

_attachment_\
The attachment

_serverTimestamp_\
Message timestamp on server

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:

Create a received message

`+ (BMXMessage *)createMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

_msgId_\
Message ID

_from_\
Message sender

_to_\
Message receiver

_type_\
Message type

_conversationId_\
Conversation ID

_content_\
Messsage content

_serverTimestamp_\
Message timestamp on server

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createRTCMessageWithFrom:to:type:conversationId:content:

Create an RTC Messsage

`+ (BMXMessage *)createRTCMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content*`

#### Parameters

_from_\
Message sender

_to_\
Message receiver

_type_\
Message type

_conversationId_\
Conversation ID

_content_\
Messsage content

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createRTCMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:

Create an RTC message received

`+ (BMXMessage *)createRTCMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

_msgId_\
Message ID

_from_\
Message sender

_to_\
Message receiver

_type_\
Message type

_conversationId_\
Conversation ID

_content_\
Messsage content

_serverTimestamp_\
Message timestamp on server

#### Declared In

* `floo_proxy.h`

## Instance Methods

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### attachment

Message attachment

`- (BMXMessageAttachment *)attachment`

#### Return Value

[BMXMessageAttachment](BMXMessageAttachment.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### clientMsgId

Client ID of Messsage

`- (long long)clientMsgId`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### clientTimestamp

Local timestamp

`- (long long)clientTimestamp`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### config

Message config

`- (BMXMessageConfig *)config`

#### Return Value

[BMXMessageConfig](BMXMessageConfig.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### content

Text content of the message

`- (NSString *)content`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### contentType

Message content type

`- (BMXMessage_ContentType)contentType`

#### Return Value

ContentType

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### conversationId

Conversation ID

`- (long long)conversationId`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### deliveryQos

Delivery QOS of message

`- (BMXMessage_DeliveryQos)deliveryQos`

#### Return Value

[BMXMessage\_DeliveryQos](../Constants/BMXMessage_DeliveryQos.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### deliveryStatus

Message delivery status

`- (BMXMessage_DeliveryStatus)deliveryStatus`

#### Return Value

[BMXMessage\_DeliveryStatus](../Constants/BMXMessage_DeliveryStatus.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### extension

Extension information of message

`- (NSString *)extension`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### fromId

Sender ID

`- (long long)fromId`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### groupAckCount

The number of users who have read the group message

`- (int)groupAckCount`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### groupAckReadAll

Whether the group message has been read by everyone

`- (BOOL)groupAckReadAll`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### groupAckUnreadCount

The number of users who have NOT read the group message

`- (int)groupAckUnreadCount`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### groupPlayAckCount

The number of users who have played the group message

`- (int)groupPlayAckCount`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### groupPlayAckReadAll

Whether the group message has been played by everyone

`- (BOOL)groupPlayAckReadAll`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### groupPlayAckUnreadCount

The number of users who have NOT played the group message

`- (int)groupPlayAckUnreadCount`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### isDeliveryAcked

For the sender, it indicates whether the message has been delivered to the receiver, and for the receiver, it indicates whether the read ACK has been sent.

`- (BOOL)isDeliveryAcked`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### isPlayAcked

For the sender, it indicates whether the message has been played by the receiver, and for the receiver, it indicates whether the play ACK has been sent.

`- (BOOL)isPlayAcked`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### isPlayed

Whether the message has been played

`- (BOOL)isPlayed`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### isPushMessage

Is it a push message

`- (BOOL)isPushMessage`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### isRead

Whether the message has been read

`- (BOOL)isRead`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### isReadAcked

For the sender, it indicates whether the message has been read by the receiver, and for the receiver, it indicates whether the read ACK has been sent.

`- (BOOL)isReadAcked`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### isReceiveMsg

Is it a received message

`- (BOOL)isReceiveMsg`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### msgId

Message ID

`- (long long)msgId`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### priority

Message Diffusion Priority

`- (int)priority`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### senderName

Sender name

`- (NSString *)senderName`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### serverTimestamp

```
Message timestamp on server
```

`- (long long)serverTimestamp`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setClientTimestamp:

```
Set local timestamp of the message
```

`- (void)setClientTimestamp:(long long)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setConfig:

Set message config

`- (void)setConfig:(BMXMessageConfig *)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setContent:

Set message content

`- (void)setContent:(NSString *)*content*`

#### Parameters

_content_\
Text content

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setDeliveryQos:

Set delivery QOS

`- (void)setDeliveryQos:(BMXMessage_DeliveryQos)*qos*`

#### Parameters

_qos_\
Delivery QOS

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setDeliveryStatus:

Set delivery status

`- (void)setDeliveryStatus:(BMXMessage_DeliveryStatus)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setExtension:

Set extension information

`- (void)setExtension:(NSString *)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setIsDeliveryAcked:

Set delivery ACK sent or received

`- (void)setIsDeliveryAcked:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setIsPlayAcked:

Set play ACK sent or received

`- (void)setIsPlayAcked:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setIsPlayed:

Set play ACK sent or received

`- (void)setIsPlayed:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setIsRead:

Set the message has been read

`- (void)setIsRead:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setIsReadAcked:

Set read ACK sent or received

`- (void)setIsReadAcked:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setIsReceiveMsg:

Set it as a received message

`- (void)setIsReceiveMsg:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setPriority:

\[0-10]. The priority of messages sent by members in the chat room is 5 by default, and messages can be discarded. For administrators, the priority defaults to 0, and messages are not dropped. Other values can be set as required

`- (void)setPriority:(int)*priority*`

#### Parameters

_priority_\
Priority value

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setPushMessageMode:

Set it as a push message

`- (void)setPushMessageMode:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setSenderName:

Set sender name

`- (void)setSenderName:(NSString *)*senderName*`

#### Parameters

_senderName_\
Sender name

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setServerTimestamp:

Set the server-side timestamp of the message

`- (void)setServerTimestamp:(long long)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### toId

Receiver ID

`- (long long)toId`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### type

Message type

`- (BMXMessage_MessageType)type`

#### Return Value

[BMXMessage\_MessageType](../Constants/BMXMessage_MessageType.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>
```
