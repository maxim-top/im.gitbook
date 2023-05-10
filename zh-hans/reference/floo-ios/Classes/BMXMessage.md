# BMXMessage Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 消息

## Class Methods

<a name="//api/name/createCommandMessageWithFrom:to:type:conversationId:content:" title="createCommandMessageWithFrom:to:type:conversationId:content:"></a>
### createCommandMessageWithFrom:to:type:conversationId:content:

创建发送命令消息(命令消息通过content字段或者extension字段存放命令信息)

`+ (BMXMessage *)createCommandMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content*`

#### Parameters

*from*  
   消息发送者  

*to*  
   消息接收者  

*type*  
   消息类型  

*conversationId*  
   会话id  

*content*  
   消息内容  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createCommandMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:" title="createCommandMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createCommandMessageWithFrom:to:type:conversationId:content:" %}{% endlanying_code_snippet %}
```
### createCommandMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:

创建收到的命令消息(命令消息通过content字段或者extension字段存放命令信息)

`+ (BMXMessage *)createCommandMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

*msgId*  
   消息id  

*from*  
   消息发送者  

*to*  
   消息接收者  

*type*  
   消息类型  

*conversationId*  
   会话id  

*content*  
   消息内容  

*serverTimestamp*  
   服务器时间戳  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createForwardMessageWithMsg:from:to:type:conversationId:" title="createForwardMessageWithMsg:from:to:type:conversationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createCommandMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:" %}{% endlanying_code_snippet %}
```
### createForwardMessageWithMsg:from:to:type:conversationId:

创建转发消息

`+ (BMXMessage *)createForwardMessageWithMsg:(BMXMessage *)*msg* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId*`

#### Parameters

*msg*  
   要转发的消息  

*from*  
   消息发送者  

*to*  
   消息接收者  

*type*  
   消息类型  

*conversationId*  
   会话id  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createMessageWithFrom:to:type:conversationId:attachment:" title="createMessageWithFrom:to:type:conversationId:attachment:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createForwardMessageWithMsg:from:to:type:conversationId:" %}{% endlanying_code_snippet %}
```
### createMessageWithFrom:to:type:conversationId:attachment:

创建发送附件消息

`+ (BMXMessage *)createMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* attachment:(BMXMessageAttachment *)*attachment*`

#### Parameters

*from*  
   消息发送者  

*to*  
   消息接收者  

*type*  
   消息类型  

*conversationId*  
   会话id  

*attachment*  
   附件  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createMessageWithFrom:to:type:conversationId:content:" title="createMessageWithFrom:to:type:conversationId:content:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createMessageWithFrom:to:type:conversationId:attachment:" %}{% endlanying_code_snippet %}
```
### createMessageWithFrom:to:type:conversationId:content:

创建发送文本消息

`+ (BMXMessage *)createMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content*`

#### Parameters

*from*  
   消息发送者  

*to*  
   消息接收者  

*type*  
   消息类型  

*conversationId*  
   会话id  

*content*  
   消息内容  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createMessageWithMsgId:from:to:type:conversationId:attachment:serverTimestamp:" title="createMessageWithMsgId:from:to:type:conversationId:attachment:serverTimestamp:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createMessageWithFrom:to:type:conversationId:content:" %}{% endlanying_code_snippet %}
```
### createMessageWithMsgId:from:to:type:conversationId:attachment:serverTimestamp:

创建收到的消息

`+ (BMXMessage *)createMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* attachment:(BMXMessageAttachment *)*attachment* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

*msgId*  
   消息id  

*from*  
   消息发送者  

*to*  
   消息接收者  

*type*  
   消息类型  

*conversationId*  
   会话id  

*attachment*  
   附件  

*serverTimestamp*  
   服务器时间戳  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:" title="createMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createMessageWithMsgId:from:to:type:conversationId:attachment:serverTimestamp:" %}{% endlanying_code_snippet %}
```
### createMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:

创建收到的消息

`+ (BMXMessage *)createMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

*msgId*  
   消息id  

*from*  
   消息发送者  

*to*  
   消息接收者  

*type*  
   消息类型  

*conversationId*  
   会话id  

*content*  
   消息内容  

*serverTimestamp*  
   服务器时间戳  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createRTCMessageWithFrom:to:type:conversationId:content:" title="createRTCMessageWithFrom:to:type:conversationId:content:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:" %}{% endlanying_code_snippet %}
```
### createRTCMessageWithFrom:to:type:conversationId:content:

创建发送RTC消息

`+ (BMXMessage *)createRTCMessageWithFrom:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content*`

