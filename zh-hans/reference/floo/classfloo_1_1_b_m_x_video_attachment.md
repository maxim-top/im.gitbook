---
title: floo::BMXVideoAttachment
summary: 视频消息附件 

---

# floo::BMXVideoAttachment



视频消息附件 


`#include <bmx_video_attachment.h>`

Inherits from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md), [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXVideoAttachment](classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(const std::string & path, int duration, const [Size] & size, const std::string & displayName ="")<br>构造函数，构建发送视频消息附件  |
| | **[BMXVideoAttachment](classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(const std::string & path, const std::string & thumbnailPath, int duration, const [Size] & size, const std::string & displayName ="")<br>构造函数，构建发送视频消息附件  |
| | **[BMXVideoAttachment](classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(const std::string & ratelUrl, int duration, const [Size] & size, const std::string & displayName, int64_t fileLength)<br>构造函数，构建接收视频消息附件  |
| | **[BMXVideoAttachment](classfloo_1_1_b_m_x_video_attachment.md#function-bmxvideoattachment)**(const std::string & ratelUrl, const std::string & thumbnailRatelUrl, int duration, const [Size] & size, const std::string & displayName, int64_t fileLength)<br>构造函数，构建接收视频消息附件  |
| virtual | **[~BMXVideoAttachment](classfloo_1_1_b_m_x_video_attachment.md#function-~bmxvideoattachment)**()<br>析构函数  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_video_attachment.md#function-type)**() const<br>返回文件类型  |
| virtual BMXMessageAttachmentPtr | **[clone](classfloo_1_1_b_m_x_video_attachment.md#function-clone)**() const<br>克隆函数  |
| const [Size] & | **[size](classfloo_1_1_b_m_x_video_attachment.md#function-size)**() const<br>视频大小，宽度和高度  |
| int32_t | **[duration](classfloo_1_1_b_m_x_video_attachment.md#function-duration)**() const<br>视频片段时长  |
| void | **[setThumbnail](classfloo_1_1_b_m_x_video_attachment.md#function-setthumbnail)**(const std::string & path)<br>设置发送视频片段消息缩略图  |
| const std::string & | **[thumbnailPath](classfloo_1_1_b_m_x_video_attachment.md#function-thumbnailpath)**() const<br>缩略图本地路径  |
| const std::string & | **[thumbnailUrl](classfloo_1_1_b_m_x_video_attachment.md#function-thumbnailurl)**() const<br>远程缩略图使用URL  |
| void | **[setThumbnailRatelUrl](classfloo_1_1_b_m_x_video_attachment.md#function-setthumbnailratelurl)**(const std::string & thumbnailRatelUrl)<br>设置发送视频片段消息缩略图ratel服务器路径  |
| const std::string & | **[thumbnailRatelUrl](classfloo_1_1_b_m_x_video_attachment.md#function-thumbnailratelurl)**() const<br>缩略图ratel服务器路径  |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | **[thumbnailDownloadStatus](classfloo_1_1_b_m_x_video_attachment.md#function-thumbnaildownloadstatus)**() const<br>缩略图下载状态  |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[Encoder< BMXVideoAttachment >](classfloo_1_1_b_m_x_video_attachment.md#friend-encoder<-bmxvideoattachment->)**  |
| class | **[Decoder< BMXVideoAttachment >](classfloo_1_1_b_m_x_video_attachment.md#friend-decoder<-bmxvideoattachment->)**  |

## Additional inherited members

**Public Functions inherited from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(const std::string & path, const std::string & displayName ="")<br>构造函数，构建发送文件消息附件  |
| | **[BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(const std::string & ratelUrl, const std::string & displayName, int64_t fileLength)<br>构造函数，构建接收文件消息附件  |
| virtual | **[~BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md#function-~bmxfileattachment)**()<br>析构函数  |
| const std::string & | **[path](classfloo_1_1_b_m_x_file_attachment.md#function-path)**() const<br>本地路径  |
| const std::string & | **[displayName](classfloo_1_1_b_m_x_file_attachment.md#function-displayname)**() const<br>显示名  |
| const std::string & | **[ratelUrl](classfloo_1_1_b_m_x_file_attachment.md#function-ratelurl)**() const<br>远程ratel使用URL  |
| const std::string & | **[url](classfloo_1_1_b_m_x_file_attachment.md#function-url)**() const<br>远程使用URL  |
| int64_t | **[fileLength](classfloo_1_1_b_m_x_file_attachment.md#function-filelength)**() const<br>文件长度  |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | **[downloadStatus](classfloo_1_1_b_m_x_file_attachment.md#function-downloadstatus)**() const<br>附件下载状态  |

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
| enum class| **[Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type)** { Image, Voice, Video, File, Location, Command, Forward}<br>附件类型  |
| enum class| **[DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus)** { Downloaing, Successed, Failed, NotStart, Canceled}<br>附件下载状态  |

**Public Functions inherited from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**()<br>构造函数  |
| virtual | **[~BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment)**()<br>析构函数  |


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


### function ~BMXVideoAttachment

```cpp
inline virtual ~BMXVideoAttachment()
```

析构函数 

### function type

```cpp
inline virtual Type type() const
```

返回文件类型 

**Return**: Type 

**Reimplements**: [floo::BMXFileAttachment::type](classfloo_1_1_b_m_x_file_attachment.md#function-type)


### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

克隆函数 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [floo::BMXFileAttachment::clone](classfloo_1_1_b_m_x_file_attachment.md#function-clone)


### function size

```cpp
const Size & size() const
```

视频大小，宽度和高度 

**Return**: Size 

### function duration

```cpp
int32_t duration() const
```

视频片段时长 

**Return**: int32_t 

### function setThumbnail

```cpp
void setThumbnail(
    const std::string & path
)
```

设置发送视频片段消息缩略图 

**Parameters**: 

  * **path** 视频片段消息缩略图 


### function thumbnailPath

```cpp
const std::string & thumbnailPath() const
```

缩略图本地路径 

**Return**: std::string 

### function thumbnailUrl

```cpp
const std::string & thumbnailUrl() const
```

远程缩略图使用URL 

**Return**: std::string 

### function setThumbnailRatelUrl

```cpp
void setThumbnailRatelUrl(
    const std::string & thumbnailRatelUrl
)
```

设置发送视频片段消息缩略图ratel服务器路径 

**Parameters**: 

  * **thumbnailRatelUrl** 视频片段消息缩略图服务器路径 


### function thumbnailRatelUrl

```cpp
const std::string & thumbnailRatelUrl() const
```

缩略图ratel服务器路径 

**Return**: std::string 

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


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800