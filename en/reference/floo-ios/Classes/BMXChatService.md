# BMXChatService Class Reference

  **Inherits from** NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Chat Service

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

Send delivery ACK

`- (void)ackMessageDeliveredWithMsg:(BMXMessage *)*msg*`

#### Discussion
Send delivery ACK

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ackMessageDeliveredWithMsg:completion:" title="ackMessageDeliveredWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="ackMessageDeliveredWithMsg:" %}{% endlanying_code_snippet %}
```
### ackMessageDeliveredWithMsg:completion:

Send delivery ACK

`- (void)ackMessageDeliveredWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Discussion
Send delivery ACK

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ackMessageWithMsg:" title="ackMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="ackMessageDeliveredWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### ackMessageWithMsg:

Send read ACK

`- (void)ackMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   Message to be ACKed  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ackMessageWithMsg:completion:" title="ackMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="ackMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### ackMessageWithMsg:completion:

Send read ACK

`- (void)ackMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   Message to be ACKed  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ackPlayMessageWithMsg:" title="ackPlayMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="ackMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### ackPlayMessageWithMsg:

Send played ACK

`- (void)ackPlayMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   Message to be ACKed  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/ackPlayMessageWithMsg:completion:" title="ackPlayMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="ackPlayMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### ackPlayMessageWithMsg:completion:

Send played ACK

`- (void)ackPlayMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   Message to be ACKed  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addChatListener:" title="addChatListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="ackPlayMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### addChatListener:

Add a chat service listener

`- (void)addChatListener:(id<BMXChatServiceProtocol>)*listener*`

#### Discussion
Add a chat service listener

#### Declared In
* `floo_proxy.h`

<a name="//api/name/addDelegate:" title="addDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="addChatListener:" %}{% endlanying_code_snippet %}
```
### addDelegate:

`- (void)addDelegate:(id<BMXChatServiceProtocol>)*aDelegate*`

<a name="//api/name/addDelegate:delegateQueue:" title="addDelegate:delegateQueue:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="addDelegate:" %}{% endlanying_code_snippet %}
```
### addDelegate:delegateQueue:

`- (void)addDelegate:(id<BMXChatServiceProtocol>)*aDelegate* delegateQueue:(dispatch_queue_t)*aQueue*`

<a name="//api/name/attachmentDir" title="attachmentDir"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="addDelegate:delegateQueue:" %}{% endlanying_code_snippet %}
```
### attachmentDir

Get the directory where attachments saved

`- (NSString *)attachmentDir`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/attachmentDirForConversationWithConversationId:" title="attachmentDirForConversationWithConversationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="attachmentDir" %}{% endlanying_code_snippet %}
```
### attachmentDirForConversationWithConversationId:

Get the directory where attachments saved

`- (NSString *)attachmentDirForConversationWithConversationId:(long long)*conversationId*`

#### Parameters

*conversationId*  
   Conversation ID  

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelDownloadAttachmentWithMsg:" title="cancelDownloadAttachmentWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="attachmentDirForConversationWithConversationId:" %}{% endlanying_code_snippet %}
```
### cancelDownloadAttachmentWithMsg:

Cancel downloading attachments 

`- (void)cancelDownloadAttachmentWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelDownloadAttachmentWithMsg:completion:" title="cancelDownloadAttachmentWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="cancelDownloadAttachmentWithMsg:" %}{% endlanying_code_snippet %}
```
### cancelDownloadAttachmentWithMsg:completion:

Cancel downloading attachments

`- (void)cancelDownloadAttachmentWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelUploadAttachmentWithMsg:" title="cancelUploadAttachmentWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="cancelDownloadAttachmentWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### cancelUploadAttachmentWithMsg:

Cancel uploading attachments

`- (void)cancelUploadAttachmentWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/cancelUploadAttachmentWithMsg:completion:" title="cancelUploadAttachmentWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="cancelUploadAttachmentWithMsg:" %}{% endlanying_code_snippet %}
```
### cancelUploadAttachmentWithMsg:completion:

Cancel uploading attachments 

`- (void)cancelUploadAttachmentWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/dealloc" title="dealloc"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="cancelUploadAttachmentWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### dealloc

`- (void)dealloc`

<a name="//api/name/deleteConversationWithConversationId:" title="deleteConversationWithConversationId:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="dealloc" %}{% endlanying_code_snippet %}
```
### deleteConversationWithConversationId:

