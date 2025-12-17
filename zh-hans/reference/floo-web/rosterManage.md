# rosterManage

## rosterManage <a href="#module_rostermanage" id="module_rostermanage"></a>

好友管理

* [rosterManage](rosterManage.md#module_rostermanage)
  * [.asyncGetRosterIdList(force)](rosterManage.md#module_rostermanage__asyncgetrosteridlist) ⇒ `Promise.<Array.<number>>`
  * [.asyncGetRosterInfo(roster\_id, force)](rosterManage.md#module_rostermanage__asyncgetrosterinfo) ⇒ [`Promise.<RosterItem>`](types.md#module_types__rosteritem)
  * [.asyncDeleteRoster(param)](rosterManage.md#module_rostermanage__asyncdeleteroster) ⇒ `Promise.<boolean>`
  * [.asnycGetRosterListDetailByIds(roster\_ids)](rosterManage.md#module_rostermanage__asnycgetrosterlistdetailbyids) ⇒ `Promise.<Array.<module:types~RosterItem>>`
  * [.getAllRosterDetail()](rosterManage.md#module_rostermanage__getallrosterdetail) ⇒ [`Array.<RosterItem>`](types.md#module_types__rosteritem)
  * [.asyncGetUserProfile(force)](rosterManage.md#module_rostermanage__asyncgetuserprofile) ⇒ [`Promise.<UserProfile>`](types.md#module_types__userprofile)
  * [.getRosterMessageByRid(uid)](rosterManage.md#module_rostermanage__getrostermessagebyrid) ⇒ [`Array.<Meta>`](types.md#module_types__meta)
  * [.readRosterMessage(roster\_id, mid)](rosterManage.md#module_rostermanage__readrostermessage)
  * [.recallMessage(uid, mid)](rosterManage.md#module_rostermanage__recallmessage)
  * [.unreadMessage(uid, mid)](rosterManage.md#module_rostermanage__unreadmessage)
  * [.deleteMessage(uid, mid)](rosterManage.md#module_rostermanage__deletemessage)
  * [.appendMessageContent(uid, mid, content)](rosterManage.md#module_rostermanage__appendmessagecontent)
  * [.replaceMessage(uid, mid, content, config, ext)](rosterManage.md#module_rostermanage__replacemessage)
  * [.getRosterInfo(rid)](rosterManage.md#module_rostermanage__getrosterinfo) ⇒ [`RosterItem`](types.md#module_types__rosteritem)
  * [.getUnreadCount(uid)](rosterManage.md#module_rostermanage__getunreadcount) ⇒ `number`
  * [.asyncGetApplyList(params)](rosterManage.md#module_rostermanage__asyncgetapplylist) ⇒ `Promise.<Array.<module:types~RosterApplication>>`
  * [.asyncGetBlockedlist(params)](rosterManage.md#module_rostermanage__asyncgetblockedlist) ⇒ `Promise.<Array.<number>>`
  * [.asyncBlockeAdd(params)](rosterManage.md#module_rostermanage__asyncblockeadd) ⇒ `Promise.<boolean>`
  * [.asyncBlockeRemove(params)](rosterManage.md#module_rostermanage__asyncblockeremove) ⇒ `Promise.<boolean>`
  * [.asyncApply(params)](rosterManage.md#module_rostermanage__asyncapply) ⇒ `Promise.<boolean>`
  * [.asyncAccept(params)](rosterManage.md#module_rostermanage__asyncaccept) ⇒ `Promise.<boolean>`
  * [.asyncDecline(params)](rosterManage.md#module_rostermanage__asyncdecline) ⇒ `Promise.<boolean>`
  * [.asyncUpdateRosterExt(params)](rosterManage.md#module_rostermanage__asyncupdaterosterext) ⇒ `Promise.<boolean>`
  * [.asyncUpdateRosterAlias(params)](rosterManage.md#module_rostermanage__asyncupdaterosteralias) ⇒ `Promise.<boolean>`
  * [.asyncSearchRosterByName(params)](rosterManage.md#module_rostermanage__asyncsearchrosterbyname) ⇒ [`Promise.<RosterItem>`](types.md#module_types__rosteritem)
  * [.asyncSearchRosterById(params)](rosterManage.md#module_rostermanage__asyncsearchrosterbyid) ⇒ [`Promise.<RosterItem>`](types.md#module_types__rosteritem)

### rosterManage.asyncGetRosterIdList(force) ⇒ `Promise.<Array.<number>>` <a href="#module_rostermanage__asyncgetrosteridlist" id="module_rostermanage__asyncgetrosteridlist"></a>

获取好友id列表

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `Promise.<Array.<number>>` - 用户ID列表

| Param | Type      | Description                               |
| ----- | --------- | ----------------------------------------- |
| force | `boolean` | 是否强制从服务器拉取：true - 从服务器获取， false - 从本地存储获取 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncGetRosterInfo(roster\_id, force) ⇒ [`Promise.<RosterItem>`](types.md#module_types__rosteritem) <a href="#module_rostermanage__asyncgetrosterinfo" id="module_rostermanage__asyncgetrosterinfo"></a>

获取好友信息

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: [`Promise.<RosterItem>`](types.md#module_types__rosteritem) - 好友信息

| Param      | Type      | Description                                  |
| ---------- | --------- | -------------------------------------------- |
| roster\_id | `number`  | 好友ID                                         |
| force      | `boolean` | 是否强制从服务器拉取： true - 从服务器拉取， false - 优先从本地存储获取 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncDeleteRoster(param) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncdeleteroster" id="module_rostermanage__asyncdeleteroster"></a>

删除好友

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `Promise.<boolean>` - 请求结果

| Param          | Type     | Description |
| -------------- | -------- | ----------- |
| param          | `object` | 参数          |
| param.user\_id | `number` | 好友的用户ID     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asnycGetRosterListDetailByIds(roster\_ids) ⇒ `Promise.<Array.<module:types~RosterItem>>` <a href="#module_rostermanage__asnycgetrosterlistdetailbyids" id="module_rostermanage__asnycgetrosterlistdetailbyids"></a>

根据id列表获取用户详细信息

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `Promise.<Array.<module:types~RosterItem>>` - 用户详细信息列表

| Param       | Type             | Description |
| ----------- | ---------------- | ----------- |
| roster\_ids | `Array.<number>` | 用户ID列表      |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.getAllRosterDetail() ⇒ [`Array.<RosterItem>`](types.md#module_types__rosteritem) <a href="#module_rostermanage__getallrosterdetail" id="module_rostermanage__getallrosterdetail"></a>

获取缓存的所有用户详细信息

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: [`Array.<RosterItem>`](types.md#module_types__rosteritem) - 用户详细信息列表\
**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncGetUserProfile(force) ⇒ [`Promise.<UserProfile>`](types.md#module_types__userprofile) <a href="#module_rostermanage__asyncgetuserprofile" id="module_rostermanage__asyncgetuserprofile"></a>

获取自己的用户信息

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: [`Promise.<UserProfile>`](types.md#module_types__userprofile) - 用户信息

| Param | Type      | Description                                  |
| ----- | --------- | -------------------------------------------- |
| force | `boolean` | 是否强制从服务器拉取： true - 从服务器拉取， false - 优先从本地存储获取 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.getRosterMessageByRid(uid) ⇒ [`Array.<Meta>`](types.md#module_types__meta) <a href="#module_rostermanage__getrostermessagebyrid" id="module_rostermanage__getrostermessagebyrid"></a>

根据会话ID获取聊天消息

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: [`Array.<Meta>`](types.md#module_types__meta) - 聊天消息列表

| Param | Type     | Description |
| ----- | -------- | ----------- |
| uid   | `number` | 会话ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.readRosterMessage(roster\_id, mid) <a href="#module_rostermanage__readrostermessage" id="module_rostermanage__readrostermessage"></a>

修改消息状态为已读

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)

| Param      | Type     | Description                 |
| ---------- | -------- | --------------------------- |
| roster\_id | `number` | 会话ID                        |
| mid        | `number` | 消息ID： 如果不设置 表示把这个会话所有消息设为已读 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.recallMessage(uid, mid) <a href="#module_rostermanage__recallmessage" id="module_rostermanage__recallmessage"></a>

撤回消息，只能撤回5分钟内的

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)

| Param | Type     | Description |
| ----- | -------- | ----------- |
| uid   | `number` | 会话ID        |
| mid   | `number` | 消息ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.unreadMessage(uid, mid) <a href="#module_rostermanage__unreadmessage" id="module_rostermanage__unreadmessage"></a>

设置消息成未读

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)

| Param | Type     | Description |
| ----- | -------- | ----------- |
| uid   | `number` | 会话ID        |
| mid   | `number` | 消息ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.deleteMessage(uid, mid) <a href="#module_rostermanage__deletemessage" id="module_rostermanage__deletemessage"></a>

删除消息

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)

| Param | Type     | Description |
| ----- | -------- | ----------- |
| uid   | `number` | 会话ID        |
| mid   | `number` | 消息ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.appendMessageContent(uid, mid, content) <a href="#module_rostermanage__appendmessagecontent" id="module_rostermanage__appendmessagecontent"></a>

追加消息内容

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)

| Param   | Type     | Description |
| ------- | -------- | ----------- |
| uid     | `number` | 会话ID        |
| mid     | `number` | 消息ID        |
| content | `string` | 消息追加内容      |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.replaceMessage(uid, mid, content, config, ext) <a href="#module_rostermanage__replacemessage" id="module_rostermanage__replacemessage"></a>

更新消息内容

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)

| Param   | Type                 | Default | Description |
| ------- | -------------------- | ------- | ----------- |
| uid     | `number`             |         | 会话ID        |
| mid     | `number`             |         | 消息ID        |
| content | `string`             |         | 消息更新内容      |
| config  | `string` \| `object` | `null`  | 消息更新配置      |
| ext     | `string` \| `object` | `null`  | 消息更新扩展信息    |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.getRosterInfo(rid) ⇒ [`RosterItem`](types.md#module_types__rosteritem) <a href="#module_rostermanage__getrosterinfo" id="module_rostermanage__getrosterinfo"></a>

获取好友信息

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: [`RosterItem`](types.md#module_types__rosteritem) - 好友信息

| Param | Type     | Description |
| ----- | -------- | ----------- |
| rid   | `number` | 好友ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.getUnreadCount(uid) ⇒ `number` <a href="#module_rostermanage__getunreadcount" id="module_rostermanage__getunreadcount"></a>

获取指定会话的未读数

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `number` - 未读数

| Param | Type     | Description |
| ----- | -------- | ----------- |
| uid   | `number` | 会话ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncGetApplyList(params) ⇒ `Promise.<Array.<module:types~RosterApplication>>` <a href="#module_rostermanage__asyncgetapplylist" id="module_rostermanage__asyncgetapplylist"></a>

获取好友申请列表

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `Promise.<Array.<module:types~RosterApplication>>` - 好友申请列表

| Param         | Type     | Description           |
| ------------- | -------- | --------------------- |
| params        | `object` | 参数                    |
| params.cursor | `number` | 从哪开始获取：可以传空字符串表示从头开始取 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncGetBlockedlist(params) ⇒ `Promise.<Array.<number>>` <a href="#module_rostermanage__asyncgetblockedlist" id="module_rostermanage__asyncgetblockedlist"></a>

获取黑名单

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `Promise.<Array.<number>>` - 用户ID列表

| Param  | Type     | Description |
| ------ | -------- | ----------- |
| params | `object` | 参数：空对象      |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncBlockeAdd(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncblockeadd" id="module_rostermanage__asyncblockeadd"></a>

加入黑名单

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | 参数          |
| params.user\_id | `number` | 用户ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncBlockeRemove(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncblockeremove" id="module_rostermanage__asyncblockeremove"></a>

移除黑名单

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | 参数          |
| params.user\_id | `number` | 用户ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncApply(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncapply" id="module_rostermanage__asyncapply"></a>

请求加为好友

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | 参数          |
| params.user\_id | `number` | 用户ID        |
| params.alias    | `string` | 备注          |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncAccept(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncaccept" id="module_rostermanage__asyncaccept"></a>

通过好友申请

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | 参数          |
| params.user\_id | `number` | 用户ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncDecline(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncdecline" id="module_rostermanage__asyncdecline"></a>

拒绝好友申请

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | 参数          |
| params.user\_id | `number` | 用户ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncUpdateRosterExt(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncupdaterosterext" id="module_rostermanage__asyncupdaterosterext"></a>

修改好友扩展字段

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param                     | Type      | Description |
| ------------------------- | --------- | ----------- |
| params                    | `object`  | 参数          |
| params.user\_id           | `number`  | 用户ID        |
| params.ext                | `string`  | 扩展字段        |
| params.mute\_notification | `boolean` | 是否接收消息提醒    |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncUpdateRosterAlias(params) ⇒ `Promise.<boolean>` <a href="#module_rostermanage__asyncupdaterosteralias" id="module_rostermanage__asyncupdaterosteralias"></a>

修改好友扩展别名字段

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param                     | Type      | Description |
| ------------------------- | --------- | ----------- |
| params                    | `object`  | 参数          |
| params.user\_id           | `number`  | 用户ID        |
| params.alias              | `string`  | 备注名称        |
| params.mute\_notification | `boolean` | 是否接收消息提醒    |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncSearchRosterByName(params) ⇒ [`Promise.<RosterItem>`](types.md#module_types__rosteritem) <a href="#module_rostermanage__asyncsearchrosterbyname" id="module_rostermanage__asyncsearchrosterbyname"></a>

按名称搜索用户

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: [`Promise.<RosterItem>`](types.md#module_types__rosteritem) - 用户信息

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | 参数          |
| params.username | `string` | 用户名         |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>

```

### rosterManage.asyncSearchRosterById(params) ⇒ [`Promise.<RosterItem>`](types.md#module_types__rosteritem) <a href="#module_rostermanage__asyncsearchrosterbyid" id="module_rostermanage__asyncsearchrosterbyid"></a>

按ID搜索用户

**Kind**: static method of [`rosterManage`](rosterManage.md#module_rostermanage)\
**Returns**: [`Promise.<RosterItem>`](types.md#module_types__rosteritem) - 用户信息

| Param           | Type     | Description |
| --------------- | -------- | ----------- |
| params          | `object` | 参数          |
| params.user\_id | `number` | 用户ID        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rosterManage'></div>
```
