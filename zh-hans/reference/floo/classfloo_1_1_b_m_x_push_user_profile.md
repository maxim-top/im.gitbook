---
title: floo::BMXPushUserProfile
summary: Push用户Profile. 

---

# floo::BMXPushUserProfile



Push用户Profile. 


`#include <bmx_push_user_profile.h>`

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXPushUserProfile](classfloo_1_1_b_m_x_push_user_profile.md#function-~bmxpushuserprofile)**()<br>析构函数  |
| virtual int64_t | **[userId](classfloo_1_1_b_m_x_push_user_profile.md#function-userid)**() =0<br>用户ID（唯一）  |
| virtual std::string | **[pushAlias](classfloo_1_1_b_m_x_push_user_profile.md#function-pushalias)**() =0<br>推送用户别名  |
| virtual std::string | **[pushToken](classfloo_1_1_b_m_x_push_user_profile.md#function-pushtoken)**() =0<br>推送用户token  |
| virtual const [MessagePushSetting] & | **[messagePushSetting](classfloo_1_1_b_m_x_push_user_profile.md#function-messagepushsetting)**() =0<br>推送用户消息设定  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXPushUserProfile](classfloo_1_1_b_m_x_push_user_profile.md#function-bmxpushuserprofile)**() |

## Public Functions Documentation

### function ~BMXPushUserProfile

```cpp
inline virtual ~BMXPushUserProfile()
```

析构函数 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushUserProfile",function="~BMXPushUserProfile" %}{% endlanying_code_snippet %}
```
### function userId

```cpp
virtual int64_t userId() =0
```

用户ID（唯一） 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushUserProfile",function="userId" %}{% endlanying_code_snippet %}
```
### function pushAlias

```cpp
virtual std::string pushAlias() =0
```

推送用户别名 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushUserProfile",function="pushAlias" %}{% endlanying_code_snippet %}
```
### function pushToken

```cpp
virtual std::string pushToken() =0
```

推送用户token 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushUserProfile",function="pushToken" %}{% endlanying_code_snippet %}
```
### function messagePushSetting

```cpp
virtual const MessagePushSetting & messagePushSetting() =0
```

推送用户消息设定 

**Return**: [MessagePushSetting]

## Protected Functions Documentation

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushUserProfile",function="messagePushSetting" %}{% endlanying_code_snippet %}
```
### function BMXPushUserProfile

```cpp
inline BMXPushUserProfile()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXPushUserProfile",function="BMXPushUserProfile" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800