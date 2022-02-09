# BMXMessageObject Class Reference

  **Inherits from** NSObject  
  **Declared in** BMXMessageObject.h  

## Properties

<a name="//api/name/attachment" title="attachment"></a>
### attachment

`@property (nonatomic, strong, readonly) BMXMessageAttachment *attachment`

<a name="//api/name/clientMsgId" title="clientMsgId"></a>
### clientMsgId

`@property (nonatomic, assign, readonly) long long clientMsgId`

<a name="//api/name/clientTimestamp" title="clientTimestamp"></a>
### clientTimestamp

`@property (nonatomic, assign) long long clientTimestamp`

<a name="//api/name/content" title="content"></a>
### content

`@property (nonatomic, copy) NSString *content`

<a name="//api/name/contentType" title="contentType"></a>
### contentType

`@property (nonatomic, assign) BMXContentType contentType`

<a name="//api/name/conversationId" title="conversationId"></a>
### conversationId

`@property (nonatomic, assign) long long conversationId`

<a name="//api/name/deliverystatus" title="deliverystatus"></a>
### deliverystatus

`@property (nonatomic, assign) BMXDeliveryStatus deliverystatus`

<a name="//api/name/extensionJson" title="extensionJson"></a>
### extensionJson

`@property (nonatomic, copy) NSString *extensionJson`

<a name="//api/name/fromId" title="fromId"></a>
### fromId

`@property (nonatomic, assign, readonly) long long fromId`

<a name="//api/name/groupAckCount" title="groupAckCount"></a>
### groupAckCount

`@property (nonatomic, assign) int groupAckCount`

<a name="//api/name/isDeliveryAcked" title="isDeliveryAcked"></a>
### isDeliveryAcked

`@property (nonatomic, assign) BOOL isDeliveryAcked`

<a name="//api/name/isPlayed" title="isPlayed"></a>
### isPlayed

`@property (nonatomic, assign) BOOL isPlayed`

<a name="//api/name/isRead" title="isRead"></a>
### isRead

`@property (nonatomic, assign) BOOL isRead`

<a name="//api/name/isReadAcked" title="isReadAcked"></a>
### isReadAcked

`@property (nonatomic, assign) BOOL isReadAcked`

<a name="//api/name/isReceiveMsg" title="isReceiveMsg"></a>
### isReceiveMsg

`@property (nonatomic, assign) BOOL isReceiveMsg`

<a name="//api/name/messageType" title="messageType"></a>
### messageType

`@property (nonatomic, assign, readonly) BMXMessageType messageType`

<a name="//api/name/messageconfig" title="messageconfig"></a>
### messageconfig

`@property (nonatomic, strong) BMXMessageConfig *messageconfig`

<a name="//api/name/msgId" title="msgId"></a>
### msgId

`@property (nonatomic, assign, readonly) long long msgId`

<a name="//api/name/qos" title="qos"></a>
### qos

`@property (nonatomic, assign) DeliveryQosMode qos`

<a name="//api/name/senderName" title="senderName"></a>
### senderName

`@property (nonatomic, copy) NSString *senderName`

<a name="//api/name/serverTimestamp" title="serverTimestamp"></a>
### serverTimestamp

`@property (nonatomic, assign, readonly) long long serverTimestamp`

<a name="//api/name/toId" title="toId"></a>
### toId

`@property (nonatomic, assign, readonly) long long toId`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/initWithBMXCommandMessageText:fromId:toId:type:conversationId:" title="initWithBMXCommandMessageText:fromId:toId:type:conversationId:"></a>
### initWithBMXCommandMessageText:fromId:toId:type:conversationId:

Create a sent command message (command message holds command information in a content field or an extension field)

`- (instancetype)initWithBMXCommandMessageText:(NSString *)*content* fromId:(long long)*fromId* toId:(long long)*toId* type:(BMXMessageType)*mtype* conversationId:(long long)*conversationId*`

#### Parameters

*content*  
   Message content  

*fromId*  
   Message sender  

*toId*  
   Message receiver  

*mtype*  
   Message type  

*conversationId*  
   Conversation id  

#### Discussion
Create a sent command message (command message holds command information in a content field or an extension field)

#### Declared In
* `BMXMessageObject.h`

<a name="//api/name/initWithBMXMessageAttachment:fromId:toId:type:conversationId:" title="initWithBMXMessageAttachment:fromId:toId:type:conversationId:"></a>
### initWithBMXMessageAttachment:fromId:toId:type:conversationId:

Create attachment-message

`- (instancetype)initWithBMXMessageAttachment:(BMXMessageAttachment *)*attachment* fromId:(long long)*fromId* toId:(long long)*toId* type:(BMXMessageType)*mtype* conversationId:(long long)*conversationId*`

#### Parameters

*attachment*  
   <a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a>  

*fromId*  
   Send id  

*toId*  
   Receive id  

*mtype*  
   Message type  

*conversationId*  
   Conversation id  

#### Return Value
BMXMessageObject

#### Discussion
Create attachment-message

