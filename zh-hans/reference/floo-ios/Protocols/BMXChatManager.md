# BMXChatManager Protocol Reference

  **Conforms to** NSObject  
  **Declared in** BMXChatManager.h  

## Overview

聊天管理器

## Instance Methods

<a name="//api/name/ackMessage:" title="ackMessage:"></a>
### ackMessage:

发送已读回执

`- (void)ackMessage:(BMXMessageObject *)*message*`

#### Discussion
发送已读回执

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/ackMessageDelivered:" title="ackMessageDelivered:"></a>
### ackMessageDelivered:

发送送达回执

`- (void)ackMessageDelivered:(BMXMessageObject *)*message*`

#### Discussion
发送送达回执

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/addChatListener:" title="addChatListener:"></a>
### addChatListener:

添加聊天监听者

`- (void)addChatListener:(id<BMXChatServiceProtocol>)*listener*`

#### Discussion
添加聊天监听者

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
### addDelegate:

`- (void)addDelegate:(id<BMXChatServiceProtocol>)*aDelegate*`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXChatServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/deleteConversationByConversationId:synchronize:" title="deleteConversationByConversationId:synchronize:"></a>
### deleteConversationByConversationId:synchronize:

删除会话

`- (void)deleteConversationByConversationId:(NSInteger)*conversationId* synchronize:(BOOL)*synchronize*`

#### Discussion
删除会话

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/downloadAttachment:" title="downloadAttachment:"></a>
### downloadAttachment:

下载附件，下载状态变化和进度通过listener通知

`- (void)downloadAttachment:(BMXMessageObject *)*message*`

#### Discussion
下载附件，下载状态变化和进度通过listener通知

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/downloadThumbnail:strategy:" title="downloadThumbnail:strategy:"></a>
### downloadThumbnail:strategy:

下载缩略图，下载状态变化和进度通过listener通知
缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。

`- (void)downloadThumbnail:(BMXMessageObject *)*message* strategy:(ThumbnailStrategy)*strategy*`

#### Discussion
下载缩略图，下载状态变化和进度通过listener通知
缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/forwardMessage:" title="forwardMessage:"></a>
### forwardMessage:

简单转发消息，用户应当通过BMXMessagse::createForwardMessage()先创建转发消息
*

`- (void)forwardMessage:(BMXMessageObject *)*message*`

#### Discussion
简单转发消息，用户应当通过BMXMessagse::createForwardMessage()先创建转发消息
*

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/getAllConversationsUnreadCountWithCompletion:" title="getAllConversationsUnreadCountWithCompletion:"></a>
### getAllConversationsUnreadCountWithCompletion:

获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内）

`- (void)getAllConversationsUnreadCountWithCompletion:(void ( ^ ) ( int count ))*aCompletionBlock*`

#### Parameters

*aCompletionBlock*  
   count  

#### Discussion
获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内）

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/getAllConversationsWithCompletion:" title="getAllConversationsWithCompletion:"></a>
### getAllConversationsWithCompletion:

获取所有会话

`- (void)getAllConversationsWithCompletion:(void ( ^ ) ( NSArray *conversations ))*aCompletionBlock*`

#### Discussion
获取所有会话

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/getAttachmentDir" title="getAttachmentDir"></a>
### getAttachmentDir

获取附件保存路径

`- (NSString *)getAttachmentDir`

#### Discussion
获取附件保存路径

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/getAttachmentDirForConversationWith:" title="getAttachmentDirForConversationWith:"></a>
### getAttachmentDirForConversationWith:

获取会话的附件保存路径

`- (NSString *)getAttachmentDirForConversationWith:(NSString *)*conversationId*`

#### Discussion
获取会话的附件保存路径

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/getGroupAckMessageUnreadUserIdListWithMessage:completion:" title="getGroupAckMessageUnreadUserIdListWithMessage:completion:"></a>
### getGroupAckMessageUnreadUserIdListWithMessage:completion:

获取发送的群组消息未读用户id列表

