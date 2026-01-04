# BMXMessage Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Message

## Class Methods

<a name="//api/name/createCommandMessageWithFrom:to:type:conversationId:content:" title="createCommandMessageWithFrom:to:type:conversationId:content:"></a>
### createCommandMessageWithFrom:to:type:conversationId:content:

Create a COMMAND message to send

`+ (BMXMessage *)createCommandMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content*`

#### Parameters

*from*  
    Message sender 

*to*  
    Message receiver

*type*  
    Message type

*conversationId*  
    Conversation ID

*content*  
    Message content

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createCommandMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:" title="createCommandMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="createCommandMessageWithFrom:to:type:conversationId:content:" %}{% endlanying_code_snippet %}
```
### createCommandMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:

Create a COMMAND message received

`+ (BMXMessage *)createCommandMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

*msgId*  
    Message ID

*from*  
    Message sender 

*to*  
    Message receiver

*type*  
    Message type

*conversationId*  
    Conversation ID

*content*  
    Message content

*serverTimestamp*  
    Message timestamp on server

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createForwardMessageWithMsg:from:to:type:conversationId:" title="createForwardMessageWithMsg:from:to:type:conversationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="createCommandMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:" %}{% endlanying_code_snippet %}
```
### createForwardMessageWithMsg:from:to:type:conversationId:

Create a message to forward

`+ (BMXMessage *)createForwardMessageWithMsg:(BMXMessage *)*msg* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId*`

#### Parameters

*msg*  
    Message to be forward

*from*  
    Message sender 

*to*  
    Message receiver

*type*  
    Message type

*conversationId*  
    Conversation ID

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createMessageWithFrom:to:type:conversationId:attachment:" title="createMessageWithFrom:to:type:conversationId:attachment:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="createForwardMessageWithMsg:from:to:type:conversationId:" %}{% endlanying_code_snippet %}
```
### createMessageWithFrom:to:type:conversationId:attachment:

Create a message with an attachment

`+ (BMXMessage *)createMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* attachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

*from*  
    Message sender 

*to*  
    Message receiver

*type*  
    Message type

*conversationId*  
    Conversation ID

*attachment*  
    The attachment

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createMessageWithFrom:to:type:conversationId:content:" title="createMessageWithFrom:to:type:conversationId:content:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="createMessageWithFrom:to:type:conversationId:attachment:" %}{% endlanying_code_snippet %}
```
### createMessageWithFrom:to:type:conversationId:content:

Create a text message

`+ (BMXMessage *)createMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content*`

#### Parameters

*from*  
    Message sender 

*to*  
    Message receiver

*type*  
    Message type

*conversationId*  
    Conversation ID

*content*  
    Message content

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createMessageWithMsgId:from:to:type:conversationId:attachment:serverTimestamp:" title="createMessageWithMsgId:from:to:type:conversationId:attachment:serverTimestamp:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="createMessageWithFrom:to:type:conversationId:content:" %}{% endlanying_code_snippet %}
```
### createMessageWithMsgId:from:to:type:conversationId:attachment:serverTimestamp:

Create a received message

`+ (BMXMessage *)createMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* attachment:(BMXMessageAttachment *)*attachment* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

*msgId*  
    Message ID

*from*  
    Message sender 

*to*  
    Message receiver

*type*  
    Message type

*conversationId*  
    Conversation ID

*attachment*  
    The attachment

*serverTimestamp*  
    Message timestamp on server

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:" title="createMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="createMessageWithMsgId:from:to:type:conversationId:attachment:serverTimestamp:" %}{% endlanying_code_snippet %}
```
### createMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:

Create a received message

`+ (BMXMessage *)createMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

*msgId*  
    Message ID

*from*  
    Message sender 

*to*  
    Message receiver

*type*  
    Message type

*conversationId*  
    Conversation ID

*content*  
    Messsage content

*serverTimestamp*  
    Message timestamp on server

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createRTCMessageWithFrom:to:type:conversationId:content:" title="createRTCMessageWithFrom:to:type:conversationId:content:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="createMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:" %}{% endlanying_code_snippet %}
```
### createRTCMessageWithFrom:to:type:conversationId:content:

Create an RTC Messsage

`+ (BMXMessage *)createRTCMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content*`

#### Parameters

*from*  
    Message sender 

*to*  
    Message receiver

*type*  
    Message type

*conversationId*  
    Conversation ID

*content*  
    Messsage content

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createRTCMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:" title="createRTCMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="createRTCMessageWithFrom:to:type:conversationId:content:" %}{% endlanying_code_snippet %}
```
### createRTCMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:

Create an RTC message received

`+ (BMXMessage *)createRTCMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

*msgId*  
    Message ID

*from*  
    Message sender 

*to*  
    Message receiver

*type*  
    Message type

*conversationId*  
    Conversation ID

*content*  
    Messsage content

*serverTimestamp*  
    Message timestamp on server

#### Declared In
* `floo_proxy.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/attachment" title="attachment"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="createRTCMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:" %}{% endlanying_code_snippet %}
```
### attachment

Message attachment

`- (BMXMessageAttachment *)attachment`

#### Return Value
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/clientMsgId" title="clientMsgId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="attachment" %}{% endlanying_code_snippet %}
```
### clientMsgId

