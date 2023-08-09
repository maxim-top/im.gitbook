---
title: im::floo::floolib::BMXImageAttachment
summary: Message picture attachment 

---

# im::floo::floolib::BMXImageAttachment



Message picture attachment 

Inherits from [im.floo.floolib.BMXFileAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md), [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-delete)**() |
| | **[BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment)**(String path, BMXMessageAttachment.Size size, String displayName)<br>Constructor, to build the message attachment of sent picture  |
| | **[BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment)**(String path, BMXMessageAttachment.Size size) |
| | **[BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment)**(String ratelUrl, BMXMessageAttachment.Size size, String displayName, long fileLength)<br>Constructor, to build the message attachment of received picture  |
| BMXMessageAttachment.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-type)**()<br>Return the type of picture attachment  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[clone](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-clone)**()<br>Cloning function  |
| BMXMessageAttachment.Size | **[size](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-size)**()<br>Picture size  |
| String | **[thumbnailUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-thumbnailurl)**() |
| void | **[setThumbnail](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-setthumbnail)**(String path)<br>Set a thumbnail for sent picture  |
| String | **[thumbnailPath](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-thumbnailpath)**()<br>Local path of thumbnail  |
| BMXMessageAttachment.DownloadStatus | **[thumbnailDownloadStatus](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-thumbnaildownloadstatus)**()<br>Thumbnail downloading state  |
| [BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md) | **[dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-dynamic-cast)**([BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-bmximageattachment)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md#function-getcptr)**([BMXImageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_image_attachment.md) obj) |

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
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="delete" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="BMXImageAttachment" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="BMXImageAttachment" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="BMXImageAttachment" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="type" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="clone" %}{% endlanying_code_snippet %}
```
### function size

```java
inline BMXMessageAttachment.Size size()
```

Picture size 

**Return**: Size 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="size" %}{% endlanying_code_snippet %}
```
### function thumbnailUrl

```java
inline String thumbnailUrl()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="thumbnailUrl" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="setThumbnail" %}{% endlanying_code_snippet %}
```
### function thumbnailPath

```java
inline String thumbnailPath()
```

Local path of thumbnail 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="thumbnailPath" %}{% endlanying_code_snippet %}
```
### function thumbnailDownloadStatus

```java
inline BMXMessageAttachment.DownloadStatus thumbnailDownloadStatus()
```

Thumbnail downloading state 

**Return**: DownloadStatus 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="thumbnailDownloadStatus" %}{% endlanying_code_snippet %}
```
### function dynamic_cast

```java
static inline BMXImageAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```


**Reimplements**: [im::floo::floolib::BMXFileAttachment::dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-dynamic-cast)


## Protected Functions Documentation

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="dynamic_cast" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="BMXImageAttachment" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Reimplements**: [im::floo::floolib::BMXFileAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-finalize)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="finalize" %}{% endlanying_code_snippet %}
```
### function getCPtr

```java
static inline long getCPtr(
    BMXImageAttachment obj
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXImageAttachment",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800