`- (void)deleteConversationWithConversationId:(long long)*conversationId*`

<a name="//api/name/deleteConversationWithConversationId:completion:" title="deleteConversationWithConversationId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="deleteConversationWithConversationId:" %}{% endlanying_code_snippet %}
```
### deleteConversationWithConversationId:completion:

`- (void)deleteConversationWithConversationId:(long long)*conversationId* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

<a name="//api/name/deleteConversationWithConversationId:synchronize:" title="deleteConversationWithConversationId:synchronize:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="deleteConversationWithConversationId:completion:" %}{% endlanying_code_snippet %}
```
### deleteConversationWithConversationId:synchronize:

Delete conversation

`- (void)deleteConversationWithConversationId:(long long)*conversationId* synchronize:(BOOL)*synchronize*`

#### Parameters

*conversationId*  
   Conversation ID  

*synchronize*  
   Whether delete conversations on other devices in the mean time or not, default to false

#### Declared In
* `floo_proxy.h`

<a name="//api/name/deleteConversationWithConversationId:synchronize:completion:" title="deleteConversationWithConversationId:synchronize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="deleteConversationWithConversationId:synchronize:" %}{% endlanying_code_snippet %}
```
### deleteConversationWithConversationId:synchronize:completion:

Delete conversation

`- (void)deleteConversationWithConversationId:(long long)*conversationId* synchronize:(BOOL)*synchronize* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*conversationId*  
   Conversation ID  

*synchronize*  
   Whether delete conversations on other devices in the mean time or not, default to false

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAttachmentByUrlWithMsgId:url:path:" title="downloadAttachmentByUrlWithMsgId:url:path:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="deleteConversationWithConversationId:synchronize:completion:" %}{% endlanying_code_snippet %}
```
### downloadAttachmentByUrlWithMsgId:url:path:

Download attachments, notify changes in download status and progress through the listener

`- (void)downloadAttachmentByUrlWithMsgId:(long long)*msgId* url:(NSString *)*url* path:(NSString *)*path*`

#### Discussion
Download attachments(Download status and progress callbacked by the listener)

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAttachmentByUrlWithMsgId:url:path:completion:" title="downloadAttachmentByUrlWithMsgId:url:path:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="downloadAttachmentByUrlWithMsgId:url:path:" %}{% endlanying_code_snippet %}
```
### downloadAttachmentByUrlWithMsgId:url:path:completion:

Download attachments(Download status and progress callbacked by the listener)

`- (void)downloadAttachmentByUrlWithMsgId:(long long)*msgId* url:(NSString *)*url* path:(NSString *)*path* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Discussion
Download attachments(Download status and progress callbacked by the listener)

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAttachmentWithMsg:" title="downloadAttachmentWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="downloadAttachmentByUrlWithMsgId:url:path:completion:" %}{% endlanying_code_snippet %}
```
### downloadAttachmentWithMsg:

Download attachments(Download status and progress callbacked by the listener)

`- (void)downloadAttachmentWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadAttachmentWithMsg:completion:" title="downloadAttachmentWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="downloadAttachmentWithMsg:" %}{% endlanying_code_snippet %}
```
### downloadAttachmentWithMsg:completion:

Download attachments(Download status and progress callbacked by the listener)

`- (void)downloadAttachmentWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadThumbnailWithMsg:" title="downloadThumbnailWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="downloadAttachmentWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### downloadThumbnailWithMsg:

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg*`

<a name="//api/name/downloadThumbnailWithMsg:completion:" title="downloadThumbnailWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="downloadThumbnailWithMsg:" %}{% endlanying_code_snippet %}
```
### downloadThumbnailWithMsg:completion:

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

<a name="//api/name/downloadThumbnailWithMsg:strategy:" title="downloadThumbnailWithMsg:strategy:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="downloadThumbnailWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### downloadThumbnailWithMsg:strategy:

