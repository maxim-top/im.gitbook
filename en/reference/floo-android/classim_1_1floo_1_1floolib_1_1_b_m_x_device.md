---
title: im::floo::floolib::BMXDevice
summary: Device information
---

# im::floo::floolib::BMXDevice

Device information

## Public Functions

|                   | Name                                                                                                                                                                    |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_device.md#function-delete)()                                                                                |
| int               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-devicesn"><strong>deviceSN</strong></a>()<br>Device serial number</p>                               |
| long              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-userid"><strong>userId</strong></a>()<br>User id</p>                                                |
| int               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-platform"><strong>platform</strong></a>()<br>Software platform</p>                                  |
| String            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-useragent"><strong>userAgent</strong></a>()<br>User agent information</p>                           |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-setuseragent"><strong>setUserAgent</strong></a>(String userAgent)<br>Set user agent information</p> |
| boolean           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-iscurrentdevice"><strong>isCurrentDevice</strong></a>()<br>Whether for the current device</p>       |

## Protected Functions

|      | Name                                                                                                                                                                |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXDevice**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_device.md#function-bmxdevice)(long cPtr, boolean cMemoryOwn)                                         |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_device.md#function-finalize)()                                                                        |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_device.md#function-getcptr)([BMXDevice](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_device.md) obj) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>
```

### function deviceSN

```java
inline int deviceSN()
```

Device serial number

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>
```

### function userId

```java
inline long userId()
```

User id

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>
```

### function platform

```java
inline int platform()
```

Software platform

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>
```

### function userAgent

```java
inline String userAgent()
```

User agent information

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>
```

### function setUserAgent

```java
inline void setUserAgent(
    String userAgent
)
```

Set user agent information

**Parameters**:

* **userAgent** User agent information

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>
```

### function isCurrentDevice

```java
inline boolean isCurrentDevice()
```

Whether for the current device

**Return**: bool

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>
```

### function BMXDevice

```java
inline BMXDevice(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>
```

### function finalize

```java
inline void finalize()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>
```

### function getCPtr

```java
static inline long getCPtr(
    BMXDevice obj
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
