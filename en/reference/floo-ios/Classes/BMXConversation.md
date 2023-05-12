# BMXConversation Class Reference

  **Inherits from** <a href="../Classes/BMXBaseObject.md">BMXBaseObject</a> :   
NSObject  
  **Declared in** floo_proxy.h  

## Overview

@interface Conversation

## Instance Methods

<a name="//api/name/conversationId" title="conversationId"></a>
### conversationId

Conversation ID

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

<a name="//api/name/editMessage" title="editMessage"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="dealloc" %}{% endlanying_code_snippet %}
```
### editMessage

Edit a message

`- (NSString *)editMessage`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/extension" title="extension"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="editMessage" %}{% endlanying_code_snippet %}
```
### extension

Extension information of a message

`- (NSString *)extension`

#### Return Value
NSString

#### Declared In
* `floo_proxy.h`

<a name="//api/name/insertMessageWithMsg:" title="insertMessageWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="extension" %}{% endlanying_code_snippet %}
```
### insertMessageWithMsg:

Insert a message

`- (BMXErrorCode)insertMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   The message  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/insertMessageWithMsg:completion:" title="insertMessageWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="insertMessageWithMsg:" %}{% endlanying_code_snippet %}
```
### insertMessageWithMsg:completion:

Insert a message

`- (void)insertMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/isMuteNotification" title="isMuteNotification"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="insertMessageWithMsg:completion:" %}{% endlanying_code_snippet %}
```
### isMuteNotification

Turn off message notifications

`- (BOOL)isMuteNotification`

#### Return Value
BOOL

#### Declared In
* `floo_proxy.h`

<a name="//api/name/lastMsg" title="lastMsg"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="isMuteNotification" %}{% endlanying_code_snippet %}
```
### lastMsg

The last message

`- (BMXMessage *)lastMsg`

#### Return Value
<a href="../Classes/BMXMessage.md">BMXMessage</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/loadMessageWithMsgId:" title="loadMessageWithMsgId:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="lastMsg" %}{% endlanying_code_snippet %}
```
### loadMessageWithMsgId:

Get a message by ID

`- (BMXMessage *)loadMessageWithMsgId:(long long)*msgId*`

#### Parameters

*msgId*  
   The message ID

#### Return Value
<a href="../Classes/BMXMessage.md">BMXMessage</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/loadMessageWithMsgId:completion:" title="loadMessageWithMsgId:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="loadMessageWithMsgId:" %}{% endlanying_code_snippet %}
```
### loadMessageWithMsgId:completion:

Get a message by ID

`- (void)loadMessageWithMsgId:(long long)*msgId* completion:(void ( ^ ) ( BMXMessage *res , BMXError *aError ))*resBlock*`

#### Parameters

*msgId*  
   The message ID

#### Return Value
<a href="../Classes/BMXMessage.md">BMXMessage</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/loadMessagesWithRefMsgId:size:arg4:completion:" title="loadMessagesWithRefMsgId:size:arg4:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="loadMessageWithMsgId:completion:" %}{% endlanying_code_snippet %}
```
### loadMessagesWithRefMsgId:size:arg4:completion:

Get messages from the starting message ID

`- (void)loadMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* arg4:(BMXConversation_Direction)*arg4* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

#### Parameters

*refMsgId*  
   Starting message ID 

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

<a name="//api/name/loadMessagesWithRefMsgId:size:completion:" title="loadMessagesWithRefMsgId:size:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="loadMessagesWithRefMsgId:size:arg4:completion:" %}{% endlanying_code_snippet %}
```
### loadMessagesWithRefMsgId:size:completion:

Search messages by message ID

`- (void)loadMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

#### Parameters

*size*  
   Maximum number of messages

*refTime*  
   Starting time

*result*  
   Message list as result

*keywords*  
   The keywords

*Direction*  
   Search direction, Up for earlier

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/loadMessagesWithRefMsgId:size:result:" title="loadMessagesWithRefMsgId:size:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="loadMessagesWithRefMsgId:size:completion:" %}{% endlanying_code_snippet %}
```
### loadMessagesWithRefMsgId:size:result:

`- (BMXErrorCode)loadMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

<a name="//api/name/loadMessagesWithRefMsgId:size:result:arg4:" title="loadMessagesWithRefMsgId:size:result:arg4:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="loadMessagesWithRefMsgId:size:result:" %}{% endlanying_code_snippet %}
```
### loadMessagesWithRefMsgId:size:result:arg4:

Load messages

`- (BMXErrorCode)loadMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result* arg4:(BMXConversation_Direction)*arg4*`

#### Parameters

*refMsgId*  
   First Message Id

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

<a name="//api/name/messageCount" title="messageCount"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="loadMessagesWithRefMsgId:size:result:arg4:" %}{% endlanying_code_snippet %}
```
### messageCount

