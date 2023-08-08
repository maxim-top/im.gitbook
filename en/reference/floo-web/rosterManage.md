# rosterManage

## rosterManage <a href="#module_rostermanage" id="module_rostermanage"></a>

Friend management

* [rosterManage](rosterManage.md#module\_rostermanage)
  * [.asyncGetRosterIdList(force)](rosterManage.md#module\_rostermanage\_\_asyncgetrosteridlist) ⇒ `Promise.<Array.<number>>`
  * [.asyncGetRosterInfo(roster\_id, force)](rosterManage.md#module\_rostermanage\_\_asyncgetrosterinfo) ⇒ [`Promise.<RosterItem>`](types.md#module\_types\_\_rosteritem)
  * [.asyncDeleteRoster(param)](rosterManage.md#module\_rostermanage\_\_asyncdeleteroster) ⇒ `Promise.<boolean>`
  * [.asnycGetRosterListDetailByIds(roster\_ids)](rosterManage.md#module\_rostermanage\_\_asnycgetrosterlistdetailbyids) ⇒ `Promise.<Array.<module:types~RosterItem>>`
  * [.getAllRosterDetail()](rosterManage.md#module\_rostermanage\_\_getallrosterdetail) ⇒ [`Array.<RosterItem>`](types.md#module\_types\_\_rosteritem)
  * [.asyncGetUserProfile(force)](rosterManage.md#module\_rostermanage\_\_asyncgetuserprofile) ⇒ [`Promise.<UserProfile>`](types.md#module\_types\_\_userprofile)
  * [.getRosterMessageByRid(uid)](rosterManage.md#module\_rostermanage\_\_getrostermessagebyrid) ⇒ [`Array.<Meta>`](types.md#module\_types\_\_meta)
  * [.readRosterMessage(roster\_id, mid)](rosterManage.md#module\_rostermanage\_\_readrostermessage)
  * [.recallMessage(uid, mid)](rosterManage.md#module\_rostermanage\_\_recallmessage)
  * [.unreadMessage(uid, mid)](rosterManage.md#module\_rostermanage\_\_unreadmessage)
  * [.deleteMessage(uid, mid)](rosterManage.md#module\_rostermanage\_\_deletemessage)
  * [.getRosterInfo(rid)](rosterManage.md#module\_rostermanage\_\_getrosterinfo) ⇒ [`RosterItem`](types.md#module\_types\_\_rosteritem)
  * [.getUnreadCount(uid)](rosterManage.md#module\_rostermanage\_\_getunreadcount) ⇒ `number`
  * [.asyncGetApplyList(params)](rosterManage.md#module\_rostermanage\_\_asyncgetapplylist) ⇒ `Promise.<Array.<module:types~RosterApplication>>`
  * [.asyncGetBlockedlist(params)](rosterManage.md#module\_rostermanage\_\_asyncgetblockedlist) ⇒ `Promise.<Array.<number>>`
  * [.asyncBlockeAdd(params)](rosterManage.md#module\_rostermanage\_\_asyncblockeadd) ⇒ `Promise.<boolean>`
  * [.asyncBlockeRemove(params)](rosterManage.md#module\_rostermanage\_\_asyncblockeremove) ⇒ `Promise.<boolean>`
  * [.asyncApply(params)](rosterManage.md#module\_rostermanage\_\_asyncapply) ⇒ `Promise.<boolean>`
  * [.asyncAccept(params)](rosterManage.md#module\_rostermanage\_\_asyncaccept) ⇒ `Promise.<boolean>`
  * [.asyncDecline(params)](rosterManage.md#module\_rostermanage\_\_asyncdecline) ⇒ `Promise.<boolean>`
  * [.asyncUpdateRosterExt(params)](rosterManage.md#module\_rostermanage\_\_asyncupdaterosterext) ⇒ `Promise.<boolean>`
  * [.asyncSearchRosterByName(params)](rosterManage.md#module\_rostermanage\_\_asyncsearchrosterbyname) ⇒ [`Promise.<RosterItem>`](types.md#module\_types\_\_rosteritem)
  * [.asyncSearchRosterById(params)](rosterManage.md#module\_rostermanage\_\_asyncsearchrosterbyid) ⇒ [`Promise.<RosterItem>`](types.md#module\_types\_\_rosteritem)

### rosterManage.asyncGetRosterIdList(force) ⇒ `Promise.<Array.<number>>` <a href="#module_rostermanage__asyncgetrosteridlist" id="module_rostermanage__asyncgetrosteridlist"></a>

Get friend id list

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: `Promise.<Array.<number>>` - List of user IDs

| Param | Type      | Description                                                                                 |
| ----- | --------- | ------------------------------------------------------------------------------------------- |
| force | `boolean` | Whether to force pull from server: true - pull from server, false - pull from local storage |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncGetRosterInfo(roster\_id, force) ⇒ [`Promise.<RosterItem>`](types.md#module\_types\_\_rosteritem) <a href="#module_rostermanage__asyncgetrosterinfo" id="module_rostermanage__asyncgetrosterinfo"></a>

Get friend information

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: [`Promise.<RosterItem>`](types.md#module\_types\_\_rosteritem) - Friend info

| Param      | Type      | Description                                                                                           |
| ---------- | --------- | ----------------------------------------------------------------------------------------------------- |
| roster\_id | `number`  | Friend ID                                                                                             |
| force      | `boolean` | Whether to force pull from server: true - pull from server, false - prefer to pull from local storage |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncDeleteRoster(param) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncdeleteroster" id="module_rostermanage__asyncdeleteroster"></a>

Delete friend

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: `Promise.<boolean>` - Request results

| Param          | Type     | Description      |
| -------------- | -------- | ---------------- |
| param          | `object` | Parameter        |
| param.user\_id | `number` | Friend's user ID |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asnycGetRosterListDetailByIds(roster\_ids) ⇒ `Promise.<Array.<module:types~RosterItem>>` <a href="#module_rostermanage__asnycgetrosterlistdetailbyids" id="module_rostermanage__asnycgetrosterlistdetailbyids"></a>

Get user details by id list

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: `Promise.<Array.<module:types~RosterItem>>` - List of user details

| Param       | Type             | Description      |
| ----------- | ---------------- | ---------------- |
| roster\_ids | `Array.<number>` | List of user IDs |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.getAllRosterDetail() ⇒ [`Array.<RosterItem>`](types.md#module\_types\_\_rosteritem) <a href="#module_rostermanage__getallrosterdetail" id="module_rostermanage__getallrosterdetail"></a>

Get all cached user details

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: [`Array.<RosterItem>`](types.md#module\_types\_\_rosteritem) - List of user details\
**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncGetUserProfile(force) ⇒ [`Promise.<UserProfile>`](types.md#module\_types\_\_userprofile) <a href="#module_rostermanage__asyncgetuserprofile" id="module_rostermanage__asyncgetuserprofile"></a>

Get your own user info

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: [`Promise.<UserProfile>`](types.md#module\_types\_\_userprofile) - User information

| Param | Type      | Description                                                                                           |
| ----- | --------- | ----------------------------------------------------------------------------------------------------- |
| force | `boolean` | Whether to force pull from server: true - pull from server, false - prefer to pull from local storage |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.getRosterMessageByRid(uid) ⇒ [`Array.<Meta>`](types.md#module\_types\_\_meta) <a href="#module_rostermanage__getrostermessagebyrid" id="module_rostermanage__getrostermessagebyrid"></a>

Get chat messages based-on session ID

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: [`Array.<Meta>`](types.md#module\_types\_\_meta) - List of chat messages

| Param | Type     | Description |
| ----- | -------- | ----------- |
| uid   | `number` | SessionID   |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.readRosterMessage(roster\_id, mid) <a href="#module_rostermanage__readrostermessage" id="module_rostermanage__readrostermessage"></a>

Modify message status to read

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)

| Param      | Type     | Description |
| ---------- | -------- | ----------- |
| roster\_id | `number` | SessionID   |
| mid        | `number` | MessageID   |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.recallMessage(uid, mid) <a href="#module_rostermanage__recallmessage" id="module_rostermanage__recallmessage"></a>

Revoke a message, only valid for last 5 minutes

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)

| Param | Type     | Description |
| ----- | -------- | ----------- |
| uid   | `number` | SessionID   |
| mid   | `number` | MessageID   |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.unreadMessage(uid, mid) <a href="#module_rostermanage__unreadmessage" id="module_rostermanage__unreadmessage"></a>

Set message to unread

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)

| Param | Type     | Description |
| ----- | -------- | ----------- |
| uid   | `number` | SessionID   |
| mid   | `number` | MessageID   |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.deleteMessage(uid, mid) <a href="#module_rostermanage__deletemessage" id="module_rostermanage__deletemessage"></a>

Delete message

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)

| Param | Type     | Description |
| ----- | -------- | ----------- |
| uid   | `number` | SessionID   |
| mid   | `number` | MessageID   |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.getRosterInfo(rid) ⇒ [`RosterItem`](types.md#module\_types\_\_rosteritem) <a href="#module_rostermanage__getrosterinfo" id="module_rostermanage__getrosterinfo"></a>

Get friend information

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: [`RosterItem`](types.md#module\_types\_\_rosteritem) - Friend info

| Param | Type     | Description |
| ----- | -------- | ----------- |
| rid   | `number` | Friend ID   |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.getUnreadCount(uid) ⇒ `number` <a href="#module_rostermanage__getunreadcount" id="module_rostermanage__getunreadcount"></a>

Get the number of unread messages for a given conversation

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: `number` - Number of unreads

| Param | Type     | Description |
| ----- | -------- | ----------- |
| uid   | `number` | SessionID   |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncGetApplyList(params) ⇒ `Promise.<Array.<module:types~RosterApplication>>` <a href="#module_rostermanage__asyncgetapplylist" id="module_rostermanage__asyncgetapplylist"></a>

Get friend request list

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: `Promise.<Array.<module:types~RosterApplication>>` - List of friend requests

| Param         | Type     | Description                                                            |
| ------------- | -------- | ---------------------------------------------------------------------- |
| params        | `object` | Parameter                                                              |
| params.cursor | `number` | Get from where: you can pass an empty string to get from the beginning |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncGetBlockedlist(params) ⇒ `Promise.<Array.<number>>` <a href="#module_rostermanage__asyncgetblockedlist" id="module_rostermanage__asyncgetblockedlist"></a>

Get blacklist

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: `Promise.<Array.<number>>` - List of user IDs

| Param  | Type     | Description            |
| ------ | -------- | ---------------------- |
| params | `object` | Parameter:Empty object |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncBlockeAdd(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncblockeadd" id="module_rostermanage__asyncblockeadd"></a>

Add to blacklist

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | Parameter   |
| params.user\_id | `number` | User ID     |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncBlockeRemove(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncblockeremove" id="module_rostermanage__asyncblockeremove"></a>

Remove blacklist

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | Parameter   |
| params.user\_id | `number` | User ID     |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncApply(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncapply" id="module_rostermanage__asyncapply"></a>

Request to add friend

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | Parameter   |
| params.user\_id | `number` | User ID     |
| params.alias    | `string` | Comment     |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncAccept(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncaccept" id="module_rostermanage__asyncaccept"></a>

Approve add-friend request

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | Parameter   |
| params.user\_id | `number` | User ID     |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncDecline(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncdecline" id="module_rostermanage__asyncdecline"></a>

Reject friend request

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | Parameter   |
| params.user\_id | `number` | User ID     |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncUpdateRosterExt(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncupdaterosterext" id="module_rostermanage__asyncupdaterosterext"></a>

Modify the Friend extension field

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: `Promise.<boolean>` - Success or not

| Param                     | Type      | Description                      |
| ------------------------- | --------- | -------------------------------- |
| params                    | `object`  | Parameter                        |
| params.user\_id           | `number`  | User ID                          |
| params.ext                | `string`  | Extension field                  |
| params.alias              | `string`  | Name in comment                  |
| params.mute\_notification | `boolean` | Whether to receive message alert |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncSearchRosterByName(params) ⇒ [`Promise.<RosterItem>`](types.md#module\_types\_\_rosteritem) <a href="#module_rostermanage__asyncsearchrosterbyname" id="module_rostermanage__asyncsearchrosterbyname"></a>

Search for user by name

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: [`Promise.<RosterItem>`](types.md#module\_types\_\_rosteritem) - User information

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | Parameter   |
| params.username | `string` | Username    |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```

### rosterManage.asyncSearchRosterById(params) ⇒ [`Promise.<RosterItem>`](types.md#module\_types\_\_rosteritem) <a href="#module_rostermanage__asyncsearchrosterbyid" id="module_rostermanage__asyncsearchrosterbyid"></a>

Search for user by ID

**Kind**: static method of [`rosterManage`](rosterManage.md#module\_rostermanage)\
**Returns**: [`Promise.<RosterItem>`](types.md#module\_types\_\_rosteritem) - User information

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | Parameter   |
| params.user\_id | `number` | User ID     |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```
