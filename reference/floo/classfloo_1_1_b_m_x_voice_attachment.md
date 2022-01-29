---
title: floo::BMXVoiceAttachment
summary: Audio attachment 

---

# floo::BMXVoiceAttachment



Audio attachment 


`#include <bmx_voice_attachment.h>`

Inherits from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md), [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXVoiceAttachment](classfloo_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)**(const std::string & path, int duration, const std::string & displayName ="")<br>Constructor to build the audio attachment to send  |
| | **[BMXVoiceAttachment](classfloo_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)**(const std::string & ratelUrl, int duration, const std::string & displayName, int64_t fileLength)<br>Constructor to build the audio attachment to receive  |
| virtual | **[~BMXVoiceAttachment](classfloo_1_1_b_m_x_voice_attachment.md#function-~bmxvoiceattachment)**()<br>Destructor  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_voice_attachment.md#function-type)**() const<br>Type of returned file  |
| virtual BMXMessageAttachmentPtr | **[clone](classfloo_1_1_b_m_x_voice_attachment.md#function-clone)**() const<br>Cloning function  |
| int32_t | **[duration](classfloo_1_1_b_m_x_voice_attachment.md#function-duration)**() const<br>Length of speech  |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[Encoder< BMXVoiceAttachment >](classfloo_1_1_b_m_x_voice_attachment.md#friend-encoder<-bmxvoiceattachment->)**  |
| class | **[Decoder< BMXVoiceAttachment >](classfloo_1_1_b_m_x_voice_attachment.md#friend-decoder<-bmxvoiceattachment->)**  |

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

### function BMXVoiceAttachment

```cpp
BMXVoiceAttachment(
    const std::string & path,
    int duration,
    const std::string & displayName =""
)
```

Constructor to build the audio attachment to send 

**Parameters**: 

  * **path** Local path of file 
  * **duration** Audio length 
  * **displayName** Display name of file 


### function BMXVoiceAttachment

```cpp
BMXVoiceAttachment(
    const std::string & ratelUrl,
    int duration,
    const std::string & displayName,
    int64_t fileLength
)
```

Constructor to build the audio attachment to receive 

**Parameters**: 

  * **ratelUrl** Address of ratel file server 
  * **duration** Audio length 
  * **displayName** Display name of file 
  * **fileLength** File size 


### function ~BMXVoiceAttachment

```cpp
inline virtual ~BMXVoiceAttachment()
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


### function duration

```cpp
int32_t duration() const
```

Length of speech 

**Return**: int32_t 

## Friends

### friend Encoder< BMXVoiceAttachment >

```cpp
friend class Encoder< BMXVoiceAttachment >(
    Encoder< BMXVoiceAttachment > 
);
```


### friend Decoder< BMXVoiceAttachment >

```cpp
friend class Decoder< BMXVoiceAttachment >(
    Decoder< BMXVoiceAttachment > 
);
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800