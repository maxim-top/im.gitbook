---
title: floo::BMXImageAttachment
summary: Message picture attachment
---

# floo::BMXImageAttachment

Message picture attachment

`#include <bmx_image_attachment.h>`

Inherits from [floo::BMXFileAttachment](classfloo_1_1_b_m_x_file_attachment.md), [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                                                                                 | Name                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                 | <p><a href="classfloo_1_1_b_m_x_image_attachment.md#function-bmximageattachment"><strong>BMXImageAttachment</strong></a>(const std::string &#x26; path, const [Size] &#x26; size, const std::string &#x26; displayName ="")<br>Constructor, to build the message attachment of sent picture</p>                         |
|                                                                                 | <p><a href="classfloo_1_1_b_m_x_image_attachment.md#function-bmximageattachment"><strong>BMXImageAttachment</strong></a>(const std::string &#x26; ratelUrl, const [Size] &#x26; size, const std::string &#x26; displayName, int64_t fileLength)<br>Constructor, to build the message attachment of received picture</p> |
| virtual                                                                         | <p><a href="classfloo_1_1_b_m_x_image_attachment.md#function-~bmximageattachment"><strong>~BMXImageAttachment</strong></a>()<br>Destructor</p>                                                                                                                                                                          |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type)             | <p><a href="classfloo_1_1_b_m_x_image_attachment.md#function-type"><strong>type</strong></a>() const<br>Return the type of picture attachment</p>                                                                                                                                                                       |
| virtual BMXMessageAttachmentPtr                                                 | <p><a href="classfloo_1_1_b_m_x_image_attachment.md#function-clone"><strong>clone</strong></a>() const<br>Cloning function</p>                                                                                                                                                                                          |
| const \[Size] &                                                                 | <p><a href="classfloo_1_1_b_m_x_image_attachment.md#function-size"><strong>size</strong></a>() const<br>Picture size</p>                                                                                                                                                                                                |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_image_attachment.md#function-thumbnailurl"><strong>thumbnailUrl</strong></a>() const<br>Thumbnail url for remote use</p>                                                                                                                                                                |
| void                                                                            | <p><a href="classfloo_1_1_b_m_x_image_attachment.md#function-setthumbnail"><strong>setThumbnail</strong></a>(const std::string &#x26; path)<br>Set a thumbnail for sent picture</p>                                                                                                                                     |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_image_attachment.md#function-thumbnailpath"><strong>thumbnailPath</strong></a>() const<br>Local path of thumbnail</p>                                                                                                                                                                   |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | <p><a href="classfloo_1_1_b_m_x_image_attachment.md#function-thumbnaildownloadstatus"><strong>thumbnailDownloadStatus</strong></a>() const<br>Thumbnail downloading state</p>                                                                                                                                           |

## Friends

|       | Name                                                                                                              |
| ----- | ----------------------------------------------------------------------------------------------------------------- |
| class | [**Encoder< BMXImageAttachment >**](classfloo_1_1_b_m_x_image_attachment.md#friend-encoder<-bmximageattachment->) |
| class | [**Decoder< BMXImageAttachment >**](classfloo_1_1_b_m_x_image_attachment.md#friend-decoder<-bmximageattachment->) |

## Additional inherited members

**Public Functions inherited from** [**floo::BMXFileAttachment**](classfloo_1_1_b_m_x_file_attachment.md)

|                                                                                 | Name                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                 | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(const std::string &#x26; path, const std::string &#x26; displayName ="")<br>Constructor to build the message attachment of sent file</p>                         |
|                                                                                 | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(const std::string &#x26; ratelUrl, const std::string &#x26; displayName, int64_t fileLength)<br>Constructor to build the message attachment of received file</p> |
| virtual                                                                         | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-~bmxfileattachment"><strong>~BMXFileAttachment</strong></a>()<br>Destructor</p>                                                                                                                                            |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-path"><strong>path</strong></a>() const<br>Local path</p>                                                                                                                                                                  |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-displayname"><strong>displayName</strong></a>() const<br>Display name</p>                                                                                                                                                  |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-ratelurl"><strong>ratelUrl</strong></a>() const<br>URL for remote ratel</p>                                                                                                                                                |
| const std::string &                                                             | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-url"><strong>url</strong></a>() const<br>URL for remote</p>                                                                                                                                                                |
| int64\_t                                                                        | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-filelength"><strong>fileLength</strong></a>() const<br>File length</p>                                                                                                                                                     |
| [DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus) | <p><a href="classfloo_1_1_b_m_x_file_attachment.md#function-downloadstatus"><strong>downloadStatus</strong></a>() const<br>Attachment download state</p>                                                                                                                               |

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

|            | Name                                                                                                                                                                                                 |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-type"><strong>Type</strong></a> { Image, Voice, Video, File, Location, Command, Forward}<br>Attachment type</p>                           |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus"><strong>DownloadStatus</strong></a> { Downloaing, Successed, Failed, NotStart, Canceled}<br>Attachment download state</p> |

**Public Functions inherited from** [**floo::BMXMessageAttachment**](classfloo_1_1_b_m_x_message_attachment.md)

|         | Name                                                                                                                                                 |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|         | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment"><strong>BMXMessageAttachment</strong></a>()<br>Constructor</p>  |
| virtual | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment"><strong>~BMXMessageAttachment</strong></a>()<br>Destructor</p> |

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXImageAttachment'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXImageAttachment'></div>

```

### function \~BMXImageAttachment

```cpp
inline virtual ~BMXImageAttachment()
```

Destructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXImageAttachment'></div>

```

### function type

```cpp
inline virtual Type type() const
```

Return the type of picture attachment

**Return**: Type

**Reimplements**: [floo::BMXFileAttachment::type](classfloo_1_1_b_m_x_file_attachment.md#function-type)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXImageAttachment'></div>

```

### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

Cloning function

**Return**: BMXMessageAttachmentPtr

**Reimplements**: [floo::BMXFileAttachment::clone](classfloo_1_1_b_m_x_file_attachment.md#function-clone)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXImageAttachment'></div>

```

### function size

```cpp
const Size & size() const
```

Picture size

**Return**: Size

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXImageAttachment'></div>

```

### function thumbnailUrl

```cpp
const std::string & thumbnailUrl() const
```

Thumbnail url for remote use

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXImageAttachment'></div>

```

### function setThumbnail

```cpp
void setThumbnail(
    const std::string & path
)
```

Set a thumbnail for sent picture

**Parameters**:

* **path** Local path

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXImageAttachment'></div>

```

### function thumbnailPath

```cpp
const std::string & thumbnailPath() const
```

Local path of thumbnail

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXImageAttachment'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXImageAttachment'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