Download attachments(Download status and progress callbacked by the listener)
Thumbnail generation strategy, 1- generated by third-party servers, 2- generated by local servers, default value is 1

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg* strategy:(BMXChatService_ThumbnailStrategy)*strategy*`

#### Parameters

*msg*  
   The message  

*strategy*  
   Thumbnail generation strategy, 1- generated by third-party servers, 2- generated by local servers, default value is 1.  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/downloadThumbnailWithMsg:strategy:completion:" title="downloadThumbnailWithMsg:strategy:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="downloadThumbnailWithMsg:strategy:" %}{% endlanying_code_snippet %}
```
### downloadThumbnailWithMsg:strategy:completion:

Download attachments
Thumbnail generation strategy, 1- generated by third-party servers, 2- generated by local servers, default value is 1.

`- (void)downloadThumbnailWithMsg:(BMXMessage *)*msg* strategy:(BMXChatService_ThumbnailStrategy)*strategy* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message 

*strategy*  
   Thumbnail generation strategy, 1- generated by third-party servers, 2- generated by local servers, default value is 1. 

#### Declared In
* `floo_proxy.h`

<a name="//api/name/forwardMessageWithList:to:newMsg:" title="forwardMessageWithList:to:newMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="downloadThumbnailWithMsg:strategy:completion:" %}{% endlanying_code_snippet %}
```
### forwardMessageWithList:to:newMsg:

Merge and forward messages

`- (BMXErrorCode)forwardMessageWithList:(BMXMessageList *)*list* to:(BMXConversation *)*to* newMsg:(BMXMessage *)*newMsg*`

#### Parameters

*list*  
   The message list

*to*  
   Destination conversation

*newMsg*  
   The new message generated from message list to be forwarded 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/forwardMessageWithMsg:" title="forwardMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="forwardMessageWithList:to:newMsg:" %}{% endlanying_code_snippet %}
```
### forwardMessageWithMsg:

Forward a single message,you should use<a href="../Classes/BMXMessage.md">BMXMessage</a>::createForwardMessage()create the new message first.

`- (void)forwardMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/forwardMessageWithMsg:completion:" title="forwardMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="forwardMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### forwardMessageWithMsg:completion:

Forward a single message,you should use<a href="../Classes/BMXMessage.md">BMXMessage</a>::createForwardMessage()create the new message first.

`- (void)forwardMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message   

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAllConversations" title="getAllConversations"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="forwardMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### getAllConversations

Get all conversations

`- (BMXConversationList *)getAllConversations`

#### Return Value
<a href="../Classes/BMXConversationList.md">BMXConversationList</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAllConversationsUnreadCount" title="getAllConversationsUnreadCount"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="getAllConversations" %}{% endlanying_code_snippet %}
```
### getAllConversationsUnreadCount

Get unread number for all conversations（Exclude blocked users and groups）

`- (int)getAllConversationsUnreadCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getAllConversationsWithCompletion:" title="getAllConversationsWithCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="getAllConversationsUnreadCount" %}{% endlanying_code_snippet %}
```
### getAllConversationsWithCompletion:

Get all conversations

`- (void)getAllConversationsWithCompletion:(void ( ^ ) ( BMXConversationList *res ))*resBlock*`

#### Return Value
<a href="../Classes/BMXConversationList.md">BMXConversationList</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupAckMessageUnreadUserIdList:completion:" title="getGroupAckMessageUnreadUserIdList:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="getAllConversationsWithCompletion:" %}{% endlanying_code_snippet %}
```
### getGroupAckMessageUnreadUserIdList:completion:

Get group member ID list who have not read the group message

`- (void)getGroupAckMessageUnreadUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

*msg*  
   The message  

*groupMemberIdList*  
   Member ID list as result 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupAckMessageUnreadUserIdList:groupMemberIdList:" title="getGroupAckMessageUnreadUserIdList:groupMemberIdList:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="getGroupAckMessageUnreadUserIdList:completion:" %}{% endlanying_code_snippet %}
```
### getGroupAckMessageUnreadUserIdList:groupMemberIdList:

Get group member ID list who have not read the group message

`- (BMXErrorCode)getGroupAckMessageUnreadUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

*msg*  
   The message

*groupMemberIdList*  
   Member ID list as result 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupAckMessageUserIdList:completion:" title="getGroupAckMessageUserIdList:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="getGroupAckMessageUnreadUserIdList:groupMemberIdList:" %}{% endlanying_code_snippet %}
