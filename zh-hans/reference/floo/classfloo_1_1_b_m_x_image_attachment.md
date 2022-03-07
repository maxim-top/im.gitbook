---
title: floo::BMXImageAttachment
summary: 图片消息附件 

---

# floo::BMXImageAttachment



图片消息附件 


`#include <bmx_image_attachment.h>`

Inherits from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md), [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXImageAttachment](classfloo_1_1_b_m_x_image_attachment.md#function-bmximageattachment)**(const std::string & path, const [Size] & size, const std::string & displayName ="")<br>构造函数，构建发送图片消息附件  |
| | **[BMXImageAttachment](classfloo_1_1_b_m_x_image_attachment.md#function-bmximageattachment)**(const std::string & ratelUrl, const [Size] & size, const std::string & displayName, int64_t fileLength)<br>构造函数，构建接收图片消息附件  |
| virtual | **[~BMXImageAttachment](classfloo_1_1_b_m_x_image_attachment.md#function-~bmximageattachment)**()<br>析构函数  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_image_attachment.md#function-type)**() const<br>返回图片附件类型  |
| virtual BMXMessageAttachmentPtr | **[clone](classfloo_1_1_b_m_x_image_attachment.md#function-clone)**() const<br>克隆函数  |
| const [Size] & | **[size](classfloo_1_1_b_m_x_image_attachment.md#function-size)**() const<br>图片大小  |
| const std::string & | **[thumbnailUrl](classfloo_1_1_b_m_x_image_attachment.md#function-thumbnailurl)**() const<br>远程使用缩略图URL  |
| void | **[setThumbnail](classfloo_1_1_b_m_x_image_attachment.md#function-setthumbnail)**(const std::string & path)<br>设置发送图片消息缩略图  |
| const std::string & | **[thumbnailPath](classfloo_1_1_b_m_x_image_attachment.md#function-thumbnailpath)**() const<br>缩略图本地路径  |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | **[thumbnailDownloadStatus](classfloo_1_1_b_m_x_image_attachment.md#function-thumbnaildownloadstatus)**() const<br>缩略图下载状态  |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[Encoder< BMXImageAttachment >](classfloo_1_1_b_m_x_image_attachment.md#friend-encoder<-bmximageattachment->)**  |
| class | **[Decoder< BMXImageAttachment >](classfloo_1_1_b_m_x_image_attachment.md#friend-decoder<-bmximageattachment->)**  |

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

### function BMXImageAttachment

```cpp
BMXImageAttachment(
    const std::string & path,
    const Size & size,
    const std::string & displayName =""
)
```

构造函数，构建发送图片消息附件 

**Parameters**: 

  * **path** 本地路径 
  * **size** 图片的大小，宽度和高度 
  * **displayName** 展示名 


### function BMXImageAttachment

```cpp
BMXImageAttachment(
    const std::string & ratelUrl,
    const Size & size,
    const std::string & displayName,
    int64_t fileLength
)
```

构造函数，构建接收图片消息附件 

**Parameters**: 

  * **url** 图片ratel服务器地址 
  * **size** 图片的大小，宽度和高度 
  * **displayName** 展示名 
  * **fileLength** 文件大小 


### function ~BMXImageAttachment

```cpp
inline virtual ~BMXImageAttachment()
```

析构函数 

### function type

```cpp
inline virtual Type type() const
```

返回图片附件类型 

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

图片大小 

**Return**: Size 

### function thumbnailUrl

```cpp
const std::string & thumbnailUrl() const
```

远程使用缩略图URL 

**Return**: std::string 

### function setThumbnail

```cpp
void setThumbnail(
    const std::string & path
)
```

设置发送图片消息缩略图 

**Parameters**: 

  * **path** 本地路径 


### function thumbnailPath

```cpp
const std::string & thumbnailPath() const
```

缩略图本地路径 

**Return**: std::string 

### function thumbnailDownloadStatus

```cpp
DownloadStatus thumbnailDownloadStatus() const
```

缩略图下载状态 

**Return**: DownloadStatus 

## Friends

### friend Encoder< BMXImageAttachment >

```cpp
friend class Encoder< BMXImageAttachment >(
    Encoder< BMXImageAttachment > 
);
```


### friend Decoder< BMXImageAttachment >

```cpp
friend class Decoder< BMXImageAttachment >(
    Decoder< BMXImageAttachment > 
);
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800