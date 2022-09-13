---
title: floo::BMXRosterItem
summary: Contact 

---

# floo::BMXRosterItem



Contact 


`#include <bmx_roster_item.h>`

Inherits from BMXBaseObject

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[RosterRelation](classfloo_1_1_b_m_x_roster_item.md#enum-rosterrelation)** { Friend, Deleted, Stranger, Blocked}<br>Friend relationship  |
| enum class| **[AddFriendAuthMode](classfloo_1_1_b_m_x_roster_item.md#enum-addfriendauthmode)** { Open, NeedApproval, AnswerQuestion, RejectAll}<br>How roster authenticated when requested to be a friend  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXRosterItem](classfloo_1_1_b_m_x_roster_item.md#function-~bmxrosteritem)**()<br>Destructor  |
| virtual int64_t | **[rosterId](classfloo_1_1_b_m_x_roster_item.md#function-rosterid)**() =0<br>Friend id  |
| virtual const std::string & | **[username](classfloo_1_1_b_m_x_roster_item.md#function-username)**() =0<br>Friend name  |
| virtual const std::string & | **[nickname](classfloo_1_1_b_m_x_roster_item.md#function-nickname)**() =0<br>Friend nickname  |
| virtual std::string | **[avatarRatelUrl](classfloo_1_1_b_m_x_roster_item.md#function-avatarratelurl)**() =0<br>Ratel server address of friend avatar  |
| virtual std::string | **[avatarUrl](classfloo_1_1_b_m_x_roster_item.md#function-avatarurl)**() =0<br>Friend avatar thumbnail server address  |
| virtual std::string | **[avatarPath](classfloo_1_1_b_m_x_roster_item.md#function-avatarpath)**() =0<br>Local storage path of friend avatar  |
| virtual std::string | **[avatarThumbnailUrl](classfloo_1_1_b_m_x_roster_item.md#function-avatarthumbnailurl)**() =0<br>Server address of friend avatar thumbnail  |
| virtual std::string | **[avatarThumbnailPath](classfloo_1_1_b_m_x_roster_item.md#function-avatarthumbnailpath)**() =0<br>Local storage path of friend avatar thumbnail  |
| virtual const JSON & | **[publicInfo](classfloo_1_1_b_m_x_roster_item.md#function-publicinfo)**() =0<br>Extension information which is visible to user's friends, such as address, personal state and more  |
| virtual const JSON & | **[alias](classfloo_1_1_b_m_x_roster_item.md#function-alias)**() =0<br>Comments added by user to adding friend  |
| virtual const JSON & | **[ext](classfloo_1_1_b_m_x_roster_item.md#function-ext)**() =0<br>User's server extension information  |
| virtual const JSON & | **[localExt](classfloo_1_1_b_m_x_roster_item.md#function-localext)**() =0<br>User's local extension information  |
| virtual [RosterRelation](classfloo_1_1_b_m_x_roster_item.md#enum-rosterrelation) | **[relation](classfloo_1_1_b_m_x_roster_item.md#function-relation)**() =0<br>Contact relationship  |
| virtual bool | **[isMuteNotification](classfloo_1_1_b_m_x_roster_item.md#function-ismutenotification)**() =0<br>Whether to alert user for message  |
| virtual [AddFriendAuthMode](classfloo_1_1_b_m_x_roster_item.md#enum-addfriendauthmode) | **[addFriendAuthMode](classfloo_1_1_b_m_x_roster_item.md#function-addfriendauthmode)**() =0<br>How roster to validate adding friend.  |
| virtual const std::string & | **[authQuestion](classfloo_1_1_b_m_x_roster_item.md#function-authquestion)**() =0<br>How roster to validate friend.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterItem](classfloo_1_1_b_m_x_roster_item.md#function-bmxrosteritem)**() |

## Public Types Documentation

### enum RosterRelation

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Friend | | Friend   |
| Deleted | | Deleted   |
| Stranger | | Stranger   |
| Blocked | | Blacklisted   |



Friend relationship 

### enum AddFriendAuthMode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Open | | No authentication required, anyone can be added as a friend   |
| NeedApproval | | Consent is required to be added as a friend   |
| AnswerQuestion | | Need to answer authentication question correctly to be added as a friend   |
| RejectAll | | Reject all adding friend requests   |



How roster authenticated when requested to be a friend 

## Public Functions Documentation

### function ~BMXRosterItem

```cpp
inline virtual ~BMXRosterItem()
```

Destructor 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="~BMXRosterItem" %}{% endlanying_code_snippet %}
```
### function rosterId

```cpp
virtual int64_t rosterId() =0
```

Friend id 

**Return**: int64_t 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="rosterId" %}{% endlanying_code_snippet %}
```
### function username

```cpp
virtual const std::string & username() =0
```

Friend name 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="username" %}{% endlanying_code_snippet %}
```
### function nickname

```cpp
virtual const std::string & nickname() =0
```

Friend nickname 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="nickname" %}{% endlanying_code_snippet %}
```
### function avatarRatelUrl

```cpp
virtual std::string avatarRatelUrl() =0
```

Ratel server address of friend avatar 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="avatarRatelUrl" %}{% endlanying_code_snippet %}
```
### function avatarUrl

```cpp
virtual std::string avatarUrl() =0
```

Friend avatar thumbnail server address 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="avatarUrl" %}{% endlanying_code_snippet %}
```
### function avatarPath

```cpp
virtual std::string avatarPath() =0
```

Local storage path of friend avatar 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="avatarPath" %}{% endlanying_code_snippet %}
```
### function avatarThumbnailUrl

```cpp
virtual std::string avatarThumbnailUrl() =0
```

Server address of friend avatar thumbnail 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="avatarThumbnailUrl" %}{% endlanying_code_snippet %}
```
### function avatarThumbnailPath

```cpp
virtual std::string avatarThumbnailPath() =0
```

Local storage path of friend avatar thumbnail 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="avatarThumbnailPath" %}{% endlanying_code_snippet %}
```
### function publicInfo

```cpp
virtual const JSON & publicInfo() =0
```

Extension information which is visible to user's friends, such as address, personal state and more 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="publicInfo" %}{% endlanying_code_snippet %}
```
### function alias

```cpp
virtual const JSON & alias() =0
```

Comments added by user to adding friend 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="alias" %}{% endlanying_code_snippet %}
```
### function ext

```cpp
virtual const JSON & ext() =0
```

User's server extension information 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="ext" %}{% endlanying_code_snippet %}
```
### function localExt

```cpp
virtual const JSON & localExt() =0
```

User's local extension information 

**Return**: JSON(std::string) 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="localExt" %}{% endlanying_code_snippet %}
```
### function relation

```cpp
virtual RosterRelation relation() =0
```

Contact relationship 

**Return**: RosterRelation 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="relation" %}{% endlanying_code_snippet %}
```
### function isMuteNotification

```cpp
virtual bool isMuteNotification() =0
```

Whether to alert user for message 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="isMuteNotification" %}{% endlanying_code_snippet %}
```
### function addFriendAuthMode

```cpp
virtual AddFriendAuthMode addFriendAuthMode() =0
```

How roster to validate adding friend. 

**Return**: AddFriendAuthMode 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="addFriendAuthMode" %}{% endlanying_code_snippet %}
```
### function authQuestion

```cpp
virtual const std::string & authQuestion() =0
```

How roster to validate friend. 

**Return**: std::string 

## Protected Functions Documentation

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="authQuestion" %}{% endlanying_code_snippet %}
```
### function BMXRosterItem

```cpp
inline BMXRosterItem()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterItem",function="BMXRosterItem" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800