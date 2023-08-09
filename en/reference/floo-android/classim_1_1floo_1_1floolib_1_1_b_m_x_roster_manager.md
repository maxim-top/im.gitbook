---
title: im::floo::floolib::BMXRosterManager
summary: Friend manager 

---

# im::floo::floolib::BMXRosterManager



Friend manager 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterManager](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-bmxrostermanager)**([BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md) service) |
| void | **[get](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-get)**(final boolean forceRefresh, final BMXDataCallBack< ListOfLongLong > callBack)<br>Get friend list, force pull from server-side if forceRefresh == true  |
| void | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-search)**(final long rosterId, final boolean forceRefresh, final BMXDataCallBack< [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) > callBack)<br>Search for users  |
| void | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-search)**(final String name, final boolean forceRefresh, final BMXDataCallBack< [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) > callBack)<br>Search for users  |
| void | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-search)**(final ListOfLongLong rosterIdList, final boolean forceRefresh, final BMXDataCallBack< BMXRosterItemList > callBack)<br>Batch search for users  |
| void | **[setItemExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-setitemextension)**(final [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, final String extension, final BMXCallBack callBack)<br>Update friend's local extension information  |
| void | **[setItemAlias](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-setitemalias)**(final [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, final String alias, final BMXCallBack callBack)<br>Update friend's alias  |
| void | **[setItemMuteNotification](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-setitemmutenotification)**(final [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, final boolean status, final BMXCallBack callBack)<br>Set whether to reject user message  |
| void | **[apply](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-apply)**(final long rosterId, final String message, final BMXCallBack callBack)<br>Request to add friend  |
| void | **[remove](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-remove)**(final long rosterId, final BMXCallBack callBack)<br>Delete friend  |
| void | **[getApplicationList](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-getapplicationlist)**(final String cursor, final int pageSize, final BMXDataCallBack< ApplicationPage > callBack)<br>Get list of adding friend requests  |
| void | **[accept](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-accept)**(final long rosterId, final BMXCallBack callBack)<br>Accept adding friend request  |
| void | **[decline](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-decline)**(final long rosterId, final String reason, final BMXCallBack callBack)<br>Reject adding friend request  |
| void | **[block](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-block)**(final long rosterId, final BMXCallBack callBack)<br>Add to blacklist  |
| void | **[unblock](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-unblock)**(final long rosterId, final BMXCallBack callBack)<br>Remove from blacklist  |
| void | **[getBlockList](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-getblocklist)**(final boolean forceRefresh, final BMXDataCallBack< ListOfLongLong > callBack)<br>Get blacklist, force pull from server-side if forceRefresh == true  |
| void | **[downloadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-downloadavatar)**(final [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, final FileProgressListener listener, final BMXCallBack callBack)<br>Download avatar  |
| void | **[addRosterListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-addrosterlistener)**([BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md) listener)<br>Add friend change listener  |
| void | **[removeRosterListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-removerosterlistener)**([BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md) listener)<br>Remove friend change listener  |

## Public Functions Documentation

### function BMXRosterManager

```java
inline BMXRosterManager(
    BMXRosterService service
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="BMXRosterManager" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode] friend id list 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="get" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode] user information returned by query 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="search" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode] user information returned by query 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="search" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode] List of friend information returned 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="search" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="setItemExtension" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="setItemAlias" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="setItemMuteNotification" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="apply" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="remove" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode] List of friend requests returned 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="getApplicationList" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="accept" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="decline" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="block" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="unblock" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode] friend id list 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="getBlockList" %}{% endlanying_code_snippet %}
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
  * **callBack** [BMXErrorCode]


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="downloadAvatar" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="addRosterListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterManager",function="removeRosterListener" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800