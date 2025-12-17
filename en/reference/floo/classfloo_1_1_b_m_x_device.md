---
title: floo::BMXDevice
summary: Device information
---

# floo::BMXDevice

Device information

`#include <bmx_device.h>`

Inherits from BMXBaseObject

## Public Functions

|                     | Name                                                                                                                                                                        |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual             | <p><a href="classfloo_1_1_b_m_x_device.md#function-~bmxdevice"><strong>~BMXDevice</strong></a>()<br>Destructor</p>                                                          |
| virtual int         | <p><a href="classfloo_1_1_b_m_x_device.md#function-devicesn"><strong>deviceSN</strong></a>() =0<br>Device serial number</p>                                                 |
| virtual int64\_t    | <p><a href="classfloo_1_1_b_m_x_device.md#function-userid"><strong>userId</strong></a>() =0<br>User id</p>                                                                  |
| virtual int         | <p><a href="classfloo_1_1_b_m_x_device.md#function-platform"><strong>platform</strong></a>() =0<br>Software platform</p>                                                    |
| virtual std::string | <p><a href="classfloo_1_1_b_m_x_device.md#function-useragent"><strong>userAgent</strong></a>() =0<br>User agent information</p>                                             |
| virtual void        | <p><a href="classfloo_1_1_b_m_x_device.md#function-setuseragent"><strong>setUserAgent</strong></a>(const std::string &#x26; userAgent) =0<br>Set user agent information</p> |
| virtual bool        | <p><a href="classfloo_1_1_b_m_x_device.md#function-iscurrentdevice"><strong>isCurrentDevice</strong></a>() =0<br>Whether for the current device</p>                         |

## Protected Functions

|   | Name                                                                |
| - | ------------------------------------------------------------------- |
|   | [**BMXDevice**](classfloo_1_1_b_m_x_device.md#function-bmxdevice)() |

## Public Functions Documentation

### function \~BMXDevice

```cpp
inline virtual ~BMXDevice()
```

Destructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>

```

### function deviceSN

```cpp
virtual int deviceSN() =0
```

Device serial number

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>

```

### function userId

```cpp
virtual int64_t userId() =0
```

User id

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>

```

### function platform

```cpp
virtual int platform() =0
```

Software platform

**Return**: int

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>

```

### function userAgent

```cpp
virtual std::string userAgent() =0
```

User agent information

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

Set user agent information

**Parameters**:

* **userAgent** User agent information

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXDevice'></div>

```

### function isCurrentDevice

```cpp
virtual bool isCurrentDevice() =0
```

Whether for the current device

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

***

Updated on 2022-01-26 at 17:20:40 +0800
