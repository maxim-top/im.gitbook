---
title: floo::BMXMessageAttachment
summary: Message attachment
---

# floo::BMXMessageAttachment

Message attachment

`#include <bmx_message_attachment.h>`

Inherits from BMXBaseObject

Inherited by [floo::BMXFileAttachment](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md), [floo::BMXForwardAttachment](classfloo\_1\_1\_b\_m\_x\_forward\_attachment.md), [floo::BMXLocationAttachment](classfloo\_1\_1\_b\_m\_x\_location\_attachment.md)

## Public Types

|            | Name                                                                                                                                                                                                 |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-type"><strong>Type</strong></a> { Image = 1, Voice, Video, File, Location, Command, Forward}<br>Attachment type</p>                       |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus"><strong>DownloadStatus</strong></a> { Downloaing, Successed, Failed, NotStart, Canceled}<br>Attachment download state</p> |

## Public Functions

|                                                                                                      | Name                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                      | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment"><strong>BMXMessageAttachment</strong></a>()<br>Constructor</p>  |
| virtual                                                                                              | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment"><strong>~BMXMessageAttachment</strong></a>()<br>Destructor</p> |
| virtual [Type](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#enum-type)                           | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-type"><strong>type</strong></a>() const =0<br>Attachment type</p>                     |
| virtual std::shared\_ptr< [BMXMessageAttachment](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md) > | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-clone"><strong>clone</strong></a>() const =0<br>Copy attachment</p>                   |

## Public Types Documentation

### enum Type

| Enumerator | Value | Description     |
| ---------- | ----- | --------------- |
| Image      | 1     | Image           |
| Voice      |       | Voice           |
| Video      |       | Video clip      |
| File       |       | File            |
| Location   |       | Location        |
| Command    |       | Command message |
| Forward    |       | Forward message |

Attachment type

### enum DownloadStatus

| Enumerator | Value | Description                  |
| ---------- | ----- | ---------------------------- |
| Downloaing |       | Downloading                  |
| Successed  |       | Download succeeded           |
| Failed     |       | Download failed              |
| NotStart   |       | Download has net started yet |
| Canceled   |       | Download canceled            |

Attachment download state

## Public Functions Documentation

### function BMXMessageAttachment

```cpp
inline BMXMessageAttachment()
```

Constructor

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageAttachment'></div>
```

### function \~BMXMessageAttachment

```cpp
inline virtual ~BMXMessageAttachment()
```

Destructor

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageAttachment'></div>
```

### function type

```cpp
virtual Type type() const =0
```

Attachment type

**Return**: Type

**Reimplemented by**: [floo::BMXFileAttachment::type](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#function-type), [floo::BMXForwardAttachment::type](classfloo\_1\_1\_b\_m\_x\_forward\_attachment.md#function-type), [floo::BMXImageAttachment::type](classfloo\_1\_1\_b\_m\_x\_image\_attachment.md#function-type), [floo::BMXLocationAttachment::type](classfloo\_1\_1\_b\_m\_x\_location\_attachment.md#function-type), [floo::BMXVideoAttachment::type](classfloo\_1\_1\_b\_m\_x\_video\_attachment.md#function-type), [floo::BMXVoiceAttachment::type](classfloo\_1\_1\_b\_m\_x\_voice\_attachment.md#function-type)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageAttachment'></div>
```

### function clone

```cpp
virtual std::shared_ptr< BMXMessageAttachment > clone() const =0
```

Copy attachment

**Return**: BMXMessageAttachmentPtr

**Reimplemented by**: [floo::BMXFileAttachment::clone](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#function-clone), [floo::BMXForwardAttachment::clone](classfloo\_1\_1\_b\_m\_x\_forward\_attachment.md#function-clone), [floo::BMXImageAttachment::clone](classfloo\_1\_1\_b\_m\_x\_image\_attachment.md#function-clone), [floo::BMXLocationAttachment::clone](classfloo\_1\_1\_b\_m\_x\_location\_attachment.md#function-clone), [floo::BMXVideoAttachment::clone](classfloo\_1\_1\_b\_m\_x\_video\_attachment.md#function-clone), [floo::BMXVoiceAttachment::clone](classfloo\_1\_1\_b\_m\_x\_voice\_attachment.md#function-clone)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageAttachment'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
