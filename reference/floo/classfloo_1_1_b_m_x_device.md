---
title: floo::BMXDevice
summary: Device information 

---

# floo::BMXDevice



Device information 


`#include <bmx_device.h>`

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXDevice](classfloo_1_1_b_m_x_device.md#function-~bmxdevice)**()<br>Destructor  |
| virtual int | **[deviceSN](classfloo_1_1_b_m_x_device.md#function-devicesn)**() =0<br>Device serial number  |
| virtual int64_t | **[userId](classfloo_1_1_b_m_x_device.md#function-userid)**() =0<br>User id  |
| virtual int | **[platform](classfloo_1_1_b_m_x_device.md#function-platform)**() =0<br>Software platform  |
| virtual std::string | **[userAgent](classfloo_1_1_b_m_x_device.md#function-useragent)**() =0<br>User agent information  |
| virtual void | **[setUserAgent](classfloo_1_1_b_m_x_device.md#function-setuseragent)**(const std::string & userAgent) =0<br>Set user agent information  |
| virtual bool | **[isCurrentDevice](classfloo_1_1_b_m_x_device.md#function-iscurrentdevice)**() =0<br>Whether for the current device  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXDevice](classfloo_1_1_b_m_x_device.md#function-bmxdevice)**() |

## Public Functions Documentation

### function ~BMXDevice

```cpp
inline virtual ~BMXDevice()
```

Destructor 

### function deviceSN

```cpp
virtual int deviceSN() =0
```

Device serial number 

**Return**: int 

### function userId

```cpp
virtual int64_t userId() =0
```

User id 

**Return**: int64_t 

### function platform

```cpp
virtual int platform() =0
```

Software platform 

**Return**: int 

### function userAgent

```cpp
virtual std::string userAgent() =0
```

User agent information 

**Return**: std::string 

### function setUserAgent

```cpp
virtual void setUserAgent(
    const std::string & userAgent
) =0
```

Set user agent information 

**Parameters**: 

  * **userAgent** User agent information 


### function isCurrentDevice

```cpp
virtual bool isCurrentDevice() =0
```

Whether for the current device 

**Return**: bool 

## Protected Functions Documentation

### function BMXDevice

```cpp
inline BMXDevice()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800