`- (void)getGroupAckMessageUnreadUserIdListWithMessage:(BMXMessageObject *)*message* completion:(void ( ^ ) ( NSArray *groupMemberIdList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*message*  
   需要获取未读用户id列表的消息  

*aCompletionBlock*  
   对该条消息未读的用户id列表，初始传入为空列表  

#### Discussion
获取发送的群组消息未读用户id列表

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/getGroupAckMessageUserIdListWithMessage:completion:" title="getGroupAckMessageUserIdListWithMessage:completion:"></a>
### getGroupAckMessageUserIdListWithMessage:completion:

获取发送的群组消息已读用户id列表

`- (void)getGroupAckMessageUserIdListWithMessage:(BMXMessageObject *)*message* completion:(void ( ^ ) ( NSArray *groupMemberIdList , BMXError *error ))*aCompletionBlock*`

#### Parameters

*message*  
   需要获取已读用户id列表的消息  

*aCompletionBlock*  
   对该条消息已读的用户id列表，初始传入为空列表  

#### Discussion
获取发送的群组消息已读用户id列表

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/getMessage:completion:" title="getMessage:completion:"></a>
### getMessage:completion:

读取一条消息

`- (void)getMessage:(NSInteger)*messageId* completion:(void ( ^ ) ( BMXMessageObject *message , BMXError *error ))*aCompletionBlock*`

#### Discussion
读取一条消息

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/insetMessages:completion:" title="insetMessages:completion:"></a>
### insetMessages:completion:

插入消息

`- (void)insetMessages:(NSArray<BMXMessageObject*> *)*list* completion:(void ( ^ ) ( BMXError *error ))*aCompletionBlock*`

#### Discussion
插入消息

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/openConversation:type:createIfNotExist:" title="openConversation:type:createIfNotExist:"></a>
### openConversation:type:createIfNotExist:

打开一个会话

`- (BMXConversation *)openConversation:(NSInteger)*conversationId* type:(BMXConversationType)*type* createIfNotExist:(bool)*create*`

#### Discussion
打开一个会话

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/readAllMessage:" title="readAllMessage:"></a>
### readAllMessage:

标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备

`- (void)readAllMessage:(BMXMessageObject *)*message*`

#### Discussion
标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/readCancel:" title="readCancel:"></a>
### readCancel:

标记此消息为未读，该消息同步到当前用户的所有设备

`- (void)readCancel:(BMXMessageObject *)*message*`

#### Discussion
标记此消息为未读，该消息同步到当前用户的所有设备

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/recallMessage:completion:" title="recallMessage:completion:"></a>
### recallMessage:completion:

撤回消息，消息状态变化会通过listener通知
*

`- (void)recallMessage:(BMXMessageObject *)*message* completion:(void ( ^ ) ( BMXMessageObject *message , BMXError *error ))*aCompletionBlock*`

#### Discussion
撤回消息，消息状态变化会通过listener通知
*

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/removeChatListener:" title="removeChatListener:"></a>
### removeChatListener:

移除聊天监听者

`- (void)removeChatListener:(id<BMXChatServiceProtocol>)*listener*`

#### Discussion
移除聊天监听者

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
### removeDelegate:

`- (void)removeDelegate:(id<BMXChatServiceProtocol>)*aDelegate*`

<a name="//api/name/removeMessage:synchronizeDeviceForce:" title="removeMessage:synchronizeDeviceForce:"></a>
### removeMessage:synchronizeDeviceForce:

删除此消息，该消息同步到当前用户的其它设备

`- (void)removeMessage:(BMXMessageObject *)*message* synchronizeDeviceForce:(BOOL)*synchronizeDeviceForce*`

#### Discussion
删除此消息，该消息同步到当前用户的其它设备

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/resendMessage:completion:" title="resendMessage:completion:"></a>
### resendMessage:completion:

重新发送消息，消息状态变化会通过listener通知
*

`- (void)resendMessage:(BMXMessageObject *)*message* completion:(void ( ^ ) ( BMXMessageObject *message , BMXError *error ))*aCompletionBlock*`

#### Discussion
重新发送消息，消息状态变化会通过listener通知
*

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/retrieveHistoryBMXconversation:msgId:size:completion:" title="retrieveHistoryBMXconversation:msgId:size:completion:"></a>
### retrieveHistoryBMXconversation:msgId:size:completion:

拉取历史消息

`- (void)retrieveHistoryBMXconversation:(BMXConversation *)*conversation* msgId:(long long)*msgId* size:(NSUInteger)*size* completion:(void ( ^ ) ( NSArray *messageListms , BMXError *error ))*aCompletionBlock*`

#### Discussion
拉取历史消息

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/searchMessagesByKeyWords:refTime:size:directionType:completion:" title="searchMessagesByKeyWords:refTime:size:directionType:completion:"></a>
### searchMessagesByKeyWords:refTime:size:directionType:completion:

搜索消息

`- (void)searchMessagesByKeyWords:(NSString *)*keywords* refTime:(NSTimeInterval)*refTime* size:(NSUInteger)*size* directionType:(BMXMessageDirection)*directionType* completion:(void ( ^ ) ( NSArray *array , BMXError *error ))*aCompletionBlock*`

#### Discussion
搜索消息

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/sendMessage:" title="sendMessage:"></a>
### sendMessage:

发送消息，消息状态变化会通过listener通知
*

`- (void)sendMessage:(BMXMessageObject *)*message*`

#### Discussion
发送消息，消息状态变化会通过listener通知
*

#### Declared In
* `BMXChatManager.h`

<a name="//api/name/transferingNum" title="transferingNum"></a>
### transferingNum

上传或下载中的文件数

`- (int)transferingNum`

#### Discussion
上传或下载中的文件数

#### Declared In
* `BMXChatManager.h`

