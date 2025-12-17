---
title: im::floo::floolib::BMXVideoAttachment
summary: Video attachment of message
---

# im::floo::floolib::BMXVideoAttachment

Video attachment of message

Inherits from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md), [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                                                                                    | Name                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| synchronized void                                                                  | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-delete)()                                                                                                                                                                                                                                       |
|                                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(String path, int duration, BMXMessageAttachment.Size size, String displayName)<br>Constructor to build the video attachment to send</p>                                              |
|                                                                                    | [**BMXVideoAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)(String path, int duration, BMXMessageAttachment.Size size)                                                                                                                                                      |
|                                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(String path, String thumbnailPath, int duration, BMXMessageAttachment.Size size, String displayName)<br>Constructor to build the video attachment to send</p>                        |
|                                                                                    | [**BMXVideoAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)(String path, String thumbnailPath, int duration, BMXMessageAttachment.Size size)                                                                                                                                |
|                                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(String ratelUrl, int duration, BMXMessageAttachment.Size size, String displayName, long fileLength)<br>Constructor to build the video attachment to receive</p>                      |
|                                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(String ratelUrl, String thumbnailUrl, int duration, BMXMessageAttachment.Size size, String displayName, long fileLength)<br>Constructor to build the video attachment to receive</p> |
| BMXMessageAttachment.Type                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-type"><strong>type</strong></a>()<br>Type of returned file</p>                                                                                                                                                                                   |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-clone"><strong>clone</strong></a>()<br>Cloning function</p>                                                                                                                                                                                      |
| BMXMessageAttachment.Size                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-size"><strong>size</strong></a>()<br>Video size, width, and height</p>                                                                                                                                                                           |
| int                                                                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-duration"><strong>duration</strong></a>()<br>Length of video clip</p>                                                                                                                                                                            |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-setthumbnail"><strong>setThumbnail</strong></a>(String path)<br>Set the thumbnail for video clip to send</p>                                                                                                                                     |
| String                                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnailpath"><strong>thumbnailPath</strong></a>()<br>Local path of thumbnail</p>                                                                                                                                                               |
| String                                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnailurl"><strong>thumbnailUrl</strong></a>()<br>Server path of thumbnail</p>                                                                                                                                                                |
| void                                                                               | [**setThumbnailRatelUrl**](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-setthumbnailratelurl)(String thumbnailRatelUrl)                                                                                                                                                                                   |
| String                                                                             | [**thumbnailRatelUrl**](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnailratelurl)()                                                                                                                                                                                                                 |
| BMXMessageAttachment.DownloadStatus                                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-thumbnaildownloadstatus"><strong>thumbnailDownloadStatus</strong></a>()<br>Thumbnail downloading state</p>                                                                                                                                       |
| [BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md)     | [**dynamic\_cast**](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-dynamic-cast)([BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment)                                                                                                                             |

## Protected Functions

|      | Name                                                                                                                                                                         |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXVideoAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)(long cPtr, boolean cMemoryOwn)                                |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-finalize)()                                                                                 |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-getcptr)([BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md) obj) |

## Additional inherited members

**Public Functions inherited from** [**im.floo.floolib.BMXFileAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md)

|                                     | Name                                                                                                                                                                                                                                                             |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(String path, String displayName)<br>Constructor to build the message attachment of sent file</p>                          |
|                                     | [**BMXFileAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)(String path)                                                                                                                                         |
|                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(String ratelUrl, String displayName, long fileLength)<br>Constructor to build the message attachment of received file</p> |
| String                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-path"><strong>path</strong></a>()<br>Local path</p>                                                                                                                                 |
| String                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-displayname"><strong>displayName</strong></a>()<br>Display name</p>                                                                                                                 |
| String                              | [**ratelUrl**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-ratelurl)()                                                                                                                                                                      |
| String                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-url"><strong>url</strong></a>()<br>Remote URL</p>                                                                                                                                   |
| long                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-filelength"><strong>fileLength</strong></a>()<br>File length</p>                                                                                                                    |
| BMXMessageAttachment.DownloadStatus | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-downloadstatus"><strong>downloadStatus</strong></a>()<br>Attachment download state</p>                                                                                              |

**Protected Functions inherited from** [**im.floo.floolib.BMXFileAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md)

|   | Name                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   | [**BMXFileAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)(long cPtr, boolean cMemoryOwn) |

**Protected Functions inherited from** [**im.floo.floolib.BMXMessageAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md)

|   | Name                                                                                                                                                |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [**BMXMessageAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)(long cPtr, boolean cMemoryOwn) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Reimplements**: [im::floo::floolib::BMXFileAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-delete)

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

Constructor to build the video attachment to send

**Parameters**:

* **path** Local path of file
* **duration** Length of video clip
* **size** Video size, width, and height
* **displayName** Display name of file

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

Constructor to build the video attachment to send

**Parameters**:

* **path** Local path of file
* **thumbnailPath** Local path of thumbnail file
* **duration** Length of video clip
* **size** Video size, width, and height
* **displayName** Display name of file

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

Constructor to build the video attachment to receive

**Parameters**:

* **ratelUrl** ratel server address
* **duration** Length of video clip
* **size** Video size, width, and height
* **displayName** Display name of file
* **fileLength** File size

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>

```

### function size

```java
inline BMXMessageAttachment.Size size()
```

Video size, width, and height

**Return**: Size

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>

```

### function duration

```java
inline int duration()
```

Length of video clip

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

Set the thumbnail for video clip to send

**Parameters**:

* **path** Thumbnail of video clip message

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>

```

### function thumbnailPath

```java
inline String thumbnailPath()
```

Local path of thumbnail

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVideoAttachment'></div>

```

### function thumbnailUrl

```java
inline String thumbnailUrl()
```

Server path of thumbnail

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

Thumbnail downloading state

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

**Reimplements**: [im::floo::floolib::BMXFileAttachment::dynamic\_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-dynamic-cast)

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

**Reimplements**: [im::floo::floolib::BMXFileAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-finalize)

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

***

Updated on 2022-01-26 at 17:18:31 +0800
