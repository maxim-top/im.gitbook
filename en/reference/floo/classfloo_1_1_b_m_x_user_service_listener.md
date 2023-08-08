---
title: floo::BMXUserServiceListener
summary: User state listener
---

# floo::BMXUserServiceListener

User state listener

`#include <bmx_user_service_listener.h>`

## Public Functions

|              | Name                                                                                                                                                                                                                                                                                                                |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-bmxuserservicelistener"><strong>BMXUserServiceListener</strong></a>()<br>Constructor</p>                                                                                                                                                          |
| virtual      | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-~bmxuserservicelistener"><strong>~BMXUserServiceListener</strong></a>()<br>Destructor</p>                                                                                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-onconnectstatuschanged"><strong>onConnectStatusChanged</strong></a>(BMXConnectStatus status)<br>Channel state changed</p>                                                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-onusersignin"><strong>onUserSignIn</strong></a>(BMXUserProfilePtr profile)<br>User login</p>                                                                                                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-onusersignout"><strong>onUserSignOut</strong></a>(BMXErrorCode error, int64_t userId)<br>User logout</p>                                                                                                                                          |
| virtual void | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-oninfoupdated"><strong>onInfoUpdated</strong></a>(BMXUserProfilePtr profile)<br>Synchronize user information updates (when user information changes in other devices)</p>                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingin"><strong>onOtherDeviceSingIn</strong></a>(int deviceSN)<br>User login on another device</p>                                                                                                                                   |
| virtual void | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-onotherdevicesingout"><strong>onOtherDeviceSingOut</strong></a>(int deviceSN)<br>User logout on another device</p>                                                                                                                                |
| void         | <p><a href="classfloo_1_1_b_m_x_user_service_listener.md#function-registeruserservice"><strong>registerUserService</strong></a>(<a href="classfloo_1_1_b_m_x_user_service.md">BMXUserService</a> * service)<br>Register BMXUserService to which BMXUserServiceListener is bound (automatic registration in SDK)</p> |

## Protected Attributes

|                                                                 | Name                                                                                   |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [BMXUserService](classfloo\_1\_1\_b\_m\_x\_user\_service.md) \* | [**mService**](classfloo\_1\_1\_b\_m\_x\_user\_service\_listener.md#variable-mservice) |

## Public Functions Documentation

### function BMXUserServiceListener

```cpp
inline BMXUserServiceListener()
```

Constructor

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXUserServiceListener'></div>
```

### function \~BMXUserServiceListener

```cpp
inline virtual ~BMXUserServiceListener()
```

Destructor

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

Channel state changed

**Parameters**:

* **status** Connection state

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

User login

**Parameters**:

* **profile** User profile

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

User logout

**Parameters**:

* **error** State error code

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

Synchronize user information updates (when user information changes in other devices)

**Parameters**:

* **profile** User profile

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

User login on another device

**Parameters**:

* **deviceSN** Device serial number

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

User logout on another device

**Parameters**:

* **deviceSN** Device serial number

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

Register BMXUserService to which BMXUserServiceListener is bound (automatic registration in SDK)

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
