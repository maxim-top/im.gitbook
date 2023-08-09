---
title: im::floo::floolib::BMXDevice
summary: 设备信息 

---

# im::floo::floolib::BMXDevice



设备信息 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-delete)**() |
| int | **[deviceSN](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-devicesn)**()<br>设备序列号  |
| long | **[userId](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-userid)**()<br>用户id  |
| int | **[platform](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-platform)**()<br>软件平台  |
| String | **[userAgent](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-useragent)**()<br>用户代理信息  |
| void | **[setUserAgent](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-setuseragent)**(String userAgent)<br>设置用户代理信息  |
| boolean | **[isCurrentDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-iscurrentdevice)**()<br>是否是当前设备  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-bmxdevice)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-getcptr)**([BMXDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md) obj) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXDevice",function="delete" %}{% endlanying_code_snippet %}
```
### function deviceSN

```java
inline int deviceSN()
```

设备序列号 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXDevice",function="deviceSN" %}{% endlanying_code_snippet %}
```
### function userId

```java
inline long userId()
```

用户id 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXDevice",function="userId" %}{% endlanying_code_snippet %}
```
### function platform

```java
inline int platform()
```

软件平台 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXDevice",function="platform" %}{% endlanying_code_snippet %}
```
### function userAgent

```java
inline String userAgent()
```

用户代理信息 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXDevice",function="userAgent" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXDevice",function="setUserAgent" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXDevice",function="isCurrentDevice" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXDevice",function="BMXDevice" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXDevice",function="finalize" %}{% endlanying_code_snippet %}
```
### function getCPtr

```java
static inline long getCPtr(
    BMXDevice obj
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXDevice",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800