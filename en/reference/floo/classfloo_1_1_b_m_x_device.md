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

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="~BMXDevice" %}{% endlanying_code_snippet %}
```
### function deviceSN

```cpp
virtual int deviceSN() =0
```

Device serial number 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="deviceSN" %}{% endlanying_code_snippet %}
```
### function userId

```cpp
virtual int64_t userId() =0
```

User id 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="userId" %}{% endlanying_code_snippet %}
```
### function platform

```cpp
virtual int platform() =0
```

Software platform 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="platform" %}{% endlanying_code_snippet %}
```
### function userAgent

```cpp
virtual std::string userAgent() =0
```

User agent information 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="userAgent" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="setUserAgent" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="isCurrentDevice" %}{% endlanying_code_snippet %}
```
### function BMXDevice

```cpp
inline BMXDevice()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="BMXDevice" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800