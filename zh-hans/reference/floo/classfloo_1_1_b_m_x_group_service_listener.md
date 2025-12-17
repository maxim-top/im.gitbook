---
title: floo::BMXGroupServiceListener
summary: 群组变化监听者
---

# floo::BMXGroupServiceListener

群组变化监听者

`#include <bmx_group_service_listener.h>`

## Public Functions

|              | Name                                                                                                                                                                                                                                                                            |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|              | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-bmxgroupservicelistener"><strong>BMXGroupServiceListener</strong></a>()<br>构造函数</p>                                                                                                                          |
| virtual      | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-~bmxgroupservicelistener"><strong>~BMXGroupServiceListener</strong></a>()<br>析构函数</p>                                                                                                                        |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-ongroupcreate"><strong>onGroupCreate</strong></a>(BMXGroupPtr group)<br>多设备同步创建群组</p>                                                                                                                        |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate"><strong>onGroupListUpdate</strong></a>(const BMXGroupList &#x26; list)<br>群列表更新了</p>                                                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-ongroupjoined"><strong>onGroupJoined</strong></a>(BMXGroupPtr group)<br>加入了某群</p>                                                                                                                            |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-ongroupleft"><strong>onGroupLeft</strong></a>(BMXGroupPtr group, const std::string &#x26; reason)<br>退出了某群</p>                                                                                               |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-oninvitated"><strong>onInvitated</strong></a>(int64_t groupId, int64_t inviter, const std::string &#x26; message)<br>收到入群邀请</p>                                                                              |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-oninvitationaccepted"><strong>onInvitationAccepted</strong></a>(BMXGroupPtr group, int64_t inviteeId)<br>入群邀请被接受</p>                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-oninvitationdeclined"><strong>onInvitationDeclined</strong></a>(BMXGroupPtr group, int64_t inviteeId, const std::string &#x26; reason)<br>入群申请被拒绝</p>                                                        |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onapplied"><strong>onApplied</strong></a>(BMXGroupPtr group, int64_t applicantId, const std::string &#x26; message)<br>收到入群申请</p>                                                                            |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onapplicationaccepted"><strong>onApplicationAccepted</strong></a>(BMXGroupPtr group, int64_t approver)<br>入群申请被接受</p>                                                                                        |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onapplicationdeclined"><strong>onApplicationDeclined</strong></a>(BMXGroupPtr group, int64_t approver, const std::string &#x26; reason)<br>入群申请被拒绝</p>                                                       |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onmembersbanned"><strong>onMembersBanned</strong></a>(BMXGroupPtr group, const std::vector&#x3C; int64_t > &#x26; members, int64_t duration)<br>群成员被禁言</p>                                                   |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onmembersunbanned"><strong>onMembersUnbanned</strong></a>(BMXGroupPtr group, const std::vector&#x3C; int64_t > &#x26; members)<br>群成员被解除禁言</p>                                                               |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onmemberjoined"><strong>onMemberJoined</strong></a>(BMXGroupPtr group, int64_t memberId, int64_t inviter)<br>加入新成员</p>                                                                                       |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onmemberleft"><strong>onMemberLeft</strong></a>(BMXGroupPtr group, int64_t memberId, const std::string &#x26; reason)<br>群成员退出</p>                                                                           |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onadminsadded"><strong>onAdminsAdded</strong></a>(BMXGroupPtr group, const std::vector&#x3C; int64_t > &#x26; members)<br>添加了新管理员</p>                                                                        |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onadminsremoved"><strong>onAdminsRemoved</strong></a>(BMXGroupPtr group, const std::vector&#x3C; int64_t > &#x26; members, const std::string &#x26; reason)<br>移除了管理员</p>                                    |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onownerassigned"><strong>onOwnerAssigned</strong></a>(BMXGroupPtr group)<br>成为群主</p>                                                                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-ongroupinfoupdate"><strong>onGroupInfoUpdate</strong></a>(BMXGroupPtr group, <a href="classfloo_1_1_b_m_x_group.md#enum-updateinfotype">BMXGroup::UpdateInfoType</a> type)<br>群组信息变更</p>                     |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onmemberchangenickname"><strong>onMemberChangeNickName</strong></a>(BMXGroupPtr group, int64_t memberId, const std::string &#x26; nickName)<br>群成员更改群内昵称</p>                                                 |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onannouncementupdate"><strong>onAnnouncementUpdate</strong></a>(BMXGroupPtr group, BMXGroup::AnnouncementPtr announcement)<br>收到群公告</p>                                                                      |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onsharedfileuploaded"><strong>onSharedFileUploaded</strong></a>(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile)<br>收到共享文件</p>                                                                         |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onsharedfiledeleted"><strong>onSharedFileDeleted</strong></a>(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile)<br>删除了共享文件</p>                                                                          |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onsharedfileupdated"><strong>onSharedFileUpdated</strong></a>(BMXGroupPtr group, BMXGroup::SharedFilePtr sharedFile)<br>共享文件更新文件名</p>                                                                        |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onblocklistadded"><strong>onBlockListAdded</strong></a>(BMXGroupPtr group, const std::vector&#x3C; int64_t > &#x26; members)<br>添加黑名单</p>                                                                    |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-onblocklistremoved"><strong>onBlockListRemoved</strong></a>(BMXGroupPtr group, const std::vector&#x3C; int64_t > &#x26; members)<br>删除黑名单</p>                                                                |
| virtual void | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-ongrouplistupdate"><strong>onGroupListUpdate</strong></a>()<br>客户端从服务器拉取到新群组时触发，用于用户群组列表更新，从SDK调用本地获取群组即可取得全部成员信息</p>                                                                                        |
| void         | <p><a href="classfloo_1_1_b_m_x_group_service_listener.md#function-registergroupservice"><strong>registerGroupService</strong></a>(<a href="classfloo_1_1_b_m_x_group_service.md">BMXGroupService</a> * service)<br>注册BMXGroupServiceListener绑定到的BMXGroupService（SDK内部自动注册）</p> |

## Protected Attributes

|                                                            | Name                                                                            |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [BMXGroupService](classfloo_1_1_b_m_x_group_service.md) \* | [**mService**](classfloo_1_1_b_m_x_group_service_listener.md#variable-mservice) |

## Public Functions Documentation

### function BMXGroupServiceListener

```cpp
inline BMXGroupServiceListener()
```

构造函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function \~BMXGroupServiceListener

```cpp
inline virtual ~BMXGroupServiceListener()
```

析构函数

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onGroupCreate

```cpp
inline virtual void onGroupCreate(
    BMXGroupPtr group
)
```

多设备同步创建群组

**Parameters**:

* **group** 新创建的群组

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onGroupListUpdate

```cpp
inline virtual void onGroupListUpdate(
    const BMXGroupList & list
)
```

群列表更新了

**Parameters**:

* **list** 更新的群组列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onGroupJoined

```cpp
inline virtual void onGroupJoined(
    BMXGroupPtr group
)
```

加入了某群

**Parameters**:

* **group** 加入的群组

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onGroupLeft

```cpp
inline virtual void onGroupLeft(
    BMXGroupPtr group,
    const std::string & reason
)
```

退出了某群

**Parameters**:

* **group** 退出的群组
* **reason** 退出原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onInvitated

```cpp
inline virtual void onInvitated(
    int64_t groupId,
    int64_t inviter,
    const std::string & message
)
```

收到入群邀请

**Parameters**:

* **groupId** 邀请进入的群组id
* **inviter** 邀请者id
* **message** 邀请原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onInvitationAccepted

```cpp
inline virtual void onInvitationAccepted(
    BMXGroupPtr group,
    int64_t inviteeId
)
```

入群邀请被接受

**Parameters**:

* **group** 邀请被同意的群组
* **inviteeId** 被邀请者id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onInvitationDeclined

```cpp
inline virtual void onInvitationDeclined(
    BMXGroupPtr group,
    int64_t inviteeId,
    const std::string & reason
)
```

入群申请被拒绝

**Parameters**:

* **group** 邀请被拒绝的群组
* **inviteeId** 被邀请者id
* **reason** 拒绝原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onApplied

```cpp
inline virtual void onApplied(
    BMXGroupPtr group,
    int64_t applicantId,
    const std::string & message
)
```

收到入群申请

**Parameters**:

* **group** 收到入群申请的群组
* **applicantId** 申请者id
* **message** 申请原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onApplicationAccepted

```cpp
inline virtual void onApplicationAccepted(
    BMXGroupPtr group,
    int64_t approver
)
```

入群申请被接受

**Parameters**:

* **group** 入群申请被接受的群组
* **approver** 申请的批准者

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onApplicationDeclined

```cpp
inline virtual void onApplicationDeclined(
    BMXGroupPtr group,
    int64_t approver,
    const std::string & reason
)
```

入群申请被拒绝

**Parameters**:

* **group** 入群申请被拒绝的群组
* **approver** 申请的批准者
* **reason** 拒绝的原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onMembersBanned

```cpp
inline virtual void onMembersBanned(
    BMXGroupPtr group,
    const std::vector< int64_t > & members,
    int64_t duration
)
```

群成员被禁言

**Parameters**:

* **group** 群成员被禁言的群组
* **members** 被禁言的群成员id列表
* **duration** 禁言时长

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onMembersUnbanned

```cpp
inline virtual void onMembersUnbanned(
    BMXGroupPtr group,
    const std::vector< int64_t > & members
)
```

群成员被解除禁言

**Parameters**:

* **group** 群成员被解除禁言的群组
* **members** 被解除禁言的群成员id列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onMemberJoined

```cpp
inline virtual void onMemberJoined(
    BMXGroupPtr group,
    int64_t memberId,
    int64_t inviter
)
```

加入新成员

**Parameters**:

* **group** 有成员加入的群组
* **memberId** 加入成员的id
* **inviter** 邀请者id

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onMemberLeft

```cpp
inline virtual void onMemberLeft(
    BMXGroupPtr group,
    int64_t memberId,
    const std::string & reason
)
```

群成员退出

**Parameters**:

* **group** 有成员退出的群组
* **memberId** 退出的群成员id
* **reason** 退出的原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onAdminsAdded

```cpp
inline virtual void onAdminsAdded(
    BMXGroupPtr group,
    const std::vector< int64_t > & members
)
```

添加了新管理员

**Parameters**:

* **group** 发生添加新管理员的群组
* **members** 被提升为管理员的成员列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onAdminsRemoved

```cpp
inline virtual void onAdminsRemoved(
    BMXGroupPtr group,
    const std::vector< int64_t > & members,
    const std::string & reason
)
```

移除了管理员

**Parameters**:

* **group** 发生移除管理员的群组
* **members** 被移除了管理员的成员列表
* **reason** 被移除的原因

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onOwnerAssigned

```cpp
inline virtual void onOwnerAssigned(
    BMXGroupPtr group
)
```

成为群主

**Parameters**:

* **group** 被转让为群主的群组

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onGroupInfoUpdate

```cpp
inline virtual void onGroupInfoUpdate(
    BMXGroupPtr group,
    BMXGroup::UpdateInfoType type
)
```

群组信息变更

**Parameters**:

* **group** 群信息发生变更的群组
* **type** 发生变更的群信息类型

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onMemberChangeNickName

```cpp
inline virtual void onMemberChangeNickName(
    BMXGroupPtr group,
    int64_t memberId,
    const std::string & nickName
)
```

群成员更改群内昵称

**Parameters**:

* **group** 发生群成员变更群昵称的群组
* **memberId** 变更群昵称的群成员id
* **nickName** 变更后的群昵称

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onAnnouncementUpdate

```cpp
inline virtual void onAnnouncementUpdate(
    BMXGroupPtr group,
    BMXGroup::AnnouncementPtr announcement
)
```

收到群公告

**Parameters**:

* **group** 发生群公告更新的群组
* **announcement** 变更后的最新的群更高

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onSharedFileUploaded

```cpp
inline virtual void onSharedFileUploaded(
    BMXGroupPtr group,
    BMXGroup::SharedFilePtr sharedFile
)
```

收到共享文件

**Parameters**:

* **group** 发生群共享文件上传的群组
* **sharedFile** 新上传的群共享文件

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onSharedFileDeleted

```cpp
inline virtual void onSharedFileDeleted(
    BMXGroupPtr group,
    BMXGroup::SharedFilePtr sharedFile
)
```

删除了共享文件

**Parameters**:

* **group** 发生群共享文件删除的群组
* **sharedFile** 被删除的群共享文件

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onSharedFileUpdated

```cpp
inline virtual void onSharedFileUpdated(
    BMXGroupPtr group,
    BMXGroup::SharedFilePtr sharedFile
)
```

共享文件更新文件名

**Parameters**:

* **group** 发生群共享文件更新的群组
* **sharedFile** 更新的群共享文件

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onBlockListAdded

```cpp
inline virtual void onBlockListAdded(
    BMXGroupPtr group,
    const std::vector< int64_t > & members
)
```

添加黑名单

**Parameters**:

* **group** 添加黑名单的群组
* **members** 添加的黑名单成员列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onBlockListRemoved

```cpp
inline virtual void onBlockListRemoved(
    BMXGroupPtr group,
    const std::vector< int64_t > & members
)
```

删除黑名单

**Parameters**:

* **group** 删除黑名单的群组
* **members** 删除的黑名单成员列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function onGroupListUpdate

```cpp
inline virtual void onGroupListUpdate()
```

客户端从服务器拉取到新群组时触发，用于用户群组列表更新，从SDK调用本地获取群组即可取得全部成员信息

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>

```

### function registerGroupService

```cpp
inline void registerGroupService(
    BMXGroupService * service
)
```

注册BMXGroupServiceListener绑定到的BMXGroupService（SDK内部自动注册）

**Parameters**:

* **service** [BMXGroupService](classfloo_1_1_b_m_x_group_service.md)

## Protected Attributes Documentation

### variable mService

```cpp
BMXGroupService * mService;
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXGroupServiceListener'></div>
```

***

Updated on 2022-01-26 at 17:20:40 +0800
