---
title: floo::BMXVoiceAttachment
summary: 音频消息附件 

---

# floo::BMXVoiceAttachment



音频消息附件 


`#include <bmx_voice_attachment.h>`

Inherits from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md), [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXVoiceAttachment](classfloo_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)**(const std::string & path, int duration, const std::string & displayName ="")<br>构造函数，构建发送音频消息附件  |
| | **[BMXVoiceAttachment](classfloo_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)**(const std::string & ratelUrl, int duration, const std::string & displayName, int64_t fileLength)<br>构造函数，构建接收音频消息附件  |
| virtual | **[~BMXVoiceAttachment](classfloo_1_1_b_m_x_voice_attachment.md#function-~bmxvoiceattachment)**()<br>析构函数  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_voice_attachment.md#function-type)**() const<br>返回文件类型  |
| virtual BMXMessageAttachmentPtr | **[clone](classfloo_1_1_b_m_x_voice_attachment.md#function-clone)**() const<br>克隆函数  |
| int32_t | **[duration](classfloo_1_1_b_m_x_voice_attachment.md#function-duration)**() const<br>语音时长  |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[Encoder< BMXVoiceAttachment >](classfloo_1_1_b_m_x_voice_attachment.md#friend-encoder<-bmxvoiceattachment->)**  |
| class | **[Decoder< BMXVoiceAttachment >](classfloo_1_1_b_m_x_voice_attachment.md#friend-decoder<-bmxvoiceattachment->)**  |

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

### function BMXVoiceAttachment

```cpp
BMXVoiceAttachment(
    const std::string & path,
    int duration,
    const std::string & displayName =""
)
```

构造函数，构建发送音频消息附件 

**Parameters**: 

  * **path** 文件的本地路径 
  * **duration** 音频时长 
  * **displayName** 文件展示名 


### function BMXVoiceAttachment

```cpp
BMXVoiceAttachment(
    const std::string & ratelUrl,
    int duration,
    const std::string & displayName,
    int64_t fileLength
)
```

构造函数，构建接收音频消息附件 

**Parameters**: 

  * **ratelUrl** ratel文件服务器地址 
  * **duration** 音频时长 
  * **displayName** 文件展示名 
  * **fileLength** 文件大小 


### function ~BMXVoiceAttachment

```cpp
inline virtual ~BMXVoiceAttachment()
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


### function duration

```cpp
int32_t duration() const
```

语音时长 

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