```
### getGroupAckMessageUserIdList:completion:

Get group member ID list who have not read the group message

`- (void)getGroupAckMessageUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

*msg*  
   The message  

*groupMemberIdList*  
   Member ID list as result  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupAckMessageUserIdList:groupMemberIdList:" title="getGroupAckMessageUserIdList:groupMemberIdList:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="getGroupAckMessageUserIdList:completion:" %}{% endlanying_code_snippet %}
```
### getGroupAckMessageUserIdList:groupMemberIdList:

Get group member ID list who read the group message

`- (BMXErrorCode)getGroupAckMessageUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

*msg*  
   The message 

*groupMemberIdList*  
   Member ID list as result

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupPlayAckMessageUserIdList:completion:" title="getGroupPlayAckMessageUserIdList:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="getGroupAckMessageUserIdList:groupMemberIdList:" %}{% endlanying_code_snippet %}
```
### getGroupPlayAckMessageUserIdList:completion:

Get group member ID list who played the media file in group message

`- (void)getGroupPlayAckMessageUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

*msg*  
   The message 

*groupMemberIdList*  
   Member ID list as result

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupPlayAckMessageUserIdList:groupMemberIdList:" title="getGroupPlayAckMessageUserIdList:groupMemberIdList:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="getGroupPlayAckMessageUserIdList:completion:" %}{% endlanying_code_snippet %}
```
### getGroupPlayAckMessageUserIdList:groupMemberIdList:

Get group member ID list who played the media file in group message

`- (BMXErrorCode)getGroupPlayAckMessageUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

*msg*  
   The message  

*groupMemberIdList*  
   Member ID list as result 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupUnPlayAckMessageUserIdList:completion:" title="getGroupUnPlayAckMessageUserIdList:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="getGroupPlayAckMessageUserIdList:groupMemberIdList:" %}{% endlanying_code_snippet %}
```
### getGroupUnPlayAckMessageUserIdList:completion:

Get group member ID list who have not played the media file in group message

`- (void)getGroupUnPlayAckMessageUserIdList:(BMXMessage *)*msg* completion:(void ( ^ ) ( ListOfLongLong *res , BMXError *error ))*resBlock*`

#### Parameters

*msg*  
   The message  

*groupMemberIdList*  
   Member ID list as result 

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getGroupUnPlayAckMessageUserIdList:groupMemberIdList:" title="getGroupUnPlayAckMessageUserIdList:groupMemberIdList:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="getGroupUnPlayAckMessageUserIdList:completion:" %}{% endlanying_code_snippet %}
```
### getGroupUnPlayAckMessageUserIdList:groupMemberIdList:

Get group member ID list who have not played the media file in group message

`- (BMXErrorCode)getGroupUnPlayAckMessageUserIdList:(BMXMessage *)*msg* groupMemberIdList:(ListOfLongLong *)*groupMemberIdList*`

#### Parameters

*msg*  
   The message  

*groupMemberIdList*  
   Member ID list as result  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/getMessage:" title="getMessage:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="getGroupUnPlayAckMessageUserIdList:groupMemberIdList:" %}{% endlanying_code_snippet %}
```
### getMessage:

Get a message by ID

`- (BMXMessage *)getMessage:(long long)*msgId*`

#### Parameters

*msgId*  
   The message ID 

#### Return Value
<a href="../Classes/BMXMessage.md">BMXMessage</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/initWithCptr:swigOwnCObject:" title="initWithCptr:swigOwnCObject:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="getMessage:" %}{% endlanying_code_snippet %}
```
### initWithCptr:swigOwnCObject:

`- (id)initWithCptr:(void *)*cptr* swigOwnCObject:(BOOL)*ownCObject*`

<a name="//api/name/insertMessagesWithList:" title="insertMessagesWithList:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="initWithCptr:swigOwnCObject:" %}{% endlanying_code_snippet %}
```
### insertMessagesWithList:

Insert messages

`- (BMXErrorCode)insertMessagesWithList:(BMXMessageList *)*list*`

#### Parameters

*list*  
   The message list  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/insertMessagesWithList:completion:" title="insertMessagesWithList:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="insertMessagesWithList:" %}{% endlanying_code_snippet %}
```
### insertMessagesWithList:completion:

