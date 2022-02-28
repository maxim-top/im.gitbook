# flooim
## flooim {#module_flooim}

* [flooim](#module_flooim)
    * [.flooim(config)](#module_flooim.flooim) ⇒ <code>object</code>
    * [.login(opt)](#module_flooim.login)
    * [.qrlogin(opt)](#module_flooim.qrlogin)
    * [.tokenLogin(opt)](#module_flooim.tokenlogin)
    * [.idLogin(opt)](#module_flooim.idlogin)
    * [.isLogin()](#module_flooim.islogin) ⇒ <code>boolean</code>
    * [.on(options, ext)](#module_flooim.on)
    * [.off(options, ext)](#module_flooim.off)
    * [.logout()](#module_flooim.logout)

### flooim.flooim(config) ⇒ <code>object</code> {#module_flooim.flooim}
初始化SDK

**Kind**: static method of [<code>flooim</code>](#module_flooim)  
**Returns**: <code>object</code> - flooim对象  

| Param | Type | Description |
| --- | --- | --- |
| config | <code>object</code> | SDK初始化设置 |
| config.appid | <code>string</code> | APPID |
| config.ws | <code>boolean</code> | 连接地址前缀是否为ws/wss: true - 连接地址前缀为ws或wss, false - 连接地址前缀为http/https |
| config.autoLogin | <code>boolean</code> | 是否自动登录 |
| config.dnsServer | <code>string</code> \| <code>undefined</code> | DNS服务器地址， 可以不设置，默认为 https://dns.maximtop.com/v2/app_dns |

**Example**  
```js
const config = {
// dnsServer: "https://dns.maximtop.com/v2/app_dns",
appid: "YOUR_APP_ID",
ws: false,
autoLogin: true
};
import flooim from 'floo-2.0.0';
const im = flooim(config);
```
### flooim.login(opt) {#module_flooim.login}
登录

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> |  |
| opt.name | <code>string</code> | 用户名 |
| opt.password | <code>string</code> | 密码 |

### flooim.qrlogin(opt) {#module_flooim.qrlogin}
二维码登录

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> |  |
| opt.user_id | <code>number</code> | 用户ID |
| opt.password | <code>string</code> | 密码 |

### flooim.tokenLogin(opt) {#module_flooim.tokenlogin}
token登录

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> |  |
| opt.user_id | <code>number</code> | 用户ID |
| opt.token | <code>string</code> | Token |

### flooim.idLogin(opt) {#module_flooim.idlogin}
使用用户ID和密码登录

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> |  |
| opt.user_id | <code>number</code> | 用户ID |
| opt.password | <code>string</code> | 密码 |

### flooim.isLogin() ⇒ <code>boolean</code> {#module_flooim.islogin}
是否已登录

**Kind**: static method of [<code>flooim</code>](#module_flooim)  
**Returns**: <code>boolean</code> - 是否已登录  
### flooim.on(options, ext) {#module_flooim.on}
事件监听

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| options | [<code>Event</code>](types.md#module_types..event) \| <code>Object.&lt;module:types~Event, module:types~EventCallback&gt;</code> | 可以为事件名，也可以为事件名和事件回调 |
| ext | [<code>EventCallback</code>](types.md#module_types..eventcallback) \| <code>undefined</code> | 事件回调，只有options为事件名时需要设置 |

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
### flooim.off(options, ext) {#module_flooim.off}
取消监听

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| options | [<code>Event</code>](types.md#module_types..event) \| <code>Object.&lt;module:types~Event, module:types~EventCallback&gt;</code> | 可以为事件名，也可以为事件名和事件回调 |
| ext | [<code>EventCallback</code>](types.md#module_types..eventcallback) \| <code>undefined</code> | 事件回调，只有options为事件名时需要设置 |

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
### flooim.logout() {#module_flooim.logout}
退出账户

**Kind**: static method of [<code>flooim</code>](#module_flooim)  
