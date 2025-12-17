# BMXChatService Class Reference

**Inherits from** NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface Chat Service

## Properties

### swigCMemOwn

`@property (nonatomic) BOOL swigCMemOwn`

### swigCPtr

`@property (nonatomic) void *swigCPtr`

## Instance Methods

### ackMessageDeliveredWithMsg:

Send delivery ACK

`- (void)ackMessageDeliveredWithMsg:(BMXMessage *)*msg*`

#### Discussion

Send delivery ACK

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### ackMessageDeliveredWithMsg:completion:

Send delivery ACK

`- (void)ackMessageDeliveredWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Discussion

Send delivery ACK

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### ackMessageWithMsg:

Send read ACK

`- (void)ackMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
Message to be ACKed

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### ackMessageWithMsg:completion:

Send read ACK

`- (void)ackMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
Message to be ACKed

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### ackPlayMessageWithMsg:

Send played ACK

`- (void)ackPlayMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
Message to be ACKed

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### ackPlayMessageWithMsg:completion:

Send played ACK

`- (void)ackPlayMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
Message to be ACKed

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### addChatListener:

Add a chat service listener

`- (void)addChatListener:(id<BMXChatServiceProtocol>)*listener*`

#### Discussion

Add a chat service listener

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

Get the directory where attachments saved

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

Get the directory where attachments saved

`- (NSString *)attachmentDirForConversationWithConversationId:(long long)*conversationId*`

#### Parameters

_conversationId_\
Conversation ID

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### cancelDownloadAttachmentWithMsg:

Cancel downloading attachments

`- (void)cancelDownloadAttachmentWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### cancelDownloadAttachmentWithMsg:completion:

Cancel downloading attachments

`- (void)cancelDownloadAttachmentWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### cancelUploadAttachmentWithMsg:

Cancel uploading attachments

`- (void)cancelUploadAttachmentWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### cancelUploadAttachmentWithMsg:completion:

Cancel uploading attachments

`- (void)cancelUploadAttachmentWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

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

Delete conversation

`- (void)deleteConversationWithConversationId:(long long)*conversationId* synchronize:(BOOL)*synchronize*`

#### Parameters

_conversationId_\
Conversation ID

_synchronize_\
Whether delete conversations on other devices in the mean time or not, default to false

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### deleteConversationWithConversationId:synchronize:completion:

Delete conversation

`- (void)deleteConversationWithConversationId:(long long)*conversationId* synchronize:(BOOL)*synchronize* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_conversationId_\
Conversation ID

_synchronize_\
Whether delete conversations on other devices in the mean time or not, default to false

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadAttachmentByUrlWithMsgId:url:path:

Download attachments, notify changes in download status and progress through the listener

`- (void)downloadAttachmentByUrlWithMsgId:(long long)*msgId* url:(NSString *)*url* path:(NSString *)*path*`

#### Discussion

Download attachments(Download status and progress callbacked by the listener)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadAttachmentByUrlWithMsgId:url:path:completion:

Download attachments(Download status and progress callbacked by the listener)

`- (void)downloadAttachmentByUrlWithMsgId:(long long)*msgId* url:(NSString *)*url* path:(NSString *)*path* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Discussion

Download attachments(Download status and progress callbacked by the listener)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadAttachmentWithMsg:

Download attachments(Download status and progress callbacked by the listener)

`- (void)downloadAttachmentWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadAttachmentWithMsg:completion:

Download attachments(Download status and progress callbacked by the listener)

`- (void)downloadAttachmentWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

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

Download attachments(Download status and progress callbacked by the listener) Thumbnail generation strategy, 1- generated by third-party servers, 2- generated by local servers, default value is 1

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg* strategy:(BMXChatService_ThumbnailStrategy)*strategy*`

#### Parameters

_msg_\
The message

_strategy_\
Thumbnail generation strategy, 1- generated by third-party servers, 2- generated by local servers, default value is 1.

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### downloadThumbnailWithMsg:strategy:completion:

Download attachments Thumbnail generation strategy, 1- generated by third-party servers, 2- generated by local servers, default value is 1.

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg* strategy:(BMXChatService_ThumbnailStrategy)*strategy* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

_strategy_\
Thumbnail generation strategy, 1- generated by third-party servers, 2- generated by local servers, default value is 1.

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### forwardMessageWithList:to:newMsg:

Merge and forward messages

`- (BMXErrorCode)forwardMessageWithList:(BMXMessageList *)*list* to:(BMXConversation *)*to* newMsg:(BMXMessage *)*newMsg*`

#### Parameters

_list_\
The message list

_to_\
Destination conversation

_newMsg_\
The new message generated from message list to be forwarded

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### forwardMessageWithMsg:

Forward a single message,you should use[BMXMessage](BMXMessage.md)::createForwardMessage()create the new message first.

`- (void)forwardMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### forwardMessageWithMsg:completion:

Forward a single message,you should use[BMXMessage](BMXMessage.md)::createForwardMessage()create the new message first.

`- (void)forwardMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getAllConversations

Get all conversations

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

Get unread number for all conversations（Exclude blocked users and groups）

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

Get all conversations

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

Get group member ID list who have not read the group message

`- (void)getGroupAckMessageUnreadUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

_msg_\
The message

_groupMemberIdList_\
Member ID list as result

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupAckMessageUnreadUserIdList:groupMemberIdList:

Get group member ID list who have not read the group message

`- (BMXErrorCode)getGroupAckMessageUnreadUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

_msg_\
The message

_groupMemberIdList_\
Member ID list as result

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupAckMessageUserIdList:completion:

