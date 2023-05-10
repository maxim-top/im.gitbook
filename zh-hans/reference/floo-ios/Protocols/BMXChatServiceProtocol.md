# BMXChatServiceProtocol Protocol Reference

  **Conforms to** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@protocol 聊天服务监听者

## Instance Methods

<a name="//api/name/conversationDidCreatedConversation:message:" title="conversationDidCreatedConversation:message:"></a>
### conversationDidCreatedConversation:message:

本地创建新会话成功

`- (void)conversationDidCreatedConversation:(BMXConversation *)*conversation* message:(BMXMessage *)*message*`

#### Parameters

*conversation*  
   新创建的本地会话  

*message*  
   会话的最新消息，存在返回不存在返回为空  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/conversationDidDeletedConversationId:error:" title="conversationDidDeletedConversationId:error:"></a>
### conversationDidDeletedConversationId:error:

删除会话

`- (void)conversationDidDeletedConversationId:(NSInteger)*conversationId* error:(BMXError *)*error*`

#### Parameters

*conversationId*  
   删除的本地会话id  

*error*  
   状态错误码  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/conversationTotalCountChanged:" title="conversationTotalCountChanged:"></a>
### conversationTotalCountChanged:

更新总未读数

`- (void)conversationTotalCountChanged:(NSInteger)*unreadCount*`

#### Parameters

*unreadCount*  
   未读数  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/loadAllConversationDidFinished" title="loadAllConversationDidFinished"></a>
### loadAllConversationDidFinished

已经加载完未读会话列表

`- (void)loadAllConversationDidFinished`

#### Discussion
已经加载完未读会话列表

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageAttachmentStatusDidChanged:error:percent:" title="messageAttachmentStatusDidChanged:error:percent:"></a>
### messageAttachmentStatusDidChanged:error:percent:

附件下载状态发生变化

`- (void)messageAttachmentStatusDidChanged:(BMXMessage *)*message* error:(BMXError *)*error* percent:(int)*percent*`

#### Discussion
附件下载状态发生变化

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageAttachmentUploadProgressChanged:percent:" title="messageAttachmentUploadProgressChanged:percent:"></a>
### messageAttachmentUploadProgressChanged:percent:

附件上传进度发送变化

`- (void)messageAttachmentUploadProgressChanged:(BMXMessage *)*message* percent:(int)*percent*`

#### Discussion
附件上传进度发送变化

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageRecallStatusDidChanged:error:" title="messageRecallStatusDidChanged:error:"></a>
### messageRecallStatusDidChanged:error:

消息撤回状态发送变化

`- (void)messageRecallStatusDidChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Discussion
消息撤回状态发送变化

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageStatusChanged:error:" title="messageStatusChanged:error:"></a>
### messageStatusChanged:error:

消息发送状态发生变化

`- (void)messageStatusChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Discussion
消息发送状态发生变化

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receiveDeleteMessages:" title="receiveDeleteMessages:"></a>
### receiveDeleteMessages:

收到删除消息 （多设备同步删除消息）

`- (void)receiveDeleteMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到删除消息 （多设备同步删除消息）

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receiveReadAllMessages:" title="receiveReadAllMessages:"></a>
### receiveReadAllMessages:

收到消息全部已读（多设备同步某消息之前消息全部设置为已读）

`- (void)receiveReadAllMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到消息全部已读（多设备同步某消息之前消息全部设置为已读）

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receiveReadCancelsMessages:" title="receiveReadCancelsMessages:"></a>
### receiveReadCancelsMessages:

收到消息已读取消（多设备其他设备同步消息已读状态变为未读）

`- (void)receiveReadCancelsMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到消息已读取消（多设备其他设备同步消息已读状态变为未读）

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedCommandMessages:" title="receivedCommandMessages:"></a>
### receivedCommandMessages:

收到命令消息

`- (void)receivedCommandMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到命令消息

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedDeliverAcks:" title="receivedDeliverAcks:"></a>
### receivedDeliverAcks:

收到消息已送达回执

`- (void)receivedDeliverAcks:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到消息已送达回执

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedMessages:" title="receivedMessages:"></a>
### receivedMessages:

收到消息

`- (void)receivedMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到消息

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedReadAcks:" title="receivedReadAcks:"></a>
### receivedReadAcks:

收到消息已读回执

`- (void)receivedReadAcks:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到消息已读回执

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedRecallMessages:" title="receivedRecallMessages:"></a>
### receivedRecallMessages:

收到撤回消息

`- (void)receivedRecallMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到撤回消息

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedSystemMessages:" title="receivedSystemMessages:"></a>
### receivedSystemMessages:

收到系统通知消息

`- (void)receivedSystemMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到系统通知消息

#### Declared In
* `floo_proxy.h`

<a name="//api/name/retrieveHistoryMessagesConversation:" title="retrieveHistoryMessagesConversation:"></a>
### retrieveHistoryMessagesConversation:

拉取历史消息

`- (void)retrieveHistoryMessagesConversation:(BMXConversation *)*conversation*`

#### Discussion
拉取历史消息

#### Declared In
* `floo_proxy.h`

