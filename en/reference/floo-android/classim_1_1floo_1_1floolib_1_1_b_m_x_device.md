---
title: im::floo::floolib::BMXDevice
summary: Device information 

---

# im::floo::floolib::BMXDevice



Device information 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-delete)**() |
| int | **[deviceSN](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-devicesn)**()<br>Device serial number  |
| long | **[userId](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-userid)**()<br>User id  |
| int | **[platform](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-platform)**()<br>Software platform  |
| String | **[userAgent](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-useragent)**()<br>User agent information  |
| void | **[setUserAgent](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-setuseragent)**(String userAgent)<br>Set user agent information  |
| boolean | **[isCurrentDevice](classim_1_1floo_1_1floolib_1_1_b_m_x_device.md#function-iscurrentdevice)**()<br>Whether for the current device  |

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

Device serial number 

**Return**: int 

### function userId

```java
inline long userId()
```

User id 

**Return**: int64_t 

### function platform

```java
inline int platform()
```

Software platform 

**Return**: int 

### function userAgent

```java
inline String userAgent()
```

User agent information 

**Return**: std::string 

### function setUserAgent

```java
inline void setUserAgent(
    String userAgent
)
```

Set user agent information 

**Parameters**: 

  * **userAgent** User agent information 


### function isCurrentDevice

```java
inline boolean isCurrentDevice()
```

Whether for the current device 

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