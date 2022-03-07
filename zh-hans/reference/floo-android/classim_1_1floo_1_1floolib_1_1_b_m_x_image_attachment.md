---
title: im::floo::floolib::BMXImageAttachment
summary: 图片消息附件 

---

# im::floo::floolib::BMXImageAttachment



图片消息附件 

Inherits from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md), [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-delete)**() |
| | **[BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment)**(String path, BMXMessageAttachment.Size size, String displayName)<br>构造函数，构建发送图片消息附件  |
| | **[BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment)**(String path, BMXMessageAttachment.Size size) |
| | **[BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment)**(String ratelUrl, BMXMessageAttachment.Size size, String displayName, long fileLength)<br>构造函数，构建接收图片消息附件  |
| BMXMessageAttachment.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-type)**()<br>返回图片附件类型  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[clone](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-clone)**()<br>克隆函数  |
| BMXMessageAttachment.Size | **[size](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-size)**()<br>图片大小  |
| String | **[thumbnailUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-thumbnailurl)**() |
| void | **[setThumbnail](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-setthumbnail)**(String path)<br>设置发送图片消息缩略图  |
| String | **[thumbnailPath](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-thumbnailpath)**()<br>缩略图本地路径  |
| BMXMessageAttachment.DownloadStatus | **[thumbnailDownloadStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-thumbnaildownloadstatus)**()<br>缩略图下载状态  |
| [BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md) | **[dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-dynamic-cast)**([BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-getcptr)**([BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md) obj) |

## Additional inherited members

**Public Functions inherited from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String path, String displayName)<br>构造函数，构建发送文件消息附件  |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String path) |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String ratelUrl, String displayName, long fileLength)<br>构造函数，构建接收文件消息附件  |
| String | **[path](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-path)**()<br>本地路径  |
| String | **[displayName](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-displayname)**()<br>显示名  |
| String | **[ratelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-ratelurl)**() |
| String | **[url](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-url)**()<br>远程URL  |
| long | **[fileLength](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-filelength)**()<br>文件长度  |
| BMXMessageAttachment.DownloadStatus | **[downloadStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-downloadstatus)**()<br>附件下载状态  |

**Protected Functions inherited from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(long cPtr, boolean cMemoryOwn) |

**Protected Functions inherited from [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**(long cPtr, boolean cMemoryOwn) |


## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


**Reimplements**: [im::floo::floolib::BMXFileAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-delete)


### function BMXImageAttachment

```java
inline BMXImageAttachment(
    String path,
    BMXMessageAttachment.Size size,
    String displayName
)
```

构造函数，构建发送图片消息附件 

**Parameters**: 

  * **path** 本地路径 
  * **size** 图片的大小，宽度和高度 
  * **displayName** 展示名 


### function BMXImageAttachment

```java
inline BMXImageAttachment(
    String path,
    BMXMessageAttachment.Size size
)
```


### function BMXImageAttachment

```java
inline BMXImageAttachment(
    String ratelUrl,
    BMXMessageAttachment.Size size,
    String displayName,
    long fileLength
)
```

构造函数，构建接收图片消息附件 

**Parameters**: 

  * **ratelUrl** ratel服务器地址 
  * **size** 图片的大小，宽度和高度 
  * **displayName** 展示名 
  * **fileLength** 文件大小 


### function type

```java
inline BMXMessageAttachment.Type type()
```

返回图片附件类型 

**Return**: Type 

**Reimplements**: [im::floo::floolib::BMXFileAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-type)


### function clone

```java
inline BMXMessageAttachment clone()
```

克隆函数 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [im::floo::floolib::BMXFileAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-clone)


### function size

```java
inline BMXMessageAttachment.Size size()
```

图片大小 

**Return**: Size 

### function thumbnailUrl

```java
inline String thumbnailUrl()
```


### function setThumbnail

```java
inline void setThumbnail(
    String path
)
```

设置发送图片消息缩略图 

**Parameters**: 

  * **path** 本地路径 


### function thumbnailPath

```java
inline String thumbnailPath()
```

缩略图本地路径 

**Return**: std::string 

### function thumbnailDownloadStatus

```java
inline BMXMessageAttachment.DownloadStatus thumbnailDownloadStatus()
```

缩略图下载状态 

**Return**: DownloadStatus 

### function dynamic_cast

```java
static inline BMXImageAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```


**Reimplements**: [im::floo::floolib::BMXFileAttachment::dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-dynamic-cast)


## Protected Functions Documentation

### function BMXImageAttachment

```java
inline BMXImageAttachment(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


**Reimplements**: [im::floo::floolib::BMXFileAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-finalize)


### function getCPtr

```java
static inline long getCPtr(
    BMXImageAttachment obj
)
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800