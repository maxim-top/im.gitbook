---
title: im::floo::floolib::BMXRosterManager
summary: 好友管理器
---

# im::floo::floolib::BMXRosterManager

好友管理器

## Public Functions

|      | Name                                                                                                                                                                                                                                                                                                              |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXRosterManager**](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-bmxrostermanager)([BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md) service)                                                                                                                      |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-get"><strong>get</strong></a>(final boolean forceRefresh, final BMXDataCallBack&#x3C; ListOfLongLong > callBack)<br>获取好友列表，如果forceRefresh == true，则强制从服务端拉取</p>                                                                       |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-search"><strong>search</strong></a>(final long rosterId, final boolean forceRefresh, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> > callBack)<br>搜索用户</p>              |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-search"><strong>search</strong></a>(final String name, final boolean forceRefresh, final BMXDataCallBack&#x3C; <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> > callBack)<br>搜索用户</p>                |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-search"><strong>search</strong></a>(final ListOfLongLong rosterIdList, final boolean forceRefresh, final BMXDataCallBack&#x3C; BMXRosterItemList > callBack)<br>批量搜索用户</p>                                                            |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-setitemextension"><strong>setItemExtension</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, final String extension, final BMXCallBack callBack)<br>更新好友本地扩展信息</p>             |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-setitemalias"><strong>setItemAlias</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, final String alias, final BMXCallBack callBack)<br>更新好友别名</p>                             |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-setitemmutenotification"><strong>setItemMuteNotification</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, final boolean status, final BMXCallBack callBack)<br>设置是否拒收用户消息</p> |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-apply"><strong>apply</strong></a>(final long rosterId, final String message, final BMXCallBack callBack)<br>申请添加好友</p>                                                                                                                |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-remove"><strong>remove</strong></a>(final long rosterId, final BMXCallBack callBack)<br>删除好友</p>                                                                                                                                      |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-getapplicationlist"><strong>getApplicationList</strong></a>(final String cursor, final int pageSize, final BMXDataCallBack&#x3C; ApplicationPage > callBack)<br>获取申请添加好友列表</p>                                                        |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-accept"><strong>accept</strong></a>(final long rosterId, final BMXCallBack callBack)<br>接受加好友申请</p>                                                                                                                                   |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-decline"><strong>decline</strong></a>(final long rosterId, final String reason, final BMXCallBack callBack)<br>拒绝加好友申请</p>                                                                                                            |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-block"><strong>block</strong></a>(final long rosterId, final BMXCallBack callBack)<br>加入黑名单</p>                                                                                                                                       |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-unblock"><strong>unblock</strong></a>(final long rosterId, final BMXCallBack callBack)<br>从黑名单移除</p>                                                                                                                                  |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-getblocklist"><strong>getBlockList</strong></a>(final boolean forceRefresh, final BMXDataCallBack&#x3C; ListOfLongLong > callBack)<br>获取黑名单，如果forceRefresh == true，则强制从服务端拉取</p>                                                      |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-downloadavatar"><strong>downloadAvatar</strong></a>(final <a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md">BMXRosterItem</a> item, final FileProgressListener listener, final BMXCallBack callBack)<br>下载头像</p>          |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-addrosterlistener"><strong>addRosterListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md">BMXRosterServiceListener</a> listener)<br>添加好友变化监听者</p>                                           |
| void | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_manager.md#function-removerosterlistener"><strong>removeRosterListener</strong></a>(<a href="classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md">BMXRosterServiceListener</a> listener)<br>移除好友变化监听者</p>                                     |

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

获取好友列表，如果forceRefresh == true，则强制从服务端拉取

**Parameters**:

* **forceRefresh** 是否从服务器读取数据，true为强制从服务器获取，false情况下本地读取列表为空的情况下会自动从服务器读取
* **callBack** \[BMXErrorCode] 好友id列表

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

搜索用户

**Parameters**:

* **rosterId** 搜索的好友id
* **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。
* **callBack** \[BMXErrorCode] 查询返回的用户的信息

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

搜索用户

**Parameters**:

* **name** 搜索的用户名
* **forceRefresh** 为true强制从服务器获取，为false情况下查询结果为空时自动从服务器获取。
* **callBack** \[BMXErrorCode] 查询返回的用户的信息

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

批量搜索用户

**Parameters**:

* **rosterIdList** 需要搜索的用户id列表
* **forceRefresh** 是否强制从服务器获取，为true则强制从服务器获取
* **callBack** \[BMXErrorCode] 返回的好友信息列表

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

更新好友本地扩展信息

**Parameters**:

* **item** 用户信息
* **extension** 本地扩展信息
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

更新好友别名

**Parameters**:

* **item** 用户信息
* **alias** 好友别名
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

设置是否拒收用户消息

**Parameters**:

* **item** 用户信息
* **status** 是否拒收用户消息，true拒收，false不拒收
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

申请添加好友

**Parameters**:

* **rosterId** 申请添加的用户id
* **message** 好友申请信息
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

删除好友

**Parameters**:

* **rosterId** 删除的好友id
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

获取申请添加好友列表

**Parameters**:

* **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor
* **pageSize** 分页大小
* **callBack** \[BMXErrorCode] 返回的申请好友列表信息

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

接受加好友申请

**Parameters**:

* **rosterId** 申请加为好友的用户id
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

拒绝加好友申请

**Parameters**:

* **rosterId** 申请加为好友的用户id
* **reason** 拒绝的原因
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

加入黑名单

**Parameters**:

* **rosterId** 加入黑名单的用户id
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

从黑名单移除

**Parameters**:

* **rosterId** 从黑名单移除的用户id
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

获取黑名单，如果forceRefresh == true，则强制从服务端拉取

**Parameters**:

* **forceRefresh** 是否从服务器读取数据，true为强制从服务器获取，false情况下本地读取列表为空的情况下会自动从服务器读取
* **callBack** \[BMXErrorCode] 好友id列表

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

下载头像

**Parameters**:

* **item** 用户信息
* **listener** 下载回调函数
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

添加好友变化监听者

**Parameters**:

* **listener** 好友变化监听者

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

移除好友变化监听者

**Parameters**:

* **listener** 好友变化监听者

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXRosterManager'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
