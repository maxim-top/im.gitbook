---
title: floo::BMXFileAttachment
summary: Message file attachment
---

# floo::BMXFileAttachment

Message file attachment

`#include <bmx_file_attachment.h>`

Inherits from [floo::BMXMessageAttachment](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md), BMXBaseObject

Inherited by [floo::BMXImageAttachment](classfloo\_1\_1\_b\_m\_x\_image\_attachment.md), [floo::BMXVideoAttachment](classfloo\_1\_1\_b\_m\_x\_video\_attachment.md), [floo::BMXVoiceAttachment](classfloo\_1\_1\_b\_m\_x\_voice\_attachment.md)

## Public Functions

|                                                                                        | Name                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                        | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(const std::string &#x26; path, const std::string &#x26; displayName ="")<br>Constructor to build the message attachment of sent file</p>                         |
|                                                                                        | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(const std::string &#x26; ratelUrl, const std::string &#x26; displayName, int64_t fileLength)<br>Constructor to build the message attachment of received file</p> |
| virtual                                                                                | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-~bmxfileattachment"><strong>~BMXFileAttachment</strong></a>()<br>Destructor</p>                                                                                                                                            |
| virtual [Type](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#enum-type)             | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-type"><strong>type</strong></a>() const<br>Type of returned file</p>                                                                                                                                                       |
| virtual BMXMessageAttachmentPtr                                                        | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-clone"><strong>clone</strong></a>() const<br>Cloning function</p>                                                                                                                                                          |
| const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-path"><strong>path</strong></a>() const<br>Local path</p>                                                                                                                                                                  |
| const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-displayname"><strong>displayName</strong></a>() const<br>Display name</p>                                                                                                                                                  |
| const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-ratelurl"><strong>ratelUrl</strong></a>() const<br>URL for remote ratel</p>                                                                                                                                                |
| const std::string &                                                                    | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-url"><strong>url</strong></a>() const<br>URL for remote</p>                                                                                                                                                                |
| int64\_t                                                                               | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-filelength"><strong>fileLength</strong></a>() const<br>File length</p>                                                                                                                                                     |
| [DownloadStatus](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#enum-downloadstatus) | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-downloadstatus"><strong>downloadStatus</strong></a>() const<br>Attachment download state</p>                                                                                                                               |

## Protected Attributes

|                                                                                        | Name                                                                                          |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| std::string                                                                            | [**mPath**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#variable-mpath)                     |
| std::string                                                                            | [**mDisplayName**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#variable-mdisplayname)       |
| std::string                                                                            | [**mRatelUrl**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#variable-mratelurl)             |
| std::string                                                                            | [**mUrl**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#variable-murl)                       |
| int64\_t                                                                               | [**mFileLength**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#variable-mfilelength)         |
| [DownloadStatus](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#enum-downloadstatus) | [**mDownloadStatus**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#variable-mdownloadstatus) |

## Friends

|       | Name                                                                                                                  |
| ----- | --------------------------------------------------------------------------------------------------------------------- |
| class | [**Encoder< BMXFileAttachment >**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#friend-encoder<-bmxfileattachment->) |
| class | [**Decoder< BMXFileAttachment >**](classfloo\_1\_1\_b\_m\_x\_file\_attachment.md#friend-decoder<-bmxfileattachment->) |

## Additional inherited members

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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXFileAttachment'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXFileAttachment'></div>
```

### function \~BMXFileAttachment

```cpp
inline virtual ~BMXFileAttachment()
```

Destructor

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXFileAttachment'></div>
```

### function type

```cpp
inline virtual Type type() const
```

Type of returned file

**Return**: Type

**Reimplements**: [floo::BMXMessageAttachment::type](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#function-type)

**Reimplemented by**: [floo::BMXImageAttachment::type](classfloo\_1\_1\_b\_m\_x\_image\_attachment.md#function-type), [floo::BMXVideoAttachment::type](classfloo\_1\_1\_b\_m\_x\_video\_attachment.md#function-type), [floo::BMXVoiceAttachment::type](classfloo\_1\_1\_b\_m\_x\_voice\_attachment.md#function-type)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXFileAttachment'></div>
```

### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

Cloning function

**Return**: BMXMessageAttachmentPtr

**Reimplements**: [floo::BMXMessageAttachment::clone](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#function-clone)

**Reimplemented by**: [floo::BMXImageAttachment::clone](classfloo\_1\_1\_b\_m\_x\_image\_attachment.md#function-clone), [floo::BMXVideoAttachment::clone](classfloo\_1\_1\_b\_m\_x\_video\_attachment.md#function-clone), [floo::BMXVoiceAttachment::clone](classfloo\_1\_1\_b\_m\_x\_voice\_attachment.md#function-clone)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXFileAttachment'></div>
```

### function path

```cpp
const std::string & path() const
```

Local path

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXFileAttachment'></div>
```

### function displayName

```cpp
const std::string & displayName() const
```

Display name

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXFileAttachment'></div>
```

### function ratelUrl

```cpp
const std::string & ratelUrl() const
```

URL for remote ratel

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXFileAttachment'></div>
```

### function url

```cpp
const std::string & url() const
```

URL for remote

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXFileAttachment'></div>
```

### function fileLength

```cpp
int64_t fileLength() const
```

File length

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXFileAttachment'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXFileAttachment'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