Client ID of Messsage

`- (long long)clientMsgId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/clientTimestamp" title="clientTimestamp"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="clientMsgId" %}{% endlanying_code_snippet %}
```
### clientTimestamp

Local timestamp

`- (long long)clientTimestamp`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/config" title="config"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="clientTimestamp" %}{% endlanying_code_snippet %}
```
### config

Message config

`- (BMXMessageConfig *)config`

#### Return Value
<a href="../Classes/BMXMessageConfig.md">BMXMessageConfig</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/content" title="content"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="config" %}{% endlanying_code_snippet %}
```
### content

Text content of the message

`- (NSString *)content`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/contentType" title="contentType"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="content" %}{% endlanying_code_snippet %}
```
### contentType

Message content type

`- (BMXMessage_ContentType)contentType`

#### Return Value
ContentType

#### Declared In
* `floo_proxy.h`

<a name="//api/name/conversationId" title="conversationId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="contentType" %}{% endlanying_code_snippet %}
```
### conversationId

Conversation ID

`- (long long)conversationId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="conversationId" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/deliveryQos" title="deliveryQos"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="dealloc" %}{% endlanying_code_snippet %}
```
### deliveryQos

Delivery QOS of message

`- (BMXMessage_DeliveryQos)deliveryQos`

#### Return Value
<a href="../Constants/BMXMessage_DeliveryQos.md">BMXMessage_DeliveryQos</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deliveryStatus" title="deliveryStatus"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="deliveryQos" %}{% endlanying_code_snippet %}
```
### deliveryStatus

Message delivery status

`- (BMXMessage_DeliveryStatus)deliveryStatus`

#### Return Value
<a href="../Constants/BMXMessage_DeliveryStatus.md">BMXMessage_DeliveryStatus</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/extension" title="extension"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="deliveryStatus" %}{% endlanying_code_snippet %}
```
### extension

Extension information of message

`- (NSString *)extension`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fromId" title="fromId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="extension" %}{% endlanying_code_snippet %}
```
### fromId

Sender ID

`- (long long)fromId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupAckCount" title="groupAckCount"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="fromId" %}{% endlanying_code_snippet %}
```
### groupAckCount

The number of users who have read the group message

`- (int)groupAckCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupAckReadAll" title="groupAckReadAll"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="groupAckCount" %}{% endlanying_code_snippet %}
```
### groupAckReadAll

Whether the group message has been read by everyone

`- (BOOL)groupAckReadAll`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupAckUnreadCount" title="groupAckUnreadCount"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="groupAckReadAll" %}{% endlanying_code_snippet %}
```
### groupAckUnreadCount

The number of users who have NOT read the group message

`- (int)groupAckUnreadCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupPlayAckCount" title="groupPlayAckCount"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="groupAckUnreadCount" %}{% endlanying_code_snippet %}
```
### groupPlayAckCount

The number of users who have played the group message

`- (int)groupPlayAckCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupPlayAckReadAll" title="groupPlayAckReadAll"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="groupPlayAckCount" %}{% endlanying_code_snippet %}
```
### groupPlayAckReadAll

Whether the group message has been played by everyone

`- (BOOL)groupPlayAckReadAll`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupPlayAckUnreadCount" title="groupPlayAckUnreadCount"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="groupPlayAckReadAll" %}{% endlanying_code_snippet %}
```
### groupPlayAckUnreadCount

The number of users who have NOT played the group message

`- (int)groupPlayAckUnreadCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isDeliveryAcked" title="isDeliveryAcked"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="groupPlayAckUnreadCount" %}{% endlanying_code_snippet %}
```
### isDeliveryAcked

For the sender, it indicates whether the message has been delivered to the receiver, and for the receiver, it indicates whether the read ACK has been sent.

`- (BOOL)isDeliveryAcked`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isPlayAcked" title="isPlayAcked"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="isDeliveryAcked" %}{% endlanying_code_snippet %}
```
### isPlayAcked

For the sender, it indicates whether the message has been played by the receiver, and for the receiver, it indicates whether the play ACK has been sent.

`- (BOOL)isPlayAcked`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isPlayed" title="isPlayed"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="isPlayAcked" %}{% endlanying_code_snippet %}
```
### isPlayed

Whether the message has been played

`- (BOOL)isPlayed`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isPushMessage" title="isPushMessage"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="isPlayed" %}{% endlanying_code_snippet %}
```
### isPushMessage

Is it a push message

`- (BOOL)isPushMessage`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isRead" title="isRead"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="isPushMessage" %}{% endlanying_code_snippet %}
```
### isRead

Whether the message has been read

`- (BOOL)isRead`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isReadAcked" title="isReadAcked"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="isRead" %}{% endlanying_code_snippet %}
```
### isReadAcked

For the sender, it indicates whether the message has been read by the receiver, and for the receiver, it indicates whether the read ACK has been sent.

