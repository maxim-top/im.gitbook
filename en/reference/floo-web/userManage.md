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
Get token of logged-in user

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>string</code> - User's token  
**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="getToken" %}{% endlanying_code_snippet %}
```
### userManage.getUid() ⇒ <code>number</code> {#module_usermanage__getuid}
Get uid of logged-in user

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>number</code> - User ID  
**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="getUid" %}{% endlanying_code_snippet %}
```
### userManage.getAppid() ⇒ <code>string</code> {#module_usermanage__getappid}
Get appid

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>string</code> - APP ID  
**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="getAppid" %}{% endlanying_code_snippet %}
```
### userManage.getConversationList() ⇒ [<code>Array.&lt;ConversationItem&gt;</code>](types.md#module_types__conversationitem) {#module_usermanage__getconversationlist}
Get list of recent conversations

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="getConversationList" %}{% endlanying_code_snippet %}
```
### userManage.getDeviceSN() ⇒ <code>number</code> {#module_usermanage__getdevicesn}
Get device serial number

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>number</code> - Device serial number  
**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="getDeviceSN" %}{% endlanying_code_snippet %}
```
### userManage.asyncBindDeviceToken(param) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncbinddevicetoken}
Bind push device

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| param | <code>object</code> | Bind request |
| param.device_sn | <code>number</code> | Device serial number |
| param.notifier_name | <code>string</code> | The certificate name, that is, the name set when uploading the certificate in the LanyingIM Console. |
| param.device_token | <code>string</code> | Push device token |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="asyncBindDeviceToken" %}{% endlanying_code_snippet %}
```
### userManage.asyncUnbindDeviceToken(param) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncunbinddevicetoken}
Unbind push device

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| param | <code>object</code> | Unbind request |
| param.deviceSn | <code>number</code> | Device serial number |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="asyncUnbindDeviceToken" %}{% endlanying_code_snippet %}
```
### userManage.asyncRegister(opt) ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings) {#module_usermanage__asyncregister}
User registeration

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings) - User settings  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> | User information |
| opt.username | <code>string</code> | Username |
| opt.password | <code>string</code> | Password |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="asyncRegister" %}{% endlanying_code_snippet %}
```
### userManage.asyncUpdateAvatar(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncupdateavatar}
Update avatar

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.avatar | <code>string</code> | Avatar url |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="asyncUpdateAvatar" %}{% endlanying_code_snippet %}
```
### userManage.asyncUpdateNickName(params) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncupdatenickname}
Update nickname

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | Parameter |
| params.nick_name | <code>string</code> | Nickname |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="asyncUpdateNickName" %}{% endlanying_code_snippet %}
```
### userManage.asyncGetProfile() ⇒ [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types__userprofile) {#module_usermanage__asyncgetprofile}
Get user profile

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserProfile&gt;</code>](types.md#module_types__userprofile) - User information  
**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="asyncGetProfile" %}{% endlanying_code_snippet %}
```
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

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="asyncUpdateProfile" %}{% endlanying_code_snippet %}
```
### userManage.asyncGetSettings() ⇒ [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings) {#module_usermanage__asyncgetsettings}
Get user settings

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: [<code>Promise.&lt;UserSettings&gt;</code>](types.md#module_types__usersettings) - User information  
**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="asyncGetSettings" %}{% endlanying_code_snippet %}
```
### userManage.asyncUpdateSettings(settings) ⇒ <code>Promise.&lt;boolean&gt;</code> {#module_usermanage__asyncupdatesettings}
Modify user settings

**Kind**: static method of [<code>userManage</code>](#module_usermanage)  
**Returns**: <code>Promise.&lt;boolean&gt;</code> - Success or not  

| Param | Type | Description |
| --- | --- | --- |
| settings | [<code>UserSettings</code>](types.md#module_types__usersettings) | Updated settings |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="userManage",function="asyncUpdateSettings" %}{% endlanying_code_snippet %}
```