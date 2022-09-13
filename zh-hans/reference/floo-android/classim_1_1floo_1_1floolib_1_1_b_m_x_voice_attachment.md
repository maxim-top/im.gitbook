---
title: im::floo::floolib::BMXVoiceAttachment
summary: 音频消息附件 

---

# im::floo::floolib::BMXVoiceAttachment



音频消息附件 

Inherits from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md), [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-delete)**() |
| | **[BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)**(String path, int duration, String displayName)<br>构造函数，构建发送音频消息附件  |
| | **[BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)**(String path, int duration) |
| | **[BMXVoiceAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-bmxvoiceattachment)**(String ratelUrl, int duration, String displayName, long fileLength)<br>构造函数，构建接收音频消息附件  |
| BMXMessageAttachment.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-type)**()<br>返回文件类型  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[clone](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-clone)**()<br>克隆函数  |
| int | **[duration](classim_1_1floo_1_1floolib_1_1_b_m_x_voice_attachment.md#function-duration)**()<br>语音时长  |
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
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String path, String displayName)<br>构造函数，构建发送文件消息附件  |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String path) |
| | **[BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-bmxfileattachment)**(String ratelUrl, String displayName, long fileLength)<br>构造函数，构建接收文件消息附件  |
| String | **[path](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-path)**()<br>本地路径  |
| String | **[displayName](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-displayname)**()<br>显示名  |
| String | **[ratelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-ratelurl)**() |
| String | **[url](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-url)**()<br>远程URL  |
| long | **[fileLength](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-filelength)**()<br>文件长度  |
| BMXMessageAttachment.DownloadStatus | **[downloadStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-downloadstatus)**()<br>附件下载状态  |

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

构造函数，构建发送音频消息附件 

**Parameters**: 

  * **path** 文件的本地路径 
  * **duration** 音频时长 
  * **displayName** 文件展示名 


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

构造函数，构建接收音频消息附件 

**Parameters**: 

  * **ratelUrl** ratel服务器地址 
  * **duration** 音频时长 
  * **displayName** 文件展示名 
  * **fileLength** 文件大小 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXVoiceAttachment",function="BMXVoiceAttachment" %}{% endlanying_code_snippet %}
```
### function type

```java
inline BMXMessageAttachment.Type type()
```

返回文件类型 

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

克隆函数 

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

语音时长 

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