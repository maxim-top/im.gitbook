---
title: floo::BMXRosterService
summary: 好友Service
---

# floo::BMXRosterService

好友Service

`#include <bmx_roster_service.h>`

## Public Types

|                                                                                                         | Name                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class                                                                                              | <p><a href="classfloo_1_1_b_m_x_roster_service.md#enum-applicationstatus"><strong>ApplicationStatus</strong></a> { Pending, Accepted, Declined}<br>请求状态</p> |
| typedef std::shared\_ptr< \[Application] >                                                              | [**ApplicationPtr**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#typedef-applicationptr)                                                                   |
| typedef std::vector< ApplicationPtr >                                                                   | [**ApplicationList**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#typedef-applicationlist)                                                                 |
| typedef [BMXResultPage](classfloo\_1\_1\_b\_m\_x\_result\_page.md)< ApplicationPtr >                    | [**BMXRosterApplicationResultPage**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#typedef-bmxrosterapplicationresultpage)                                   |
| typedef std::shared\_ptr< [BMXRosterApplicationResultPage](classfloo\_1\_1\_b\_m\_x\_result\_page.md) > | [**BMXRosterApplicationResultPagePtr**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#typedef-bmxrosterapplicationresultpageptr)                             |
| typedef std::function< void(int percent)>                                                               | [**Callback**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#typedef-callback)                                                                               |

## Public Functions

|                      | Name                                                                                                                                                                                                                                                      |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual              | [**\~BMXRosterService**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#function-\~bmxrosterservice)()                                                                                                                                                      |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-get"><strong>get</strong></a>(std::vector&#x3C; int64_t > &#x26; list, bool forceRefresh) =0<br>获取好友列表，如果forceRefresh == true，则强制从服务端拉取</p>                                                    |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-fetchrosterbyid"><strong>fetchRosterById</strong></a>(int64_t rosterId, bool forceRefresh, BMXRosterItemPtr &#x26; item) =0<br>通过联系人id搜索用户</p>                                                 |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-search"><strong>search</strong></a>(int64_t rosterId, bool forceRefresh, BMXRosterItemPtr &#x26; item) =0<br>Deprecated.</p>                                                                   |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-fetchrosterbyname"><strong>fetchRosterByName</strong></a>(const std::string &#x26; name, bool forceRefresh, BMXRosterItemPtr &#x26; item) =0<br>通过用户名搜索用户</p>                                  |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-search"><strong>search</strong></a>(const std::string &#x26; name, bool forceRefresh, BMXRosterItemPtr &#x26; item) =0<br>Deprecated.</p>                                                      |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-fetchrostersbyidlist"><strong>fetchRostersByIdList</strong></a>(const std::vector&#x3C; int64_t > &#x26; rosterIdList, BMXRosterList &#x26; list, bool forceRefresh) =0<br>通过联系人id列表批量搜索用户</p> |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-search"><strong>search</strong></a>(const std::vector&#x3C; int64_t > &#x26; rosterIdList, BMXRosterList &#x26; list, bool forceRefresh) =0<br>Deprecated.</p>                                 |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-setitemlocalextension"><strong>setItemLocalExtension</strong></a>(BMXRosterItemPtr item, const JSON &#x26; extension) =0<br>更新好友本地扩展信息</p>                                                     |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-setitemextension"><strong>setItemExtension</strong></a>(BMXRosterItemPtr item, const JSON &#x26; extension) =0<br>更新好友服务器扩展信息</p>                                                              |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-setitemalias"><strong>setItemAlias</strong></a>(BMXRosterItemPtr item, const JSON &#x26; alias) =0<br>更新好友别名</p>                                                                               |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-setitemmutenotification"><strong>setItemMuteNotification</strong></a>(BMXRosterItemPtr item, bool status) =0<br>设置是否拒收用户消息</p>                                                                 |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-getapplicationlist"><strong>getApplicationList</strong></a>(BMXRosterApplicationResultPagePtr &#x26; result, const std::string &#x26; cursor, int pageSize =10) =0<br>获取申请添加好友列表</p>           |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-apply"><strong>apply</strong></a>(int64_t rosterId, const std::string &#x26; message, const std::string &#x26; authAnswer ="") =0<br>申请添加好友</p>                                                |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-remove"><strong>remove</strong></a>(int64_t rosterId) =0<br>删除好友</p>                                                                                                                           |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-accept"><strong>accept</strong></a>(int64_t rosterId) =0<br>接受加好友申请</p>                                                                                                                        |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-decline"><strong>decline</strong></a>(int64_t rosterId, const std::string &#x26; reason) =0<br>拒绝加好友申请</p>                                                                                     |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-block"><strong>block</strong></a>(int64_t rosterId) =0<br>加入黑名单</p>                                                                                                                            |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-unblock"><strong>unblock</strong></a>(int64_t rosterId) =0<br>从黑名单移除</p>                                                                                                                       |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-getblocklist"><strong>getBlockList</strong></a>(std::vector&#x3C; int64_t > &#x26; list, bool forceRefresh) =0<br>获取黑名单，如果forceRefresh == true，则强制从服务端拉取</p>                                   |
| virtual BMXErrorCode | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(BMXRosterItemPtr item, bool thumbnail, Callback callback) =0<br>下载头像</p>                                                                   |
| virtual void         | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-addrosterlistener"><strong>addRosterListener</strong></a>(<a href="classfloo_1_1_b_m_x_roster_service_listener.md">BMXRosterServiceListener</a> * listener) =0<br>添加好友变化监听者</p>                |
| virtual void         | <p><a href="classfloo_1_1_b_m_x_roster_service.md#function-removerosterlistener"><strong>removeRosterListener</strong></a>(<a href="classfloo_1_1_b_m_x_roster_service_listener.md">BMXRosterServiceListener</a> * listener) =0<br>移除好友变化监听者</p>          |

## Protected Functions

|   | Name                                                                                             |
| - | ------------------------------------------------------------------------------------------------ |
|   | [**BMXRosterService**](classfloo\_1\_1\_b\_m\_x\_roster\_service.md#function-bmxrosterservice)() |

## Public Types Documentation

### enum ApplicationStatus

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Pending    |       | 请求待处理       |
| Accepted   |       | 请求已接受       |
| Declined   |       | 请求已拒绝       |

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

获取好友列表，如果forceRefresh == true，则强制从服务端拉取

**Parameters**:

* **list** 好友id列表，传入空列表函数返回后从此处获取返回的好友id列表
* **forceRefresh** 是否从服务器读取数据，true为强制从服务器获取，false情况下本地读取列表为空的情况下会自动从服务器读取

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

通过联系人id搜索用户

**Parameters**:

* **rosterId** 搜索的好友id
* **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。
* **item** 查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

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

* **rosterId** 搜索的好友id
* **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。
* **item** 查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

**Return**: BMXErrorCode

use fetchRosterById instead.

搜索用户

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

通过用户名搜索用户

**Parameters**:

* **name** 搜索的用户名
* **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。
* **item** 查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

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

* **name** 搜索的用户名
* **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。
* **item** 查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

**Return**: BMXErrorCode

use fetchRosterByName instead.

搜索用户

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

通过联系人id列表批量搜索用户

**Parameters**:

* **rosterIdList** 需要搜索的用户id列表
* **list** 返回的好友信息列表，传入空列表函数返回后从此处获取返回的好友信息列表
* **forceRefresh** 是否强制从服务器获取，为true则强制从服务器获取

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

* **rosterIdList** 需要搜索的用户id列表
* **list** 返回的好友信息列表，传入空列表函数返回后从此处获取返回的好友信息列表
* **forceRefresh** 是否强制从服务器获取，为true则强制从服务器获取

**Return**: BMXErrorCode

use fetchRostersByIdList instead.

批量搜索用户

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

更新好友本地扩展信息

**Parameters**:

* **item** 用户信息
* **extension** 本地扩展信息

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

更新好友服务器扩展信息

**Parameters**:

* **item** 用户信息
* **extension** 服务器扩展信息

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

更新好友别名

**Parameters**:

* **item** 用户信息
* **alias** 好友别名

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

设置是否拒收用户消息

**Parameters**:

* **item** 用户信息
* **status** 是否拒收用户消息，true拒收，false不拒收

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

获取申请添加好友列表

**Parameters**:

* **result** 返回的申请好友列表信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。
* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小

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

申请添加好友

**Parameters**:

* **rosterId** 申请添加的用户id
* **message** 好友申请信息

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

删除好友

**Parameters**:

* **rosterId** 删除的好友id

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

接受加好友申请

**Parameters**:

* **rosterId** 申请加为好友的用户id

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

拒绝加好友申请

**Parameters**:

* **rosterId** 申请加为好友的用户id
* **reason** 拒绝的原因

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

加入黑名单

**Parameters**:

* **rosterId** 加入黑名单的用户id

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

从黑名单移除

**Parameters**:

* **rosterId** 从黑名单移除的用户id

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

获取黑名单，如果forceRefresh == true，则强制从服务端拉取

**Parameters**:

* **list** 好友id列表，传入空列表函数返回后从此处获取返回的黑名单id列表
* **forceRefresh** 是否从服务器读取数据，true为强制从服务器获取，false情况下本地读取列表为空的情况下会自动从服务器读取

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

下载头像

**Parameters**:

* **item** 用户信息
* **thumbnail** 是否下载缩略图，ture为缩略图，false为原图
* **callback** 下载回调函数

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

添加好友变化监听者

**Parameters**:

* **listener** 好友变化监听者

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

移除好友变化监听者

**Parameters**:

* **listener** 好友变化监听者

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
