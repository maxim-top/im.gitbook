# flooim
## flooim {#module_flooim}

* [flooim](#module_flooim)
    * [.flooim(config)](#module_flooim__flooim) ⇒ <code>object</code>
    * [.login(opt)](#module_flooim__login)
    * [.qrlogin(opt)](#module_flooim__qrlogin)
    * [.tokenLogin(user_id, token)](#module_flooim__tokenlogin)
    * [.idLogin(opt)](#module_flooim__idlogin)
    * [.isLogin()](#module_flooim__islogin) ⇒ <code>boolean</code>
    * [.on(options, ext)](#module_flooim__on)
    * [.off(options, ext)](#module_flooim__off)
    * [.logout()](#module_flooim__logout)

### flooim.flooim(config) ⇒ <code>object</code> {#module_flooim__flooim}
初始化SDK

**Kind**: static method of [<code>flooim</code>](#module_flooim)  
**Returns**: <code>object</code> - flooim对象  

| Param | Type | Description |
| --- | --- | --- |
| config | <code>object</code> | SDK初始化设置 |
| config.appid | <code>string</code> | APPID |
| config.ws | <code>boolean</code> | 连接地址前缀是否为ws/wss: true - 连接地址前缀为ws或wss, false - 连接地址前缀为http/https |
| config.autoLogin | <code>boolean</code> | 是否自动登录 |
| config.dnsServer | <code>string</code> &#124; <code>undefined</code> | DNS服务器地址， 可以不设置，默认为 https://dns.lanyingim.com/v2/app_dns |

**Example**  
```js
const config = {
// dnsServer: "https://dns.lanyingim.com/v2/app_dns",
appid: "YOUR_APP_ID",
ws: false, // uniapp版需要设置为true, web版需要设置为false
autoLogin: true
};
import flooim from 'floo-2.0.0';
const im = flooim(config);
{% lanying_code_snippet repo="lanying-im-web",class="",function="flooim" %}{% endlanying_code_snippet %}
```
### flooim.login(opt) {#module_flooim__login}
登录

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> |  |
| opt.name | <code>string</code> | 用户名 |
| opt.password | <code>string</code> | 密码 |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="im",function="login" %}{% endlanying_code_snippet %}
```
### flooim.qrlogin(opt) {#module_flooim__qrlogin}
二维码登录

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> |  |
| opt.user_id | <code>number</code> | 用户ID |
| opt.password | <code>string</code> | 密码 |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="im",function="qrlogin" %}{% endlanying_code_snippet %}
```
### flooim.tokenLogin(user_id, token) {#module_flooim__tokenlogin}
token登录

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| user_id | <code>number</code> | 用户ID |
| token | <code>string</code> | Token |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="im",function="tokenLogin" %}{% endlanying_code_snippet %}
```
### flooim.idLogin(opt) {#module_flooim__idlogin}
使用用户ID和密码登录

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| opt | <code>object</code> |  |
| opt.user_id | <code>number</code> | 用户ID |
| opt.password | <code>string</code> | 密码 |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="im",function="idLogin" %}{% endlanying_code_snippet %}
```
### flooim.isLogin() ⇒ <code>boolean</code> {#module_flooim__islogin}
是否已登录

**Kind**: static method of [<code>flooim</code>](#module_flooim)  
**Returns**: <code>boolean</code> - 是否已登录  
**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="im",function="isLogin" %}{% endlanying_code_snippet %}
```
### flooim.on(options, ext) {#module_flooim__on}
事件监听

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| options | [<code>Event</code>](types.md#module_types__event) &#124; Object.&lt;[<code>Event</code>](types.md#module_types__event), [<code>EventCallback</code>](types.md#module_types__eventcallback)&gt; | 可以为事件名，也可以为事件名和事件回调 |
| ext | [<code>EventCallback</code>](types.md#module_types__eventcallback) &#124; <code>undefined</code> | 事件回调，只有options为事件名时需要设置 |

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
{% lanying_code_snippet repo="lanying-im-web",class="im",function="on" %}{% endlanying_code_snippet %}
```
### flooim.off(options, ext) {#module_flooim__off}
取消监听

**Kind**: static method of [<code>flooim</code>](#module_flooim)  

| Param | Type | Description |
| --- | --- | --- |
| options | [<code>Event</code>](types.md#module_types__event) &#124; Object.&lt;[<code>Event</code>](types.md#module_types__event), [<code>EventCallback</code>](types.md#module_types__eventcallback)&gt; | 可以为事件名，也可以为事件名和事件回调 |
| ext | [<code>EventCallback</code>](types.md#module_types__eventcallback) &#124; <code>undefined</code> | 事件回调，只有options为事件名时需要设置 |

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
{% lanying_code_snippet repo="lanying-im-web",class="im",function="off" %}{% endlanying_code_snippet %}
```
### flooim.logout() {#module_flooim__logout}
退出账户

**Kind**: static method of [<code>flooim</code>](#module_flooim)  
**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="im",function="logout" %}{% endlanying_code_snippet %}
```
