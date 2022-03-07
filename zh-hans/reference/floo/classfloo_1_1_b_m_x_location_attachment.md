---
title: floo::BMXLocationAttachment
summary: 位置消息附件 

---

# floo::BMXLocationAttachment



位置消息附件 


`#include <bmx_location_attachment.h>`

Inherits from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXLocationAttachment](classfloo_1_1_b_m_x_location_attachment.md#function-bmxlocationattachment)**(double latitude, double longitude, const std::string & address)<br>构造函数  |
| virtual | **[~BMXLocationAttachment](classfloo_1_1_b_m_x_location_attachment.md#function-~bmxlocationattachment)**()<br>析构函数  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_location_attachment.md#function-type)**() const<br>返回位置附件类型  |
| virtual BMXMessageAttachmentPtr | **[clone](classfloo_1_1_b_m_x_location_attachment.md#function-clone)**() const<br>克隆函数  |
| double | **[latitude](classfloo_1_1_b_m_x_location_attachment.md#function-latitude)**() const<br>纬度  |
| double | **[longitude](classfloo_1_1_b_m_x_location_attachment.md#function-longitude)**() const<br>经度  |
| const std::string & | **[address](classfloo_1_1_b_m_x_location_attachment.md#function-address)**() const<br>地址  |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[Encoder< BMXLocationAttachment >](classfloo_1_1_b_m_x_location_attachment.md#friend-encoder<-bmxlocationattachment->)**  |
| class | **[Decoder< BMXLocationAttachment >](classfloo_1_1_b_m_x_location_attachment.md#friend-decoder<-bmxlocationattachment->)**  |

## Additional inherited members

**Public Types inherited from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| enum class| **[Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type)** { Image, Voice, Video, File, Location, Command, Forward}<br>附件类型  |
| enum class| **[DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus)** { Downloaing, Successed, Failed, NotStart, Canceled}<br>附件下载状态  |

**Public Functions inherited from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**()<br>构造函数  |
| virtual | **[~BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment)**()<br>析构函数  |


## Public Functions Documentation

### function BMXLocationAttachment

```cpp
BMXLocationAttachment(
    double latitude,
    double longitude,
    const std::string & address
)
```

构造函数 

**Parameters**: 

  * **latitude** 纬度 
  * **longitude** 经度 
  * **address** 地址名称 


### function ~BMXLocationAttachment

```cpp
inline virtual ~BMXLocationAttachment()
```

析构函数 

### function type

```cpp
inline virtual Type type() const
```

返回位置附件类型 

**Return**: Type 

**Reimplements**: [floo::BMXMessageAttachment::type](classfloo_1_1_b_m_x_message_attachment.md#function-type)


### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

克隆函数 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [floo::BMXMessageAttachment::clone](classfloo_1_1_b_m_x_message_attachment.md#function-clone)


### function latitude

```cpp
double latitude() const
```

纬度 

**Return**: double 

### function longitude

```cpp
double longitude() const
```

经度 

**Return**: double 

### function address

```cpp
const std::string & address() const
```

地址 

**Return**: std::string 

## Friends

### friend Encoder< BMXLocationAttachment >

```cpp
friend class Encoder< BMXLocationAttachment >(
    Encoder< BMXLocationAttachment > 
);
```


### friend Decoder< BMXLocationAttachment >

```cpp
friend class Decoder< BMXLocationAttachment >(
    Decoder< BMXLocationAttachment > 
);
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800