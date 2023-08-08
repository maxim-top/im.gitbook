---
title: floo::BMXChatServiceListener
summary: 聊天监听者
---

# floo::BMXChatServiceListener

聊天监听者

`#include <bmx_chat_service_listener.h>`

## Public Functions

|              | Name                                                                                                                                                                                                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-bmxchatservicelistener"><strong>BMXChatServiceListener</strong></a>()<br>构造函数</p>                                                                                                                      |
| virtual      | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-~bmxchatservicelistener"><strong>~BMXChatServiceListener</strong></a>()<br>析构函数</p>                                                                                                                    |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onstatuschanged"><strong>onStatusChanged</strong></a>(BMXMessagePtr msg, BMXErrorCode error)<br>消息发送状态发生变化</p>                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentuploadprogresschanged"><strong>onAttachmentUploadProgressChanged</strong></a>(BMXMessagePtr msg, int percent)<br>附件上传进度发送变化</p>                                                            |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onrecallstatuschanged"><strong>onRecallStatusChanged</strong></a>(BMXMessagePtr msg, BMXErrorCode error)<br>消息撤回状态发送变化</p>                                                                             |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceive"><strong>onReceive</strong></a>(const BMXMessageList &#x26; list)<br>收到消息</p>                                                                                                                |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivecommandmessages"><strong>onReceiveCommandMessages</strong></a>(const BMXMessageList &#x26; list)<br>收到命令消息</p>                                                                                |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivesystemmessages"><strong>onReceiveSystemMessages</strong></a>(const BMXMessageList &#x26; list)<br>收到系统通知消息</p>                                                                                |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadacks"><strong>onReceiveReadAcks</strong></a>(const BMXMessageList &#x26; list)<br>收到消息已读回执</p>                                                                                            |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivedeliveracks"><strong>onReceiveDeliverAcks</strong></a>(const BMXMessageList &#x26; list)<br>收到消息已送达回执</p>                                                                                     |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceiverecallmessages"><strong>onReceiveRecallMessages</strong></a>(const BMXMessageList &#x26; list)<br>收到撤回消息</p>                                                                                  |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadcancels"><strong>onReceiveReadCancels</strong></a>(const BMXMessageList &#x26; list)<br>收到消息已读取消（多设备其他设备同步消息已读状态变为未读）</p>                                                                 |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivereadallmessages"><strong>onReceiveReadAllMessages</strong></a>(const BMXMessageList &#x26; list)<br>收到消息全部已读（多设备同步某消息之前消息全部设置为已读）</p>                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceivedeletemessages"><strong>onReceiveDeleteMessages</strong></a>(const BMXMessageList &#x26; list)<br>收到删除消息 （多设备同步删除消息）</p>                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onreceiveplayacks"><strong>onReceivePlayAcks</strong></a>(const BMXMessageList &#x26; list)<br>收到音频/视频消息已播放回执</p>                                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentstatuschanged"><strong>onAttachmentStatusChanged</strong></a>(BMXMessagePtr msg, BMXErrorCode error, int percent)<br>附件下载状态发生变化</p>                                                        |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onattachmentdownloadbyurlstatuschanged"><strong>onAttachmentDownloadByUrlStatusChanged</strong></a>(int64_t msgId, BMXErrorCode error, int percent)<br>附件下载状态发生变化</p>                                  |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onretrievehistorymessages"><strong>onRetrieveHistoryMessages</strong></a>(BMXConversationPtr conversation)<br>拉取历史消息</p>                                                                               |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onloadallconversation"><strong>onLoadAllConversation</strong></a>()<br>已经加载完未读会话列表</p>                                                                                                                 |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onconversationcreate"><strong>onConversationCreate</strong></a>(BMXConversationPtr conversation, BMXMessagePtr msg)<br>本地创建新会话</p>                                                                     |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-onconversationdelete"><strong>onConversationDelete</strong></a>(int64_t conversationId, BMXErrorCode error)<br>删除会话</p>                                                                                |
| virtual void | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-ontotalunreadcountchanged"><strong>onTotalUnreadCountChanged</strong></a>(int unreadCount)<br>更新总未读数</p>                                                                                               |
| void         | <p><a href="classfloo_1_1_b_m_x_chat_service_listener.md#function-registerchatservice"><strong>registerChatService</strong></a>(<a href="classfloo_1_1_b_m_x_chat_service.md">BMXChatService</a> * service)<br>注册BMXChatServiceListener绑定到的BMXChatService（SDK内部自动注册）</p> |

## Protected Attributes

|                                                                 | Name                                                                                   |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [BMXChatService](classfloo\_1\_1\_b\_m\_x\_chat\_service.md) \* | [**mService**](classfloo\_1\_1\_b\_m\_x\_chat\_service\_listener.md#variable-mservice) |

## Public Functions Documentation

### function BMXChatServiceListener

```cpp
inline BMXChatServiceListener()
```

构造函数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function \~BMXChatServiceListener

```cpp
inline virtual ~BMXChatServiceListener()
```

析构函数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onStatusChanged

```cpp
inline virtual void onStatusChanged(
    BMXMessagePtr msg,
    BMXErrorCode error
)
```

消息发送状态发生变化

**Parameters**:

* **msg** 发生状态变化的消息
* **error** 状态错误码

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onAttachmentUploadProgressChanged

```cpp
inline virtual void onAttachmentUploadProgressChanged(
    BMXMessagePtr msg,
    int percent
)
```

附件上传进度发送变化

**Parameters**:

* **msg** 上传附件的消息
* **percent** 附件上传的进度

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onRecallStatusChanged

```cpp
inline virtual void onRecallStatusChanged(
    BMXMessagePtr msg,
    BMXErrorCode error
)
```

消息撤回状态发送变化

**Parameters**:

* **msg** 撤回状态发生变化的消息
* **error** 状态错误码

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onReceive

```cpp
inline virtual void onReceive(
    const BMXMessageList & list
)
```

收到消息

**Parameters**:

* **list** 接收到的消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onReceiveCommandMessages

```cpp
inline virtual void onReceiveCommandMessages(
    const BMXMessageList & list
)
```

收到命令消息

**Parameters**:

* **list** 接收到的消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onReceiveSystemMessages

```cpp
inline virtual void onReceiveSystemMessages(
    const BMXMessageList & list
)
```

收到系统通知消息

**Parameters**:

* **list** 接收到的系统消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onReceiveReadAcks

```cpp
inline virtual void onReceiveReadAcks(
    const BMXMessageList & list
)
```

收到消息已读回执

**Parameters**:

* **list** 接收到的已读回执消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onReceiveDeliverAcks

```cpp
inline virtual void onReceiveDeliverAcks(
    const BMXMessageList & list
)
```

收到消息已送达回执

**Parameters**:

* **list** 接收到的已送达回执消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onReceiveRecallMessages

```cpp
inline virtual void onReceiveRecallMessages(
    const BMXMessageList & list
)
```

收到撤回消息

**Parameters**:

* **list** 接收到的撤回消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onReceiveReadCancels

```cpp
inline virtual void onReceiveReadCancels(
    const BMXMessageList & list
)
```

收到消息已读取消（多设备其他设备同步消息已读状态变为未读）

**Parameters**:

* **list** 接收到的消息已读取消消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onReceiveReadAllMessages

```cpp
inline virtual void onReceiveReadAllMessages(
    const BMXMessageList & list
)
```

收到消息全部已读（多设备同步某消息之前消息全部设置为已读）

**Parameters**:

* **list** 接收到的消息全部已读消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onReceiveDeleteMessages

```cpp
inline virtual void onReceiveDeleteMessages(
    const BMXMessageList & list
)
```

收到删除消息 （多设备同步删除消息）

**Parameters**:

* **list** 接收到的删除消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onReceivePlayAcks

```cpp
inline virtual void onReceivePlayAcks(
    const BMXMessageList & list
)
```

收到音频/视频消息已播放回执

**Parameters**:

* **list** 接收到的音频/视频消息已播放回执消息列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onAttachmentStatusChanged

```cpp
inline virtual void onAttachmentStatusChanged(
    BMXMessagePtr msg,
    BMXErrorCode error,
    int percent
)
```

附件下载状态发生变化

**Parameters**:

* **msg** 发生下载状态变化的消息
* **error** 状态错误码
* **percent** 附件下载的进度

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onAttachmentDownloadByUrlStatusChanged

```cpp
inline virtual void onAttachmentDownloadByUrlStatusChanged(
    int64_t msgId,
    BMXErrorCode error,
    int percent
)
```

附件下载状态发生变化

**Parameters**:

* **msgId** 发生下载状态变化的消息Id
* **error** 状态错误码
* **percent** 附件下载的进度

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onRetrieveHistoryMessages

```cpp
inline virtual void onRetrieveHistoryMessages(
    BMXConversationPtr conversation
)
```

拉取历史消息

**Parameters**:

* **conversation** 发生了拉取指历史消息的会话

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onLoadAllConversation

```cpp
inline virtual void onLoadAllConversation()
```

已经加载完未读会话列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onConversationCreate

```cpp
inline virtual void onConversationCreate(
    BMXConversationPtr conversation,
    BMXMessagePtr msg
)
```

本地创建新会话

**Parameters**:

* **conversation** 新创建的本地会话
* **msg** 会话的最新消息，存在返回不存在返回为空

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onConversationDelete

```cpp
inline virtual void onConversationDelete(
    int64_t conversationId,
    BMXErrorCode error
)
```

删除会话

**Parameters**:

* **conversationId** 删除的本地会话id
* **error** 状态错误码

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function onTotalUnreadCountChanged

```cpp
inline virtual void onTotalUnreadCountChanged(
    int unreadCount
)
```

更新总未读数

**Parameters**:

* **unreadCount** 本地全部会话未读总数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```

### function registerChatService

```cpp
inline void registerChatService(
    BMXChatService * service
)
```

注册BMXChatServiceListener绑定到的BMXChatService（SDK内部自动注册）

**Parameters**:

* **service** [BMXChatService](classfloo\_1\_1\_b\_m\_x\_chat\_service.md)

## Protected Attributes Documentation

### variable mService

```cpp
BMXChatService * mService;
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXChatServiceListener'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
