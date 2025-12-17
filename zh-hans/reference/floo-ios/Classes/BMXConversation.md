# BMXConversation Class Reference

**Inherits from** [BMXBaseObject](BMXBaseObject.md) :\
NSObject\
**Declared in** floo\_proxy.h

## Overview

@interface 会话

## Instance Methods

### conversationId

会话Id

`- (long long)conversationId`

#### Return Value

long long

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### dealloc

`- (void)dealloc`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### editMessage

编辑消息

`- (NSString *)editMessage`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### extension

扩展信息

`- (NSString *)extension`

#### Return Value

NSString

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### insertMessageWithMsg:

插入一条消息

`- (BMXErrorCode)insertMessageWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
插入的消息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### insertMessageWithMsg:completion:

插入一条消息

`- (void)insertMessageWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
插入的消息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### isMuteNotification

是否提醒用户消息,不提醒的情况下会话总未读数不会统计该会话计数。

`- (BOOL)isMuteNotification`

#### Return Value

BOOL

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### lastMsg

最新消息

`- (BMXMessage *)lastMsg`

#### Return Value

[BMXMessage](BMXMessage.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### loadMessageWithMsgId:

读取一条消息

`- (BMXMessage *)loadMessageWithMsgId:(long long)*msgId*`

#### Parameters

_msgId_\
需要读取的消息的消息id

#### Return Value

[BMXMessage](BMXMessage.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### loadMessageWithMsgId:completion:

读取一条消息

`- (void)loadMessageWithMsgId:(long long)*msgId* completion:(void ( ^ ) ( BMXMessage *res , BMXError *aError ))*resBlock*`

#### Parameters

_msgId_\
需要读取的消息的消息id

#### Return Value

[BMXMessage](BMXMessage.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### loadMessagesWithRefMsgId:size:arg4:completion:

加载消息，如果不指定则从最新消息开始

`- (void)loadMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* arg4:(BMXConversation_Direction)*arg4* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

#### Parameters

_refMsgId_\
加载消息的起始id

_size_\
最大加载消息条数

_result_\
数据库返回的加载消息列表

_Direction_\
加载消息的方向，默认是加载更早的消息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='4' data-2='4' data-3='4' data-4='4' data-5='4' data-6='4' data-7='4' data-8='4' data-9='4' data-10='4' data-11='4' data-12='4' data-13='4' data-14='4' data-15='4' data-16='4' data-17='4' data-18='4' data-19='4' data-20='4' data-21='4' data-22='4' data-23='4' data-24='4' data-25='4' data-26='4' data-27='4' data-28='4' data-29='4' data-30='4' data-31='4' data-32='4' data-33='4' data-34='4' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### loadMessagesWithRefMsgId:size:completion:

搜索消息，如果不指定则从最新消息开始

`- (void)loadMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

#### Parameters

_size_\
最大加载消息条数

_refTime_\
搜索消息的起始时间

_result_\
搜索到的消息结果列表

_keywords_\
搜索消息的关键字

_Direction_\
消息搜索方向，默认（Direction::Up）是从更早的消息中搜索

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### loadMessagesWithRefMsgId:size:result:

`- (BMXErrorCode)loadMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### loadMessagesWithRefMsgId:size:result:arg4:

加载消息，如果不指定则从最新消息开始

`- (BMXErrorCode)loadMessagesWithRefMsgId:(long long)*refMsgId* size:(unsigned long)*size* result:(BMXMessageList *)*result* arg4:(BMXConversation_Direction)*arg4*`

#### Parameters

_refMsgId_\
加载消息的起始id

_size_\
最大加载消息条数

_result_\
数据库返回的加载消息列表

_Direction_\
加载消息的方向，默认是加载更早的消息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='4' data-2='4' data-3='4' data-4='4' data-5='4' data-6='4' data-7='4' data-8='4' data-9='4' data-10='4' data-11='4' data-12='4' data-13='4' data-14='4' data-15='4' data-16='4' data-17='4' data-18='4' data-19='4' data-20='4' data-21='4' data-22='4' data-23='4' data-24='4' data-25='4' data-26='4' data-27='4' data-28='4' data-29='4' data-30='4' data-31='4' data-32='4' data-33='4' data-34='4' data-35='4' data-36='4' data-37='4' data-38='4' data-39='4' data-40='4' data-41='4' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### messageCount

会话中所有消息的数量

`- (int)messageCount`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### refreshConversation

读取数据库当前会话所有消息数量，强制更新conversation的消息总数和未读消息数。

`- (BMXErrorCode)refreshConversation`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### refreshConversationWithCompletion:

读取数据库当前会话所有消息数量，强制更新conversation的消息总数和未读消息数。

`- (void)refreshConversationWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### removeAllMessages

删除会话中的所有消息

`- (BMXErrorCode)removeAllMessages`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### removeAllMessagesWithCompletion:

删除会话中的所有消息

`- (void)removeAllMessagesWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:arg5:completion:

搜索消息，如果不指定则从最新消息开始

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* arg5:(BMXConversation_Direction)*arg5* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

#### Parameters

_keywords_\
搜索消息的关键字

_refTime_\
搜索消息的起始时间

_size_\
最大加载消息条数

_result_\
搜索到的消息结果列表

_Direction_\
消息搜索方向，默认（Direction::Up）是从更早的消息中搜索

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Discussion

Deprecated. use searchMessagesByKeyWords instead.

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-54='5' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:completion:

`- (void)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:result:

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByKeyWordsWithKeywords:refTime:size:result:arg5:

搜索消息，如果不指定则从最新消息开始

`- (BMXErrorCode)searchMessagesByKeyWordsWithKeywords:(NSString *)*keywords* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageList *)*result* arg5:(BMXConversation_Direction)*arg5*`

#### Parameters

_keywords_\
搜索消息的关键字

_refTime_\
搜索消息的起始时间

_size_\
最大加载消息条数

_result_\
搜索到的消息结果列表

_arg5_\
消息搜索方向，默认（Direction::Up）是从更早的消息中搜索

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-54='5' data-55='5' data-56='5' data-57='5' data-58='5' data-59='5' data-60='5' data-61='5' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByTypeWithType:refTime:size:arg5:completion:

按照类型搜索消息，如果不指定则从最新消息开始

`- (void)searchMessagesByTypeWithType:(BMXMessage_ContentType)*type* refTime:(long long)*refTime* size:(unsigned long)*size* arg5:(BMXConversation_Direction)*arg5* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

#### Parameters

_type_\
搜索消息的类型

_refTime_\
搜索消息的起始时间

_size_\
最大加载消息条数

_result_\
搜索到的消息结果列表

_Direction_\
消息搜索方向，默认（Direction::Up）是从更早的消息中搜索

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByTypeWithType:refTime:size:completion:

`- (void)searchMessagesByTypeWithType:(BMXMessage_ContentType)*type* refTime:(long long)*refTime* size:(unsigned long)*size* completion:(void ( ^ ) ( BMXMessageList *result , BMXError *aError ))*resBlock*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByTypeWithType:refTime:size:result:

`- (BMXErrorCode)searchMessagesByTypeWithType:(BMXMessage_ContentType)*type* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageList *)*result*`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### searchMessagesByTypeWithType:refTime:size:result:arg5:

按照类型搜索消息，如果不指定则从最新消息开始

`- (BMXErrorCode)searchMessagesByTypeWithType:(BMXMessage_ContentType)*type* refTime:(long long)*refTime* size:(unsigned long)*size* result:(BMXMessageList *)*result* arg5:(BMXConversation_Direction)*arg5*`

#### Parameters

_type_\
搜索消息的类型

_refTime_\
搜索消息的起始时间

_size_\
最大加载消息条数

_result_\
搜索到的消息结果列表

_Direction_\
消息搜索方向，默认（Direction::Up）是从更早的消息中搜索

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-1='5' data-2='5' data-3='5' data-4='5' data-5='5' data-6='5' data-7='5' data-8='5' data-9='5' data-10='5' data-11='5' data-12='5' data-13='5' data-14='5' data-15='5' data-16='5' data-17='5' data-18='5' data-19='5' data-20='5' data-21='5' data-22='5' data-23='5' data-24='5' data-25='5' data-26='5' data-27='5' data-28='5' data-29='5' data-30='5' data-31='5' data-32='5' data-33='5' data-34='5' data-35='5' data-36='5' data-37='5' data-38='5' data-39='5' data-40='5' data-41='5' data-42='5' data-43='5' data-44='5' data-45='5' data-46='5' data-47='5' data-48='5' data-49='5' data-50='5' data-51='5' data-52='5' data-53='5' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setAllMessagesRead

把所有消息设置为已读，更新未读消息数

`- (BMXErrorCode)setAllMessagesRead`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setAllMessagesReadWithCompletion:

把所有消息设置为已读，更新未读消息数

`- (void)setAllMessagesReadWithCompletion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setEditMessage:

设置编辑消息

`- (BMXErrorCode)setEditMessage:(NSString *)*editMessage*`

#### Parameters

_editMessage_\
会话正在编辑的文本消息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setExtension:

设置扩展信息

`- (BMXErrorCode)setExtension:(NSString *)*ext*`

#### Parameters

_ext_\
会话扩展消息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setMessagePlayedStatus:status:

设置消息播放状态（只对语音/视频消息有效）

`- (BMXErrorCode)setMessagePlayedStatus:(BMXMessage *)*msg* status:(BOOL)*status*`

#### Parameters

_msg_\
需要设置播放状态的消息

_status_\
消息是否已经播放

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setMessagePlayedStatus:status:completion:

设置消息播放状态（只对语音/视频消息有效）

`- (void)setMessagePlayedStatus:(BMXMessage *)*msg* status:(BOOL)*status* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
需要设置播放状态的消息

_status_\
消息是否已经播放

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setMessageReadStatus:status:

设置消息未读状态，更新未读消息数

`- (BMXErrorCode)setMessageReadStatus:(BMXMessage *)*msg* status:(BOOL)*status*`

#### Parameters

_msg_\
需要设置消息已读状态的消息

_status_\
消息是否设置已读

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### setMessageReadStatus:status:completion:

设置消息未读状态，更新未读消息数

`- (void)setMessageReadStatus:(BMXMessage *)*msg* status:(BOOL)*status* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
需要设置消息已读状态的消息

_status_\
消息是否设置已读

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### type

会话类型

`- (BMXConversation_Type)type`

#### Return Value

[BMXConversation\_Type](../Constants/BMXConversation_Type.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### unreadNumber

未读消息数

`- (int)unreadNumber`

#### Return Value

int

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### updateMessageExtensionWithMsg:

更新一条数据库存储消息的扩展字段信息

`- (BMXErrorCode)updateMessageExtensionWithMsg:(BMXMessage *)*msg*`

#### Parameters

_msg_\
需要更改扩展信息的消息此时msg部分已经更新扩展字椴信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>

```

### updateMessageExtensionWithMsg:completion:

更新一条数据库存储消息的扩展字段信息

`- (void)updateMessageExtensionWithMsg:(BMXMessage *)*msg* completion:(void ( ^ ) ( BMXError *aError ))*resBlock*`

#### Parameters

_msg_\
需要更改扩展信息的消息此时msg部分已经更新扩展字椴信息

#### Return Value

[BMXErrorCode](../Constants/BMXErrorCode.md)

#### Declared In

* `floo_proxy.h`

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-ios' data-class='BMXConversation'></div>
```
