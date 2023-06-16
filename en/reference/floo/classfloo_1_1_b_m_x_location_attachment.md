---
title: floo::BMXLocationAttachment
summary: Location message attachment 

---

# floo::BMXLocationAttachment



Location message attachment 


`#include <bmx_location_attachment.h>`

Inherits from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXLocationAttachment](classfloo_1_1_b_m_x_location_attachment.md#function-bmxlocationattachment)**(double latitude, double longitude, const std::string & address)<br>Constructor  |
| virtual | **[~BMXLocationAttachment](classfloo_1_1_b_m_x_location_attachment.md#function-~bmxlocationattachment)**()<br>Destructor  |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | **[type](classfloo_1_1_b_m_x_location_attachment.md#function-type)**() const<br>Return the type of location attachment  |
| virtual BMXMessageAttachmentPtr | **[clone](classfloo_1_1_b_m_x_location_attachment.md#function-clone)**() const<br>Cloning function  |
| double | **[latitude](classfloo_1_1_b_m_x_location_attachment.md#function-latitude)**() const<br>Latitude  |
| double | **[longitude](classfloo_1_1_b_m_x_location_attachment.md#function-longitude)**() const<br>Longitude  |
| const std::string & | **[address](classfloo_1_1_b_m_x_location_attachment.md#function-address)**() const<br>Address  |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[Encoder< BMXLocationAttachment >](classfloo_1_1_b_m_x_location_attachment.md#friend-encoder<-bmxlocationattachment->)**  |
| class | **[Decoder< BMXLocationAttachment >](classfloo_1_1_b_m_x_location_attachment.md#friend-decoder<-bmxlocationattachment->)**  |

## Additional inherited members

**Public Types inherited from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| enum class| **[Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type)** { Image, Voice, Video, File, Location, Command, Forward}<br>Attachment type  |
| enum class| **[DownloadStatus](classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus)** { Downloaing, Successed, Failed, NotStart, Canceled}<br>Attachment download state  |

**Public Functions inherited from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**()<br>Constructor  |
| virtual | **[~BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment)**()<br>Destructor  |


## Public Functions Documentation

### function BMXLocationAttachment

```cpp
BMXLocationAttachment(
    double latitude,
    double longitude,
    const std::string & address
)
```

Constructor 

**Parameters**: 

  * **latitude** Latitude 
  * **longitude** Longitude 
  * **address** Address name 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXLocationAttachment",function="BMXLocationAttachment" %}{% endlanying_code_snippet %}
```
### function ~BMXLocationAttachment

```cpp
inline virtual ~BMXLocationAttachment()
```

Destructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXLocationAttachment",function="~BMXLocationAttachment" %}{% endlanying_code_snippet %}
```
### function type

```cpp
inline virtual Type type() const
```

Return the type of location attachment 

**Return**: Type 

**Reimplements**: [floo::BMXMessageAttachment::type](classfloo_1_1_b_m_x_message_attachment.md#function-type)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXLocationAttachment",function="type" %}{% endlanying_code_snippet %}
```
### function clone

```cpp
virtual BMXMessageAttachmentPtr clone() const
```

Cloning function 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [floo::BMXMessageAttachment::clone](classfloo_1_1_b_m_x_message_attachment.md#function-clone)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXLocationAttachment",function="clone" %}{% endlanying_code_snippet %}
```
### function latitude

```cpp
double latitude() const
```

Latitude 

**Return**: double 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXLocationAttachment",function="latitude" %}{% endlanying_code_snippet %}
```
### function longitude

```cpp
double longitude() const
```

Longitude 

**Return**: double 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXLocationAttachment",function="longitude" %}{% endlanying_code_snippet %}
```
### function address

```cpp
const std::string & address() const
```

Address 

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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXLocationAttachment",function="address" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800