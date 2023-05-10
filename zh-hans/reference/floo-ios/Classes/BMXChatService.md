# BMXChatService Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface 聊天Service

## Properties

<a name="//api/name/swigCMemOwn" title="swigCMemOwn"></a>
### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

<a name="//api/name/swigCPtr" title="swigCPtr"></a>
### swigCPtr

`@property (nonatomic) void *swigCPtr`

<a title="Instance Methods" name="instance_methods"></a>
## Instance Methods

<a name="//api/name/ackMessageDeliveredWithMsg:" title="ackMessageDeliveredWithMsg:"></a>
### ackMessageDeliveredWithMsg:

发送送达回执

`- (void)ackMessageDeliveredWithMsg:(BMXMessage *)*msg*`

#### Discussion
发送送达回执

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ackMessageDeliveredWithMsg:completion:" title="ackMessageDeliveredWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="ackMessageDeliveredWithMsg:" %}{% endlanying_code_snippet %}
```
### ackMessageDeliveredWithMsg:completion:

发送送达回执

`- (void)ackMessageDeliveredWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Discussion
发送送达回执

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ackMessageWithMsg:" title="ackMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="ackMessageDeliveredWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### ackMessageWithMsg:

发送已读回执

`- (void)ackMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   需要发送已读回执的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ackMessageWithMsg:completion:" title="ackMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="ackMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### ackMessageWithMsg:completion:

发送已读回执

`- (void)ackMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   需要发送已读回执的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ackPlayMessageWithMsg:" title="ackPlayMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="ackMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### ackPlayMessageWithMsg:

发送音频/视频消息已播放回执

`- (void)ackPlayMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   需要发送已读回执的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ackPlayMessageWithMsg:completion:" title="ackPlayMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="ackPlayMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### ackPlayMessageWithMsg:completion:

发送音频/视频消息已播放回执

`- (void)ackPlayMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   需要发送已读回执的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addChatListener:" title="addChatListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="ackPlayMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### addChatListener:

添加聊天监听者

`- (void)addChatListener:(id<BMXChatServiceProtocol>)*listener*`

#### Discussion
添加聊天监听者

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="addChatListener:" %}{% endlanying_code_snippet %}
```
### addDelegate:

`- (void)addDelegate:(id<BMXChatServiceProtocol>)*aDelegate*`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="addDelegate:" %}{% endlanying_code_snippet %}
```
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXChatServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/attachmentDir" title="attachmentDir"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="addDelegate:delegateQueue:" %}{% endlanying_code_snippet %}
```
### attachmentDir

获取附件保存路径

`- (NSString *)attachmentDir`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/attachmentDirForConversationWithConversationId:" title="attachmentDirForConversationWithConversationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="attachmentDir" %}{% endlanying_code_snippet %}
```
### attachmentDirForConversationWithConversationId:

获取会话的附件保存路径

`- (NSString *)attachmentDirForConversationWithConversationId:(long long)*conversationId*`

#### Parameters

*conversationId*  
   需要获取会话附件路径的会话id  

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelDownloadAttachmentWithMsg:" title="cancelDownloadAttachmentWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="attachmentDirForConversationWithConversationId:" %}{% endlanying_code_snippet %}
```
### cancelDownloadAttachmentWithMsg:

取消下载附件

`- (void)cancelDownloadAttachmentWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   需要取消下载附件的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelDownloadAttachmentWithMsg:completion:" title="cancelDownloadAttachmentWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="cancelDownloadAttachmentWithMsg:" %}{% endlanying_code_snippet %}
```
### cancelDownloadAttachmentWithMsg:completion:

取消下载附件

`- (void)cancelDownloadAttachmentWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   需要取消下载附件的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelUploadAttachmentWithMsg:" title="cancelUploadAttachmentWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="cancelDownloadAttachmentWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### cancelUploadAttachmentWithMsg:

取消上传附件

`- (void)cancelUploadAttachmentWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   需要取消上传附件的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelUploadAttachmentWithMsg:completion:" title="cancelUploadAttachmentWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="cancelUploadAttachmentWithMsg:" %}{% endlanying_code_snippet %}
```
### cancelUploadAttachmentWithMsg:completion:

取消上传附件

