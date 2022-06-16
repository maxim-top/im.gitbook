# userManage
## userManage {#module_usermanage}

* [userManage](#module_usermanage)
    * [.getToken()](#module_usermanage__gettoken) ⇒ <code>string</code>
    * [.getUid()](#module_usermanage__getuid) ⇒ <code>number</code>
    * [.getAppid()](#module_usermanage__getappid) ⇒ <code>string</code>
    * [.getConversationList()](#module_usermanage__getconversationlist) ⇒ [<code>Array.&lt;ConversationItem&gt;</code>](types.md#module_types__conversationitem)
    * [.asyncRegister(opt)](#module_usermanage__asyncregister) ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings)
    * [.asyncUpdateAvatar(params)](#module_usermanage__asyncupdateavatar) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncUpdateNickName(params)](#module_usermanage__asyncupdatenickname) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncGetProfile()](#module_usermanage__asyncgetprofile) ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types__userprofile)
    * [.asyncUpdateProfile(params)](#module_usermanage__asyncupdateprofile) ⇒ <code>Promise.&lt;boolean&gt;</code>
    * [.asyncGetSettings()](#module_usermanage__asyncgetsettings) ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings)
    * [.asyncUpdateSettings(settings)](#module_usermanage__asyncupdatesettings) ⇒ <code>Promise.&lt;boolean&gt;</code>

### userManage.getToken() ⇒ <code>string</code> {#module_usermanage__gettoken}
Get token of logged-in user

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>string</code> - User's token  
### userManage.getUid() ⇒ <code>number</code> {#module_usermanage__getuid}
Get uid of logged-in user

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>number</code> - User ID  
### userManage.getAppid() ⇒ <code>string</code> {#module_usermanage__getappid}
Get appid

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>string</code> - APP ID  
### userManage.getConversationList() ⇒ [<code>Array.&lt;ConversationItem&gt;</code>](types.md#module_types__conversationitem) {#module_usermanage__getconversationlist}
Get list of recent conversations

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
### userManage.asyncRegister(opt) ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings) {#module_usermanage__asyncregister}
User registeration

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings) - User settings 

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> | User information |
| opt.username | <code>string</code> | Username |
| opt.password | <code>string</code> | Password |

### userManage.asyncUpdateAvatar(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncupdateavatar}
Update avatar

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.avatar | <code>string</code> | Avatar url |

### userManage.asyncUpdateNickName(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncupdatenickname}
Update nickname

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.nick_name | <code>string</code> | Nickname |

### userManage.asyncGetProfile() ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types__userprofile) {#module_usermanage__asyncgetprofile}
Get user profile

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types__userprofile) - User information  
### userManage.asyncUpdateProfile(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncupdateprofile}
Update user profile

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> |  |
| params.description | <code>string</code> | Description |
| params.nick_name | <code>string</code> | Nickname |
| params.private_info | <code>string</code> | Private information, visible only to yourself |
| params.public_info | <code>string</code> | Public information, visible to both friends and strangers |

### userManage.asyncGetSettings() ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings) {#module_usermanage__asyncgetsettings}
Get user settings

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings) - User information  
### userManage.asyncUpdateSettings(settings) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncupdatesettings}
Modify user settings

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| settings | [<code>UserSettings</code>](types.md#module_types__usersettings) | Updated settings |
