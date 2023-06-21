---
title: top::maxim::rtc::RTCManager
summary: Description : RTC Created by Mango on 2018/12/2. 

---

# top::maxim::rtc::RTCManager



Description : RTC Created by Mango on 2018/12/2. 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [RTCManager](classtop_1_1maxim_1_1rtc_1_1_r_t_c_manager.md) | **[getInstance](classtop_1_1maxim_1_1rtc_1_1_r_t_c_manager.md#function-getinstance)**() |
| void | **[init](classtop_1_1maxim_1_1rtc_1_1_r_t_c_manager.md#function-init)**(Application application, BMXClient bmxClient) |
| BMXRTCEngine | **[getRTCEngine](classtop_1_1maxim_1_1rtc_1_1_r_t_c_manager.md#function-getrtcengine)**() |
| void | **[addRTCServiceListener](classtop_1_1maxim_1_1rtc_1_1_r_t_c_manager.md#function-addrtcservicelistener)**(BMXRTCServiceListener listener)<br>Add a RTC service listener  |
| void | **[removeRTCServiceListener](classtop_1_1maxim_1_1rtc_1_1_r_t_c_manager.md#function-removertcservicelistener)**(BMXRTCServiceListener listener)<br>Remove a RTC service listener  |

## Public Functions Documentation

### function getInstance

```java
static inline RTCManager getInstance()
```


### function init

```java
inline void init(
    Application application,
    BMXClient bmxClient
)
```


### function getRTCEngine

```java
inline BMXRTCEngine getRTCEngine()
```


### function addRTCServiceListener

```java
inline void addRTCServiceListener(
    BMXRTCServiceListener listener
)
```

Add a RTC service listener 

### function removeRTCServiceListener

```java
inline void removeRTCServiceListener(
    BMXRTCServiceListener listener
)
```

Remove a RTC service listener 

-------------------------------

Updated on 2023-06-21 at 16:26:43 +0800