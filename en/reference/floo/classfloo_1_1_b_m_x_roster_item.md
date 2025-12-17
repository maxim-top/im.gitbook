---
title: floo::BMXRosterItem
summary: Contact
---

# floo::BMXRosterItem

Contact

`#include <bmx_roster_item.h>`

Inherits from BMXBaseObject

## Public Types

|            | Name                                                                                                                                                                                                                         |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_roster_item.md#enum-rosterrelation"><strong>RosterRelation</strong></a> { Friend, Deleted, Stranger, Blocked}<br>Friend relationship</p>                                                     |
| enum class | <p><a href="classfloo_1_1_b_m_x_roster_item.md#enum-addfriendauthmode"><strong>AddFriendAuthMode</strong></a> { Open, NeedApproval, AnswerQuestion, RejectAll}<br>How roster authenticated when requested to be a friend</p> |

## Public Functions

|                                                                                        | Name                                                                                                                                                                                                               |
| -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| virtual                                                                                | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-~bmxrosteritem"><strong>~BMXRosterItem</strong></a>()<br>Destructor</p>                                                                                    |
| virtual int64\_t                                                                       | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-rosterid"><strong>rosterId</strong></a>() =0<br>Friend id</p>                                                                                              |
| virtual const std::string &                                                            | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-username"><strong>username</strong></a>() =0<br>Friend name</p>                                                                                            |
| virtual const std::string &                                                            | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-nickname"><strong>nickname</strong></a>() =0<br>Friend nickname</p>                                                                                        |
| virtual std::string                                                                    | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-avatarratelurl"><strong>avatarRatelUrl</strong></a>() =0<br>Ratel server address of friend avatar</p>                                                      |
| virtual std::string                                                                    | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-avatarurl"><strong>avatarUrl</strong></a>() =0<br>Friend avatar thumbnail server address</p>                                                               |
| virtual std::string                                                                    | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-avatarpath"><strong>avatarPath</strong></a>() =0<br>Local storage path of friend avatar</p>                                                                |
| virtual std::string                                                                    | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-avatarthumbnailurl"><strong>avatarThumbnailUrl</strong></a>() =0<br>Server address of friend avatar thumbnail</p>                                          |
| virtual std::string                                                                    | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-avatarthumbnailpath"><strong>avatarThumbnailPath</strong></a>() =0<br>Local storage path of friend avatar thumbnail</p>                                    |
| virtual const JSON &                                                                   | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-publicinfo"><strong>publicInfo</strong></a>() =0<br>Extension information which is visible to user's friends, such as address, personal state and more</p> |
| virtual const JSON &                                                                   | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-alias"><strong>alias</strong></a>() =0<br>Comments added by user to adding friend</p>                                                                      |
| virtual const JSON &                                                                   | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-ext"><strong>ext</strong></a>() =0<br>User's server extension information</p>                                                                              |
| virtual const JSON &                                                                   | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-localext"><strong>localExt</strong></a>() =0<br>User's local extension information</p>                                                                     |
| virtual [RosterRelation](classfloo_1_1_b_m_x_roster_item.md#enum-rosterrelation)       | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-relation"><strong>relation</strong></a>() =0<br>Contact relationship</p>                                                                                   |
| virtual bool                                                                           | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-ismutenotification"><strong>isMuteNotification</strong></a>() =0<br>Whether to alert user for message</p>                                                  |
| virtual [AddFriendAuthMode](classfloo_1_1_b_m_x_roster_item.md#enum-addfriendauthmode) | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-addfriendauthmode"><strong>addFriendAuthMode</strong></a>() =0<br>How roster to validate adding friend.</p>                                                |
| virtual const std::string &                                                            | <p><a href="classfloo_1_1_b_m_x_roster_item.md#function-authquestion"><strong>authQuestion</strong></a>() =0<br>How roster to validate friend.</p>                                                                 |

## Protected Functions

|   | Name                                                                             |
| - | -------------------------------------------------------------------------------- |
|   | [**BMXRosterItem**](classfloo_1_1_b_m_x_roster_item.md#function-bmxrosteritem)() |

## Public Types Documentation

### enum RosterRelation

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Friend     |       | Friend      |
| Deleted    |       | Deleted     |
| Stranger   |       | Stranger    |
| Blocked    |       | Blacklisted |

Friend relationship

### enum AddFriendAuthMode

| Enumerator     | Value | Description                                                              |
| -------------- | ----- | ------------------------------------------------------------------------ |
| Open           |       | No authentication required, anyone can be added as a friend              |
| NeedApproval   |       | Consent is required to be added as a friend                              |
| AnswerQuestion |       | Need to answer authentication question correctly to be added as a friend |
| RejectAll      |       | Reject all adding friend requests                                        |

How roster authenticated when requested to be a friend

## Public Functions Documentation

### function \~BMXRosterItem

```cpp
inline virtual ~BMXRosterItem()
```

Destructor

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function rosterId

```cpp
virtual int64_t rosterId() =0
```

Friend id

**Return**: int64\_t

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function username

```cpp
virtual const std::string & username() =0
```

Friend name

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function nickname

```cpp
virtual const std::string & nickname() =0
```

Friend nickname

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function avatarRatelUrl

```cpp
virtual std::string avatarRatelUrl() =0
```

Ratel server address of friend avatar

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function avatarUrl

```cpp
virtual std::string avatarUrl() =0
```

Friend avatar thumbnail server address

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function avatarPath

```cpp
virtual std::string avatarPath() =0
```

Local storage path of friend avatar

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function avatarThumbnailUrl

```cpp
virtual std::string avatarThumbnailUrl() =0
```

Server address of friend avatar thumbnail

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function avatarThumbnailPath

```cpp
virtual std::string avatarThumbnailPath() =0
```

Local storage path of friend avatar thumbnail

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function publicInfo

```cpp
virtual const JSON & publicInfo() =0
```

Extension information which is visible to user's friends, such as address, personal state and more

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function alias

```cpp
virtual const JSON & alias() =0
```

Comments added by user to adding friend

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function ext

```cpp
virtual const JSON & ext() =0
```

User's server extension information

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function localExt

```cpp
virtual const JSON & localExt() =0
```

User's local extension information

**Return**: JSON(std::string)

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function relation

```cpp
virtual RosterRelation relation() =0
```

Contact relationship

**Return**: RosterRelation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function isMuteNotification

```cpp
virtual bool isMuteNotification() =0
```

Whether to alert user for message

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function addFriendAuthMode

```cpp
virtual AddFriendAuthMode addFriendAuthMode() =0
```

How roster to validate adding friend.

**Return**: AddFriendAuthMode

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>

```

### function BMXRosterItem

```cpp
inline BMXRosterItem()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterItem'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
