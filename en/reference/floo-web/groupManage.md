# groupManage

## groupManage <a href="#module_groupmanage" id="module_groupmanage"></a>

Group management

* [groupManage](groupManage.md#module_groupmanage)
  * [.asyncGetGroupInfo(group\_id, froce)](groupManage.md#module_groupmanage__asyncgetgroupinfo) ⇒ [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings)
  * [.asyncGetJoinedGroups(froce)](groupManage.md#module_groupmanage__asyncgetjoinedgroups) ⇒ `Promise.<Array.<number>>`
  * [.openGroup(group\_id)](groupManage.md#module_groupmanage__opengroup)
  * [.getAllGroupDetail()](groupManage.md#module_groupmanage__getallgroupdetail) ⇒ `Object.<number, module:types~GroupInfoAndSettings>`
  * [.asyncGetGroupMembers(group\_id)](groupManage.md#module_groupmanage__asyncgetgroupmembers) ⇒ `Promise.<Array.<number>>`
  * [.getGroupMembers(group\_id)](groupManage.md#module_groupmanage__getgroupmembers) ⇒ [`Array.<GroupMember>`](types.md#module_types__groupmember)
  * [.asyncGetGroupListDetail(gids)](groupManage.md#module_groupmanage__asyncgetgrouplistdetail) ⇒ `Promise.<Array.<module:types~BriefGroupInfoAndSettings>>`
  * [.getGruopMessage(gid)](groupManage.md#module_groupmanage__getgruopmessage) ⇒ [`Array.<Meta>`](types.md#module_types__meta)
  * [.asyncGetInfo(params)](groupManage.md#module_groupmanage__asyncgetinfo) ⇒ [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings)
  * [.asyncGetMemberList(param)](groupManage.md#module_groupmanage__asyncgetmemberlist) ⇒ `Promise.<Array.<module:types~GroupMember>>`
  * [.readGroupMessage(group\_id, mid)](groupManage.md#module_groupmanage__readgroupmessage)
  * [.recallMessage(uid, mid)](groupManage.md#module_groupmanage__recallmessage)
  * [.getUnreadCount(gid)](groupManage.md#module_groupmanage__getunreadcount) ⇒ `number`
  * [.asyncGetAdminList(params)](groupManage.md#module_groupmanage__asyncgetadminlist) ⇒ `Promise.<Array.<module:types~GroupMember>>`
  * [.asyncAdminAdd(params)](groupManage.md#module_groupmanage__asyncadminadd) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>`
  * [.asyncAdminRemove(params)](groupManage.md#module_groupmanage__asyncadminremove) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>`
  * [.asyncGetAnouncementById(params)](groupManage.md#module_groupmanage__asyncgetanouncementbyid) ⇒ [`Promise.<GroupAnnouncement>`](types.md#module_types__groupannouncement)
  * [.asyncAnouncementDelete(params)](groupManage.md#module_groupmanage__asyncanouncementdelete) ⇒ `Promise.<boolean>`
  * [.asyncAnnouncementEdit(params)](groupManage.md#module_groupmanage__asyncannouncementedit) ⇒ [`Promise.<GroupAnnouncement>`](types.md#module_types__groupannouncement)
  * [.asyncGetAnnouncementList(params)](groupManage.md#module_groupmanage__asyncgetannouncementlist) ⇒ `Promise.<Array.<module:types~GroupAnnouncement>>`
  * [.asyncCreate(params)](groupManage.md#module_groupmanage__asynccreate) ⇒ [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings)
  * [.asyncDestroy(params)](groupManage.md#module_groupmanage__asyncdestroy) ⇒ `Promise.<boolean>`
  * [.asyncUpdateAvatar(params)](groupManage.md#module_groupmanage__asyncupdateavatar) ⇒ `Promise.<boolean>`
  * [.asyncUpdateDescription(params)](groupManage.md#module_groupmanage__asyncupdatedescription) ⇒ `Promise.<boolean>`
  * [.asyncUpdateExt(params)](groupManage.md#module_groupmanage__asyncupdateext) ⇒ `Promise.<boolean>`
  * [.asyncUpdateName(params)](groupManage.md#module_groupmanage__asyncupdatename) ⇒ `Promise.<boolean>`
  * [.asyncGroupMsgMutemode(params)](groupManage.md#module_groupmanage__asyncgroupmsgmutemode) ⇒ `Promise.<boolean>`
  * [.asyncGroupBannedList(params)](groupManage.md#module_groupmanage__asyncgroupbannedlist) ⇒ `Promise.<Array.<module:types~GroupMemberBanned>>`
  * [.asyncGroupBab(params)](groupManage.md#module_groupmanage__asyncgroupbab) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>`
  * [.asyncGroupUnban(params)](groupManage.md#module_groupmanage__asyncgroupunban) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>`
  * [.asyncGetSettings(group\_id)](groupManage.md#module_groupmanage__asyncgetsettings) ⇒ [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings)
  * [.asyncUpdateAllowMemberInvitation(params)](groupManage.md#module_groupmanage__asyncupdateallowmemberinvitation) ⇒ `Promise.<boolean>`
  * [.asyncUpdateAllowMemberModify(params)](groupManage.md#module_groupmanage__asyncupdateallowmembermodify) ⇒ `Promise.<boolean>`
  * [.asyncUpdateEnableReadack(params)](groupManage.md#module_groupmanage__asyncupdateenablereadack) ⇒ `Promise.<boolean>`
  * [.asyncUpdateHistoryVisible(params)](groupManage.md#module_groupmanage__asyncupdatehistoryvisible) ⇒ `Promise.<boolean>`
  * [.asyncUpdateRequireadminapproval(params)](groupManage.md#module_groupmanage__asyncupdaterequireadminapproval) ⇒ `Promise.<boolean>`
  * [.asyncBanAll(params)](groupManage.md#module_groupmanage__asyncbanall) ⇒ [`Promise.<GroupBanAllResponse>`](types.md#module_types__groupbanallresponse)
  * [.asyncUnBanAll(params)](groupManage.md#module_groupmanage__asyncunbanall) ⇒ `Promise.<boolean>`
  * [.asyncOwnerTransfer(params)](groupManage.md#module_groupmanage__asyncownertransfer) ⇒ [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse)
  * [.asyncGetUserJoined(params)](groupManage.md#module_groupmanage__asyncgetuserjoined) ⇒ `Promise.<Array.<number>>`
  * [.asyncApply(params)](groupManage.md#module_groupmanage__asyncapply) ⇒ [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse)
  * [.asyncApplyHandle(params)](groupManage.md#module_groupmanage__asyncapplyhandle) ⇒ [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse)
  * [.asyncGroupBockedlist(params)](groupManage.md#module_groupmanage__asyncgroupbockedlist) ⇒ `Promise.<Array.<module:types~GroupBlockedListItem>>`
  * [.asyncGroupBlock(params)](groupManage.md#module_groupmanage__asyncgroupblock) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>`
  * [.asyncGroupUnblock(params)](groupManage.md#module_groupmanage__asyncgroupunblock) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>`
  * [.asyncKick(params)](groupManage.md#module_groupmanage__asynckick) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>`
  * [.asyncGetInvitationList()](groupManage.md#module_groupmanage__asyncgetinvitationlist) ⇒ `Promise.<Array.<module:types~GroupInvitation>>`
  * [.asyncInvite(params)](groupManage.md#module_groupmanage__asyncinvite) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>`
  * [.asyncInviteHandle(params)](groupManage.md#module_groupmanage__asyncinvitehandle) ⇒ `Promise.<boolean>`
  * [.asyncGetMemberDisplayName(params)](groupManage.md#module_groupmanage__asyncgetmemberdisplayname) ⇒ `Promise.<Array.<module:types~GroupMember>>`
  * [.asyncLeave(params)](groupManage.md#module_groupmanage__asyncleave) ⇒ `Promise.<boolean>`
  * [.asyncUpdateDisplayName(params)](groupManage.md#module_groupmanage__asyncupdatedisplayname) ⇒ `Promise.<boolean>`
  * [.asncGetApplicationList(params)](groupManage.md#module_groupmanage__asncgetapplicationlist) ⇒ `Promise.<Array.<module:types~GroupApplication>>`
  * [.asyncGetFileList(params)](groupManage.md#module_groupmanage__asyncgetfilelist) ⇒ `Promise.<Array.<module:types~GroupSharedFile>>`
  * [.asyncFileDelete(params)](groupManage.md#module_groupmanage__asyncfiledelete) ⇒ `Promise.<Array.<module:types~GroupSharedFileResponse>>`
  * [.asyncFileUpload(params)](groupManage.md#module_groupmanage__asyncfileupload) ⇒ `Promise.<Array.<module:types~GroupSharedFile>>`

### groupManage.asyncGetGroupInfo(group\_id, froce) ⇒ [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) <a href="#module_groupmanage__asyncgetgroupinfo" id="module_groupmanage__asyncgetgroupinfo"></a>

Get group information

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) - Group info

| Param     | Type      | Description                                                                                           |
| --------- | --------- | ----------------------------------------------------------------------------------------------------- |
| group\_id | `number`  | GroupID                                                                                               |
| froce     | `boolean` | Whether to force pull from server: true - pull from server, false - prefer to pull from local storage |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetJoinedGroups(froce) ⇒ `Promise.<Array.<number>>` <a href="#module_groupmanage__asyncgetjoinedgroups" id="module_groupmanage__asyncgetjoinedgroups"></a>

Get the group to join

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<number>>` - Group ID list

| Param | Type      | Description                                                                                           |
| ----- | --------- | ----------------------------------------------------------------------------------------------------- |
| froce | `boolean` | Whether to force pull from server: true - pull from server, false - prefer to pull from local storage |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.openGroup(group\_id) <a href="#module_groupmanage__opengroup" id="module_groupmanage__opengroup"></a>

Open group, this method will prepare some necessary information for the group chat screen.

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)

| Param     | Type     | Description |
| --------- | -------- | ----------- |
| group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.getAllGroupDetail() ⇒ `Object.<number, module:types~GroupInfoAndSettings>` <a href="#module_groupmanage__getallgroupdetail" id="module_groupmanage__getallgroupdetail"></a>

Get all cached group details

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Object.<number, module:types~GroupInfoAndSettings>` - Group details\
**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetGroupMembers(group\_id) ⇒ `Promise.<Array.<number>>` <a href="#module_groupmanage__asyncgetgroupmembers" id="module_groupmanage__asyncgetgroupmembers"></a>

Get group member ids (asynchronous)

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<number>>` - List of group member ids

| Param     | Type     | Description |
| --------- | -------- | ----------- |
| group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.getGroupMembers(group\_id) ⇒ [`Array.<GroupMember>`](types.md#module_types__groupmember) <a href="#module_groupmanage__getgroupmembers" id="module_groupmanage__getgroupmembers"></a>

Get group members (synchronous)

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Array.<GroupMember>`](types.md#module_types__groupmember) - List of group members

| Param     | Type     | Description |
| --------- | -------- | ----------- |
| group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetGroupListDetail(gids) ⇒ `Promise.<Array.<module:types~BriefGroupInfoAndSettings>>` <a href="#module_groupmanage__asyncgetgrouplistdetail" id="module_groupmanage__asyncgetgrouplistdetail"></a>

Get group details by id

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~BriefGroupInfoAndSettings>>` - List of group details

| Param | Type             | Description   |
| ----- | ---------------- | ------------- |
| gids  | `Array.<number>` | Group ID list |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.getGruopMessage(gid) ⇒ [`Array.<Meta>`](types.md#module_types__meta) <a href="#module_groupmanage__getgruopmessage" id="module_groupmanage__getgruopmessage"></a>

Get group information

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Array.<Meta>`](types.md#module_types__meta) - List of group messages

| Param | Type     | Description |
| ----- | -------- | ----------- |
| gid   | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetInfo(params) ⇒ [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) <a href="#module_groupmanage__asyncgetinfo" id="module_groupmanage__asyncgetinfo"></a>

Get group details

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) - Group details

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | Parameter   |
| params.group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetMemberList(param) ⇒ `Promise.<Array.<module:types~GroupMember>>` <a href="#module_groupmanage__asyncgetmemberlist" id="module_groupmanage__asyncgetmemberlist"></a>

Get group member list

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupMember>>` - List of group members

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| param            | `object` | Parameter   |
| params.group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.readGroupMessage(group\_id, mid) <a href="#module_groupmanage__readgroupmessage" id="module_groupmanage__readgroupmessage"></a>

Set group message to read

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)

| Param     | Type     | Description |
| --------- | -------- | ----------- |
| group\_id | `number` | GroupID     |
| mid       | `number` | MessageID   |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.recallMessage(uid, mid) <a href="#module_groupmanage__recallmessage" id="module_groupmanage__recallmessage"></a>

Revoke message

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)

| Param | Type     | Description |
| ----- | -------- | ----------- |
| uid   | `number` | GroupID     |
| mid   | `number` | MessageID   |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.getUnreadCount(gid) ⇒ `number` <a href="#module_groupmanage__getunreadcount" id="module_groupmanage__getunreadcount"></a>

Get number of unread group messages

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `number` - Unread message-number

| Param | Type     | Description |
| ----- | -------- | ----------- |
| gid   | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetAdminList(params) ⇒ `Promise.<Array.<module:types~GroupMember>>` <a href="#module_groupmanage__asyncgetadminlist" id="module_groupmanage__asyncgetadminlist"></a>

Get the list of group Admins

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupMember>>` - List of group admins

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | Parameter   |
| params.group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncAdminAdd(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncadminadd" id="module_groupmanage__asyncadminadd"></a>

Add group Admin

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - List of results

| Param             | Type             | Description           |
| ----------------- | ---------------- | --------------------- |
| params            | `object`         | Parameter             |
| params.group\_id  | `number`         | GroupID               |
| params.user\_list | `Array.<number>` | List of group members |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncAdminRemove(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncadminremove" id="module_groupmanage__asyncadminremove"></a>

Remove group Admin

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - List of results

| Param             | Type             | Description           |
| ----------------- | ---------------- | --------------------- |
| params            | `object`         | Parameter             |
| params.group\_id  | `number`         | GroupID               |
| params.user\_list | `Array.<number>` | List of group members |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetAnouncementById(params) ⇒ [`Promise.<GroupAnnouncement>`](types.md#module_types__groupannouncement) <a href="#module_groupmanage__asyncgetanouncementbyid" id="module_groupmanage__asyncgetanouncementbyid"></a>

Get group announcement details

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupAnnouncement>`](types.md#module_types__groupannouncement) - Group announcement details

| Param                   | Type             | Description     |
| ----------------------- | ---------------- | --------------- |
| params                  | `object`         | Parameter       |
| params.group\_id        | `number`         | GroupID         |
| params.announcement\_id | `Array.<number>` | Announcement ID |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncAnouncementDelete(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncanouncementdelete" id="module_groupmanage__asyncanouncementdelete"></a>

Delete group announcement

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param                   | Type             | Description     |
| ----------------------- | ---------------- | --------------- |
| params                  | `object`         | Parameter       |
| params.group\_id        | `number`         | GroupID         |
| params.announcement\_id | `Array.<number>` | Announcement ID |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncAnnouncementEdit(params) ⇒ [`Promise.<GroupAnnouncement>`](types.md#module_types__groupannouncement) <a href="#module_groupmanage__asyncannouncementedit" id="module_groupmanage__asyncannouncementedit"></a>

Edit group announcement

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupAnnouncement>`](types.md#module_types__groupannouncement) - Group announcement details

| Param            | Type     | Description          |
| ---------------- | -------- | -------------------- |
| params           | `object` | Parameter            |
| params.group\_id | `number` | GroupID              |
| params.title     | `string` | Announcement tittle  |
| params.content   | `string` | Announcement content |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetAnnouncementList(params) ⇒ `Promise.<Array.<module:types~GroupAnnouncement>>` <a href="#module_groupmanage__asyncgetannouncementlist" id="module_groupmanage__asyncgetannouncementlist"></a>

Group announcement list

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupAnnouncement>>` - List of group announcement details

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | Parameter   |
| params.group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncCreate(params) ⇒ [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) <a href="#module_groupmanage__asynccreate" id="module_groupmanage__asynccreate"></a>

Create group

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) - Group details

| Param  | Type                                                          | Description        |
| ------ | ------------------------------------------------------------- | ------------------ |
| params | [`GroupInfoRequest`](types.md#module_types__groupinforequest) | Request parameters |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncDestroy(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncdestroy" id="module_groupmanage__asyncdestroy"></a>

Dissolve group

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | Parameter   |
| params.group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateAvatar(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdateavatar" id="module_groupmanage__asyncupdateavatar"></a>

Update group avatar

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type     | Description   |
| ---------------- | -------- | ------------- |
| params           | `object` | Parameter     |
| params.group\_id | `number` | GroupID       |
| params.value     | `string` | AvatarAddress |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateDescription(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdatedescription" id="module_groupmanage__asyncupdatedescription"></a>

Update group description

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type     | Description       |
| ---------------- | -------- | ----------------- |
| params           | `object` | Parameter         |
| params.group\_id | `number` | GroupID           |
| params.value     | `string` | Group description |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateExt(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdateext" id="module_groupmanage__asyncupdateext"></a>

Update group extension information

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type     | Description           |
| ---------------- | -------- | --------------------- |
| params           | `object` | Parameter             |
| params.group\_id | `number` | GroupID               |
| params.value     | `string` | Extension information |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateName(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdatename" id="module_groupmanage__asyncupdatename"></a>

Update group name

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | Parameter   |
| params.group\_id | `number` | GroupID     |
| params.value     | `string` | Group name  |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupMsgMutemode(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncgroupmsgmutemode" id="module_groupmanage__asyncgroupmsgmutemode"></a>

Set do-not-disturb conditions for group message

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param                  | Type     | Description                                                                                                                            |
| ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| params                 | `object` | Parameter                                                                                                                              |
| params.group\_id       | `number` | GroupID                                                                                                                                |
| params.msg\_mute\_mode | `number` | Group message blocking mode: 0 - no blocking, 1 - blocking local message notifications, 2 - blocking all, means not receiving messages |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupBannedList(params) ⇒ `Promise.<Array.<module:types~GroupMemberBanned>>` <a href="#module_groupmanage__asyncgroupbannedlist" id="module_groupmanage__asyncgroupbannedlist"></a>

Get group ban list

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupMemberBanned>>` - List of banned members

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | Parameter   |
| params.group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupBab(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncgroupbab" id="module_groupmanage__asyncgroupbab"></a>

Ban group member

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - List of request results

| Param  | Type                                                                          | Description        |
| ------ | ----------------------------------------------------------------------------- | ------------------ |
| params | [`GroupBannedMemberRequest`](types.md#module_types__groupbannedmemberrequest) | Request parameters |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupUnban(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncgroupunban" id="module_groupmanage__asyncgroupunban"></a>

Unban group memberBan

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - List of request results

| Param             | Type             | Description           |
| ----------------- | ---------------- | --------------------- |
| params            | `object`         | Parameter             |
| params.group\_id  | `number`         | GroupID               |
| params.user\_list | `Array.<number>` | List of group members |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetSettings(group\_id) ⇒ [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) <a href="#module_groupmanage__asyncgetsettings" id="module_groupmanage__asyncgetsettings"></a>

Get group settings

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) - Group settings

| Param     | Type     | Description |
| --------- | -------- | ----------- |
| group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateAllowMemberInvitation(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdateallowmemberinvitation" id="module_groupmanage__asyncupdateallowmemberinvitation"></a>

Set whether group members can invite new member

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type      | Description                                                                                        |
| ---------------- | --------- | -------------------------------------------------------------------------------------------------- |
| params           | `object`  | Parameter                                                                                          |
| params.group\_id | `number`  | GroupID                                                                                            |
| params.value     | `boolean` | Group member invite settings: false - do not allow invitations, true - allow invitations (default) |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateAllowMemberModify(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdateallowmembermodify" id="module_groupmanage__asyncupdateallowmembermodify"></a>

Set whether group members can modify group information

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type      | Description                                                                                                                                   |
| ---------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| params           | `object`  | Parameter                                                                                                                                     |
| params.group\_id | `number`  | GroupID                                                                                                                                       |
| params.value     | `boolean` | Group members modify group info settings: false - group members can't modify group info (default), true - group members can modify group info |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateEnableReadack(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdateenablereadack" id="module_groupmanage__asyncupdateenablereadack"></a>

Set whether to enable read mode in group

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type      | Description                                                                    |
| ---------------- | --------- | ------------------------------------------------------------------------------ |
| params           | `object`  | Parameter                                                                      |
| params.group\_id | `number`  | GroupID                                                                        |
| params.value     | `boolean` | Enable or disable group message read feature: false - disabled, true - enabled |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateHistoryVisible(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdatehistoryvisible" id="module_groupmanage__asyncupdatehistoryvisible"></a>

Set whether group history is visible

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type      | Description                                                                   |
| ---------------- | --------- | ----------------------------------------------------------------------------- |
| params           | `object`  | Parameter                                                                     |
| params.group\_id | `number`  | GroupID                                                                       |
| params.value     | `boolean` | Set whether the group history is visible: false - not visible, true - visible |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateRequireadminapproval(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdaterequireadminapproval" id="module_groupmanage__asyncupdaterequireadminapproval"></a>

Set whether need to apply for group joining

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param                  | Type      | Description                                                                                                     |
| ---------------------- | --------- | --------------------------------------------------------------------------------------------------------------- |
| params                 | `object`  | Parameter                                                                                                       |
| params.group\_id       | `number`  | GroupID                                                                                                         |
| params.apply\_approval | `boolean` | Group membership application settings, 0: Agree all requests 1: Need to confirm by Admin 2: Reject all requests |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncBanAll(params) ⇒ [`Promise.<GroupBanAllResponse>`](types.md#module_types__groupbanallresponse) <a href="#module_groupmanage__asyncbanall" id="module_groupmanage__asyncbanall"></a>

Ban all members, only Admins can send messages

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupBanAllResponse>`](types.md#module_types__groupbanallresponse) - Results

| Param            | Type     | Description                         |
| ---------------- | -------- | ----------------------------------- |
| params           | `object` | Parameter                           |
| params.duration  | `number` | Duration of banned in minutes,int64 |
| params.group\_id | `number` | Group id,int64                      |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUnBanAll(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncunbanall" id="module_groupmanage__asyncunbanall"></a>

Unban all members

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type     | Description    |
| ---------------- | -------- | -------------- |
| params           | `object` | Parameter      |
| params.group\_id | `number` | Group id,int64 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncOwnerTransfer(params) ⇒ [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse) <a href="#module_groupmanage__asyncownertransfer" id="module_groupmanage__asyncownertransfer"></a>

Change group Owner

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse) - Results

| Param             | Type     | Description                    |
| ----------------- | -------- | ------------------------------ |
| params            | `object` | Parameter                      |
| params.group\_id  | `number` | GroupID                        |
| params.new\_owner | `number` | User ID of the new group owner |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetUserJoined(params) ⇒ `Promise.<Array.<number>>` <a href="#module_groupmanage__asyncgetuserjoined" id="module_groupmanage__asyncgetuserjoined"></a>

Get the list of groups for the user

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<number>>` - List of group IDs

| Param  | Type     | Description             |
| ------ | -------- | ----------------------- |
| params | `object` | Parameter, Empty object |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncApply(params) ⇒ [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse) <a href="#module_groupmanage__asyncapply" id="module_groupmanage__asyncapply"></a>

Apply to join group

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse) - Results

| Param            | Type     | Description                       |
| ---------------- | -------- | --------------------------------- |
| params           | `object` | Parameter                         |
| params.group\_id | `number` | GroupID                           |
| params.reason    | `string` | Reason for membership application |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncApplyHandle(params) ⇒ [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse) <a href="#module_groupmanage__asyncapplyhandle" id="module_groupmanage__asyncapplyhandle"></a>

Process user's group joining application

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse) - Results

| Param            | Type      | Description                                       |
| ---------------- | --------- | ------------------------------------------------- |
| params           | `object`  | Parameter                                         |
| params.group\_id | `number`  | GroupID                                           |
| params.user\_id  | `number`  | User ID                                           |
| params.approval  | `boolean` | Approval result: true for agree, false for reject |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupBockedlist(params) ⇒ `Promise.<Array.<module:types~GroupBlockedListItem>>` <a href="#module_groupmanage__asyncgroupbockedlist" id="module_groupmanage__asyncgroupbockedlist"></a>

Get group blacklist

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupBlockedListItem>>` - GroupList of blacklists

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | Parameter   |
| params.group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupBlock(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncgroupblock" id="module_groupmanage__asyncgroupblock"></a>

Add member to blacklist

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - List of results

| Param             | Type             | Description           |
| ----------------- | ---------------- | --------------------- |
| params            | `object`         | Parameter             |
| params.group\_id  | `number`         | GroupID               |
| params.user\_list | `Array.<number>` | List of group members |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupUnblock(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncgroupunblock" id="module_groupmanage__asyncgroupunblock"></a>

Remove member from blacklist

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - List of results

| Param             | Type             | Description           |
| ----------------- | ---------------- | --------------------- |
| params            | `object`         | Parameter             |
| params.group\_id  | `number`         | GroupID               |
| params.user\_list | `Array.<number>` | List of group members |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncKick(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asynckick" id="module_groupmanage__asynckick"></a>

Kick out group member

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - List of results

| Param             | Type             | Description           |
| ----------------- | ---------------- | --------------------- |
| params            | `object`         | Parameter             |
| params.group\_id  | `number`         | GroupID               |
| params.user\_list | `Array.<number>` | List of group members |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetInvitationList() ⇒ `Promise.<Array.<module:types~GroupInvitation>>` <a href="#module_groupmanage__asyncgetinvitationlist" id="module_groupmanage__asyncgetinvitationlist"></a>

Get group invitation list

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupInvitation>>` - List of group invitations\
**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncInvite(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncinvite" id="module_groupmanage__asyncinvite"></a>

Invite member to group

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - List of results

| Param             | Type             | Description           |
| ----------------- | ---------------- | --------------------- |
| params            | `object`         | Parameter             |
| params.group\_id  | `number`         | GroupID               |
| params.user\_list | `Array.<number>` | List of group members |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncInviteHandle(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncinvitehandle" id="module_groupmanage__asyncinvitehandle"></a>

Process group invitations

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type      | Description                                       |
| ---------------- | --------- | ------------------------------------------------- |
| params           | `object`  | Parameter                                         |
| params.group\_id | `number`  | GroupID                                           |
| params.user\_id  | `number`  | User ID                                           |
| params.approval  | `boolean` | Approval result: true for agree, false for reject |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetMemberDisplayName(params) ⇒ `Promise.<Array.<module:types~GroupMember>>` <a href="#module_groupmanage__asyncgetmemberdisplayname" id="module_groupmanage__asyncgetmemberdisplayname"></a>

Batch retrieval of group member profiles

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupMember>>` - List of group members

| Param             | Type             | Description           |
| ----------------- | ---------------- | --------------------- |
| params            | `object`         | Parameter             |
| params.group\_id  | `number`         | GroupID               |
| params.user\_list | `Array.<number>` | List of group members |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncLeave(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncleave" id="module_groupmanage__asyncleave"></a>

Quit group

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | Parameter   |
| params.group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateDisplayName(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdatedisplayname" id="module_groupmanage__asyncupdatedisplayname"></a>

Modify group profile

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param            | Type     | Description      |
| ---------------- | -------- | ---------------- |
| params           | `object` | Parameter        |
| params.group\_id | `number` | GroupID          |
| params.value     | `string` | New user profile |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asncGetApplicationList(params) ⇒ `Promise.<Array.<module:types~GroupApplication>>` <a href="#module_groupmanage__asncgetapplicationlist" id="module_groupmanage__asncgetapplicationlist"></a>

Get the list of group membership requests

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupApplication>>` - List of group applications

| Param              | Type             | Description    |
| ------------------ | ---------------- | -------------- |
| params             | `object`         | Parameter      |
| params.group\_list | `Array.<number>` | List of groups |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetFileList(params) ⇒ `Promise.<Array.<module:types~GroupSharedFile>>` <a href="#module_groupmanage__asyncgetfilelist" id="module_groupmanage__asyncgetfilelist"></a>

Get the list of group files

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupSharedFile>>` - List of group files

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | Parameter   |
| params.group\_id | `number` | GroupID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncFileDelete(params) ⇒ `Promise.<Array.<module:types~GroupSharedFileResponse>>` <a href="#module_groupmanage__asyncfiledelete" id="module_groupmanage__asyncfiledelete"></a>

Delete group file

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupSharedFileResponse>>` - List of results

| Param             | Type             | Description      |
| ----------------- | ---------------- | ---------------- |
| params            | `object`         | Parameter        |
| params.group\_id  | `number`         | GroupID          |
| params.file\_list | `Array.<number>` | List of file IDs |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncFileUpload(params) ⇒ `Promise.<Array.<module:types~GroupSharedFile>>` <a href="#module_groupmanage__asyncfileupload" id="module_groupmanage__asyncfileupload"></a>

Upload group file

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupSharedFile>>` - List of group files

| Param            | Type     | Description     |
| ---------------- | -------- | --------------- |
| params           | `object` | Parameter       |
| params.group\_id | `number` | Group id,int64  |
| params.name      | `string` | File name       |
| params.size      | `number` | File size,int64 |
| params.type      | `string` | File type       |
| params.url       | `string` | File url        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>
```
