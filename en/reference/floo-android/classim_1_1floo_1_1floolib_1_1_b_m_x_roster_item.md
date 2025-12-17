---
title: im::floo::floolib::BMXRosterItem
summary: Contact
---

# im::floo::floolib::BMXRosterItem

Contact

Inherits from BMXBaseObject

## Public Functions

|                                 | Name                                                                                                                                                                                                                             |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                 | [**BMXRosterItem**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-bmxrosteritem)()                                                                                                                                |
| synchronized void               | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-delete)()                                                                                                                                              |
| long                            | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-rosterid"><strong>rosterId</strong></a>()<br>Friend id</p>                                                                                              |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-username"><strong>username</strong></a>()<br>Friend name</p>                                                                                            |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-nickname"><strong>nickname</strong></a>()<br>Friend nickname</p>                                                                                        |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarratelurl"><strong>avatarRatelUrl</strong></a>()<br>Ratel server address of friend avatar</p>                                                      |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarurl"><strong>avatarUrl</strong></a>()<br>Friend avatar thumbnail server address</p>                                                               |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarpath"><strong>avatarPath</strong></a>()<br>Local storage path of friend avatar</p>                                                                |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarthumbnailurl"><strong>avatarThumbnailUrl</strong></a>()<br>Friend avatar thumbnail address</p>                                                    |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-avatarthumbnailpath"><strong>avatarThumbnailPath</strong></a>()<br>Local storage path of friend avatar thumbnail</p>                                    |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-publicinfo"><strong>publicInfo</strong></a>()<br>Extension information which is visible to user's friends, such as address, personal state and more</p> |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-alias"><strong>alias</strong></a>()<br>Comments added by user to adding friend</p>                                                                      |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-ext"><strong>ext</strong></a>()<br>User's server extension information</p>                                                                              |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-localext"><strong>localExt</strong></a>()<br>User's local extension information</p>                                                                     |
| BMXRosterItem.RosterRelation    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-relation"><strong>relation</strong></a>()<br>Contact relationship</p>                                                                                   |
| boolean                         | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-ismutenotification"><strong>isMuteNotification</strong></a>()<br>Whether to alert user for message</p>                                                  |
| BMXRosterItem.AddFriendAuthMode | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-addfriendauthmode"><strong>addFriendAuthMode</strong></a>()<br>How roster to validate adding friend.</p>                                                |
| String                          | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-authquestion"><strong>authQuestion</strong></a>()<br>How roster to validate friend.</p>                                                                 |

## Protected Functions

|      | Name                                                                                                                                                          |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXRosterItem**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-bmxrosteritem)(long cPtr, boolean cMemoryOwn)                                |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-finalize)()                                                                       |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#function-getcptr)([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) obj) |

## Public Attributes

|                | Name                                                                                  |
| -------------- | ------------------------------------------------------------------------------------- |
| transient long | [**swigCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md#variable-swigcptr) |

## Public Functions Documentation

### function BMXRosterItem

```java
inline BMXRosterItem()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function delete

```java
inline synchronized void delete()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function rosterId

```java
inline long rosterId()
```

Friend id

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function username

```java
inline String username()
```

Friend name

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function nickname

```java
inline String nickname()
```

Friend nickname

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function avatarRatelUrl

```java
inline String avatarRatelUrl()
```

Ratel server address of friend avatar

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function avatarUrl

```java
inline String avatarUrl()
```

Friend avatar thumbnail server address

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function avatarPath

```java
inline String avatarPath()
```

Local storage path of friend avatar

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function avatarThumbnailUrl

```java
inline String avatarThumbnailUrl()
```

Friend avatar thumbnail address

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function avatarThumbnailPath

```java
inline String avatarThumbnailPath()
```

Local storage path of friend avatar thumbnail

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function publicInfo

```java
inline String publicInfo()
```

Extension information which is visible to user's friends, such as address, personal state and more

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function alias

```java
inline String alias()
```

Comments added by user to adding friend

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function ext

```java
inline String ext()
```

User's server extension information

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function localExt

```java
inline String localExt()
```

User's local extension information

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function relation

```java
inline BMXRosterItem.RosterRelation relation()
```

Contact relationship

**Return**: \[RosterRelation]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function isMuteNotification

```java
inline boolean isMuteNotification()
```

Whether to alert user for message

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function addFriendAuthMode

```java
inline BMXRosterItem.AddFriendAuthMode addFriendAuthMode()
```

How roster to validate adding friend.

**Return**: \[AddFriendAuthMode]

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

```

### function finalize

```java
inline void finalize()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterItem'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
