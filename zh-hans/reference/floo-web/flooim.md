# flooim

## flooim <a href="#module_flooim" id="module_flooim"></a>

* [flooim](flooim.md#module_flooim)
  * [.flooim(config)](flooim.md#module_flooim__flooim) ⇒ `object`
  * [.login(opt)](flooim.md#module_flooim__login)
  * [.qrlogin(opt)](flooim.md#module_flooim__qrlogin)
  * [.tokenLogin(user\_id, token)](flooim.md#module_flooim__tokenlogin)
  * [.idLogin(opt)](flooim.md#module_flooim__idlogin)
  * [.isLogin()](flooim.md#module_flooim__islogin) ⇒ `boolean`
  * [.on(options, ext)](flooim.md#module_flooim__on)
  * [.off(options, ext)](flooim.md#module_flooim__off)
  * [.logout()](flooim.md#module_flooim__logout)
  * [.setLogLevel(logLevel)](flooim.md#module_flooim__setloglevel)

### flooim.flooim(config) ⇒ `object` <a href="#module_flooim__flooim" id="module_flooim__flooim"></a>

初始化SDK

**Kind**: static method of [`flooim`](flooim.md#module_flooim)\
**Returns**: `object` - flooim对象

| Param            | Type                    | Description                                                       |
| ---------------- | ----------------------- | ----------------------------------------------------------------- |
| config           | `object`                | SDK初始化设置                                                          |
| config.appid     | `string`                | APPID                                                             |
| config.ws        | `boolean`               | 连接地址前缀是否为ws/wss: true - 连接地址前缀为ws或wss, false - 连接地址前缀为http/https  |
| config.autoLogin | `boolean`               | 是否自动登录                                                            |
| config.dnsServer | `string` \| `undefined` | DNS服务器地址， 可以不设置，默认为 https://dns.lanyingim.com/v2/app\_dns         |
| config.logLevel  | `string`                | SDK的日志等级， 默认为debug, 取值为 debug、info、warn、error 或 off, 其中off为不打印日志。 |

**Example**

```js
const config = {
// dnsServer: "https://dns.lanyingim.com/v2/app_dns",
appid: "YOUR_APP_ID",
ws: false, // uniapp版需要设置为true, web版需要设置为false
autoLogin: true
};
import flooim from 'floo-3.0.0';
const im = flooim(config);

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class=''></div>

```

### flooim.login(opt) <a href="#module_flooim__login" id="module_flooim__login"></a>

登录

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param        | Type     | Description |
| ------------ | -------- | ----------- |
| opt          | `object` |             |
| opt.name     | `string` | 用户名         |
| opt.password | `string` | 密码          |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.qrlogin(opt) <a href="#module_flooim__qrlogin" id="module_flooim__qrlogin"></a>

二维码登录

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param        | Type     | Description |
| ------------ | -------- | ----------- |
| opt          | `object` |             |
| opt.user\_id | `number` | 用户ID        |
| opt.password | `string` | 密码          |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.tokenLogin(user\_id, token) <a href="#module_flooim__tokenlogin" id="module_flooim__tokenlogin"></a>

token登录

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param    | Type     | Description |
| -------- | -------- | ----------- |
| user\_id | `number` | 用户ID        |
| token    | `string` | Token       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.idLogin(opt) <a href="#module_flooim__idlogin" id="module_flooim__idlogin"></a>

使用用户ID和密码登录

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param        | Type     | Description |
| ------------ | -------- | ----------- |
| opt          | `object` |             |
| opt.user\_id | `number` | 用户ID        |
| opt.password | `string` | 密码          |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.isLogin() ⇒ `boolean` <a href="#module_flooim__islogin" id="module_flooim__islogin"></a>

是否已登录

**Kind**: static method of [`flooim`](flooim.md#module_flooim)\
**Returns**: `boolean` - 是否已登录\
**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.on(options, ext) <a href="#module_flooim__on" id="module_flooim__on"></a>

事件监听

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param   | Type                                                                                                                                                 | Description             |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| options | [`Event`](types.md#module_types__event) \| Object.<[`Event`](types.md#module_types__event), [`EventCallback`](types.md#module_types__eventcallback)> | 可以为事件名，也可以为事件名和事件回调     |
| ext     | [`EventCallback`](types.md#module_types__eventcallback) \| `undefined`                                                                               | 事件回调，只有options为事件名时需要设置 |

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.off(options, ext) <a href="#module_flooim__off" id="module_flooim__off"></a>

取消监听

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param   | Type                                                                                                                                                 | Description             |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| options | [`Event`](types.md#module_types__event) \| Object.<[`Event`](types.md#module_types__event), [`EventCallback`](types.md#module_types__eventcallback)> | 可以为事件名，也可以为事件名和事件回调     |
| ext     | [`EventCallback`](types.md#module_types__eventcallback) \| `undefined`                                                                               | 事件回调，只有options为事件名时需要设置 |

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

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.logout() <a href="#module_flooim__logout" id="module_flooim__logout"></a>

退出账户

**Kind**: static method of [`flooim`](flooim.md#module_flooim)\
**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.setLogLevel(logLevel) <a href="#module_flooim__setloglevel" id="module_flooim__setloglevel"></a>

设置日志等级

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param    | Type     | Description                                                       |
| -------- | -------- | ----------------------------------------------------------------- |
| logLevel | `string` | SDK的日志等级， 默认为debug, 取值为 debug、info、warn、error 或 off, 其中off为不打印日志。 |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>
```
