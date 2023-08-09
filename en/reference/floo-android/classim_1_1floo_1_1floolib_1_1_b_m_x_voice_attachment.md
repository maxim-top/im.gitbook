---
title: im::floo::floolib::BMXVoiceAttachment
summary: Audio attachment 

---

# im::floo::floolib::BMXVoiceAttachment



Audio attachment 

Inherits from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md), [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-delete)**() |
| | **[BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)**(String path, int duration, String displayName)<br>Constructor to build the audio attachment to send  |
| | **[BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)**(String path, int duration) |
| | **[BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)**(String ratelUrl, int duration, String displayName, long fileLength)<br>Constructor to build the audio attachment to receive  |
| BMXMessageAttachment.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-type)**()<br>Type of returned file  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[clone](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-clone)**()<br>Cloning function  |
| int | **[duration](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-duration)**()<br>Length of speech  |
| [BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md) | **[dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-dynamic-cast)**([BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-getcptr)**([BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md) obj) |

## Additional inherited members

**Public Functions inherited from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String path, String displayName)<br>Constructor to build the message attachment of sent file  |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String path) |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String ratelUrl, String displayName, long fileLength)<br>Constructor to build the message attachment of received file  |
| String | **[path](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-path)**()<br>Local path  |
| String | **[displayName](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-displayname)**()<br>Display name  |
| String | **[ratelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-ratelurl)**() |
| String | **[url](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-url)**()<br>Remote URL  |
| long | **[fileLength](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-filelength)**()<br>File length  |
| BMXMessageAttachment.DownloadStatus | **[downloadStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-downloadstatus)**()<br>Attachment download state  |

**Protected Functions inherited from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(long cPtr, boolean cMemoryOwn) |

**Protected Functions inherited from [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**(long cPtr, boolean cMemoryOwn) |


## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


**Reimplements**: [im::floo::floolib::BMXFileAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-delete)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVoiceAttachment",function="delete" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXVoiceAttachment",function="BMXVoiceAttachment" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXVoiceAttachment",function="BMXVoiceAttachment" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXVoiceAttachment",function="BMXVoiceAttachment" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXVoiceAttachment",function="type" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXVoiceAttachment",function="clone" %}{% endlanying_code_snippet %}
```
### function duration

```java
inline int duration()
```

Length of speech 

**Return**: int32_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVoiceAttachment",function="duration" %}{% endlanying_code_snippet %}
```
### function dynamic_cast

```java
static inline BMXVoiceAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```


**Reimplements**: [im::floo::floolib::BMXFileAttachment::dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-dynamic-cast)


## Protected Functions Documentation

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVoiceAttachment",function="dynamic_cast" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXVoiceAttachment",function="BMXVoiceAttachment" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Reimplements**: [im::floo::floolib::BMXFileAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-finalize)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVoiceAttachment",function="finalize" %}{% endlanying_code_snippet %}
```
### function getCPtr

```java
static inline long getCPtr(
    BMXVoiceAttachment obj
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVoiceAttachment",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800