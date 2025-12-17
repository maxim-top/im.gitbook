# rtcManage

## rtcManage <a href="#module_rtcmanage" id="module_rtcmanage"></a>

RTC management

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

Initiate an audio and video call

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param              | Type      | Description                 |
| ------------------ | --------- | --------------------------- |
| params             | `object`  | initialization parameter    |
| params.server      | `string`  | RTC server address          |
| params.id          | `number`  | user id                     |
| params.name        | `string`  | user name                   |
| params.receiver    | `number`  | receiver id                 |
| params.caller      | `boolean` | user is caller or not       |
| params.secret      | `string`  | create rtc room secret      |
| params.pin         | `string`  | join room pin code          |
| params.hasVideo    | `boolean` | has video stream            |
| params.hasAudio    | `boolean` | has audio stream            |
| params.width       | `number`  | video width                 |
| params.height      | `number`  | video height                |
| params.localVideo  | `string`  | local video document id     |
| params.remoteVideo | `string`  | remote video document id    |
| params.remoteAudio | `string`  | remote audio document id    |
| params.getThrough  | `boolean` | getThrough process function |
| params.hangupCall  | `boolean` | hangupCall process function |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.destroy() ⇒ `null` <a href="#module_rtcmanage__destroy" id="module_rtcmanage__destroy"></a>

Destroy function（destroy rtc environment）

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Type   |
| ------ |
| `null` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.sendRTCMessage(msg) ⇒ `number` <a href="#module_rtcmanage__sendrtcmessage" id="module_rtcmanage__sendrtcmessage"></a>

Send RTC message

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)\
**Returns**: `number` - client generate RTC message id

| Param       | Type                 | Description           |
| ----------- | -------------------- | --------------------- |
| msg         | `object`             | message body          |
| msg.uid     | `string`             | receiver ID           |
| msg.content | `string`             | message content       |
| msg.config  | `string` \| `object` | message config fields |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.joinRoom(params) ⇒ `null` <a href="#module_rtcmanage__joinroom" id="module_rtcmanage__joinroom"></a>

Join RTC room

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param  | Type     | Description               |
| ------ | -------- | ------------------------- |
| params | `object` | initialization parameters |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.leaveRoom() ⇒ `null` <a href="#module_rtcmanage__leaveroom" id="module_rtcmanage__leaveroom"></a>

Leave RTC room

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Type   |
| ------ |
| `null` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.publish(type, hasVideo, hasAudio) ⇒ `null` <a href="#module_rtcmanage__publish" id="module_rtcmanage__publish"></a>

Publish local video/audio streams

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param    | Type      | Description      |
| -------- | --------- | ---------------- |
| type     | `enum`    | disable flag     |
| hasVideo | `boolean` | has video stream |
| hasAudio | `boolean` | has audio stream |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.unPublish() ⇒ `null` <a href="#module_rtcmanage__unpublish" id="module_rtcmanage__unpublish"></a>

Unpublish operation

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Type   |
| ------ |
| `null` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.subscribe(sources) ⇒ `null` <a href="#module_rtcmanage__subscribe" id="module_rtcmanage__subscribe"></a>

Subscribe remote video/audio streams

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param   | Type    |
| ------- | ------- |
| sources | `Array` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.unSubscribe(id) ⇒ `null` <a href="#module_rtcmanage__unsubscribe" id="module_rtcmanage__unsubscribe"></a>

UnSubscribe stream operation

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param | Type     | Description           |
| ----- | -------- | --------------------- |
| id    | `number` | unSubscribe stream id |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.muteLocalAudio(mute) ⇒ `null` <a href="#module_rtcmanage__mutelocalaudio" id="module_rtcmanage__mutelocalaudio"></a>

Mute local audio or not

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param | Type      | Description |
| ----- | --------- | ----------- |
| mute  | `boolean` | mute flag   |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.muteLocalVideo(mute) ⇒ `null` <a href="#module_rtcmanage__mutelocalvideo" id="module_rtcmanage__mutelocalvideo"></a>

Mute local video or not

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param | Type      | Description |
| ----- | --------- | ----------- |
| mute  | `boolean` | mute flag   |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.muteRemoteAudio(stream, mute) ⇒ `null` <a href="#module_rtcmanage__muteremoteaudio" id="module_rtcmanage__muteremoteaudio"></a>

Mute remote audio or not

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param  | Type      | Description    |
| ------ | --------- | -------------- |
| stream | `object`  | mute stream id |
| mute   | `boolean` | mute flag      |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.muteRemoteVideo(stream, mute) ⇒ `null` <a href="#module_rtcmanage__muteremotevideo" id="module_rtcmanage__muteremotevideo"></a>

Mute remote video or not

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Param  | Type      | Description    |
| ------ | --------- | -------------- |
| stream | `object`  | mute stream id |
| mute   | `boolean` | mute flag      |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.getJanusObject() ⇒ `object` <a href="#module_rtcmanage__getjanusobject" id="module_rtcmanage__getjanusobject"></a>

Get janus object handler

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Type   |
| ------ |
| `null` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.getPublishHandler() ⇒ `object` <a href="#module_rtcmanage__getpublishhandler" id="module_rtcmanage__getpublishhandler"></a>

Get publisher object handler

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Type   |
| ------ |
| `null` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>

```

### rtcManage.getSubscribeHandler() ⇒ `object` <a href="#module_rtcmanage__getsubscribehandler" id="module_rtcmanage__getsubscribehandler"></a>

Get subscriber object handler

**Kind**: static method of [`rtcManage`](rtcManage.md#module_rtcmanage)

| Type   |
| ------ |
| `null` |

**Example**

```js

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-web' data-class='rtcManage'></div>
```
