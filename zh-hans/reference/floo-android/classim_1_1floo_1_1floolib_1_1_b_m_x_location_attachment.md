---
title: im::floo::floolib::BMXLocationAttachment
summary: 位置消息附件 

---

# im::floo::floolib::BMXLocationAttachment



位置消息附件 

Inherits from [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-delete)**() |
| | **[BMXLocationAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-bmxlocationattachment)**(double latitude, double longitude, String address)<br>构造函数  |
| BMXMessageAttachment.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-type)**()<br>返回位置附件类型  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[clone](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-clone)**()<br>克隆函数  |
| double | **[latitude](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-latitude)**()<br>纬度  |
| double | **[longitude](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-longitude)**()<br>经度  |
| String | **[address](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-address)**()<br>地址  |
| [BMXLocationAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md) | **[dynamic_cast](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-dynamic-cast)**([BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) attachment) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXLocationAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-bmxlocationattachment)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-getcptr)**([BMXLocationAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md) obj) |

## Additional inherited members

**Protected Functions inherited from [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md)**

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-bmxmessageattachment)**(long cPtr, boolean cMemoryOwn) |


## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


**Reimplements**: [im::floo::floolib::BMXMessageAttachment::delete](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-delete)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXLocationAttachment",function="delete" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXLocationAttachment",function="BMXLocationAttachment" %}{% endlanying_code_snippet %}
```
### function type

```java
inline BMXMessageAttachment.Type type()
```

返回位置附件类型 

**Return**: Type 

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-type)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXLocationAttachment",function="type" %}{% endlanying_code_snippet %}
```
### function clone

```java
inline BMXMessageAttachment clone()
```

克隆函数 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-clone)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXLocationAttachment",function="clone" %}{% endlanying_code_snippet %}
```
### function latitude

```java
inline double latitude()
```

纬度 

**Return**: double 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXLocationAttachment",function="latitude" %}{% endlanying_code_snippet %}
```
### function longitude

```java
inline double longitude()
```

经度 

**Return**: double 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXLocationAttachment",function="longitude" %}{% endlanying_code_snippet %}
```
### function address

```java
inline String address()
```

地址 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXLocationAttachment",function="address" %}{% endlanying_code_snippet %}
```
### function dynamic_cast

```java
static inline BMXLocationAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```


## Protected Functions Documentation

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXLocationAttachment",function="dynamic_cast" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXLocationAttachment",function="BMXLocationAttachment" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Reimplements**: [im::floo::floolib::BMXMessageAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-finalize)


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXLocationAttachment",function="finalize" %}{% endlanying_code_snippet %}
```
### function getCPtr

```java
static inline long getCPtr(
    BMXLocationAttachment obj
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXLocationAttachment",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800