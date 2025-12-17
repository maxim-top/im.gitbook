# BMXChatService Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 聊天Service

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### ackMessageDeliveredWithMsg:

发送送达回执

`- (void)ackMessageDeliveredWithMsg:(BMXMessage *)*msg*`

#### Discussion

发送送达回执

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### ackMessageDeliveredWithMsg:completion:

发送送达回执

`- (void)ackMessageDeliveredWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Discussion

发送送达回执

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### ackMessageWithMsg:

发送已读回执

`- (void)ackMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
需要发送已读回执的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### ackMessageWithMsg:completion:

发送已读回执

`- (void)ackMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
需要发送已读回执的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### ackPlayMessageWithMsg:

发送音频/视频消息已播放回执

`- (void)ackPlayMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
需要发送已读回执的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### ackPlayMessageWithMsg:completion:

发送音频/视频消息已播放回执

`- (void)ackPlayMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
需要发送已读回执的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### addChatListener:

添加聊天监听者

`- (void)addChatListener:(id<BMXChatServiceProtocol>)*listener*`

#### Discussion

添加聊天监听者

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### addDelegate:

`- (void)addDelegate:(id<BMXChatServiceProtocol>)*aDelegate*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXChatServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### attachmentDir

获取附件保存路径

`- (NSString *)attachmentDir`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### attachmentDirForConversationWithConversationId:

获取会话的附件保存路径

`- (NSString *)attachmentDirForConversationWithConversationId:(long long)*conversationId*`

#### Parameters

_conversationId_\
需要获取会话附件路径的会话id

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### cancelDownloadAttachmentWithMsg:

取消下载附件

`- (void)cancelDownloadAttachmentWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
需要取消下载附件的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### cancelDownloadAttachmentWithMsg:completion:

取消下载附件

`- (void)cancelDownloadAttachmentWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
需要取消下载附件的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### cancelUploadAttachmentWithMsg:

取消上传附件

`- (void)cancelUploadAttachmentWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
需要取消上传附件的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### cancelUploadAttachmentWithMsg:completion:

取消上传附件

`- (void)cancelUploadAttachmentWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
需要取消上传附件的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### deleteConversationWithConversationId:

`- (void)deleteConversationWithConversationId:(long long)*conversationId*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### deleteConversationWithConversationId:completion:

`- (void)deleteConversationWithConversationId:(long long)*conversationId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### deleteConversationWithConversationId:synchronize:

删除会话

`- (void)deleteConversationWithConversationId:(long long)*conversationId* synchronize:(BOOL)*synchronize*`

#### Parameters

_conversationId_\
需要删除会话的会话id

_synchronize_\
是否同步删除其它设备该会话，默认为false，仅删除本设备会话

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### deleteConversationWithConversationId:synchronize:completion:

删除会话

`- (void)deleteConversationWithConversationId:(long long)*conversationId* synchronize:(BOOL)*synchronize* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_conversationId_\
需要删除会话的会话id

_synchronize_\
是否同步删除其它设备该会话，默认为false，仅删除本设备会话

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadAttachmentByUrlWithMsgId:url:path:

下载附件，下载状态变化和进度通过listener通知

`- (void)downloadAttachmentByUrlWithMsgId:(long long)*msgId* url:(NSString *)*url* path:(NSString *)*path*`

#### Discussion

下载附件，下载状态变化和进度通过listener通知

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadAttachmentByUrlWithMsgId:url:path:completion:

下载附件，下载状态变化和进度通过listener通知

`- (void)downloadAttachmentByUrlWithMsgId:(long long)*msgId* url:(NSString *)*url* path:(NSString *)*path* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Discussion

下载附件，下载状态变化和进度通过listener通知

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadAttachmentWithMsg:

下载附件，下载状态变化和进度通过listener通知

`- (void)downloadAttachmentWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
需要下载附件的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadAttachmentWithMsg:completion:

下载附件，下载状态变化和进度通过listener通知

`- (void)downloadAttachmentWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
需要下载附件的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadThumbnailWithMsg:

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadThumbnailWithMsg:completion:

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadThumbnailWithMsg:strategy:

下载缩略图，下载状态变化和进度通过listener通知 缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg* strategy:(BMXChatService_ThumbnailStrategy)*strategy*`

#### Parameters

_msg_\
需要下载缩略图的消息

_strategy_\
缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadThumbnailWithMsg:strategy:completion:

下载缩略图，下载状态变化和进度通过listener通知 缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg* strategy:(BMXChatService_ThumbnailStrategy)*strategy* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
需要下载缩略图的消息

_strategy_\
缩略图生成策略，1 - 第三方服务器生成， 2 - 本地服务器生成，默认值是 1。

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### forwardMessageWithList:to:newMsg:

合并转发消息

`- (BMXErrorCode)forwardMessageWithList:(BMXMessageList *)*list* to:(BMXConversation *)*to* newMsg:(BMXMessage *)*newMsg*`

#### Parameters

_list_\
转发的消息列表

_to_\
消息被转发到的会话

_newMsg_\
转发的消息列表合并后生成的新的单条转发消息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### forwardMessageWithMsg:

简单转发消息，用户应当通过[BMXMessage](BMXMessage.md)::createForwardMessage()先创建转发消息

`- (void)forwardMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
转发的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### forwardMessageWithMsg:completion:

