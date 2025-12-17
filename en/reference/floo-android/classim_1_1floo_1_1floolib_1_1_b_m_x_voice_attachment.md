---
title: im::floo::floolib::BMXVoiceAttachment
summary: Audio attachment
---

# im::floo::floolib::BMXVoiceAttachment

Audio attachment

Inherits from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md), [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                                                                                    | Name                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void                                                                  | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-delete)()                                                                                                                                                                                  |
|                                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment"><strong>BMXVoiceAttachment</strong></a>(String path, int duration, String displayName)<br>Constructor to build the audio attachment to send</p>                         |
|                                                                                    | [**BMXVoiceAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)(String path, int duration)                                                                                                                                 |
|                                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment"><strong>BMXVoiceAttachment</strong></a>(String ratelUrl, int duration, String displayName, long fileLength)<br>Constructor to build the audio attachment to receive</p> |
| BMXMessageAttachment.Type                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-type"><strong>type</strong></a>()<br>Type of returned file</p>                                                                                                                              |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-clone"><strong>clone</strong></a>()<br>Cloning function</p>                                                                                                                                 |
| int                                                                                | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-duration"><strong>duration</strong></a>()<br>Length of speech</p>                                                                                                                           |
| [BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md)     | [**dynamic\_cast**](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-dynamic-cast)([BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment)                                                                        |

## Protected Functions

|      | Name                                                                                                                                                                         |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXVoiceAttachment**](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)(long cPtr, boolean cMemoryOwn)                                |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-finalize)()                                                                                 |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-getcptr)([BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md) obj) |

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVoiceAttachment'></div>

```

### function BMXVoiceAttachment

```java
inline BMXVoiceAttachment(
    String path,
    int duration,
    String displayName
)
```

Constructor to build the audio attachment to send

**Parameters**:

* **path** Local path of file
* **duration** Audio length
* **displayName** Display name of file

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVoiceAttachment'></div>

```

### function BMXVoiceAttachment

```java
inline BMXVoiceAttachment(
    String path,
    int duration
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVoiceAttachment'></div>

```

### function BMXVoiceAttachment

```java
inline BMXVoiceAttachment(
    String ratelUrl,
    int duration,
    String displayName,
    long fileLength
)
```

Constructor to build the audio attachment to receive

**Parameters**:

* **ratelUrl** ratel server address
* **duration** Audio length
* **displayName** Display name of file
* **fileLength** File size

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVoiceAttachment'></div>

```

### function type

```java
inline BMXMessageAttachment.Type type()
```

Type of returned file

**Return**: Type

**Reimplements**: [im::floo::floolib::BMXFileAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-type)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVoiceAttachment'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVoiceAttachment'></div>

```

### function duration

```java
inline int duration()
```

Length of speech

**Return**: int32\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVoiceAttachment'></div>

```

### function dynamic\_cast

```java
static inline BMXVoiceAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```

**Reimplements**: [im::floo::floolib::BMXFileAttachment::dynamic\_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-dynamic-cast)

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVoiceAttachment'></div>

```

### function BMXVoiceAttachment

```java
inline BMXVoiceAttachment(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVoiceAttachment'></div>

```

### function finalize

```java
inline void finalize()
```

**Reimplements**: [im::floo::floolib::BMXFileAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-finalize)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVoiceAttachment'></div>

```

### function getCPtr

```java
static inline long getCPtr(
    BMXVoiceAttachment obj
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXVoiceAttachment'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