`- (BOOL)isReadAcked`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isReceiveMsg" title="isReceiveMsg"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="isReadAcked" %}{% endlanying_code_snippet %}
```
### isReceiveMsg

Is it a received message

`- (BOOL)isReceiveMsg`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/msgId" title="msgId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="isReceiveMsg" %}{% endlanying_code_snippet %}
```
### msgId

Message ID

`- (long long)msgId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/priority" title="priority"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="msgId" %}{% endlanying_code_snippet %}
```
### priority

Message Diffusion Priority

`- (int)priority`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/senderName" title="senderName"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="priority" %}{% endlanying_code_snippet %}
```
### senderName

Sender name

`- (NSString *)senderName`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/serverTimestamp" title="serverTimestamp"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="senderName" %}{% endlanying_code_snippet %}
```
### serverTimestamp

    Message timestamp on server

`- (long long)serverTimestamp`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setClientTimestamp:" title="setClientTimestamp:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="serverTimestamp" %}{% endlanying_code_snippet %}
```
### setClientTimestamp:

    Set local timestamp of the message
`- (void)setClientTimestamp:(long long)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setConfig:" title="setConfig:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setClientTimestamp:" %}{% endlanying_code_snippet %}
```
### setConfig:

Set message config

`- (void)setConfig:(BMXMessageConfig *)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setContent:" title="setContent:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setConfig:" %}{% endlanying_code_snippet %}
```
### setContent:

Set message content

`- (void)setContent:(NSString *)*content*`

#### Parameters

*content*  
    Text content

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setDeliveryQos:" title="setDeliveryQos:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setContent:" %}{% endlanying_code_snippet %}
```
### setDeliveryQos:

Set delivery QOS

`- (void)setDeliveryQos:(BMXMessage_DeliveryQos)*qos*`

#### Parameters

*qos*  
    Delivery QOS  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setDeliveryStatus:" title="setDeliveryStatus:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setDeliveryQos:" %}{% endlanying_code_snippet %}
```
### setDeliveryStatus:

Set delivery status

`- (void)setDeliveryStatus:(BMXMessage_DeliveryStatus)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setExtension:" title="setExtension:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setDeliveryStatus:" %}{% endlanying_code_snippet %}
```
### setExtension:

Set extension information

`- (void)setExtension:(NSString *)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setGroupAckCount:" title="setGroupAckCount:"></a>

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setExtension:" %}{% endlanying_code_snippet %}
```
### setIsDeliveryAcked:

Set delivery ACK sent or received

`- (void)setIsDeliveryAcked:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setIsPlayAcked:" title="setIsPlayAcked:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setIsDeliveryAcked:" %}{% endlanying_code_snippet %}
```
### setIsPlayAcked:

Set play ACK sent or received

`- (void)setIsPlayAcked:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setIsPlayed:" title="setIsPlayed:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setIsPlayAcked:" %}{% endlanying_code_snippet %}
```
### setIsPlayed:

Set play ACK sent or received

`- (void)setIsPlayed:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setIsRead:" title="setIsRead:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setIsPlayed:" %}{% endlanying_code_snippet %}
```
### setIsRead:

Set the message has been read

`- (void)setIsRead:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setIsReadAcked:" title="setIsReadAcked:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setIsRead:" %}{% endlanying_code_snippet %}
```
### setIsReadAcked:

Set read ACK sent or received

`- (void)setIsReadAcked:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setIsReceiveMsg:" title="setIsReceiveMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setIsReadAcked:" %}{% endlanying_code_snippet %}
```
### setIsReceiveMsg:

Set it as a received message

`- (void)setIsReceiveMsg:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPriority:" title="setPriority:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setIsReceiveMsg:" %}{% endlanying_code_snippet %}
```
### setPriority:

[0-10]. The priority of messages sent by members in the chat room is 5 by default, and messages can be discarded. For administrators, the priority defaults to 0, and messages are not dropped. Other values can be set as required

`- (void)setPriority:(int)*priority*`

#### Parameters

*priority*  
    Priority value

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushMessageMode:" title="setPushMessageMode:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setPriority:" %}{% endlanying_code_snippet %}
```
### setPushMessageMode:

Set it as a push message

`- (void)setPushMessageMode:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setSenderName:" title="setSenderName:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setPushMessageMode:" %}{% endlanying_code_snippet %}
```
### setSenderName:

Set sender name

`- (void)setSenderName:(NSString *)*senderName*`

#### Parameters

*senderName*  
    Sender name

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setServerTimestamp:" title="setServerTimestamp:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setSenderName:" %}{% endlanying_code_snippet %}
```
### setServerTimestamp:

Set the server-side timestamp of the message

`- (void)setServerTimestamp:(long long)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/toId" title="toId"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="setServerTimestamp:" %}{% endlanying_code_snippet %}
```
### toId

Receiver ID

`- (long long)toId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/type" title="type"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="toId" %}{% endlanying_code_snippet %}
```
### type

Message type

`- (BMXMessage_MessageType)type`

#### Return Value
<a href="../Constants/BMXMessage_MessageType.md">BMXMessage_MessageType</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXMessage",function="type" %}{% endlanying_code_snippet %}
```
