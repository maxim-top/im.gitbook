---
title: floo::BMXVoiceAttachment
summary: Audio attachment
---

# floo::BMXVoiceAttachment

Audio attachment

`#include <bmx_voice_attachment.h>`

Inherits from [floo::BMXFileAttachment](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md), [floo::BMXMessageAttachment](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md), BMXBaseObject

## Public Functions

|                                                                            | Name                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                            | <p><a href="classfloo_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment"><strong>BMXVoiceAttachment</strong></a>(const std::string &#x26; path, int duration, const std::string &#x26; displayName ="")<br>Constructor to build the audio attachment to send</p>                        |
|                                                                            | <p><a href="classfloo_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment"><strong>BMXVoiceAttachment</strong></a>(const std::string &#x26; ratelUrl, int duration, const std::string &#x26; displayName, int64_t fileLength)<br>Constructor to build the audio attachment to receive</p> |
| virtual                                                                    | <p><a href="classfloo_1_1_b_m_x_voice_attachment.md#function-~bmxvoiceattachment"><strong>~BMXVoiceAttachment</strong></a>()<br>Destructor</p>                                                                                                                                                  |
| virtual [Type](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#enum-type) | <p><a href="classfloo_1_1_b_m_x_voice_attachment.md#function-type"><strong>type</strong></a>() const<br>Type of returned file</p>                                                                                                                                                               |
| virtual BMXMessageAttachmentPtr                                            | <p><a href="classfloo_1_1_b_m_x_voice_attachment.md#function-clone"><strong>clone</strong></a>() const<br>Cloning function</p>                                                                                                                                                                  |
| int32\_t                                                                   | <p><a href="classfloo_1_1_b_m_x_voice_attachment.md#function-duration"><strong>duration</strong></a>() const<br>Length of speech</p>                                                                                                                                                            |

## Friends

|       | Name                                                                                                                     |
| ----- | ------------------------------------------------------------------------------------------------------------------------ |
| class | [**Encoder< BMXVoiceAttachment >**](classfloo\_1\_1\_b\_m\_x\_voice\_attachment.md#friend-encoder<-bmxvoiceattachment->) |
| class | [**Decoder< BMXVoiceAttachment >**](classfloo\_1\_1\_b\_m\_x\_voice\_attachment.md#friend-decoder<-bmxvoiceattachment->) |

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

Constructor to build the audio attachment to receive

**Parameters**:

* **ratelUrl** Address of ratel file server
* **duration** Audio length
* **displayName** Display name of file
* **fileLength** File size

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVoiceAttachment'></div>
```

### function \~BMXVoiceAttachment

```cpp
inline virtual ~BMXVoiceAttachment()
```

Destructor

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVoiceAttachment'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVoiceAttachment'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXVoiceAttachment'></div>
```

### function duration

```cpp
int32_t duration() const
```

Length of speech

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



Updated on 2022-01-26 at 17:20:40 +0800
