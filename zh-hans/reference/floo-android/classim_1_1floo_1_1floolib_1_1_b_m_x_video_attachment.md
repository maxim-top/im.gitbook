---
title: im::floo::floolib::BMXVideoAttachment
summary: 视频消息附件
---

# im::floo::floolib::BMXVideoAttachment

视频消息附件

Inherits from [im.floo.floolib.BMXFileAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md), [im.floo.floolib.BMXMessageAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md), BMXBaseObject

## Public Functions

|                                                                                               | Name                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void                                                                             | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-delete)()                                                                                                                                                                                       |
|                                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(String path, int duration, BMXMessageAttachment.Size size, String displayName)<br>构造函数，构建发送视频消息附件</p>                                           |
|                                                                                               | [**BMXVideoAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-bmxvideoattachment)(String path, int duration, BMXMessageAttachment.Size size)                                                                                                      |
|                                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(String path, String thumbnailPath, int duration, BMXMessageAttachment.Size size, String displayName)<br>构造函数，构建发送视频消息附件</p>                     |
|                                                                                               | [**BMXVideoAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-bmxvideoattachment)(String path, String thumbnailPath, int duration, BMXMessageAttachment.Size size)                                                                                |
|                                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(String ratelUrl, int duration, BMXMessageAttachment.Size size, String displayName, long fileLength)<br>构造函数，构建接收视频消息附件</p>                      |
|                                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(String ratelUrl, String thumbnailUrl, int duration, BMXMessageAttachment.Size size, String displayName, long fileLength)<br>构造函数，构建接收视频消息附件</p> |
| BMXMessageAttachment.Type                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-type"><strong>type</strong></a>()<br>返回文件类型</p>                                                                                                                                                             |
| [BMXMessageAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-clone"><strong>clone</strong></a>()<br>克隆函数</p>                                                                                                                                                             |
| BMXMessageAttachment.Size                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-size"><strong>size</strong></a>()<br>视频大小，宽度和高度</p>                                                                                                                                                         |
| int                                                                                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-duration"><strong>duration</strong></a>()<br>视频片段时长</p>                                                                                                                                                     |
| void                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-setthumbnail"><strong>setThumbnail</strong></a>(String path)<br>设置发送视频片段消息缩略图</p>                                                                                                                           |
| String                                                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnailpath"><strong>thumbnailPath</strong></a>()<br>缩略图本地路径</p>                                                                                                                                          |
| String                                                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnailurl"><strong>thumbnailUrl</strong></a>()<br>缩略图服务器路径</p>                                                                                                                                           |
| void                                                                                          | [**setThumbnailRatelUrl**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-setthumbnailratelurl)(String thumbnailRatelUrl)                                                                                                                                   |
| String                                                                                        | [**thumbnailRatelUrl**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-thumbnailratelurl)()                                                                                                                                                                 |
| BMXMessageAttachment.DownloadStatus                                                           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnaildownloadstatus"><strong>thumbnailDownloadStatus</strong></a>()<br>缩略图下载状态</p>                                                                                                                      |
| [BMXVideoAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md)     | [**dynamic\_cast**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-dynamic-cast)([BMXMessageAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md) attachment)                                                                  |

## Protected Functions

|      | Name                                                                                                                                                                                               |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXVideoAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-bmxvideoattachment)(long cPtr, boolean cMemoryOwn)                                           |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-finalize)()                                                                                            |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md#function-getcptr)([BMXVideoAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_video\_attachment.md) obj) |

## Additional inherited members

**Public Functions inherited from** [**im.floo.floolib.BMXFileAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md)

|                                     | Name                                                                                                                                                                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(String path, String displayName)<br>构造函数，构建发送文件消息附件</p>                      |
|                                     | [**BMXFileAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md#function-bmxfileattachment)(String path)                                                                                 |
|                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(String ratelUrl, String displayName, long fileLength)<br>构造函数，构建接收文件消息附件</p> |
| String                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-path"><strong>path</strong></a>()<br>本地路径</p>                                                                                          |
| String                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-displayname"><strong>displayName</strong></a>()<br>显示名</p>                                                                             |
| String                              | [**ratelUrl**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md#function-ratelurl)()                                                                                                              |
| String                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-url"><strong>url</strong></a>()<br>远程URL</p>                                                                                           |
| long                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-filelength"><strong>fileLength</strong></a>()<br>文件长度</p>                                                                              |
| BMXMessageAttachment.DownloadStatus | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-downloadstatus"><strong>downloadStatus</strong></a>()<br>附件下载状态</p>                                                                    |

**Protected Functions inherited from** [**im.floo.floolib.BMXFileAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md)

|   | Name                                                                                                                                                  |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [**BMXFileAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md#function-bmxfileattachment)(long cPtr, boolean cMemoryOwn) |

**Protected Functions inherited from** [**im.floo.floolib.BMXMessageAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md)

|   | Name                                                                                                                                                           |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [**BMXMessageAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md#function-bmxmessageattachment)(long cPtr, boolean cMemoryOwn) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Reimplements**: [im::floo::floolib::BMXFileAttachment::delete](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md#function-delete)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```

### function type

```java
inline BMXMessageAttachment.Type type()
```

返回文件类型

**Return**: Type

**Reimplements**: [im::floo::floolib::BMXFileAttachment::type](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md#function-type)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```

### function clone

```java
inline BMXMessageAttachment clone()
```

克隆函数

**Return**: BMXMessageAttachmentPtr

**Reimplements**: [im::floo::floolib::BMXFileAttachment::clone](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md#function-clone)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```

### function size

```java
inline BMXMessageAttachment.Size size()
```

视频大小，宽度和高度

**Return**: Size

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```

### function duration

```java
inline int duration()
```

视频片段时长

**Return**: int32\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```

### function thumbnailPath

```java
inline String thumbnailPath()
```

缩略图本地路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```

### function thumbnailUrl

```java
inline String thumbnailUrl()
```

缩略图服务器路径

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```

### function setThumbnailRatelUrl

```java
inline void setThumbnailRatelUrl(
    String thumbnailRatelUrl
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```

### function thumbnailRatelUrl

```java
inline String thumbnailRatelUrl()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```

### function thumbnailDownloadStatus

```java
inline BMXMessageAttachment.DownloadStatus thumbnailDownloadStatus()
```

缩略图下载状态

**Return**: DownloadStatus

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```

### function dynamic\_cast

```java
static inline BMXVideoAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```

**Reimplements**: [im::floo::floolib::BMXFileAttachment::dynamic\_cast](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md#function-dynamic-cast)

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```

### function finalize

```java
inline void finalize()
```

**Reimplements**: [im::floo::floolib::BMXFileAttachment::finalize](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_file\_attachment.md#function-finalize)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```

### function getCPtr

```java
static inline long getCPtr(
    BMXVideoAttachment obj
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
