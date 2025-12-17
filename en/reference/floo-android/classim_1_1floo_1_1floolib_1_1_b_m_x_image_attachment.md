---
title: im::floo::floolib::BMXImageAttachment
summary: Message picture attachment
---

# im::floo::floolib::BMXImageAttachment

Message picture attachment

Inherits from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md), [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                                                                                    | Name                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void                                                                  | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-delete)()                                                                                                                                                                                                                |
|                                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment"><strong>BMXImageAttachment</strong></a>(String path, BMXMessageAttachment.Size size, String displayName)<br>Constructor, to build the message attachment of sent picture</p>                          |
|                                                                                    | [**BMXImageAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment)(String path, BMXMessageAttachment.Size size)                                                                                                                                             |
|                                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment"><strong>BMXImageAttachment</strong></a>(String ratelUrl, BMXMessageAttachment.Size size, String displayName, long fileLength)<br>Constructor, to build the message attachment of received picture</p> |
| BMXMessageAttachment.Type                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-type"><strong>type</strong></a>()<br>Return the type of picture attachment</p>                                                                                                                                            |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-clone"><strong>clone</strong></a>()<br>Cloning function</p>                                                                                                                                                               |
| BMXMessageAttachment.Size                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-size"><strong>size</strong></a>()<br>Picture size</p>                                                                                                                                                                     |
| String                                                                             | [**thumbnailUrl**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-thumbnailurl)()                                                                                                                                                                                                    |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-setthumbnail"><strong>setThumbnail</strong></a>(String path)<br>Set a thumbnail for sent picture</p>                                                                                                                      |
| String                                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-thumbnailpath"><strong>thumbnailPath</strong></a>()<br>Local path of thumbnail</p>                                                                                                                                        |
| BMXMessageAttachment.DownloadStatus                                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-thumbnaildownloadstatus"><strong>thumbnailDownloadStatus</strong></a>()<br>Thumbnail downloading state</p>                                                                                                                |
| [BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md)     | [**dynamic\_cast**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-dynamic-cast)([BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment)                                                                                                      |

## Protected Functions

|      | Name                                                                                                                                                                         |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXImageAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment)(long cPtr, boolean cMemoryOwn)                                |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-finalize)()                                                                                 |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-getcptr)([BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md) obj) |

## Additional inherited members

**Public Functions inherited from** [**im.floo.floolib.BMXFileAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md)

|                                     | Name                                                                                                                                                                                                                                                             |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(String path, String displayName)<br>Constructor to build the message attachment of sent file</p>                          |
|                                     | [**BMXFileAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)(String path)                                                                                                                                         |
|                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(String ratelUrl, String displayName, long fileLength)<br>Constructor to build the message attachment of received file</p> |
| String                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-path"><strong>path</strong></a>()<br>Local path</p>                                                                                                                                 |
| String                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-displayname"><strong>displayName</strong></a>()<br>Display name</p>                                                                                                                 |
| String                              | [**ratelUrl**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-ratelurl)()                                                                                                                                                                      |
| String                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-url"><strong>url</strong></a>()<br>Remote URL</p>                                                                                                                                   |
| long                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-filelength"><strong>fileLength</strong></a>()<br>File length</p>                                                                                                                    |
| BMXMessageAttachment.DownloadStatus | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-downloadstatus"><strong>downloadStatus</strong></a>()<br>Attachment download state</p>                                                                                              |

**Protected Functions inherited from** [**im.floo.floolib.BMXFileAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md)

|   | Name                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------------ |
|   | [**BMXFileAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)(long cPtr, boolean cMemoryOwn) |

**Protected Functions inherited from** [**im.floo.floolib.BMXMessageAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md)

|   | Name                                                                                                                                                |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [**BMXMessageAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)(long cPtr, boolean cMemoryOwn) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Reimplements**: [im::floo::floolib::BMXFileAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-delete)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function BMXImageAttachment

```java
inline BMXImageAttachment(
    String path,
    BMXMessageAttachment.Size size,
    String displayName
)
```

Constructor, to build the message attachment of sent picture

**Parameters**:

* **path** Local path
* **size** Size, width, and height of image
* **displayName** Display name

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function BMXImageAttachment

```java
inline BMXImageAttachment(
    String path,
    BMXMessageAttachment.Size size
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function BMXImageAttachment

```java
inline BMXImageAttachment(
    String ratelUrl,
    BMXMessageAttachment.Size size,
    String displayName,
    long fileLength
)
```

Constructor, to build the message attachment of received picture

**Parameters**:

* **ratelUrl** ratel server address
* **size** Size, width, and height of image
* **displayName** Display name
* **fileLength** File size

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function type

```java
inline BMXMessageAttachment.Type type()
```

Return the type of picture attachment

**Return**: Type

**Reimplements**: [im::floo::floolib::BMXFileAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-type)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function clone

```java
inline BMXMessageAttachment clone()
```

Cloning function

**Return**: BMXMessageAttachmentPtr

**Reimplements**: [im::floo::floolib::BMXFileAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-clone)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function size

```java
inline BMXMessageAttachment.Size size()
```

Picture size

**Return**: Size

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function thumbnailUrl

```java
inline String thumbnailUrl()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function setThumbnail

```java
inline void setThumbnail(
    String path
)
```

Set a thumbnail for sent picture

**Parameters**:

* **path** Local path

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function thumbnailPath

```java
inline String thumbnailPath()
```

Local path of thumbnail

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function thumbnailDownloadStatus

```java
inline BMXMessageAttachment.DownloadStatus thumbnailDownloadStatus()
```

Thumbnail downloading state

**Return**: DownloadStatus

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function dynamic\_cast

```java
static inline BMXImageAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```

**Reimplements**: [im::floo::floolib::BMXFileAttachment::dynamic\_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-dynamic-cast)

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function BMXImageAttachment

```java
inline BMXImageAttachment(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function finalize

```java
inline void finalize()
```

**Reimplements**: [im::floo::floolib::BMXFileAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-finalize)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function getCPtr

```java
static inline long getCPtr(
    BMXImageAttachment obj
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