`- (void)cancelUploadAttachmentWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   需要取消上传附件的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="cancelUploadAttachmentWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/deleteConversationWithConversationId:" title="deleteConversationWithConversationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### deleteConversationWithConversationId:

`- (void)deleteConversationWithConversationId:(long long)*conversationId*`

<a name="//api/name/deleteConversationWithConversationId:completion:" title="deleteConversationWithConversationId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="deleteConversationWithConversationId:" %}{% endlanying_code_snippet %}
```
### deleteConversationWithConversationId:completion:

`- (void)deleteConversationWithConversationId:(long long)*conversationId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

<a name="//api/name/deleteConversationWithConversationId:synchronize:" title="deleteConversationWithConversationId:synchronize:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="deleteConversationWithConversationId:completion:" %}{% endlanying_code_snippet %}
```
### deleteConversationWithConversationId:synchronize:

删除会话

`- (void)deleteConversationWithConversationId:(long long)*conversationId* synchronize:(BOOL)*synchronize*`

#### Parameters

*conversationId*  
   需要删除会话的会话id  

*synchronize*  
   是否同步删除其它设备该会话，默认为false，仅删除本设备会话  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deleteConversationWithConversationId:synchronize:completion:" title="deleteConversationWithConversationId:synchronize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="deleteConversationWithConversationId:synchronize:" %}{% endlanying_code_snippet %}
```
### deleteConversationWithConversationId:synchronize:completion:

删除会话

`- (void)deleteConversationWithConversationId:(long long)*conversationId* synchronize:(BOOL)*synchronize* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*conversationId*  
   需要删除会话的会话id  

*synchronize*  
   是否同步删除其它设备该会话，默认为false，仅删除本设备会话  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAttachmentByUrlWithMsgId:url:path:" title="downloadAttachmentByUrlWithMsgId:url:path:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="deleteConversationWithConversationId:synchronize:completion:" %}{% endlanying_code_snippet %}
```
### downloadAttachmentByUrlWithMsgId:url:path:

下载附件，下载状态变化和进度通过listener通知

`- (void)downloadAttachmentByUrlWithMsgId:(long long)*msgId* url:(NSString *)*url* path:(NSString *)*path*`

#### Discussion
下载附件，下载状态变化和进度通过listener通知

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAttachmentByUrlWithMsgId:url:path:completion:" title="downloadAttachmentByUrlWithMsgId:url:path:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadAttachmentByUrlWithMsgId:url:path:" %}{% endlanying_code_snippet %}
```
### downloadAttachmentByUrlWithMsgId:url:path:completion:

下载附件，下载状态变化和进度通过listener通知

`- (void)downloadAttachmentByUrlWithMsgId:(long long)*msgId* url:(NSString *)*url* path:(NSString *)*path* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Discussion
下载附件，下载状态变化和进度通过listener通知

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAttachmentWithMsg:" title="downloadAttachmentWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadAttachmentByUrlWithMsgId:url:path:completion:" %}{% endlanying_code_snippet %}
```
### downloadAttachmentWithMsg:

下载附件，下载状态变化和进度通过listener通知

`- (void)downloadAttachmentWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   需要下载附件的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAttachmentWithMsg:completion:" title="downloadAttachmentWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadAttachmentWithMsg:" %}{% endlanying_code_snippet %}
```
### downloadAttachmentWithMsg:completion:

下载附件，下载状态变化和进度通过listener通知

`- (void)downloadAttachmentWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   需要下载附件的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadThumbnailWithMsg:" title="downloadThumbnailWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadAttachmentWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### downloadThumbnailWithMsg:

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg*`

<a name="//api/name/downloadThumbnailWithMsg:completion:" title="downloadThumbnailWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadThumbnailWithMsg:" %}{% endlanying_code_snippet %}
```
### downloadThumbnailWithMsg:completion:

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

<a name="//api/name/downloadThumbnailWithMsg:strategy:" title="downloadThumbnailWithMsg:strategy:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadThumbnailWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### downloadThumbnailWithMsg:strategy:

下载缩略图，下载状态变化和进度通过listener通知
缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg* strategy:(BMXChatService_ThumbnailStrategy)*strategy*`

#### Parameters

*msg*  
   需要下载缩略图的消息  

