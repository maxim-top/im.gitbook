---
title: im::floo::floolib::BMXLocationAttachment
summary: 位置消息附件
---

# im::floo::floolib::BMXLocationAttachment

位置消息附件

Inherits from [im.floo.floolib.BMXMessageAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md), BMXBaseObject

## Public Functions

|                                                                                                 | Name                                                                                                                                                                                                                        |
| ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void                                                                               | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_location\_attachment.md#function-delete)()                                                                                                                      |
|                                                                                                 | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-bmxlocationattachment"><strong>BMXLocationAttachment</strong></a>(double latitude, double longitude, String address)<br>构造函数</p>           |
| BMXMessageAttachment.Type                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-type"><strong>type</strong></a>()<br>返回位置附件类型</p>                                                                                          |
| [BMXMessageAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md)   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-clone"><strong>clone</strong></a>()<br>克隆函数</p>                                                                                            |
| double                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-latitude"><strong>latitude</strong></a>()<br>纬度</p>                                                                                        |
| double                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-longitude"><strong>longitude</strong></a>()<br>经度</p>                                                                                      |
| String                                                                                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-address"><strong>address</strong></a>()<br>地址</p>                                                                                          |
| [BMXLocationAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_location\_attachment.md) | [**dynamic\_cast**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_location\_attachment.md#function-dynamic-cast)([BMXMessageAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md) attachment) |

## Protected Functions

|      | Name                                                                                                                                                                                                        |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXLocationAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_location\_attachment.md#function-bmxlocationattachment)(long cPtr, boolean cMemoryOwn)                                           |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_location\_attachment.md#function-finalize)()                                                                                                  |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_location\_attachment.md#function-getcptr)([BMXLocationAttachment](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_location\_attachment.md) obj) |

## Additional inherited members

**Protected Functions inherited from** [**im.floo.floolib.BMXMessageAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md)

|   | Name                                                                                                                                                           |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | [**BMXMessageAttachment**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md#function-bmxmessageattachment)(long cPtr, boolean cMemoryOwn) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::delete](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md#function-delete)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXLocationAttachment'></div>
```

### function BMXLocationAttachment

```java
inline BMXLocationAttachment(
    double latitude,
    double longitude,
    String address
)
```

构造函数

**Parameters**:

* **latitude** 纬度
* **longitude** 经度
* **address** 地址名称

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXLocationAttachment'></div>
```

### function type

```java
inline BMXMessageAttachment.Type type()
```

返回位置附件类型

**Return**: Type

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::type](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md#function-type)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXLocationAttachment'></div>
```

### function clone

```java
inline BMXMessageAttachment clone()
```

克隆函数

**Return**: BMXMessageAttachmentPtr

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::clone](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md#function-clone)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXLocationAttachment'></div>
```

### function latitude

```java
inline double latitude()
```

纬度

**Return**: double

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXLocationAttachment'></div>
```

### function longitude

```java
inline double longitude()
```

经度

**Return**: double

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXLocationAttachment'></div>
```

### function address

```java
inline String address()
```

地址

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXLocationAttachment'></div>
```

### function dynamic\_cast

```java
static inline BMXLocationAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXLocationAttachment'></div>
```

### function BMXLocationAttachment

```java
inline BMXLocationAttachment(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXLocationAttachment'></div>
```

### function finalize

```java
inline void finalize()
```

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::finalize](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_message\_attachment.md#function-finalize)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXLocationAttachment'></div>
```

### function getCPtr

```java
static inline long getCPtr(
    BMXLocationAttachment obj
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXLocationAttachment'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
