---
title: floo::BMXDevice
summary: 设备信息 

---

# floo::BMXDevice



设备信息 


`#include <bmx_device.h>`

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXDevice](classfloo_1_1_b_m_x_device.md#function-~bmxdevice)**()<br>析构函数  |
| virtual int | **[deviceSN](classfloo_1_1_b_m_x_device.md#function-devicesn)**() =0<br>设备序列号  |
| virtual int64_t | **[userId](classfloo_1_1_b_m_x_device.md#function-userid)**() =0<br>用户id  |
| virtual int | **[platform](classfloo_1_1_b_m_x_device.md#function-platform)**() =0<br>软件平台  |
| virtual std::string | **[userAgent](classfloo_1_1_b_m_x_device.md#function-useragent)**() =0<br>用户代理信息  |
| virtual void | **[setUserAgent](classfloo_1_1_b_m_x_device.md#function-setuseragent)**(const std::string & userAgent) =0<br>设置用户代理信息  |
| virtual bool | **[isCurrentDevice](classfloo_1_1_b_m_x_device.md#function-iscurrentdevice)**() =0<br>是否是当前设备  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXDevice](classfloo_1_1_b_m_x_device.md#function-bmxdevice)**() |

## Public Functions Documentation

### function ~BMXDevice

```cpp
inline virtual ~BMXDevice()
```

析构函数 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="~BMXDevice" %}{% endlanying_code_snippet %}
```
### function deviceSN

```cpp
virtual int deviceSN() =0
```

设备序列号 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="deviceSN" %}{% endlanying_code_snippet %}
```
### function userId

```cpp
virtual int64_t userId() =0
```

用户id 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="userId" %}{% endlanying_code_snippet %}
```
### function platform

```cpp
virtual int platform() =0
```

软件平台 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="platform" %}{% endlanying_code_snippet %}
```
### function userAgent

```cpp
virtual std::string userAgent() =0
```

用户代理信息 

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

设置用户代理信息 

**Parameters**: 

  * **userAgent** 用户代理信息 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXDevice",function="setUserAgent" %}{% endlanying_code_snippet %}
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