Insert messages

`- (void)insertMessagesWithList:(BMXMessageList *)*list* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*list*  
   The message list  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/openConversationWithConversationId:type:" title="openConversationWithConversationId:type:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="insertMessagesWithList:completion:" %}{% endlanying_code_snippet %}
```
### openConversationWithConversationId:type:

`- (BMXConversation *)openConversationWithConversationId:(long long)*conversationId* type:(BMXConversation_Type)*type*`

<a name="//api/name/openConversationWithConversationId:type:createIfNotExist:" title="openConversationWithConversationId:type:createIfNotExist:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="openConversationWithConversationId:type:" %}{% endlanying_code_snippet %}
```
### openConversationWithConversationId:type:createIfNotExist:

Open a conversation

`- (BMXConversation *)openConversationWithConversationId:(long long)*conversationId* type:(BMXConversation_Type)*type* createIfNotExist:(BOOL)*createIfNotExist*`

#### Parameters

*conversationId*  
   The conversation ID  

*type*  
   Conversation type: Single or Group

*createIfNotExist*  
   Create if NOT exist 

#### Return Value
<a href="../Classes/BMXConversation.md">BMXConversation</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/readAllMessageWithMsg:" title="readAllMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="openConversationWithConversationId:type:createIfNotExist:" %}{% endlanying_code_snippet %}
```
### readAllMessageWithMsg:

Mark this message and all previous messages as read and synchronize to all devices of the current user

`- (void)readAllMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/readAllMessageWithMsg:completion:" title="readAllMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="readAllMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### readAllMessageWithMsg:completion:

Mark this message and all previous messages as read and synchronize to all devices of the current user

`- (void)readAllMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/readCancelWithMsg:" title="readCancelWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="readAllMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### readCancelWithMsg:

Mark this message as unread and synchronize to all devices of the current user

`- (void)readCancelWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   The message 

#### Declared In
* `floo_proxy.h`

<a name="//api/name/readCancelWithMsg:completion:" title="readCancelWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="readCancelWithMsg:" %}{% endlanying_code_snippet %}
```
### readCancelWithMsg:completion:

Mark this message as unread and synchronize to all devices of the current user

`- (void)readCancelWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/recallMessageWithMsg:" title="recallMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="readCancelWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### recallMessageWithMsg:

Recall a message

`- (void)recallMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/recallMessageWithMsg:completion:" title="recallMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="recallMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### recallMessageWithMsg:completion:

Recall a message

`- (void)recallMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeChatListener:" title="removeChatListener:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="recallMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### removeChatListener:

Remove chat service listener

`- (void)removeChatListener:(id<BMXChatServiceProtocol>)*listener*`

#### Discussion
Remove chat service listener

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeDelegate:" title="removeDelegate:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="removeChatListener:" %}{% endlanying_code_snippet %}
```
### removeDelegate:

`- (void)removeDelegate:(id<BMXChatServiceProtocol>)*aDelegate*`

<a name="//api/name/removeMessageWithMsg:" title="removeMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="removeDelegate:" %}{% endlanying_code_snippet %}
```
### removeMessageWithMsg:

`- (void)removeMessageWithMsg:(BMXMessage *)*msg*`

<a name="//api/name/removeMessageWithMsg:completion:" title="removeMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="removeMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### removeMessageWithMsg:completion:

`- (void)removeMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

<a name="//api/name/removeMessageWithMsg:synchronize:" title="removeMessageWithMsg:synchronize:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="removeMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### removeMessageWithMsg:synchronize:

Remove a message

`- (void)removeMessageWithMsg:(BMXMessage *)*msg* synchronize:(BOOL)*synchronize*`

#### Parameters

*msg*  
   The message  

*synchronize*  
   Whether or not to synchronize to all devices of the current user

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeMessageWithMsg:synchronize:completion:" title="removeMessageWithMsg:synchronize:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="removeMessageWithMsg:synchronize:" %}{% endlanying_code_snippet %}
```
### removeMessageWithMsg:synchronize:completion:

Remove a message备

`- (void)removeMessageWithMsg:(BMXMessage *)*msg* synchronize:(BOOL)*synchronize* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message  

*synchronize*  
   Whether or not to synchronize to all devices of the current user 

