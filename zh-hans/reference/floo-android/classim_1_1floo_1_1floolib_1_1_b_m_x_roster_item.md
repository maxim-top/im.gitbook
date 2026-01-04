---
title: im::floo::floolib::BMXRosterItem
summary: 联系人 

---

# im::floo::floolib::BMXRosterItem



联系人 

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-bmxrosteritem)**() |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-delete)**() |
| long | **[rosterId](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-rosterid)**()<br>好友Id  |
| String | **[username](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-username)**()<br>好友名  |
| String | **[nickname](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-nickname)**()<br>好友昵称  |
| String | **[avatarRatelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarratelurl)**()<br>好友头像ratel服务器地址  |
| String | **[avatarUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarurl)**()<br>好友头像服务器地址  |
| String | **[avatarPath](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarpath)**()<br>好友头像本地存储路径  |
| String | **[avatarThumbnailUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarthumbnailurl)**()<br>好友头像缩略图地址  |
| String | **[avatarThumbnailPath](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarthumbnailpath)**()<br>好友头像缩略图本地存储路径  |
| String | **[publicInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-publicinfo)**()<br>扩展信息，用户设置的好友可以看到的信息，比如地址，个性签名等  |
| String | **[alias](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-alias)**()<br>用户对好友添加的备注等信息  |
| String | **[ext](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-ext)**()<br>用户的服务器扩展信息  |
| String | **[localExt](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-localext)**()<br>用户的本地扩展信息  |
| BMXRosterItem.RosterRelation | **[relation](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-relation)**()<br>联系人关系  |
| boolean | **[isMuteNotification](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-ismutenotification)**()<br>是否提醒用户消息  |
| BMXRosterItem.AddFriendAuthMode | **[addFriendAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-addfriendauthmode)**()<br>roster的好友添加验证方式。  |
| String | **[authQuestion](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-authquestion)**()<br>roster的好友验证问题。  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-bmxrosteritem)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-getcptr)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) obj) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| transient long | **[swigCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#variable-swigcptr)**  |

## Public Functions Documentation

### function BMXRosterItem

```java
inline BMXRosterItem()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="BMXRosterItem" %}{% endlanying_code_snippet %}
```
### function delete

```java
inline synchronized void delete()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="delete" %}{% endlanying_code_snippet %}
```
### function rosterId

```java
inline long rosterId()
```

好友Id 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="rosterId" %}{% endlanying_code_snippet %}
```
### function username

```java
inline String username()
```

好友名 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="username" %}{% endlanying_code_snippet %}
```
### function nickname

```java
inline String nickname()
```

好友昵称 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="nickname" %}{% endlanying_code_snippet %}
```
### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

好友头像ratel服务器地址 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="avatarRatelUrl" %}{% endlanying_code_snippet %}
```
### function avatarUrl

```java
inline String avatarUrl()
```

好友头像服务器地址 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="avatarUrl" %}{% endlanying_code_snippet %}
```
### function avatarPath

```java
inline String avatarPath()
```

好友头像本地存储路径 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="avatarPath" %}{% endlanying_code_snippet %}
```
### function avatarThumbnailUrl

```java
inline String avatarThumbnailUrl()
```

好友头像缩略图地址 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="avatarThumbnailUrl" %}{% endlanying_code_snippet %}
```
### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

好友头像缩略图本地存储路径 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="avatarThumbnailPath" %}{% endlanying_code_snippet %}
```
### function publicInfo

```java
inline String publicInfo()
```

扩展信息，用户设置的好友可以看到的信息，比如地址，个性签名等 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="publicInfo" %}{% endlanying_code_snippet %}
```
### function alias

```java
inline String alias()
```

用户对好友添加的备注等信息 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="alias" %}{% endlanying_code_snippet %}
```
### function ext

```java
inline String ext()
```

用户的服务器扩展信息 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="ext" %}{% endlanying_code_snippet %}
```
### function localExt

```java
inline String localExt()
```

用户的本地扩展信息 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="localExt" %}{% endlanying_code_snippet %}
```
### function relation

```java
inline BMXRosterItem.RosterRelation relation()
```

联系人关系 

**Return**: [RosterRelation]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="relation" %}{% endlanying_code_snippet %}
```
### function isMuteNotification

```java
inline boolean isMuteNotification()
```

是否提醒用户消息 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="isMuteNotification" %}{% endlanying_code_snippet %}
```
### function addFriendAuthMode

```java
inline BMXRosterItem.AddFriendAuthMode addFriendAuthMode()
```

roster的好友添加验证方式。 

**Return**: [AddFriendAuthMode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="addFriendAuthMode" %}{% endlanying_code_snippet %}
```
### function authQuestion

```java
inline String authQuestion()
```

roster的好友验证问题。 

**Return**: std::string 

## Protected Functions Documentation

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="authQuestion" %}{% endlanying_code_snippet %}
```
### function BMXRosterItem

```java
inline BMXRosterItem(
    long cPtr,
    boolean cMemoryOwn
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="BMXRosterItem" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="finalize" %}{% endlanying_code_snippet %}
```
### function getCPtr

```java
static inline long getCPtr(
    BMXRosterItem obj
)
```


## Public Attributes Documentation

### variable swigCPtr

```java
transient long swigCPtr;
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800