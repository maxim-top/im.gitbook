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


### function BMXImageAttachment

```java
inline BMXImageAttachment(
    String path,
    BMXMessageAttachment.Size size
)
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


### function type

```java
inline BMXMessageAttachment.Type type()
```

Return the type of picture attachment 

**Return**: Type 

**Reimplements**: [im::floo::floolib::BMXFileAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-type)


### function clone

```java
inline BMXMessageAttachment clone()
```

Cloning function 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [im::floo::floolib::BMXFileAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-clone)


### function size

```java
inline BMXMessageAttachment.Size size()
```

Picture size 

**Return**: Size 

### function thumbnailUrl

```java
inline String thumbnailUrl()
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


### function thumbnailPath

```java
inline String thumbnailPath()
```

Local path of thumbnail 

**Return**: std::string 

### function thumbnailDownloadStatus

```java
inline BMXMessageAttachment.DownloadStatus thumbnailDownloadStatus()
```

Thumbnail downloading state 

**Return**: DownloadStatus 

### function dynamic_cast

```java
static inline BMXImageAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```


**Reimplements**: [im::floo::floolib::BMXFileAttachment::dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-dynamic-cast)


## Protected Functions Documentation

### function BMXImageAttachment

```java
inline BMXImageAttachment(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


**Reimplements**: [im::floo::floolib::BMXFileAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_file_attachment.md#function-finalize)


### function getCPtr

```java
static inline long getCPtr(
    BMXImageAttachment obj
)
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800