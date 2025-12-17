---
title: im::floo::floolib::BMXFileAttachment
summary: 消息文件附件
---

# im::floo::floolib::BMXFileAttachment

消息文件附件

Inherits from [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

Inherited by [im.floo.floolib.BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md), [im.floo.floolib.BMXVideoAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md), [im.floo.floolib.BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md)

## Public Functions

|                                                                                    | Name                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void                                                                  | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-delete)()                                                                                                                             |
|                                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(String path, String displayName)<br>构造函数，构建发送文件消息附件</p>                      |
|                                                                                    | [**BMXFileAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)(String path)                                                                                            |
|                                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment"><strong>BMXFileAttachment</strong></a>(String ratelUrl, String displayName, long fileLength)<br>构造函数，构建接收文件消息附件</p> |
| BMXMessageAttachment.Type                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-type"><strong>type</strong></a>()<br>返回文件类型</p>                                                                                        |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-clone"><strong>clone</strong></a>()<br>克隆函数</p>                                                                                        |
| String                                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-path"><strong>path</strong></a>()<br>本地路径</p>                                                                                          |
| String                                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-displayname"><strong>displayName</strong></a>()<br>显示名</p>                                                                             |
| String                                                                             | [**ratelUrl**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-ratelurl)()                                                                                                                         |
| String                                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-url"><strong>url</strong></a>()<br>远程URL</p>                                                                                           |
| long                                                                               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-filelength"><strong>fileLength</strong></a>()<br>文件长度</p>                                                                              |
| BMXMessageAttachment.DownloadStatus                                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-downloadstatus"><strong>downloadStatus</strong></a>()<br>附件下载状态</p>                                                                    |
| [BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md)       | [**dynamic\_cast**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-dynamic-cast)([BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment)                   |

## Protected Functions

|      | Name                                                                                                                                                                      |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXFileAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)(long cPtr, boolean cMemoryOwn)                                |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-finalize)()                                                                               |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-getcptr)([BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md) obj) |

## Additional inherited members

**Protected Functions inherited from** [**im.floo.floolib.BMXMessageAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md)

|   | Name                                                                                                                                                |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [**BMXMessageAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)(long cPtr, boolean cMemoryOwn) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-delete)

**Reimplemented by**: [im::floo::floolib::BMXImageAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-delete), [im::floo::floolib::BMXVideoAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-delete), [im::floo::floolib::BMXVoiceAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-delete)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function BMXFileAttachment

```java
inline BMXFileAttachment(
    String path,
    String displayName
)
```

构造函数，构建发送文件消息附件

**Parameters**:

* **path** 文件的本地路径
* **displayName** 文件展示名

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function BMXFileAttachment

```java
inline BMXFileAttachment(
    String path
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function BMXFileAttachment

```java
inline BMXFileAttachment(
    String ratelUrl,
    String displayName,
    long fileLength
)
```

构造函数，构建接收文件消息附件

**Parameters**:

* **ratelUrl** ratel服务器地址
* **displayName** 文件展示名
* **fileLength** 文件大小

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function type

```java
inline BMXMessageAttachment.Type type()
```

返回文件类型

**Return**: Type

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-type)

**Reimplemented by**: [im::floo::floolib::BMXImageAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-type), [im::floo::floolib::BMXVideoAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-type), [im::floo::floolib::BMXVoiceAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-type)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function clone

```java
inline BMXMessageAttachment clone()
```

克隆函数

**Return**: BMXMessageAttachmentPtr

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-clone)

**Reimplemented by**: [im::floo::floolib::BMXImageAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-clone), [im::floo::floolib::BMXVideoAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-clone), [im::floo::floolib::BMXVoiceAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-clone)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function path

```java
inline String path()
```

本地路径

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function displayName

```java
inline String displayName()
```

显示名

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function ratelUrl

```java
inline String ratelUrl()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function url

```java
inline String url()
```

远程URL

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function fileLength

```java
inline long fileLength()
```

文件长度

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function downloadStatus

```java
inline BMXMessageAttachment.DownloadStatus downloadStatus()
```

附件下载状态

**Return**: DownloadStatus

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function dynamic\_cast

```java
static inline BMXFileAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```

**Reimplemented by**: [im::floo::floolib::BMXImageAttachment::dynamic\_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-dynamic-cast), [im::floo::floolib::BMXVideoAttachment::dynamic\_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-dynamic-cast), [im::floo::floolib::BMXVoiceAttachment::dynamic\_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-dynamic-cast)

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function BMXFileAttachment

```java
inline BMXFileAttachment(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function finalize

```java
inline void finalize()
```

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-finalize)

**Reimplemented by**: [im::floo::floolib::BMXImageAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-finalize), [im::floo::floolib::BMXVideoAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_video_attachment.md#function-finalize), [im::floo::floolib::BMXVoiceAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-finalize)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>

```

### function getCPtr

```java
static inline long getCPtr(
    BMXFileAttachment obj
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXFileAttachment'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
