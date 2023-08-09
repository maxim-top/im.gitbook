---
title: im::floo::floolib::BMXVideoAttachment
summary: 视频消息附件 

---

# im::floo::floolib::BMXVideoAttachment



视频消息附件 

Inherits from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md), [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-delete)**() |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(String path, int duration, BMXMessageAttachment.Size size, String displayName)<br>构造函数，构建发送视频消息附件  |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(String path, int duration, BMXMessageAttachment.Size size) |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(String path, String thumbnailPath, int duration, BMXMessageAttachment.Size size, String displayName)<br>构造函数，构建发送视频消息附件  |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(String path, String thumbnailPath, int duration, BMXMessageAttachment.Size size) |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(String ratelUrl, int duration, BMXMessageAttachment.Size size, String displayName, long fileLength)<br>构造函数，构建接收视频消息附件  |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(String ratelUrl, String thumbnailUrl, int duration, BMXMessageAttachment.Size size, String displayName, long fileLength)<br>构造函数，构建接收视频消息附件  |
| BMXMessageAttachment.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-type)**()<br>返回文件类型  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[clone](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-clone)**()<br>克隆函数  |
| BMXMessageAttachment.Size | **[size](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-size)**()<br>视频大小，宽度和高度  |
| int | **[duration](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-duration)**()<br>视频片段时长  |
| void | **[setThumbnail](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-setthumbnail)**(String path)<br>设置发送视频片段消息缩略图  |
| String | **[thumbnailPath](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnailpath)**()<br>缩略图本地路径  |
| String | **[thumbnailUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnailurl)**()<br>缩略图服务器路径  |
| void | **[setThumbnailRatelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-setthumbnailratelurl)**(String thumbnailRatelUrl) |
| String | **[thumbnailRatelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnailratelurl)**() |
| BMXMessageAttachment.DownloadStatus | **[thumbnailDownloadStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnaildownloadstatus)**()<br>缩略图下载状态  |
| [BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md) | **[dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-dynamic-cast)**([BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-getcptr)**([BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md) obj) |

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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="delete" %}{% endlanying_code_snippet %}
```
### function BMXVideoAttachment

```java
inline BMXVideoAttachment(
    String path,
    int duration,
    BMXMessageAttachment.Size size,
    String displayName
)
```

构造函数，构建发送视频消息附件 

**Parameters**: 

  * **path** 文件的本地路径 
  * **duration** 视频片段时长 
  * **size** 视频大小，宽度和高度 
  * **displayName** 文件展示名 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="BMXVideoAttachment" %}{% endlanying_code_snippet %}
```
### function BMXVideoAttachment

```java
inline BMXVideoAttachment(
    String path,
    int duration,
    BMXMessageAttachment.Size size
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="BMXVideoAttachment" %}{% endlanying_code_snippet %}
```
### function BMXVideoAttachment

```java
inline BMXVideoAttachment(
    String path,
    String thumbnailPath,
    int duration,
    BMXMessageAttachment.Size size,
    String displayName
)
```

构造函数，构建发送视频消息附件 

**Parameters**: 

  * **path** 文件的本地路径 
  * **thumbnailPath** 缩略图文件的本地路径 
  * **duration** 视频片段时长 
  * **size** 视频大小，宽度和高度 
  * **displayName** 文件展示名 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="BMXVideoAttachment" %}{% endlanying_code_snippet %}
```
### function BMXVideoAttachment

```java
inline BMXVideoAttachment(
    String path,
    String thumbnailPath,
    int duration,
    BMXMessageAttachment.Size size
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="BMXVideoAttachment" %}{% endlanying_code_snippet %}
```
### function BMXVideoAttachment

```java
inline BMXVideoAttachment(
    String ratelUrl,
    int duration,
    BMXMessageAttachment.Size size,
    String displayName,
    long fileLength
)
```

构造函数，构建接收视频消息附件 

**Parameters**: 

  * **ratelUrl** ratel服务器地址 
  * **duration** 视频片段时长 
  * **size** 视频大小，宽度和高度 
  * **displayName** 文件展示名 
  * **fileLength** 文件大小 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="BMXVideoAttachment" %}{% endlanying_code_snippet %}
```
### function BMXVideoAttachment

```java
inline BMXVideoAttachment(
    String ratelUrl,
    String thumbnailUrl,
    int duration,
    BMXMessageAttachment.Size size,
    String displayName,
    long fileLength
)
```

构造函数，构建接收视频消息附件 

**Parameters**: 

  * **ratelUrl** ratel服务器地址 
  * **thumbnailUrl** 缩略图文件服务器地址 
  * **duration** 视频片段时长 
  * **size** 视频大小，宽度和高度 
  * **displayName** 文件展示名 
  * **fileLength** 文件大小 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="BMXVideoAttachment" %}{% endlanying_code_snippet %}
```
### function type

```java
inline BMXMessageAttachment.Type type()
```

返回文件类型 

**Return**: Type 

**Reimplements**: [im::floo::floolib::BMXFileAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-type)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="type" %}{% endlanying_code_snippet %}
```
### function clone

```java
inline BMXMessageAttachment clone()
```

克隆函数 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [im::floo::floolib::BMXFileAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-clone)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="clone" %}{% endlanying_code_snippet %}
```
### function size

```java
inline BMXMessageAttachment.Size size()
```

视频大小，宽度和高度 

**Return**: Size 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="size" %}{% endlanying_code_snippet %}
```
### function duration

```java
inline int duration()
```

视频片段时长 

**Return**: int32_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="duration" %}{% endlanying_code_snippet %}
```
### function setThumbnail

```java
inline void setThumbnail(
    String path
)
```

设置发送视频片段消息缩略图 

**Parameters**: 

  * **path** 视频片段消息缩略图 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="setThumbnail" %}{% endlanying_code_snippet %}
```
### function thumbnailPath

```java
inline String thumbnailPath()
```

缩略图本地路径 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="thumbnailPath" %}{% endlanying_code_snippet %}
```
### function thumbnailUrl

```java
inline String thumbnailUrl()
```

缩略图服务器路径 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="thumbnailUrl" %}{% endlanying_code_snippet %}
```
### function setThumbnailRatelUrl

```java
inline void setThumbnailRatelUrl(
    String thumbnailRatelUrl
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="setThumbnailRatelUrl" %}{% endlanying_code_snippet %}
```
### function thumbnailRatelUrl

```java
inline String thumbnailRatelUrl()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="thumbnailRatelUrl" %}{% endlanying_code_snippet %}
```
### function thumbnailDownloadStatus

```java
inline BMXMessageAttachment.DownloadStatus thumbnailDownloadStatus()
```

缩略图下载状态 

**Return**: DownloadStatus 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="thumbnailDownloadStatus" %}{% endlanying_code_snippet %}
```
### function dynamic_cast

```java
static inline BMXVideoAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```


**Reimplements**: [im::floo::floolib::BMXFileAttachment::dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-dynamic-cast)


## Protected Functions Documentation

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="dynamic_cast" %}{% endlanying_code_snippet %}
```
### function BMXVideoAttachment

```java
inline BMXVideoAttachment(
    long cPtr,
    boolean cMemoryOwn
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="BMXVideoAttachment" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Reimplements**: [im::floo::floolib::BMXFileAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-finalize)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="finalize" %}{% endlanying_code_snippet %}
```
### function getCPtr

```java
static inline long getCPtr(
    BMXVideoAttachment obj
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800