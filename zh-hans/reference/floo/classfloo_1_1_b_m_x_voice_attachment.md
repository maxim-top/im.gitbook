---
title: floo::BMXVoiceAttachment
summary: 音频消息附件
---

# floo::BMXVoiceAttachment

音频消息附件

`#include <bmx_voice_attachment.h>`

Inherits from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md), [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                                                                     | Name                                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                     | <p><a href="classfloo_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment"><strong>BMXVoiceAttachment</strong></a>(const std::string &#x26; path, int duration, const std::string &#x26; displayName ="")<br>构造函数，构建发送音频消息附件</p>                     |
|                                                                     | <p><a href="classfloo_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment"><strong>BMXVoiceAttachment</strong></a>(const std::string &#x26; ratelUrl, int duration, const std::string &#x26; displayName, int64_t fileLength)<br>构造函数，构建接收音频消息附件</p> |
| virtual                                                             | <p><a href="classfloo_1_1_b_m_x_voice_attachment.md#function-~bmxvoiceattachment"><strong>~BMXVoiceAttachment</strong></a>()<br>析构函数</p>                                                                                                                   |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | <p><a href="classfloo_1_1_b_m_x_voice_attachment.md#function-type"><strong>type</strong></a>() const<br>返回文件类型</p>                                                                                                                                         |
| virtual BMXMessageAttachmentPtr                                     | <p><a href="classfloo_1_1_b_m_x_voice_attachment.md#function-clone"><strong>clone</strong></a>() const<br>克隆函数</p>                                                                                                                                         |
| int32\_t                                                            | <p><a href="classfloo_1_1_b_m_x_voice_attachment.md#function-duration"><strong>duration</strong></a>() const<br>语音时长</p>                                                                                                                                   |

## Friends

|       | Name                                                                                                              |
| ----- | ----------------------------------------------------------------------------------------------------------------- |
| class | [**Encoder< BMXVoiceAttachment >**](classfloo_1_1_b_m_x_voice_attachment.md#friend-encoder<-bmxvoiceattachment->) |
| class | [**Decoder< BMXVoiceAttachment >**](classfloo_1_1_b_m_x_voice_attachment.md#friend-decoder<-bmxvoiceattachment->) |

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVoiceAttachment'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVoiceAttachment'></div>

```

### function \~BMXVoiceAttachment

```cpp
inline virtual ~BMXVoiceAttachment()
```

析构函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVoiceAttachment'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVoiceAttachment'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVoiceAttachment'></div>

```

### function duration

```cpp
int32_t duration() const
```

语音时长

**Return**: int32\_t

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVoiceAttachment'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