*strategy*  
   缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadThumbnailWithMsg:strategy:completion:" title="downloadThumbnailWithMsg:strategy:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadThumbnailWithMsg:strategy:" %}{% endlanying_code_snippet %}
```
### downloadThumbnailWithMsg:strategy:completion:

下载缩略图，下载状态变化和进度通过listener通知
缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg* strategy:(BMXChatService_ThumbnailStrategy)*strategy* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   需要下载缩略图的消息  

*strategy*  
   缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/forwardMessageWithList:to:newMsg:" title="forwardMessageWithList:to:newMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="downloadThumbnailWithMsg:strategy:completion:" %}{% endlanying_code_snippet %}
```
### forwardMessageWithList:to:newMsg:

合并转发消息

`- (BMXErrorCode)forwardMessageWithList:(BMXMessageList *)*list* to:(BMXConversation *)*to* newMsg:(BMXMessage *)*newMsg*`

#### Parameters

*list*  
   转发的消息列表  

*to*  
   消息被转发到的会话  

*newMsg*  
   转发的消息列表合并后生成的新的单条转发消息  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/forwardMessageWithMsg:" title="forwardMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="forwardMessageWithList:to:newMsg:" %}{% endlanying_code_snippet %}
```
### forwardMessageWithMsg:

简单转发消息，用户应当通过<a href="../Classes/BMXMessage.md">BMXMessage</a>::createForwardMessage()先创建转发消息

`- (void)forwardMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   转发的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/forwardMessageWithMsg:completion:" title="forwardMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="forwardMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### forwardMessageWithMsg:completion:

简单转发消息，用户应当通过<a href="../Classes/BMXMessage.md">BMXMessage</a>::createForwardMessage()先创建转发消息

`- (void)forwardMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   转发的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAllConversations" title="getAllConversations"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="forwardMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### getAllConversations

获取所有会话

`- (BMXConversationList *)getAllConversations`

#### Return Value
<a href="../Classes/BMXConversationList.md">BMXConversationList</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAllConversationsUnreadCount" title="getAllConversationsUnreadCount"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getAllConversations" %}{% endlanying_code_snippet %}
```
### getAllConversationsUnreadCount

获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内）

`- (int)getAllConversationsUnreadCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAllConversationsWithCompletion:" title="getAllConversationsWithCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getAllConversationsUnreadCount" %}{% endlanying_code_snippet %}
```
### getAllConversationsWithCompletion:

获取所有会话

`- (void)getAllConversationsWithCompletion:(void ( ^ ) ( BMXConversationList *res ))*resBlock*`

#### Return Value
<a href="../Classes/BMXConversationList.md">BMXConversationList</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupAckMessageUnreadUserIdList:completion:" title="getGroupAckMessageUnreadUserIdList:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getAllConversationsWithCompletion:" %}{% endlanying_code_snippet %}
```
### getGroupAckMessageUnreadUserIdList:completion:

获取发送的群组消息未读用户id列表

`- (void)getGroupAckMessageUnreadUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

*msg*  
   需要获取未读用户id列表的消息  

*groupMemberIdList*  
   对该条消息未读的用户id列表，初始传入为空列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupAckMessageUnreadUserIdList:groupMemberIdList:" title="getGroupAckMessageUnreadUserIdList:groupMemberIdList:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getGroupAckMessageUnreadUserIdList:completion:" %}{% endlanying_code_snippet %}
```
### getGroupAckMessageUnreadUserIdList:groupMemberIdList:

获取发送的群组消息未读用户id列表

`- (BMXErrorCode)getGroupAckMessageUnreadUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

*msg*  
   需要获取未读用户id列表的消息  

*groupMemberIdList*  
   对该条消息未读的用户id列表，初始传入为空列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupAckMessageUserIdList:completion:" title="getGroupAckMessageUserIdList:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getGroupAckMessageUnreadUserIdList:groupMemberIdList:" %}{% endlanying_code_snippet %}
```
### getGroupAckMessageUserIdList:completion:

获取发送的群组消息已读用户id列表

`- (void)getGroupAckMessageUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

*msg*  
   需要获取已读用户id列表的消息  

*groupMemberIdList*  
   对该条消息已读的用户id列表，初始传入为空列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupAckMessageUserIdList:groupMemberIdList:" title="getGroupAckMessageUserIdList:groupMemberIdList:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getGroupAckMessageUserIdList:completion:" %}{% endlanying_code_snippet %}