#### Declared In
* `BMXMessageObject.h`

<a name="//api/name/initWithBMXMessageText:fromId:toId:type:conversationId:" title="initWithBMXMessageText:fromId:toId:type:conversationId:"></a>
### initWithBMXMessageText:fromId:toId:type:conversationId:

Create text message

`- (instancetype)initWithBMXMessageText:(NSString *)*content* fromId:(long long)*fromId* toId:(long long)*toId* type:(BMXMessageType)*mtype* conversationId:(long long)*conversationId*`

#### Parameters

*content*  
   Content  

*fromId*  
   Send id  

*toId*  
   Receive id  

*mtype*  
   Message type  

*conversationId*  
   Conversation id  

#### Return Value
BMXMessageObject

#### Discussion
Create text message

#### Declared In
* `BMXMessageObject.h`

<a name="//api/name/initWithForwardMessage:fromId:toId:type:conversationId:" title="initWithForwardMessage:fromId:toId:type:conversationId:"></a>
### initWithForwardMessage:fromId:toId:type:conversationId:

Create a forwarding message

`- (instancetype)initWithForwardMessage:(BMXMessageObject *)*message* fromId:(long long)*fromId* toId:(long long)*toId* type:(BMXMessageType)*mtype* conversationId:(long long)*conversationId*`

#### Parameters

*message*  
   BMXMessageObject  

*fromId*  
   Send id  

*toId*  
   Receive id  

*mtype*  
   Message type  

*conversationId*  
   Conversation id  

#### Return Value
BMXMessageObject

#### Discussion
Create a forwarding message

#### Declared In
* `BMXMessageObject.h`

<a name="//api/name/initWithRecieveBMXMessageAttachment:msgId:fromId:toId:type:conversationId:timeStamp:" title="initWithRecieveBMXMessageAttachment:msgId:fromId:toId:type:conversationId:timeStamp:"></a>
### initWithRecieveBMXMessageAttachment:msgId:fromId:toId:type:conversationId:timeStamp:

Create receive attachment-message

`- (instancetype)initWithRecieveBMXMessageAttachment:(BMXMessageAttachment *)*attachment* msgId:(long long)*msgId* fromId:(long long)*fromId* toId:(long long)*toId* type:(BMXMessageType)*mtype* conversationId:(long long)*conversationId* timeStamp:(long long)*timeStamp*`

#### Parameters

*attachment*  
   <a href="../Classes/BMXMessageAttachment.md">BMXMessageAttachment</a>  

*msgId*  
   Message id  

*fromId*  
   Send id  

*toId*  
   Receive id  

*mtype*  
   Message type  

*conversationId*  
   Conversation id  

*timeStamp*  
   Timestamp  

#### Return Value
BMXMessageObject

#### Discussion
Create receive attachment-message

#### Declared In
* `BMXMessageObject.h`

<a name="//api/name/initWithRecieveBMXMessageCommandMessageText:msgId:fromId:toId:type:conversationId:timeStamp:" title="initWithRecieveBMXMessageCommandMessageText:msgId:fromId:toId:type:conversationId:timeStamp:"></a>
### initWithRecieveBMXMessageCommandMessageText:msgId:fromId:toId:type:conversationId:timeStamp:

Create a received command message (command message holds command information in a content field or an extension field)

`- (instancetype)initWithRecieveBMXMessageCommandMessageText:(NSString *)*content* msgId:(long long)*msgId* fromId:(long long)*fromId* toId:(long long)*toId* type:(BMXMessageType)*mtype* conversationId:(long long)*conversationId* timeStamp:(long long)*timeStamp*`

#### Parameters

*content*  
   Message content  

*msgId*  
   Message id  

*fromId*  
   Message sender  

*toId*  
   Message receiver  

*mtype*  
   Message type  

*conversationId*  
   Conversation id  

*timeStamp*  
   Server timestamp  

#### Discussion
Create a received command message (command message holds command information in a content field or an extension field)

#### Declared In
* `BMXMessageObject.h`

<a name="//api/name/initWithRecieveBMXMessageText:msgId:fromId:toId:type:conversationId:timeStamp:" title="initWithRecieveBMXMessageText:msgId:fromId:toId:type:conversationId:timeStamp:"></a>
### initWithRecieveBMXMessageText:msgId:fromId:toId:type:conversationId:timeStamp:

Create receive text-message

`- (instancetype)initWithRecieveBMXMessageText:(NSString *)*content* msgId:(long long)*msgId* fromId:(long long)*fromId* toId:(long long)*toId* type:(BMXMessageType)*mtype* conversationId:(long long)*conversationId* timeStamp:(long long)*timeStamp*`

#### Parameters

*content*  
   Content  

*msgId*  
   Message id  

*fromId*  
   Send id  

*toId*  
   Receive id  

*mtype*  
   Message type  

*conversationId*  
   Conversation id  

*timeStamp*  
   Timestamp  

#### Return Value
BMXMessageObject

#### Discussion
Create receive text-message

#### Declared In
* `BMXMessageObject.h`

