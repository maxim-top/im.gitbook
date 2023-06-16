# rosterManage
## rosterManage {#module_rostermanage}
Friend management


* [rosterManage](#module_rostermanage)
    * [.asyncGetRosterIdList(force)](#module_rostermanage__asyncgetrosteridlist) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code>
    * [.asyncGetRosterInfo(roster_id, force)](#module_rostermanage__asyncgetrosterinfo) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types__rosteritem)
    * [.asyncDeleteRoster(param)](#module_rostermanage__asyncdeleteroster) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asnycGetRosterListDetailByIds(roster_ids)](#module_rostermanage__asnycgetrosterlistdetailbyids) ⇒ <code>Promise.&lt;Array.&lt;module:types~RosterItem&gt;&gt;</code>
    * [.getAllRosterDetail()](#module_rostermanage__getallrosterdetail) ⇒ [<code>Array.&lt;RosterItem&gt;</code>](types.md#module_types__rosteritem)
    * [.asyncGetUserProfile(force)](#module_rostermanage__asyncgetuserprofile) ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types__userprofile)
    * [.getRosterMessageByRid(uid)](#module_rostermanage__getrostermessagebyrid) ⇒ [<code>Array.&lt;Meta&gt;</code>](types.md#module_types__meta)
    * [.readRosterMessage(roster_id, mid)](#module_rostermanage__readrostermessage)
    * [.recallMessage(uid, mid)](#module_rostermanage__recallmessage)
    * [.unreadMessage(uid, mid)](#module_rostermanage__unreadmessage)
    * [.deleteMessage(uid, mid)](#module_rostermanage__deletemessage)
    * [.getRosterInfo(rid)](#module_rostermanage__getrosterinfo) ⇒ [<code>RosterItem</code>](types.md#module_types__rosteritem)
    * [.getUnreadCount(uid)](#module_rostermanage__getunreadcount) ⇒ <code>number</code>
    * [.asyncGetApplyList(params)](#module_rostermanage__asyncgetapplylist) ⇒ <code>Promise.&lt;Array.&lt;module:types~RosterApplication&gt;&gt;</code>
    * [.asyncGetBlockedlist(params)](#module_rostermanage__asyncgetblockedlist) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code>
    * [.asyncBlockeAdd(params)](#module_rostermanage__asyncblockeadd) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncBlockeRemove(params)](#module_rostermanage__asyncblockeremove) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncApply(params)](#module_rostermanage__asyncapply) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncAccept(params)](#module_rostermanage__asyncaccept) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncDecline(params)](#module_rostermanage__asyncdecline) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateRosterExt(params)](#module_rostermanage__asyncupdaterosterext) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncSearchRosterByName(params)](#module_rostermanage__asyncsearchrosterbyname) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types__rosteritem)
    * [.asyncSearchRosterById(params)](#module_rostermanage__asyncsearchrosterbyid) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types__rosteritem)

### rosterManage.asyncGetRosterIdList(force) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> {#module_rostermanage__asyncgetrosteridlist}
Get friend id list

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> - List of user IDs  

| Param | Type | Description |
| --- | --- | --- |
| force | <code>boolean</code> | Whether to force pull from server: true - pull from server, false - pull from local storage |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncGetRosterIdList" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncGetRosterInfo(roster_id, force) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types__rosteritem) {#module_rostermanage__asyncgetrosterinfo}
Get friend information

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types__rosteritem) - Friend info  

| Param | Type | Description |
| --- | --- | --- |
| roster_id | <code>number</code> | Friend ID |
| force | <code>boolean</code> | Whether to force pull from server: true - pull from server, false - prefer to pull from local storage |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncGetRosterInfo" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncDeleteRoster(param) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage__asyncdeleteroster}
Delete friend

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Request results  

| Param | Type | Description |
| --- | --- | --- |
| param | <code>object</code> | Parameter |
| param.user_id | <code>number</code> | Friend's user ID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncDeleteRoster" %}{% endlanying_code_snippet %}
```
### rosterManage.asnycGetRosterListDetailByIds(roster_ids) ⇒ <code>Promise.&lt;Array.&lt;module:types~RosterItem&gt;&gt;</code> {#module_rostermanage__asnycgetrosterlistdetailbyids}
Get user details by id list

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~RosterItem&gt;&gt;</code> - List of user details  

| Param | Type | Description |
| --- | --- | --- |
| roster_ids | <code>Array.&lt;number&gt;</code> | List of user IDs |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asnycGetRosterListDetailByIds" %}{% endlanying_code_snippet %}
```
### rosterManage.getAllRosterDetail() ⇒ [<code>Array.&lt;RosterItem&gt;</code>](types.md#module_types__rosteritem) {#module_rostermanage__getallrosterdetail}
Get all cached user details

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Array.&lt;RosterItem&gt;</code>](types.md#module_types__rosteritem) - List of user details  
**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="getAllRosterDetail" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncGetUserProfile(force) ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types__userprofile) {#module_rostermanage__asyncgetuserprofile}
Get your own user info

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types__userprofile) - User information  

| Param | Type | Description |
| --- | --- | --- |
| force | <code>boolean</code> | Whether to force pull from server: true - pull from server, false - prefer to pull from local storage |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncGetUserProfile" %}{% endlanying_code_snippet %}
```
### rosterManage.getRosterMessageByRid(uid) ⇒ [<code>Array.&lt;Meta&gt;</code>](types.md#module_types__meta) {#module_rostermanage__getrostermessagebyrid}
Get chat messages based-on session ID

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Array.&lt;Meta&gt;</code>](types.md#module_types__meta) - List of chat messages  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | SessionID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="getRosterMessageByRid" %}{% endlanying_code_snippet %}
```
### rosterManage.readRosterMessage(roster_id, mid) {#module_rostermanage__readrostermessage}
Modify message status to read

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  

| Param | Type | Description |
| --- | --- | --- |
| roster_id | <code>number</code> | SessionID |
| mid | <code>number</code> | MessageID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="readRosterMessage" %}{% endlanying_code_snippet %}
```
### rosterManage.recallMessage(uid, mid) {#module_rostermanage__recallmessage}
Revoke a message, only valid for last 5 minutes

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | SessionID |
| mid | <code>number</code> | MessageID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="recallMessage" %}{% endlanying_code_snippet %}
```
### rosterManage.unreadMessage(uid, mid) {#module_rostermanage__unreadmessage}
Set message to unread

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | SessionID |
| mid | <code>number</code> | MessageID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="unreadMessage" %}{% endlanying_code_snippet %}
```
### rosterManage.deleteMessage(uid, mid) {#module_rostermanage__deletemessage}
Delete message

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | SessionID |
| mid | <code>number</code> | MessageID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="deleteMessage" %}{% endlanying_code_snippet %}
```
### rosterManage.getRosterInfo(rid) ⇒ [<code>RosterItem</code>](types.md#module_types__rosteritem) {#module_rostermanage__getrosterinfo}
Get friend information

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>RosterItem</code>](types.md#module_types__rosteritem) - Friend info  

| Param | Type | Description |
| --- | --- | --- |
| rid | <code>number</code> | Friend ID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="getRosterInfo" %}{% endlanying_code_snippet %}
```
### rosterManage.getUnreadCount(uid) ⇒ <code>number</code> {#module_rostermanage__getunreadcount}
Get the number of unread messages for a given conversation

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>number</code> - Number of unreads  

| Param | Type | Description |
| --- | --- | --- |
| uid | <code>number</code> | SessionID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="getUnreadCount" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncGetApplyList(params) ⇒ <code>Promise.&lt;Array.&lt;module:types~RosterApplication&gt;&gt;</code> {#module_rostermanage__asyncgetapplylist}
Get friend request list

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;Array.&lt;module:types~RosterApplication&gt;&gt;</code> - List of friend requests  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.cursor | <code>number</code> | Get from where: you can pass an empty string to get from the beginning |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncGetApplyList" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncGetBlockedlist(params) ⇒ <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> {#module_rostermanage__asyncgetblockedlist}
Get blacklist

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;Array.&lt;number&gt;&gt;</code> - List of user IDs  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter:Empty object |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncGetBlockedlist" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncBlockeAdd(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage__asyncblockeadd}
Add to blacklist

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncBlockeAdd" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncBlockeRemove(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage__asyncblockeremove}
Remove blacklist

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncBlockeRemove" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncApply(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage__asyncapply}
Request to add friend

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |
| params.alias | <code>string</code> | Comment |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncApply" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncAccept(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage__asyncaccept}
Approve add-friend request

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncAccept" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncDecline(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage__asyncdecline}
Reject friend request

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncDecline" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncUpdateRosterExt(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_rostermanage__asyncupdaterosterext}
Modify the Friend extension field

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |
| params.ext | <code>string</code> | Extension field |
| params.alias | <code>string</code> | Name in comment |
| params.mute_notification | <code>boolean</code> | Whether to receive message alert |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncUpdateRosterExt" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncSearchRosterByName(params) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types__rosteritem) {#module_rostermanage__asyncsearchrosterbyname}
Search for user by name

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types__rosteritem) - User information  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.username | <code>string</code> | Username |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncSearchRosterByName" %}{% endlanying_code_snippet %}
```
### rosterManage.asyncSearchRosterById(params) ⇒ [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types__rosteritem) {#module_rostermanage__asyncsearchrosterbyid}
Search for user by ID

**Kind**: static method of [<code>rosterManage</code>](#module_rostermanage)  
**Returns**: [<code>Promise.&lt;RosterItem&gt;</code>](types.md#module_types__rosteritem) - User information  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.user_id | <code>number</code> | User ID |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rosterManage",function="asyncSearchRosterById" %}{% endlanying_code_snippet %}
```