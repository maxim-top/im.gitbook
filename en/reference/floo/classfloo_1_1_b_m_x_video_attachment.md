---
title: floo::BMXVideoAttachment
summary: Video attachment of message
---

# floo::BMXVideoAttachment

Video attachment of message

`#include <bmx_video_attachment.h>`

Inherits from [floo::BMXFileAttachment](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md), [floo::BMXMessageAttachment](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md), BMXBaseObject

## Public Functions

|                                                                                        | Name                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                        | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(const std::string &#x26; path, int duration, const [Size] &#x26; size, const std::string &#x26; displayName ="")<br>Constructor to build the video attachment to send</p>                                                                    |
|                                                                                        | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(const std::string &#x26; path, const std::string &#x26; thumbnailPath, int duration, const [Size] &#x26; size, const std::string &#x26; displayName ="")<br>Constructor to build the video attachment to send</p>                            |
|                                                                                        | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(const std::string &#x26; ratelUrl, int duration, const [Size] &#x26; size, const std::string &#x26; displayName, int64_t fileLength)<br>Constructor to build the video attachment to receive</p>                                             |
|                                                                                        | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment"><strong>BMXVideoAttachment</strong></a>(const std::string &#x26; ratelUrl, const std::string &#x26; thumbnailRatelUrl, int duration, const [Size] &#x26; size, const std::string &#x26; displayName, int64_t fileLength)<br>Constructor to build the video attachment to receive</p> |
| virtual                                                                                | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-~bmxvideoattachment"><strong>~BMXVideoAttachment</strong></a>()<br>Destructor</p>                                                                                                                                                                                                                        |
| virtual [Type](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#enum-type)             | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-type"><strong>type</strong></a>() const<br>Type of returned file</p>                                                                                                                                                                                                                                     |
| virtual BMXMessageAttachmentPtr                                                        | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-clone"><strong>clone</strong></a>() const<br>Cloning function</p>                                                                                                                                                                                                                                        |
| const \[Size] &                                                                        | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-size"><strong>size</strong></a>() const<br>Video size, width, and height</p>                                                                                                                                                                                                                             |
| int32\_t                                                                               | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-duration"><strong>duration</strong></a>() const<br>Length of video clip</p>                                                                                                                                                                                                                              |
| void                                                                                   | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-setthumbnail"><strong>setThumbnail</strong></a>(const std::string &#x26; path)<br>Set the thumbnail for video clip to send</p>                                                                                                                                                                           |
| const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-thumbnailpath"><strong>thumbnailPath</strong></a>() const<br>Local path of thumbnail</p>                                                                                                                                                                                                                 |
| const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-thumbnailurl"><strong>thumbnailUrl</strong></a>() const<br>URL for remote thumbnail</p>                                                                                                                                                                                                                  |
| void                                                                                   | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-setthumbnailratelurl"><strong>setThumbnailRatelUrl</strong></a>(const std::string &#x26; thumbnailRatelUrl)<br>Set thumbnail ratel server path to send video clip message</p>                                                                                                                            |
| const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-thumbnailratelurl"><strong>thumbnailRatelUrl</strong></a>() const<br>Thumbnail ratel server path</p>                                                                                                                                                                                                     |
| [DownloadStatus](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#enum-downloadstatus) | <p><a href="classfloo_1_1_b_m_x_video_attachment.md#function-thumbnaildownloadstatus"><strong>thumbnailDownloadStatus</strong></a>() const<br>Thumbnail downloading state</p>                                                                                                                                                                                         |

## Friends

|       | Name                                                                                                                     |
| ----- | ------------------------------------------------------------------------------------------------------------------------ |
| class | [**Encoder< BMXVideoAttachment >**](classfloo\_1\_1\_b\_m\_x\_video\_attachment.md#friend-encoder<-bmxvideoattachment->) |
| class | [**Decoder< BMXVideoAttachment >**](classfloo\_1\_1\_b\_m\_x\_video\_attachment.md#friend-decoder<-bmxvideoattachment->) |

## Additional inherited members

**Public Functions inherited from** [**floo::BMXFileAttachment**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md)

|                                                                                        | Name                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                        | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(const std::string &#x26; path, const std::string &#x26; displayName ="")<br>Constructor to build the message attachment of sent file</p>                         |
|                                                                                        | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(const std::string &#x26; ratelUrl, const std::string &#x26; displayName, int64_t fileLength)<br>Constructor to build the message attachment of received file</p> |
| virtual                                                                                | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-~bmxfileattachment"><strong>~BMXFileAttachment</strong></a>()<br>Destructor</p>                                                                                                                                            |
| const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-path"><strong>path</strong></a>() const<br>Local path</p>                                                                                                                                                                  |
| const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-displayname"><strong>displayName</strong></a>() const<br>Display name</p>                                                                                                                                                  |
| const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-ratelurl"><strong>ratelUrl</strong></a>() const<br>URL for remote ratel</p>                                                                                                                                                |
| const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-url"><strong>url</strong></a>() const<br>URL for remote</p>                                                                                                                                                                |
| int64\_t                                                                               | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-filelength"><strong>fileLength</strong></a>() const<br>File length</p>                                                                                                                                                     |
| [DownloadStatus](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#enum-downloadstatus) | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-downloadstatus"><strong>downloadStatus</strong></a>() const<br>Attachment download state</p>                                                                                                                               |

**Protected Attributes inherited from** [**floo::BMXFileAttachment**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md)

|                                                                                        | Name                                                                                          |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| std::string                                                                            | [**mPath**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#variable-mpath)                     |
| std::string                                                                            | [**mDisplayName**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#variable-mdisplayname)       |
| std::string                                                                            | [**mRatelUrl**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#variable-mratelurl)             |
| std::string                                                                            | [**mUrl**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#variable-murl)                       |
| int64\_t                                                                               | [**mFileLength**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#variable-mfilelength)         |
| [DownloadStatus](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#enum-downloadstatus) | [**mDownloadStatus**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#variable-mdownloadstatus) |

**Friends inherited from** [**floo::BMXFileAttachment**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md)

|       | Name                                                                                                                  |
| ----- | --------------------------------------------------------------------------------------------------------------------- |
| class | [**Encoder< BMXFileAttachment >**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#friend-encoder<-bmxfileattachment->) |
| class | [**Decoder< BMXFileAttachment >**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#friend-decoder<-bmxfileattachment->) |

**Public Types inherited from** [**floo::BMXMessageAttachment**](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md)

|            | Name                                                                                                                                                                                                 |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-type"><strong>Type</strong></a> { Image, Voice, Video, File, Location, Command, Forward}<br>Attachment type</p>                           |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus"><strong>DownloadStatus</strong></a> { Downloaing, Successed, Failed, NotStart, Canceled}<br>Attachment download state</p> |

**Public Functions inherited from** [**floo::BMXMessageAttachment**](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md)

|         | Name                                                                                                                                                 |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|         | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment"><strong>BMXMessageAttachment</strong></a>()<br>Constructor</p>  |
| virtual | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment"><strong>~BMXMessageAttachment</strong></a>()<br>Destructor</p> |

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

Constructor to build the video attachment to send

**Parameters**:

* **path** Local path of file
* **duration** Length of video clip
* **size** Video size, width, and height
* **displayName** Display name of file

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

Constructor to build the video attachment to send

**Parameters**:

* **path** Local path of file
* **thumbnailPath** Local path of thumbnail file
* **duration** Length of video clip
* **size** Video size, width, and height
* **displayName** Display name of file

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

Constructor to build the video attachment to receive

**Parameters**:

* **ratelUrl** Address of ratel file server
* **duration** Length of video clip
* **size** Video size, width, and height
* **displayName** Display name of file
* **fileLength** File size

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

Constructor to build the video attachment to receive

**Parameters**:

* **ratelUrl** Address of ratel file server
* **thumbnailRatelUrl** Thumbnail ratel file server address
* **duration** Length of video clip
* **size** Video size, width, and height
* **displayName** Display name of file
* **fileLength** File size

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>
```

### function \~BMXVideoAttachment

```cpp
inline virtual ~BMXVideoAttachment()
```

Destructor

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>
```

### function type

```cpp
inline virtual Type type() const
```

Type of returned file

**Return**: Type

**Reimplements**: [floo::BMXFileAttachment::type](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#function-type)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>
```

### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

Cloning function

**Return**: BMXMessageAttachmentPtr

**Reimplements**: [floo::BMXFileAttachment::clone](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#function-clone)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>
```

### function size

```cpp
const Size & size() const
```

Video size, width, and height

**Return**: Size

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>
```

### function duration

```cpp
int32_t duration() const
```

Length of video clip

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

Set the thumbnail for video clip to send

**Parameters**:

* **path** Thumbnail of video clip message

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>
```

### function thumbnailPath

```cpp
const std::string & thumbnailPath() const
```

Local path of thumbnail

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>
```

### function thumbnailUrl

```cpp
const std::string & thumbnailUrl() const
```

URL for remote thumbnail

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

Set thumbnail ratel server path to send video clip message

**Parameters**:

* **thumbnailRatelUrl** Thumbnail server path for video clip message

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>
```

### function thumbnailRatelUrl

```cpp
const std::string & thumbnailRatelUrl() const
```

Thumbnail ratel server path

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVideoAttachment'></div>
```

### function thumbnailDownloadStatus

```cpp
DownloadStatus thumbnailDownloadStatus() const
```

Thumbnail downloading state

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



Updated on 2022-01-26 at 17:20:40 +0800
