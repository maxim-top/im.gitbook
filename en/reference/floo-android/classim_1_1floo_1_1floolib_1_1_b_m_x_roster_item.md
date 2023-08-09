---
title: im::floo::floolib::BMXRosterItem
summary: Contact 

---

# im::floo::floolib::BMXRosterItem



Contact 

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-bmxrosteritem)**() |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-delete)**() |
| long | **[rosterId](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-rosterid)**()<br>Friend id  |
| String | **[username](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-username)**()<br>Friend name  |
| String | **[nickname](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-nickname)**()<br>Friend nickname  |
| String | **[avatarRatelUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarratelurl)**()<br>Ratel server address of friend avatar  |
| String | **[avatarUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarurl)**()<br>Friend avatar thumbnail server address  |
| String | **[avatarPath](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarpath)**()<br>Local storage path of friend avatar  |
| String | **[avatarThumbnailUrl](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarthumbnailurl)**()<br>Friend avatar thumbnail address  |
| String | **[avatarThumbnailPath](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarthumbnailpath)**()<br>Local storage path of friend avatar thumbnail  |
| String | **[publicInfo](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-publicinfo)**()<br>Extension information which is visible to user's friends, such as address, personal state and more  |
| String | **[alias](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-alias)**()<br>Comments added by user to adding friend  |
| String | **[ext](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-ext)**()<br>User's server extension information  |
| String | **[localExt](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-localext)**()<br>User's local extension information  |
| BMXRosterItem.RosterRelation | **[relation](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-relation)**()<br>Contact relationship  |
| boolean | **[isMuteNotification](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-ismutenotification)**()<br>Whether to alert user for message  |
| BMXRosterItem.AddFriendAuthMode | **[addFriendAuthMode](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-addfriendauthmode)**()<br>How roster to validate adding friend.  |
| String | **[authQuestion](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-authquestion)**()<br>How roster to validate friend.  |

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

Friend id 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="rosterId" %}{% endlanying_code_snippet %}
```
### function username

```java
inline String username()
```

Friend name 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="username" %}{% endlanying_code_snippet %}
```
### function nickname

```java
inline String nickname()
```

Friend nickname 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="nickname" %}{% endlanying_code_snippet %}
```
### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

Ratel server address of friend avatar 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="avatarRatelUrl" %}{% endlanying_code_snippet %}
```
### function avatarUrl

```java
inline String avatarUrl()
```

Friend avatar thumbnail server address 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="avatarUrl" %}{% endlanying_code_snippet %}
```
### function avatarPath

```java
inline String avatarPath()
```

Local storage path of friend avatar 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="avatarPath" %}{% endlanying_code_snippet %}
```
### function avatarThumbnailUrl

```java
inline String avatarThumbnailUrl()
```

Friend avatar thumbnail address 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="avatarThumbnailUrl" %}{% endlanying_code_snippet %}
```
### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

Local storage path of friend avatar thumbnail 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="avatarThumbnailPath" %}{% endlanying_code_snippet %}
```
### function publicInfo

```java
inline String publicInfo()
```

Extension information which is visible to user's friends, such as address, personal state and more 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="publicInfo" %}{% endlanying_code_snippet %}
```
### function alias

```java
inline String alias()
```

Comments added by user to adding friend 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="alias" %}{% endlanying_code_snippet %}
```
### function ext

```java
inline String ext()
```

User's server extension information 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="ext" %}{% endlanying_code_snippet %}
```
### function localExt

```java
inline String localExt()
```

User's local extension information 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="localExt" %}{% endlanying_code_snippet %}
```
### function relation

```java
inline BMXRosterItem.RosterRelation relation()
```

Contact relationship 

**Return**: [RosterRelation]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="relation" %}{% endlanying_code_snippet %}
```
### function isMuteNotification

```java
inline boolean isMuteNotification()
```

Whether to alert user for message 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="isMuteNotification" %}{% endlanying_code_snippet %}
```
### function addFriendAuthMode

```java
inline BMXRosterItem.AddFriendAuthMode addFriendAuthMode()
```

How roster to validate adding friend. 

**Return**: [AddFriendAuthMode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterItem",function="addFriendAuthMode" %}{% endlanying_code_snippet %}
```
### function authQuestion

```java
inline String authQuestion()
```

How roster to validate friend. 

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