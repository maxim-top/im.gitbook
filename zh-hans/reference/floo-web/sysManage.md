# sysManage

## sysManage <a href="#module_sysmanage" id="module_sysmanage"></a>

* [sysManage](sysManage.md#module_sysmanage)
  * [.sendRosterMessage(msg)](sysManage.md#module_sysmanage__sendrostermessage) ⇒ `number`
  * [.sendGroupMessage(msg)](sysManage.md#module_sysmanage__sendgroupmessage) ⇒ `number`
  * [.requireHistoryMessage(uid, sid, amount)](sysManage.md#module_sysmanage__requirehistorymessage)
  * [.sendMentionMessage(params)](sysManage.md#module_sysmanage__sendmentionmessage) ⇒ `number`
  * [.sendInputStatusMessage(uid, status)](sysManage.md#module_sysmanage__sendinputstatusmessage) ⇒ `number`
  * [.forwardMessage(param)](sysManage.md#module_sysmanage__forwardmessage) ⇒ `number`
  * [.getMessageStatus(cid, mid, isGroup)](sysManage.md#module_sysmanage__getmessagestatus) ⇒ `string`
  * [.asyncFileUpload(param)](sysManage.md#module_sysmanage__asyncfileupload) ⇒ [`Promise.<FileUploadResult>`](types.md#module_types__fileuploadresult)
  * [.getImage(param)](sysManage.md#module_sysmanage__getimage) ⇒ `string`
  * [.deleteConversation(id, other\_devices)](sysManage.md#module_sysmanage__deleteconversation)
  * [.asyncGetGroupAvatarUploadUrl(params)](sysManage.md#module_sysmanage__asyncgetgroupavataruploadurl) ⇒ [`Promise.<FileUpload>`](types.md#module_types__fileupload)
  * [.asyncGetFileUploadChatFileUrl(params)](sysManage.md#module_sysmanage__asyncgetfileuploadchatfileurl) ⇒ [`Promise.<FileUpload>`](types.md#module_types__fileupload)

### sysManage.sendRosterMessage(msg) ⇒ `number` <a href="#module_sysmanage__sendrostermessage" id="module_sysmanage__sendrostermessage"></a>

发送单聊消息

**Kind**: static method of [`sysManage`](sysManage.md#module_sysmanage)\
**Returns**: `number` - 客户端生成的消息ID

| Param          | Type                 | Description                                                                                              |
| -------------- | -------------------- | -------------------------------------------------------------------------------------------------------- |
| msg            | `object`             | 消息体                                                                                                      |
| msg.uid        | `string`             | 接收者ID                                                                                                    |
| msg.content    | `string`             | 消息内容                                                                                                     |
| msg.type       | `string`             | 消息类型： text - 文本, image - 图片， audio - 语音, video - 视频，file - 文件, location - 位置， command - 命令, forward - 转发 |
| msg.ext        | `string` \| `object` | 扩展字段                                                                                                     |
| msg.attachment | `string` \| `object` | 附件信息                                                                                                     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='sysManage'></div>

```

### sysManage.sendGroupMessage(msg) ⇒ `number` <a href="#module_sysmanage__sendgroupmessage" id="module_sysmanage__sendgroupmessage"></a>

发送群聊消息

**Kind**: static method of [`sysManage`](sysManage.md#module_sysmanage)\
**Returns**: `number` - 客户端生成的消息ID

| Param          | Type                 | Description                                                                                              |
| -------------- | -------------------- | -------------------------------------------------------------------------------------------------------- |
| msg            | `object`             | 发送消息体                                                                                                    |
| msg.gid        | `string`             | 群组ID                                                                                                     |
| msg.content    | `string`             | 消息内容                                                                                                     |
| msg.type       | `string`             | 消息类型： text - 文本, image - 图片， audio - 语音, video - 视频，file - 文件, location - 位置， command - 命令, forward - 转发 |
| msg.ext        | `string` \| `object` | 扩展字段                                                                                                     |
| msg.attachment | `string` \| `object` | 附件信息                                                                                                     |
| msg.priority   | `number`             | 设置消息的扩散优先级，默认为0。0表示扩散，数字越小扩散的越多。                                                                         |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='sysManage'></div>

```

### sysManage.requireHistoryMessage(uid, sid, amount) <a href="#module_sysmanage__requirehistorymessage" id="module_sysmanage__requirehistorymessage"></a>

请求历史消息

**Kind**: static method of [`sysManage`](sysManage.md#module_sysmanage)

| Param  | Type     | Description                      |
| ------ | -------- | -------------------------------- |
| uid    | `number` | 会话ID                             |
| sid    | `number` | 消息ID: 从哪个消息向前拉取，传0表示从最新一条消息开始拉取。 |
| amount | `number` | 拉取的条数                            |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='sysManage'></div>

```

### sysManage.sendMentionMessage(params) ⇒ `number` <a href="#module_sysmanage__sendmentionmessage" id="module_sysmanage__sendmentionmessage"></a>

群发送@消息

**Kind**: static method of [`sysManage`](sysManage.md#module_sysmanage)\
**Returns**: `number` - 客户端生成的消息ID

| Param                   | Type             | Description |
| ----------------------- | ---------------- | ----------- |
| params                  | `object`         |             |
| params.gid              | `number`         | 群ID         |
| params.txt              | `string`         | 消息文本内容      |
| params.mentionAll       | `boolean`        | 是否@所有人      |
| params.mentionList      | `Array.<number>` | @的成员ID列表    |
| params.mentionedMessage | `string`         | @消息的显示内容    |
| params.mentionedMessage | `string`         | @消息的推送内容    |
| params.senderNickname   | `string`         | 发送者昵称       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='sysManage'></div>

```

### sysManage.sendInputStatusMessage(uid, status) ⇒ `number` <a href="#module_sysmanage__sendinputstatusmessage" id="module_sysmanage__sendinputstatusmessage"></a>

发送输入状态消息

**Kind**: static method of [`sysManage`](sysManage.md#module_sysmanage)\
**Returns**: `number` - 客户端生成的消息ID

| Param  | Type     | Description                      |
| ------ | -------- | -------------------------------- |
| uid    | `number` | 会话ID                             |
| status | `string` | 状态： nothing - 未输入， typing - 正在输入 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='sysManage'></div>

```

### sysManage.forwardMessage(param) ⇒ `number` <a href="#module_sysmanage__forwardmessage" id="module_sysmanage__forwardmessage"></a>

转发消息

**Kind**: static method of [`sysManage`](sysManage.md#module_sysmanage)\
**Returns**: `number` - 客户端生成的消息ID

| Param     | Type     | Description       |
| --------- | -------- | ----------------- |
| param     | `object` | 参数                |
| param.uid | `number` | 接收方用户ID（仅转发单聊时设置） |
| param.gid | `number` | 接收方群组ID（仅转发群聊时设置） |
| param.mid | `number` | 要转发的消息ID          |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='sysManage'></div>

```

### sysManage.getMessageStatus(cid, mid, isGroup) ⇒ `string` <a href="#module_sysmanage__getmessagestatus" id="module_sysmanage__getmessagestatus"></a>

获取消息的状态

**Kind**: static method of [`sysManage`](sysManage.md#module_sysmanage)\
**Returns**: `string` - 消息状态: unread - 未读， delivered - 已投递， read - 已读

| Param   | Type      | Default | Description |
| ------- | --------- | ------- | ----------- |
| cid     | `number`  |         | 会话ID        |
| mid     | `number`  |         | 消息ID        |
| isGroup | `boolean` | `false` | 是否是群聊       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='sysManage'></div>

```

### sysManage.asyncFileUpload(param) ⇒ [`Promise.<FileUploadResult>`](types.md#module_types__fileuploadresult) <a href="#module_sysmanage__asyncfileupload" id="module_sysmanage__asyncfileupload"></a>

上传文件

**Kind**: static method of [`sysManage`](sysManage.md#module_sysmanage)\
**Returns**: [`Promise.<FileUploadResult>`](types.md#module_types__fileuploadresult) - 文件上传结果

| Param                 | Type                                                              | Description                                                                                                                                                                            |
| --------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| param                 | `object`                                                          | 参数                                                                                                                                                                                     |
| param.group\_d        | `number`                                                          | 群组ID                                                                                                                                                                                   |
| param.toType          | `number`                                                          | 接收者类型：rosterAvatar - 用户头像， chat - 聊天文件， groupAvatar - 群头像                                                                                                                              |
| param.to\_id          | `number`                                                          | 接收者ID                                                                                                                                                                                  |
| param.file            | `File`                                                            | 文件                                                                                                                                                                                     |
| param.fileType        | `string`                                                          | 文件类型：file - 普通聊天文件, audio - 语音聊天文件(amr格式),image - 图片聊天文件, video - 视频聊天文件, audio-mp3 - 语音聊天文件(mp3格式), shareFile - 普通共享文件, shareAudio - 语音共享文件, shareImage - 图片共享文件, shareVideo - 视频共享文件 |
| param.chatType        | `number`                                                          | 聊天类型： roster - 单聊, group - 群聊                                                                                                                                                          |
| param.processCallback | [`fileUploadProgress`](types.md#module_types__fileuploadprogress) | 上传进度回调                                                                                                                                                                                 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='sysManage'></div>

```

### sysManage.getImage(param) ⇒ `string` <a href="#module_sysmanage__getimage" id="module_sysmanage__getimage"></a>

拼装图片路径

**Kind**: static method of [`sysManage`](sysManage.md#module_sysmanage)\
**Returns**: `string` - 图片地址

| Param           | Type      | Description                |
| --------------- | --------- | -------------------------- |
| param           | `object`  |                            |
| param.avatar    | `string`  | 文件地址                       |
| param.type      | `string`  | 类型： roster - 用户, group - 群 |
| param.thumbnail | `boolean` | 是否缩略图：默认为true              |
| param.sdefault  | `string`  | 默认图片地址                     |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='sysManage'></div>

```

### sysManage.deleteConversation(id, other\_devices) <a href="#module_sysmanage__deleteconversation" id="module_sysmanage__deleteconversation"></a>

删除会话

**Kind**: static method of [`sysManage`](sysManage.md#module_sysmanage)

| Param          | Type      | Default | Description    |
| -------------- | --------- | ------- | -------------- |
| id             | `number`  |         | 会话ID           |
| other\_devices | `boolean` | `true`  | 是否同时删除其它设备上的会话 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='sysManage'></div>
```

### sysManage.asyncGetGroupAvatarUploadUrl(params) ⇒ [`Promise.<FileUpload>`](types.md#module_types__fileupload) <a href="#module_sysmanage__asyncgetgroupavataruploadurl" id="module_sysmanage__asyncgetgroupavataruploadurl"></a>

获取上传群头像URL

**Kind**: static method of [`sysManage`](sysManage.md#module_sysmanage)\
**Returns**: [`Promise.<FileUpload>`](types.md#module_types__fileupload) - 文件上传信息

| Param            | Type     | Description |
| ---------------- | -------- | ----------- |
| params           | `object` | 参数          |
| params.group\_id | `number` | 群组ID        |

### sysManage.asyncGetFileUploadChatFileUrl(params) ⇒ [`Promise.<FileUpload>`](types.md#module_types__fileupload) <a href="#module_sysmanage__asyncgetfileuploadchatfileurl" id="module_sysmanage__asyncgetfileuploadchatfileurl"></a>

获取聊天文件上传地址

**Kind**: static method of [`sysManage`](sysManage.md#module_sysmanage)\
**Returns**: [`Promise.<FileUpload>`](types.md#module_types__fileupload) - 文件上传信息

| Param             | Type     | Description                                                                                                                                   |
| ----------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| params            | `object` | 参数                                                                                                                                            |
| params.file\_type | `number` | 文件类型: 100 - 普通聊天文件, 101 - 语音聊天文件(amr格式),102 - 图片聊天文件, 103 - 视频聊天文件, 104 - 语音聊天文件(mp3格式)200 - 普通共享文件, 201 - 语音共享文件, 202 - 图片共享文件, 203 - 视频共享文件 |
| params.to\_type   | `number` | 会话类型： 1 - 用户，2 - 群组                                                                                                                           |
| params.to\_id     | `number` | 会话ID                                                                                                                                          |