#### Declared In
* `floo_proxy.h`

<a name="//api/name/resendMessageWithMsg:" title="resendMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="removeMessageWithMsg:synchronize:completion:" %}{% endlanying_code_snippet %}
```
### resendMessageWithMsg:

Resend a message

`- (void)resendMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   The message

#### Declared In
* `floo_proxy.h`

<a name="//api/name/resendMessageWithMsg:completion:" title="resendMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="resendMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### resendMessageWithMsg:completion:

Resend a message

`- (void)resendMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message

#### Declared In
* `floo_proxy.h`

<a name="//api/name/retrieveHistoryMessagesWithConversation:refMsgId:size:completion:" title="retrieveHistoryMessagesWithConversation:refMsgId:size:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="resendMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### retrieveHistoryMessagesWithConversation:refMsgId:size:completion:

Retrieve history messages

`- (void)retrieveHistoryMessagesWithConversation:(BMXConversation *)*conversation* refMsgId:(long long)*refMsgId* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *res , BMXError *aError ))*resBlock*`

#### Parameters

*conversation*  
   The conversation  

*refMsgId*  
   First Message Id  

*size*  
   Maximum number of messages

*result*  
   Message list as result

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/retrieveHistoryMessagesWithConversation:refMsgId:size:result:" title="retrieveHistoryMessagesWithConversation:refMsgId:size:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="retrieveHistoryMessagesWithConversation:refMsgId:size:completion:" %}{% endlanying_code_snippet %}
```
### retrieveHistoryMessagesWithConversation:refMsgId:size:result:

Retrieve history messages

`- (BMXErrorCode)retrieveHistoryMessagesWithConversation:(BMXConversation *)*conversation* refMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

#### Parameters

*conversation*  
   The conversation  

*refMsgId*  
   First Message Id

*size*  
   Maximum number of messages

*result*  
   Message list as result

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:" title="searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="retrieveHistoryMessagesWithConversation:refMsgId:size:result:" %}{% endlanying_code_snippet %}
```
### searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:

Search messages by keywords

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* arg5:(BMXConversation_Direction)*arg5* completion:(void ( ^ ) ( BMXMessageListList *res , BMXError *aError ))*resBlock*`

#### Parameters

*keywords*  
   The keywords

*refTime*  
   Starting time

*size*  
   Maximum number of messages

*result*  
   Message list as result

*Direction*  
   Search direction, Up for earlier

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/searchMessagesByKeyWordsWithKeywords:refTime:size:completion:" title="searchMessagesByKeyWordsWithKeywords:refTime:size:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:" %}{% endlanying_code_snippet %}
```
### searchMessagesByKeyWordsWithKeywords:refTime:size:completion:

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageListList *res , BMXError *aError ))*resBlock*`

<a name="//api/name/searchMessagesByKeyWordsWithKeywords:refTime:size:result:" title="searchMessagesByKeyWordsWithKeywords:refTime:size:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="searchMessagesByKeyWordsWithKeywords:refTime:size:completion:" %}{% endlanying_code_snippet %}
```
### searchMessagesByKeyWordsWithKeywords:refTime:size:result:

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageListList *)*result*`

<a name="//api/name/searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:" title="searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="searchMessagesByKeyWordsWithKeywords:refTime:size:result:" %}{% endlanying_code_snippet %}
```
### searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:

Search messages by keywords

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageListList *)*result* arg5:(BMXConversation_Direction)*arg5*`

#### Parameters

*keywords*  
   The keywords

*refTime*  
   Starting time

*size*  
   Maximum number of messages 

*result*  
   Message list as result  

*Direction*  
   Search direction, Up for earlier

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sendMessageWithMsg:" title="sendMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:" %}{% endlanying_code_snippet %}
```
### sendMessageWithMsg:

Send a message

`- (void)sendMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   The message  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/sendMessageWithMsg:completion:" title="sendMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="sendMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### sendMessageWithMsg:completion:

Send a message

`- (void)sendMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   发送的消息  

#### Declared In
* `floo_proxy.h`

<a name="//api/name/transferingNum" title="transferingNum"></a>
**Example**:
```
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="sendMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-ios",class="BMXChatService",function="transferingNum" %}{% endlanying_code_snippet %}
```
