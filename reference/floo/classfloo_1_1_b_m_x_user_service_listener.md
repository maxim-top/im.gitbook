---
title: floo::BMXUserServiceListener
summary: User state listener 

---

# floo::BMXUserServiceListener



User state listener 


`#include <bmx_user_service_listener.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXUserServiceListener](classfloo_1_1_b_m_x_user_service_listener.md#function-bmxuserservicelistener)**()<br>Constructor  |
| virtual | **[~BMXUserServiceListener](classfloo_1_1_b_m_x_user_service_listener.md#function-~bmxuserservicelistener)**()<br>Destructor  |
| virtual void | **[onConnectStatusChanged](classfloo_1_1_b_m_x_user_service_listener.md#function-onconnectstatuschanged)**(BMXConnectStatus status)<br>Channel state changed  |
| virtual void | **[onUserSignIn](classfloo_1_1_b_m_x_user_service_listener.md#function-onusersignin)**(BMXUserProfilePtr profile)<br>User login  |
| virtual void | **[onUserSignOut](classfloo_1_1_b_m_x_user_service_listener.md#function-onusersignout)**(BMXErrorCode error, int64_t userId)<br>User logout  |
| virtual void | **[onInfoUpdated](classfloo_1_1_b_m_x_user_service_listener.md#function-oninfoupdated)**(BMXUserProfilePtr profile)<br>Synchronize user information updates (when user information changes in other devices)  |
| virtual void | **[onOtherDeviceSingIn](classfloo_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingin)**(int deviceSN)<br>User login on another device  |
| virtual void | **[onOtherDeviceSingOut](classfloo_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingout)**(int deviceSN)<br>User logout on another device  |
| void | **[registerUserService](classfloo_1_1_b_m_x_user_service_listener.md#function-registeruserservice)**([BMXUserService](classfloo_1_1_b_m_x_user_service.md) * service)<br>Register BMXUserService to which BMXUserServiceListener is bound (automatic registration in SDK)  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [BMXUserService](classfloo_1_1_b_m_x_user_service.md) * | **[mService](classfloo_1_1_b_m_x_user_service_listener.md#variable-mservice)**  |

## Public Functions Documentation

### function BMXUserServiceListener

```cpp
inline BMXUserServiceListener()
```

Constructor 

### function ~BMXUserServiceListener

```cpp
inline virtual ~BMXUserServiceListener()
```

Destructor 

### function onConnectStatusChanged

```cpp
inline virtual void onConnectStatusChanged(
    BMXConnectStatus status
)
```

Channel state changed 

**Parameters**: 

  * **status** Connection state 


### function onUserSignIn

```cpp
inline virtual void onUserSignIn(
    BMXUserProfilePtr profile
)
```

User login 

**Parameters**: 

  * **profile** User profile 


### function onUserSignOut

```cpp
inline virtual void onUserSignOut(
    BMXErrorCode error,
    int64_t userId
)
```

User logout 

**Parameters**: 

  * **error** State error code 


### function onInfoUpdated

```cpp
inline virtual void onInfoUpdated(
    BMXUserProfilePtr profile
)
```

Synchronize user information updates (when user information changes in other devices) 

**Parameters**: 

  * **profile** User profile 


### function onOtherDeviceSingIn

```cpp
inline virtual void onOtherDeviceSingIn(
    int deviceSN
)
```

User login on another device 

**Parameters**: 

  * **deviceSN** Device serial number 


### function onOtherDeviceSingOut

```cpp
inline virtual void onOtherDeviceSingOut(
    int deviceSN
)
```

User logout on another device 

**Parameters**: 

  * **deviceSN** Device serial number 


### function registerUserService

```cpp
inline void registerUserService(
    BMXUserService * service
)
```

Register BMXUserService to which BMXUserServiceListener is bound (automatic registration in SDK) 

**Parameters**: 

  * **service** [BMXUserService](classfloo_1_1_b_m_x_user_service.md)


## Protected Attributes Documentation

### variable mService

```cpp
BMXUserService * mService;
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800