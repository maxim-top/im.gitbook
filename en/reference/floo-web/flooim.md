# flooim
## flooim {#module_flooim}

* [flooim](#module_flooim)
    * [.flooim(config)](#module_flooim__flooim) ⇒ <code>object</code>
    * [.login(opt)](#module_flooim__login)
    * [.qrlogin(opt)](#module_flooim__qrlogin)
    * [.tokenLogin(opt)](#module_flooim__tokenlogin)
    * [.idLogin(opt)](#module_flooim__idlogin)
    * [.isLogin()](#module_flooim__islogin) ⇒ <code>boolean</code>
    * [.on(options, ext)](#module_flooim__on)
    * [.off(options, ext)](#module_flooim__off)
    * [.logout()](#module_flooim__logout)

### flooim.flooim(config) ⇒ <code>object</code> {#module_flooim__flooim}
InitializationSDK

**Kind**: static method of [<code>flooim</code>](#module_flooim)  
**Returns**: <code>object</code> - flooim object  

| Param | Type | Description |
| --- | --- | --- |
| config | <code>object</code> | SDK initialization settings |
| config.appid | <code>string</code> | APPID |
| config.ws | <code>boolean</code> | Whether the connection address is prefixed with ws/wss: ture - the connection address is prefixed with ws or wss; false - the connection address is prefixed with http/https |
| config.autoLogin | <code>boolean</code> | Whether to login automatically |
| config.dnsServer | <code>string</code> &#124; <code>undefined</code> | DNS server address, can be empty, default https://dns.lanyingim.com/v2/app_dns |

**Example**  
```js
const config = {
// dnsServer: "https://dns.lanyingim.com/v2/app_dns",
appid: "YOUR_APP_ID",
ws: false,
autoLogin: true
};
import flooim from 'floo-2.0.0';
const im = flooim(config);
```
### flooim.login(opt) {#module_flooim__login}
Login

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> |  |
| opt.name | <code>string</code> | Username |
| opt.password | <code>string</code> | Password |

### flooim.qrlogin(opt) {#module_flooim__qrlogin}
QR code login

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> |  |
| opt.user_id | <code>number</code> | User ID |
| opt.password | <code>string</code> | Password |

### flooim.tokenLogin(opt) {#module_flooim__tokenlogin}
token login

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> |  |
| opt.user_id | <code>number</code> | User ID |
| opt.token | <code>string</code> | Token |

### flooim.idLogin(opt) {#module_flooim__idlogin}
Login with user ID and password

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> |  |
| opt.user_id | <code>number</code> | User ID |
| opt.password | <code>string</code> | Password |

### flooim.isLogin() ⇒ <code>boolean</code> {#module_flooim__islogin}
Logged in or not

**Kind**: static method of [<code>flooim</code>](#module_flooim)  
**Returns**: <code>boolean</code> - Logged in or not  
### flooim.on(options, ext) {#module_flooim__on}
Event listening

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| options | [<code>Event</code>](types.md#module_types__event) &#124; Object.&lt;[<code>Event</code>](types.md#module_types__event), [<code>EventCallback</code>](types.md#module_types__eventcallback)&gt; | Can be event name, and also event name plus event callback |
| ext | [<code>EventCallback</code>](types.md#module_types__eventcallback) &#124; <code>undefined</code> | Event callback, only required if options is set as event name |

**Example**  
```js
const im = flooim(config);
im.on('event', (ret) => {
   //do something with ret
 })
 // or
im.on({
   eventName: (ret) => {
     //do something with ret
   },
   ...
 })
```
### flooim.off(options, ext) {#module_flooim__off}
Unlisten

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| options | [<code>Event</code>](types.md#module_types__event) &#124; Object.&lt;[<code>Event</code>](types.md#module_types__event), [<code>EventCallback</code>](types.md#module_types__eventcallback)&gt; | Can be event name, and also event name plus event callback |
| ext | [<code>EventCallback</code>](types.md#module_types__eventcallback) &#124; <code>undefined</code> | Event callback, only required if options is set as event name |

**Example**  
```js
const im = flooim(config);
 im.off('events', (ret) => {
   //do something with ret
 })
 // or
 im.off({
   eventName: (ret) => {
     //do something with ret
   },
 ...
 })
```
### flooim.logout() {#module_flooim__logout}
Log out

**Kind**: static method of [<code>flooim</code>](#module_flooim)  
