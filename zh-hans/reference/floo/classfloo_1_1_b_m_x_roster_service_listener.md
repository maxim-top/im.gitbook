---
title: floo::BMXRosterServiceListener
summary: 好友变化监听者
---

# floo::BMXRosterServiceListener

好友变化监听者

`#include <bmx_roster_service_listener.h>`

## Public Functions

|              | Name                                                                                                                                                                                                                                                                                   |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-bmxrosterservicelistener"><strong>BMXRosterServiceListener</strong></a>()<br>构造函数</p>                                                                                                                              |
| virtual      | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-~bmxrosterservicelistener"><strong>~BMXRosterServiceListener</strong></a>()<br>析构函数</p>                                                                                                                            |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onfriendadded"><strong>onFriendAdded</strong></a>(int64_t sponsorId, int64_t recipientId)<br>添加好友</p>                                                                                                              |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onfriendremoved"><strong>onFriendRemoved</strong></a>(int64_t sponsorId, int64_t recipientId)<br>删除好友</p>                                                                                                          |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onapplied"><strong>onApplied</strong></a>(int64_t sponsorId, int64_t recipientId, const std::string &#x26; message)<br>收到加好友申请</p>                                                                                 |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onapplicationaccepted"><strong>onApplicationAccepted</strong></a>(int64_t sponsorId, int64_t recipientId)<br>加好友申请被通过了</p>                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onapplicationdeclined"><strong>onApplicationDeclined</strong></a>(int64_t sponsorId, int64_t recipientId, const std::string &#x26; reason)<br>加好友申请被拒绝了</p>                                                        |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onblocklistadded"><strong>onBlockListAdded</strong></a>(int64_t sponsorId, int64_t recipientId)<br>添加黑名单</p>                                                                                                       |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onblocklistremoved"><strong>onBlockListRemoved</strong></a>(int64_t sponsorId, int64_t recipientId)<br>删除黑名单</p>                                                                                                   |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onrosterinfoupdate"><strong>onRosterInfoUpdate</strong></a>(BMXRosterItemPtr item)<br>用户信息更新</p>                                                                                                                   |
| virtual void | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-onrosterlistupdate"><strong>onRosterListUpdate</strong></a>()<br>客户端从服务器拉取到新联系人时触发，用于用户联系人列表更新，从SDK调用本地获取联系人即可取得全部成员信息</p>                                                                                         |
| void         | <p><a href="classfloo_1_1_b_m_x_roster_service_listener.md#function-registerrosterservice"><strong>registerRosterService</strong></a>(<a href="classfloo_1_1_b_m_x_roster_service.md">BMXRosterService</a> * service)<br>注册BMXRosterServiceListener绑定到的BMXRosterService（SDK内部自动注册）</p> |

## Protected Attributes

|                                                              | Name                                                                             |
| ------------------------------------------------------------ | -------------------------------------------------------------------------------- |
| [BMXRosterService](classfloo_1_1_b_m_x_roster_service.md) \* | [**mService**](classfloo_1_1_b_m_x_roster_service_listener.md#variable-mservice) |

## Public Functions Documentation

### function BMXRosterServiceListener

```cpp
inline BMXRosterServiceListener()
```

构造函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function \~BMXRosterServiceListener

```cpp
inline virtual ~BMXRosterServiceListener()
```

析构函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function onRosterInfoUpdate

```cpp
inline virtual void onRosterInfoUpdate(
    BMXRosterItemPtr item
)
```

用户信息更新

**Parameters**:

* **item** 更新的好友信息

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

### function onRosterListUpdate

```cpp
inline virtual void onRosterListUpdate()
```

客户端从服务器拉取到新联系人时触发，用于用户联系人列表更新，从SDK调用本地获取联系人即可取得全部成员信息

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>

```

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

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXRosterServiceListener'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
