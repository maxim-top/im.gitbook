---
title: floo::BMXDevice
summary: 设备信息
---

# floo::BMXDevice

设备信息

`#include <bmx_device.h>`

Inherits from BMXBaseObject

## Public Functions

|                     | Name                                                                                                                                                      |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual             | <p><a href="classfloo_1_1_b_m_x_device.md#function-~bmxdevice"><strong>~BMXDevice</strong></a>()<br>析构函数</p>                                              |
| virtual int         | <p><a href="classfloo_1_1_b_m_x_device.md#function-devicesn"><strong>deviceSN</strong></a>() =0<br>设备序列号</p>                                              |
| virtual int64\_t    | <p><a href="classfloo_1_1_b_m_x_device.md#function-userid"><strong>userId</strong></a>() =0<br>用户id</p>                                                   |
| virtual int         | <p><a href="classfloo_1_1_b_m_x_device.md#function-platform"><strong>platform</strong></a>() =0<br>软件平台</p>                                               |
| virtual std::string | <p><a href="classfloo_1_1_b_m_x_device.md#function-useragent"><strong>userAgent</strong></a>() =0<br>用户代理信息</p>                                           |
| virtual void        | <p><a href="classfloo_1_1_b_m_x_device.md#function-setuseragent"><strong>setUserAgent</strong></a>(const std::string &#x26; userAgent) =0<br>设置用户代理信息</p> |
| virtual bool        | <p><a href="classfloo_1_1_b_m_x_device.md#function-iscurrentdevice"><strong>isCurrentDevice</strong></a>() =0<br>是否是当前设备</p>                              |

## Protected Functions

|   | Name                                                                      |
| - | ------------------------------------------------------------------------- |
|   | [**BMXDevice**](classfloo\_1\_1\_b\_m\_x\_device.md#function-bmxdevice)() |

## Public Functions Documentation

### function \~BMXDevice

```cpp
inline virtual ~BMXDevice()
```

析构函数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>
```

### function deviceSN

```cpp
virtual int deviceSN() =0
```

设备序列号

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>
```

### function userId

```cpp
virtual int64_t userId() =0
```

用户id

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>
```

### function platform

```cpp
virtual int platform() =0
```

软件平台

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>
```

### function userAgent

```cpp
virtual std::string userAgent() =0
```

用户代理信息

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>
```

### function setUserAgent

```cpp
virtual void setUserAgent(
    const std::string & userAgent
) =0
```

设置用户代理信息

**Parameters**:

* **userAgent** 用户代理信息

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>
```

### function isCurrentDevice

```cpp
virtual bool isCurrentDevice() =0
```

是否是当前设备

**Return**: bool

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>
```

### function BMXDevice

```cpp
inline BMXDevice()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
