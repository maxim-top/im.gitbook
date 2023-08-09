---
title: floo::BMXMessageAttachment
summary: Message attachment 

---

# floo::BMXMessageAttachment



Message attachment 


`#include <bmx_message_attachment.h>`

Inherits from BMXBaseObject

Inherited by [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md), [floo::BMXForwardAttachment](classfloo_1_1_b_m_x_forward_attachment.md), [floo::BMXLocationAttachment](classfloo_1_1_b_m_x_location_attachment.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type)** { Image = 1, Voice, Video, File, Location, Command, Forward}<br>Attachment type  |
| enum class| **[DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus)** { Downloaing, Successed, Failed, NotStart, Canceled}<br>Attachment download state  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**()<br>Constructor  |
| virtual | **[~BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment)**()<br>Destructor  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_message_attachment.md#function-type)**() const =0<br>Attachment type  |
| virtual std::shared_ptr< [BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md) > | **[clone](classfloo_1_1_b_m_x_message_attachment.md#function-clone)**() const =0<br>Copy attachment  |

## Public Types Documentation

### enum Type

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Image | 1| Image   |
| Voice | | Voice   |
| Video | | Video clip   |
| File | | File   |
| Location | | Location   |
| Command | | Command message   |
| Forward | | Forward message   |



Attachment type 

### enum DownloadStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Downloaing | | Downloading   |
| Successed | | Download succeeded   |
| Failed | | Download failed   |
| NotStart | | Download has net started yet   |
| Canceled | | Download canceled   |



Attachment download state 

## Public Functions Documentation

### function BMXMessageAttachment

```cpp
inline BMXMessageAttachment()
```

Constructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageAttachment",function="BMXMessageAttachment" %}{% endlanying_code_snippet %}
```
### function ~BMXMessageAttachment

```cpp
inline virtual ~BMXMessageAttachment()
```

Destructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageAttachment",function="~BMXMessageAttachment" %}{% endlanying_code_snippet %}
```
### function type

```cpp
virtual Type type() const =0
```

Attachment type 

**Return**: Type 

**Reimplemented by**: [floo::BMXFileAttachment::type](classfloo_1_1_b_m_x_file_attachment.md#function-type), [floo::BMXForwardAttachment::type](classfloo_1_1_b_m_x_forward_attachment.md#function-type), [floo::BMXImageAttachment::type](classfloo_1_1_b_m_x_image_attachment.md#function-type), [floo::BMXLocationAttachment::type](classfloo_1_1_b_m_x_location_attachment.md#function-type), [floo::BMXVideoAttachment::type](classfloo_1_1_b_m_x_video_attachment.md#function-type), [floo::BMXVoiceAttachment::type](classfloo_1_1_b_m_x_voice_attachment.md#function-type)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageAttachment",function="type" %}{% endlanying_code_snippet %}
```
### function clone

```cpp
virtual std::shared_ptr< BMXMessageAttachment > clone() const =0
```

Copy attachment 

**Return**: BMXMessageAttachmentPtr 

**Reimplemented by**: [floo::BMXFileAttachment::clone](classfloo_1_1_b_m_x_file_attachment.md#function-clone), [floo::BMXForwardAttachment::clone](classfloo_1_1_b_m_x_forward_attachment.md#function-clone), [floo::BMXImageAttachment::clone](classfloo_1_1_b_m_x_image_attachment.md#function-clone), [floo::BMXLocationAttachment::clone](classfloo_1_1_b_m_x_location_attachment.md#function-clone), [floo::BMXVideoAttachment::clone](classfloo_1_1_b_m_x_video_attachment.md#function-clone), [floo::BMXVoiceAttachment::clone](classfloo_1_1_b_m_x_voice_attachment.md#function-clone)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageAttachment",function="clone" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800