简单转发消息，用户应当通过[BMXMessage](BMXMessage.md)::createForwardMessage()先创建转发消息

`- (void)forwardMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
转发的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getAllConversations

获取所有会话

`- (BMXConversationList *)getAllConversations`

#### Return Value

[BMXConversationList](BMXConversationList.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getAllConversationsUnreadCount

获取所有会话的全部未读数（标记为屏蔽的个人和群组的未读数不统计在内）

`- (int)getAllConversationsUnreadCount`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getAllConversationsWithCompletion:

获取所有会话

`- (void)getAllConversationsWithCompletion:(void ( ^ ) ( BMXConversationList *res ))*resBlock*`

#### Return Value

[BMXConversationList](BMXConversationList.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupAckMessageUnreadUserIdList:completion:

获取发送的群组消息未读用户id列表

`- (void)getGroupAckMessageUnreadUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

_msg_\
需要获取未读用户id列表的消息

_groupMemberIdList_\
对该条消息未读的用户id列表，初始传入为空列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupAckMessageUnreadUserIdList:groupMemberIdList:

获取发送的群组消息未读用户id列表

`- (BMXErrorCode)getGroupAckMessageUnreadUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

_msg_\
需要获取未读用户id列表的消息

_groupMemberIdList_\
对该条消息未读的用户id列表，初始传入为空列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupAckMessageUserIdList:completion:

获取发送的群组消息已读用户id列表

`- (void)getGroupAckMessageUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

_msg_\
需要获取已读用户id列表的消息

_groupMemberIdList_\
对该条消息已读的用户id列表，初始传入为空列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupAckMessageUserIdList:groupMemberIdList:

获取发送的群组消息已读用户id列表

`- (BMXErrorCode)getGroupAckMessageUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

_msg_\
需要获取已读用户id列表的消息

_groupMemberIdList_\
对该条消息已读的用户id列表，初始传入为空列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupPlayAckMessageUserIdList:completion:

获取发送的群组音频/视频消息已播放用户id列表（仅用于音频/视频消息）

`- (void)getGroupPlayAckMessageUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

_msg_\
需要获取已播放用户id列表的消息

_groupMemberIdList_\
对该条消息已播放的用户id列表，初始传入为空列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupPlayAckMessageUserIdList:groupMemberIdList:

获取发送的群组音频/视频消息已播放用户id列表（仅用于音频/视频消息）

`- (BMXErrorCode)getGroupPlayAckMessageUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

_msg_\
需要获取已播放用户id列表的消息

_groupMemberIdList_\
对该条消息已播放的用户id列表，初始传入为空列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupUnPlayAckMessageUserIdList:completion:

获取发送的群组音频/视频消息未播放用户id列表（仅用于音频/视频消息）

`- (void)getGroupUnPlayAckMessageUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

_msg_\
需要获取未播放用户id列表的消息

_groupMemberIdList_\
对该条消息未播放的用户id列表，初始传入为空列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupUnPlayAckMessageUserIdList:groupMemberIdList:

获取发送的群组音频/视频消息未播放用户id列表（仅用于音频/视频消息）

`- (BMXErrorCode)getGroupUnPlayAckMessageUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

_msg_\
需要获取未播放用户id列表的消息

_groupMemberIdList_\
对该条消息未播放的用户id列表，初始传入为空列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getMessage:

读取一条消息

`- (BMXMessage *)getMessage:(long long)*msgId*`

#### Parameters

_msgId_\
需要获取消息的消息id

#### Return Value

[BMXMessage](BMXMessage.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### insertMessagesWithList:

插入消息

`- (BMXErrorCode)insertMessagesWithList:(BMXMessageList *)*list*`

#### Parameters

_list_\
插入消息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### insertMessagesWithList:completion:

插入消息

`- (void)insertMessagesWithList:(BMXMessageList *)*list* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_list_\
插入消息列表

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### openConversationWithConversationId:type:

`- (BMXConversation *)openConversationWithConversationId:(long long)*conversationId* type:(BMXConversation_Type)*type*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### openConversationWithConversationId:type:createIfNotExist:

打开一个会话

`- (BMXConversation *)openConversationWithConversationId:(long long)*conversationId* type:(BMXConversation_Type)*type* createIfNotExist:(BOOL)*createIfNotExist*`

#### Parameters

_conversationId_\
需要打开的会话的会话id

_type_\
会话的类型，单聊还是群聊。

_createIfNotExist_\
会话不存在的情况下是否要创建本地会话，默认为创建

#### Return Value

[BMXConversation](BMXConversation.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### readAllMessageWithMsg:

标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备

`- (void)readAllMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
需要标记为此消息以前全部消息为已读的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### readAllMessageWithMsg:completion:

