---
title: im::floo::floolib::BMXRosterService
summary: Friend Service
---

# im::floo::floolib::BMXRosterService

Friend Service

## Public Classes

|       | Name                                                                                                                                          |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| class | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_1_1_application.md"><strong>Application</strong></a><br>Friend invitation</p> |

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                                     |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_service.md#function-delete)()                                                                                                                                                                                                        |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-get"><strong>get</strong></a>(ListOfLongLong list, boolean forceRefresh)<br>Get friend list, force pull from server-side if forceRefresh == true</p>                                                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-fetchrosterbyid"><strong>fetchRosterById</strong></a>(long rosterId, boolean forceRefresh, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item)<br>Search for users</p>                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-search"><strong>search</strong></a>(long rosterId, boolean forceRefresh, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item)<br>Search for users</p>                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-fetchrosterbyname"><strong>fetchRosterByName</strong></a>(String name, boolean forceRefresh, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item)<br>Search for users</p>                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-search"><strong>search</strong></a>(String name, boolean forceRefresh, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item)<br>Search for users</p>                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-fetchrostersbyidlist"><strong>fetchRostersByIdList</strong></a>(ListOfLongLong rosterIdList, BMXRosterItemList list, boolean forceRefresh)<br>Batch search for users</p>                                                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-search"><strong>search</strong></a>(ListOfLongLong rosterIdList, BMXRosterItemList list, boolean forceRefresh)<br>Batch search for users</p>                                                                                 |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemlocalextension"><strong>setItemLocalExtension</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, String extension)<br>Update friend's local extension information</p> |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemextension"><strong>setItemExtension</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, String extension)<br>Update friend server extension information</p>            |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemalias"><strong>setItemAlias</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, String alias)<br>Update friend's alias</p>                                             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemmutenotification"><strong>setItemMuteNotification</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, boolean status)<br>Set whether to reject user message</p>        |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-getapplicationlist"><strong>getApplicationList</strong></a>(ApplicationPage result, String cursor, int pageSize)<br>Get list of adding friend requests</p>                                                                   |
| \[BMXErrorCode]   | [**apply**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_service.md#function-apply)(long rosterId, String message, String authAnswer)                                                                                                                                                          |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-apply"><strong>apply</strong></a>(long rosterId, String message)<br>Request to add friend</p>                                                                                                                                |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-remove"><strong>remove</strong></a>(long rosterId)<br>Delete friend</p>                                                                                                                                                      |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-accept"><strong>accept</strong></a>(long rosterId)<br>Accept adding friend request</p>                                                                                                                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-decline"><strong>decline</strong></a>(long rosterId, String reason)<br>Reject adding friend request</p>                                                                                                                      |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-block"><strong>block</strong></a>(long rosterId)<br>Add to blacklist</p>                                                                                                                                                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-unblock"><strong>unblock</strong></a>(long rosterId)<br>Remove from blacklist</p>                                                                                                                                            |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-getblocklist"><strong>getBlockList</strong></a>(ListOfLongLong list, boolean forceRefresh)<br>Get blacklist, force pull from server-side if forceRefresh == true</p>                                                         |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, boolean thumbnail, FileProgressListener listener)<br>Download avatar</p>           |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-addrosterlistener"><strong>addRosterListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md">BMXRosterServiceListener</a> listener)<br>Add friend change listener</p>                 |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-removerosterlistener"><strong>removeRosterListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md">BMXRosterServiceListener</a> listener)<br>Remove friend change listener</p>        |

## Protected Functions

|      | Name                                                                                                                                                                                         |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXRosterService**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_service.md#function-bmxrosterservice)(long cPtr, boolean cMemoryOwn)                                           |
| void | [**finalize**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_service.md#function-finalize)()                                                                                        |
| long | [**getCPtr**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_service.md#function-getcptr)([BMXRosterService](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_service.md) obj) |

## Protected Attributes

|                   | Name                                                                                                      |
| ----------------- | --------------------------------------------------------------------------------------------------------- |
| transient boolean | [**swigCMemOwn**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_service.md#variable-swigcmemown) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function get

```java
inline BMXErrorCode get(
    ListOfLongLong list,
    boolean forceRefresh
)
```

Get friend list, force pull from server-side if forceRefresh == true

**Parameters**:

* **list** List of friend ids, pass in an empty list function and fetch the returned friend id list here
* **forceRefresh** Whether to read data from server, true to force read from server, false to automatically read from server if the local read list is empty

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function fetchRosterById

```java
inline BMXErrorCode fetchRosterById(
    long rosterId,
    boolean forceRefresh,
    BMXRosterItem item
)
```

Search for users

**Parameters**:

* **rosterId** Friend id to search
* **forceRefresh** True to force fetch from server, false to automatically fetch from server when query result is empty.
* **item** User information returned by query, passed in a pointing-to-empty shared\_ptr objective function and assigned automatically after executed.

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function search

```java
inline BMXErrorCode search(
    long rosterId,
    boolean forceRefresh,
    BMXRosterItem item
)
```

Search for users

**Parameters**:

* **rosterId** Friend id to search
* **forceRefresh** True to force fetch from server, false to automatically fetch from server when query result is empty.
* **item** User information returned by query, passed in a pointing-to-empty shared\_ptr objective function and assigned automatically after executed.

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function fetchRosterByName

```java
inline BMXErrorCode fetchRosterByName(
    String name,
    boolean forceRefresh,
    BMXRosterItem item
)
```

Search for users

**Parameters**:

* **name** Username to search
* **forceRefresh** True to force fetch from server, false to automatically fetch from server when query result is empty.
* **item** User information returned by query, passed in a pointing-to-empty shared\_ptr objective function and assigned automatically after executed.

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function search

```java
inline BMXErrorCode search(
    String name,
    boolean forceRefresh,
    BMXRosterItem item
)
```

Search for users

**Parameters**:

* **name** Username to search
* **forceRefresh** True to force fetch from server, false to automatically fetch from server when query result is empty.
* **item** User information returned by query, passed in a pointing-to-empty shared\_ptr objective function and assigned automatically after executed.

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function fetchRostersByIdList

```java
inline BMXErrorCode fetchRostersByIdList(
    ListOfLongLong rosterIdList,
    BMXRosterItemList list,
    boolean forceRefresh
)
```

Batch search for users

**Parameters**:

* **rosterIdList** List of user ids to search
* **list** Returned friend information list, pass in an empty list function and fetch the returned result here
* **forceRefresh** Whether to force fetch from server, true to force fetch from server

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function search

```java
inline BMXErrorCode search(
    ListOfLongLong rosterIdList,
    BMXRosterItemList list,
    boolean forceRefresh
)
```

Batch search for users

**Parameters**:

* **rosterIdList** List of user ids to search
* **list** Returned friend information list, pass in an empty list function and fetch the returned result here
* **forceRefresh** Whether to force fetch from server, true to force fetch from server

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function setItemLocalExtension

```java
inline BMXErrorCode setItemLocalExtension(
    BMXRosterItem item,
    String extension
)
```

Update friend's local extension information

**Parameters**:

* **item** User information
* **extension** Local extension information

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function setItemExtension

```java
inline BMXErrorCode setItemExtension(
    BMXRosterItem item,
    String extension
)
```

Update friend server extension information

**Parameters**:

* **item** User information
* **extension** Server extension information

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function setItemAlias

```java
inline BMXErrorCode setItemAlias(
    BMXRosterItem item,
    String alias
)
```

Update friend's alias

**Parameters**:

* **item** User information
* **alias** Friend alias

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function setItemMuteNotification

```java
inline BMXErrorCode setItemMuteNotification(
    BMXRosterItem item,
    boolean status
)
```

Set whether to reject user message

**Parameters**:

* **item** User information
* **status** Whether to reject user message, true to reject, false to accept

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function getApplicationList

```java
inline BMXErrorCode getApplicationList(
    ApplicationPage result,
    String cursor,
    int pageSize
)
```

Get list of adding friend requests

**Parameters**:

* **result** Returned friend application list information, pass in a pointing-to-empty shared\_ptr objective function which will be automatically assigned after executed.
* **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation
* **pageSize** Page size

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function apply

```java
inline BMXErrorCode apply(
    long rosterId,
    String message,
    String authAnswer
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function apply

```java
inline BMXErrorCode apply(
    long rosterId,
    String message
)
```

Request to add friend

**Parameters**:

* **rosterId** User id requested to be added
* **message** Friend application information

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function remove

```java
inline BMXErrorCode remove(
    long rosterId
)
```

Delete friend

**Parameters**:

* **rosterId** Delete friend id

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function accept

```java
inline BMXErrorCode accept(
    long rosterId
)
```

Accept adding friend request

**Parameters**:

* **rosterId** User id to be added as a friend

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function decline

```java
inline BMXErrorCode decline(
    long rosterId,
    String reason
)
```

Reject adding friend request

**Parameters**:

* **rosterId** User id to be added as a friend
* **reason** Reason for rejection

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function block

```java
inline BMXErrorCode block(
    long rosterId
)
```

Add to blacklist

**Parameters**:

* **rosterId** Blacklisted user id

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function unblock

```java
inline BMXErrorCode unblock(
    long rosterId
)
```

Remove from blacklist

**Parameters**:

* **rosterId** Unblacklisted user id

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function getBlockList

```java
inline BMXErrorCode getBlockList(
    ListOfLongLong list,
    boolean forceRefresh
)
```

Get blacklist, force pull from server-side if forceRefresh == true

**Parameters**:

* **list** List of friend ids, pass in an empty list function and fetch the returned blacklist id list here.
* **forceRefresh** Whether to read data from server, true to force read from server, false to automatically read from server if the local read list is empty

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function downloadAvatar

```java
inline BMXErrorCode downloadAvatar(
    BMXRosterItem item,
    boolean thumbnail,
    FileProgressListener listener
)
```

Download avatar

**Parameters**:

* **item** User information
* **thumbnail** Whether to download thumbnail, true for thumbnail, false for original
* **listener** Download callback function

**Return**: \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function addRosterListener

```java
inline void addRosterListener(
    BMXRosterServiceListener listener
)
```

Add friend change listener

**Parameters**:

* **listener** Friend change listener

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function removeRosterListener

```java
inline void removeRosterListener(
    BMXRosterServiceListener listener
)
```

Remove friend change listener

**Parameters**:

* **listener** Friend change listener

## Protected Functions Documentation

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function BMXRosterService

```java
inline BMXRosterService(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function finalize

```java
inline void finalize()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```

### function getCPtr

```java
static inline long getCPtr(
    BMXRosterService obj
)
```

## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterService'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
