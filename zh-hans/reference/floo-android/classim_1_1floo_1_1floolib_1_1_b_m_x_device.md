---
title: im::floo::floolib::BMXDevice
summary: 设备信息
---

# im::floo::floolib::BMXDevice

设备信息

## Public Functions

|                   | Name                                                                                                                                                  |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-delete)()                                                                        |
| int               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-devicesn"><strong>deviceSN</strong></a>()<br>设备序列号</p>                            |
| long              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-userid"><strong>userId</strong></a>()<br>用户id</p>                                 |
| int               | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-platform"><strong>platform</strong></a>()<br>软件平台</p>                             |
| String            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-useragent"><strong>userAgent</strong></a>()<br>用户代理信息</p>                         |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-setuseragent"><strong>setUserAgent</strong></a>(String userAgent)<br>设置用户代理信息</p> |
| boolean           | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-iscurrentdevice"><strong>isCurrentDevice</strong></a>()<br>是否是当前设备</p>            |

## Protected Functions

|      | Name                                                                                                                                            |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXDevice**](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-bmxdevice)(long cPtr, boolean cMemoryOwn)                               |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-finalize)()                                                              |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-getcptr)([BMXDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md) obj) |

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

设备序列号

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>

```

### function userId

```java
inline long userId()
```

用户id

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>

```

### function platform

```java
inline int platform()
```

软件平台

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>

```

### function userAgent

```java
inline String userAgent()
```

用户代理信息

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

设置用户代理信息

**Parameters**:

* **userAgent** 用户代理信息

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXDevice'></div>

```

### function isCurrentDevice

```java
inline boolean isCurrentDevice()
```

是否是当前设备

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

***

Updated on 2022-01-26 at 17:18:31 +0800
