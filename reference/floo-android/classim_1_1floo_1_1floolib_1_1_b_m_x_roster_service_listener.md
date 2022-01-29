---
title: im::floo::floolib::BMXRosterServiceListener
summary: 好友变化监听者 

---

# im::floo::floolib::BMXRosterServiceListener



好友变化监听者 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-delete)**() |
| void | **[swigReleaseOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-swigreleaseownership)**() |
| void | **[swigTakeOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-swigtakeownership)**() |
| void | **[onFriendAdded](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onfriendadded)**(long sponsorId, long recipientId)<br>添加好友  |
| void | **[onFriendRemoved](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onfriendremoved)**(long sponsorId, long recipientId)<br>删除好友  |
| void | **[onApplied](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onapplied)**(long sponsorId, long recipientId, String message)<br>收到加好友申请  |
| void | **[onApplicationAccepted](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onapplicationaccepted)**(long sponsorId, long recipientId)<br>加好友申请被通过了  |
| void | **[onApplicationDeclined](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onapplicationdeclined)**(long sponsorId, long recipientId, String reason)<br>加好友申请被拒绝了  |
| void | **[onBlockListAdded](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onblocklistadded)**(long sponsorId, long recipientId)<br>添加黑名单  |
| void | **[onBlockListRemoved](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onblocklistremoved)**(long sponsorId, long recipientId)<br>删除黑名单  |
| void | **[onRosterInfoUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onrosterinfoupdate)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item)<br>用户信息更新  |
| void | **[onRosterListUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onrosterlistupdate)**()<br>客户端从服务器拉取到新联系人时触发，用于用户联系人列表更新，从SDK调用本地获取联系人即可取得全部成员信息  |
| | **[BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-bmxrosterservicelistener)**() |
| void | **[registerRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-registerrosterservice)**([BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md) service) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-bmxrosterservicelistener)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-finalize)**() |
| void | **[swigDirectorDisconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-swigdirectordisconnect)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-getcptr)**([BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#variable-swigcmemown)**  |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```


### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```


### function onFriendAdded

```java
inline void onFriendAdded(
    long sponsorId,
    long recipientId
)
```

添加好友 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 


### function onFriendRemoved

```java
inline void onFriendRemoved(
    long sponsorId,
    long recipientId
)
```

删除好友 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 


### function onApplied

```java
inline void onApplied(
    long sponsorId,
    long recipientId,
    String message
)
```

收到加好友申请 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 
  * **message** 好友申请消息 


### function onApplicationAccepted

```java
inline void onApplicationAccepted(
    long sponsorId,
    long recipientId
)
```

加好友申请被通过了 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 


### function onApplicationDeclined

```java
inline void onApplicationDeclined(
    long sponsorId,
    long recipientId,
    String reason
)
```

加好友申请被拒绝了 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 
  * **reason** 申请拒绝原因 


### function onBlockListAdded

```java
inline void onBlockListAdded(
    long sponsorId,
    long recipientId
)
```

添加黑名单 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 


### function onBlockListRemoved

```java
inline void onBlockListRemoved(
    long sponsorId,
    long recipientId
)
```

删除黑名单 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 


### function onRosterInfoUpdate

```java
inline void onRosterInfoUpdate(
    BMXRosterItem item
)
```

用户信息更新 

**Parameters**: 

  * **item** 更新的好友信息 


### function onRosterListUpdate

```java
inline void onRosterListUpdate()
```

客户端从服务器拉取到新联系人时触发，用于用户联系人列表更新，从SDK调用本地获取联系人即可取得全部成员信息 

### function BMXRosterServiceListener

```java
inline BMXRosterServiceListener()
```


### function registerRosterService

```java
inline void registerRosterService(
    BMXRosterService service
)
```


## Protected Functions Documentation

### function BMXRosterServiceListener

```java
inline BMXRosterServiceListener(
    long cPtr,
    boolean cMemoryOwn
)
```


### function finalize

```java
inline void finalize()
```


### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```


### function getCPtr

```java
static inline long getCPtr(
    BMXRosterServiceListener obj
)
```


## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```


-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800