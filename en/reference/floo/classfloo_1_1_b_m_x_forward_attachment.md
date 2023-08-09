---
title: floo::BMXForwardAttachment
summary: Forwarded attachment in message 

---

# floo::BMXForwardAttachment



Forwarded attachment in message 


`#include <bmx_forward_attachment.h>`

Inherits from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Message](classfloo_1_1_b_m_x_forward_attachment_1_1_message.md)** <br>Custom message to forward attachment  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXForwardAttachment](classfloo_1_1_b_m_x_forward_attachment.md#function-bmxforwardattachment)**()<br>Constructor  |
| virtual | **[~BMXForwardAttachment](classfloo_1_1_b_m_x_forward_attachment.md#function-~bmxforwardattachment)**()<br>Destructor  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_forward_attachment.md#function-type)**() const<br>Attachment type  |
| virtual BMXMessageAttachmentPtr | **[clone](classfloo_1_1_b_m_x_forward_attachment.md#function-clone)**() const<br>Cloning function  |

## Additional inherited members

**Public Types inherited from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| enum class| **[Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type)** { Image, Voice, Video, File, Location, Command, Forward}<br>Attachment type  |
| enum class| **[DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus)** { Downloaing, Successed, Failed, NotStart, Canceled}<br>Attachment download state  |

**Public Functions inherited from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**()<br>Constructor  |
| virtual | **[~BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment)**()<br>Destructor  |


## Public Functions Documentation

### function BMXForwardAttachment

```cpp
inline BMXForwardAttachment()
```

Constructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXForwardAttachment",function="BMXForwardAttachment" %}{% endlanying_code_snippet %}
```
### function ~BMXForwardAttachment

```cpp
inline virtual ~BMXForwardAttachment()
```

Destructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXForwardAttachment",function="~BMXForwardAttachment" %}{% endlanying_code_snippet %}
```
### function type

```cpp
inline virtual Type type() const
```

Attachment type 

**Return**: Type 

**Reimplements**: [floo::BMXMessageAttachment::type](classfloo_1_1_b_m_x_message_attachment.md#function-type)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXForwardAttachment",function="type" %}{% endlanying_code_snippet %}
```
### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

Cloning function 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [floo::BMXMessageAttachment::clone](classfloo_1_1_b_m_x_message_attachment.md#function-clone)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXForwardAttachment",function="clone" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800