The number of messages

`- (int)messageCount`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/refreshConversation" title="refreshConversation"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="messageCount" %}{% endlanying_code_snippet %}
```
### refreshConversation

Force update the total number of messages and unread messages for the conversation

`- (BMXErrorCode)refreshConversation`

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/refreshConversationWithCompletion:" title="refreshConversationWithCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="refreshConversation" %}{% endlanying_code_snippet %}
```
### refreshConversationWithCompletion:

Force update the total number of messages and unread messages for the conversation

`- (void)refreshConversationWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeAllMessages" title="removeAllMessages"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="refreshConversationWithCompletion:" %}{% endlanying_code_snippet %}
```
### removeAllMessages

Remove all messages in the conversation

`- (BMXErrorCode)removeAllMessages`

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/removeAllMessagesWithCompletion:" title="removeAllMessagesWithCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeAllMessages" %}{% endlanying_code_snippet %}
```
### removeAllMessagesWithCompletion:

Remove all messages in the conversation

`- (void)removeAllMessagesWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:" title="searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="removeAllMessagesWithCompletion:" %}{% endlanying_code_snippet %}
```
### searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:

Search messages by keywords

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* arg5:(BMXConversation_Direction)*arg5* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

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

#### Discussion
Deprecated. use searchMessagesByKeyWords instead.

#### Declared In
* `floo_proxy.h`

<a name="//api/name/searchMessagesByKeyWordsWithKeywords:refTime:size:completion:" title="searchMessagesByKeyWordsWithKeywords:refTime:size:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:" %}{% endlanying_code_snippet %}
```
### searchMessagesByKeyWordsWithKeywords:refTime:size:completion:

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

<a name="//api/name/searchMessagesByKeyWordsWithKeywords:refTime:size:result:" title="searchMessagesByKeyWordsWithKeywords:refTime:size:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchMessagesByKeyWordsWithKeywords:refTime:size:completion:" %}{% endlanying_code_snippet %}
```
### searchMessagesByKeyWordsWithKeywords:refTime:size:result:

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

<a name="//api/name/searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:" title="searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchMessagesByKeyWordsWithKeywords:refTime:size:result:" %}{% endlanying_code_snippet %}
```
### searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:

Search messages by keywords

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageList *)*result* arg5:(BMXConversation_Direction)*arg5*`

#### Parameters

*keywords*  
   The keywords

*refTime*  
   Starting time

*size*  
   Maximum number of messages

*result*  
   Message list as result

*arg5*  
   Search direction, Up for earlier

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/searchMessagesByTypeWithType:refTime:size:arg5:completion:" title="searchMessagesByTypeWithType:refTime:size:arg5:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:" %}{% endlanying_code_snippet %}
```
### searchMessagesByTypeWithType:refTime:size:arg5:completion:

Search messages by type

`- (void)searchMessagesByTypeWithType:(BMXMessage_ContentType)*type* refTime:(long long)*refTime* size:(unsigned long)*size* arg5:(BMXConversation_Direction)*arg5* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

#### Parameters

*type*  
   The type  

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

<a name="//api/name/searchMessagesByTypeWithType:refTime:size:completion:" title="searchMessagesByTypeWithType:refTime:size:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchMessagesByTypeWithType:refTime:size:arg5:completion:" %}{% endlanying_code_snippet %}
```
### searchMessagesByTypeWithType:refTime:size:completion:

`- (void)searchMessagesByTypeWithType:(BMXMessage_ContentType)*type* refTime:(long long)*refTime* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

<a name="//api/name/searchMessagesByTypeWithType:refTime:size:result:" title="searchMessagesByTypeWithType:refTime:size:result:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchMessagesByTypeWithType:refTime:size:completion:" %}{% endlanying_code_snippet %}
```
### searchMessagesByTypeWithType:refTime:size:result:

`- (BMXErrorCode)searchMessagesByTypeWithType:(BMXMessage_ContentType)*type* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

<a name="//api/name/searchMessagesByTypeWithType:refTime:size:result:arg5:" title="searchMessagesByTypeWithType:refTime:size:result:arg5:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchMessagesByTypeWithType:refTime:size:result:" %}{% endlanying_code_snippet %}
```
### searchMessagesByTypeWithType:refTime:size:result:arg5:

Search messages by type

