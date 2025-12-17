---
title: floo::BMXForwardAttachment
summary: 消息转发附件
---

# floo::BMXForwardAttachment

消息转发附件

`#include <bmx_forward_attachment.h>`

Inherits from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Classes

|       | Name                                                                                                               |
| ----- | ------------------------------------------------------------------------------------------------------------------ |
| class | <p><a href="classfloo_1_1_b_m_x_forward_attachment_1_1_message.md"><strong>Message</strong></a><br>转发消息附件自定义消息</p> |

## Public Functions

|                                                                     | Name                                                                                                                                           |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                     | <p><a href="classfloo_1_1_b_m_x_forward_attachment.md#function-bmxforwardattachment"><strong>BMXForwardAttachment</strong></a>()<br>构造函数</p>   |
| virtual                                                             | <p><a href="classfloo_1_1_b_m_x_forward_attachment.md#function-~bmxforwardattachment"><strong>~BMXForwardAttachment</strong></a>()<br>析构函数</p> |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | <p><a href="classfloo_1_1_b_m_x_forward_attachment.md#function-type"><strong>type</strong></a>() const<br>附件类型</p>                             |
| virtual BMXMessageAttachmentPtr                                     | <p><a href="classfloo_1_1_b_m_x_forward_attachment.md#function-clone"><strong>clone</strong></a>() const<br>克隆函数</p>                           |

## Additional inherited members

**Public Types inherited from** [**floo::BMXMessageAttachment**](classfloo_1_1_b_m_x_message_attachment.md)

|            | Name                                                                                                                                                                              |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-type"><strong>Type</strong></a> { Image, Voice, Video, File, Location, Command, Forward}<br>附件类型</p>                   |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus"><strong>DownloadStatus</strong></a> { Downloaing, Successed, Failed, NotStart, Canceled}<br>附件下载状态</p> |

**Public Functions inherited from** [**floo::BMXMessageAttachment**](classfloo_1_1_b_m_x_message_attachment.md)

|         | Name                                                                                                                                           |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|         | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment"><strong>BMXMessageAttachment</strong></a>()<br>构造函数</p>   |
| virtual | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment"><strong>~BMXMessageAttachment</strong></a>()<br>析构函数</p> |

## Public Functions Documentation

### function BMXForwardAttachment

```cpp
inline BMXForwardAttachment()
```

构造函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXForwardAttachment'></div>

```

### function \~BMXForwardAttachment

```cpp
inline virtual ~BMXForwardAttachment()
```

析构函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXForwardAttachment'></div>

```

### function type

```cpp
inline virtual Type type() const
```

附件类型

**Return**: Type

**Reimplements**: [floo::BMXMessageAttachment::type](classfloo_1_1_b_m_x_message_attachment.md#function-type)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXForwardAttachment'></div>

```

### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

克隆函数

**Return**: BMXMessageAttachmentPtr

**Reimplements**: [floo::BMXMessageAttachment::clone](classfloo_1_1_b_m_x_message_attachment.md#function-clone)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXForwardAttachment'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
