---
title: floo::BMXRosterServiceListener
summary: 好友变化监听者 

---

# floo::BMXRosterServiceListener



好友变化监听者 


`#include <bmx_roster_service_listener.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterServiceListener](classfloo_1_1_b_m_x_roster_service_listener.md#function-bmxrosterservicelistener)**()<br>构造函数  |
| virtual | **[~BMXRosterServiceListener](classfloo_1_1_b_m_x_roster_service_listener.md#function-~bmxrosterservicelistener)**()<br>析构函数  |
| virtual void | **[onFriendAdded](classfloo_1_1_b_m_x_roster_service_listener.md#function-onfriendadded)**(int64_t sponsorId, int64_t recipientId)<br>添加好友  |
| virtual void | **[onFriendRemoved](classfloo_1_1_b_m_x_roster_service_listener.md#function-onfriendremoved)**(int64_t sponsorId, int64_t recipientId)<br>删除好友  |
| virtual void | **[onApplied](classfloo_1_1_b_m_x_roster_service_listener.md#function-onapplied)**(int64_t sponsorId, int64_t recipientId, const std::string & message)<br>收到加好友申请  |
| virtual void | **[onApplicationAccepted](classfloo_1_1_b_m_x_roster_service_listener.md#function-onapplicationaccepted)**(int64_t sponsorId, int64_t recipientId)<br>加好友申请被通过了  |
| virtual void | **[onApplicationDeclined](classfloo_1_1_b_m_x_roster_service_listener.md#function-onapplicationdeclined)**(int64_t sponsorId, int64_t recipientId, const std::string & reason)<br>加好友申请被拒绝了  |
| virtual void | **[onBlockListAdded](classfloo_1_1_b_m_x_roster_service_listener.md#function-onblocklistadded)**(int64_t sponsorId, int64_t recipientId)<br>添加黑名单  |
| virtual void | **[onBlockListRemoved](classfloo_1_1_b_m_x_roster_service_listener.md#function-onblocklistremoved)**(int64_t sponsorId, int64_t recipientId)<br>删除黑名单  |
| virtual void | **[onRosterInfoUpdate](classfloo_1_1_b_m_x_roster_service_listener.md#function-onrosterinfoupdate)**(BMXRosterItemPtr item)<br>用户信息更新  |
| virtual void | **[onRosterListUpdate](classfloo_1_1_b_m_x_roster_service_listener.md#function-onrosterlistupdate)**()<br>客户端从服务器拉取到新联系人时触发，用于用户联系人列表更新，从SDK调用本地获取联系人即可取得全部成员信息  |
| void | **[registerRosterService](classfloo_1_1_b_m_x_roster_service_listener.md#function-registerrosterservice)**([BMXRosterService](classfloo_1_1_b_m_x_roster_service.md) * service)<br>注册BMXRosterServiceListener绑定到的BMXRosterService（SDK内部自动注册）  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md) * | **[mService](classfloo_1_1_b_m_x_roster_service_listener.md#variable-mservice)**  |

## Public Functions Documentation

### function BMXRosterServiceListener

```cpp
inline BMXRosterServiceListener()
```

构造函数 

### function ~BMXRosterServiceListener

```cpp
inline virtual ~BMXRosterServiceListener()
```

析构函数 

### function onFriendAdded

```cpp
inline virtual void onFriendAdded(
    int64_t sponsorId,
    int64_t recipientId
)
```

添加好友 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 


### function onFriendRemoved

```cpp
inline virtual void onFriendRemoved(
    int64_t sponsorId,
    int64_t recipientId
)
```

删除好友 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 


### function onApplied

```cpp
inline virtual void onApplied(
    int64_t sponsorId,
    int64_t recipientId,
    const std::string & message
)
```

收到加好友申请 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 
  * **message** 好友申请消息 


### function onApplicationAccepted

```cpp
inline virtual void onApplicationAccepted(
    int64_t sponsorId,
    int64_t recipientId
)
```

加好友申请被通过了 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 


### function onApplicationDeclined

```cpp
inline virtual void onApplicationDeclined(
    int64_t sponsorId,
    int64_t recipientId,
    const std::string & reason
)
```

加好友申请被拒绝了 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 
  * **reason** 申请拒绝原因 


### function onBlockListAdded

```cpp
inline virtual void onBlockListAdded(
    int64_t sponsorId,
    int64_t recipientId
)
```

添加黑名单 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 


### function onBlockListRemoved

```cpp
inline virtual void onBlockListRemoved(
    int64_t sponsorId,
    int64_t recipientId
)
```

删除黑名单 

**Parameters**: 

  * **sponsorId** 操作的发起者 
  * **recipientId** 操作的接受者 


### function onRosterInfoUpdate

```cpp
inline virtual void onRosterInfoUpdate(
    BMXRosterItemPtr item
)
```

用户信息更新 

**Parameters**: 

  * **item** 更新的好友信息 


### function onRosterListUpdate

```cpp
inline virtual void onRosterListUpdate()
```

客户端从服务器拉取到新联系人时触发，用于用户联系人列表更新，从SDK调用本地获取联系人即可取得全部成员信息 

### function registerRosterService

```cpp
inline void registerRosterService(
    BMXRosterService * service
)
```

注册BMXRosterServiceListener绑定到的BMXRosterService（SDK内部自动注册） 

**Parameters**: 

  * **service** [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md)


## Protected Attributes Documentation

### variable mService

```cpp
BMXRosterService * mService;
```


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800