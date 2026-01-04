---
title: floo::BMXRosterService
summary: Friend Service 

---

# floo::BMXRosterService



Friend Service 


`#include <bmx_roster_service.h>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[ApplicationStatus](classfloo_1_1_b_m_x_roster_service.md#enum-applicationstatus)** { Pending, Accepted, Declined}<br>Request state  |
| typedef std::shared_ptr< [Application] > | **[ApplicationPtr](classfloo_1_1_b_m_x_roster_service.md#typedef-applicationptr)**  |
| typedef std::vector< ApplicationPtr > | **[ApplicationList](classfloo_1_1_b_m_x_roster_service.md#typedef-applicationlist)**  |
| typedef [BMXResultPage](classfloo_1_1_b_m_x_result_page.md)< ApplicationPtr > | **[BMXRosterApplicationResultPage](classfloo_1_1_b_m_x_roster_service.md#typedef-bmxrosterapplicationresultpage)**  |
| typedef std::shared_ptr< [BMXRosterApplicationResultPage](classfloo_1_1_b_m_x_result_page.md) > | **[BMXRosterApplicationResultPagePtr](classfloo_1_1_b_m_x_roster_service.md#typedef-bmxrosterapplicationresultpageptr)**  |
| typedef std::function< void(int percent)> | **[Callback](classfloo_1_1_b_m_x_roster_service.md#typedef-callback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXRosterService](classfloo_1_1_b_m_x_roster_service.md#function-~bmxrosterservice)**() |
| virtual BMXErrorCode | **[get](classfloo_1_1_b_m_x_roster_service.md#function-get)**(std::vector< int64_t > & list, bool forceRefresh) =0<br>Get friend list, force pull from server-side if forceRefresh == true  |
| virtual BMXErrorCode | **[fetchRosterById](classfloo_1_1_b_m_x_roster_service.md#function-fetchrosterbyid)**(int64_t rosterId, bool forceRefresh, BMXRosterItemPtr & item) =0<br>Search for user by contact id  |
| virtual BMXErrorCode | **[search](classfloo_1_1_b_m_x_roster_service.md#function-search)**(int64_t rosterId, bool forceRefresh, BMXRosterItemPtr & item) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[fetchRosterByName](classfloo_1_1_b_m_x_roster_service.md#function-fetchrosterbyname)**(const std::string & name, bool forceRefresh, BMXRosterItemPtr & item) =0<br>Search for user by username  |
| virtual BMXErrorCode | **[search](classfloo_1_1_b_m_x_roster_service.md#function-search)**(const std::string & name, bool forceRefresh, BMXRosterItemPtr & item) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[fetchRostersByIdList](classfloo_1_1_b_m_x_roster_service.md#function-fetchrostersbyidlist)**(const std::vector< int64_t > & rosterIdList, BMXRosterList & list, bool forceRefresh) =0<br>Search for user in batch by contact id list  |
| virtual BMXErrorCode | **[search](classfloo_1_1_b_m_x_roster_service.md#function-search)**(const std::vector< int64_t > & rosterIdList, BMXRosterList & list, bool forceRefresh) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[setItemLocalExtension](classfloo_1_1_b_m_x_roster_service.md#function-setitemlocalextension)**(BMXRosterItemPtr item, const JSON & extension) =0<br>Update friend's local extension information  |
| virtual BMXErrorCode | **[setItemExtension](classfloo_1_1_b_m_x_roster_service.md#function-setitemextension)**(BMXRosterItemPtr item, const JSON & extension) =0<br>Update friend server extension information  |
| virtual BMXErrorCode | **[setItemAlias](classfloo_1_1_b_m_x_roster_service.md#function-setitemalias)**(BMXRosterItemPtr item, const JSON & alias) =0<br>Update friend's alias  |
| virtual BMXErrorCode | **[setItemMuteNotification](classfloo_1_1_b_m_x_roster_service.md#function-setitemmutenotification)**(BMXRosterItemPtr item, bool status) =0<br>Set whether to reject user message  |
| virtual BMXErrorCode | **[getApplicationList](classfloo_1_1_b_m_x_roster_service.md#function-getapplicationlist)**(BMXRosterApplicationResultPagePtr & result, const std::string & cursor, int pageSize =10) =0<br>Get list of adding friend requests  |
| virtual BMXErrorCode | **[apply](classfloo_1_1_b_m_x_roster_service.md#function-apply)**(int64_t rosterId, const std::string & message, const std::string & authAnswer ="") =0<br>Request to add friend  |
| virtual BMXErrorCode | **[remove](classfloo_1_1_b_m_x_roster_service.md#function-remove)**(int64_t rosterId) =0<br>Delete friend  |
| virtual BMXErrorCode | **[accept](classfloo_1_1_b_m_x_roster_service.md#function-accept)**(int64_t rosterId) =0<br>Accept adding friend request  |
| virtual BMXErrorCode | **[decline](classfloo_1_1_b_m_x_roster_service.md#function-decline)**(int64_t rosterId, const std::string & reason) =0<br>Reject adding friend request  |
| virtual BMXErrorCode | **[block](classfloo_1_1_b_m_x_roster_service.md#function-block)**(int64_t rosterId) =0<br>Add to blacklist  |
| virtual BMXErrorCode | **[unblock](classfloo_1_1_b_m_x_roster_service.md#function-unblock)**(int64_t rosterId) =0<br>Remove from blacklist  |
| virtual BMXErrorCode | **[getBlockList](classfloo_1_1_b_m_x_roster_service.md#function-getblocklist)**(std::vector< int64_t > & list, bool forceRefresh) =0<br>Get blacklist, force pull from server-side if forceRefresh == true  |
| virtual BMXErrorCode | **[downloadAvatar](classfloo_1_1_b_m_x_roster_service.md#function-downloadavatar)**(BMXRosterItemPtr item, bool thumbnail, Callback callback) =0<br>Download avatar  |
| virtual void | **[addRosterListener](classfloo_1_1_b_m_x_roster_service.md#function-addrosterlistener)**([BMXRosterServiceListener](classfloo_1_1_b_m_x_roster_service_listener.md) * listener) =0<br>Add friend change listener  |
| virtual void | **[removeRosterListener](classfloo_1_1_b_m_x_roster_service.md#function-removerosterlistener)**([BMXRosterServiceListener](classfloo_1_1_b_m_x_roster_service_listener.md) * listener) =0<br>Remove friend change listener  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterService](classfloo_1_1_b_m_x_roster_service.md#function-bmxrosterservice)**() |

## Public Types Documentation

### enum ApplicationStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Pending | | Request pending   |
| Accepted | | Request accepted   |
| Declined | | Request rejected   |



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

### function ~BMXRosterService

```cpp
inline virtual ~BMXRosterService()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="~BMXRosterService" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="get" %}{% endlanying_code_snippet %}
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
  * **item** User information returned by query, passed in a pointing-to-empty shared_ptr objective function and assigned automatically after executed. 