Get group member ID list who have not read the group message

`- (void)getGroupAckMessageUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

_msg_\
The message

_groupMemberIdList_\
Member ID list as result

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupAckMessageUserIdList:groupMemberIdList:

Get group member ID list who read the group message

`- (BMXErrorCode)getGroupAckMessageUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

_msg_\
The message

_groupMemberIdList_\
Member ID list as result

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupPlayAckMessageUserIdList:completion:

Get group member ID list who played the media file in group message

`- (void)getGroupPlayAckMessageUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

_msg_\
The message

_groupMemberIdList_\
Member ID list as result

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupPlayAckMessageUserIdList:groupMemberIdList:

Get group member ID list who played the media file in group message

`- (BMXErrorCode)getGroupPlayAckMessageUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

_msg_\
The message

_groupMemberIdList_\
Member ID list as result

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupUnPlayAckMessageUserIdList:completion:

Get group member ID list who have not played the media file in group message

`- (void)getGroupUnPlayAckMessageUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

_msg_\
The message

_groupMemberIdList_\
Member ID list as result

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getGroupUnPlayAckMessageUserIdList:groupMemberIdList:

Get group member ID list who have not played the media file in group message

`- (BMXErrorCode)getGroupUnPlayAckMessageUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

_msg_\
The message

_groupMemberIdList_\
Member ID list as result

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### getMessage:

Get a message by ID

`- (BMXMessage *)getMessage:(long long)*msgId*`

#### Parameters

_msgId_\
The message ID

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

Insert messages

`- (BMXErrorCode)insertMessagesWithList:(BMXMessageList *)*list*`

#### Parameters

_list_\
The message list

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### insertMessagesWithList:completion:

Insert messages

`- (void)insertMessagesWithList:(BMXMessageList *)*list* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_list_\
The message list

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

Open a conversation

`- (BMXConversation *)openConversationWithConversationId:(long long)*conversationId* type:(BMXConversation_Type)*type* createIfNotExist:(BOOL)*createIfNotExist*`

#### Parameters

_conversationId_\
The conversation ID

_type_\
Conversation type: Single or Group

_createIfNotExist_\
Create if NOT exist

#### Return Value

[BMXConversation](BMXConversation.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### readAllMessageWithMsg:

Mark this message and all previous messages as read and synchronize to all devices of the current user

`- (void)readAllMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### readAllMessageWithMsg:completion:

Mark this message and all previous messages as read and synchronize to all devices of the current user

`- (void)readAllMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### readCancelWithMsg:

Mark this message as unread and synchronize to all devices of the current user

`- (void)readCancelWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### readCancelWithMsg:completion:

Mark this message as unread and synchronize to all devices of the current user

`- (void)readCancelWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### recallMessageWithMsg:

Recall a message

`- (void)recallMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### recallMessageWithMsg:completion:

Recall a message

`- (void)recallMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### removeChatListener:

Remove chat service listener

`- (void)removeChatListener:(id<BMXChatServiceProtocol>)*listener*`

#### Discussion

Remove chat service listener

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

Remove a message

`- (void)removeMessageWithMsg:(BMXMessage *)*msg* synchronize:(BOOL)*synchronize*`

#### Parameters

_msg_\
The message

_synchronize_\
Whether or not to synchronize to all devices of the current user

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### removeMessageWithMsg:synchronize:completion:

Remove a message备

`- (void)removeMessageWithMsg:(BMXMessage *)*msg* synchronize:(BOOL)*synchronize* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

_synchronize_\
Whether or not to synchronize to all devices of the current user

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### resendMessageWithMsg:

Resend a message

`- (void)resendMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### resendMessageWithMsg:completion:

Resend a message

`- (void)resendMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### retrieveHistoryMessagesWithConversation:refMsgId:size:completion:

Retrieve history messages

`- (void)retrieveHistoryMessagesWithConversation:(BMXConversation *)*conversation* refMsgId:(long long)*refMsgId* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *res , BMXError *aError ))*resBlock*`

#### Parameters

_conversation_\
The conversation

_refMsgId_\
First Message Id

_size_\
Maximum number of messages

_result_\
Message list as result

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### retrieveHistoryMessagesWithConversation:refMsgId:size:result:

Retrieve history messages

`- (BMXErrorCode)retrieveHistoryMessagesWithConversation:(BMXConversation *)*conversation* refMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

#### Parameters

_conversation_\
The conversation

_refMsgId_\
First Message Id

_size_\
Maximum number of messages

_result_\
Message list as result

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:

Search messages by keywords

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* arg5:(BMXConversation_Direction)*arg5* completion:(void ( ^ ) ( BMXMessageListList *res , BMXError *aError ))*resBlock*`

#### Parameters

_keywords_\
The keywords

_refTime_\
Starting time

_size_\
Maximum number of messages

_result_\
Message list as result

_Direction_\
Search direction, Up for earlier

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

Search messages by keywords

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageListList *)*result* arg5:(BMXConversation_Direction)*arg5*`

#### Parameters

_keywords_\
The keywords

_refTime_\
Starting time

_size_\
Maximum number of messages

_result_\
Message list as result

_Direction_\
Search direction, Up for earlier

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-54='5' data-55='5' data-56='5' data-57='5' data-58='5' data-59='5' data-60='5' data-61='5' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### sendMessageWithMsg:

Send a message

`- (void)sendMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
The message

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>

```

### sendMessageWithMsg:completion:

Send a message

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

Number of files in transfer

`- (int)transferingNum`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXChatService'></div>
```
