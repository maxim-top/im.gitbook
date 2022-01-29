---
title: floo::BMXUserServiceListener
summary: 用户状态监听者 

---

# floo::BMXUserServiceListener



用户状态监听者 


`#include <bmx_user_service_listener.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXUserServiceListener](classfloo_1_1_b_m_x_user_service_listener.md#function-bmxuserservicelistener)**()<br>构造函数  |
| virtual | **[~BMXUserServiceListener](classfloo_1_1_b_m_x_user_service_listener.md#function-~bmxuserservicelistener)**()<br>析构函数  |
| virtual void | **[onConnectStatusChanged](classfloo_1_1_b_m_x_user_service_listener.md#function-onconnectstatuschanged)**(BMXConnectStatus status)<br>链接状态发生变化  |
| virtual void | **[onUserSignIn](classfloo_1_1_b_m_x_user_service_listener.md#function-onusersignin)**(BMXUserProfilePtr profile)<br>用户登陆  |
| virtual void | **[onUserSignOut](classfloo_1_1_b_m_x_user_service_listener.md#function-onusersignout)**(BMXErrorCode error, int64_t userId)<br>用户登出  |
| virtual void | **[onInfoUpdated](classfloo_1_1_b_m_x_user_service_listener.md#function-oninfoupdated)**(BMXUserProfilePtr profile)<br>同步用户信息更新（其他设备操作发生用户信息变更）  |
| virtual void | **[onOtherDeviceSingIn](classfloo_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingin)**(int deviceSN)<br>用户在其他设备上登陆  |
| virtual void | **[onOtherDeviceSingOut](classfloo_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingout)**(int deviceSN)<br>用户在其他设备上登出  |
| void | **[registerUserService](classfloo_1_1_b_m_x_user_service_listener.md#function-registeruserservice)**([BMXUserService](classfloo_1_1_b_m_x_user_service.md) * service)<br>注册BMXUserServiceListener绑定到的BMXUserService（SDK内部自动注册）  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [BMXUserService](classfloo_1_1_b_m_x_user_service.md) * | **[mService](classfloo_1_1_b_m_x_user_service_listener.md#variable-mservice)**  |

## Public Functions Documentation

### function BMXUserServiceListener

```cpp
inline BMXUserServiceListener()
```

构造函数 

### function ~BMXUserServiceListener

```cpp
inline virtual ~BMXUserServiceListener()
```

析构函数 

### function onConnectStatusChanged

```cpp
inline virtual void onConnectStatusChanged(
    BMXConnectStatus status
)
```

链接状态发生变化 

**Parameters**: 

  * **status** 连接状态 


### function onUserSignIn

```cpp
inline virtual void onUserSignIn(
    BMXUserProfilePtr profile
)
```

用户登陆 

**Parameters**: 

  * **profile** 用户profile 


### function onUserSignOut

```cpp
inline virtual void onUserSignOut(
    BMXErrorCode error,
    int64_t userId
)
```

用户登出 

**Parameters**: 

  * **error** 状态错误码 


### function onInfoUpdated

```cpp
inline virtual void onInfoUpdated(
    BMXUserProfilePtr profile
)
```

同步用户信息更新（其他设备操作发生用户信息变更） 

**Parameters**: 

  * **profile** 用户profile 


### function onOtherDeviceSingIn

```cpp
inline virtual void onOtherDeviceSingIn(
    int deviceSN
)
```

用户在其他设备上登陆 

**Parameters**: 

  * **deviceSN** 设备序列号 


### function onOtherDeviceSingOut

```cpp
inline virtual void onOtherDeviceSingOut(
    int deviceSN
)
```

用户在其他设备上登出 

**Parameters**: 

  * **deviceSN** 设备序列号 


### function registerUserService

```cpp
inline void registerUserService(
    BMXUserService * service
)
```

注册BMXUserServiceListener绑定到的BMXUserService（SDK内部自动注册） 

**Parameters**: 

  * **service** [BMXUserService](classfloo_1_1_b_m_x_user_service.md)


## Protected Attributes Documentation

### variable mService

```cpp
BMXUserService * mService;
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800