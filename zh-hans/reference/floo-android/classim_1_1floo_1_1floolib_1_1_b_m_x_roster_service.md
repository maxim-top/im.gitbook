---
title: im::floo::floolib::BMXRosterService
summary: 好友Service
---

# im::floo::floolib::BMXRosterService

好友Service

## Public Classes

|       | Name                                                                                                                             |
| ----- | -------------------------------------------------------------------------------------------------------------------------------- |
| class | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_1_1_application.md"><strong>Application</strong></a><br>好友邀请</p> |

## Public Functions

|                   | Name                                                                                                                                                                                                                                                                                |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| synchronized void | [**delete**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_service.md#function-delete)()                                                                                                                                                                                   |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-get"><strong>get</strong></a>(ListOfLongLong list, boolean forceRefresh)<br>获取好友列表，如果forceRefresh == true，则强制从服务端拉取</p>                                                                                 |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-fetchrosterbyid"><strong>fetchRosterById</strong></a>(long rosterId, boolean forceRefresh, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item)<br>搜索用户</p>            |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-search"><strong>search</strong></a>(long rosterId, boolean forceRefresh, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item)<br>搜索用户</p>                              |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-fetchrosterbyname"><strong>fetchRosterByName</strong></a>(String name, boolean forceRefresh, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item)<br>搜索用户</p>          |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-search"><strong>search</strong></a>(String name, boolean forceRefresh, <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item)<br>搜索用户</p>                                |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-fetchrostersbyidlist"><strong>fetchRostersByIdList</strong></a>(ListOfLongLong rosterIdList, BMXRosterItemList list, boolean forceRefresh)<br>批量搜索用户</p>                                                |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-search"><strong>search</strong></a>(ListOfLongLong rosterIdList, BMXRosterItemList list, boolean forceRefresh)<br>批量搜索用户</p>                                                                            |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemlocalextension"><strong>setItemLocalExtension</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, String extension)<br>更新好友本地扩展信息</p>             |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemextension"><strong>setItemExtension</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, String extension)<br>更新好友服务器扩展信息</p>                      |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemalias"><strong>setItemAlias</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, String alias)<br>更新好友别名</p>                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemmutenotification"><strong>setItemMuteNotification</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, boolean status)<br>设置是否拒收用户消息</p>           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-getapplicationlist"><strong>getApplicationList</strong></a>(ApplicationPage result, String cursor, int pageSize)<br>获取申请添加好友列表</p>                                                                      |
| \[BMXErrorCode]   | [**apply**](classim\_1\_1floo\_1\_1floolib\_1\_1\_b\_m\_x\_roster\_service.md#function-apply)(long rosterId, String message, String authAnswer)                                                                                                                                     |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-apply"><strong>apply</strong></a>(long rosterId, String message)<br>申请添加好友</p>                                                                                                                          |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-remove"><strong>remove</strong></a>(long rosterId)<br>删除好友</p>                                                                                                                                          |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-accept"><strong>accept</strong></a>(long rosterId)<br>接受加好友申请</p>                                                                                                                                       |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-decline"><strong>decline</strong></a>(long rosterId, String reason)<br>拒绝加好友申请</p>                                                                                                                      |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-block"><strong>block</strong></a>(long rosterId)<br>加入黑名单</p>                                                                                                                                           |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-unblock"><strong>unblock</strong></a>(long rosterId)<br>从黑名单移除</p>                                                                                                                                      |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-getblocklist"><strong>getBlockList</strong></a>(ListOfLongLong list, boolean forceRefresh)<br>获取黑名单，如果forceRefresh == true，则强制从服务端拉取</p>                                                                |
| \[BMXErrorCode]   | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, boolean thumbnail, FileProgressListener listener)<br>下载头像</p> |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-addrosterlistener"><strong>addRosterListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md">BMXRosterServiceListener</a> listener)<br>添加好友变化监听者</p>             |
| void              | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-removerosterlistener"><strong>removeRosterListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md">BMXRosterServiceListener</a> listener)<br>移除好友变化监听者</p>       |

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

获取好友列表，如果forceRefresh == true，则强制从服务端拉取

**Parameters**:

* **list** 好友id列表，传入空列表函数返回后从此处获取返回的好友id列表
* **forceRefresh** 是否从服务器读取数据，true为强制从服务器获取，false情况下本地读取列表为空的情况下会自动从服务器读取

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

搜索用户

**Parameters**:

* **rosterId** 搜索的好友id
* **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。
* **item** 查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

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

搜索用户

**Parameters**:

* **rosterId** 搜索的好友id
* **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。
* **item** 查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

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

搜索用户

**Parameters**:

* **name** 搜索的用户名
* **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。
* **item** 查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

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

搜索用户

**Parameters**:

* **name** 搜索的用户名
* **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。
* **item** 查询返回的用户的信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。

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

批量搜索用户

**Parameters**:

* **rosterIdList** 需要搜索的用户id列表
* **list** 返回的好友信息列表，传入空列表函数返回后从此处获取返回的好友信息列表
* **forceRefresh** 是否强制从服务器获取，为true则强制从服务器获取

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

批量搜索用户

**Parameters**:

* **rosterIdList** 需要搜索的用户id列表
* **list** 返回的好友信息列表，传入空列表函数返回后从此处获取返回的好友信息列表
* **forceRefresh** 是否强制从服务器获取，为true则强制从服务器获取

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

更新好友本地扩展信息

**Parameters**:

* **item** 用户信息
* **extension** 本地扩展信息

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

更新好友服务器扩展信息

**Parameters**:

* **item** 用户信息
* **extension** 服务器扩展信息

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

更新好友别名

**Parameters**:

* **item** 用户信息
* **alias** 好友别名

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

设置是否拒收用户消息

**Parameters**:

* **item** 用户信息
* **status** 是否拒收用户消息，true拒收，false不拒收

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

获取申请添加好友列表

**Parameters**:

* **result** 返回的申请好友列表信息，传入指向为空的shared\_ptr对象函数执行后会自动赋值。
* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小

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

申请添加好友

**Parameters**:

* **rosterId** 申请添加的用户id
* **message** 好友申请信息

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

删除好友

**Parameters**:

* **rosterId** 删除的好友id

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

接受加好友申请

**Parameters**:

* **rosterId** 申请加为好友的用户id

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

拒绝加好友申请

**Parameters**:

* **rosterId** 申请加为好友的用户id
* **reason** 拒绝的原因

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

加入黑名单

**Parameters**:

* **rosterId** 加入黑名单的用户id

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

从黑名单移除

**Parameters**:

* **rosterId** 从黑名单移除的用户id

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

获取黑名单，如果forceRefresh == true，则强制从服务端拉取

**Parameters**:

* **list** 好友id列表，传入空列表函数返回后从此处获取返回的黑名单id列表
* **forceRefresh** 是否从服务器读取数据，true为强制从服务器获取，false情况下本地读取列表为空的情况下会自动从服务器读取

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

下载头像

**Parameters**:

* **item** 用户信息
* **thumbnail** 是否下载缩略图，ture为缩略图，false为原图
* **listener** 下载回调函数

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

添加好友变化监听者

**Parameters**:

* **listener** 好友变化监听者

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

移除好友变化监听者

**Parameters**:

* **listener** 好友变化监听者

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