#### Parameters

*from*  
   消息发送者  

*to*  
   消息接收者  

*type*  
   消息类型  

*conversationId*  
   会话id  

*content*  
   消息内容  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/createRTCMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:" title="createRTCMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createRTCMessageWithFrom:to:type:conversationId:content:" %}{% endlanying_code_snippet %}
```
### createRTCMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:

创建收到的RTC消息

`+ (BMXMessage *)createRTCMessageWithMsgId:(long long)*msgId* from:(long long)*from* to:(long long)*to* type:(BMXMessage_MessageType)*type* conversationId:(long long)*conversationId* content:(NSString *)*content* serverTimestamp:(long long)*serverTimestamp*`

#### Parameters

*msgId*  
   消息id  

*from*  
   消息发送者  

*to*  
   消息接收者  

*type*  
   消息类型  

*conversationId*  
   会话id  

*content*  
   消息内容  

*serverTimestamp*  
   服务器时间戳  

#### Declared In
* `floo_proxy.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/attachment" title="attachment"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="createRTCMessageWithMsgId:from:to:type:conversationId:content:serverTimestamp:" %}{% endlanying_code_snippet %}
```
### attachment

消息附件，BMXMessage拥有附件的所有权，负责释放

`- (BMXMessageAttachment *)attachment`

#### Return Value
<a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/clientMsgId" title="clientMsgId"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="attachment" %}{% endlanying_code_snippet %}
```
### clientMsgId

消息客户端ID,仅在消息发送端存在

`- (long long)clientMsgId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/clientTimestamp" title="clientTimestamp"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="clientMsgId" %}{% endlanying_code_snippet %}
```
### clientTimestamp

本地时间戳（消息创建或者收到时的本地时间）

`- (long long)clientTimestamp`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/config" title="config"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="clientTimestamp" %}{% endlanying_code_snippet %}
```
### config

消息的配置信息

`- (BMXMessageConfig *)config`

#### Return Value
<a href="../Classes/BMXMessageConfig.md">BMXMessageConfig</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/content" title="content"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="config" %}{% endlanying_code_snippet %}
```
### content

消息文本内容

`- (NSString *)content`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/contentType" title="contentType"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="content" %}{% endlanying_code_snippet %}
```
### contentType

消息内容类型，如果带附件就表示附件类型，不带附件就是文本类型

`- (BMXMessage_ContentType)contentType`

#### Return Value
ContentType

#### Declared In
* `floo_proxy.h`

<a name="//api/name/conversationId" title="conversationId"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="contentType" %}{% endlanying_code_snippet %}
```
### conversationId

消息所属会话ID

`- (long long)conversationId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="conversationId" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/deliveryQos" title="deliveryQos"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### deliveryQos

消息投递QOS

`- (BMXMessage_DeliveryQos)deliveryQos`

#### Return Value
<a href="../Constants/BMXMessage_DeliveryQos.md">BMXMessage_DeliveryQos</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deliveryStatus" title="deliveryStatus"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="deliveryQos" %}{% endlanying_code_snippet %}
```
### deliveryStatus

消息投递状态

`- (BMXMessage_DeliveryStatus)deliveryStatus`

#### Return Value
<a href="../Constants/BMXMessage_DeliveryStatus.md">BMXMessage_DeliveryStatus</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/extension" title="extension"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="deliveryStatus" %}{% endlanying_code_snippet %}
```
### extension

消息扩展信息

`- (NSString *)extension`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/fromId" title="fromId"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="extension" %}{% endlanying_code_snippet %}
```
### fromId

消息发送方ID

`- (long long)fromId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupAckCount" title="groupAckCount"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="fromId" %}{% endlanying_code_snippet %}
```
### groupAckCount

群消息已读AckCount数目

`- (int)groupAckCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupAckReadAll" title="groupAckReadAll"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="groupAckCount" %}{% endlanying_code_snippet %}
```
### groupAckReadAll

群消息是否全部已读

`- (BOOL)groupAckReadAll`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupAckUnreadCount" title="groupAckUnreadCount"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="groupAckReadAll" %}{% endlanying_code_snippet %}
```
### groupAckUnreadCount

群消息未读AckCount数目

`- (int)groupAckUnreadCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupPlayAckCount" title="groupPlayAckCount"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="groupAckUnreadCount" %}{% endlanying_code_snippet %}
```
### groupPlayAckCount

群消息已播放AckCount数目（仅用于音频/视频附件消息）

`- (int)groupPlayAckCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupPlayAckReadAll" title="groupPlayAckReadAll"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="groupPlayAckCount" %}{% endlanying_code_snippet %}
```
### groupPlayAckReadAll

群消息是否全部已播放

`- (BOOL)groupPlayAckReadAll`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/groupPlayAckUnreadCount" title="groupPlayAckUnreadCount"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="groupPlayAckReadAll" %}{% endlanying_code_snippet %}
```
### groupPlayAckUnreadCount

