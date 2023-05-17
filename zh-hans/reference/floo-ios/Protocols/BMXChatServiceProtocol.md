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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="conversationDidCreatedConversation:message:" %}{% endlanying_code_snippet %}
```
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
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="conversationDidDeletedConversationId:error:" %}{% endlanying_code_snippet %}
```
### conversationTotalCountChanged:

更新总未读数

`- (void)conversationTotalCountChanged:(NSInteger)*unreadCount*`

#### Parameters

*unreadCount*  
   未读数  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/loadAllConversationDidFinished" title="loadAllConversationDidFinished"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="conversationTotalCountChanged:" %}{% endlanying_code_snippet %}
```
### loadAllConversationDidFinished

已经加载完未读会话列表

`- (void)loadAllConversationDidFinished`

#### Discussion
已经加载完未读会话列表

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageAttachmentStatusDidChanged:error:percent:" title="messageAttachmentStatusDidChanged:error:percent:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="loadAllConversationDidFinished" %}{% endlanying_code_snippet %}
```
### messageAttachmentStatusDidChanged:error:percent:

附件下载状态发生变化

`- (void)messageAttachmentStatusDidChanged:(BMXMessage *)*message* error:(BMXError *)*error* percent:(int)*percent*`

#### Discussion
附件下载状态发生变化

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageAttachmentUploadProgressChanged:percent:" title="messageAttachmentUploadProgressChanged:percent:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="messageAttachmentStatusDidChanged:error:percent:" %}{% endlanying_code_snippet %}
```
### messageAttachmentUploadProgressChanged:percent:

附件上传进度发送变化

`- (void)messageAttachmentUploadProgressChanged:(BMXMessage *)*message* percent:(int)*percent*`

#### Discussion
附件上传进度发送变化

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageRecallStatusDidChanged:error:" title="messageRecallStatusDidChanged:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="messageAttachmentUploadProgressChanged:percent:" %}{% endlanying_code_snippet %}
```
### messageRecallStatusDidChanged:error:

消息撤回状态发送变化

`- (void)messageRecallStatusDidChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Discussion
消息撤回状态发送变化

#### Declared In
* `floo_proxy.h`

<a name="//api/name/messageStatusChanged:error:" title="messageStatusChanged:error:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="messageRecallStatusDidChanged:error:" %}{% endlanying_code_snippet %}
```
### messageStatusChanged:error:

消息发送状态发生变化

`- (void)messageStatusChanged:(BMXMessage *)*message* error:(BMXError *)*error*`

#### Discussion
消息发送状态发生变化

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receiveDeleteMessages:" title="receiveDeleteMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="messageStatusChanged:error:" %}{% endlanying_code_snippet %}
```
### receiveDeleteMessages:

收到删除消息 （多设备同步删除消息）

`- (void)receiveDeleteMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到删除消息 （多设备同步删除消息）

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receiveReadAllMessages:" title="receiveReadAllMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receiveDeleteMessages:" %}{% endlanying_code_snippet %}
```
### receiveReadAllMessages:

收到消息全部已读（多设备同步某消息之前消息全部设置为已读）

`- (void)receiveReadAllMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到消息全部已读（多设备同步某消息之前消息全部设置为已读）

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receiveReadCancelsMessages:" title="receiveReadCancelsMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receiveReadAllMessages:" %}{% endlanying_code_snippet %}
```
### receiveReadCancelsMessages:

收到消息已读取消（多设备其他设备同步消息已读状态变为未读）

`- (void)receiveReadCancelsMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到消息已读取消（多设备其他设备同步消息已读状态变为未读）

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedCommandMessages:" title="receivedCommandMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receiveReadCancelsMessages:" %}{% endlanying_code_snippet %}
```
### receivedCommandMessages:

收到命令消息

`- (void)receivedCommandMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到命令消息

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedDeliverAcks:" title="receivedDeliverAcks:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedCommandMessages:" %}{% endlanying_code_snippet %}
```
### receivedDeliverAcks:

收到消息已送达回执

`- (void)receivedDeliverAcks:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到消息已送达回执

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedMessages:" title="receivedMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedDeliverAcks:" %}{% endlanying_code_snippet %}
```
### receivedMessages:

收到消息

`- (void)receivedMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到消息

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedReadAcks:" title="receivedReadAcks:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedMessages:" %}{% endlanying_code_snippet %}
```
### receivedReadAcks:

收到消息已读回执

`- (void)receivedReadAcks:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到消息已读回执

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedRecallMessages:" title="receivedRecallMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedReadAcks:" %}{% endlanying_code_snippet %}
```
### receivedRecallMessages:

收到撤回消息

`- (void)receivedRecallMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到撤回消息

#### Declared In
* `floo_proxy.h`

<a name="//api/name/receivedSystemMessages:" title="receivedSystemMessages:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedRecallMessages:" %}{% endlanying_code_snippet %}
```
### receivedSystemMessages:

收到系统通知消息

`- (void)receivedSystemMessages:(NSArray<BMXMessage*> *)*messages*`

#### Discussion
收到系统通知消息

#### Declared In
* `floo_proxy.h`

<a name="//api/name/retrieveHistoryMessagesConversation:" title="retrieveHistoryMessagesConversation:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="receivedSystemMessages:" %}{% endlanying_code_snippet %}
```
### retrieveHistoryMessagesConversation:

拉取历史消息

`- (void)retrieveHistoryMessagesConversation:(BMXConversation *)*conversation*`

#### Discussion
拉取历史消息

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatServiceProtocol",function="retrieveHistoryMessagesConversation:" %}{% endlanying_code_snippet %}
```
