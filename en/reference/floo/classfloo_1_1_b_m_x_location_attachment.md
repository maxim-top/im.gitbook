---
title: floo::BMXLocationAttachment
summary: Location message attachment
---

# floo::BMXLocationAttachment

Location message attachment

`#include <bmx_location_attachment.h>`

Inherits from [floo::BMXMessageAttachment](classfloo_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                                                                     | Name                                                                                                                                                                                                                      |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                     | <p><a href="classfloo_1_1_b_m_x_location_attachment.md#function-bmxlocationattachment"><strong>BMXLocationAttachment</strong></a>(double latitude, double longitude, const std::string &#x26; address)<br>Constructor</p> |
| virtual                                                             | <p><a href="classfloo_1_1_b_m_x_location_attachment.md#function-~bmxlocationattachment"><strong>~BMXLocationAttachment</strong></a>()<br>Destructor</p>                                                                   |
| virtual [Type](classfloo_1_1_b_m_x_message_attachment.md#enum-type) | <p><a href="classfloo_1_1_b_m_x_location_attachment.md#function-type"><strong>type</strong></a>() const<br>Return the type of location attachment</p>                                                                     |
| virtual BMXMessageAttachmentPtr                                     | <p><a href="classfloo_1_1_b_m_x_location_attachment.md#function-clone"><strong>clone</strong></a>() const<br>Cloning function</p>                                                                                         |
| double                                                              | <p><a href="classfloo_1_1_b_m_x_location_attachment.md#function-latitude"><strong>latitude</strong></a>() const<br>Latitude</p>                                                                                           |
| double                                                              | <p><a href="classfloo_1_1_b_m_x_location_attachment.md#function-longitude"><strong>longitude</strong></a>() const<br>Longitude</p>                                                                                        |
| const std::string &                                                 | <p><a href="classfloo_1_1_b_m_x_location_attachment.md#function-address"><strong>address</strong></a>() const<br>Address</p>                                                                                              |

## Friends

|       | Name                                                                                                                       |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |
| class | [**Encoder< BMXLocationAttachment >**](classfloo_1_1_b_m_x_location_attachment.md#friend-encoder<-bmxlocationattachment->) |
| class | [**Decoder< BMXLocationAttachment >**](classfloo_1_1_b_m_x_location_attachment.md#friend-decoder<-bmxlocationattachment->) |

## Additional inherited members

**Public Types inherited from** [**floo::BMXMessageAttachment**](classfloo_1_1_b_m_x_message_attachment.md)

|            | Name                                                                                                                                                                                                 |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-type"><strong>Type</strong></a> { Image, Voice, Video, File, Location, Command, Forward}<br>Attachment type</p>                           |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#enum-downloadstatus"><strong>DownloadStatus</strong></a> { Downloaing, Successed, Failed, NotStart, Canceled}<br>Attachment download state</p> |

**Public Functions inherited from** [**floo::BMXMessageAttachment**](classfloo_1_1_b_m_x_message_attachment.md)

|         | Name                                                                                                                                                 |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|         | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment"><strong>BMXMessageAttachment</strong></a>()<br>Constructor</p>  |
| virtual | <p><a href="classfloo_1_1_b_m_x_message_attachment.md#function-~bmxmessageattachment"><strong>~BMXMessageAttachment</strong></a>()<br>Destructor</p> |

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXLocationAttachment'></div>

```

### function \~BMXLocationAttachment

```cpp
inline virtual ~BMXLocationAttachment()
```

Destructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXLocationAttachment'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXLocationAttachment'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXLocationAttachment'></div>

```

### function latitude

```cpp
double latitude() const
```

Latitude

**Return**: double

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXLocationAttachment'></div>

```

### function longitude

```cpp
double longitude() const
```

Longitude

**Return**: double

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXLocationAttachment'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXLocationAttachment'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