**Return**: BMXErrorCode 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="fetchRosterById" %}{% endlanying_code_snippet %}
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
  * **item** User information returned by query, passed in a pointing-to-empty shared_ptr objective function and assigned automatically after executed. 


**Return**: BMXErrorCode 

use fetchRosterById instead.

Search for users 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="search" %}{% endlanying_code_snippet %}
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
  * **item** User information returned by query, passed in a pointing-to-empty shared_ptr objective function and assigned automatically after executed. 


**Return**: BMXErrorCode 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="fetchRosterByName" %}{% endlanying_code_snippet %}
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
  * **item** User information returned by query, passed in a pointing-to-empty shared_ptr objective function and assigned automatically after executed. 


**Return**: BMXErrorCode 

use fetchRosterByName instead.

Search for users 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="search" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="fetchRostersByIdList" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="search" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="setItemLocalExtension" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="setItemExtension" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="setItemAlias" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="setItemMuteNotification" %}{% endlanying_code_snippet %}
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

  * **result** Returned friend application list information, pass in a pointing-to-empty shared_ptr objective function which will be automatically assigned after executed. 
  * **cursor** Paged starting cursor, passed in as empty-valued first, followed by the cursor in the result returned by last operation 
  * **pageSize** Page size 


**Return**: BMXErrorCode 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="getApplicationList" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="apply" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="remove" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="accept" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="decline" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="block" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="unblock" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="getBlockList" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="downloadAvatar" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="addRosterListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="removeRosterListener" %}{% endlanying_code_snippet %}
```
### function BMXRosterService

```cpp
inline BMXRosterService()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXRosterService",function="BMXRosterService" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800