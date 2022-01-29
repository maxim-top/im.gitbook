---
title: floo::BMXMessageAttachment
summary: 消息附件 

---

# floo::BMXMessageAttachment



消息附件 


`#include <bmx_message_attachment.h>`

Inherits from BMXBaseObject

Inherited by [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md), [floo::BMXForwardAttachment](classfloo_1_1_b_m_x_forward_attachment.md), [floo::BMXLocationAttachment](classfloo_1_1_b_m_x_location_attachment.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type)** { Image = 1, Voice, Video, File, Location, Command, Forward}<br>附件类型  |
| enum class| **[DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus)** { Downloaing, Successed, Failed, NotStart, Canceled}<br>附件下载状态  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**()<br>构造函数  |
| virtual | **[~BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment)**()<br>析构函数  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_message_attachment.md#function-type)**() const =0<br>附件类型  |
| virtual std::shared_ptr< [BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md) > | **[clone](classfloo_1_1_b_m_x_message_attachment.md#function-clone)**() const =0<br>复制附件  |

## Public Types Documentation

### enum Type

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Image | 1| 图片   |
| Voice | | 语音   |
| Video | | 视频片段   |
| File | | 文件   |
| Location | | 位置   |
| Command | | 命令消息   |
| Forward | | 转发消息   |



附件类型 

### enum DownloadStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Downloaing | | 下载中   |
| Successed | | 下载成功   |
| Failed | | 下载失败   |
| NotStart | | 下载尚未开始   |
| Canceled | | 下载被取消   |



附件下载状态 

## Public Functions Documentation

### function BMXMessageAttachment

```cpp
inline BMXMessageAttachment()
```

构造函数 

### function ~BMXMessageAttachment

```cpp
inline virtual ~BMXMessageAttachment()
```

析构函数 

### function type

```cpp
virtual Type type() const =0
```

附件类型 

**Return**: Type 

**Reimplemented by**: [floo::BMXFileAttachment::type](classfloo_1_1_b_m_x_file_attachment.md#function-type), [floo::BMXForwardAttachment::type](classfloo_1_1_b_m_x_forward_attachment.md#function-type), [floo::BMXImageAttachment::type](classfloo_1_1_b_m_x_image_attachment.md#function-type), [floo::BMXLocationAttachment::type](classfloo_1_1_b_m_x_location_attachment.md#function-type), [floo::BMXVideoAttachment::type](classfloo_1_1_b_m_x_video_attachment.md#function-type), [floo::BMXVoiceAttachment::type](classfloo_1_1_b_m_x_voice_attachment.md#function-type)


### function clone

```cpp
virtual std::shared_ptr< BMXMessageAttachment > clone() const =0
```

复制附件 

**Return**: BMXMessageAttachmentPtr 

**Reimplemented by**: [floo::BMXFileAttachment::clone](classfloo_1_1_b_m_x_file_attachment.md#function-clone), [floo::BMXForwardAttachment::clone](classfloo_1_1_b_m_x_forward_attachment.md#function-clone), [floo::BMXImageAttachment::clone](classfloo_1_1_b_m_x_image_attachment.md#function-clone), [floo::BMXLocationAttachment::clone](classfloo_1_1_b_m_x_location_attachment.md#function-clone), [floo::BMXVideoAttachment::clone](classfloo_1_1_b_m_x_video_attachment.md#function-clone), [floo::BMXVoiceAttachment::clone](classfloo_1_1_b_m_x_voice_attachment.md#function-clone)


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800