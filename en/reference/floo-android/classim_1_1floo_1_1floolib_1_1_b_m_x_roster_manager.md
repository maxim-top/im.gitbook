---
title: im::floo::floolib::BMXRosterManager
summary: Friend manager
---

# im::floo::floolib::BMXRosterManager

Friend manager

## Public Functions

|      | Name                                                                                                                                                                                                                                                                                                                                      |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXRosterManager**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_manager.md#function-bmxrostermanager)([BMXRosterService](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_service.md) service)                                                                                                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-get"><strong>get</strong></a>(final boolean forceRefresh, final BMXDataCallBack&#x3C; ListOfLongLong > callBack)<br>Get friend list, force pull from server-side if forceRefresh == true</p>                                                                  |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-search"><strong>search</strong></a>(final long rosterId, final boolean forceRefresh, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> > callBack)<br>Search for users</p>                          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-search"><strong>search</strong></a>(final String name, final boolean forceRefresh, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> > callBack)<br>Search for users</p>                            |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-search"><strong>search</strong></a>(final ListOfLongLong rosterIdList, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXRosterItemList > callBack)<br>Batch search for users</p>                                                                    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-setitemextension"><strong>setItemExtension</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, final String extension, final BMXCallBack callBack)<br>Update friend's local extension information</p>    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-setitemalias"><strong>setItemAlias</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, final String alias, final BMXCallBack callBack)<br>Update friend's alias</p>                                      |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-setitemmutenotification"><strong>setItemMuteNotification</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, final boolean status, final BMXCallBack callBack)<br>Set whether to reject user message</p> |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-apply"><strong>apply</strong></a>(final long rosterId, final String message, final BMXCallBack callBack)<br>Request to add friend</p>                                                                                                                         |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-remove"><strong>remove</strong></a>(final long rosterId, final BMXCallBack callBack)<br>Delete friend</p>                                                                                                                                                     |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-getapplicationlist"><strong>getApplicationList</strong></a>(final String cursor, final int pageSize, final BMXDataCallBack&#x3C; ApplicationPage > callBack)<br>Get list of adding friend requests</p>                                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-accept"><strong>accept</strong></a>(final long rosterId, final BMXCallBack callBack)<br>Accept adding friend request</p>                                                                                                                                      |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-decline"><strong>decline</strong></a>(final long rosterId, final String reason, final BMXCallBack callBack)<br>Reject adding friend request</p>                                                                                                               |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-block"><strong>block</strong></a>(final long rosterId, final BMXCallBack callBack)<br>Add to blacklist</p>                                                                                                                                                    |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-unblock"><strong>unblock</strong></a>(final long rosterId, final BMXCallBack callBack)<br>Remove from blacklist</p>                                                                                                                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-getblocklist"><strong>getBlockList</strong></a>(final boolean forceRefresh, final BMXDataCallBack&#x3C; ListOfLongLong > callBack)<br>Get blacklist, force pull from server-side if forceRefresh == true</p>                                                  |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, final FileProgressListener listener, final BMXCallBack callBack)<br>Download avatar</p>                       |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-addrosterlistener"><strong>addRosterListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md">BMXRosterServiceListener</a> listener)<br>Add friend change listener</p>                                                  |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-removerosterlistener"><strong>removeRosterListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md">BMXRosterServiceListener</a> listener)<br>Remove friend change listener</p>                                         |

## Public Functions Documentation

### function BMXRosterManager