标记此消息及之前全部消息为已读，该消息同步到当前用户的所有设备

`- (void)readAllMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
需要标记为此消息以前全部消息为已读的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### readCancelWithMsg:

标记此消息为未读，该消息同步到当前用户的所有设备

`- (void)readCancelWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
需要发送消息已读取消的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### readCancelWithMsg:completion:

标记此消息为未读，该消息同步到当前用户的所有设备

`- (void)readCancelWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
需要发送消息已读取消的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### recallMessageWithMsg:

撤回消息，消息状态变化会通过listener通知

`- (void)recallMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
撤回的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### recallMessageWithMsg:completion:

撤回消息，消息状态变化会通过listener通知

`- (void)recallMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
撤回的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### removeChatListener:

移除聊天监听者

`- (void)removeChatListener:(id<BMXChatServiceProtocol>)*listener*`

#### Discussion

移除聊天监听者

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### removeDelegate:

`- (void)removeDelegate:(id<BMXChatServiceProtocol>)*aDelegate*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### removeMessageWithMsg:

`- (void)removeMessageWithMsg:(BMXMessage *)*msg*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### removeMessageWithMsg:completion:

`- (void)removeMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### removeMessageWithMsg:synchronize:

删除此消息，该消息同步到当前用户的其它设备

`- (void)removeMessageWithMsg:(BMXMessage *)*msg* synchronize:(BOOL)*synchronize*`

#### Parameters

_msg_\
需要删除的消息

_synchronize_\
是否同步到其它设备，不同步的情况下只会删除本地存储的该条消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### removeMessageWithMsg:synchronize:completion:

删除此消息，该消息同步到当前用户的其它设备

`- (void)removeMessageWithMsg:(BMXMessage *)*msg* synchronize:(BOOL)*synchronize* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
需要删除的消息

_synchronize_\
是否同步到其它设备，不同步的情况下只会删除本地存储的该条消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### resendMessageWithMsg:

重新发送消息，消息状态变化会通过listener通知

`- (void)resendMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
重新发送的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### resendMessageWithMsg:completion:

重新发送消息，消息状态变化会通过listener通知

`- (void)resendMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
重新发送的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### retrieveHistoryMessagesWithConversation:refMsgId:size:completion:

拉取历史消息

`- (void)retrieveHistoryMessagesWithConversation:(BMXConversation *)*conversation* refMsgId:(long long)*refMsgId* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *res , BMXError *aError ))*resBlock*`

#### Parameters

_conversation_\
需要拉取历史消息的会话

_refMsgId_\
拉取会话消息的起始消息Id

_size_\
拉取的最大消息条数

_result_\
拉取操作获取的消息列表，外部初始化传入空列表。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### retrieveHistoryMessagesWithConversation:refMsgId:size:result:

拉取历史消息

`- (BMXErrorCode)retrieveHistoryMessagesWithConversation:(BMXConversation *)*conversation* refMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

#### Parameters

_conversation_\
需要拉取历史消息的会话

_refMsgId_\
拉取会话消息的起始消息Id

_size_\
拉取的最大消息条数

_result_\
拉取操作获取的消息列表，外部初始化传入空列表。

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:

使用关键字搜索消息

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* arg5:(BMXConversation_Direction)*arg5* completion:(void ( ^ ) ( BMXMessageListList *res , BMXError *aError ))*resBlock*`

#### Parameters

_keywords_\
搜索的关键字

_refTime_\
搜索消息的起始时间

_size_\
搜索的最大消息条数

_result_\
搜索到的消息结果列表，外部初始化传入空列表。

_Direction_\
消息搜索方向，默认（Direction::Up）是从更早的消息中搜索

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-54='5' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:completion:

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageListList *res , BMXError *aError ))*resBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:result:

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageListList *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:

使用关键字搜索消息

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageListList *)*result* arg5:(BMXConversation_Direction)*arg5*`

#### Parameters

_keywords_\
搜索的关键字

_refTime_\
搜索消息的起始时间

_size_\
搜索的最大消息条数

_result_\
搜索到的消息结果列表，外部初始化传入空列表。

_Direction_\
消息搜索方向，默认（Direction::Up）是从更早的消息中搜索

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-54='5' data-55='5' data-56='5' data-57='5' data-58='5' data-59='5' data-60='5' data-61='5' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### sendMessageWithMsg:

发送消息，消息状态变化会通过listener通知

`- (void)sendMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
发送的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### sendMessageWithMsg:completion:

发送消息，消息状态变化会通过listener通知

`- (void)sendMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
发送的消息

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>
```
