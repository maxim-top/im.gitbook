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


### function delete

```java
inline synchronized void delete()
```


### function rosterId

```java
inline long rosterId()
```

Friend id 

**Return**: int64_t 

### function username

```java
inline String username()
```

Friend name 

**Return**: std::string 

### function nickname

```java
inline String nickname()
```

Friend nickname 

**Return**: std::string 

### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

Ratel server address of friend avatar 

**Return**: std::string 

### function avatarUrl

```java
inline String avatarUrl()
```

Friend avatar thumbnail server address 

**Return**: std::string 

### function avatarPath

```java
inline String avatarPath()
```

Local storage path of friend avatar 

**Return**: std::string 

### function avatarThumbnailUrl

```java
inline String avatarThumbnailUrl()
```

Friend avatar thumbnail address 

**Return**: std::string 

### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

Local storage path of friend avatar thumbnail 

**Return**: std::string 

### function publicInfo

```java
inline String publicInfo()
```

Extension information which is visible to user's friends, such as address, personal state and more 

**Return**: JSON(std::string) 

### function alias

```java
inline String alias()
```

Comments added by user to adding friend 

**Return**: JSON(std::string) 

### function ext

```java
inline String ext()
```

User's server extension information 

**Return**: JSON(std::string) 

### function localExt

```java
inline String localExt()
```

User's local extension information 

**Return**: JSON(std::string) 

### function relation

```java
inline BMXRosterItem.RosterRelation relation()
```

Contact relationship 

**Return**: [RosterRelation]

### function isMuteNotification

```java
inline boolean isMuteNotification()
```

Whether to alert user for message 

**Return**: bool 

### function addFriendAuthMode

```java
inline BMXRosterItem.AddFriendAuthMode addFriendAuthMode()
```

How roster to validate adding friend. 

**Return**: [AddFriendAuthMode]

### function authQuestion

```java
inline String authQuestion()
```

How roster to validate friend. 

**Return**: std::string 

## Protected Functions Documentation

### function BMXRosterItem

```java
inline BMXRosterItem(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
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


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800