```
### getGroupAckMessageUserIdList:groupMemberIdList:

获取发送的群组消息已读用户id列表

`- (BMXErrorCode)getGroupAckMessageUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

*msg*  
   需要获取已读用户id列表的消息  

*groupMemberIdList*  
   对该条消息已读的用户id列表，初始传入为空列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupPlayAckMessageUserIdList:completion:" title="getGroupPlayAckMessageUserIdList:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getGroupAckMessageUserIdList:groupMemberIdList:" %}{% endlanying_code_snippet %}
```
### getGroupPlayAckMessageUserIdList:completion:

获取发送的群组音频/视频消息已播放用户id列表（仅用于音频/视频消息）

`- (void)getGroupPlayAckMessageUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

*msg*  
   需要获取已播放用户id列表的消息  

*groupMemberIdList*  
   对该条消息已播放的用户id列表，初始传入为空列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupPlayAckMessageUserIdList:groupMemberIdList:" title="getGroupPlayAckMessageUserIdList:groupMemberIdList:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getGroupPlayAckMessageUserIdList:completion:" %}{% endlanying_code_snippet %}
```
### getGroupPlayAckMessageUserIdList:groupMemberIdList:

获取发送的群组音频/视频消息已播放用户id列表（仅用于音频/视频消息）

`- (BMXErrorCode)getGroupPlayAckMessageUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

*msg*  
   需要获取已播放用户id列表的消息  

*groupMemberIdList*  
   对该条消息已播放的用户id列表，初始传入为空列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupUnPlayAckMessageUserIdList:completion:" title="getGroupUnPlayAckMessageUserIdList:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getGroupPlayAckMessageUserIdList:groupMemberIdList:" %}{% endlanying_code_snippet %}
```
### getGroupUnPlayAckMessageUserIdList:completion:

获取发送的群组音频/视频消息未播放用户id列表（仅用于音频/视频消息）

`- (void)getGroupUnPlayAckMessageUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

*msg*  
   需要获取未播放用户id列表的消息  

*groupMemberIdList*  
   对该条消息未播放的用户id列表，初始传入为空列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupUnPlayAckMessageUserIdList:groupMemberIdList:" title="getGroupUnPlayAckMessageUserIdList:groupMemberIdList:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getGroupUnPlayAckMessageUserIdList:completion:" %}{% endlanying_code_snippet %}
```
### getGroupUnPlayAckMessageUserIdList:groupMemberIdList:

获取发送的群组音频/视频消息未播放用户id列表（仅用于音频/视频消息）

`- (BMXErrorCode)getGroupUnPlayAckMessageUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

*msg*  
   需要获取未播放用户id列表的消息  

*groupMemberIdList*  
   对该条消息未播放的用户id列表，初始传入为空列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMessage:" title="getMessage:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getGroupUnPlayAckMessageUserIdList:groupMemberIdList:" %}{% endlanying_code_snippet %}
```
### getMessage:

读取一条消息

`- (BMXMessage *)getMessage:(long long)*msgId*`

#### Parameters

*msgId*  
   需要获取消息的消息id  

#### Return Value
<a href="../Classes/BMXMessage.md">BMXMessage</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="getMessage:" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/insertMessagesWithList:" title="insertMessagesWithList:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### insertMessagesWithList:

插入消息

`- (BMXErrorCode)insertMessagesWithList:(BMXMessageList *)*list*`

#### Parameters

*list*  
   插入消息列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/insertMessagesWithList:completion:" title="insertMessagesWithList:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="insertMessagesWithList:" %}{% endlanying_code_snippet %}
```
### insertMessagesWithList:completion:

插入消息

`- (void)insertMessagesWithList:(BMXMessageList *)*list* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*list*  
   插入消息列表  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/openConversationWithConversationId:type:" title="openConversationWithConversationId:type:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="insertMessagesWithList:completion:" %}{% endlanying_code_snippet %}
```
### openConversationWithConversationId:type:

`- (BMXConversation *)openConversationWithConversationId:(long long)*conversationId* type:(BMXConversation_Type)*type*`

