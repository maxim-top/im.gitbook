# userManage

## userManage <a href="#module_usermanage" id="module_usermanage"></a>

* [userManage](userManage.md#module\_usermanage)
  * [.getToken()](userManage.md#module\_usermanage\_\_gettoken) ⇒ `string`
  * [.getUid()](userManage.md#module\_usermanage\_\_getuid) ⇒ `number`
  * [.getAppid()](userManage.md#module\_usermanage\_\_getappid) ⇒ `string`
  * [.getConversationList()](userManage.md#module\_usermanage\_\_getconversationlist) ⇒ [`Array.<ConversationItem>`](types.md#module\_types\_\_conversationitem)
  * [.getDeviceSN()](userManage.md#module\_usermanage\_\_getdevicesn) ⇒ `number`
  * [.asyncBindDeviceToken(param)](userManage.md#module\_usermanage\_\_asyncbinddevicetoken) ⇒ `Promise.<boolean>`
  * [.asyncUnbindDeviceToken(param)](userManage.md#module\_usermanage\_\_asyncunbinddevicetoken) ⇒ `Promise.<boolean>`
  * [.asyncRegister(opt)](userManage.md#module\_usermanage\_\_asyncregister) ⇒ [`Promise.<UserSettings>`](types.md#module\_types\_\_usersettings)
  * [.asyncUpdateAvatar(params)](userManage.md#module\_usermanage\_\_asyncupdateavatar) ⇒ `Promise.<boolean>`
  * [.asyncUpdateNickName(params)](userManage.md#module\_usermanage\_\_asyncupdatenickname) ⇒ `Promise.<boolean>`
  * [.asyncGetProfile()](userManage.md#module\_usermanage\_\_asyncgetprofile) ⇒ [`Promise.<UserProfile>`](types.md#module\_types\_\_userprofile)
  * [.asyncUpdateProfile(params)](userManage.md#module\_usermanage\_\_asyncupdateprofile) ⇒ `Promise.<boolean>`
  * [.asyncGetSettings()](userManage.md#module\_usermanage\_\_asyncgetsettings) ⇒ [`Promise.<UserSettings>`](types.md#module\_types\_\_usersettings)
  * [.asyncUpdateSettings(settings)](userManage.md#module\_usermanage\_\_asyncupdatesettings) ⇒ `Promise.<boolean>`

### userManage.getToken() ⇒ `string` <a href="#module_usermanage__gettoken" id="module_usermanage__gettoken"></a>

获取登录用户的token

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: `string` - 用户的token\
**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.getUid() ⇒ `number` <a href="#module_usermanage__getuid" id="module_usermanage__getuid"></a>

获取登录用户的uid

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: `number` - 用户ID\
**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.getAppid() ⇒ `string` <a href="#module_usermanage__getappid" id="module_usermanage__getappid"></a>

获取appid

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: `string` - APP ID\
**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.getConversationList() ⇒ [`Array.<ConversationItem>`](types.md#module\_types\_\_conversationitem) <a href="#module_usermanage__getconversationlist" id="module_usermanage__getconversationlist"></a>

获取最近会话列表

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.getDeviceSN() ⇒ `number` <a href="#module_usermanage__getdevicesn" id="module_usermanage__getdevicesn"></a>

获取设备序号

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: `number` - 设备序号\
**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.asyncBindDeviceToken(param) ⇒ `Promise.<boolean>` <a href="#module_usermanage__asyncbinddevicetoken" id="module_usermanage__asyncbinddevicetoken"></a>

绑定推送设备

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param                | Type     | Description                 |
| -------------------- | -------- | --------------------------- |
| param                | `object` | 绑定请求                        |
| param.device\_sn     | `number` | 设备序号                        |
| param.notifier\_name | `string` | 证书名称，即在蓝莺IM控制台内上传证书时候设置的名称。 |
| param.device\_token  | `string` | 推送设备Token                   |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.asyncUnbindDeviceToken(param) ⇒ `Promise.<boolean>` <a href="#module_usermanage__asyncunbinddevicetoken" id="module_usermanage__asyncunbinddevicetoken"></a>

解绑推送设备

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param          | Type     | Description |
| -------------- | -------- | ----------- |
| param          | `object` | 解绑请求        |
| param.deviceSn | `number` | 设备序号        |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.asyncRegister(opt) ⇒ [`Promise.<UserSettings>`](types.md#module\_types\_\_usersettings) <a href="#module_usermanage__asyncregister" id="module_usermanage__asyncregister"></a>

用户注册

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: [`Promise.<UserSettings>`](types.md#module\_types\_\_usersettings) - 用户设置

| Param        | Type     | Description |
| ------------ | -------- | ----------- |
| opt          | `object` | 用户信息        |
| opt.username | `string` | 用户名         |
| opt.password | `string` | 密码          |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.asyncUpdateAvatar(params) ⇒ `Promise.<boolean>` <a href="#module_usermanage__asyncupdateavatar" id="module_usermanage__asyncupdateavatar"></a>

更新头像

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param         | Type     | Description |
| ------------- | -------- | ----------- |
| params        | `object` | 参数          |
| params.avatar | `string` | 头像 url      |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.asyncUpdateNickName(params) ⇒ `Promise.<boolean>` <a href="#module_usermanage__asyncupdatenickname" id="module_usermanage__asyncupdatenickname"></a>

更新昵称

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param             | Type     | Description |
| ----------------- | -------- | ----------- |
| params            | `object` | 参数          |
| params.nick\_name | `string` | 昵称          |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.asyncGetProfile() ⇒ [`Promise.<UserProfile>`](types.md#module\_types\_\_userprofile) <a href="#module_usermanage__asyncgetprofile" id="module_usermanage__asyncgetprofile"></a>

获取用户profile

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: [`Promise.<UserProfile>`](types.md#module\_types\_\_userprofile) - 用户信息\
**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.asyncUpdateProfile(params) ⇒ `Promise.<boolean>` <a href="#module_usermanage__asyncupdateprofile" id="module_usermanage__asyncupdateprofile"></a>

更新用户profile

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param                | Type     | Description   |
| -------------------- | -------- | ------------- |
| params               | `object` |               |
| params.description   | `string` | 描述信息          |
| params.nick\_name    | `string` | 昵称            |
| params.private\_info | `string` | 私有信息，仅自己可见    |
| params.public\_info  | `string` | 公开信息，好友和陌生人可见 |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.asyncGetSettings() ⇒ [`Promise.<UserSettings>`](types.md#module\_types\_\_usersettings) <a href="#module_usermanage__asyncgetsettings" id="module_usermanage__asyncgetsettings"></a>

获取用户设置信息

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: [`Promise.<UserSettings>`](types.md#module\_types\_\_usersettings) - 用户信息\
**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```

### userManage.asyncUpdateSettings(settings) ⇒ `Promise.<boolean>` <a href="#module_usermanage__asyncupdatesettings" id="module_usermanage__asyncupdatesettings"></a>

修改用户设置

**Kind**: static method of [`userManage`](userManage.md#module\_usermanage)\
**Returns**: `Promise.<boolean>` - 是否成功

| Param    | Type                                                     | Description |
| -------- | -------------------------------------------------------- | ----------- |
| settings | [`UserSettings`](types.md#module\_types\_\_usersettings) | 更新的设置       |

**Example**

```js
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='userManage'></div>
```
