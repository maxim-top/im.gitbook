---
title: floo::BMXImageAttachment
summary: Message picture attachment 

---

# floo::BMXImageAttachment



Message picture attachment 


`#include <bmx_image_attachment.h>`

Inherits from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md), [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXImageAttachment](classfloo_1_1_b_m_x_image_attachment.md#function-bmximageattachment)**(const std::string & path, const [Size] & size, const std::string & displayName ="")<br>Constructor, to build the message attachment of sent picture  |
| | **[BMXImageAttachment](classfloo_1_1_b_m_x_image_attachment.md#function-bmximageattachment)**(const std::string & ratelUrl, const [Size] & size, const std::string & displayName, int64_t fileLength)<br>Constructor, to build the message attachment of received picture  |
| virtual | **[~BMXImageAttachment](classfloo_1_1_b_m_x_image_attachment.md#function-~bmximageattachment)**()<br>Destructor  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_image_attachment.md#function-type)**() const<br>Return the type of picture attachment  |
| virtual BMXMessageAttachmentPtr | **[clone](classfloo_1_1_b_m_x_image_attachment.md#function-clone)**() const<br>Cloning function  |
| const [Size] & | **[size](classfloo_1_1_b_m_x_image_attachment.md#function-size)**() const<br>Picture size  |
| const std::string & | **[thumbnailUrl](classfloo_1_1_b_m_x_image_attachment.md#function-thumbnailurl)**() const<br>Thumbnail url for remote use  |
| void | **[setThumbnail](classfloo_1_1_b_m_x_image_attachment.md#function-setthumbnail)**(const std::string & path)<br>Set a thumbnail for sent picture  |
| const std::string & | **[thumbnailPath](classfloo_1_1_b_m_x_image_attachment.md#function-thumbnailpath)**() const<br>Local path of thumbnail  |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | **[thumbnailDownloadStatus](classfloo_1_1_b_m_x_image_attachment.md#function-thumbnaildownloadstatus)**() const<br>Thumbnail downloading state  |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[Encoder< BMXImageAttachment >](classfloo_1_1_b_m_x_image_attachment.md#friend-encoder<-bmximageattachment->)**  |
| class | **[Decoder< BMXImageAttachment >](classfloo_1_1_b_m_x_image_attachment.md#friend-decoder<-bmximageattachment->)**  |

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

### function BMXImageAttachment

```cpp
BMXImageAttachment(
    const std::string & path,
    const Size & size,
    const std::string & displayName =""
)
```

Constructor, to build the message attachment of sent picture 

**Parameters**: 

  * **path** Local path 
  * **size** Size, width, and height of image 
  * **displayName** Display name 


### function BMXImageAttachment

```cpp
BMXImageAttachment(
    const std::string & ratelUrl,
    const Size & size,
    const std::string & displayName,
    int64_t fileLength
)
```

Constructor, to build the message attachment of received picture 

**Parameters**: 

  * **url** Address of image ratel server 
  * **size** Size, width, and height of image 
  * **displayName** Display name 
  * **fileLength** File size 


### function ~BMXImageAttachment

```cpp
inline virtual ~BMXImageAttachment()
```

Destructor 

### function type

```cpp
inline virtual Type type() const
```

Return the type of picture attachment 

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

Picture size 

**Return**: Size 

### function thumbnailUrl

```cpp
const std::string & thumbnailUrl() const
```

Thumbnail url for remote use 

**Return**: std::string 

### function setThumbnail

```cpp
void setThumbnail(
    const std::string & path
)
```

Set a thumbnail for sent picture 

**Parameters**: 

  * **path** Local path 


### function thumbnailPath

```cpp
const std::string & thumbnailPath() const
```

Local path of thumbnail 

**Return**: std::string 

### function thumbnailDownloadStatus

```cpp
DownloadStatus thumbnailDownloadStatus() const
```

Thumbnail downloading state 

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