`- (BMXErrorCode)searchMessagesByTypeWithType:(BMXMessage_ContentType)*type* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageList *)*result* arg5:(BMXConversation_Direction)*arg5*`

#### Parameters

*type*  
   The type

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

<a name="//api/name/setAllMessagesRead" title="setAllMessagesRead"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="searchMessagesByTypeWithType:refTime:size:result:arg5:" %}{% endlanying_code_snippet %}
```
### setAllMessagesRead

Set all messages as read

`- (BMXErrorCode)setAllMessagesRead`

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setAllMessagesReadWithCompletion:" title="setAllMessagesReadWithCompletion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setAllMessagesRead" %}{% endlanying_code_snippet %}
```
### setAllMessagesReadWithCompletion:

Set all messages as read

`- (void)setAllMessagesReadWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setEditMessage:" title="setEditMessage:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setAllMessagesReadWithCompletion:" %}{% endlanying_code_snippet %}
```
### setEditMessage:

Set message in editting

`- (BMXErrorCode)setEditMessage:(NSString *)*editMessage*`

#### Parameters

*editMessage*  
   The message content

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setExtension:" title="setExtension:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setEditMessage:" %}{% endlanying_code_snippet %}
```
### setExtension:

Set extension information of messages

`- (BMXErrorCode)setExtension:(NSString *)*ext*`

#### Parameters

*ext*  
   The extension information  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMessagePlayedStatus:status:" title="setMessagePlayedStatus:status:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setExtension:" %}{% endlanying_code_snippet %}
```
### setMessagePlayedStatus:status:

Set palyed status of messages

`- (BMXErrorCode)setMessagePlayedStatus:(BMXMessage *)*msg* status:(BOOL)*status*`

#### Parameters

*msg*  
    The message

*status*  
    Played or not

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMessagePlayedStatus:status:completion:" title="setMessagePlayedStatus:status:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMessagePlayedStatus:status:" %}{% endlanying_code_snippet %}
```
### setMessagePlayedStatus:status:completion:

Set the palyed status of messages

`- (void)setMessagePlayedStatus:(BMXMessage *)*msg* status:(BOOL)*status* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message

*status*  
   Played or not

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMessageReadStatus:status:" title="setMessageReadStatus:status:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMessagePlayedStatus:status:completion:" %}{% endlanying_code_snippet %}
```
### setMessageReadStatus:status:

Set the read status of messages

`- (BMXErrorCode)setMessageReadStatus:(BMXMessage *)*msg* status:(BOOL)*status*`

#### Parameters

*msg*  
   The message

*status*  
   Read or not

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/setMessageReadStatus:status:completion:" title="setMessageReadStatus:status:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMessageReadStatus:status:" %}{% endlanying_code_snippet %}
```
### setMessageReadStatus:status:completion:

Set the read status of messages

`- (void)setMessageReadStatus:(BMXMessage *)*msg* status:(BOOL)*status* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message

*status*  
   Read or not

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/type" title="type"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="setMessageReadStatus:status:completion:" %}{% endlanying_code_snippet %}
```
### type

Conversation type

`- (BMXConversation_Type)type`

#### Return Value
<a href="../Constants/BMXConversation_Type.md">BMXConversation_Type</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/unreadNumber" title="unreadNumber"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="type" %}{% endlanying_code_snippet %}
```
### unreadNumber

THe number of unread messages

`- (int)unreadNumber`

#### Return Value
int

#### Declared In
* `floo_proxy.h`

<a name="//api/name/updateMessageExtensionWithMsg:" title="updateMessageExtensionWithMsg:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="unreadNumber" %}{% endlanying_code_snippet %}
```
### updateMessageExtensionWithMsg:

Update the extension information of a message

`- (BMXErrorCode)updateMessageExtensionWithMsg:(BMXMessage *)*msg*`

#### Parameters

*msg*  
   The message  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

<a name="//api/name/updateMessageExtensionWithMsg:completion:" title="updateMessageExtensionWithMsg:completion:"></a>
**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="updateMessageExtensionWithMsg:" %}{% endlanying_code_snippet %}
```
### updateMessageExtensionWithMsg:completion:

Update the extension information of a message

`- (void)updateMessageExtensionWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

*msg*  
   The message  

#### Return Value
<a href="../Constants/BMXErrorCode.md">BMXErrorCode</a>

#### Declared In
* `floo_proxy.h`

**Example**:
```
{% lanying_code_snippet repo="floo-ios",class="",function="updateMessageExtensionWithMsg:completion:" %}{% endlanying_code_snippet %}
```
