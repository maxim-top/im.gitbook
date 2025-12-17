# groupManage

## groupManage <a href="#module_groupmanage" id="module_groupmanage"></a>

群管理

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
  * [.appendMessageContent(uid, mid, content)](groupManage.md#module_groupmanage__appendmessagecontent)
  * [.replaceMessage(uid, mid, content, config, ext)](groupManage.md#module_groupmanage__replacemessage)
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

获取群信息

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) - 群信息

| Param     | Type      | Description                                  |
| --------- | --------- | -------------------------------------------- |
| group\_id | `number`  | 群ID                                          |
| froce     | `boolean` | 是否强制从服务器拉取： true - 从服务器拉取， false - 优先从本地存储获取 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetJoinedGroups(froce) ⇒ `Promise.<Array.<number>>` <a href="#module_groupmanage__asyncgetjoinedgroups" id="module_groupmanage__asyncgetjoinedgroups"></a>

获取加入的群组

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<number>>` - 群组ID列表

| Param | Type      | Description                                  |
| ----- | --------- | -------------------------------------------- |
| froce | `boolean` | 是否强制从服务器拉取： true - 从服务器拉取， false - 优先从本地存储获取 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.openGroup(group\_id) <a href="#module_groupmanage__opengroup" id="module_groupmanage__opengroup"></a>

打开群组， 此方法会准备群组聊天界面的一些必备信息。

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)

| Param     | Type     | Description |
| --------- | -------- | ----------- |
| group\_id | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.getAllGroupDetail() ⇒ `Object.<number, module:types~GroupInfoAndSettings>` <a href="#module_groupmanage__getallgroupdetail" id="module_groupmanage__getallgroupdetail"></a>

获取缓存的所有群组详情

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Object.<number, module:types~GroupInfoAndSettings>` - 群组详情\
**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetGroupMembers(group\_id) ⇒ `Promise.<Array.<number>>` <a href="#module_groupmanage__asyncgetgroupmembers" id="module_groupmanage__asyncgetgroupmembers"></a>

获取群组成员ID列表（异步）

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<number>>` - 群成员ID列表

| Param     | Type     | Description |
| --------- | -------- | ----------- |
| group\_id | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.getGroupMembers(group\_id) ⇒ [`Array.<GroupMember>`](types.md#module_types__groupmember) <a href="#module_groupmanage__getgroupmembers" id="module_groupmanage__getgroupmembers"></a>

获取群组成员（同步）

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Array.<GroupMember>`](types.md#module_types__groupmember) - 群成员列表

| Param     | Type     | Description |
| --------- | -------- | ----------- |
| group\_id | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetGroupListDetail(gids) ⇒ `Promise.<Array.<module:types~BriefGroupInfoAndSettings>>` <a href="#module_groupmanage__asyncgetgrouplistdetail" id="module_groupmanage__asyncgetgrouplistdetail"></a>

按id获取群组详情

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~BriefGroupInfoAndSettings>>` - 群组详情列表

| Param | Type             | Description |
| ----- | ---------------- | ----------- |
| gids  | `Array.<number>` | 群组ID列表      |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.getGruopMessage(gid) ⇒ [`Array.<Meta>`](types.md#module_types__meta) <a href="#module_groupmanage__getgruopmessage" id="module_groupmanage__getgruopmessage"></a>

获取群消息

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Array.<Meta>`](types.md#module_types__meta) - 群消息列表

| Param | Type     | Description |
| ----- | -------- | ----------- |
| gid   | `number` | 群ID         |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetInfo(params) ⇒ [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) <a href="#module_groupmanage__asyncgetinfo" id="module_groupmanage__asyncgetinfo"></a>

获取群组详情

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) - 群组详情

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetMemberList(param) ⇒ `Promise.<Array.<module:types~GroupMember>>` <a href="#module_groupmanage__asyncgetmemberlist" id="module_groupmanage__asyncgetmemberlist"></a>

