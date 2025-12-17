---
title: floo::BMXPushUserProfile
summary: Push user Profile.
---

# floo::BMXPushUserProfile

Push user Profile.

`#include <bmx_push_user_profile.h>`

Inherits from BMXBaseObject

## Public Functions

|                                       | Name                                                                                                                                                                 |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                               | <p><a href="classfloo_1_1_b_m_x_push_user_profile.md#function-~bmxpushuserprofile"><strong>~BMXPushUserProfile</strong></a>()<br>Destructor</p>                      |
| virtual int64\_t                      | <p><a href="classfloo_1_1_b_m_x_push_user_profile.md#function-userid"><strong>userId</strong></a>() =0<br>User ID (unique)</p>                                       |
| virtual std::string                   | <p><a href="classfloo_1_1_b_m_x_push_user_profile.md#function-pushalias"><strong>pushAlias</strong></a>() =0<br>Push user alias</p>                                  |
| virtual std::string                   | <p><a href="classfloo_1_1_b_m_x_push_user_profile.md#function-pushtoken"><strong>pushToken</strong></a>() =0<br>Push user token</p>                                  |
| virtual const \[MessagePushSetting] & | <p><a href="classfloo_1_1_b_m_x_push_user_profile.md#function-messagepushsetting"><strong>messagePushSetting</strong></a>() =0<br>Push user information settings</p> |

## Protected Functions

|   | Name                                                                                             |
| - | ------------------------------------------------------------------------------------------------ |
|   | [**BMXPushUserProfile**](classfloo_1_1_b_m_x_push_user_profile.md#function-bmxpushuserprofile)() |

## Public Functions Documentation

### function \~BMXPushUserProfile

```cpp
inline virtual ~BMXPushUserProfile()
```

Destructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushUserProfile'></div>

```

### function userId

```cpp
virtual int64_t userId() =0
```

User ID (unique)

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushUserProfile'></div>

```

### function pushAlias

```cpp
virtual std::string pushAlias() =0
```

Push user alias

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushUserProfile'></div>

```

### function pushToken

```cpp
virtual std::string pushToken() =0
```

Push user token

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushUserProfile'></div>

```

### function messagePushSetting

```cpp
virtual const MessagePushSetting & messagePushSetting() =0
```

Push user information settings

**Return**: \[MessagePushSetting]

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushUserProfile'></div>

```

### function BMXPushUserProfile

```cpp
inline BMXPushUserProfile()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushUserProfile'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
