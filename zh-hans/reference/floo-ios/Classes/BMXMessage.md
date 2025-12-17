# BMXMessage Class Reference

**Inherits from** [BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 消息

## Class Methods

### createCommandMessageWithFrom:to:type:conversationId:content:

创建发送命令消息(命令消息通过content字段或者extension字段存放命令信息)

`+ (BMXMessage *)createCommandMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content*`

#### Parameters

_from_\
消息发送者

_to_\
消息接收者

_type_\
消息类型

_conversationId_\
会话id

_content_\
消息内容

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createCommandMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:

创建收到的命令消息(命令消息通过content字段或者extension字段存放命令信息)

`+ (BMXMessage *)createCommandMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

_msgId_\
消息id

_from_\
消息发送者

_to_\
消息接收者

_type_\
消息类型

_conversationId_\
会话id

_content_\
消息内容

_serverTimestamp_\
服务器时间戳

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createForwardMessageWithMsg:from:to:type:conversationId:

创建转发消息

`+ (BMXMessage *)createForwardMessageWithMsg:(BMXMessage *)*msg* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId*`

#### Parameters

_msg_\
要转发的消息

_from_\
消息发送者

_to_\
消息接收者

_type_\
消息类型

_conversationId_\
会话id

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createMessageWithFrom:to:type:conversationId:attachment:

创建发送附件消息

`+ (BMXMessage *)createMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* attachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

_from_\
消息发送者

_to_\
消息接收者

_type_\
消息类型

_conversationId_\
会话id

_attachment_\
附件

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createMessageWithFrom:to:type:conversationId:content:

创建发送文本消息

`+ (BMXMessage *)createMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content*`

#### Parameters

_from_\
消息发送者

_to_\
消息接收者

_type_\
消息类型

_conversationId_\
会话id

_content_\
消息内容

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createMessageWithMsgId:from:to:type:conversationId:attachment:serverTimestamp:

创建收到的消息

`+ (BMXMessage *)createMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* attachment:(BMXMessageAttachment *)*attachment* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

_msgId_\
消息id

_from_\
消息发送者

_to_\
消息接收者

_type_\
消息类型

_conversationId_\
会话id

_attachment_\
附件

_serverTimestamp_\
服务器时间戳

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:

创建收到的消息

`+ (BMXMessage *)createMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

_msgId_\
消息id

_from_\
消息发送者

_to_\
消息接收者

_type_\
消息类型

_conversationId_\
会话id

_content_\
消息内容

_serverTimestamp_\
服务器时间戳

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createRTCMessageWithFrom:to:type:conversationId:content:

创建发送RTC消息

`+ (BMXMessage *)createRTCMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content*`

#### Parameters

_from_\
消息发送者

_to_\
消息接收者

_type_\
消息类型

_conversationId_\
会话id

_content_\
消息内容

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### createRTCMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:

创建收到的RTC消息

`+ (BMXMessage *)createRTCMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

_msgId_\
消息id

_from_\
消息发送者

_to_\
消息接收者

_type_\
消息类型

_conversationId_\
会话id

_content_\
消息内容

_serverTimestamp_\
服务器时间戳

#### Declared In

* `floo_proxy.h`

## Instance Methods

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### attachment

消息附件，BMXMessage拥有附件的所有权，负责释放

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

消息客户端ID,仅在消息发送端存在

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

本地时间戳（消息创建或者收到时的本地时间）

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

消息的配置信息

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

消息文本内容

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

消息内容类型，如果带附件就表示附件类型，不带附件就是文本类型

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

消息所属会话ID

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

消息投递QOS

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

消息投递状态

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

消息扩展信息

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

消息发送方ID

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

群消息已读AckCount数目

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

群消息是否全部已读

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

群消息未读AckCount数目

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

群消息已播放AckCount数目（仅用于音频/视频附件消息）

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

群消息是否全部已播放

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

群消息未播放AckCount数目（仅用于音频/视频附件消息）

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

对于发送方表示消息是否已投递到对方，对于接收方表示是否发送了消息已到达回执

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

对于发送方表示是否收到了已播放回执，对于接收方表示是否发送了已播放回执

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

语音或者视频消息是否播放过，仅对收到的音视频消息有效

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

消息是否是推送消息

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

消息是否已读标志

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

对于发送方表示是否收到了已读回执，对于接收方表示是否发送了已读回执

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

是否接收的消息

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

消息唯一ID

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

消息的扩散优先级

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

消息发送者的显示名称

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

消息时间戳（服务端收到时的时间）

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

设置消息本地时间戳

`- (void)setClientTimestamp:(long long)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setConfig:

设置消息配置信息

`- (void)setConfig:(BMXMessageConfig *)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setContent:

消息文本内容

`- (void)setContent:(NSString *)*content*`

#### Parameters

_content_\
消息文本内容

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setDeliveryQos:

设置消息投递QOS

`- (void)setDeliveryQos:(BMXMessage_DeliveryQos)*qos*`

#### Parameters

_qos_\
消息投递QOS

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setDeliveryStatus:

设置消息投递状态

`- (void)setDeliveryStatus:(BMXMessage_DeliveryStatus)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setExtension:

设置消息扩展信息

`- (void)setExtension:(NSString *)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setGroupAckCount:

设置消息已读groupAckCount数目(SDK 内部调用接口，上层不应该调用)

`- (void)setGroupAckCount:(int)*count*`

#### Parameters

_count_\
设置群消息已读数目

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setGroupAckUnreadCount:

设置消息未读groupAckCount数目(SDK 内部调用接口，上层不应该调用)

`- (void)setGroupAckUnreadCount:(int)*count*`

#### Parameters

_count_\
设置群消息未读数目

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setGroupPlayAckCount:

设置消息已播放groupAckCount数目(SDK 内部调用接口，上层不应该调用)（仅用于音频/视频附件消息）

`- (void)setGroupPlayAckCount:(int)*count*`

#### Parameters

_count_\
设置群消息已读数目

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setGroupPlayAckUnreadCount:

设置消息未播放groupAckCount数目(SDK 内部调用接口，上层不应该调用)（仅用于音频/视频附件消息）

`- (void)setGroupPlayAckUnreadCount:(int)*count*`

#### Parameters

_count_\
设置群消息未播放数目

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setIsDeliveryAcked:

设置投递回执

`- (void)setIsDeliveryAcked:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setIsPlayAcked:

设置已播放回执

`- (void)setIsPlayAcked:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setIsPlayed:

设置语音或者视频消息是否播放过，仅对收到的音视频消息有效

`- (void)setIsPlayed:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setIsRead:

消息是否已读标志

`- (void)setIsRead:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setIsReadAcked:

设置已读回执

`- (void)setIsReadAcked:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setIsReceiveMsg:

设置是否接收的消息

`- (void)setIsReceiveMsg:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setPriority:

取值范围0-10。普通人在聊天室发送的消息级别默认为5，可以丢弃。管理员默认为0不会丢弃。其它值可以根据业务自行设置。

`- (void)setPriority:(int)*priority*`

#### Parameters

_priority_\
优先级

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setPushMessageMode:

设置消息是否为推送消息。

`- (void)setPushMessageMode:(BOOL)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setSenderName:

设置消息的发送者显示名称

`- (void)setSenderName:(NSString *)*senderName*`

#### Parameters

_senderName_\
消息文本内容

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### setServerTimestamp:

设置时间戳（服务端收到时的时间）

`- (void)setServerTimestamp:(long long)*arg1*`

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>

```

### toId

消息接收方ID

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

消息类型

`- (BMXMessage_MessageType)type`

#### Return Value

[BMXMessage\_MessageType](../Constants/BMXMessage_MessageType.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXMessage'></div>
```