获取群成员列表

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupMember>>` - 群成员列表

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| param            | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.readGroupMessage(group\_id, mid) <a href="#module_groupmanage__readgroupmessage" id="module_groupmanage__readgroupmessage"></a>

将群消息设置已读

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)

| Param     | Type     | Description |
| --------- | -------- | ----------- |
| group\_id | `number` | 群组ID        |
| mid       | `number` | 消息ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.recallMessage(uid, mid) <a href="#module_groupmanage__recallmessage" id="module_groupmanage__recallmessage"></a>

撤回消息

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)

| Param | Type     | Description |
| ----- | -------- | ----------- |
| uid   | `number` | 群组ID        |
| mid   | `number` | 消息ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.appendMessageContent(uid, mid, content) <a href="#module_groupmanage__appendmessagecontent" id="module_groupmanage__appendmessagecontent"></a>

追加消息内容

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)

| Param   | Type     | Description |
| ------- | -------- | ----------- |
| uid     | `number` | 会话ID        |
| mid     | `number` | 消息ID        |
| content | `string` | 消息追加内容      |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.replaceMessage(uid, mid, content, config, ext) <a href="#module_groupmanage__replacemessage" id="module_groupmanage__replacemessage"></a>

更新消息内容

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)

| Param   | Type                 | Default | Description |
| ------- | -------------------- | ------- | ----------- |
| uid     | `number`             |         | 会话ID        |
| mid     | `number`             |         | 消息ID        |
| content | `string`             |         | 消息更新内容      |
| config  | `string` \| `object` | `null`  | 消息更新配置      |
| ext     | `string` \| `object` | `null`  | 消息更新扩展信息    |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.getUnreadCount(gid) ⇒ `number` <a href="#module_groupmanage__getunreadcount" id="module_groupmanage__getunreadcount"></a>

获取群未读消息数

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `number` - 未读消息数

| Param | Type     | Description |
| ----- | -------- | ----------- |
| gid   | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetAdminList(params) ⇒ `Promise.<Array.<module:types~GroupMember>>` <a href="#module_groupmanage__asyncgetadminlist" id="module_groupmanage__asyncgetadminlist"></a>

获取群管理员列表

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupMember>>` - 群管理员列表

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncAdminAdd(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncadminadd" id="module_groupmanage__asyncadminadd"></a>

群添加管理员

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - 结果列表

| Param             | Type             | Description |
| ----------------- | ---------------- | ----------- |
| params            | `object`         | 参数          |
| params.group\_id  | `number`         | 群组ID        |
| params.user\_list | `Array.<number>` | 群成员列表       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncAdminRemove(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncadminremove" id="module_groupmanage__asyncadminremove"></a>

移除管理员

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - 结果列表

| Param             | Type             | Description |
| ----------------- | ---------------- | ----------- |
| params            | `object`         | 参数          |
| params.group\_id  | `number`         | 群组ID        |
| params.user\_list | `Array.<number>` | 群成员列表       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetAnouncementById(params) ⇒ [`Promise.<GroupAnnouncement>`](types.md#module_types__groupannouncement) <a href="#module_groupmanage__asyncgetanouncementbyid" id="module_groupmanage__asyncgetanouncementbyid"></a>

获取群公告详情

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupAnnouncement>`](types.md#module_types__groupannouncement) - 群公告详情

| Param                   | Type             | Description |
| ----------------------- | ---------------- | ----------- |
| params                  | `object`         | 参数          |
| params.group\_id        | `number`         | 群组ID        |
| params.announcement\_id | `Array.<number>` | 公告ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncAnouncementDelete(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncanouncementdelete" id="module_groupmanage__asyncanouncementdelete"></a>

删除群公告

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param                   | Type             | Description |
| ----------------------- | ---------------- | ----------- |
| params                  | `object`         | 参数          |
| params.group\_id        | `number`         | 群组ID        |
| params.announcement\_id | `Array.<number>` | 公告ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncAnnouncementEdit(params) ⇒ [`Promise.<GroupAnnouncement>`](types.md#module_types__groupannouncement) <a href="#module_groupmanage__asyncannouncementedit" id="module_groupmanage__asyncannouncementedit"></a>

编辑群公告

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupAnnouncement>`](types.md#module_types__groupannouncement) - 群公告详情

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |
| params.title     | `string` | 公告标题        |
| params.content   | `string` | 公告内容        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetAnnouncementList(params) ⇒ `Promise.<Array.<module:types~GroupAnnouncement>>` <a href="#module_groupmanage__asyncgetannouncementlist" id="module_groupmanage__asyncgetannouncementlist"></a>

群公告列表

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupAnnouncement>>` - 群公告详情列表

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncCreate(params) ⇒ [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) <a href="#module_groupmanage__asynccreate" id="module_groupmanage__asynccreate"></a>

创建群组

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) - 群详情

| Param  | Type                                                          | Description |
| ------ | ------------------------------------------------------------- | ----------- |
| params | [`GroupInfoRequest`](types.md#module_types__groupinforequest) | 请求参数        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncDestroy(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncdestroy" id="module_groupmanage__asyncdestroy"></a>

解散群组

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateAvatar(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdateavatar" id="module_groupmanage__asyncupdateavatar"></a>

更新群头像

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |
| params.value     | `string` | 头像地址        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateDescription(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdatedescription" id="module_groupmanage__asyncupdatedescription"></a>

更新群描述

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |
| params.value     | `string` | 群组描述        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateExt(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdateext" id="module_groupmanage__asyncupdateext"></a>

更新群扩展信息

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |
| params.value     | `string` | 扩展信息        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateName(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdatename" id="module_groupmanage__asyncupdatename"></a>

更新群名称

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |
| params.value     | `string` | 群名称         |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupMsgMutemode(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncgroupmsgmutemode" id="module_groupmanage__asyncgroupmsgmutemode"></a>

设置群消息免打扰情况

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param                  | Type     | Description                                          |
| ---------------------- | -------- | ---------------------------------------------------- |
| params                 | `object` | 参数                                                   |
| params.group\_id       | `number` | 群组ID                                                 |
| params.msg\_mute\_mode | `number` | 群消息屏蔽模式: 0 - 表示不屏蔽, 1 - 表示屏蔽本地消息通知, 2 - 表示屏蔽消息，不接收消息 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupBannedList(params) ⇒ `Promise.<Array.<module:types~GroupMemberBanned>>` <a href="#module_groupmanage__asyncgroupbannedlist" id="module_groupmanage__asyncgroupbannedlist"></a>

获取群禁言列表

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupMemberBanned>>` - 禁言成员列表

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupBab(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncgroupbab" id="module_groupmanage__asyncgroupbab"></a>

禁言群成员

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - 请求结果列表

| Param  | Type                                                                          | Description |
| ------ | ----------------------------------------------------------------------------- | ----------- |
| params | [`GroupBannedMemberRequest`](types.md#module_types__groupbannedmemberrequest) | 请求参数        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupUnban(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncgroupunban" id="module_groupmanage__asyncgroupunban"></a>

解除成员禁言

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - 请求结果列表

| Param             | Type             | Description |
| ----------------- | ---------------- | ----------- |
| params            | `object`         | 参数          |
| params.group\_id  | `number`         | 群组ID        |
| params.user\_list | `Array.<number>` | 群成员列表       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetSettings(group\_id) ⇒ [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) <a href="#module_groupmanage__asyncgetsettings" id="module_groupmanage__asyncgetsettings"></a>

获取群设置

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupInfoAndSettings>`](types.md#module_types__groupinfoandsettings) - 群设置

| Param     | Type     | Description |
| --------- | -------- | ----------- |
| group\_id | `number` | 群ID         |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateAllowMemberInvitation(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdateallowmemberinvitation" id="module_groupmanage__asyncupdateallowmemberinvitation"></a>

设置群成员是否可以邀请

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type      | Description                             |
| ---------------- | --------- | --------------------------------------- |
| params           | `object`  | 参数                                      |
| params.group\_id | `number`  | 群组ID                                    |
| params.value     | `boolean` | 群成员邀请设置: false - 不允许邀请, true - 允许邀请(默认) |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateAllowMemberModify(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdateallowmembermodify" id="module_groupmanage__asyncupdateallowmembermodify"></a>

设置群成员是否可以修改群信息

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type      | Description                                           |
| ---------------- | --------- | ----------------------------------------------------- |
| params           | `object`  | 参数                                                    |
| params.group\_id | `number`  | 群组ID                                                  |
| params.value     | `boolean` | 群成员修改群信息设置: false - 群成员不能修改群信息(默认), true - 群成员可以修改群信息 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateEnableReadack(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdateenablereadack" id="module_groupmanage__asyncupdateenablereadack"></a>

设置群是否开启已读模式

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type      | Description                         |
| ---------------- | --------- | ----------------------------------- |
| params           | `object`  | 参数                                  |
| params.group\_id | `number`  | 群组ID                                |
| params.value     | `boolean` | 是否开启群消息已读功能: false - 不开启, true - 开启 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateHistoryVisible(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdatehistoryvisible" id="module_groupmanage__asyncupdatehistoryvisible"></a>

设置群历史是否可见

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type      | Description                       |
| ---------------- | --------- | --------------------------------- |
| params           | `object`  | 参数                                |
| params.group\_id | `number`  | 群组ID                              |
| params.value     | `boolean` | 设置群历史是否可见: false - 不可见, true - 可见 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateRequireadminapproval(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdaterequireadminapproval" id="module_groupmanage__asyncupdaterequireadminapproval"></a>

设置入群是否需要申请

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param                  | Type      | Description                           |
| ---------------------- | --------- | ------------------------------------- |
| params                 | `object`  | 参数                                    |
| params.group\_id       | `number`  | 群组ID                                  |
| params.apply\_approval | `boolean` | 入群申请审批设置, 0:同意所有申请 1:需要管理员确认 2:拒绝所有申请 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncBanAll(params) ⇒ [`Promise.<GroupBanAllResponse>`](types.md#module_types__groupbanallresponse) <a href="#module_groupmanage__asyncbanall" id="module_groupmanage__asyncbanall"></a>

全员禁言，只允许管理员发消息

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupBanAllResponse>`](types.md#module_types__groupbanallresponse) - 结果

| Param            | Type     | Description      |
| ---------------- | -------- | ---------------- |
| params           | `object` | 参数               |
| params.duration  | `number` | 禁言时长，单位为分钟,int64 |
| params.group\_id | `number` | 群id,int64        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUnBanAll(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncunbanall" id="module_groupmanage__asyncunbanall"></a>

取消全员禁言

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群id,int64   |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncOwnerTransfer(params) ⇒ [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse) <a href="#module_groupmanage__asyncownertransfer" id="module_groupmanage__asyncownertransfer"></a>

更换群主

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse) - 结果

| Param             | Type     | Description |
| ----------------- | -------- | ----------- |
| params            | `object` | 参数          |
| params.group\_id  | `number` | 群组ID        |
| params.new\_owner | `number` | 新群主的用户ID    |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetUserJoined(params) ⇒ `Promise.<Array.<number>>` <a href="#module_groupmanage__asyncgetuserjoined" id="module_groupmanage__asyncgetuserjoined"></a>

获取用户的群组列表

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<number>>` - 群ID的列表

| Param  | Type     | Description |
| ------ | -------- | ----------- |
| params | `object` | 参数, 空对象     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncApply(params) ⇒ [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse) <a href="#module_groupmanage__asyncapply" id="module_groupmanage__asyncapply"></a>

申请加入群

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse) - 结果

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |
| params.reason    | `string` | 申请入群原因      |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncApplyHandle(params) ⇒ [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse) <a href="#module_groupmanage__asyncapplyhandle" id="module_groupmanage__asyncapplyhandle"></a>

处理用户的入群申请

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: [`Promise.<GroupUserRelationResponse>`](types.md#module_types__groupuserrelationresponse) - 结果

| Param            | Type      | Description           |
| ---------------- | --------- | --------------------- |
| params           | `object`  | 参数                    |
| params.group\_id | `number`  | 群组ID                  |
| params.user\_id  | `number`  | 用户ID                  |
| params.approval  | `boolean` | 审批结果：true为同意，false为拒绝 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupBockedlist(params) ⇒ `Promise.<Array.<module:types~GroupBlockedListItem>>` <a href="#module_groupmanage__asyncgroupbockedlist" id="module_groupmanage__asyncgroupbockedlist"></a>

获取群黑名单

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupBlockedListItem>>` - 群黑名单列表

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupBlock(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncgroupblock" id="module_groupmanage__asyncgroupblock"></a>

将成员加入黑名单

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - 结果列表

| Param             | Type             | Description |
| ----------------- | ---------------- | ----------- |
| params            | `object`         | 参数          |
| params.group\_id  | `number`         | 群组ID        |
| params.user\_list | `Array.<number>` | 群成员列表       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGroupUnblock(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncgroupunblock" id="module_groupmanage__asyncgroupunblock"></a>

解除黑名单

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - 结果列表

| Param             | Type             | Description |
| ----------------- | ---------------- | ----------- |
| params            | `object`         | 参数          |
| params.group\_id  | `number`         | 群组ID        |
| params.user\_list | `Array.<number>` | 群成员列表       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncKick(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asynckick" id="module_groupmanage__asynckick"></a>

踢出群组

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - 结果列表

| Param             | Type             | Description |
| ----------------- | ---------------- | ----------- |
| params            | `object`         | 参数          |
| params.group\_id  | `number`         | 群组ID        |
| params.user\_list | `Array.<number>` | 群成员列表       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetInvitationList() ⇒ `Promise.<Array.<module:types~GroupInvitation>>` <a href="#module_groupmanage__asyncgetinvitationlist" id="module_groupmanage__asyncgetinvitationlist"></a>

获取群邀请列表

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupInvitation>>` - 群邀请列表\
**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncInvite(params) ⇒ `Promise.<Array.<module:types~GroupUserRelationResponse>>` <a href="#module_groupmanage__asyncinvite" id="module_groupmanage__asyncinvite"></a>

邀请成员加入群

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupUserRelationResponse>>` - 结果列表

| Param             | Type             | Description |
| ----------------- | ---------------- | ----------- |
| params            | `object`         | 参数          |
| params.group\_id  | `number`         | 群组ID        |
| params.user\_list | `Array.<number>` | 群成员列表       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncInviteHandle(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncinvitehandle" id="module_groupmanage__asyncinvitehandle"></a>

处理群邀请

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type      | Description           |
| ---------------- | --------- | --------------------- |
| params           | `object`  | 参数                    |
| params.group\_id | `number`  | 群组ID                  |
| params.user\_id  | `number`  | 用户ID                  |
| params.approval  | `boolean` | 审批结果：true为同意，false为拒绝 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetMemberDisplayName(params) ⇒ `Promise.<Array.<module:types~GroupMember>>` <a href="#module_groupmanage__asyncgetmemberdisplayname" id="module_groupmanage__asyncgetmemberdisplayname"></a>

批量获取群成员的群名片

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupMember>>` - 群成员列表

| Param             | Type             | Description |
| ----------------- | ---------------- | ----------- |
| params            | `object`         | 参数          |
| params.group\_id  | `number`         | 群组ID        |
| params.user\_list | `Array.<number>` | 群成员列表       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncLeave(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncleave" id="module_groupmanage__asyncleave"></a>

退出群

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncUpdateDisplayName(params) ⇒ `Promise.<boolean>` <a href="#module_groupmanage__asyncupdatedisplayname" id="module_groupmanage__asyncupdatedisplayname"></a>

修改群名片

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |
| params.value     | `string` | 新名片         |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asncGetApplicationList(params) ⇒ `Promise.<Array.<module:types~GroupApplication>>` <a href="#module_groupmanage__asncgetapplicationlist" id="module_groupmanage__asncgetapplicationlist"></a>

获取群申请列表

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupApplication>>` - 群申请列表

| Param              | Type             | Description |
| ------------------ | ---------------- | ----------- |
| params             | `object`         | 参数          |
| params.group\_list | `Array.<number>` | 群列表         |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncGetFileList(params) ⇒ `Promise.<Array.<module:types~GroupSharedFile>>` <a href="#module_groupmanage__asyncgetfilelist" id="module_groupmanage__asyncgetfilelist"></a>

获取群文件列表

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupSharedFile>>` - 群文件列表

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncFileDelete(params) ⇒ `Promise.<Array.<module:types~GroupSharedFileResponse>>` <a href="#module_groupmanage__asyncfiledelete" id="module_groupmanage__asyncfiledelete"></a>

删除群文件

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupSharedFileResponse>>` - 结果列表

| Param             | Type             | Description |
| ----------------- | ---------------- | ----------- |
| params            | `object`         | 参数          |
| params.group\_id  | `number`         | 群组ID        |
| params.file\_list | `Array.<number>` | 文件ID列表      |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>

```

### groupManage.asyncFileUpload(params) ⇒ `Promise.<Array.<module:types~GroupSharedFile>>` <a href="#module_groupmanage__asyncfileupload" id="module_groupmanage__asyncfileupload"></a>

上传群文件

**Kind**: static method of [`groupManage`](groupManage.md#module_groupmanage)\
**Returns**: `Promise.<Array.<module:types~GroupSharedFile>>` - 群文件列表

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群id,int64   |
| params.name      | `string` | 文件名称        |
| params.size      | `number` | 文件大小,int64  |
| params.type      | `string` | 文件类型        |
| params.url       | `string` | 文件url       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='groupManage'></div>
```
