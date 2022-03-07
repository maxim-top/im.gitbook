---
title: floo::BMXVideoAttachment
summary: Video attachment of message 

---

# floo::BMXVideoAttachment



Video attachment of message 


`#include <bmx_video_attachment.h>`

Inherits from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md), [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXVideoAttachment](classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(const std::string & path, int duration, const [Size] & size, const std::string & displayName ="")<br>Constructor to build the video attachment to send  |
| | **[BMXVideoAttachment](classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(const std::string & path, const std::string & thumbnailPath, int duration, const [Size] & size, const std::string & displayName ="")<br>Constructor to build the video attachment to send  |
| | **[BMXVideoAttachment](classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(const std::string & ratelUrl, int duration, const [Size] & size, const std::string & displayName, int64_t fileLength)<br>Constructor to build the video attachment to receive  |
| | **[BMXVideoAttachment](classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(const std::string & ratelUrl, const std::string & thumbnailRatelUrl, int duration, const [Size] & size, const std::string & displayName, int64_t fileLength)<br>Constructor to build the video attachment to receive  |
| virtual | **[~BMXVideoAttachment](classfloo_1_1_b_m_x_video_attachment.md#function-~bmxvideoattachment)**()<br>Destructor  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_video_attachment.md#function-type)**() const<br>Type of returned file  |
| virtual BMXMessageAttachmentPtr | **[clone](classfloo_1_1_b_m_x_video_attachment.md#function-clone)**() const<br>Cloning function  |
| const [Size] & | **[size](classfloo_1_1_b_m_x_video_attachment.md#function-size)**() const<br>Video size, width, and height  |
| int32_t | **[duration](classfloo_1_1_b_m_x_video_attachment.md#function-duration)**() const<br>Length of video clip  |
| void | **[setThumbnail](classfloo_1_1_b_m_x_video_attachment.md#function-setthumbnail)**(const std::string & path)<br>Set the thumbnail for video clip to send  |
| const std::string & | **[thumbnailPath](classfloo_1_1_b_m_x_video_attachment.md#function-thumbnailpath)**() const<br>Local path of thumbnail  |
| const std::string & | **[thumbnailUrl](classfloo_1_1_b_m_x_video_attachment.md#function-thumbnailurl)**() const<br>URL for remote thumbnail  |
| void | **[setThumbnailRatelUrl](classfloo_1_1_b_m_x_video_attachment.md#function-setthumbnailratelurl)**(const std::string & thumbnailRatelUrl)<br>Set thumbnail ratel server path to send video clip message  |
| const std::string & | **[thumbnailRatelUrl](classfloo_1_1_b_m_x_video_attachment.md#function-thumbnailratelurl)**() const<br>Thumbnail ratel server path  |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | **[thumbnailDownloadStatus](classfloo_1_1_b_m_x_video_attachment.md#function-thumbnaildownloadstatus)**() const<br>Thumbnail downloading state  |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[Encoder< BMXVideoAttachment >](classfloo_1_1_b_m_x_video_attachment.md#friend-encoder<-bmxvideoattachment->)**  |
| class | **[Decoder< BMXVideoAttachment >](classfloo_1_1_b_m_x_video_attachment.md#friend-decoder<-bmxvideoattachment->)**  |

## Additional inherited members

**Public Functions inherited from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(const std::string & path, const std::string & displayName ="")<br>Constructor to build the message attachment of sent file  |
| | **[BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(const std::string & ratelUrl, const std::string & displayName, int64_t fileLength)<br>Constructor to build the message attachment of received file  |
| virtual | **[~BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md#function-~bmxfileattachment)**()<br>Destructor  |
| const std::string & | **[path](classfloo_1_1_b_m_x_file_attachment.md#function-path)**() const<br>Local path  |
| const std::string & | **[displayName](classfloo_1_1_b_m_x_file_attachment.md#function-displayname)**() const<br>Display name  |
| const std::string & | **[ratelUrl](classfloo_1_1_b_m_x_file_attachment.md#function-ratelurl)**() const<br>URL for remote ratel  |
| const std::string & | **[url](classfloo_1_1_b_m_x_file_attachment.md#function-url)**() const<br>URL for remote  |
| int64_t | **[fileLength](classfloo_1_1_b_m_x_file_attachment.md#function-filelength)**() const<br>File length  |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | **[downloadStatus](classfloo_1_1_b_m_x_file_attachment.md#function-downloadstatus)**() const<br>Attachment download state  |

**Protected Attributes inherited from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| std::string | **[mPath](classfloo_1_1_b_m_x_file_attachment.md#variable-mpath)**  |
| std::string | **[mDisplayName](classfloo_1_1_b_m_x_file_attachment.md#variable-mdisplayname)**  |
| std::string | **[mRatelUrl](classfloo_1_1_b_m_x_file_attachment.md#variable-mratelurl)**  |
| std::string | **[mUrl](classfloo_1_1_b_m_x_file_attachment.md#variable-murl)**  |
| int64_t | **[mFileLength](classfloo_1_1_b_m_x_file_attachment.md#variable-mfilelength)**  |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | **[mDownloadStatus](classfloo_1_1_b_m_x_file_attachment.md#variable-mdownloadstatus)**  |

**Friends inherited from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| class | **[Encoder< BMXFileAttachment >](classfloo_1_1_b_m_x_file_attachment.md#friend-encoder<-bmxfileattachment->)**  |
| class | **[Decoder< BMXFileAttachment >](classfloo_1_1_b_m_x_file_attachment.md#friend-decoder<-bmxfileattachment->)**  |

**Public Types inherited from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| enum class| **[Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type)** { Image, Voice, Video, File, Location, Command, Forward}<br>Attachment type  |
| enum class| **[DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus)** { Downloaing, Successed, Failed, NotStart, Canceled}<br>Attachment download state  |

**Public Functions inherited from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**()<br>Constructor  |
| virtual | **[~BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment)**()<br>Destructor  |


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


### function ~BMXVideoAttachment

```cpp
inline virtual ~BMXVideoAttachment()
```

Destructor 

### function type

```cpp
inline virtual Type type() const
```

Type of returned file 

**Return**: Type 

**Reimplements**: [floo::BMXFileAttachment::type](classfloo_1_1_b_m_x_file_attachment.md#function-type)


### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

Cloning function 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [floo::BMXFileAttachment::clone](classfloo_1_1_b_m_x_file_attachment.md#function-clone)


### function size

```cpp
const Size & size() const
```

Video size, width, and height 

**Return**: Size 

### function duration

```cpp
int32_t duration() const
```

Length of video clip 

**Return**: int32_t 

### function setThumbnail

```cpp
void setThumbnail(
    const std::string & path
)
```

Set the thumbnail for video clip to send 

**Parameters**: 

  * **path** Thumbnail of video clip message 


### function thumbnailPath

```cpp
const std::string & thumbnailPath() const
```

Local path of thumbnail 

**Return**: std::string 

### function thumbnailUrl

```cpp
const std::string & thumbnailUrl() const
```

URL for remote thumbnail 

**Return**: std::string 

### function setThumbnailRatelUrl

```cpp
void setThumbnailRatelUrl(
    const std::string & thumbnailRatelUrl
)
```

Set thumbnail ratel server path to send video clip message 

**Parameters**: 

  * **thumbnailRatelUrl** Thumbnail server path for video clip message 


### function thumbnailRatelUrl

```cpp
const std::string & thumbnailRatelUrl() const
```

Thumbnail ratel server path 

**Return**: std::string 

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


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800