# groupManage
## groupManage {#module_groupmanage}
Group management


* [groupManage](#module_groupmanage)
    * [.asyncGetGroupInfo(group_id, froce)](#module_groupmanage__asyncgetgroupinfo) ⇒ [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings)
    * [.asyncGetJoinedGroups(froce)](#module_groupmanage__asyncgetjoinedgroups) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code>
    * [.openGroup(group_id)](#module_groupmanage__opengroup)
    * [.getAllGroupDetail()](#module_groupmanage__getallgroupdetail) ⇒ <code>Object.&lt;number, module:types~GroupInfoAndSettings&gt;</code>
    * [.asyncGetGroupMembers(group_id)](#module_groupmanage__asyncgetgroupmembers) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code>    
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
Get group information

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) - Group info  

| Param | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | GroupID |
| froce | <code>boolean</code> | Whether to force pull from server: true - pull from server, false - prefer to pull from local storage |

### groupManage.asyncGetJoinedGroups(froce) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> {#module_groupmanage__asyncgetjoinedgroups}
Get the group to join

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> - Group ID list  

| Param | Type | Description |
| --- | --- | --- |
| froce | <code>boolean</code> | Whether to force pull from server: true - pull from server, false - prefer to pull from local storage |

### groupManage.openGroup(group_id) {#module_groupmanage__opengroup}
Open group, this method will prepare some necessary information for the group chat screen.

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  

| Param | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | GroupID |

### groupManage.getAllGroupDetail() ⇒ <code>Object.&lt;number, module:types~GroupInfoAndSettings&gt;</code> {#module_groupmanage__getallgroupdetail}
Get all cached group details

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Object.&lt;number, module:types~GroupInfoAndSettings&gt;</code> - Group details  
### groupManage.asyncGetGroupMembers(group_id) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> {#module_groupmanage__asyncgetgroupmembers}
Get group member ids (asynchronous)

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> - List of group member ids  

| Param | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | GroupID |

### groupManage.getGroupMembers(group_id) ⇒ [<code>Array.&lt;GroupMember&gt;</code>](types.md#module_types__groupmember) {#module_groupmanage__getgroupmembers}
Get group members (synchronous)

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Array.&lt;GroupMember&gt;</code>](types.md#module_types__groupmember) - List of group members  

| Param | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | GroupID |

### groupManage.asyncGetGroupListDetail(gids) ⇒ <code>Promise.&lt;Array.&lt;module:types~BriefGroupInfoAndSettings&gt;&gt;</code> {#module_groupmanage__asyncgetgrouplistdetail}
Get group details by id

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~BriefGroupInfoAndSettings&gt;&gt;</code> - List of group details  

| Param | Type | Description |
| --- | --- | --- |
| gids | <code>Array.&lt;number&gt;</code> | Group ID list |

### groupManage.getGruopMessage(gid) ⇒ [<code>Array.&lt;Meta&gt;</code>](types.md#module_types__meta) {#module_groupmanage__getgruopmessage}
Get group information

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Array.&lt;Meta&gt;</code>](types.md#module_types__meta) - List of group messages  

| Param | Type | Description |
| --- | --- | --- |
| gid | <code>number</code> | GroupID |

### groupManage.asyncGetInfo(params) ⇒ [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) {#module_groupmanage__asyncgetinfo}
Get group details

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) - Group details  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |

### groupManage.asyncGetMemberList(param) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> {#module_groupmanage__asyncgetmemberlist}
Get group member list

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> - List of group members  

| Param | Type | Description |
| --- | --- | --- |
| param | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |

### groupManage.readGroupMessage(group_id, mid) {#module_groupmanage__readgroupmessage}
Set group message to read

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  

| Param | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | GroupID |
| mid | <code>number</code> | MessageID |

### groupManage.recallMessage(uid, mid) {#module_groupmanage__recallmessage}
Revoke message

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | GroupID |
| mid | <code>number</code> | MessageID |

### groupManage.getUnreadCount(gid) ⇒ <code>number</code> {#module_groupmanage__getunreadcount}
Get number of unread group messages

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>number</code> - Unread message-number  

| Param | Type | Description |
| --- | --- | --- |
| gid | <code>number</code> | GroupID |

### groupManage.asyncGetAdminList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> {#module_groupmanage__asyncgetadminlist}
Get the list of group Admins

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> - List of group admins  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |

### groupManage.asyncAdminAdd(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncadminadd}
Add group Admin

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - List of results  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.user_list | <code>Array.&lt;number&gt;</code> | List of group members |

### groupManage.asyncAdminRemove(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncadminremove}
Remove group Admin

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - List of results  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.user_list | <code>Array.&lt;number&gt;</code> | List of group members |

### groupManage.asyncGetAnouncementById(params) ⇒ [<code>Promise.&lt;GroupAnnouncement&gt;</code>](types.md#module_types__groupannouncement) {#module_groupmanage__asyncgetanouncementbyid}
Get group announcement details

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupAnnouncement&gt;</code>](types.md#module_types__groupannouncement) - Group announcement details  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.announcement_id | <code>Array.&lt;number&gt;</code> | Announcement ID |

### groupManage.asyncAnouncementDelete(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncanouncementdelete}
Delete group announcement

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.announcement_id | <code>Array.&lt;number&gt;</code> | Announcement ID |

### groupManage.asyncAnnouncementEdit(params) ⇒ [<code>Promise.&lt;GroupAnnouncement&gt;</code>](types.md#module_types__groupannouncement) {#module_groupmanage__asyncannouncementedit}
Edit group announcement

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupAnnouncement&gt;</code>](types.md#module_types__groupannouncement) - Group announcement details  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.title | <code>string</code> | Announcement tittle |
| params.content | <code>string</code> | Announcement content |

### groupManage.asyncGetAnnouncementList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupAnnouncement&gt;&gt;</code> {#module_groupmanage__asyncgetannouncementlist}
Group announcement list

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupAnnouncement&gt;&gt;</code> - List of group announcement details  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |

### groupManage.asyncCreate(params) ⇒ [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) {#module_groupmanage__asynccreate}
Create group

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) - Group details  

| Param | Type | Description |
| --- | --- | --- |
| params | [<code>GroupInfoRequest</code>](types.md#module_types__groupinforequest) | Request parameters |

### groupManage.asyncDestroy(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncdestroy}
Dissolve group

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |

### groupManage.asyncUpdateAvatar(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdateavatar}
Update group avatar

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.value | <code>string</code> | AvatarAddress |

### groupManage.asyncUpdateDescription(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdatedescription}
Update group description

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.value | <code>string</code> | Group description |

### groupManage.asyncUpdateExt(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdateext}
Update group extension information

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.value | <code>string</code> | Extension information |

### groupManage.asyncUpdateName(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdatename}
Update group name

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.value | <code>string</code> | Group name |

### groupManage.asyncGroupMsgMutemode(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncgroupmsgmutemode}
Set do-not-disturb conditions for group message

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.msg_mute_mode | <code>number</code> | Group message blocking mode: 0 - no blocking, 1 - blocking local message notifications, 2 - blocking all, means not receiving messages |

### groupManage.asyncGroupBannedList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMemberBanned&gt;&gt;</code> {#module_groupmanage__asyncgroupbannedlist}
Get group ban list

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupMemberBanned&gt;&gt;</code> - List of banned members  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |

### groupManage.asyncGroupBab(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncgroupbab}
Ban group member

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - List of request results  

| Param | Type | Description |
| --- | --- | --- |
| params | [<code>GroupBannedMemberRequest</code>](types.md#module_types__groupbannedmemberrequest) | Request parameters |

### groupManage.asyncGroupUnban(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncgroupunban}
Unban group memberBan

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - List of request results  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.user_list | <code>Array.&lt;number&gt;</code> | List of group members |

### groupManage.asyncGetSettings(group_id) ⇒ [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) {#module_groupmanage__asyncgetsettings}
Get group settings

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupInfoAndSettings&gt;</code>](types.md#module_types__groupinfoandsettings) - Group settings  

| Param | Type | Description |
| --- | --- | --- |
| group_id | <code>number</code> | GroupID |

### groupManage.asyncUpdateAllowMemberInvitation(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdateallowmemberinvitation}
Set whether group members can invite new member

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.value | <code>boolean</code> | Group member invite settings: false - do not allow invitations, true - allow invitations (default) |

### groupManage.asyncUpdateAllowMemberModify(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdateallowmembermodify}
Set whether group members can modify group information

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.value | <code>boolean</code> | Group members modify group info settings: false - group members can't modify group info (default), true - group members can modify group info |

### groupManage.asyncUpdateEnableReadack(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdateenablereadack}
Set whether to enable read mode in group

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.value | <code>boolean</code> | Enable or disable group message read feature: false - disabled, true - enabled |

### groupManage.asyncUpdateHistoryVisible(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdatehistoryvisible}
Set whether group history is visible

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.value | <code>boolean</code> | Set whether the group history is visible: false - not visible, true - visible |

### groupManage.asyncUpdateRequireadminapproval(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdaterequireadminapproval}
Set whether need to apply for group joining

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.apply_approval | <code>boolean</code> | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests |

### groupManage.asyncBanAll(params) ⇒ [<code>Promise.&lt;GroupBanAllResponse&gt;</code>](types.md#module_types__groupbanallresponse) {#module_groupmanage__asyncbanall}
Ban all members, only Admins can send messages

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupBanAllResponse&gt;</code>](types.md#module_types__groupbanallresponse) - Results  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.duration | <code>number</code> | Duration of banned in minutes,int64 |
| params.group_id | <code>number</code> | Group id,int64 |

### groupManage.asyncUnBanAll(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncunbanall}
Unban all members

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | Group id,int64 |

### groupManage.asyncOwnerTransfer(params) ⇒ [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse) {#module_groupmanage__asyncownertransfer}
Change group Owner

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse) - Results  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.new_owner | <code>number</code> | User ID of the new group owner |

### groupManage.asyncGetUserJoined(params) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> {#module_groupmanage__asyncgetuserjoined}
Get the list of groups for the user

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> - List of group IDs  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter, Empty object |

### groupManage.asyncApply(params) ⇒ [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse) {#module_groupmanage__asyncapply}
Apply to join group

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse) - Results  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.reason | <code>string</code> | Reason for membership application |

### groupManage.asyncApplyHandle(params) ⇒ [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse) {#module_groupmanage__asyncapplyhandle}
Process user's group joining application

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: [<code>Promise.&lt;GroupUserRelationResponse&gt;</code>](types.md#module_types__groupuserrelationresponse) - Results  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.user_id | <code>number</code> | User ID |
| params.approval | <code>boolean</code> | Approval result: true for agree, false for reject |

### groupManage.asyncGroupBockedlist(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupBlockedListItem&gt;&gt;</code> {#module_groupmanage__asyncgroupbockedlist}
Get group blacklist

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupBlockedListItem&gt;&gt;</code> - GroupList of blacklists  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |

### groupManage.asyncGroupBlock(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncgroupblock}
Add member to blacklist

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - List of results  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.user_list | <code>Array.&lt;number&gt;</code> | List of group members |

### groupManage.asyncGroupUnblock(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncgroupunblock}
Remove member from blacklist

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - List of results  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.user_list | <code>Array.&lt;number&gt;</code> | List of group members |

### groupManage.asyncKick(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asynckick}
Kick out group member

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - List of results  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.user_list | <code>Array.&lt;number&gt;</code> | List of group members |

### groupManage.asyncGetInvitationList() ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupInvitation&gt;&gt;</code> {#module_groupmanage__asyncgetinvitationlist}
Get group invitation list

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupInvitation&gt;&gt;</code> - List of group invitations  
### groupManage.asyncInvite(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> {#module_groupmanage__asyncinvite}
Invite member to group

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupUserRelationResponse&gt;&gt;</code> - List of results  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.user_list | <code>Array.&lt;number&gt;</code> | List of group members |

### groupManage.asyncInviteHandle(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncinvitehandle}
Process group invitations

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.user_id | <code>number</code> | User ID |
| params.approval | <code>boolean</code> | Approval result: true for agree, false for reject |

### groupManage.asyncGetMemberDisplayName(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> {#module_groupmanage__asyncgetmemberdisplayname}
Batch retrieval of group member profiles

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupMember&gt;&gt;</code> - List of group members  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.user_list | <code>Array.&lt;number&gt;</code> | List of group members |

### groupManage.asyncLeave(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncleave}
Quit group

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |

### groupManage.asyncUpdateDisplayName(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_groupmanage__asyncupdatedisplayname}
Modify group profile

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.value | <code>string</code> | New user profile |

### groupManage.asncGetApplicationList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupApplication&gt;&gt;</code> {#module_groupmanage__asncgetapplicationlist}
Get the list of group membership requests

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupApplication&gt;&gt;</code> - List of group applications  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_list | <code>Array.&lt;number&gt;</code> | List of groups |

### groupManage.asyncGetFileList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupSharedFile&gt;&gt;</code> {#module_groupmanage__asyncgetfilelist}
Get the list of group files

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupSharedFile&gt;&gt;</code> - List of group files  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |

### groupManage.asyncFileDelete(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupSharedFileResponse&gt;&gt;</code> {#module_groupmanage__asyncfiledelete}
Delete group file

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupSharedFileResponse&gt;&gt;</code> - List of results  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | GroupID |
| params.file_list | <code>Array.&lt;number&gt;</code> | List of file IDs |

### groupManage.asyncFileUpload(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~GroupSharedFile&gt;&gt;</code> {#module_groupmanage__asyncfileupload}
Upload group file

**Kind**: static method of [<code>groupManage</code>](#module_groupmanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~GroupSharedFile&gt;&gt;</code> - List of group files  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.group_id | <code>number</code> | Group id,int64 |
| params.name | <code>string</code> | File name |
| params.size | <code>number</code> | File size,int64 |
| params.type | <code>string</code> | File type |
| params.url | <code>string</code> | File url |
