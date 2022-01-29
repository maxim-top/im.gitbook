---
title: floo::BMXPushUserProfile
summary: Push user Profile. 

---

# floo::BMXPushUserProfile



Push user Profile. 


`#include <bmx_push_user_profile.h>`

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXPushUserProfile](classfloo_1_1_b_m_x_push_user_profile.md#function-~bmxpushuserprofile)**()<br>Destructor  |
| virtual int64_t | **[userId](classfloo_1_1_b_m_x_push_user_profile.md#function-userid)**() =0<br>User ID (unique)  |
| virtual std::string | **[pushAlias](classfloo_1_1_b_m_x_push_user_profile.md#function-pushalias)**() =0<br>Push user alias  |
| virtual std::string | **[pushToken](classfloo_1_1_b_m_x_push_user_profile.md#function-pushtoken)**() =0<br>Push user token  |
| virtual const [MessagePushSetting] & | **[messagePushSetting](classfloo_1_1_b_m_x_push_user_profile.md#function-messagepushsetting)**() =0<br>Push user information settings  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXPushUserProfile](classfloo_1_1_b_m_x_push_user_profile.md#function-bmxpushuserprofile)**() |

## Public Functions Documentation

### function ~BMXPushUserProfile

```cpp
inline virtual ~BMXPushUserProfile()
```

Destructor 

### function userId

```cpp
virtual int64_t userId() =0
```

User ID (unique) 

**Return**: int64_t 

### function pushAlias

```cpp
virtual std::string pushAlias() =0
```

Push user alias 

**Return**: std::string 

### function pushToken

```cpp
virtual std::string pushToken() =0
```

Push user token 

**Return**: std::string 

### function messagePushSetting

```cpp
virtual const MessagePushSetting & messagePushSetting() =0
```

Push user information settings 

**Return**: [MessagePushSetting]

## Protected Functions Documentation

### function BMXPushUserProfile

```cpp
inline BMXPushUserProfile()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800