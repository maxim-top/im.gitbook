# groupManage
## groupManage {#module_groupmanage}
群管理


* [groupManage](#module_groupmanage)
    * [.asyncGetGroupInfo(group_id, froce)](#module_groupmanage__asyncgetgroupinfo) ⇒ [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings)
    * [.asyncGetJoinedGroups(froce)](#module_groupmanage__asyncgetjoinedgroups) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code>
    * [.openGroup(group_id)](#module_groupmanage__opengroup)
    * [.getAllGroupDetail()](#module_groupmanage__getallgroupdetail) ⇒ <code>Object.&lt;number, module:types~GroupInfoAndSettings&gt;</code>
    * [.asyncGetGroupMembers(group_id)](#module_groupmanage__asyncgetgroupmembers) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code>
    * [.getGroupMembers(group_id)](#module_groupmanage__getgroupmembers) ⇒ [<code>Array.&lt;GroupMember&gt;</code>](types.md#module_types__groupmember)
    * [.asyncGetGroupListDetail(gids)](#module_groupmanage__asyncgetgrouplistdetail) ⇒ <code>Promise.&lt;Array.&lt;module:types~BriefGroupInfoAndSettings&gt;&gt;</code>
    * [.getGruopMessage(gid)](#module_groupmanage__getgruopmessage) ⇒ [<code>Array.&lt;Meta&gt;</code>](types.md#module_types__meta)
    * [.asyncGetInfo(params)](#module_groupmanage__asyncgetinfo) ⇒ [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings)
    * [.asyncGetMemberList(param)](#module_groupmanage__asyncgetmemberlist) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code>
    * [.readGroupMessage(group_id, mid)](#module_groupmanage__readgroupmessage)
    * [.recallMessage(uid, mid)](#module_groupmanage__recallmessage)
    * [.getUnreadCount(gid)](#module_groupmanage__getunreadcount) ⇒ <code>number</code>
    * [.asyncGetAdminList(params)](#module_groupmanage__asyncgetadminlist) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code>
    * [.asyncAdminAdd(params)](#module_groupmanage__asyncadminadd) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code>
    * [.asyncAdminRemove(params)](#module_groupmanage__asyncadminremove) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code>
    * [.asyncGetAnouncementById(params)](#module_groupmanage__asyncgetanouncementbyid) ⇒ [<code>Promise.&lt;GroupAnnouncement&gt;</code>](types.md#module_types__groupannouncement)
    * [.asyncAnouncementDelete(params)](#module_groupmanage__asyncanouncementdelete) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncAnnouncementEdit(params)](#module_groupmanage__asyncannouncementedit) ⇒ [<code>Promise.&lt;GroupAnnouncement&gt;</code>](types.md#module_types__groupannouncement)
    * [.asyncGetAnnouncementList(params)](#module_groupmanage__asyncgetannouncementlist) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupAnnouncement&gt;&gt;</code>
    * [.asyncCreate(params)](#module_groupmanage__asynccreate) ⇒ [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings)
    * [.asyncDestroy(params)](#module_groupmanage__asyncdestroy) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateAvatar(params)](#module_groupmanage__asyncupdateavatar) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateDescription(params)](#module_groupmanage__asyncupdatedescription) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateExt(params)](#module_groupmanage__asyncupdateext) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateName(params)](#module_groupmanage__asyncupdatename) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncGroupMsgMutemode(params)](#module_groupmanage__asyncgroupmsgmutemode) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncGroupBannedList(params)](#module_groupmanage__asyncgroupbannedlist) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMemberBanned&gt;&gt;</code>
    * [.asyncGroupBab(params)](#module_groupmanage__asyncgroupbab) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code>
    * [.asyncGroupUnban(params)](#module_groupmanage__asyncgroupunban) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code>
    * [.asyncGetSettings(group_id)](#module_groupmanage__asyncgetsettings) ⇒ [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings)
    * [.asyncUpdateAllowMemberInvitation(params)](#module_groupmanage__asyncupdateallowmemberinvitation) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateAllowMemberModify(params)](#module_groupmanage__asyncupdateallowmembermodify) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateEnableReadack(params)](#module_groupmanage__asyncupdateenablereadack) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateHistoryVisible(params)](#module_groupmanage__asyncupdatehistoryvisible) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateRequireadminapproval(params)](#module_groupmanage__asyncupdaterequireadminapproval) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncBanAll(params)](#module_groupmanage__asyncbanall) ⇒ [<code>Promise.&lt;GroupBanAllResponse&gt;</code>](types.md#module_types__groupbanallresponse)
    * [.asyncUnBanAll(params)](#module_groupmanage__asyncunbanall) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncOwnerTransfer(params)](#module_groupmanage__asyncownertransfer) ⇒ [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse)
    * [.asyncGetUserJoined(params)](#module_groupmanage__asyncgetuserjoined) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code>
    * [.asyncApply(params)](#module_groupmanage__asyncapply) ⇒ [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse)
    * [.asyncApplyHandle(params)](#module_groupmanage__asyncapplyhandle) ⇒ [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse)
    * [.asyncGroupBockedlist(params)](#module_groupmanage__asyncgroupbockedlist) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupBlockedListItem&gt;&gt;</code>
    * [.asyncGroupBlock(params)](#module_groupmanage__asyncgroupblock) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code>
    * [.asyncGroupUnblock(params)](#module_groupmanage__asyncgroupunblock) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code>
    * [.asyncKick(params)](#module_groupmanage__asynckick) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code>
    * [.asyncGetInvitationList()](#module_groupmanage__asyncgetinvitationlist) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupInvitation&gt;&gt;</code>
    * [.asyncInvite(params)](#module_groupmanage__asyncinvite) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code>
    * [.asyncInviteHandle(params)](#module_groupmanage__asyncinvitehandle) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncGetMemberDisplayName(params)](#module_groupmanage__asyncgetmemberdisplayname) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code>
    * [.asyncLeave(params)](#module_groupmanage__asyncleave) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateDisplayName(params)](#module_groupmanage__asyncupdatedisplayname) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asncGetApplicationList(params)](#module_groupmanage__asncgetapplicationlist) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupApplication&gt;&gt;</code>
    * [.asyncGetFileList(params)](#module_groupmanage__asyncgetfilelist) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupSharedFile&gt;&gt;</code>
    * [.asyncFileDelete(params)](#module_groupmanage__asyncfiledelete) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupSharedFileResponse&gt;&gt;</code>
    * [.asyncFileUpload(params)](#module_groupmanage__asyncfileupload) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupSharedFile&gt;&gt;</code>

### groupManage.asyncGetGroupInfo(group_id, froce) ⇒ [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) {#module_groupmanage__asyncgetgroupinfo}
获取群信息

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) - 群信息  

| Param | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | 群ID |
| froce | <code>boolean</code> | 是否强制从服务器拉取： true - 从服务器拉取， false - 优先从本地存储获取 |

### groupManage.asyncGetJoinedGroups(froce) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> {#module_groupmanage__asyncgetjoinedgroups}
获取加入的群组

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> - 群组ID列表  

| Param | Type | Description |
| --- | --- | --- |
| froce | <code>boolean</code> | 是否强制从服务器拉取： true - 从服务器拉取， false - 优先从本地存储获取 |

### groupManage.openGroup(group_id) {#module_groupmanage__opengroup}
打开群组， 此方法会准备群组聊天界面的一些必备信息。

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  

| Param | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | 群组ID |

### groupManage.getAllGroupDetail() ⇒ <code>Object.&lt;number, module:types~GroupInfoAndSettings&gt;</code> {#module_groupmanage__getallgroupdetail}
获取缓存的所有群组详情

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Object.&lt;number, module:types~GroupInfoAndSettings&gt;</code> - 群组详情  
### groupManage.asyncGetGroupMembers(group_id) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> {#module_groupmanage__asyncgetgroupmembers}
获取群组成员（异步）

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> - 群成员列表  

| Param | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | 群组ID |

### groupManage.getGroupMembers(group_id) ⇒ [<code>Array.&lt;GroupMember&gt;</code>](types.md#module_types__groupmember) {#module_groupmanage__getgroupmembers}
获取群组成员（同步）

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Array.&lt;GroupMember&gt;</code>](types.md#module_types__groupmember) - 群成员列表  

| Param | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | 群组ID |

### groupManage.asyncGetGroupListDetail(gids) ⇒ <code>Promise.&lt;Array.&lt;module:types~BriefGroupInfoAndSettings&gt;&gt;</code> {#module_groupmanage__asyncgetgrouplistdetail}
按id获取群组详情

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~BriefGroupInfoAndSettings&gt;&gt;</code> - 群组详情列表  

| Param | Type | Description |
| --- | --- | --- |
| gids | <code>Array.&lt;number&gt;</code> | 群组ID列表 |

### groupManage.getGruopMessage(gid) ⇒ [<code>Array.&lt;Meta&gt;</code>](types.md#module_types__meta) {#module_groupmanage__getgruopmessage}
获取群消息

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Array.&lt;Meta&gt;</code>](types.md#module_types__meta) - 群消息列表  

| Param | Type | Description |
| --- | --- | --- |
| gid | <code>number</code> | 群ID |

### groupManage.asyncGetInfo(params) ⇒ [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) {#module_groupmanage__asyncgetinfo}
获取群组详情

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) - 群组详情  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |

### groupManage.asyncGetMemberList(param) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> {#module_groupmanage__asyncgetmemberlist}
获取群成员列表

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> - 群成员列表  

| Param | Type | Description |
| --- | --- | --- |
| param | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |

### groupManage.readGroupMessage(group_id, mid) {#module_groupmanage__readgroupmessage}
将群消息设置已读

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  

| Param | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | 群组ID |
| mid | <code>number</code> | 消息ID |

### groupManage.recallMessage(uid, mid) {#module_groupmanage__recallmessage}
撤回消息

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | 群组ID |
| mid | <code>number</code> | 消息ID |

### groupManage.getUnreadCount(gid) ⇒ <code>number</code> {#module_groupmanage__getunreadcount}
获取群未读消息数

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>number</code> - 未读消息数  

| Param | Type | Description |
| --- | --- | --- |
| gid | <code>number</code> | 群组ID |

### groupManage.asyncGetAdminList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> {#module_groupmanage__asyncgetadminlist}
获取群管理员列表

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> - 群管理员列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |

### groupManage.asyncAdminAdd(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncadminadd}
群添加管理员

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - 结果列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.user_list | <code>Array.&lt;number&gt;</code> | 群成员列表 |

### groupManage.asyncAdminRemove(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncadminremove}
移除管理员

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - 结果列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.user_list | <code>Array.&lt;number&gt;</code> | 群成员列表 |

### groupManage.asyncGetAnouncementById(params) ⇒ [<code>Promise.&lt;GroupAnnouncement&gt;</code>](types.md#module_types__groupannouncement) {#module_groupmanage__asyncgetanouncementbyid}
获取群公告详情

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupAnnouncement&gt;</code>](types.md#module_types__groupannouncement) - 群公告详情  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.announcement_id | <code>Array.&lt;number&gt;</code> | 公告ID |

### groupManage.asyncAnouncementDelete(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncanouncementdelete}
删除群公告

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.announcement_id | <code>Array.&lt;number&gt;</code> | 公告ID |

### groupManage.asyncAnnouncementEdit(params) ⇒ [<code>Promise.&lt;GroupAnnouncement&gt;</code>](types.md#module_types__groupannouncement) {#module_groupmanage__asyncannouncementedit}
编辑群公告

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupAnnouncement&gt;</code>](types.md#module_types__groupannouncement) - 群公告详情  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.title | <code>string</code> | 公告标题 |
| params.content | <code>string</code> | 公告内容 |

### groupManage.asyncGetAnnouncementList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupAnnouncement&gt;&gt;</code> {#module_groupmanage__asyncgetannouncementlist}
群公告列表

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupAnnouncement&gt;&gt;</code> - 群公告详情列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |

### groupManage.asyncCreate(params) ⇒ [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) {#module_groupmanage__asynccreate}
创建群组

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) - 群详情  

| Param | Type | Description |
| --- | --- | --- |
| params | [<code>GroupInfoRequest</code>](types.md#module_types__groupinforequest) | 请求参数 |

### groupManage.asyncDestroy(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncdestroy}
解散群组

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |

### groupManage.asyncUpdateAvatar(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdateavatar}
更新群头像

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.value | <code>string</code> | 头像地址 |

### groupManage.asyncUpdateDescription(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdatedescription}
更新群描述

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.value | <code>string</code> | 群组描述 |

### groupManage.asyncUpdateExt(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdateext}
更新群扩展信息

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.value | <code>string</code> | 扩展信息 |

### groupManage.asyncUpdateName(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdatename}
更新群名称

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.value | <code>string</code> | 群名称 |

### groupManage.asyncGroupMsgMutemode(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncgroupmsgmutemode}
设置群消息免打扰情况

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.msg_mute_mode | <code>number</code> | 群消息屏蔽模式: 0 - 表示不屏蔽, 1 - 表示屏蔽本地消息通知, 2 - 表示屏蔽消息，不接收消息 |

### groupManage.asyncGroupBannedList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMemberBanned&gt;&gt;</code> {#module_groupmanage__asyncgroupbannedlist}
获取群禁言列表

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupMemberBanned&gt;&gt;</code> - 禁言成员列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |

### groupManage.asyncGroupBab(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncgroupbab}
禁言群成员

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - 请求结果列表  

| Param | Type | Description |
| --- | --- | --- |
| params | [<code>GroupBannedMemberRequest</code>](types.md#module_types__groupbannedmemberrequest) | 请求参数 |

### groupManage.asyncGroupUnban(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncgroupunban}
解除成员禁言

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - 请求结果列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.user_list | <code>Array.&lt;number&gt;</code> | 群成员列表 |

### groupManage.asyncGetSettings(group_id) ⇒ [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) {#module_groupmanage__asyncgetsettings}
获取群设置

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) - 群设置  

| Param | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | 群ID |

### groupManage.asyncUpdateAllowMemberInvitation(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdateallowmemberinvitation}
设置群成员是否可以邀请

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.value | <code>boolean</code> | 群成员邀请设置: false - 不允许邀请, true - 允许邀请(默认) |

### groupManage.asyncUpdateAllowMemberModify(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdateallowmembermodify}
设置群成员是否可以修改群信息

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.value | <code>boolean</code> | 群成员修改群信息设置:  false - 群成员不能修改群信息(默认), true - 群成员可以修改群信息 |

### groupManage.asyncUpdateEnableReadack(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdateenablereadack}
设置群是否开启已读模式

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.value | <code>boolean</code> | 是否开启群消息已读功能:  false - 不开启, true - 开启 |

### groupManage.asyncUpdateHistoryVisible(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdatehistoryvisible}
设置群历史是否可见

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.value | <code>boolean</code> | 设置群历史是否可见:  false - 不可见, true - 可见 |

### groupManage.asyncUpdateRequireadminapproval(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdaterequireadminapproval}
设置入群是否需要申请

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.apply_approval | <code>boolean</code> | 入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请 |

### groupManage.asyncBanAll(params) ⇒ [<code>Promise.&lt;GroupBanAllResponse&gt;</code>](types.md#module_types__groupbanallresponse) {#module_groupmanage__asyncbanall}
全员禁言，只允许管理员发消息

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupBanAllResponse&gt;</code>](types.md#module_types__groupbanallresponse) - 结果  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.duration | <code>number</code> | 禁言时长，单位为分钟,int64 |
| params.group_id | <code>number</code> | 群id,int64 |

### groupManage.asyncUnBanAll(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncunbanall}
取消全员禁言

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群id,int64 |

### groupManage.asyncOwnerTransfer(params) ⇒ [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse) {#module_groupmanage__asyncownertransfer}
更换群主

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse) - 结果  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.new_owner | <code>number</code> | 新群主的用户ID |

### groupManage.asyncGetUserJoined(params) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> {#module_groupmanage__asyncgetuserjoined}
获取用户的群组列表

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> - 群ID的列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数, 空对象 |

### groupManage.asyncApply(params) ⇒ [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse) {#module_groupmanage__asyncapply}
申请加入群

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse) - 结果  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.reason | <code>string</code> | 申请入群原因 |

### groupManage.asyncApplyHandle(params) ⇒ [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse) {#module_groupmanage__asyncapplyhandle}
处理用户的入群申请

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse) - 结果  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.user_id | <code>number</code> | 用户ID |
| params.approval | <code>boolean</code> | 审批结果：true为同意，false为拒绝 |

### groupManage.asyncGroupBockedlist(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupBlockedListItem&gt;&gt;</code> {#module_groupmanage__asyncgroupbockedlist}
获取群黑名单

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupBlockedListItem&gt;&gt;</code> - 群黑名单列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |

### groupManage.asyncGroupBlock(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncgroupblock}
将成员加入黑名单

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - 结果列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.user_list | <code>Array.&lt;number&gt;</code> | 群成员列表 |

### groupManage.asyncGroupUnblock(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncgroupunblock}
解除黑名单

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - 结果列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.user_list | <code>Array.&lt;number&gt;</code> | 群成员列表 |

### groupManage.asyncKick(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asynckick}
踢出群组

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - 结果列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.user_list | <code>Array.&lt;number&gt;</code> | 群成员列表 |

### groupManage.asyncGetInvitationList() ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupInvitation&gt;&gt;</code> {#module_groupmanage__asyncgetinvitationlist}
获取群邀请列表

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupInvitation&gt;&gt;</code> - 群邀请列表  
### groupManage.asyncInvite(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncinvite}
邀请成员加入群

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - 结果列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.user_list | <code>Array.&lt;number&gt;</code> | 群成员列表 |

### groupManage.asyncInviteHandle(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncinvitehandle}
处理群邀请

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.user_id | <code>number</code> | 用户ID |
| params.approval | <code>boolean</code> | 审批结果：true为同意，false为拒绝 |

### groupManage.asyncGetMemberDisplayName(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> {#module_groupmanage__asyncgetmemberdisplayname}
批量获取群成员的群名片

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> - 群成员列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.user_list | <code>Array.&lt;number&gt;</code> | 群成员列表 |

### groupManage.asyncLeave(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncleave}
退出群

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |

### groupManage.asyncUpdateDisplayName(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdatedisplayname}
修改群名片

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.value | <code>string</code> | 新名片 |

### groupManage.asncGetApplicationList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupApplication&gt;&gt;</code> {#module_groupmanage__asncgetapplicationlist}
获取群申请列表

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupApplication&gt;&gt;</code> - 群申请列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_list | <code>Array.&lt;number&gt;</code> | 群列表 |

### groupManage.asyncGetFileList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupSharedFile&gt;&gt;</code> {#module_groupmanage__asyncgetfilelist}
获取群文件列表

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupSharedFile&gt;&gt;</code> - 群文件列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |

### groupManage.asyncFileDelete(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupSharedFileResponse&gt;&gt;</code> {#module_groupmanage__asyncfiledelete}
删除群文件

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupSharedFileResponse&gt;&gt;</code> - 结果列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群组ID |
| params.file_list | <code>Array.&lt;number&gt;</code> | 文件ID列表 |

### groupManage.asyncFileUpload(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupSharedFile&gt;&gt;</code> {#module_groupmanage__asyncfileupload}
上传群文件

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupSharedFile&gt;&gt;</code> - 群文件列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.group_id | <code>number</code> | 群id,int64 |
| params.name | <code>string</code> | 文件名称 |
| params.size | <code>number</code> | 文件大小,int64 |
| params.type | <code>string</code> | 文件类型 |
| params.url | <code>string</code> | 文件url |
