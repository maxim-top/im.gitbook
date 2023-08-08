---
title: floo::BMXPushUserProfile
summary: Push用户Profile.
---

# floo::BMXPushUserProfile

Push用户Profile.

`#include <bmx_push_user_profile.h>`

Inherits from BMXBaseObject

## Public Functions

|                                       | Name                                                                                                                                           |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                               | <p><a href="classfloo_1_1_b_m_x_push_user_profile.md#function-~bmxpushuserprofile"><strong>~BMXPushUserProfile</strong></a>()<br>析构函数</p>      |
| virtual int64\_t                      | <p><a href="classfloo_1_1_b_m_x_push_user_profile.md#function-userid"><strong>userId</strong></a>() =0<br>用户ID（唯一）</p>                         |
| virtual std::string                   | <p><a href="classfloo_1_1_b_m_x_push_user_profile.md#function-pushalias"><strong>pushAlias</strong></a>() =0<br>推送用户别名</p>                     |
| virtual std::string                   | <p><a href="classfloo_1_1_b_m_x_push_user_profile.md#function-pushtoken"><strong>pushToken</strong></a>() =0<br>推送用户token</p>                  |
| virtual const \[MessagePushSetting] & | <p><a href="classfloo_1_1_b_m_x_push_user_profile.md#function-messagepushsetting"><strong>messagePushSetting</strong></a>() =0<br>推送用户消息设定</p> |

## Protected Functions

|   | Name                                                                                                     |
| - | -------------------------------------------------------------------------------------------------------- |
|   | [**BMXPushUserProfile**](classfloo\_1\_1\_b\_m\_x\_push\_user\_profile.md#function-bmxpushuserprofile)() |

## Public Functions Documentation

### function \~BMXPushUserProfile

```cpp
inline virtual ~BMXPushUserProfile()
```

析构函数

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushUserProfile'></div>
```

### function userId

```cpp
virtual int64_t userId() =0
```

用户ID（唯一）

**Return**: int64\_t

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushUserProfile'></div>
```

### function pushAlias

```cpp
virtual std::string pushAlias() =0
```

推送用户别名

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushUserProfile'></div>
```

### function pushToken

```cpp
virtual std::string pushToken() =0
```

推送用户token

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXPushUserProfile'></div>
```

### function messagePushSetting

```cpp
virtual const MessagePushSetting & messagePushSetting() =0
```

推送用户消息设定

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



Updated on 2022-01-26 at 17:20:40 +0800
