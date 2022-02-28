# rosterManage
## rosterManage {#module_rostermanage}
好友管理


* [rosterManage](#module_rostermanage)
    * [.asyncGetRosterIdList(force)](#module_rostermanage.asyncgetrosteridlist) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code>
    * [.asyncGetRosterInfo(roster_id, force)](#module_rostermanage.asyncgetrosterinfo) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem)
    * [.asyncRegester(opt)](#module_rostermanage.asyncregester) ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types..usersettings)
    * [.asyncDeleteRoster(param)](#module_rostermanage.asyncdeleteroster) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asnycGetRosterListDetailByIds(roster_ids)](#module_rostermanage.asnycgetrosterlistdetailbyids) ⇒ <code>Promise.&lt;Array.&lt;module:types~RosterItem&gt;&gt;</code>
    * [.getAllRosterDetail()](#module_rostermanage.getallrosterdetail) ⇒ [<code>Array.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem)
    * [.asyncGetUserProfile(force)](#module_rostermanage.asyncgetuserprofile) ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types..userprofile)
    * [.getRosterMessageByRid(uid)](#module_rostermanage.getrostermessagebyrid) ⇒ [<code>Array.&lt;Meta&gt;</code>](types.md#module_types..meta)
    * [.readRosterMessage(roster_id, mid)](#module_rostermanage.readrostermessage)
    * [.recallMessage(uid, mid)](#module_rostermanage.recallmessage)
    * [.unreadMessage(uid, mid)](#module_rostermanage.unreadmessage)
    * [.deleteMessage(uid, mid)](#module_rostermanage.deletemessage)
    * [.getRosterInfo(rid)](#module_rostermanage.getrosterinfo) ⇒ [<code>RosterItem</code>](types.md#module_types..rosteritem)
    * [.getUnreadCount(uid)](#module_rostermanage.getunreadcount) ⇒ <code>number</code>
    * [.asyncGetApplyList(params)](#module_rostermanage.asyncgetapplylist) ⇒ <code>Promise.&lt;Array.&lt;module:types~RosterApplication&gt;&gt;</code>
    * [.asyncGetBlockedlist(params)](#module_rostermanage.asyncgetblockedlist) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code>
    * [.asyncBlockeAdd(params)](#module_rostermanage.asyncblockeadd) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncBlockeRemove(params)](#module_rostermanage.asyncblockeremove) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncApply(params)](#module_rostermanage.asyncapply) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncAccept(params)](#module_rostermanage.asyncaccept) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncDecline(params)](#module_rostermanage.asyncdecline) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateRosterExt(params)](#module_rostermanage.asyncupdaterosterext) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncSearchRosterByName(params)](#module_rostermanage.asyncsearchrosterbyname) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem)
    * [.asyncSearchRosterById(params)](#module_rostermanage.asyncsearchrosterbyid) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem)

### rosterManage.asyncGetRosterIdList(force) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> {#module_rostermanage.asyncgetrosteridlist}
获取好友id列表

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> - 用户ID列表  

| Param | Type | Description |
| --- | --- | --- |
| force | <code>boolean</code> | 是否强制从服务器拉取：true - 从服务器获取， false - 从本地存储获取 |

### rosterManage.asyncGetRosterInfo(roster_id, force) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) {#module_rostermanage.asyncgetrosterinfo}
获取好友信息

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) - 好友信息  

| Param | Type | Description |
| --- | --- | --- |
| roster_id | <code>number</code> | 好友ID |
| force | <code>boolean</code> | 是否强制从服务器拉取： true - 从服务器拉取， false - 优先从本地存储获取 |

### rosterManage.asyncRegester(opt) ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types..usersettings) {#module_rostermanage.asyncregester}
用户注册

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types..usersettings) - 用户设置  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> | 用户信息 |
| opt.username | <code>string</code> | 用户名 |
| opt.password | <code>string</code> | 密码 |

### rosterManage.asyncDeleteRoster(param) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncdeleteroster}
删除好友

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 请求结果  

| Param | Type | Description |
| --- | --- | --- |
| param | <code>object</code> | 参数 |
| param.user_id | <code>number</code> | 好友的用户ID |

### rosterManage.asnycGetRosterListDetailByIds(roster_ids) ⇒ <code>Promise.&lt;Array.&lt;module:types~RosterItem&gt;&gt;</code> {#module_rostermanage.asnycgetrosterlistdetailbyids}
根据id列表获取用户详细信息

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~RosterItem&gt;&gt;</code> - 用户详细信息列表  

| Param | Type | Description |
| --- | --- | --- |
| roster_ids | <code>Array.&lt;number&gt;</code> | 用户ID列表 |

### rosterManage.getAllRosterDetail() ⇒ [<code>Array.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) {#module_rostermanage.getallrosterdetail}
获取缓存的所有用户详细信息

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Array.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) - 用户详细信息列表  
### rosterManage.asyncGetUserProfile(force) ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types..userprofile) {#module_rostermanage.asyncgetuserprofile}
获取自己的用户信息

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types..userprofile) - 用户信息  

| Param | Type | Description |
| --- | --- | --- |
| force | <code>boolean</code> | 是否强制从服务器拉取： true - 从服务器拉取， false - 优先从本地存储获取 |

### rosterManage.getRosterMessageByRid(uid) ⇒ [<code>Array.&lt;Meta&gt;</code>](types.md#module_types..meta) {#module_rostermanage.getrostermessagebyrid}
根据会话ID获取聊天消息

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Array.&lt;Meta&gt;</code>](types.md#module_types..meta) - 聊天消息列表  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | 会话ID |

### rosterManage.readRosterMessage(roster_id, mid) {#module_rostermanage.readrostermessage}
修改消息状态为已读

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  

| Param | Type | Description |
| --- | --- | --- |
| roster_id | <code>number</code> | 会话ID |
| mid | <code>number</code> | 消息ID |

### rosterManage.recallMessage(uid, mid) {#module_rostermanage.recallmessage}
撤回消息，只能撤回5分钟内的

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | 会话ID |
| mid | <code>number</code> | 消息ID |

### rosterManage.unreadMessage(uid, mid) {#module_rostermanage.unreadmessage}
设置消息成未读

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | 会话ID |
| mid | <code>number</code> | 消息ID |

### rosterManage.deleteMessage(uid, mid) {#module_rostermanage.deletemessage}
删除消息

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | 会话ID |
| mid | <code>number</code> | 消息ID |

### rosterManage.getRosterInfo(rid) ⇒ [<code>RosterItem</code>](types.md#module_types..rosteritem) {#module_rostermanage.getrosterinfo}
获取好友信息

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>RosterItem</code>](types.md#module_types..rosteritem) - 好友信息  

| Param | Type | Description |
| --- | --- | --- |
| rid | <code>number</code> | 好友ID |

### rosterManage.getUnreadCount(uid) ⇒ <code>number</code> {#module_rostermanage.getunreadcount}
获取指定会话的未读数

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>number</code> - 未读数  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | 会话IID |

### rosterManage.asyncGetApplyList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~RosterApplication&gt;&gt;</code> {#module_rostermanage.asyncgetapplylist}
获取好友申请列表

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~RosterApplication&gt;&gt;</code> - 好友申请列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.cursor | <code>number</code> | 从哪开始获取：可以传空字符串表示从头开始取 |

### rosterManage.asyncGetBlockedlist(params) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> {#module_rostermanage.asyncgetblockedlist}
获取黑名单

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> - 用户ID列表  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数：空对象 |

### rosterManage.asyncBlockeAdd(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncblockeadd}
加入黑名单

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.user_id | <code>number</code> | 用户ID |

### rosterManage.asyncBlockeRemove(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncblockeremove}
移除黑名单

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.user_id | <code>number</code> | 用户ID |

### rosterManage.asyncApply(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncapply}
请求加为好友

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.user_id | <code>number</code> | 用户ID |
| params.alias | <code>string</code> | 备注 |

### rosterManage.asyncAccept(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncaccept}
通过好友申请

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.user_id | <code>number</code> | 用户ID |

### rosterManage.asyncDecline(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncdecline}
拒绝好友申请

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.user_id | <code>number</code> | 用户ID |

### rosterManage.asyncUpdateRosterExt(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncupdaterosterext}
修改好友扩展字段

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.user_id | <code>number</code> | 用户ID |
| params.ext | <code>string</code> | 扩展字段 |

### rosterManage.asyncSearchRosterByName(params) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) {#module_rostermanage.asyncsearchrosterbyname}
按名称搜索用户

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) - 用户信息  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.username | <code>string</code> | 用户名 |

### rosterManage.asyncSearchRosterById(params) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) {#module_rostermanage.asyncsearchrosterbyid}
按ID搜索用户

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) - 用户信息  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.user_id | <code>number</code> | 用户ID |
