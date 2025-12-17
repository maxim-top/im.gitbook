---
title: im::floo::floolib::BMXUserServiceListener
summary: 用户状态监听者
---

# im::floo::floolib::BMXUserServiceListener

用户状态监听者

## Public Functions

|                   | Name                                                                                                                                                                                                                                                            |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-delete)()                                                                                                                                                                   |
| void              | [**swigReleaseOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-swigreleaseownership)()                                                                                                                                       |
| void              | [**swigTakeOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-swigtakeownership)()                                                                                                                                             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onconnectstatuschanged"><strong>onConnectStatusChanged</strong></a>([BMXConnectStatus] status)<br>链接状态发生变化</p>                                                               |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onusersignin"><strong>onUserSignIn</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> profile)<br>用户登陆</p>                       |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onusersignout"><strong>onUserSignOut</strong></a>([BMXErrorCode] error, long userId)<br>用户登出</p>                                                                             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-oninfoupdated"><strong>onInfoUpdated</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> profile)<br>同步用户信息更新（其他设备操作发生用户信息变更）</p> |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingin"><strong>onOtherDeviceSingIn</strong></a>(int deviceSN)<br>用户在其他设备上登陆</p>                                                                                |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingout"><strong>onOtherDeviceSingOut</strong></a>(int deviceSN)<br>用户在其他设备上登出</p>                                                                              |
|                   | [**BMXUserServiceListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-bmxuserservicelistener)()                                                                                                                                   |
| void              | [**registerUserService**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-registeruserservice)([BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md) service)                                                           |

## Protected Functions

|      | Name                                                                                                                                                                                       |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|      | [**BMXUserServiceListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-bmxuserservicelistener)(long cPtr, boolean cMemoryOwn)                                 |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-finalize)()                                                                                          |
| void | [**swigDirectorDisconnect**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-swigdirectordisconnect)()                                                              |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-getcptr)([BMXUserServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md) obj) |

## Protected Attributes

|                   | Name                                                                                                  |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| transient boolean | [**swigCMemOwn**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#variable-swigcmemown) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function onConnectStatusChanged

```java
inline void onConnectStatusChanged(
    BMXConnectStatus status
)
```

链接状态发生变化

**Parameters**:

* **status** 连接状态

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function onUserSignIn

```java
inline void onUserSignIn(
    BMXUserProfile profile
)
```

用户登陆

**Parameters**:

* **profile** 用户profile

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function onUserSignOut

```java
inline void onUserSignOut(
    BMXErrorCode error,
    long userId
)
```

用户登出

**Parameters**:

* **error** 状态错误码

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function onInfoUpdated

```java
inline void onInfoUpdated(
    BMXUserProfile profile
)
```

同步用户信息更新（其他设备操作发生用户信息变更）

**Parameters**:

* **profile** 用户profile

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function onOtherDeviceSingIn

```java
inline void onOtherDeviceSingIn(
    int deviceSN
)
```

用户在其他设备上登陆

**Parameters**:

* **deviceSN** 设备序列号

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function onOtherDeviceSingOut

```java
inline void onOtherDeviceSingOut(
    int deviceSN
)
```

用户在其他设备上登出

**Parameters**:

* **deviceSN** 设备序列号

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function BMXUserServiceListener

```java
inline BMXUserServiceListener()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function registerUserService

```java
inline void registerUserService(
    BMXUserService service
)
```

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function BMXUserServiceListener

```java
inline BMXUserServiceListener(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function finalize

```java
inline void finalize()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

```

### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXUserServiceListener'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
