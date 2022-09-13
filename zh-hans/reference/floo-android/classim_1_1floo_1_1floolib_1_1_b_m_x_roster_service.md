---
title: im::floo::floolib::BMXRosterService
summary: 好友Service 

---

# im::floo::floolib::BMXRosterService



好友Service 

## Public Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Application](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_1_1_application.md)** <br>好友邀请  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-delete)**() |
| [BMXErrorCode] | **[get](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-get)**(ListOfLongLong list, boolean forceRefresh)<br>获取好友列表，如果forceRefresh == true，则强制从服务端拉取  |
| [BMXErrorCode] | **[fetchRosterById](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-fetchrosterbyid)**(long rosterId, boolean forceRefresh, [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item)<br>搜索用户  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-search)**(long rosterId, boolean forceRefresh, [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item)<br>搜索用户  |
| [BMXErrorCode] | **[fetchRosterByName](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-fetchrosterbyname)**(String name, boolean forceRefresh, [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item)<br>搜索用户  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-search)**(String name, boolean forceRefresh, [BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item)<br>搜索用户  |
| [BMXErrorCode] | **[fetchRostersByIdList](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-fetchrostersbyidlist)**(ListOfLongLong rosterIdList, BMXRosterItemList list, boolean forceRefresh)<br>批量搜索用户  |
| [BMXErrorCode] | **[search](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-search)**(ListOfLongLong rosterIdList, BMXRosterItemList list, boolean forceRefresh)<br>批量搜索用户  |
| [BMXErrorCode] | **[setItemLocalExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemlocalextension)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, String extension)<br>更新好友本地扩展信息  |
| [BMXErrorCode] | **[setItemExtension](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemextension)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, String extension)<br>更新好友服务器扩展信息  |
| [BMXErrorCode] | **[setItemAlias](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemalias)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, String alias)<br>更新好友别名  |
| [BMXErrorCode] | **[setItemMuteNotification](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-setitemmutenotification)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, boolean status)<br>设置是否拒收用户消息  |
| [BMXErrorCode] | **[getApplicationList](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-getapplicationlist)**(ApplicationPage result, String cursor, int pageSize)<br>获取申请添加好友列表  |
| [BMXErrorCode] | **[apply](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-apply)**(long rosterId, String message, String authAnswer) |
| [BMXErrorCode] | **[apply](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-apply)**(long rosterId, String message)<br>申请添加好友  |
| [BMXErrorCode] | **[remove](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-remove)**(long rosterId)<br>删除好友  |
| [BMXErrorCode] | **[accept](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-accept)**(long rosterId)<br>接受加好友申请  |
| [BMXErrorCode] | **[decline](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-decline)**(long rosterId, String reason)<br>拒绝加好友申请  |
| [BMXErrorCode] | **[block](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-block)**(long rosterId)<br>加入黑名单  |
| [BMXErrorCode] | **[unblock](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-unblock)**(long rosterId)<br>从黑名单移除  |
| [BMXErrorCode] | **[getBlockList](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-getblocklist)**(ListOfLongLong list, boolean forceRefresh)<br>获取黑名单，如果forceRefresh == true，则强制从服务端拉取  |
| [BMXErrorCode] | **[downloadAvatar](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-downloadavatar)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item, boolean thumbnail, FileProgressListener listener)<br>下载头像  |
| void | **[addRosterListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-addrosterlistener)**([BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md) listener)<br>添加好友变化监听者  |
| void | **[removeRosterListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md#function-removerosterlistener)**([BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md) listener)<br>移除好友变化监听者  |

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


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="delete" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="get" %}{% endlanying_code_snippet %}
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
  * **item** 查询返回的用户的信息，传入指向为空的shared_ptr对象函数执行后会自动赋值。 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="fetchRosterById" %}{% endlanying_code_snippet %}
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
  * **item** 查询返回的用户的信息，传入指向为空的shared_ptr对象函数执行后会自动赋值。 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="search" %}{% endlanying_code_snippet %}
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
  * **item** 查询返回的用户的信息，传入指向为空的shared_ptr对象函数执行后会自动赋值。 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="fetchRosterByName" %}{% endlanying_code_snippet %}
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
  * **item** 查询返回的用户的信息，传入指向为空的shared_ptr对象函数执行后会自动赋值。 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="search" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="fetchRostersByIdList" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="search" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="setItemLocalExtension" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="setItemExtension" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="setItemAlias" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="setItemMuteNotification" %}{% endlanying_code_snippet %}
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

  * **result** 返回的申请好友列表信息，传入指向为空的shared_ptr对象函数执行后会自动赋值。 
  * **cursor** 分页获取的起始cursor，第一次传入为空，后续传入上次操作返回的result中的cursor 
  * **pageSize** 分页大小 


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="getApplicationList" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="apply" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="apply" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="remove" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="accept" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="decline" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="block" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="unblock" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="getBlockList" %}{% endlanying_code_snippet %}
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


**Return**: [BMXErrorCode]

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="downloadAvatar" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="addRosterListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="removeRosterListener" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="BMXRosterService" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="finalize" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterService",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800