<a name="//api/name/openConversationWithConversationId:type:createIfNotExist:" title="openConversationWithConversationId:type:createIfNotExist:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="openConversationWithConversationId:type:" %}{% endlanying_code_snippet %}
```
### openConversationWithConversationId:type:createIfNotExist:

打开一个会话

`- (BMXConversation *)openConversationWithConversationId:(long long)*conversationId* type:(BMXConversation_Type)*type* createIfNotExist:(BOOL)*createIfNotExist*`

#### Parameters

*conversationId*  
   需要打开的会话的会话id  

*type*  
   会话的类型，单聊还是群聊。  

*createIfNotExist*  
   会话不存在的情况下是否要创建本地会话，默认为创建  

#### Return Value
<a href="../Classes/BMXConversation.md">BMXConversation</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/readAllMessageWithMsg:" title="readAllMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="openConversationWithConversationId:type:createIfNotExist:" %}{% endlanying_code_snippet %}
```
### readAllMessageWithMsg:

标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备

`- (void)readAllMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   需要标记为此消息以前全部消息为已读的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/readAllMessageWithMsg:completion:" title="readAllMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="readAllMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### readAllMessageWithMsg:completion:

标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备

`- (void)readAllMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   需要标记为此消息以前全部消息为已读的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/readCancelWithMsg:" title="readCancelWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="readAllMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### readCancelWithMsg:

标记此消息为未读，该消息同步到当前用户的所有设备

`- (void)readCancelWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   需要发送消息已读取消的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/readCancelWithMsg:completion:" title="readCancelWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="readCancelWithMsg:" %}{% endlanying_code_snippet %}
```
### readCancelWithMsg:completion:

标记此消息为未读，该消息同步到当前用户的所有设备

`- (void)readCancelWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   需要发送消息已读取消的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/recallMessageWithMsg:" title="recallMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="readCancelWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### recallMessageWithMsg:

撤回消息，消息状态变化会通过listener通知

`- (void)recallMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   撤回的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/recallMessageWithMsg:completion:" title="recallMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="recallMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### recallMessageWithMsg:completion:

撤回消息，消息状态变化会通过listener通知

`- (void)recallMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   撤回的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeChatListener:" title="removeChatListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="recallMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### removeChatListener:

移除聊天监听者

`- (void)removeChatListener:(id<BMXChatServiceProtocol>)*listener*`

#### Discussion
移除聊天监听者

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeChatListener:" %}{% endlanying_code_snippet %}
```
### removeDelegate:

`- (void)removeDelegate:(id<BMXChatServiceProtocol>)*aDelegate*`

<a name="//api/name/removeMessageWithMsg:" title="removeMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeDelegate:" %}{% endlanying_code_snippet %}
```
### removeMessageWithMsg:

`- (void)removeMessageWithMsg:(BMXMessage *)*msg*`

<a name="//api/name/removeMessageWithMsg:completion:" title="removeMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### removeMessageWithMsg:completion:

`- (void)removeMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

<a name="//api/name/removeMessageWithMsg:synchronize:" title="removeMessageWithMsg:synchronize:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### removeMessageWithMsg:synchronize:

删除此消息，该消息同步到当前用户的其它设备

`- (void)removeMessageWithMsg:(BMXMessage *)*msg* synchronize:(BOOL)*synchronize*`

#### Parameters

*msg*  
   需要删除的消息  

*synchronize*  
   是否同步到其它设备，不同步的情况下只会删除本地存储的该条消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeMessageWithMsg:synchronize:completion:" title="removeMessageWithMsg:synchronize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeMessageWithMsg:synchronize:" %}{% endlanying_code_snippet %}
```
### removeMessageWithMsg:synchronize:completion:

删除此消息，该消息同步到当前用户的其它设备

`- (void)removeMessageWithMsg:(BMXMessage *)*msg* synchronize:(BOOL)*synchronize* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   需要删除的消息  

*synchronize*  
   是否同步到其它设备，不同步的情况下只会删除本地存储的该条消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/resendMessageWithMsg:" title="resendMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeMessageWithMsg:synchronize:completion:" %}{% endlanying_code_snippet %}
```
### resendMessageWithMsg:

重新发送消息，消息状态变化会通过listener通知

`- (void)resendMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   重新发送的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/resendMessageWithMsg:completion:" title="resendMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="resendMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### resendMessageWithMsg:completion:

