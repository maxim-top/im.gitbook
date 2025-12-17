---
title: im::floo::floolib::BMXImageAttachment
summary: 图片消息附件
---

# im::floo::floolib::BMXImageAttachment

图片消息附件

Inherits from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md), [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                                                                                    | Name                                                                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| synchronized void                                                                  | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-delete)()                                                                                                                                                               |
|                                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment"><strong>BMXImageAttachment</strong></a>(String path, BMXMessageAttachment.Size size, String displayName)<br>构造函数，构建发送图片消息附件</p>                      |
|                                                                                    | [**BMXImageAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment)(String path, BMXMessageAttachment.Size size)                                                                                            |
|                                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment"><strong>BMXImageAttachment</strong></a>(String ratelUrl, BMXMessageAttachment.Size size, String displayName, long fileLength)<br>构造函数，构建接收图片消息附件</p> |
| BMXMessageAttachment.Type                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-type"><strong>type</strong></a>()<br>返回图片附件类型</p>                                                                                                                        |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-clone"><strong>clone</strong></a>()<br>克隆函数</p>                                                                                                                          |
| BMXMessageAttachment.Size                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-size"><strong>size</strong></a>()<br>图片大小</p>                                                                                                                            |
| String                                                                             | [**thumbnailUrl**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-thumbnailurl)()                                                                                                                                                   |
| void                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-setthumbnail"><strong>setThumbnail</strong></a>(String path)<br>设置发送图片消息缩略图</p>                                                                                          |
| String                                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-thumbnailpath"><strong>thumbnailPath</strong></a>()<br>缩略图本地路径</p>                                                                                                       |
| BMXMessageAttachment.DownloadStatus                                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-thumbnaildownloadstatus"><strong>thumbnailDownloadStatus</strong></a>()<br>缩略图下载状态</p>                                                                                   |
| [BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md)     | [**dynamic\_cast**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-dynamic-cast)([BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment)                                                     |

## Protected Functions

|      | Name                                                                                                                                                                         |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXImageAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment)(long cPtr, boolean cMemoryOwn)                                |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-finalize)()                                                                                 |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-getcptr)([BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md) obj) |

## Additional inherited members

**Public Functions inherited from** [**im.floo.floolib.BMXFileAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md)

|                                     | Name                                                                                                                                                                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(String path, String displayName)<br>构造函数，构建发送文件消息附件</p>                      |
|                                     | [**BMXFileAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)(String path)                                                                                            |
|                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(String ratelUrl, String displayName, long fileLength)<br>构造函数，构建接收文件消息附件</p> |
| String                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-path"><strong>path</strong></a>()<br>本地路径</p>                                                                                          |
| String                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-displayname"><strong>displayName</strong></a>()<br>显示名</p>                                                                             |
| String                              | [**ratelUrl**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-ratelurl)()                                                                                                                         |
| String                              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-url"><strong>url</strong></a>()<br>远程URL</p>                                                                                           |
| long                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-filelength"><strong>fileLength</strong></a>()<br>文件长度</p>                                                                              |
| BMXMessageAttachment.DownloadStatus | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-downloadstatus"><strong>downloadStatus</strong></a>()<br>附件下载状态</p>                                                                    |

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

构造函数，构建发送图片消息附件

**Parameters**:

* **path** 本地路径
* **size** 图片的大小，宽度和高度
* **displayName** 展示名

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

构造函数，构建接收图片消息附件

**Parameters**:

* **ratelUrl** ratel服务器地址
* **size** 图片的大小，宽度和高度
* **displayName** 展示名
* **fileLength** 文件大小

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function type

```java
inline BMXMessageAttachment.Type type()
```

返回图片附件类型

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

克隆函数

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

图片大小

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

设置发送图片消息缩略图

**Parameters**:

* **path** 本地路径

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function thumbnailPath

```java
inline String thumbnailPath()
```

缩略图本地路径

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXImageAttachment'></div>

```

### function thumbnailDownloadStatus

```java
inline BMXMessageAttachment.DownloadStatus thumbnailDownloadStatus()
```

缩略图下载状态

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
