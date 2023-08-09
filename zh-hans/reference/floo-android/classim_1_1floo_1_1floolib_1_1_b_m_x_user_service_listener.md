---
title: im::floo::floolib::BMXUserServiceListener
summary: 用户状态监听者 

---

# im::floo::floolib::BMXUserServiceListener



用户状态监听者 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-delete)**() |
| void | **[swigReleaseOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-swigreleaseownership)**() |
| void | **[swigTakeOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-swigtakeownership)**() |
| void | **[onConnectStatusChanged](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onconnectstatuschanged)**([BMXConnectStatus] status)<br>链接状态发生变化  |
| void | **[onUserSignIn](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onusersignin)**([BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) profile)<br>用户登陆  |
| void | **[onUserSignOut](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onusersignout)**([BMXErrorCode] error, long userId)<br>用户登出  |
| void | **[onInfoUpdated](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-oninfoupdated)**([BMXUserProfile](classim_1_1floo_1_1floolib_1_1_b_m_x_user_profile.md) profile)<br>同步用户信息更新（其他设备操作发生用户信息变更）  |
| void | **[onOtherDeviceSingIn](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingin)**(int deviceSN)<br>用户在其他设备上登陆  |
| void | **[onOtherDeviceSingOut](classim_1_1floo_1_1floolib_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingout)**(int deviceSN)<br>用户在其他设备上登出  |
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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="delete" %}{% endlanying_code_snippet %}
```
### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="swigReleaseOwnership" %}{% endlanying_code_snippet %}
```
### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="swigTakeOwnership" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="onConnectStatusChanged" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="onUserSignIn" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="onUserSignOut" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="onInfoUpdated" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="onOtherDeviceSingIn" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="onOtherDeviceSingOut" %}{% endlanying_code_snippet %}
```
### function BMXUserServiceListener

```java
inline BMXUserServiceListener()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="BMXUserServiceListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="registerUserService" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="BMXUserServiceListener" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="finalize" %}{% endlanying_code_snippet %}
```
### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="swigDirectorDisconnect" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXUserServiceListener",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800