重新发送消息，消息状态变化会通过listener通知

`- (void)resendMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   重新发送的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/retrieveHistoryMessagesWithConversation:refMsgId:size:completion:" title="retrieveHistoryMessagesWithConversation:refMsgId:size:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="resendMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### retrieveHistoryMessagesWithConversation:refMsgId:size:completion:

拉取历史消息

`- (void)retrieveHistoryMessagesWithConversation:(BMXConversation *)*conversation* refMsgId:(long long)*refMsgId* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *res , BMXError *aError ))*resBlock*`

#### Parameters

*conversation*  
   需要拉取历史消息的会话  

*refMsgId*  
   拉取会话消息的起始消息Id  

*size*  
   拉取的最大消息条数  

*result*  
   拉取操作获取的消息列表，外部初始化传入空列表。  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/retrieveHistoryMessagesWithConversation:refMsgId:size:result:" title="retrieveHistoryMessagesWithConversation:refMsgId:size:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="retrieveHistoryMessagesWithConversation:refMsgId:size:completion:" %}{% endlanying_code_snippet %}
```
### retrieveHistoryMessagesWithConversation:refMsgId:size:result:

拉取历史消息

`- (BMXErrorCode)retrieveHistoryMessagesWithConversation:(BMXConversation *)*conversation* refMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

#### Parameters

*conversation*  
   需要拉取历史消息的会话  

*refMsgId*  
   拉取会话消息的起始消息Id  

*size*  
   拉取的最大消息条数  

*result*  
   拉取操作获取的消息列表，外部初始化传入空列表。  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:" title="searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="retrieveHistoryMessagesWithConversation:refMsgId:size:result:" %}{% endlanying_code_snippet %}
```
### searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:

使用关键字搜索消息

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* arg5:(BMXConversation_Direction)*arg5* completion:(void ( ^ ) ( BMXMessageListList *res , BMXError *aError ))*resBlock*`

#### Parameters

*keywords*  
   搜索的关键字  

*refTime*  
   搜索消息的起始时间  

*size*  
   搜索的最大消息条数  

*result*  
   搜索到的消息结果列表，外部初始化传入空列表。  

*Direction*  
   消息搜索方向，默认（Direction::Up）是从更早的消息中搜索  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/searchMessagesByKeyWordsWithKeywords:refTime:size:completion:" title="searchMessagesByKeyWordsWithKeywords:refTime:size:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:" %}{% endlanying_code_snippet %}
```
### searchMessagesByKeyWordsWithKeywords:refTime:size:completion:

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageListList *res , BMXError *aError ))*resBlock*`

<a name="//api/name/searchMessagesByKeyWordsWithKeywords:refTime:size:result:" title="searchMessagesByKeyWordsWithKeywords:refTime:size:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchMessagesByKeyWordsWithKeywords:refTime:size:completion:" %}{% endlanying_code_snippet %}
```
### searchMessagesByKeyWordsWithKeywords:refTime:size:result:

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageListList *)*result*`

<a name="//api/name/searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:" title="searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchMessagesByKeyWordsWithKeywords:refTime:size:result:" %}{% endlanying_code_snippet %}
```
### searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:

使用关键字搜索消息

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageListList *)*result* arg5:(BMXConversation_Direction)*arg5*`

#### Parameters

*keywords*  
   搜索的关键字  

*refTime*  
   搜索消息的起始时间  

*size*  
   搜索的最大消息条数  

*result*  
   搜索到的消息结果列表，外部初始化传入空列表。  

*Direction*  
   消息搜索方向，默认（Direction::Up）是从更早的消息中搜索  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sendMessageWithMsg:" title="sendMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:" %}{% endlanying_code_snippet %}
```
### sendMessageWithMsg:

发送消息，消息状态变化会通过listener通知

`- (void)sendMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   发送的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sendMessageWithMsg:completion:" title="sendMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="sendMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### sendMessageWithMsg:completion:

发送消息，消息状态变化会通过listener通知

`- (void)sendMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   发送的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/transferingNum" title="transferingNum"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="sendMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### transferingNum

上传或下载中的文件数

`- (int)transferingNum`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="transferingNum" %}{% endlanying_code_snippet %}
```
