---
title: floo::BMXVideoAttachment
summary: 视频消息附件
---

# floo::BMXVideoAttachment

视频消息附件

`#include <bmx_video_attachment.h>`

Inherits from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md), [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                                                                                 | Name                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                 | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(const std::string &#x26; path, int duration, const [Size] &#x26; size, const std::string &#x26; displayName ="")<br>构造函数，构建发送视频消息附件</p>                                                                 |
|                                                                                 | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(const std::string &#x26; path, const std::string &#x26; thumbnailPath, int duration, const [Size] &#x26; size, const std::string &#x26; displayName ="")<br>构造函数，构建发送视频消息附件</p>                         |
|                                                                                 | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(const std::string &#x26; ratelUrl, int duration, const [Size] &#x26; size, const std::string &#x26; displayName, int64_t fileLength)<br>构造函数，构建接收视频消息附件</p>                                             |
|                                                                                 | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(const std::string &#x26; ratelUrl, const std::string &#x26; thumbnailRatelUrl, int duration, const [Size] &#x26; size, const std::string &#x26; displayName, int64_t fileLength)<br>构造函数，构建接收视频消息附件</p> |
| virtual                                                                         | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-~bmxvideoattachment"><strong>~BMXVideoAttachment</strong></a>()<br>析构函数</p>                                                                                                                                                                                         |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type)             | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-type"><strong>type</strong></a>() const<br>返回文件类型</p>                                                                                                                                                                                                               |
| virtual BMXMessageAttachmentPtr                                                 | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-clone"><strong>clone</strong></a>() const<br>克隆函数</p>                                                                                                                                                                                                               |
| const \[Size] &                                                                 | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-size"><strong>size</strong></a>() const<br>视频大小，宽度和高度</p>                                                                                                                                                                                                           |
| int32\_t                                                                        | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-duration"><strong>duration</strong></a>() const<br>视频片段时长</p>                                                                                                                                                                                                       |
| void                                                                            | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-setthumbnail"><strong>setThumbnail</strong></a>(const std::string &#x26; path)<br>设置发送视频片段消息缩略图</p>                                                                                                                                                                 |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-thumbnailpath"><strong>thumbnailPath</strong></a>() const<br>缩略图本地路径</p>                                                                                                                                                                                            |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-thumbnailurl"><strong>thumbnailUrl</strong></a>() const<br>远程缩略图使用URL</p>                                                                                                                                                                                           |
| void                                                                            | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-setthumbnailratelurl"><strong>setThumbnailRatelUrl</strong></a>(const std::string &#x26; thumbnailRatelUrl)<br>设置发送视频片段消息缩略图ratel服务器路径</p>                                                                                                                          |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-thumbnailratelurl"><strong>thumbnailRatelUrl</strong></a>() const<br>缩略图ratel服务器路径</p>                                                                                                                                                                              |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-thumbnaildownloadstatus"><strong>thumbnailDownloadStatus</strong></a>() const<br>缩略图下载状态</p>                                                                                                                                                                        |

## Friends

|       | Name                                                                                                              |
| ----- | ----------------------------------------------------------------------------------------------------------------- |
| class | [**Encoder< BMXVideoAttachment >**](classfloo_1_1_b_m_x_video_attachment.md#friend-encoder<-bmxvideoattachment->) |
| class | [**Decoder< BMXVideoAttachment >**](classfloo_1_1_b_m_x_video_attachment.md#friend-decoder<-bmxvideoattachment->) |

## Additional inherited members

**Public Functions inherited from** [**floo::BMXFileAttachment**](classfloo_1_1_b_m_x_file_attachment.md)

|                                                                                 | Name                                                                                                                                                                                                                                      |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                 | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(const std::string &#x26; path, const std::string &#x26; displayName ="")<br>构造函数，构建发送文件消息附件</p>                     |
|                                                                                 | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(const std::string &#x26; ratelUrl, const std::string &#x26; displayName, int64_t fileLength)<br>构造函数，构建接收文件消息附件</p> |
| virtual                                                                         | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-~bmxfileattachment"><strong>~BMXFileAttachment</strong></a>()<br>析构函数</p>                                                                                                     |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-path"><strong>path</strong></a>() const<br>本地路径</p>                                                                                                                           |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-displayname"><strong>displayName</strong></a>() const<br>显示名</p>                                                                                                              |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-ratelurl"><strong>ratelUrl</strong></a>() const<br>远程ratel使用URL</p>                                                                                                           |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-url"><strong>url</strong></a>() const<br>远程使用URL</p>                                                                                                                          |
| int64\_t                                                                        | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-filelength"><strong>fileLength</strong></a>() const<br>文件长度</p>                                                                                                               |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-downloadstatus"><strong>downloadStatus</strong></a>() const<br>附件下载状态</p>                                                                                                     |

**Protected Attributes inherited from** [**floo::BMXFileAttachment**](classfloo_1_1_b_m_x_file_attachment.md)

|                                                                                 | Name                                                                                   |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| std::string                                                                     | [**mPath**](classfloo_1_1_b_m_x_file_attachment.md#variable-mpath)                     |
| std::string                                                                     | [**mDisplayName**](classfloo_1_1_b_m_x_file_attachment.md#variable-mdisplayname)       |
| std::string                                                                     | [**mRatelUrl**](classfloo_1_1_b_m_x_file_attachment.md#variable-mratelurl)             |
| std::string                                                                     | [**mUrl**](classfloo_1_1_b_m_x_file_attachment.md#variable-murl)                       |
| int64\_t                                                                        | [**mFileLength**](classfloo_1_1_b_m_x_file_attachment.md#variable-mfilelength)         |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | [**mDownloadStatus**](classfloo_1_1_b_m_x_file_attachment.md#variable-mdownloadstatus) |

**Friends inherited from** [**floo::BMXFileAttachment**](classfloo_1_1_b_m_x_file_attachment.md)

|       | Name                                                                                                           |
| ----- | -------------------------------------------------------------------------------------------------------------- |
| class | [**Encoder< BMXFileAttachment >**](classfloo_1_1_b_m_x_file_attachment.md#friend-encoder<-bmxfileattachment->) |
| class | [**Decoder< BMXFileAttachment >**](classfloo_1_1_b_m_x_file_attachment.md#friend-decoder<-bmxfileattachment->) |

**Public Types inherited from** [**floo::BMXMessageAttachment**](classfloo_1_1_b_m_x_message_attachment.md)

|            | Name                                                                                                                                                                              |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-type"><strong>Type</strong></a> { Image, Voice, Video, File, Location, Command, Forward}<br>附件类型</p>                   |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus"><strong>DownloadStatus</strong></a> { Downloaing, Successed, Failed, NotStart, Canceled}<br>附件下载状态</p> |

**Public Functions inherited from** [**floo::BMXMessageAttachment**](classfloo_1_1_b_m_x_message_attachment.md)

|         | Name                                                                                                                                           |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|         | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment"><strong>BMXMessageAttachment</strong></a>()<br>构造函数</p>   |
| virtual | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment"><strong>~BMXMessageAttachment</strong></a>()<br>析构函数</p> |

## Public Functions Documentation

### function BMXVideoAttachment

```cpp
BMXVideoAttachment(
    const std::string & path,
    int duration,
    const Size & size,
    const std::string & displayName =""
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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function BMXVideoAttachment

```cpp
BMXVideoAttachment(
    const std::string & path,
    const std::string & thumbnailPath,
    int duration,
    const Size & size,
    const std::string & displayName =""
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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function BMXVideoAttachment

```cpp
BMXVideoAttachment(
    const std::string & ratelUrl,
    int duration,
    const Size & size,
    const std::string & displayName,
    int64_t fileLength
)
```

构造函数，构建接收视频消息附件

**Parameters**:

* **ratelUrl** ratel文件服务器地址
* **duration** 视频片段时长
* **size** 视频大小，宽度和高度
* **displayName** 文件展示名
* **fileLength** 文件大小

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function BMXVideoAttachment

```cpp
BMXVideoAttachment(
    const std::string & ratelUrl,
    const std::string & thumbnailRatelUrl,
    int duration,
    const Size & size,
    const std::string & displayName,
    int64_t fileLength
)
```

构造函数，构建接收视频消息附件

**Parameters**:

* **ratelUrl** ratel文件服务器地址
* **thumbnailRatelUrl** 缩略图ratel文件服务器地址
* **duration** 视频片段时长
* **size** 视频大小，宽度和高度
* **displayName** 文件展示名
* **fileLength** 文件大小

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function \~BMXVideoAttachment

```cpp
inline virtual ~BMXVideoAttachment()
```

析构函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function type

```cpp
inline virtual Type type() const
```

返回文件类型

**Return**: Type

**Reimplements**: [floo::BMXFileAttachment::type](classfloo_1_1_b_m_x_file_attachment.md#function-type)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

克隆函数

**Return**: BMXMessageAttachmentPtr

**Reimplements**: [floo::BMXFileAttachment::clone](classfloo_1_1_b_m_x_file_attachment.md#function-clone)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function size

```cpp
const Size & size() const
```

视频大小，宽度和高度

**Return**: Size

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function duration

```cpp
int32_t duration() const
```

视频片段时长

**Return**: int32\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function setThumbnail

```cpp
void setThumbnail(
    const std::string & path
)
```

设置发送视频片段消息缩略图

**Parameters**:

* **path** 视频片段消息缩略图

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function thumbnailPath

```cpp
const std::string & thumbnailPath() const
```

缩略图本地路径

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function thumbnailUrl

```cpp
const std::string & thumbnailUrl() const
```

远程缩略图使用URL

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function setThumbnailRatelUrl

```cpp
void setThumbnailRatelUrl(
    const std::string & thumbnailRatelUrl
)
```

设置发送视频片段消息缩略图ratel服务器路径

**Parameters**:

* **thumbnailRatelUrl** 视频片段消息缩略图服务器路径

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function thumbnailRatelUrl

```cpp
const std::string & thumbnailRatelUrl() const
```

缩略图ratel服务器路径

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>

```

### function thumbnailDownloadStatus

```cpp
DownloadStatus thumbnailDownloadStatus() const
```

缩略图下载状态

**Return**: DownloadStatus

## Friends

### friend Encoder< BMXVideoAttachment >

```cpp
friend class Encoder< BMXVideoAttachment >(
    Encoder< BMXVideoAttachment > 
);
```

### friend Decoder< BMXVideoAttachment >

```cpp
friend class Decoder< BMXVideoAttachment >(
    Decoder< BMXVideoAttachment > 
);
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