群消息未播放AckCount数目（仅用于音频/视频附件消息）

`- (int)groupPlayAckUnreadCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isDeliveryAcked" title="isDeliveryAcked"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="groupPlayAckUnreadCount" %}{% endlanying_code_snippet %}
```
### isDeliveryAcked

对于发送方表示消息是否已投递到对方，对于接收方表示是否发送了消息已到达回执

`- (BOOL)isDeliveryAcked`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isPlayAcked" title="isPlayAcked"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="isDeliveryAcked" %}{% endlanying_code_snippet %}
```
### isPlayAcked

对于发送方表示是否收到了已播放回执，对于接收方表示是否发送了已播放回执

`- (BOOL)isPlayAcked`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isPlayed" title="isPlayed"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="isPlayAcked" %}{% endlanying_code_snippet %}
```
### isPlayed

语音或者视频消息是否播放过，仅对收到的音视频消息有效

`- (BOOL)isPlayed`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isPushMessage" title="isPushMessage"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="isPlayed" %}{% endlanying_code_snippet %}
```
### isPushMessage

消息是否是推送消息

`- (BOOL)isPushMessage`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isRead" title="isRead"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="isPushMessage" %}{% endlanying_code_snippet %}
```
### isRead

消息是否已读标志

`- (BOOL)isRead`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isReadAcked" title="isReadAcked"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="isRead" %}{% endlanying_code_snippet %}
```
### isReadAcked

对于发送方表示是否收到了已读回执，对于接收方表示是否发送了已读回执

`- (BOOL)isReadAcked`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isReceiveMsg" title="isReceiveMsg"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="isReadAcked" %}{% endlanying_code_snippet %}
```
### isReceiveMsg

是否接收的消息

`- (BOOL)isReceiveMsg`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/msgId" title="msgId"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="isReceiveMsg" %}{% endlanying_code_snippet %}
```
### msgId

消息唯一ID

`- (long long)msgId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/priority" title="priority"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="msgId" %}{% endlanying_code_snippet %}
```
### priority

消息的扩散优先级

`- (int)priority`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/senderName" title="senderName"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="priority" %}{% endlanying_code_snippet %}
```
### senderName

消息发送者的显示名称

`- (NSString *)senderName`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/serverTimestamp" title="serverTimestamp"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="senderName" %}{% endlanying_code_snippet %}
```
### serverTimestamp

消息时间戳（服务端收到时的时间）

`- (long long)serverTimestamp`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setClientTimestamp:" title="setClientTimestamp:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="serverTimestamp" %}{% endlanying_code_snippet %}
```
### setClientTimestamp:

设置消息本地时间戳

`- (void)setClientTimestamp:(long long)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setConfig:" title="setConfig:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setClientTimestamp:" %}{% endlanying_code_snippet %}
```
### setConfig:

设置消息配置信息

`- (void)setConfig:(BMXMessageConfig *)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setContent:" title="setContent:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setConfig:" %}{% endlanying_code_snippet %}
```
### setContent:

消息文本内容

`- (void)setContent:(NSString *)*content*`

#### Parameters

*content*  
   消息文本内容  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setDeliveryQos:" title="setDeliveryQos:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setContent:" %}{% endlanying_code_snippet %}
```
### setDeliveryQos:

设置消息投递QOS

`- (void)setDeliveryQos:(BMXMessage_DeliveryQos)*qos*`

#### Parameters

*qos*  
   消息投递QOS  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setDeliveryStatus:" title="setDeliveryStatus:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setDeliveryQos:" %}{% endlanying_code_snippet %}
```
### setDeliveryStatus:

设置消息投递状态

`- (void)setDeliveryStatus:(BMXMessage_DeliveryStatus)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setExtension:" title="setExtension:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setDeliveryStatus:" %}{% endlanying_code_snippet %}
```
### setExtension:

设置消息扩展信息

`- (void)setExtension:(NSString *)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setGroupAckCount:" title="setGroupAckCount:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setExtension:" %}{% endlanying_code_snippet %}
```
### setGroupAckCount:

设置消息已读groupAckCount数目(SDK 内部调用接口，上层不应该调用)

`- (void)setGroupAckCount:(int)*count*`

