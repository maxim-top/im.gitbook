---
title: floo::BMXRosterService
summary: 好友Service 

---

# floo::BMXRosterService



好友Service 


`#include <bmx_roster_service.h>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[ApplicationStatus](classfloo_1_1_b_m_x_roster_service.md#enum-applicationstatus)** { Pending, Accepted, Declined}<br>请求状态  |
| typedef std::shared_ptr< [Application] > | **[ApplicationPtr](classfloo_1_1_b_m_x_roster_service.md#typedef-applicationptr)**  |
| typedef std::vector< ApplicationPtr > | **[ApplicationList](classfloo_1_1_b_m_x_roster_service.md#typedef-applicationlist)**  |
| typedef [BMXResultPage](classfloo_1_1_b_m_x_result_page.md)< ApplicationPtr > | **[BMXRosterApplicationResultPage](classfloo_1_1_b_m_x_roster_service.md#typedef-bmxrosterapplicationresultpage)**  |
| typedef std::shared_ptr< [BMXRosterApplicationResultPage](classfloo_1_1_b_m_x_result_page.md) > | **[BMXRosterApplicationResultPagePtr](classfloo_1_1_b_m_x_roster_service.md#typedef-bmxrosterapplicationresultpageptr)**  |
| typedef std::function< void(int percent)> | **[Callback](classfloo_1_1_b_m_x_roster_service.md#typedef-callback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXRosterService](classfloo_1_1_b_m_x_roster_service.md#function-~bmxrosterservice)**() |
| virtual BMXErrorCode | **[get](classfloo_1_1_b_m_x_roster_service.md#function-get)**(std::vector< int64_t > & list, bool forceRefresh) =0<br>获取好友列表，如果forceRefresh == true，则强制从服务端拉取  |
| virtual BMXErrorCode | **[fetchRosterById](classfloo_1_1_b_m_x_roster_service.md#function-fetchrosterbyid)**(int64_t rosterId, bool forceRefresh, BMXRosterItemPtr & item) =0<br>通过联系人id搜索用户  |
| virtual BMXErrorCode | **[search](classfloo_1_1_b_m_x_roster_service.md#function-search)**(int64_t rosterId, bool forceRefresh, BMXRosterItemPtr & item) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[fetchRosterByName](classfloo_1_1_b_m_x_roster_service.md#function-fetchrosterbyname)**(const std::string & name, bool forceRefresh, BMXRosterItemPtr & item) =0<br>通过用户名搜索用户  |
| virtual BMXErrorCode | **[search](classfloo_1_1_b_m_x_roster_service.md#function-search)**(const std::string & name, bool forceRefresh, BMXRosterItemPtr & item) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[fetchRostersByIdList](classfloo_1_1_b_m_x_roster_service.md#function-fetchrostersbyidlist)**(const std::vector< int64_t > & rosterIdList, BMXRosterList & list, bool forceRefresh) =0<br>通过联系人id列表批量搜索用户  |
| virtual BMXErrorCode | **[search](classfloo_1_1_b_m_x_roster_service.md#function-search)**(const std::vector< int64_t > & rosterIdList, BMXRosterList & list, bool forceRefresh) =0<br>Deprecated.  |
| virtual BMXErrorCode | **[setItemLocalExtension](classfloo_1_1_b_m_x_roster_service.md#function-setitemlocalextension)**(BMXRosterItemPtr item, const JSON & extension) =0<br>更新好友本地扩展信息  |
| virtual BMXErrorCode | **[setItemExtension](classfloo_1_1_b_m_x_roster_service.md#function-setitemextension)**(BMXRosterItemPtr item, const JSON & extension) =0<br>更新好友服务器扩展信息  |
| virtual BMXErrorCode | **[setItemAlias](classfloo_1_1_b_m_x_roster_service.md#function-setitemalias)**(BMXRosterItemPtr item, const JSON & alias) =0<br>更新好友别名  |
| virtual BMXErrorCode | **[setItemMuteNotification](classfloo_1_1_b_m_x_roster_service.md#function-setitemmutenotification)**(BMXRosterItemPtr item, bool status) =0<br>设置是否拒收用户消息  |
| virtual BMXErrorCode | **[getApplicationList](classfloo_1_1_b_m_x_roster_service.md#function-getapplicationlist)**(BMXRosterApplicationResultPagePtr & result, const std::string & cursor, int pageSize =10) =0<br>获取申请添加好友列表  |
| virtual BMXErrorCode | **[apply](classfloo_1_1_b_m_x_roster_service.md#function-apply)**(int64_t rosterId, const std::string & message, const std::string & authAnswer ="") =0<br>申请添加好友  |
| virtual BMXErrorCode | **[remove](classfloo_1_1_b_m_x_roster_service.md#function-remove)**(int64_t rosterId) =0<br>删除好友  |
| virtual BMXErrorCode | **[accept](classfloo_1_1_b_m_x_roster_service.md#function-accept)**(int64_t rosterId) =0<br>接受加好友申请  |
| virtual BMXErrorCode | **[decline](classfloo_1_1_b_m_x_roster_service.md#function-decline)**(int64_t rosterId, const std::string & reason) =0<br>拒绝加好友申请  |
| virtual BMXErrorCode | **[block](classfloo_1_1_b_m_x_roster_service.md#function-block)**(int64_t rosterId) =0<br>加入黑名单  |
| virtual BMXErrorCode | **[unblock](classfloo_1_1_b_m_x_roster_service.md#function-unblock)**(int64_t rosterId) =0<br>从黑名单移除  |
| virtual BMXErrorCode | **[getBlockList](classfloo_1_1_b_m_x_roster_service.md#function-getblocklist)**(std::vector< int64_t > & list, bool forceRefresh) =0<br>获取黑名单，如果forceRefresh == true，则强制从服务端拉取  |
| virtual BMXErrorCode | **[downloadAvatar](classfloo_1_1_b_m_x_roster_service.md#function-downloadavatar)**(BMXRosterItemPtr item, bool thumbnail, Callback callback) =0<br>下载头像  |
| virtual void | **[addRosterListener](classfloo_1_1_b_m_x_roster_service.md#function-addrosterlistener)**([BMXRosterServiceListener](classfloo_1_1_b_m_x_roster_service_listener.md) * listener) =0<br>添加好友变化监听者  |
| virtual void | **[removeRosterListener](classfloo_1_1_b_m_x_roster_service.md#function-removerosterlistener)**([BMXRosterServiceListener](classfloo_1_1_b_m_x_roster_service_listener.md) * listener) =0<br>移除好友变化监听者  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterService](classfloo_1_1_b_m_x_roster_service.md#function-bmxrosterservice)**() |

## Public Types Documentation

### enum ApplicationStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Pending | | 请求待处理   |
| Accepted | | 请求已接受   |
| Declined | | 请求已拒绝   |



请求状态 

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


### function get

```cpp
virtual BMXErrorCode get(
    std::vector< int64_t > & list,
    bool forceRefresh
) =0
```

获取好友列表，如果forceRefresh == true，则强制从服务端拉取 

**Parameters**: 

  * **list** 好友id列表，传入空列表函数返回后从此处获取返回的好友id列表 
  * **forceRefresh** 是否从服务器读取数据，true为强制从服务器获取，false情况下本地读取列表为空的情况下会自动从服务器读取 


**Return**: BMXErrorCode 

### function fetchRosterById

```cpp
virtual BMXErrorCode fetchRosterById(
    int64_t rosterId,
    bool forceRefresh,
    BMXRosterItemPtr & item
) =0
```

通过联系人id搜索用户 

**Parameters**: 

  * **rosterId** 搜索的好友id 
  * **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。 
  * **item** 查询返回的用户的信息，传入指向为空的shared_ptr对象函数执行后会自动赋值。 


**Return**: BMXErrorCode 

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

  * **rosterId** 搜索的好友id 
  * **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。 
  * **item** 查询返回的用户的信息，传入指向为空的shared_ptr对象函数执行后会自动赋值。 


**Return**: BMXErrorCode 

use fetchRosterById instead.

搜索用户 


### function fetchRosterByName

```cpp
virtual BMXErrorCode fetchRosterByName(
    const std::string & name,
    bool forceRefresh,
    BMXRosterItemPtr & item
) =0
```

通过用户名搜索用户 

**Parameters**: 

  * **name** 搜索的用户名 
  * **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。 
  * **item** 查询返回的用户的信息，传入指向为空的shared_ptr对象函数执行后会自动赋值。 


**Return**: BMXErrorCode 

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

  * **name** 搜索的用户名 
  * **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。 
  * **item** 查询返回的用户的信息，传入指向为空的shared_ptr对象函数执行后会自动赋值。 


**Return**: BMXErrorCode 

use fetchRosterByName instead.

搜索用户 


### function fetchRostersByIdList

```cpp
virtual BMXErrorCode fetchRostersByIdList(
    const std::vector< int64_t > & rosterIdList,
    BMXRosterList & list,
    bool forceRefresh
) =0
```

通过联系人id列表批量搜索用户 

**Parameters**: 

  * **rosterIdList** 需要搜索的用户id列表 
  * **list** 返回的好友信息列表，传入空列表函数返回后从此处获取返回的好友信息列表 
  * **forceRefresh** 是否强制从服务器获取，为true则强制从服务器获取 


**Return**: BMXErrorCode 

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

  * **rosterIdList** 需要搜索的用户id列表 
  * **list** 返回的好友信息列表，传入空列表函数返回后从此处获取返回的好友信息列表 
  * **forceRefresh** 是否强制从服务器获取，为true则强制从服务器获取 


**Return**: BMXErrorCode 

use fetchRostersByIdList instead.

批量搜索用户 


### function setItemLocalExtension

```cpp
virtual BMXErrorCode setItemLocalExtension(
    BMXRosterItemPtr item,
    const JSON & extension
) =0
```

更新好友本地扩展信息 

**Parameters**: 

  * **item** 用户信息 
  * **extension** 本地扩展信息 


**Return**: BMXErrorCode 

### function setItemExtension

```cpp
virtual BMXErrorCode setItemExtension(
    BMXRosterItemPtr item,
    const JSON & extension
) =0
```

更新好友服务器扩展信息 

**Parameters**: 

  * **item** 用户信息 
  * **extension** 服务器扩展信息 


**Return**: BMXErrorCode 

### function setItemAlias

```cpp
virtual BMXErrorCode setItemAlias(
    BMXRosterItemPtr item,
    const JSON & alias
) =0
```

更新好友别名 

**Parameters**: 

  * **item** 用户信息 
  * **alias** 好友别名 


**Return**: BMXErrorCode 

### function setItemMuteNotification

```cpp
virtual BMXErrorCode setItemMuteNotification(
    BMXRosterItemPtr item,
    bool status
) =0
```

设置是否拒收用户消息 

**Parameters**: 

  * **item** 用户信息 
  * **status** 是否拒收用户消息，true拒收，false不拒收 


**Return**: BMXErrorCode 

### function getApplicationList

```cpp
virtual BMXErrorCode getApplicationList(
    BMXRosterApplicationResultPagePtr & result,
    const std::string & cursor,
    int pageSize =10
) =0
```

获取申请添加好友列表 

**Parameters**: 

  * **result** 返回的申请好友列表信息，传入指向为空的shared_ptr对象函数执行后会自动赋值。 
  * **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor 
  * **pageSize** 分页大小 


**Return**: BMXErrorCode 

### function apply

```cpp
virtual BMXErrorCode apply(
    int64_t rosterId,
    const std::string & message,
    const std::string & authAnswer =""
) =0
```

申请添加好友 

**Parameters**: 

  * **rosterId** 申请添加的用户id 
  * **message** 好友申请信息 


**Return**: BMXErrorCode 

### function remove

```cpp
virtual BMXErrorCode remove(
    int64_t rosterId
) =0
```

删除好友 

**Parameters**: 

  * **rosterId** 删除的好友id 


**Return**: BMXErrorCode 

### function accept

```cpp
virtual BMXErrorCode accept(
    int64_t rosterId
) =0
```

接受加好友申请 

**Parameters**: 

  * **rosterId** 申请加为好友的用户id 


**Return**: BMXErrorCode 

### function decline

```cpp
virtual BMXErrorCode decline(
    int64_t rosterId,
    const std::string & reason
) =0
```

拒绝加好友申请 

**Parameters**: 

  * **rosterId** 申请加为好友的用户id 
  * **reason** 拒绝的原因 


**Return**: BMXErrorCode 

### function block

```cpp
virtual BMXErrorCode block(
    int64_t rosterId
) =0
```

加入黑名单 

**Parameters**: 

  * **rosterId** 加入黑名单的用户id 


**Return**: BMXErrorCode 

### function unblock

```cpp
virtual BMXErrorCode unblock(
    int64_t rosterId
) =0
```

从黑名单移除 

**Parameters**: 

  * **rosterId** 从黑名单移除的用户id 


**Return**: BMXErrorCode 

### function getBlockList

```cpp
virtual BMXErrorCode getBlockList(
    std::vector< int64_t > & list,
    bool forceRefresh
) =0
```

获取黑名单，如果forceRefresh == true，则强制从服务端拉取 

**Parameters**: 

  * **list** 好友id列表，传入空列表函数返回后从此处获取返回的黑名单id列表 
  * **forceRefresh** 是否从服务器读取数据，true为强制从服务器获取，false情况下本地读取列表为空的情况下会自动从服务器读取 


**Return**: BMXErrorCode 

### function downloadAvatar

```cpp
virtual BMXErrorCode downloadAvatar(
    BMXRosterItemPtr item,
    bool thumbnail,
    Callback callback
) =0
```

下载头像 

**Parameters**: 

  * **item** 用户信息 
  * **thumbnail** 是否下载缩略图，ture为缩略图，false为原图 
  * **callback** 下载回调函数 


**Return**: BMXErrorCode 

### function addRosterListener

```cpp
virtual void addRosterListener(
    BMXRosterServiceListener * listener
) =0
```

添加好友变化监听者 

**Parameters**: 

  * **listener** 好友变化监听者 


### function removeRosterListener

```cpp
virtual void removeRosterListener(
    BMXRosterServiceListener * listener
) =0
```

移除好友变化监听者 

**Parameters**: 

  * **listener** 好友变化监听者 


## Protected Functions Documentation

### function BMXRosterService

```cpp
inline BMXRosterService()
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800