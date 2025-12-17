---
title: im::floo::floolib::BMXUserServiceListener
summary: User state listener
---

# im::floo::floolib::BMXUserServiceListener

User state listener

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                                                         |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-delete)()                                                                                                                                                                                                                                |
| void              | [**swigReleaseOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-swigreleaseownership)()                                                                                                                                                                                                    |
| void              | [**swigTakeOwnership**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-swigtakeownership)()                                                                                                                                                                                                          |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onconnectstatuschanged"><strong>onConnectStatusChanged</strong></a>([BMXConnectStatus] status)<br>Channel state changed</p>                                                                                                               |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onusersignin"><strong>onUserSignIn</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> profile)<br>User login</p>                                                                              |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onusersignout"><strong>onUserSignOut</strong></a>([BMXErrorCode] error, long userId)<br>User logout</p>                                                                                                                                   |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-oninfoupdated"><strong>onInfoUpdated</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md">BMXUserProfile</a> profile)<br>Synchronize user information updates (when user information changes in other devices)</p> |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingin"><strong>onOtherDeviceSingIn</strong></a>(int deviceSN)<br>User login on another device</p>                                                                                                                           |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingout"><strong>onOtherDeviceSingOut</strong></a>(int deviceSN)<br>User logout on another device</p>                                                                                                                        |
|                   | [**BMXUserServiceListener**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-bmxuserservicelistener)()                                                                                                                                                                                                |
| void              | [**registerUserService**](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-registeruserservice)([BMXUserService](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service.md) service)                                                                                                                        |

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

Channel state changed

**Parameters**:

* **status** Connection state

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

User login

**Parameters**:

* **profile** User profile

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

User logout

**Parameters**:

* **error** State error code

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

Synchronize user information updates (when user information changes in other devices)

**Parameters**:

* **profile** User profile

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

User login on another device

**Parameters**:

* **deviceSN** Device serial number

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

User logout on another device

**Parameters**:

* **deviceSN** Device serial number

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
