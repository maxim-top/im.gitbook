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
Get token of logged-in user

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>string</code> - User's token  
### userManage.getUid() ⇒ <code>number</code> {#module_usermanage.getuid}
Get uid of logged-in user

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>number</code> - User ID  
### userManage.getAppid() ⇒ <code>string</code> {#module_usermanage.getappid}
Get appid

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>string</code> - APP ID  
### userManage.getConversationList() ⇒ [<code>Array.&lt;ConversationItem&gt;</code>](types.md#module_types..conversationitem) {#module_usermanage.getconversationlist}
Get list of recent conversations

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
### userManage.asyncUpdateAvatar(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage.asyncupdateavatar}
Update avatar

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.avatar | <code>string</code> | Avatar url |

### userManage.asyncUpdateNickName(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage.asyncupdatenickname}
Update nickname

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.nick_name | <code>string</code> | Nickname |

### userManage.asyncGetProfile() ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types..userprofile) {#module_usermanage.asyncgetprofile}
Get user profile

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types..userprofile) - User information  
### userManage.asyncUpdateProfile(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage.asyncupdateprofile}
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

### userManage.asyncGetSettings() ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types..usersettings) {#module_usermanage.asyncgetsettings}
Get user settings

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types..usersettings) - User information  
### userManage.asyncUpdateSettings(settings) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage.asyncupdatesettings}
Modify user settings

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| settings | [<code>UserSettings</code>](types.md#module_types..usersettings) | Updated settings |
