---
title: floo::BMXFileAttachment
summary: Message file attachment 

---

# floo::BMXFileAttachment



Message file attachment 


`#include <bmx_file_attachment.h>`

Inherits from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

Inherited by [floo::BMXImageAttachment](classfloo_1_1_b_m_x_image_attachment.md), [floo::BMXVideoAttachment](classfloo_1_1_b_m_x_video_attachment.md), [floo::BMXVoiceAttachment](classfloo_1_1_b_m_x_voice_attachment.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(const std::string & path, const std::string & displayName ="")<br>Constructor to build the message attachment of sent file  |
| | **[BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(const std::string & ratelUrl, const std::string & displayName, int64_t fileLength)<br>Constructor to build the message attachment of received file  |
| virtual | **[~BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md#function-~bmxfileattachment)**()<br>Destructor  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_file_attachment.md#function-type)**() const<br>Type of returned file  |
| virtual BMXMessageAttachmentPtr | **[clone](classfloo_1_1_b_m_x_file_attachment.md#function-clone)**() const<br>Cloning function  |
| const std::string & | **[path](classfloo_1_1_b_m_x_file_attachment.md#function-path)**() const<br>Local path  |
| const std::string & | **[displayName](classfloo_1_1_b_m_x_file_attachment.md#function-displayname)**() const<br>Display name  |
| const std::string & | **[ratelUrl](classfloo_1_1_b_m_x_file_attachment.md#function-ratelurl)**() const<br>URL for remote ratel  |
| const std::string & | **[url](classfloo_1_1_b_m_x_file_attachment.md#function-url)**() const<br>URL for remote  |
| int64_t | **[fileLength](classfloo_1_1_b_m_x_file_attachment.md#function-filelength)**() const<br>File length  |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | **[downloadStatus](classfloo_1_1_b_m_x_file_attachment.md#function-downloadstatus)**() const<br>Attachment download state  |

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
| enum class| **[Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type)** { Image, Voice, Video, File, Location, Command, Forward}<br>Attachment type  |
| enum class| **[DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus)** { Downloaing, Successed, Failed, NotStart, Canceled}<br>Attachment download state  |

**Public Functions inherited from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**()<br>Constructor  |
| virtual | **[~BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment)**()<br>Destructor  |


## Public Functions Documentation

### function BMXFileAttachment

```cpp
BMXFileAttachment(
    const std::string & path,
    const std::string & displayName =""
)
```

Constructor to build the message attachment of sent file 

**Parameters**: 

  * **path** Local path of file 
  * **displayName** Display name of file 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXFileAttachment",function="BMXFileAttachment" %}{% endlanying_code_snippet %}
```
### function BMXFileAttachment

```cpp
BMXFileAttachment(
    const std::string & ratelUrl,
    const std::string & displayName,
    int64_t fileLength
)
```

Constructor to build the message attachment of received file 

**Parameters**: 

  * **ratelUrl** Address of ratel file server 
  * **displayName** Display name of file 
  * **fileLength** File size 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXFileAttachment",function="BMXFileAttachment" %}{% endlanying_code_snippet %}
```
### function ~BMXFileAttachment

```cpp
inline virtual ~BMXFileAttachment()
```

Destructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXFileAttachment",function="~BMXFileAttachment" %}{% endlanying_code_snippet %}
```
### function type

```cpp
inline virtual Type type() const
```

Type of returned file 

**Return**: Type 

**Reimplements**: [floo::BMXMessageAttachment::type](classfloo_1_1_b_m_x_message_attachment.md#function-type)


**Reimplemented by**: [floo::BMXImageAttachment::type](classfloo_1_1_b_m_x_image_attachment.md#function-type), [floo::BMXVideoAttachment::type](classfloo_1_1_b_m_x_video_attachment.md#function-type), [floo::BMXVoiceAttachment::type](classfloo_1_1_b_m_x_voice_attachment.md#function-type)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXFileAttachment",function="type" %}{% endlanying_code_snippet %}
```
### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

Cloning function 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [floo::BMXMessageAttachment::clone](classfloo_1_1_b_m_x_message_attachment.md#function-clone)


**Reimplemented by**: [floo::BMXImageAttachment::clone](classfloo_1_1_b_m_x_image_attachment.md#function-clone), [floo::BMXVideoAttachment::clone](classfloo_1_1_b_m_x_video_attachment.md#function-clone), [floo::BMXVoiceAttachment::clone](classfloo_1_1_b_m_x_voice_attachment.md#function-clone)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXFileAttachment",function="clone" %}{% endlanying_code_snippet %}
```
### function path

```cpp
const std::string & path() const
```

Local path 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXFileAttachment",function="path" %}{% endlanying_code_snippet %}
```
### function displayName

```cpp
const std::string & displayName() const
```

Display name 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXFileAttachment",function="displayName" %}{% endlanying_code_snippet %}
```
### function ratelUrl

```cpp
const std::string & ratelUrl() const
```

URL for remote ratel 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXFileAttachment",function="ratelUrl" %}{% endlanying_code_snippet %}
```
### function url

```cpp
const std::string & url() const
```

URL for remote 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXFileAttachment",function="url" %}{% endlanying_code_snippet %}
```
### function fileLength

```cpp
int64_t fileLength() const
```

File length 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXFileAttachment",function="fileLength" %}{% endlanying_code_snippet %}
```
### function downloadStatus

```cpp
DownloadStatus downloadStatus() const
```

Attachment download state 

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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXFileAttachment",function="downloadStatus" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800