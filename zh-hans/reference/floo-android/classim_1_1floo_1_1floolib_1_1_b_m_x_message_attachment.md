---
title: im::floo::floolib::BMXMessageAttachment
summary: 消息附件 

---

# im::floo::floolib::BMXMessageAttachment



消息附件 

Inherits from BMXBaseObject

Inherited by [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md), [im.floo.floolib.BMXLocationAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-delete)**() |
| BMXMessageAttachment.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-type)**()<br>附件类型  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[clone](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-clone)**()<br>复制附件  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-getcptr)**([BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) obj) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


**Reimplemented by**: [im::floo::floolib::BMXFileAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-delete), [im::floo::floolib::BMXImageAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-delete), [im::floo::floolib::BMXLocationAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-delete), [im::floo::floolib::BMXVideoAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-delete), [im::floo::floolib::BMXVoiceAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-delete)


### function type

```java
inline BMXMessageAttachment.Type type()
```

附件类型 

**Return**: [Type]

**Reimplemented by**: [im::floo::floolib::BMXFileAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-type), [im::floo::floolib::BMXImageAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-type), [im::floo::floolib::BMXLocationAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-type), [im::floo::floolib::BMXVideoAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-type), [im::floo::floolib::BMXVoiceAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-type)


### function clone

```java
inline BMXMessageAttachment clone()
```

复制附件 

**Return**: BMXMessageAttachmentPtr 

**Reimplemented by**: [im::floo::floolib::BMXFileAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-clone), [im::floo::floolib::BMXImageAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-clone), [im::floo::floolib::BMXLocationAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-clone), [im::floo::floolib::BMXVideoAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-clone), [im::floo::floolib::BMXVoiceAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-clone)


## Protected Functions Documentation

### function BMXMessageAttachment

```java
inline BMXMessageAttachment(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


**Reimplemented by**: [im::floo::floolib::BMXFileAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-finalize), [im::floo::floolib::BMXImageAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-finalize), [im::floo::floolib::BMXLocationAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-finalize), [im::floo::floolib::BMXVideoAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-finalize), [im::floo::floolib::BMXVoiceAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-finalize)


### function getCPtr

```java
static inline long getCPtr(
    BMXMessageAttachment obj
)
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800