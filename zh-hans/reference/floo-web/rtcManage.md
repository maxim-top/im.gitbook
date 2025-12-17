# rtcManage

## rtcManage <a href="#module_rtcmanage" id="module_rtcmanage"></a>

音视频管理

* [rtcManage](rtcManage.md#module_rtcmanage)
  * [.initRTCEngine(params)](rtcManage.md#module_rtcmanage__initrtcengine) ⇒ `null`
  * [.destroy()](rtcManage.md#module_rtcmanage__destroy) ⇒ `null`
  * [.sendRTCMessage(msg)](rtcManage.md#module_rtcmanage__sendrtcmessage) ⇒ `number`
  * [.joinRoom(params)](rtcManage.md#module_rtcmanage__joinroom) ⇒ `null`
  * [.leaveRoom()](rtcManage.md#module_rtcmanage__leaveroom) ⇒ `null`
  * [.publish(type, hasVideo, hasAudio)](rtcManage.md#module_rtcmanage__publish) ⇒ `null`
  * [.unPublish()](rtcManage.md#module_rtcmanage__unpublish) ⇒ `null`
  * [.subscribe(sources)](rtcManage.md#module_rtcmanage__subscribe) ⇒ `null`
  * [.unSubscribe(id)](rtcManage.md#module_rtcmanage__unsubscribe) ⇒ `null`
  * [.muteLocalAudio(mute)](rtcManage.md#module_rtcmanage__mutelocalaudio) ⇒ `null`
  * [.muteLocalVideo(mute)](rtcManage.md#module_rtcmanage__mutelocalvideo) ⇒ `null`
  * [.muteRemoteAudio(stream, mute)](rtcManage.md#module_rtcmanage__muteremoteaudio) ⇒ `null`
  * [.muteRemoteVideo(stream, mute)](rtcManage.md#module_rtcmanage__muteremotevideo) ⇒ `null`
  * [.getJanusObject()](rtcManage.md#module_rtcmanage__getjanusobject) ⇒ `object`
  * [.getPublishHandler()](rtcManage.md#module_rtcmanage__getpublishhandler) ⇒ `object`
  * [.getSubscribeHandler()](rtcManage.md#module_rtcmanage__getsubscribehandler) ⇒ `object`

### rtcManage.initRTCEngine(params) ⇒ `null` <a href="#module_rtcmanage__initrtcengine" id="module_rtcmanage__initrtcengine"></a>

发起端发起音视频呼叫

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param                  | Type       | Description                                      |
| ---------------------- | ---------- | ------------------------------------------------ |
| params                 | `object`   | 初始化参数                                            |
| params.server          | `string`   | RTC服务器地址                                         |
| params.id              | `number`   | 音视频用户id                                          |
| params.caller          | `boolean`  | 是否为呼叫发起者                                         |
| params.receiver        | `number`   | 音视频用户对方id                                        |
| params.pin             | `string`   | 房间加入pin码（caller为true时发起者需要创建新的pin码）              |
| params.hasVideo        | `boolean`  | 是否存在视频流                                          |
| params.hasAudio        | `boolean`  | 是否存在音频流                                          |
| params.attachStream    | `function` | 音视频通话信息流处理函数                                     |
| params.getThrough      | `function` | 音视频通话是否接通                                        |
| params.hangupCall      | `function` | 音视频通话是否挂断                                        |
| params.getHangUpStatus | `function` | 获取挂断状态函数 以下是caller为 true 的必须参数（被呼叫者必须参数）         |
| params.roomId          | `number`   | 被呼叫者邀请加入的 room id 以下是caller为 true 的必须参数（呼叫者必须参数） |
| params.secret          | `string`   | 创建的房间操作密码                                        |
| params.callId          | `string`   | 创建音视频呼叫时音视频 callid 以下时视频会话必须的参数（视频宽度和高度设置函数）     |
| params.width           | `number`   | 视频流画面宽度                                          |
| params.height          | `number`   | 视频流画面高度                                          |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.destroy() ⇒ `null` <a href="#module_rtcmanage__destroy" id="module_rtcmanage__destroy"></a>

销毁操作（在关闭音视频界面时使用）

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Type   |
| ------ |
| `null` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.sendRTCMessage(msg) ⇒ `number` <a href="#module_rtcmanage__sendrtcmessage" id="module_rtcmanage__sendrtcmessage"></a>

发送音视频消息

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)\
**Returns**: `number` - 客户端生成的消息ID

| Param       | Type                 | Description |
| ----------- | -------------------- | ----------- |
| msg         | `object`             | 消息体         |
| msg.uid     | `string`             | 接收者ID       |
| msg.content | `string`             | 消息内容        |
| msg.config  | `string` \| `object` | 扩展字段        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.joinRoom(params) ⇒ `null` <a href="#module_rtcmanage__joinroom" id="module_rtcmanage__joinroom"></a>

加入房间操作

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param  | Type     | Description |
| ------ | -------- | ----------- |
| params | `object` | 初始化参数       |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.leaveRoom() ⇒ `null` <a href="#module_rtcmanage__leaveroom" id="module_rtcmanage__leaveroom"></a>

离开加入房间操作

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Type   |
| ------ |
| `null` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.publish(type, hasVideo, hasAudio) ⇒ `null` <a href="#module_rtcmanage__publish" id="module_rtcmanage__publish"></a>

发布本地流操作

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param    | Type      | Description |
| -------- | --------- | ----------- |
| type     | `enum`    | 禁止标记        |
| hasVideo | `boolean` | 是否发布视频      |
| hasAudio | `boolean` | 是否发布音频      |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.unPublish() ⇒ `null` <a href="#module_rtcmanage__unpublish" id="module_rtcmanage__unpublish"></a>

取消发布流操作

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Type   |
| ------ |
| `null` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.subscribe(sources) ⇒ `null` <a href="#module_rtcmanage__subscribe" id="module_rtcmanage__subscribe"></a>

订阅流信息操作

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param   | Type    |
| ------- | ------- |
| sources | `Array` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.unSubscribe(id) ⇒ `null` <a href="#module_rtcmanage__unsubscribe" id="module_rtcmanage__unsubscribe"></a>

取消订阅流操作

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param | Type     | Description |
| ----- | -------- | ----------- |
| id    | `number` | 取消订阅的流id    |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.muteLocalAudio(mute) ⇒ `null` <a href="#module_rtcmanage__mutelocalaudio" id="module_rtcmanage__mutelocalaudio"></a>

禁止本地发布音频流操作

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param | Type      | Description |
| ----- | --------- | ----------- |
| mute  | `boolean` | 禁止标记        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.muteLocalVideo(mute) ⇒ `null` <a href="#module_rtcmanage__mutelocalvideo" id="module_rtcmanage__mutelocalvideo"></a>

禁止本地发布视频流操作

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param | Type      | Description |
| ----- | --------- | ----------- |
| mute  | `boolean` | 禁止标记        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.muteRemoteAudio(stream, mute) ⇒ `null` <a href="#module_rtcmanage__muteremoteaudio" id="module_rtcmanage__muteremoteaudio"></a>

禁止远程订阅音频流操作

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param  | Type      | Description |
| ------ | --------- | ----------- |
| stream | `object`  | 订阅流对象       |
| mute   | `boolean` | 禁止标记        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.muteRemoteVideo(stream, mute) ⇒ `null` <a href="#module_rtcmanage__muteremotevideo" id="module_rtcmanage__muteremotevideo"></a>

禁止远程订阅视频流操作

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param  | Type      | Description |
| ------ | --------- | ----------- |
| stream | `object`  | 订阅流对象       |
| mute   | `boolean` | 禁止标记        |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.getJanusObject() ⇒ `object` <a href="#module_rtcmanage__getjanusobject" id="module_rtcmanage__getjanusobject"></a>

获取Janus对象句柄

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Type   |
| ------ |
| `null` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.getPublishHandler() ⇒ `object` <a href="#module_rtcmanage__getpublishhandler" id="module_rtcmanage__getpublishhandler"></a>

获取发布操作对象句柄

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Type   |
| ------ |
| `null` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.getSubscribeHandler() ⇒ `object` <a href="#module_rtcmanage__getsubscribehandler" id="module_rtcmanage__getsubscribehandler"></a>

获取订阅操作对象句柄

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Type   |
| ------ |
| `null` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>
```
