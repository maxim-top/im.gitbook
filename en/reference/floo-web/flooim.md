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

InitializationSDK

**Kind**: static method of [`flooim`](flooim.md#module_flooim)\
**Returns**: `object` - flooim object

| Param            | Type                    | Description                                                                                                                                                                  |
| ---------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| config           | `object`                | SDK initialization settings                                                                                                                                                  |
| config.appid     | `string`                | APPID                                                                                                                                                                        |
| config.ws        | `boolean`               | Whether the connection address is prefixed with ws/wss: ture - the connection address is prefixed with ws or wss; false - the connection address is prefixed with http/https |
| config.autoLogin | `boolean`               | Whether to login automatically                                                                                                                                               |
| config.dnsServer | `string` \| `undefined` | DNS server address, can be empty, default https://dns.lanyingim.com/v2/app\_dns                                                                                              |
| config.logLevel  | `string`                | The log level of the SDK, the default is debug, and the value can be debug, info, warn, error or off, where off means no log is printed.                                     |

**Example**

```js
const config = {
// dnsServer: "https://dns.lanyingim.com/v2/app_dns",
appid: "YOUR_APP_ID",
ws: false, // The uniapp version needs to be set to true, the web version needs to be set to false
autoLogin: true
};
import flooim from 'floo-3.0.0';
const im = flooim(config);

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class=''></div>

```

### flooim.login(opt) <a href="#module_flooim__login" id="module_flooim__login"></a>

Login

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param        | Type     | Description |
| ------------ | -------- | ----------- |
| opt          | `object` |             |
| opt.name     | `string` | Username    |
| opt.password | `string` | Password    |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.qrlogin(opt) <a href="#module_flooim__qrlogin" id="module_flooim__qrlogin"></a>

QR code login

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param        | Type     | Description |
| ------------ | -------- | ----------- |
| opt          | `object` |             |
| opt.user\_id | `number` | User ID     |
| opt.password | `string` | Password    |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.tokenLogin(user\_id, token) <a href="#module_flooim__tokenlogin" id="module_flooim__tokenlogin"></a>

token login

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param    | Type     | Description |
| -------- | -------- | ----------- |
| user\_id | `number` | User ID     |
| token    | `string` | Token       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.idLogin(opt) <a href="#module_flooim__idlogin" id="module_flooim__idlogin"></a>

Login with user ID and password

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param        | Type     | Description |
| ------------ | -------- | ----------- |
| opt          | `object` |             |
| opt.user\_id | `number` | User ID     |
| opt.password | `string` | Password    |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.isLogin() ⇒ `boolean` <a href="#module_flooim__islogin" id="module_flooim__islogin"></a>

Logged in or not

**Kind**: static method of [`flooim`](flooim.md#module_flooim)\
**Returns**: `boolean` - Logged in or not\
**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.on(options, ext) <a href="#module_flooim__on" id="module_flooim__on"></a>

Event listening

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param   | Type                                                                                                                                                 | Description                                                   |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| options | [`Event`](types.md#module_types__event) \| Object.<[`Event`](types.md#module_types__event), [`EventCallback`](types.md#module_types__eventcallback)> | Can be event name, and also event name plus event callback    |
| ext     | [`EventCallback`](types.md#module_types__eventcallback) \| `undefined`                                                                               | Event callback, only required if options is set as event name |

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

Unlisten

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param   | Type                                                                                                                                                 | Description                                                   |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| options | [`Event`](types.md#module_types__event) \| Object.<[`Event`](types.md#module_types__event), [`EventCallback`](types.md#module_types__eventcallback)> | Can be event name, and also event name plus event callback    |
| ext     | [`EventCallback`](types.md#module_types__eventcallback) \| `undefined`                                                                               | Event callback, only required if options is set as event name |

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

Log out

**Kind**: static method of [`flooim`](flooim.md#module_flooim)\
**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>

```

### flooim.setLogLevel(logLevel) <a href="#module_flooim__setloglevel" id="module_flooim__setloglevel"></a>

set log level

**Kind**: static method of [`flooim`](flooim.md#module_flooim)

| Param    | Type     | Description                                                                                                                              |
| -------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| logLevel | `string` | The log level of the SDK, the default is debug, and the value can be debug, info, warn, error or off, where off means no log is printed. |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='im'></div>
```
