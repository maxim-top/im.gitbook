# BMXConversation Class Reference

  **Inherits from** NSObject  
  **Declared in** BMXConversation.h  

## Properties

<a name="//api/name/conversationId" title="conversationId"></a>
### conversationId

会话Id

`@property (nonatomic, assign, readonly) long long conversationId`

#### Discussion
会话Id

#### Declared In
* `BMXConversation.h`

<a name="//api/name/editMessage" title="editMessage"></a>
### editMessage

编辑消息

`@property (nonatomic, copy) NSString *editMessage`

#### Discussion
编辑消息

#### Declared In
* `BMXConversation.h`

<a name="//api/name/extensionJson" title="extensionJson"></a>
### extensionJson

扩展信息

`@property (nonatomic, copy) NSString *extensionJson`

#### Discussion
扩展信息

#### Declared In
* `BMXConversation.h`

<a name="//api/name/isMuteNotication" title="isMuteNotication"></a>
### isMuteNotication

是否提醒用户消息,不提醒的情况下会话总未读数不会统计该会话计数。

`@property (nonatomic, assign) BOOL isMuteNotication`

#### Discussion
是否提醒用户消息,不提醒的情况下会话总未读数不会统计该会话计数。

#### Declared In
* `BMXConversation.h`

<a name="//api/name/lastMessage" title="lastMessage"></a>
### lastMessage

最新消息

`@property (nonatomic, strong, readonly) BMXMessageObject *lastMessage`

#### Discussion
最新消息

#### Declared In
* `BMXConversation.h`

<a name="//api/name/messageCount" title="messageCount"></a>
### messageCount

会话中所有消息数量

`@property (nonatomic, assign, readonly) NSInteger messageCount`

#### Discussion
会话中所有消息数量

#### Declared In
* `BMXConversation.h`

<a name="//api/name/type" title="type"></a>
### type

会话类型

`@property (nonatomic, assign, readonly) BMXConversationType type`

#### Discussion
会话类型

#### Declared In
* `BMXConversation.h`

<a name="//api/name/unreadNumber" title="unreadNumber"></a>
### unreadNumber

未读消息数量

`@property (nonatomic, assign, readonly) NSInteger unreadNumber`

#### Discussion
未读消息数量

#### Declared In
* `BMXConversation.h`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/insertMessage:completion:" title="insertMessage:completion:"></a>
### insertMessage:completion:

插入一条消息

`- (void)insertMessage:(BMXMessageObject *)*msg* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*msg*  
   message  

*aCompletionBlock*  
   Result  

#### Discussion
插入一条消息

#### Declared In
* `BMXConversation.h`

<a name="//api/name/loadMessage:completion:" title="loadMessage:completion:"></a>
### loadMessage:completion:

读取一条消息

`- (void)loadMessage:(long long)*msgId* completion:(void ( ^ ) ( BMXMessageObject *message ))*aCompletionBlock*`

#### Parameters

*msgId*  
   msgId  

*aCompletionBlock*  
   Result  

#### Discussion
读取一条消息

#### Declared In
* `BMXConversation.h`

<a name="//api/name/loadMessageFromMessageId:size:completion:" title="loadMessageFromMessageId:size:completion:"></a>
### loadMessageFromMessageId:size:completion:

加载消息，从参考消息向前加载，如果不指定则从最新消息开始

`- (void)loadMessageFromMessageId:(long long)*reMsgId* size:(NSUInteger)*size* completion:(void ( ^ ) ( NSArray *messageList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*reMsgId*  
   参考消息Id  

*size*  
   size  

*aCompletionBlock*  
   Result：MessageList  

#### Discussion
加载消息，从参考消息向前加载，如果不指定则从最新消息开始

#### Declared In
* `BMXConversation.h`

<a name="//api/name/removeAllMessagescompletion:" title="removeAllMessagescompletion:"></a>
### removeAllMessagescompletion:

删除会话中的所有消息

`- (void)removeAllMessagescompletion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*aCompletionBlock*  
   Result  

#### Discussion
删除会话中的所有消息

#### Declared In
* `BMXConversation.h`

<a name="//api/name/searchMessagesByKeyWords:refTime:size:directionType:completion:" title="searchMessagesByKeyWords:refTime:size:directionType:completion:"></a>
### searchMessagesByKeyWords:refTime:size:directionType:completion:

搜索消息，如果不指定则从最新消息开始

`- (void)searchMessagesByKeyWords:(NSString *)*keywords* refTime:(NSTimeInterval)*refTime* size:(NSUInteger)*size* directionType:(BMXMessageDirection)*directionType* completion:(void ( ^ ) ( NSArray<BMXMessageObject*> *messageList , BMXError *error ))*aCompletionBlock*`

#### Discussion
搜索消息，如果不指定则从最新消息开始

#### Declared In
* `BMXConversation.h`

<a name="//api/name/searchMessagesBycontentType:refTime:size:directionType:completion:" title="searchMessagesBycontentType:refTime:size:directionType:completion:"></a>
### searchMessagesBycontentType:refTime:size:directionType:completion:

按照类型搜索消息，如果不指定则从最新消息开始

`- (void)searchMessagesBycontentType:(BMXContentType)*contentType* refTime:(NSTimeInterval)*refTime* size:(NSUInteger)*size* directionType:(BMXMessageDirection)*directionType* completion:(void ( ^ ) ( NSArray<BMXMessageObject*> *messageList , BMXError *error ))*aCompletionBlock*`

#### Discussion
按照类型搜索消息，如果不指定则从最新消息开始

#### Declared In
* `BMXConversation.h`

<a name="//api/name/setAllMessagesReadCompletion:" title="setAllMessagesReadCompletion:"></a>
### setAllMessagesReadCompletion:

把所有消息设置为已读，更新未读消息数

`- (void)setAllMessagesReadCompletion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
把所有消息设置为已读，更新未读消息数

#### Declared In
* `BMXConversation.h`

<a name="//api/name/setMessagePlayedStatus:status:completion:" title="setMessagePlayedStatus:status:completion:"></a>
### setMessagePlayedStatus:status:completion:

设置消息播放状态（只对语音/视频消息有效）

`- (void)setMessagePlayedStatus:(BMXMessageObject *)*message* status:(bool)*status* completion:(void ( ^ ) ( BMXMessageObject *aMessage , BMXError *error ))*aCompletionBlock*`

#### Parameters

*message*  
   message  

*status*  
   播放状态  

*aCompletionBlock*  
   Result  

#### Discussion
设置消息播放状态（只对语音/视频消息有效）

#### Declared In
* `BMXConversation.h`

<a name="//api/name/setMessageReadStatus:status:completion:" title="setMessageReadStatus:status:completion:"></a>
### setMessageReadStatus:status:completion:

设置消息未读状态，更新未读消息数, 本地

`- (void)setMessageReadStatus:(BMXMessageObject *)*message* status:(BOOL)*status* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*message*  
   message  

*status*  
   是否已读  

*aCompletionBlock*  
   Result  

#### Discussion
设置消息未读状态，更新未读消息数, 本地

#### Declared In
* `BMXConversation.h`

<a name="//api/name/updateMessageExtension:completion:" title="updateMessageExtension:completion:"></a>
### updateMessageExtension:completion:

更新一条数据库存储消息的扩展字段信息

`- (void)updateMessageExtension:(BMXMessageObject *)*message* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Parameters

*message*  
   需要更改扩展信息的消息此时msg部分已经更新扩展字椴信息  

*aCompletionBlock*  
   更新结果  

#### Discussion
更新一条数据库存储消息的扩展字段信息

#### Declared In
* `BMXConversation.h`

