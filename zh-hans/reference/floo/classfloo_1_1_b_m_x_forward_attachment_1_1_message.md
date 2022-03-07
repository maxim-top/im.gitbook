---
title: floo::BMXForwardAttachment::Message
summary: 转发消息附件自定义消息 

---

# floo::BMXForwardAttachment::Message



转发消息附件自定义消息 


`#include <bmx_forward_attachment.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Message](classfloo_1_1_b_m_x_forward_attachment_1_1_message.md#function-message)**(std::shared_ptr< [BMXMessage](classfloo_1_1_b_m_x_message.md) > msg) |
| virtual | **[~Message](classfloo_1_1_b_m_x_forward_attachment_1_1_message.md#function-~message)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int64_t | **[msgId](classfloo_1_1_b_m_x_forward_attachment_1_1_message.md#variable-msgid)**  |
| int64_t | **[fromId](classfloo_1_1_b_m_x_forward_attachment_1_1_message.md#variable-fromid)**  |
| int64_t | **[clientTimestamp](classfloo_1_1_b_m_x_forward_attachment_1_1_message.md#variable-clienttimestamp)**  |
| int64_t | **[serverTimestamp](classfloo_1_1_b_m_x_forward_attachment_1_1_message.md#variable-servertimestamp)**  |
| std::string | **[content](classfloo_1_1_b_m_x_forward_attachment_1_1_message.md#variable-content)**  |
| [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[contentType](classfloo_1_1_b_m_x_forward_attachment_1_1_message.md#variable-contenttype)**  |
| BMXMessageAttachmentPtr | **[attachment](classfloo_1_1_b_m_x_forward_attachment_1_1_message.md#variable-attachment)**  |
| JSON | **[extension](classfloo_1_1_b_m_x_forward_attachment_1_1_message.md#variable-extension)**  |

## Public Functions Documentation

### function Message

```cpp
Message(
    std::shared_ptr< BMXMessage > msg
)
```


### function ~Message

```cpp
inline virtual ~Message()
```


## Public Attributes Documentation

### variable msgId

```cpp
int64_t msgId;
```


### variable fromId

```cpp
int64_t fromId;
```


### variable clientTimestamp

```cpp
int64_t clientTimestamp;
```


### variable serverTimestamp

```cpp
int64_t serverTimestamp;
```


### variable content

```cpp
std::string content;
```


### variable contentType

```cpp
Type contentType;
```


### variable attachment

```cpp
BMXMessageAttachmentPtr attachment;
```


### variable extension

```cpp
JSON extension;
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800