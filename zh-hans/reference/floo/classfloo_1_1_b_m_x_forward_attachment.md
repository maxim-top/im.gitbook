---
title: floo::BMXForwardAttachment
summary: 消息转发附件 

---

# floo::BMXForwardAttachment



消息转发附件 


`#include <bmx_forward_attachment.h>`

Inherits from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Message](classfloo_1_1_b_m_x_forward_attachment_1_1_message.md)** <br>转发消息附件自定义消息  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXForwardAttachment](classfloo_1_1_b_m_x_forward_attachment.md#function-bmxforwardattachment)**()<br>构造函数  |
| virtual | **[~BMXForwardAttachment](classfloo_1_1_b_m_x_forward_attachment.md#function-~bmxforwardattachment)**()<br>析构函数  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_forward_attachment.md#function-type)**() const<br>附件类型  |
| virtual BMXMessageAttachmentPtr | **[clone](classfloo_1_1_b_m_x_forward_attachment.md#function-clone)**() const<br>克隆函数  |

## Additional inherited members

**Public Types inherited from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| enum class| **[Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type)** { Image, Voice, Video, File, Location, Command, Forward}<br>附件类型  |
| enum class| **[DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus)** { Downloaing, Successed, Failed, NotStart, Canceled}<br>附件下载状态  |

**Public Functions inherited from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**()<br>构造函数  |
| virtual | **[~BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment)**()<br>析构函数  |


## Public Functions Documentation

### function BMXForwardAttachment

```cpp
inline BMXForwardAttachment()
```

构造函数 

### function ~BMXForwardAttachment

```cpp
inline virtual ~BMXForwardAttachment()
```

析构函数 

### function type

```cpp
inline virtual Type type() const
```

附件类型 

**Return**: Type 

**Reimplements**: [floo::BMXMessageAttachment::type](classfloo_1_1_b_m_x_message_attachment.md#function-type)


### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

克隆函数 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [floo::BMXMessageAttachment::clone](classfloo_1_1_b_m_x_message_attachment.md#function-clone)


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800