#### Parameters

*count*  
   设置群消息已读数目  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setGroupAckUnreadCount:" title="setGroupAckUnreadCount:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setGroupAckCount:" %}{% endlanying_code_snippet %}
```
### setGroupAckUnreadCount:

设置消息未读groupAckCount数目(SDK 内部调用接口，上层不应该调用)

`- (void)setGroupAckUnreadCount:(int)*count*`

#### Parameters

*count*  
   设置群消息未读数目  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setGroupPlayAckCount:" title="setGroupPlayAckCount:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setGroupAckUnreadCount:" %}{% endlanying_code_snippet %}
```
### setGroupPlayAckCount:

设置消息已播放groupAckCount数目(SDK 内部调用接口，上层不应该调用)（仅用于音频/视频附件消息）

`- (void)setGroupPlayAckCount:(int)*count*`

#### Parameters

*count*  
   设置群消息已读数目  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setGroupPlayAckUnreadCount:" title="setGroupPlayAckUnreadCount:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setGroupPlayAckCount:" %}{% endlanying_code_snippet %}
```
### setGroupPlayAckUnreadCount:

设置消息未播放groupAckCount数目(SDK 内部调用接口，上层不应该调用)（仅用于音频/视频附件消息）

`- (void)setGroupPlayAckUnreadCount:(int)*count*`

#### Parameters

*count*  
   设置群消息未播放数目  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setIsDeliveryAcked:" title="setIsDeliveryAcked:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setGroupPlayAckUnreadCount:" %}{% endlanying_code_snippet %}
```
### setIsDeliveryAcked:

设置投递回执

`- (void)setIsDeliveryAcked:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setIsPlayAcked:" title="setIsPlayAcked:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setIsDeliveryAcked:" %}{% endlanying_code_snippet %}
```
### setIsPlayAcked:

设置已播放回执

`- (void)setIsPlayAcked:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setIsPlayed:" title="setIsPlayed:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setIsPlayAcked:" %}{% endlanying_code_snippet %}
```
### setIsPlayed:

设置语音或者视频消息是否播放过，仅对收到的音视频消息有效

`- (void)setIsPlayed:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setIsRead:" title="setIsRead:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setIsPlayed:" %}{% endlanying_code_snippet %}
```
### setIsRead:

消息是否已读标志

`- (void)setIsRead:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setIsReadAcked:" title="setIsReadAcked:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setIsRead:" %}{% endlanying_code_snippet %}
```
### setIsReadAcked:

设置已读回执

`- (void)setIsReadAcked:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setIsReceiveMsg:" title="setIsReceiveMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setIsReadAcked:" %}{% endlanying_code_snippet %}
```
### setIsReceiveMsg:

设置是否接收的消息

`- (void)setIsReceiveMsg:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPriority:" title="setPriority:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setIsReceiveMsg:" %}{% endlanying_code_snippet %}
```
### setPriority:

取值范围0-10。普通人在聊天室发送的消息级别默认为5，可以丢弃。管理员默认为0不会丢弃。其它值可以根据业务自行设置。

`- (void)setPriority:(int)*priority*`

#### Parameters

*priority*  
   优先级  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setPushMessageMode:" title="setPushMessageMode:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setPriority:" %}{% endlanying_code_snippet %}
```
### setPushMessageMode:

设置消息是否为推送消息。

`- (void)setPushMessageMode:(BOOL)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setSenderName:" title="setSenderName:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setPushMessageMode:" %}{% endlanying_code_snippet %}
```
### setSenderName:

设置消息的发送者显示名称

`- (void)setSenderName:(NSString *)*senderName*`

#### Parameters

*senderName*  
   消息文本内容  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setServerTimestamp:" title="setServerTimestamp:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setSenderName:" %}{% endlanying_code_snippet %}
```
### setServerTimestamp:

设置时间戳（服务端收到时的时间）

`- (void)setServerTimestamp:(long long)*arg1*`

#### Declared In
* `floo_proxy.h`

<a name="//api/name/toId" title="toId"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setServerTimestamp:" %}{% endlanying_code_snippet %}
```
### toId

消息接收方ID

`- (long long)toId`

#### Return Value
long long

#### Declared In
* `floo_proxy.h`

<a name="//api/name/type" title="type"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="toId" %}{% endlanying_code_snippet %}
```
### type

消息类型

`- (BMXMessage_MessageType)type`

#### Return Value
<a href="../Constants/BMXMessage_MessageType.md">BMXMessage_MessageType</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="type" %}{% endlanying_code_snippet %}
```
