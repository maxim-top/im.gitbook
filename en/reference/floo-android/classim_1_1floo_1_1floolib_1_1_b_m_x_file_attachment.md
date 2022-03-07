---
title: im::floo::floolib::BMXFileAttachment
summary: Message file attachment 

---

# im::floo::floolib::BMXFileAttachment



Message file attachment 

Inherits from [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

Inherited by [im.floo.floolib.BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md), [im.floo.floolib.BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md), [im.floo.floolib.BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-delete)**() |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String path, String displayName)<br>Constructor to build the message attachment of sent file  |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String path) |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String ratelUrl, String displayName, long fileLength)<br>Constructor to build the message attachment of received file  |
| BMXMessageAttachment.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-type)**()<br>Type of returned file  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[clone](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-clone)**()<br>Cloning function  |
| String | **[path](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-path)**()<br>Local path  |
| String | **[displayName](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-displayname)**()<br>Display name  |
| String | **[ratelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-ratelurl)**() |
| String | **[url](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-url)**()<br>Remote URL  |
| long | **[fileLength](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-filelength)**()<br>File length  |
| BMXMessageAttachment.DownloadStatus | **[downloadStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-downloadstatus)**()<br>Attachment download state  |
| [BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md) | **[dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-dynamic-cast)**([BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-getcptr)**([BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md) obj) |

## Additional inherited members

**Protected Functions inherited from [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**(long cPtr, boolean cMemoryOwn) |


## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


**Reimplements**: [im::floo::floolib::BMXMessageAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-delete)


**Reimplemented by**: [im::floo::floolib::BMXImageAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-delete), [im::floo::floolib::BMXVideoAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-delete), [im::floo::floolib::BMXVoiceAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-delete)


### function BMXFileAttachment

```java
inline BMXFileAttachment(
    String path,
    String displayName
)
```

Constructor to build the message attachment of sent file 

**Parameters**: 

  * **path** Local path of file 
  * **displayName** Display name of file 


### function BMXFileAttachment

```java
inline BMXFileAttachment(
    String path
)
```


### function BMXFileAttachment

```java
inline BMXFileAttachment(
    String ratelUrl,
    String displayName,
    long fileLength
)
```

Constructor to build the message attachment of received file 

**Parameters**: 

  * **ratelUrl** ratel server address 
  * **displayName** Display name of file 
  * **fileLength** File size 


### function type

```java
inline BMXMessageAttachment.Type type()
```

Type of returned file 

**Return**: Type 

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-type)


**Reimplemented by**: [im::floo::floolib::BMXImageAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-type), [im::floo::floolib::BMXVideoAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-type), [im::floo::floolib::BMXVoiceAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-type)


### function clone

```java
inline BMXMessageAttachment clone()
```

Cloning function 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-clone)


**Reimplemented by**: [im::floo::floolib::BMXImageAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-clone), [im::floo::floolib::BMXVideoAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-clone), [im::floo::floolib::BMXVoiceAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-clone)


### function path

```java
inline String path()
```

Local path 

**Return**: std::string 

### function displayName

```java
inline String displayName()
```

Display name 

**Return**: std::string 

### function ratelUrl

```java
inline String ratelUrl()
```


### function url

```java
inline String url()
```

Remote URL 

**Return**: std::string 

### function fileLength

```java
inline long fileLength()
```

File length 

**Return**: std::string 

### function downloadStatus

```java
inline BMXMessageAttachment.DownloadStatus downloadStatus()
```

Attachment download state 

**Return**: DownloadStatus 

### function dynamic_cast

```java
static inline BMXFileAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```


**Reimplemented by**: [im::floo::floolib::BMXImageAttachment::dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-dynamic-cast), [im::floo::floolib::BMXVideoAttachment::dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-dynamic-cast), [im::floo::floolib::BMXVoiceAttachment::dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-dynamic-cast)


## Protected Functions Documentation

### function BMXFileAttachment

```java
inline BMXFileAttachment(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


**Reimplements**: [im::floo::floolib::BMXMessageAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-finalize)


**Reimplemented by**: [im::floo::floolib::BMXImageAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-finalize), [im::floo::floolib::BMXVideoAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-finalize), [im::floo::floolib::BMXVoiceAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-finalize)


### function getCPtr

```java
static inline long getCPtr(
    BMXFileAttachment obj
)
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800