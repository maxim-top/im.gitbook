---
title: im::floo::floolib::BMXRosterService
summary: Friend Service 

---

# im::floo::floolib::BMXRosterService



Friend Service 

## Public Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Application](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_1_1_application.md)** <br>Friend invitation  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-delete)**() |
| [BMXErrorCode] | **[get](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-get)**(ListOfLongLong list, boolean forceRefresh)<br>Get friend list, force pull from server-side if forceRefresh == true  |
| [BMXErrorCode] | **[fetchRosterById](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-fetchrosterbyid)**(long rosterId, boolean forceRefresh, [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item)<br>Search for users  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-search)**(long rosterId, boolean forceRefresh, [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item)<br>Search for users  |
| [BMXErrorCode] | **[fetchRosterByName](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-fetchrosterbyname)**(String name, boolean forceRefresh, [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item)<br>Search for users  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-search)**(String name, boolean forceRefresh, [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item)<br>Search for users  |
| [BMXErrorCode] | **[fetchRostersByIdList](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-fetchrostersbyidlist)**(ListOfLongLong rosterIdList, BMXRosterItemList list, boolean forceRefresh)<br>Batch search for users  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-search)**(ListOfLongLong rosterIdList, BMXRosterItemList list, boolean forceRefresh)<br>Batch search for users  |
| [BMXErrorCode] | **[setItemLocalExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemlocalextension)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, String extension)<br>Update friend's local extension information  |
| [BMXErrorCode] | **[setItemExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemextension)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, String extension)<br>Update friend server extension information  |
| [BMXErrorCode] | **[setItemAlias](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemalias)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, String alias)<br>Update friend's alias  |
| [BMXErrorCode] | **[setItemMuteNotification](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemmutenotification)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, boolean status)<br>Set whether to reject user message  |
| [BMXErrorCode] | **[getApplicationList](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-getapplicationlist)**(ApplicationPage result, String cursor, int pageSize)<br>Get list of adding friend requests  |
| [BMXErrorCode] | **[apply](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-apply)**(long rosterId, String message, String authAnswer) |
| [BMXErrorCode] | **[apply](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-apply)**(long rosterId, String message)<br>Request to add friend  |
| [BMXErrorCode] | **[remove](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-remove)**(long rosterId)<br>Delete friend  |
| [BMXErrorCode] | **[accept](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-accept)**(long rosterId)<br>Accept adding friend request  |
| [BMXErrorCode] | **[decline](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-decline)**(long rosterId, String reason)<br>Reject adding friend request  |
| [BMXErrorCode] | **[block](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-block)**(long rosterId)<br>Add to blacklist  |
| [BMXErrorCode] | **[unblock](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-unblock)**(long rosterId)<br>Remove from blacklist  |
| [BMXErrorCode] | **[getBlockList](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-getblocklist)**(ListOfLongLong list, boolean forceRefresh)<br>Get blacklist, force pull from server-side if forceRefresh == true  |
| [BMXErrorCode] | **[downloadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-downloadavatar)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, boolean thumbnail, FileProgressListener listener)<br>Download avatar  |
| void | **[addRosterListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-addrosterlistener)**([BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md) listener)<br>Add friend change listener  |
| void | **[removeRosterListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-removerosterlistener)**([BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md) listener)<br>Remove friend change listener  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-bmxrosterservice)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-getcptr)**([BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#variable-swigcmemown)**  |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
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


**Return**: [BMXErrorCode]

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
  * **item** User information returned by query, passed in a pointing-to-empty shared_ptr objective function and assigned automatically after executed. 


**Return**: [BMXErrorCode]

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
  * **item** User information returned by query, passed in a pointing-to-empty shared_ptr objective function and assigned automatically after executed. 


**Return**: [BMXErrorCode]

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
  * **item** User information returned by query, passed in a pointing-to-empty shared_ptr objective function and assigned automatically after executed. 


**Return**: [BMXErrorCode]

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
  * **item** User information returned by query, passed in a pointing-to-empty shared_ptr objective function and assigned automatically after executed. 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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

  * **result** Returned friend application list information, pass in a pointing-to-empty shared_ptr objective function which will be automatically assigned after executed. 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 


**Return**: [BMXErrorCode]

### function apply

```java
inline BMXErrorCode apply(
    long rosterId,
    String message,
    String authAnswer
)
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


**Return**: [BMXErrorCode]

### function remove

```java
inline BMXErrorCode remove(
    long rosterId
)
```

Delete friend 

**Parameters**: 

  * **rosterId** Delete friend id 


**Return**: [BMXErrorCode]

### function accept

```java
inline BMXErrorCode accept(
    long rosterId
)
```

Accept adding friend request 

**Parameters**: 

  * **rosterId** User id to be added as a friend 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

### function block

```java
inline BMXErrorCode block(
    long rosterId
)
```

Add to blacklist 

**Parameters**: 

  * **rosterId** Blacklisted user id 


**Return**: [BMXErrorCode]

### function unblock

```java
inline BMXErrorCode unblock(
    long rosterId
)
```

Remove from blacklist 

**Parameters**: 

  * **rosterId** Unblacklisted user id 


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

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


**Return**: [BMXErrorCode]

### function addRosterListener

```java
inline void addRosterListener(
    BMXRosterServiceListener listener
)
```

Add friend change listener 

**Parameters**: 

  * **listener** Friend change listener 


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

### function BMXRosterService

```java
inline BMXRosterService(
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
    BMXRosterService obj
)
```


## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800