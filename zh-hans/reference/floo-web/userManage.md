# userManage
## userManage {#module_usermanage}

* [userManage](#module_usermanage)
    * [.getToken()](#module_usermanage__gettoken) ⇒ <code>string</code>
    * [.getUid()](#module_usermanage__getuid) ⇒ <code>number</code>
    * [.getAppid()](#module_usermanage__getappid) ⇒ <code>string</code>
    * [.getConversationList()](#module_usermanage__getconversationlist) ⇒ [<code>Array.&lt;ConversationItem&gt;</code>](types.md#module_types__conversationitem)
    * [.getDeviceSN()](#module_usermanage__getdevicesn) ⇒ <code>number</code>
    * [.asyncBindDeviceToken(param)](#module_usermanage__asyncbinddevicetoken) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUnbindDeviceToken(param)](#module_usermanage__asyncunbinddevicetoken) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncRegister(opt)](#module_usermanage__asyncregister) ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings)
    * [.asyncUpdateAvatar(params)](#module_usermanage__asyncupdateavatar) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateNickName(params)](#module_usermanage__asyncupdatenickname) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncGetProfile()](#module_usermanage__asyncgetprofile) ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types__userprofile)
    * [.asyncUpdateProfile(params)](#module_usermanage__asyncupdateprofile) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncGetSettings()](#module_usermanage__asyncgetsettings) ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings)
    * [.asyncUpdateSettings(settings)](#module_usermanage__asyncupdatesettings) ⇒ <code>Promise.&lt;boolean&gt;</code>

### userManage.getToken() ⇒ <code>string</code> {#module_usermanage__gettoken}
获取登录用户的token

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>string</code> - 用户的token  
### userManage.getUid() ⇒ <code>number</code> {#module_usermanage__getuid}
获取登录用户的uid

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>number</code> - 用户ID  
### userManage.getAppid() ⇒ <code>string</code> {#module_usermanage__getappid}
获取appid

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>string</code> - APP ID  
### userManage.getConversationList() ⇒ [<code>Array.&lt;ConversationItem&gt;</code>](types.md#module_types__conversationitem) {#module_usermanage__getconversationlist}
获取最近会话列表

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
### userManage.getDeviceSN() ⇒ <code>number</code> {#module_usermanage__getdevicesn}
获取设备序号

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>number</code> - 设备序号  
### userManage.asyncBindDeviceToken(param) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncbinddevicetoken}
绑定推送设备

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| param | <code>object</code> | 绑定请求 |
| param.device_sn | <code>number</code> | 设备序号 |
| param.notifier_name | <code>string</code> | 证书名称，即在蓝莺IM控制台内上传证书时候设置的名称。 |
| param.device_token | <code>string</code> | 推送设备Token |

### userManage.asyncUnbindDeviceToken(param) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncunbinddevicetoken}
解绑推送设备

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| param | <code>object</code> | 解绑请求 |
| param.deviceSn | <code>number</code> | 设备序号 |

### userManage.asyncRegister(opt) ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings) {#module_usermanage__asyncregister}
用户注册

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings) - 用户设置  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> | 用户信息 |
| opt.username | <code>string</code> | 用户名 |
| opt.password | <code>string</code> | 密码 |

### userManage.asyncUpdateAvatar(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncupdateavatar}
更新头像

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.avatar | <code>string</code> | 头像 url |

### userManage.asyncUpdateNickName(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncupdatenickname}
更新昵称

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.nick_name | <code>string</code> | 昵称 |

### userManage.asyncGetProfile() ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types__userprofile) {#module_usermanage__asyncgetprofile}
获取用户profile

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types__userprofile) - 用户信息  
### userManage.asyncUpdateProfile(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncupdateprofile}
更新用户profile

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> |  |
| params.description | <code>string</code> | 描述信息 |
| params.nick_name | <code>string</code> | 昵称 |
| params.private_info | <code>string</code> | 私有信息，仅自己可见 |
| params.public_info | <code>string</code> | 公开信息，好友和陌生人可见 |

### userManage.asyncGetSettings() ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings) {#module_usermanage__asyncgetsettings}
获取用户设置信息

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings) - 用户信息  
### userManage.asyncUpdateSettings(settings) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncupdatesettings}
修改用户设置

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| settings | [<code>UserSettings</code>](types.md#module_types__usersettings) | 更新的设置 |
