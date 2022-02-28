# userManage
## userManage {#module_usermanage}

* [userManage](#module_usermanage)
    * [.getToken()](#module_usermanage.gettoken) ⇒ <code>string</code>
    * [.getUid()](#module_usermanage.getuid) ⇒ <code>number</code>
    * [.getAppid()](#module_usermanage.getappid) ⇒ <code>string</code>
    * [.getConversationList()](#module_usermanage.getconversationlist) ⇒ [<code>Array.&lt;ConversationItem&gt;</code>](types.md#module_types..conversationitem)
    * [.asyncUpdateAvatar(params)](#module_usermanage.asyncupdateavatar) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateNickName(params)](#module_usermanage.asyncupdatenickname) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncGetProfile()](#module_usermanage.asyncgetprofile) ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types..userprofile)
    * [.asyncUpdateProfile(params)](#module_usermanage.asyncupdateprofile) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncGetSettings()](#module_usermanage.asyncgetsettings) ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types..usersettings)
    * [.asyncUpdateSettings(settings)](#module_usermanage.asyncupdatesettings) ⇒ <code>Promise.&lt;boolean&gt;</code>

### userManage.getToken() ⇒ <code>string</code> {#module_usermanage.gettoken}
获取登录用户的token

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>string</code> - 用户的token  
### userManage.getUid() ⇒ <code>number</code> {#module_usermanage.getuid}
获取登录用户的uid

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>number</code> - 用户ID  
### userManage.getAppid() ⇒ <code>string</code> {#module_usermanage.getappid}
获取appid

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>string</code> - APP ID  
### userManage.getConversationList() ⇒ [<code>Array.&lt;ConversationItem&gt;</code>](types.md#module_types..conversationitem) {#module_usermanage.getconversationlist}
获取最近会话列表

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
### userManage.asyncUpdateAvatar(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage.asyncupdateavatar}
更新头像

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.avatar | <code>string</code> | 头像 url |

### userManage.asyncUpdateNickName(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage.asyncupdatenickname}
更新昵称

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 参数 |
| params.nick_name | <code>string</code> | 昵称 |

### userManage.asyncGetProfile() ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types..userprofile) {#module_usermanage.asyncgetprofile}
获取用户profile

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types..userprofile) - 用户信息  
### userManage.asyncUpdateProfile(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage.asyncupdateprofile}
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

### userManage.asyncGetSettings() ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types..usersettings) {#module_usermanage.asyncgetsettings}
获取用户设置信息

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types..usersettings) - 用户信息  
### userManage.asyncUpdateSettings(settings) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage.asyncupdatesettings}
修改用户设置

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - 是否成功  

| Param | Type | Description |
| --- | --- | --- |
| settings | [<code>UserSettings</code>](types.md#module_types..usersettings) | 更新的设置 |
