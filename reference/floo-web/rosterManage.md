# rosterManage
## rosterManage {#module_rostermanage}
Friend management


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
Get friend id list

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> - List of user IDs  

| Param | Type | Description |
| --- | --- | --- |
| force | <code>boolean</code> | Whether to force pull from server: true - pull from server, false - pull from local storage |

### rosterManage.asyncGetRosterInfo(roster_id, force) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) {#module_rostermanage.asyncgetrosterinfo}
Get friend information

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) - Friend info  

| Param | Type | Description |
| --- | --- | --- |
| roster_id | <code>number</code> | Friend ID |
| force | <code>boolean</code> | Whether to force pull from server: true - pull from server, false - prefer to pull from local storage |

### rosterManage.asyncRegester(opt) ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types..usersettings) {#module_rostermanage.asyncregester}
User registeration

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types..usersettings) - User settings  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> | User information |
| opt.username | <code>string</code> | Username |
| opt.password | <code>string</code> | Password |

### rosterManage.asyncDeleteRoster(param) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncdeleteroster}
Delete friend

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Request results  

| Param | Type | Description |
| --- | --- | --- |
| param | <code>object</code> | Parameter |
| param.user_id | <code>number</code> | Friend's user ID |

### rosterManage.asnycGetRosterListDetailByIds(roster_ids) ⇒ <code>Promise.&lt;Array.&lt;module:types~RosterItem&gt;&gt;</code> {#module_rostermanage.asnycgetrosterlistdetailbyids}
Get user details by id list

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~RosterItem&gt;&gt;</code> - List of user details  

| Param | Type | Description |
| --- | --- | --- |
| roster_ids | <code>Array.&lt;number&gt;</code> | List of user IDs |

### rosterManage.getAllRosterDetail() ⇒ [<code>Array.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) {#module_rostermanage.getallrosterdetail}
Get all cached user details

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Array.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) - List of user details  
### rosterManage.asyncGetUserProfile(force) ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types..userprofile) {#module_rostermanage.asyncgetuserprofile}
Get your own user info

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types..userprofile) - User information  

| Param | Type | Description |
| --- | --- | --- |
| force | <code>boolean</code> | Whether to force pull from server: true - pull from server, false - prefer to pull from local storage |

### rosterManage.getRosterMessageByRid(uid) ⇒ [<code>Array.&lt;Meta&gt;</code>](types.md#module_types..meta) {#module_rostermanage.getrostermessagebyrid}
Get chat messages based-on session ID

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Array.&lt;Meta&gt;</code>](types.md#module_types..meta) - List of chat messages  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | SessionID |

### rosterManage.readRosterMessage(roster_id, mid) {#module_rostermanage.readrostermessage}
Modify message status to read

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  

| Param | Type | Description |
| --- | --- | --- |
| roster_id | <code>number</code> | SessionID |
| mid | <code>number</code> | MessageID |

### rosterManage.recallMessage(uid, mid) {#module_rostermanage.recallmessage}
Revoke a message, only valid for last 5 minutes

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | SessionID |
| mid | <code>number</code> | MessageID |

### rosterManage.unreadMessage(uid, mid) {#module_rostermanage.unreadmessage}
Set message to unread

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | SessionID |
| mid | <code>number</code> | MessageID |

### rosterManage.deleteMessage(uid, mid) {#module_rostermanage.deletemessage}
Delete message

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | SessionID |
| mid | <code>number</code> | MessageID |

### rosterManage.getRosterInfo(rid) ⇒ [<code>RosterItem</code>](types.md#module_types..rosteritem) {#module_rostermanage.getrosterinfo}
Get friend information

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>RosterItem</code>](types.md#module_types..rosteritem) - Friend info  

| Param | Type | Description |
| --- | --- | --- |
| rid | <code>number</code> | Friend ID |

### rosterManage.getUnreadCount(uid) ⇒ <code>number</code> {#module_rostermanage.getunreadcount}
Get the number of unread messages for a given conversation

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>number</code> - Number of unreads  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | SessionIID |

### rosterManage.asyncGetApplyList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~RosterApplication&gt;&gt;</code> {#module_rostermanage.asyncgetapplylist}
Get friend request list

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~RosterApplication&gt;&gt;</code> - List of friend requests  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.cursor | <code>number</code> | Get from where: you can pass an empty string to get from the beginning |

### rosterManage.asyncGetBlockedlist(params) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> {#module_rostermanage.asyncgetblockedlist}
Get blacklist

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> - List of user IDs  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter:Empty object |

### rosterManage.asyncBlockeAdd(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncblockeadd}
Add to blacklist

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |

### rosterManage.asyncBlockeRemove(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncblockeremove}
Remove blacklist

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |

### rosterManage.asyncApply(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncapply}
Request to add friend

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |
| params.alias | <code>string</code> | Comment |

### rosterManage.asyncAccept(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncaccept}
Approve add-friend request

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |

### rosterManage.asyncDecline(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncdecline}
Reject friend request

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |

### rosterManage.asyncUpdateRosterExt(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage.asyncupdaterosterext}
Modify the Friend extension field

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |
| params.ext | <code>string</code> | Extension field |

### rosterManage.asyncSearchRosterByName(params) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) {#module_rostermanage.asyncsearchrosterbyname}
Search for user by name

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) - User information  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.username | <code>string</code> | Username |

### rosterManage.asyncSearchRosterById(params) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) {#module_rostermanage.asyncsearchrosterbyid}
Search for user by ID

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types..rosteritem) - User information  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |
