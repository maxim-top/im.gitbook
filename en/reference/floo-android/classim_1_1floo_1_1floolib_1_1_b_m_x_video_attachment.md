---
title: im::floo::floolib::BMXVideoAttachment
summary: Video attachment of message 

---

# im::floo::floolib::BMXVideoAttachment



Video attachment of message 

Inherits from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md), [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-delete)**() |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(String path, int duration, BMXMessageAttachment.Size size, String displayName)<br>Constructor to build the video attachment to send  |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(String path, int duration, BMXMessageAttachment.Size size) |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(String path, String thumbnailPath, int duration, BMXMessageAttachment.Size size, String displayName)<br>Constructor to build the video attachment to send  |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(String path, String thumbnailPath, int duration, BMXMessageAttachment.Size size) |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(String ratelUrl, int duration, BMXMessageAttachment.Size size, String displayName, long fileLength)<br>Constructor to build the video attachment to receive  |
| | **[BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(String ratelUrl, String thumbnailUrl, int duration, BMXMessageAttachment.Size size, String displayName, long fileLength)<br>Constructor to build the video attachment to receive  |
| BMXMessageAttachment.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-type)**()<br>Type of returned file  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[clone](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-clone)**()<br>Cloning function  |
| BMXMessageAttachment.Size | **[size](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-size)**()<br>Video size, width, and height  |
| int | **[duration](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-duration)**()<br>Length of video clip  |
| void | **[setThumbnail](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-setthumbnail)**(String path)<br>Set the thumbnail for video clip to send  |
| String | **[thumbnailPath](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnailpath)**()<br>Local path of thumbnail  |
| String | **[thumbnailUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnailurl)**()<br>Server path of thumbnail  |
| void | **[setThumbnailRatelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-setthumbnailratelurl)**(String thumbnailRatelUrl) |
| String | **[thumbnailRatelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnailratelurl)**() |
| BMXMessageAttachment.DownloadStatus | **[thumbnailDownloadStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnaildownloadstatus)**()<br>Thumbnail downloading state  |
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
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String path, String displayName)<br>Constructor to build the message attachment of sent file  |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String path) |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String ratelUrl, String displayName, long fileLength)<br>Constructor to build the message attachment of received file  |
| String | **[path](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-path)**()<br>Local path  |
| String | **[displayName](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-displayname)**()<br>Display name  |
| String | **[ratelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-ratelurl)**() |
| String | **[url](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-url)**()<br>Remote URL  |
| long | **[fileLength](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-filelength)**()<br>File length  |
| BMXMessageAttachment.DownloadStatus | **[downloadStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-downloadstatus)**()<br>Attachment download state  |

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

Constructor to build the video attachment to send 

**Parameters**: 

  * **path** Local path of file 
  * **duration** Length of video clip 
  * **size** Video size, width, and height 
  * **displayName** Display name of file 


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

Constructor to build the video attachment to send 

**Parameters**: 

  * **path** Local path of file 
  * **thumbnailPath** Local path of thumbnail file 
  * **duration** Length of video clip 
  * **size** Video size, width, and height 
  * **displayName** Display name of file 


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

Constructor to build the video attachment to receive 

**Parameters**: 

  * **ratelUrl** ratel server address 
  * **duration** Length of video clip 
  * **size** Video size, width, and height 
  * **displayName** Display name of file 
  * **fileLength** File size 


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

Constructor to build the video attachment to receive 

**Parameters**: 

  * **ratelUrl** ratel server address 
  * **thumbnailUrl** Server address of thumbnail file 
  * **duration** Length of video clip 
  * **size** Video size, width, and height 
  * **displayName** Display name of file 
  * **fileLength** File size 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="BMXVideoAttachment" %}{% endlanying_code_snippet %}
```
### function type

```java
inline BMXMessageAttachment.Type type()
```

Type of returned file 

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

Cloning function 

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

Video size, width, and height 

**Return**: Size 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="size" %}{% endlanying_code_snippet %}
```
### function duration

```java
inline int duration()
```

Length of video clip 

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

Set the thumbnail for video clip to send 

**Parameters**: 

  * **path** Thumbnail of video clip message 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="setThumbnail" %}{% endlanying_code_snippet %}
```
### function thumbnailPath

```java
inline String thumbnailPath()
```

Local path of thumbnail 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVideoAttachment",function="thumbnailPath" %}{% endlanying_code_snippet %}
```
### function thumbnailUrl

```java
inline String thumbnailUrl()
```

Server path of thumbnail 

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

Thumbnail downloading state 

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