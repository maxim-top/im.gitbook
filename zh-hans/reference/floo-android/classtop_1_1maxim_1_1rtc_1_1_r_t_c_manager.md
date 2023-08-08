---
title: top::maxim::rtc::RTCManager
---

# top::maxim::rtc::RTCManager

Description : RTC Created by Mango on 2018/12/2.

## Public Functions

|                                                                       | Name                                                                                                                                                                                    |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [RTCManager](classtop\_1\_1maxim\_1\_1rtc\_1\_1\_r\_t\_c\_manager.md) | [**getInstance**](classtop\_1\_1maxim\_1\_1rtc\_1\_1\_r\_t\_c\_manager.md#function-getinstance)()                                                                                       |
| void                                                                  | [**init**](classtop\_1\_1maxim\_1\_1rtc\_1\_1\_r\_t\_c\_manager.md#function-init)(Application application, BMXClient bmxClient)                                                         |
| BMXRTCEngine                                                          | [**getRTCEngine**](classtop\_1\_1maxim\_1\_1rtc\_1\_1\_r\_t\_c\_manager.md#function-getrtcengine)()                                                                                     |
| void                                                                  | <p><a href="classtop_1_1maxim_1_1rtc_1_1_r_t_c_manager.md#function-addrtcservicelistener"><strong>addRTCServiceListener</strong></a>(BMXRTCServiceListener listener)<br>添加监听者</p>       |
| void                                                                  | <p><a href="classtop_1_1maxim_1_1rtc_1_1_r_t_c_manager.md#function-removertcservicelistener"><strong>removeRTCServiceListener</strong></a>(BMXRTCServiceListener listener)<br>移除监听者</p> |

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

添加监听者

### function removeRTCServiceListener

```java
inline void removeRTCServiceListener(
    BMXRTCServiceListener listener
)
```

移除监听者



Updated on 2023-06-21 at 16:26:43 +0800
