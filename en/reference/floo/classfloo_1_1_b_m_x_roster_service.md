---
title: floo::BMXRosterService
summary: Friend Service
---

# floo::BMXRosterService

Friend Service

`#include <bmx_roster_service.h>`

## Public Types

|                                                                                                         | Name                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class                                                                                              | <p><a href="classfloo_1_1_b_m_x_roster_service.md#enum-applicationstatus"><strong>ApplicationStatus</strong></a> { Pending, Accepted, Declined}<br>Request state</p> |
| typedef std::shared\_ptr< \[Application] >                                                              | [**ApplicationPtr**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#typedef-applicationptr)                                                                            |
| typedef std::vector< ApplicationPtr >                                                                   | [**ApplicationList**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#typedef-applicationlist)                                                                          |
| typedef [BMXResultPage](classfloo\_1\_1\_b\_m\_x\_result\_page.md)< ApplicationPtr >                    | [**BMXRosterApplicationResultPage**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#typedef-bmxrosterapplicationresultpage)                                            |
| typedef std::shared\_ptr< [BMXRosterApplicationResultPage](classfloo\_1\_1\_b\_m\_x\_result\_page.md) > | [**BMXRosterApplicationResultPagePtr**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#typedef-bmxrosterapplicationresultpageptr)                                      |
| typedef std::function< void(int percent)>                                                               | [**Callback**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#typedef-callback)                                                                                        |

## Public Functions

|                      | Name                                                                                                                                                                                                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual              | [**\~BMXRosterService**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#function-\~bmxrosterservice)()                                                                                                                                                                                  |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-get"><strong>get</strong></a>(std::vector&#x3C; int64_t > &#x26; list, bool forceRefresh) =0<br>Get friend list, force pull from server-side if forceRefresh == true</p>                                                   |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-fetchrosterbyid"><strong>fetchRosterById</strong></a>(int64_t rosterId, bool forceRefresh, BMXRosterItemPtr &#x26; item) =0<br>Search for user by contact id</p>                                                           |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-search"><strong>search</strong></a>(int64_t rosterId, bool forceRefresh, BMXRosterItemPtr &#x26; item) =0<br>Deprecated.</p>                                                                                               |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-fetchrosterbyname"><strong>fetchRosterByName</strong></a>(const std::string &#x26; name, bool forceRefresh, BMXRosterItemPtr &#x26; item) =0<br>Search for user by username</p>                                            |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-search"><strong>search</strong></a>(const std::string &#x26; name, bool forceRefresh, BMXRosterItemPtr &#x26; item) =0<br>Deprecated.</p>                                                                                  |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-fetchrostersbyidlist"><strong>fetchRostersByIdList</strong></a>(const std::vector&#x3C; int64_t > &#x26; rosterIdList, BMXRosterList &#x26; list, bool forceRefresh) =0<br>Search for user in batch by contact id list</p> |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-search"><strong>search</strong></a>(const std::vector&#x3C; int64_t > &#x26; rosterIdList, BMXRosterList &#x26; list, bool forceRefresh) =0<br>Deprecated.</p>                                                             |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-setitemlocalextension"><strong>setItemLocalExtension</strong></a>(BMXRosterItemPtr item, const JSON &#x26; extension) =0<br>Update friend's local extension information</p>                                                |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-setitemextension"><strong>setItemExtension</strong></a>(BMXRosterItemPtr item, const JSON &#x26; extension) =0<br>Update friend server extension information</p>                                                           |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-setitemalias"><strong>setItemAlias</strong></a>(BMXRosterItemPtr item, const JSON &#x26; alias) =0<br>Update friend's alias</p>                                                                                            |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-setitemmutenotification"><strong>setItemMuteNotification</strong></a>(BMXRosterItemPtr item, bool status) =0<br>Set whether to reject user message</p>                                                                     |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-getapplicationlist"><strong>getApplicationList</strong></a>(BMXRosterApplicationResultPagePtr &#x26; result, const std::string &#x26; cursor, int pageSize =10) =0<br>Get list of adding friend requests</p>               |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-apply"><strong>apply</strong></a>(int64_t rosterId, const std::string &#x26; message, const std::string &#x26; authAnswer ="") =0<br>Request to add friend</p>                                                             |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-remove"><strong>remove</strong></a>(int64_t rosterId) =0<br>Delete friend</p>                                                                                                                                              |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-accept"><strong>accept</strong></a>(int64_t rosterId) =0<br>Accept adding friend request</p>                                                                                                                               |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-decline"><strong>decline</strong></a>(int64_t rosterId, const std::string &#x26; reason) =0<br>Reject adding friend request</p>                                                                                            |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-block"><strong>block</strong></a>(int64_t rosterId) =0<br>Add to blacklist</p>                                                                                                                                             |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-unblock"><strong>unblock</strong></a>(int64_t rosterId) =0<br>Remove from blacklist</p>                                                                                                                                    |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-getblocklist"><strong>getBlockList</strong></a>(std::vector&#x3C; int64_t > &#x26; list, bool forceRefresh) =0<br>Get blacklist, force pull from server-side if forceRefresh == true</p>                                   |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(BMXRosterItemPtr item, bool thumbnail, Callback callback) =0<br>Download avatar</p>                                                                                    |
| virtual void         | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-addrosterlistener"><strong>addRosterListener</strong></a>(<a href="classfloo_1_1_b_m_x_roster_service_listener.md">BMXRosterServiceListener</a> * listener) =0<br>Add friend change listener</p>                           |
| virtual void         | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-removerosterlistener"><strong>removeRosterListener</strong></a>(<a href="classfloo_1_1_b_m_x_roster_service_listener.md">BMXRosterServiceListener</a> * listener) =0<br>Remove friend change listener</p>                  |

## Protected Functions

|   | Name                                                                                             |
| - | ------------------------------------------------------------------------------------------------ |
|   | [**BMXRosterService**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#function-bmxrosterservice)() |

## Public Types Documentation

### enum ApplicationStatus

| Enumerator | Value | Description      |
| ---------- | ----- | ---------------- |
| Pending    |       | Request pending  |
| Accepted   |       | Request accepted |
| Declined   |       | Request rejected |

Request state

### typedef ApplicationPtr

```cpp
typedef std::shared_ptr<Application> floo::BMXRosterService::ApplicationPtr;
```

### typedef ApplicationList

```cpp
typedef std::vector<ApplicationPtr> floo::BMXRosterService::ApplicationList;
```

### typedef BMXRosterApplicationResultPage

```cpp
typedef BMXResultPage<ApplicationPtr> floo::BMXRosterService::BMXRosterApplicationResultPage;
```

### typedef BMXRosterApplicationResultPagePtr

```cpp
typedef std::shared_ptr<BMXRosterApplicationResultPage> floo::BMXRosterService::BMXRosterApplicationResultPagePtr;
```

### typedef Callback

```cpp
typedef std::function<void(int percent)> floo::BMXRosterService::Callback;
```

## Public Functions Documentation

### function \~BMXRosterService

```cpp
inline virtual ~BMXRosterService()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function get

```cpp
virtual BMXErrorCode get(
    std::vector< int64_t > & list,
    bool forceRefresh
) =0
```

Get friend list, force pull from server-side if forceRefresh == true

**Parameters**:

* **list** List of friend ids, pass in an empty list function and fetch the returned friend id list here
* **forceRefresh** Whether to read data from server, true to force read from server, false to automatically read from server if the local read list is empty

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function fetchRosterById

```cpp
virtual BMXErrorCode fetchRosterById(
    int64_t rosterId,
    bool forceRefresh,
    BMXRosterItemPtr & item
) =0
```

Search for user by contact id

**Parameters**:

* **rosterId** Friend id to search
* **forceRefresh** True to force fetch from server, false to automatically fetch from server when query result is empty.
* **item** User information returned by query, passed in a pointing-to-empty shared\_ptr objective function and assigned automatically after executed.

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function search

```cpp
virtual BMXErrorCode search(
    int64_t rosterId,
    bool forceRefresh,
    BMXRosterItemPtr & item
) =0
```

Deprecated.

**Parameters**:

* **rosterId** Friend id to search
* **forceRefresh** True to force fetch from server, false to automatically fetch from server when query result is empty.
* **item** User information returned by query, passed in a pointing-to-empty shared\_ptr objective function and assigned automatically after executed.

**Return**: BMXErrorCode

use fetchRosterById instead.

Search for users

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function fetchRosterByName

```cpp
virtual BMXErrorCode fetchRosterByName(
    const std::string & name,
    bool forceRefresh,
    BMXRosterItemPtr & item
) =0
```

Search for user by username

**Parameters**:

* **name** Username to search
* **forceRefresh** True to force fetch from server, false to automatically fetch from server when query result is empty.
* **item** User information returned by query, passed in a pointing-to-empty shared\_ptr objective function and assigned automatically after executed.

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function search

```cpp
virtual BMXErrorCode search(
    const std::string & name,
    bool forceRefresh,
    BMXRosterItemPtr & item
) =0
```

Deprecated.

**Parameters**:

* **name** Username to search
* **forceRefresh** True to force fetch from server, false to automatically fetch from server when query result is empty.
* **item** User information returned by query, passed in a pointing-to-empty shared\_ptr objective function and assigned automatically after executed.

**Return**: BMXErrorCode

use fetchRosterByName instead.

Search for users

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function fetchRostersByIdList

```cpp
virtual BMXErrorCode fetchRostersByIdList(
    const std::vector< int64_t > & rosterIdList,
    BMXRosterList & list,
    bool forceRefresh
) =0
```

Search for user in batch by contact id list

**Parameters**:

* **rosterIdList** List of user ids to search
* **list** Returned friend information list, pass in an empty list function and fetch the returned result here
* **forceRefresh** Whether to force fetch from server, true to force fetch from server

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function search

```cpp
virtual BMXErrorCode search(
    const std::vector< int64_t > & rosterIdList,
    BMXRosterList & list,
    bool forceRefresh
) =0
```

Deprecated.

**Parameters**:

* **rosterIdList** List of user ids to search
* **list** Returned friend information list, pass in an empty list function and fetch the returned result here
* **forceRefresh** Whether to force fetch from server, true to force fetch from server

**Return**: BMXErrorCode

use fetchRostersByIdList instead.

Batch search for users

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function setItemLocalExtension

```cpp
virtual BMXErrorCode setItemLocalExtension(
    BMXRosterItemPtr item,
    const JSON & extension
) =0
```

Update friend's local extension information

**Parameters**:

* **item** User information
* **extension** Local extension information

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function setItemExtension

```cpp
virtual BMXErrorCode setItemExtension(
    BMXRosterItemPtr item,
    const JSON & extension
) =0
```

Update friend server extension information

**Parameters**:

* **item** User information
* **extension** Server extension information

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function setItemAlias

```cpp
virtual BMXErrorCode setItemAlias(
    BMXRosterItemPtr item,
    const JSON & alias
) =0
```

Update friend's alias

**Parameters**:

* **item** User information
* **alias** Friend alias

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function setItemMuteNotification

```cpp
virtual BMXErrorCode setItemMuteNotification(
    BMXRosterItemPtr item,
    bool status
) =0
```

Set whether to reject user message

**Parameters**:

* **item** User information
* **status** Whether to reject user message, true to reject, false to accept

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function getApplicationList

```cpp
virtual BMXErrorCode getApplicationList(
    BMXRosterApplicationResultPagePtr & result,
    const std::string & cursor,
    int pageSize =10
) =0
```

Get list of adding friend requests

**Parameters**:

* **result** Returned friend application list information, pass in a pointing-to-empty shared\_ptr objective function which will be automatically assigned after executed.
* **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation
* **pageSize** Page size

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function apply

```cpp
virtual BMXErrorCode apply(
    int64_t rosterId,
    const std::string & message,
    const std::string & authAnswer =""
) =0
```

Request to add friend

**Parameters**:

* **rosterId** User id requested to be added
* **message** Friend application information

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function remove

```cpp
virtual BMXErrorCode remove(
    int64_t rosterId
) =0
```

Delete friend

**Parameters**:

* **rosterId** Delete friend id

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function accept

```cpp
virtual BMXErrorCode accept(
    int64_t rosterId
) =0
```

Accept adding friend request

**Parameters**:

* **rosterId** User id to be added as a friend

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function decline

```cpp
virtual BMXErrorCode decline(
    int64_t rosterId,
    const std::string & reason
) =0
```

Reject adding friend request

**Parameters**:

* **rosterId** User id to be added as a friend
* **reason** Reason for rejection

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function block

```cpp
virtual BMXErrorCode block(
    int64_t rosterId
) =0
```

Add to blacklist

**Parameters**:

* **rosterId** Blacklisted user id

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function unblock

```cpp
virtual BMXErrorCode unblock(
    int64_t rosterId
) =0
```

Remove from blacklist

**Parameters**:

* **rosterId** Unblacklisted user id

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function getBlockList

```cpp
virtual BMXErrorCode getBlockList(
    std::vector< int64_t > & list,
    bool forceRefresh
) =0
```

Get blacklist, force pull from server-side if forceRefresh == true

**Parameters**:

* **list** List of friend ids, pass in an empty list function and fetch the returned blacklist id list here.
* **forceRefresh** Whether to read data from server, true to force read from server, false to automatically read from server if the local read list is empty

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function downloadAvatar

```cpp
virtual BMXErrorCode downloadAvatar(
    BMXRosterItemPtr item,
    bool thumbnail,
    Callback callback
) =0
```

Download avatar

**Parameters**:

* **item** User information
* **thumbnail** Whether to download thumbnail, true for thumbnail, false for original
* **callback** Download callback function

**Return**: BMXErrorCode

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function addRosterListener

```cpp
virtual void addRosterListener(
    BMXRosterServiceListener * listener
) =0
```

Add friend change listener

**Parameters**:

* **listener** Friend change listener

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function removeRosterListener

```cpp
virtual void removeRosterListener(
    BMXRosterServiceListener * listener
) =0
```

Remove friend change listener

**Parameters**:

* **listener** Friend change listener

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```

### function BMXRosterService

```cpp
inline BMXRosterService()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterService'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