```java
inline BMXRosterManager(
    BMXRosterService service
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function get

```java
inline void get(
    final boolean forceRefresh,
    final BMXDataCallBack< ListOfLongLong > callBack
)
```

Get friend list, force pull from server-side if forceRefresh == true

**Parameters**:

* **forceRefresh** Whether to read data from server, true to force read from server, false to automatically read from server if the local read list is empty
* **callBack** \[BMXErrorCode] friend id list

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function search

```java
inline void search(
    final long rosterId,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXRosterItem > callBack
)
```

Search for users

**Parameters**:

* **rosterId** Friend id to search
* **forceRefresh** True to force fetch from server, false to automatically fetch from server when query result is empty.
* **callBack** \[BMXErrorCode] user information returned by query

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function search

```java
inline void search(
    final String name,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXRosterItem > callBack
)
```

Search for users

**Parameters**:

* **name** Username to search
* **forceRefresh** True to force fetch from server, false to automatically fetch from server when query result is empty.
* **callBack** \[BMXErrorCode] user information returned by query

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function search

```java
inline void search(
    final ListOfLongLong rosterIdList,
    final boolean forceRefresh,
    final BMXDataCallBack< BMXRosterItemList > callBack
)
```

Batch search for users

**Parameters**:

* **rosterIdList** List of user ids to search
* **forceRefresh** Whether to force fetch from server, true to force fetch from server
* **callBack** \[BMXErrorCode] List of friend information returned

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function setItemExtension

```java
inline void setItemExtension(
    final BMXRosterItem item,
    final String extension,
    final BMXCallBack callBack
)
```

Update friend's local extension information

**Parameters**:

* **item** User information
* **extension** Local extension information
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function setItemAlias

```java
inline void setItemAlias(
    final BMXRosterItem item,
    final String alias,
    final BMXCallBack callBack
)
```

Update friend's alias

**Parameters**:

* **item** User information
* **alias** Friend alias
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function setItemMuteNotification

```java
inline void setItemMuteNotification(
    final BMXRosterItem item,
    final boolean status,
    final BMXCallBack callBack
)
```

Set whether to reject user message

**Parameters**:

* **item** User information
* **status** Whether to reject user message, true to reject, false to accept
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function apply

```java
inline void apply(
    final long rosterId,
    final String message,
    final BMXCallBack callBack
)
```

Request to add friend

**Parameters**:

* **rosterId** User id requested to be added
* **message** Friend application information
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function remove

```java
inline void remove(
    final long rosterId,
    final BMXCallBack callBack
)
```

Delete friend

**Parameters**:

* **rosterId** Delete friend id
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function getApplicationList

```java
inline void getApplicationList(
    final String cursor,
    final int pageSize,
    final BMXDataCallBack< ApplicationPage > callBack
)
```

Get list of adding friend requests

**Parameters**:

* **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation
* **pageSize** Page size
* **callBack** \[BMXErrorCode] List of friend requests returned

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function accept

```java
inline void accept(
    final long rosterId,
    final BMXCallBack callBack
)
```

Accept adding friend request

**Parameters**:

* **rosterId** User id to be added as a friend
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function decline

```java
inline void decline(
    final long rosterId,
    final String reason,
    final BMXCallBack callBack
)
```

Reject adding friend request

**Parameters**:

* **rosterId** User id to be added as a friend
* **reason** Reason for rejection
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function block

```java
inline void block(
    final long rosterId,
    final BMXCallBack callBack
)
```

Add to blacklist

**Parameters**:

* **rosterId** Blacklisted user id
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function unblock

```java
inline void unblock(
    final long rosterId,
    final BMXCallBack callBack
)
```

Remove from blacklist

**Parameters**:

* **rosterId** Unblacklisted user id
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function getBlockList

```java
inline void getBlockList(
    final boolean forceRefresh,
    final BMXDataCallBack< ListOfLongLong > callBack
)
```

Get blacklist, force pull from server-side if forceRefresh == true

**Parameters**:

* **forceRefresh** Whether to read data from server, true to force read from server, false to automatically read from server if the local read list is empty
* **callBack** \[BMXErrorCode] friend id list

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

### function downloadAvatar

```java
inline void downloadAvatar(
    final BMXRosterItem item,
    final FileProgressListener listener,
    final BMXCallBack callBack
)
```

Download avatar

**Parameters**:

* **item** User information
* **listener** Download callback function
* **callBack** \[BMXErrorCode]

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
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
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
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

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```



Updated on 2022-01-26 at 17:18:31 +0800
