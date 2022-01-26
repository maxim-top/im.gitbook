---
title: im::floo::floolib::BMXFileAttachment
summary: 消息文件附件 

---

# im::floo::floolib::BMXFileAttachment



消息文件附件 

Inherits from [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

Inherited by [im.floo.floolib.BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md), [im.floo.floolib.BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md), [im.floo.floolib.BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-delete)**() |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String path, String displayName)<br>构造函数，构建发送文件消息附件  |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String path) |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String ratelUrl, String displayName, long fileLength)<br>构造函数，构建接收文件消息附件  |
| BMXMessageAttachment.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-type)**()<br>返回文件类型  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[clone](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-clone)**()<br>克隆函数  |
| String | **[path](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-path)**()<br>本地路径  |
| String | **[displayName](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-displayname)**()<br>显示名  |
| String | **[ratelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-ratelurl)**() |
| String | **[url](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-url)**()<br>远程URL  |
| long | **[fileLength](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-filelength)**()<br>文件长度  |
| BMXMessageAttachment.DownloadStatus | **[downloadStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-downloadstatus)**()<br>附件下载状态  |
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

构造函数，构建发送文件消息附件 

**Parameters**: 

  * **path** 文件的本地路径 
  * **displayName** 文件展示名 


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

构造函数，构建接收文件消息附件 

**Parameters**: 

  * **ratelUrl** ratel服务器地址 
  * **displayName** 文件展示名 
  * **fileLength** 文件大小 


### function type

```java
inline BMXMessageAttachment.Type type()
```

返回文件类型 

**Return**: Type 

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-type)


**Reimplemented by**: [im::floo::floolib::BMXImageAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-type), [im::floo::floolib::BMXVideoAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-type), [im::floo::floolib::BMXVoiceAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-type)


### function clone

```java
inline BMXMessageAttachment clone()
```

克隆函数 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-clone)


**Reimplemented by**: [im::floo::floolib::BMXImageAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-clone), [im::floo::floolib::BMXVideoAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-clone), [im::floo::floolib::BMXVoiceAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-clone)


### function path

```java
inline String path()
```

本地路径 

**Return**: std::string 

### function displayName

```java
inline String displayName()
```

显示名 

**Return**: std::string 

### function ratelUrl

```java
inline String ratelUrl()
```


### function url

```java
inline String url()
```

远程URL 

**Return**: std::string 

### function fileLength

```java
inline long fileLength()
```

文件长度 

**Return**: std::string 

### function downloadStatus

```java
inline BMXMessageAttachment.DownloadStatus downloadStatus()
```

附件下载状态 

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