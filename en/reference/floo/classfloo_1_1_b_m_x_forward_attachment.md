---
title: floo::BMXForwardAttachment
summary: Forwarded attachment in message
---

# floo::BMXForwardAttachment

Forwarded attachment in message

`#include <bmx_forward_attachment.h>`

Inherits from [floo::BMXMessageAttachment](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md), BMXBaseObject

## Public Classes

|       | Name                                                                                                                                        |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| class | <p><a href="classfloo_1_1_b_m_x_forward_attachment_1_1_message.md"><strong>Message</strong></a><br>Custom message to forward attachment</p> |

## Public Functions

|                                                                            | Name                                                                                                                                                 |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                            | <p><a href="classfloo_1_1_b_m_x_forward_attachment.md#function-bmxforwardattachment"><strong>BMXForwardAttachment</strong></a>()<br>Constructor</p>  |
| virtual                                                                    | <p><a href="classfloo_1_1_b_m_x_forward_attachment.md#function-~bmxforwardattachment"><strong>~BMXForwardAttachment</strong></a>()<br>Destructor</p> |
| virtual [Type](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#enum-type) | <p><a href="classfloo_1_1_b_m_x_forward_attachment.md#function-type"><strong>type</strong></a>() const<br>Attachment type</p>                        |
| virtual BMXMessageAttachmentPtr                                            | <p><a href="classfloo_1_1_b_m_x_forward_attachment.md#function-clone"><strong>clone</strong></a>() const<br>Cloning function</p>                     |

## Additional inherited members

**Public Types inherited from** [**floo::BMXMessageAttachment**](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md)

|            | Name                                                                                                                                                                                                 |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-type"><strong>Type</strong></a> { Image, Voice, Video, File, Location, Command, Forward}<br>Attachment type</p>                           |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus"><strong>DownloadStatus</strong></a> { Downloaing, Successed, Failed, NotStart, Canceled}<br>Attachment download state</p> |

**Public Functions inherited from** [**floo::BMXMessageAttachment**](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md)

|         | Name                                                                                                                                                 |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|         | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment"><strong>BMXMessageAttachment</strong></a>()<br>Constructor</p>  |
| virtual | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment"><strong>~BMXMessageAttachment</strong></a>()<br>Destructor</p> |

## Public Functions Documentation

### function BMXForwardAttachment

```cpp
inline BMXForwardAttachment()
```

Constructor

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXForwardAttachment'></div>
```

### function \~BMXForwardAttachment

```cpp
inline virtual ~BMXForwardAttachment()
```

Destructor

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXForwardAttachment'></div>
```

### function type

```cpp
inline virtual Type type() const
```

Attachment type

**Return**: Type

**Reimplements**: [floo::BMXMessageAttachment::type](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#function-type)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXForwardAttachment'></div>
```

### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

Cloning function

**Return**: BMXMessageAttachmentPtr

**Reimplements**: [floo::BMXMessageAttachment::clone](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#function-clone)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXForwardAttachment'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
