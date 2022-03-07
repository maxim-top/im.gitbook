---
title: floo::BMXFileAttachment
summary: 消息文件附件 

---

# floo::BMXFileAttachment



消息文件附件 


`#include <bmx_file_attachment.h>`

Inherits from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

Inherited by [floo::BMXImageAttachment](classfloo_1_1_b_m_x_image_attachment.md), [floo::BMXVideoAttachment](classfloo_1_1_b_m_x_video_attachment.md), [floo::BMXVoiceAttachment](classfloo_1_1_b_m_x_voice_attachment.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(const std::string & path, const std::string & displayName ="")<br>构造函数，构建发送文件消息附件  |
| | **[BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(const std::string & ratelUrl, const std::string & displayName, int64_t fileLength)<br>构造函数，构建接收文件消息附件  |
| virtual | **[~BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md#function-~bmxfileattachment)**()<br>析构函数  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_file_attachment.md#function-type)**() const<br>返回文件类型  |
| virtual BMXMessageAttachmentPtr | **[clone](classfloo_1_1_b_m_x_file_attachment.md#function-clone)**() const<br>克隆函数  |
| const std::string & | **[path](classfloo_1_1_b_m_x_file_attachment.md#function-path)**() const<br>本地路径  |
| const std::string & | **[displayName](classfloo_1_1_b_m_x_file_attachment.md#function-displayname)**() const<br>显示名  |
| const std::string & | **[ratelUrl](classfloo_1_1_b_m_x_file_attachment.md#function-ratelurl)**() const<br>远程ratel使用URL  |
| const std::string & | **[url](classfloo_1_1_b_m_x_file_attachment.md#function-url)**() const<br>远程使用URL  |
| int64_t | **[fileLength](classfloo_1_1_b_m_x_file_attachment.md#function-filelength)**() const<br>文件长度  |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | **[downloadStatus](classfloo_1_1_b_m_x_file_attachment.md#function-downloadstatus)**() const<br>附件下载状态  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[mPath](classfloo_1_1_b_m_x_file_attachment.md#variable-mpath)**  |
| std::string | **[mDisplayName](classfloo_1_1_b_m_x_file_attachment.md#variable-mdisplayname)**  |
| std::string | **[mRatelUrl](classfloo_1_1_b_m_x_file_attachment.md#variable-mratelurl)**  |
| std::string | **[mUrl](classfloo_1_1_b_m_x_file_attachment.md#variable-murl)**  |
| int64_t | **[mFileLength](classfloo_1_1_b_m_x_file_attachment.md#variable-mfilelength)**  |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | **[mDownloadStatus](classfloo_1_1_b_m_x_file_attachment.md#variable-mdownloadstatus)**  |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[Encoder< BMXFileAttachment >](classfloo_1_1_b_m_x_file_attachment.md#friend-encoder<-bmxfileattachment->)**  |
| class | **[Decoder< BMXFileAttachment >](classfloo_1_1_b_m_x_file_attachment.md#friend-decoder<-bmxfileattachment->)**  |

## Additional inherited members

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

### function BMXFileAttachment

```cpp
BMXFileAttachment(
    const std::string & path,
    const std::string & displayName =""
)
```

构造函数，构建发送文件消息附件 

**Parameters**: 

  * **path** 文件的本地路径 
  * **displayName** 文件展示名 


### function BMXFileAttachment

```cpp
BMXFileAttachment(
    const std::string & ratelUrl,
    const std::string & displayName,
    int64_t fileLength
)
```

构造函数，构建接收文件消息附件 

**Parameters**: 

  * **ratelUrl** ratel文件服务器地址 
  * **displayName** 文件展示名 
  * **fileLength** 文件大小 


### function ~BMXFileAttachment

```cpp
inline virtual ~BMXFileAttachment()
```

析构函数 

### function type

```cpp
inline virtual Type type() const
```

返回文件类型 

**Return**: Type 

**Reimplements**: [floo::BMXMessageAttachment::type](classfloo_1_1_b_m_x_message_attachment.md#function-type)


**Reimplemented by**: [floo::BMXImageAttachment::type](classfloo_1_1_b_m_x_image_attachment.md#function-type), [floo::BMXVideoAttachment::type](classfloo_1_1_b_m_x_video_attachment.md#function-type), [floo::BMXVoiceAttachment::type](classfloo_1_1_b_m_x_voice_attachment.md#function-type)


### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

克隆函数 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [floo::BMXMessageAttachment::clone](classfloo_1_1_b_m_x_message_attachment.md#function-clone)


**Reimplemented by**: [floo::BMXImageAttachment::clone](classfloo_1_1_b_m_x_image_attachment.md#function-clone), [floo::BMXVideoAttachment::clone](classfloo_1_1_b_m_x_video_attachment.md#function-clone), [floo::BMXVoiceAttachment::clone](classfloo_1_1_b_m_x_voice_attachment.md#function-clone)


### function path

```cpp
const std::string & path() const
```

本地路径 

**Return**: std::string 

### function displayName

```cpp
const std::string & displayName() const
```

显示名 

**Return**: std::string 

### function ratelUrl

```cpp
const std::string & ratelUrl() const
```

远程ratel使用URL 

**Return**: std::string 

### function url

```cpp
const std::string & url() const
```

远程使用URL 

**Return**: std::string 

### function fileLength

```cpp
int64_t fileLength() const
```

文件长度 

**Return**: std::string 

### function downloadStatus

```cpp
DownloadStatus downloadStatus() const
```

附件下载状态 

**Return**: DownloadStatus 

## Protected Attributes Documentation

### variable mPath

```cpp
std::string mPath;
```


### variable mDisplayName

```cpp
std::string mDisplayName;
```


### variable mRatelUrl

```cpp
std::string mRatelUrl;
```


### variable mUrl

```cpp
std::string mUrl;
```


### variable mFileLength

```cpp
int64_t mFileLength;
```


### variable mDownloadStatus

```cpp
DownloadStatus mDownloadStatus;
```


## Friends

### friend Encoder< BMXFileAttachment >

```cpp
friend class Encoder< BMXFileAttachment >(
    Encoder< BMXFileAttachment > 
);
```


### friend Decoder< BMXFileAttachment >

```cpp
friend class Decoder< BMXFileAttachment >(
    Decoder< BMXFileAttachment > 
);
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800