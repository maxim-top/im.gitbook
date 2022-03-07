---
title: im::floo::floolib::BMXLocationAttachment
summary: Location message attachment 

---

# im::floo::floolib::BMXLocationAttachment



Location message attachment 

Inherits from [im.floo.floolib.BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md), BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-delete)**() |
| | **[BMXLocationAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-bmxlocationattachment)**(double latitude, double longitude, String address)<br>Constructor  |
| BMXMessageAttachment.Type | **[type](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-type)**()<br>Return the type of location attachment  |
| [BMXMessageAttachment](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md) | **[clone](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-clone)**()<br>Cloning function  |
| double | **[latitude](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-latitude)**()<br>Latitude  |
| double | **[longitude](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-longitude)**()<br>Longitude  |
| String | **[address](classim_1_1floo_1_1floolib_1_1_b_m_x_location_attachment.md#function-address)**()<br>Address  |
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


### function BMXLocationAttachment

```java
inline BMXLocationAttachment(
    double latitude,
    double longitude,
    String address
)
```

Constructor 

**Parameters**: 

  * **latitude** Latitude 
  * **longitude** Longitude 
  * **address** Address name 


### function type

```java
inline BMXMessageAttachment.Type type()
```

Return the type of location attachment 

**Return**: Type 

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::type](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-type)


### function clone

```java
inline BMXMessageAttachment clone()
```

Cloning function 

**Return**: BMXMessageAttachmentPtr 

**Reimplements**: [im::floo::floolib::BMXMessageAttachment::clone](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-clone)


### function latitude

```java
inline double latitude()
```

Latitude 

**Return**: double 

### function longitude

```java
inline double longitude()
```

Longitude 

**Return**: double 

### function address

```java
inline String address()
```

Address 

**Return**: std::string 

### function dynamic_cast

```java
static inline BMXLocationAttachment dynamic_cast(
    BMXMessageAttachment attachment
)
```


## Protected Functions Documentation

### function BMXLocationAttachment

```java
inline BMXLocationAttachment(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


**Reimplements**: [im::floo::floolib::BMXMessageAttachment::finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_message_attachment.md#function-finalize)


### function getCPtr

```java
static inline long getCPtr(
    BMXLocationAttachment obj
)
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800