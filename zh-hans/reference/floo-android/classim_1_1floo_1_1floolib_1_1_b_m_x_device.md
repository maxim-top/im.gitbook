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


### function deviceSN

```java
inline int deviceSN()
```

设备序列号 

**Return**: int 

### function userId

```java
inline long userId()
```

用户id 

**Return**: int64_t 

### function platform

```java
inline int platform()
```

软件平台 

**Return**: int 

### function userAgent

```java
inline String userAgent()
```

用户代理信息 

**Return**: std::string 

### function setUserAgent

```java
inline void setUserAgent(
    String userAgent
)
```

设置用户代理信息 

**Parameters**: 

  * **userAgent** 用户代理信息 


### function isCurrentDevice

```java
inline boolean isCurrentDevice()
```

是否是当前设备 

**Return**: bool 

## Protected Functions Documentation

### function BMXDevice

```java
inline BMXDevice(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


### function getCPtr

```java
static inline long getCPtr(
    BMXDevice obj
)
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800