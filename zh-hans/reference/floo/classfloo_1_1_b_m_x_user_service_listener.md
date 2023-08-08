---
title: floo::BMXUserServiceListener
summary: 用户状态监听者
---

# floo::BMXUserServiceListener

用户状态监听者

`#include <bmx_user_service_listener.h>`

## Public Functions

|              | Name                                                                                                                                                                                                                                                                     |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|              | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-bmxuserservicelistener"><strong>BMXUserServiceListener</strong></a>()<br>构造函数</p>                                                                                                                      |
| virtual      | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-~bmxuserservicelistener"><strong>~BMXUserServiceListener</strong></a>()<br>析构函数</p>                                                                                                                    |
| virtual void | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-onconnectstatuschanged"><strong>onConnectStatusChanged</strong></a>(BMXConnectStatus status)<br>链接状态发生变化</p>                                                                                           |
| virtual void | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-onusersignin"><strong>onUserSignIn</strong></a>(BMXUserProfilePtr profile)<br>用户登陆</p>                                                                                                                 |
| virtual void | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-onusersignout"><strong>onUserSignOut</strong></a>(BMXErrorCode error, int64_t userId)<br>用户登出</p>                                                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-oninfoupdated"><strong>onInfoUpdated</strong></a>(BMXUserProfilePtr profile)<br>同步用户信息更新（其他设备操作发生用户信息变更）</p>                                                                                           |
| virtual void | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingin"><strong>onOtherDeviceSingIn</strong></a>(int deviceSN)<br>用户在其他设备上登陆</p>                                                                                                          |
| virtual void | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingout"><strong>onOtherDeviceSingOut</strong></a>(int deviceSN)<br>用户在其他设备上登出</p>                                                                                                        |
| void         | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-registeruserservice"><strong>registerUserService</strong></a>(<a href="classfloo_1_1_b_m_x_user_service.md">BMXUserService</a> * service)<br>注册BMXUserServiceListener绑定到的BMXUserService（SDK内部自动注册）</p> |

## Protected Attributes

|                                                                 | Name                                                                                   |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [BMXUserService](classfloo\_1\_1\_b\_m\_x\_user\_service.md) \* | [**mService**](classfloo\_1\_1\_b\_m\_x\_user\_service\_listener.md#variable-mservice) |

## Public Functions Documentation

### function BMXUserServiceListener

```cpp
inline BMXUserServiceListener()
```

构造函数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserServiceListener'></div>
```

### function \~BMXUserServiceListener

```cpp
inline virtual ~BMXUserServiceListener()
```

析构函数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserServiceListener'></div>
```

### function onConnectStatusChanged

```cpp
inline virtual void onConnectStatusChanged(
    BMXConnectStatus status
)
```

链接状态发生变化

**Parameters**:

* **status** 连接状态

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserServiceListener'></div>
```

### function onUserSignIn

```cpp
inline virtual void onUserSignIn(
    BMXUserProfilePtr profile
)
```

用户登陆

**Parameters**:

* **profile** 用户profile

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserServiceListener'></div>
```

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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserServiceListener'></div>
```

### function onInfoUpdated

```cpp
inline virtual void onInfoUpdated(
    BMXUserProfilePtr profile
)
```

同步用户信息更新（其他设备操作发生用户信息变更）

**Parameters**:

* **profile** 用户profile

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserServiceListener'></div>
```

### function onOtherDeviceSingIn

```cpp
inline virtual void onOtherDeviceSingIn(
    int deviceSN
)
```

用户在其他设备上登陆

**Parameters**:

* **deviceSN** 设备序列号

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserServiceListener'></div>
```

### function onOtherDeviceSingOut

```cpp
inline virtual void onOtherDeviceSingOut(
    int deviceSN
)
```

用户在其他设备上登出

**Parameters**:

* **deviceSN** 设备序列号

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserServiceListener'></div>
```

### function registerUserService

```cpp
inline void registerUserService(
    BMXUserService * service
)
```

注册BMXUserServiceListener绑定到的BMXUserService（SDK内部自动注册）

**Parameters**:

* **service** [BMXUserService](classfloo\_1\_1\_b\_m\_x\_user\_service.md)

## Protected Attributes Documentation

### variable mService

```cpp
BMXUserService * mService;
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserServiceListener'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
