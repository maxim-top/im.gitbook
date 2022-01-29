---
title: im::floo::floolib::BMXUserServiceListener
summary: User state listener 

---

# im::floo::floolib::BMXUserServiceListener



User state listener 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-delete)**() |
| void | **[swigReleaseOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-swigreleaseownership)**() |
| void | **[swigTakeOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-swigtakeownership)**() |
| void | **[onConnectStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onconnectstatuschanged)**([BMXConnectStatus] status)<br>Channel state changed  |
| void | **[onUserSignIn](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onusersignin)**([BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) profile)<br>User login  |
| void | **[onUserSignOut](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onusersignout)**([BMXErrorCode] error, long userId)<br>User logout  |
| void | **[onInfoUpdated](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-oninfoupdated)**([BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) profile)<br>Synchronize user information updates (when user information changes in other devices)  |
| void | **[onOtherDeviceSingIn](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingin)**(int deviceSN)<br>User login on another device  |
| void | **[onOtherDeviceSingOut](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingout)**(int deviceSN)<br>User logout on another device  |
| | **[BMXUserServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-bmxuserservicelistener)**() |
| void | **[registerUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-registeruserservice)**([BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md) service) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXUserServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-bmxuserservicelistener)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-finalize)**() |
| void | **[swigDirectorDisconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-swigdirectordisconnect)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-getcptr)**([BMXUserServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#variable-swigcmemown)**  |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```


### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```


### function onConnectStatusChanged

```java
inline void onConnectStatusChanged(
    BMXConnectStatus status
)
```

Channel state changed 

**Parameters**: 

  * **status** Connection state 


### function onUserSignIn

```java
inline void onUserSignIn(
    BMXUserProfile profile
)
```

User login 

**Parameters**: 

  * **profile** User profile 


### function onUserSignOut

```java
inline void onUserSignOut(
    BMXErrorCode error,
    long userId
)
```

User logout 

**Parameters**: 

  * **error** State error code 


### function onInfoUpdated

```java
inline void onInfoUpdated(
    BMXUserProfile profile
)
```

Synchronize user information updates (when user information changes in other devices) 

**Parameters**: 

  * **profile** User profile 


### function onOtherDeviceSingIn

```java
inline void onOtherDeviceSingIn(
    int deviceSN
)
```

User login on another device 

**Parameters**: 

  * **deviceSN** Device serial number 


### function onOtherDeviceSingOut

```java
inline void onOtherDeviceSingOut(
    int deviceSN
)
```

User logout on another device 

**Parameters**: 

  * **deviceSN** Device serial number 


### function BMXUserServiceListener

```java
inline BMXUserServiceListener()
```


### function registerUserService

```java
inline void registerUserService(
    BMXUserService service
)
```


## Protected Functions Documentation

### function BMXUserServiceListener

```java
inline BMXUserServiceListener(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```


### function getCPtr

```java
static inline long getCPtr(
    BMXUserServiceListener obj
)
```


## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800