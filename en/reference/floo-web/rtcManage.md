# rtcManage
## rtcManage {#module_rtcmanage}
RTC management


* [rtcManage](#module_rtcmanage)
    * [.initRTCEngine(params)](#module_rtcmanage__initrtcengine) ⇒ <code>null</code>
    * [.destroy()](#module_rtcmanage__destroy) ⇒ <code>null</code>
    * [.sendRTCMessage(msg)](#module_rtcmanage__sendrtcmessage) ⇒ <code>number</code>
    * [.joinRoom(params)](#module_rtcmanage__joinroom) ⇒ <code>null</code>
    * [.leaveRoom()](#module_rtcmanage__leaveroom) ⇒ <code>null</code>
    * [.publish(type, hasVideo, hasAudio)](#module_rtcmanage__publish) ⇒ <code>null</code>
    * [.unPublish()](#module_rtcmanage__unpublish) ⇒ <code>null</code>
    * [.subscribe(sources)](#module_rtcmanage__subscribe) ⇒ <code>null</code>
    * [.unSubscribe(id)](#module_rtcmanage__unsubscribe) ⇒ <code>null</code>
    * [.muteLocalAudio(mute)](#module_rtcmanage__mutelocalaudio) ⇒ <code>null</code>
    * [.muteLocalVideo(mute)](#module_rtcmanage__mutelocalvideo) ⇒ <code>null</code>
    * [.muteRemoteAudio(stream, mute)](#module_rtcmanage__muteremoteaudio) ⇒ <code>null</code>
    * [.muteRemoteVideo(stream, mute)](#module_rtcmanage__muteremotevideo) ⇒ <code>null</code>
    * [.getJanusObject()](#module_rtcmanage__getjanusobject) ⇒ <code>object</code>
    * [.getPublishHandler()](#module_rtcmanage__getpublishhandler) ⇒ <code>object</code>
    * [.getSubscribeHandler()](#module_rtcmanage__getsubscribehandler) ⇒ <code>object</code>

### rtcManage.initRTCEngine(params) ⇒ <code>null</code> {#module_rtcmanage__initrtcengine}
Initiate an audio and video call

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | initialization parameter |
| params.server | <code>string</code> | RTC server address |
| params.id | <code>number</code> | user id |
| params.name | <code>string</code> | user name |
| params.receiver | <code>number</code> | receiver id |
| params.caller | <code>boolean</code> | user is caller or not |
| params.secret | <code>string</code> | create rtc room secret |
| params.pin | <code>string</code> | join room pin code |
| params.hasVideo | <code>boolean</code> | has video stream |
| params.hasAudio | <code>boolean</code> | has audio stream |
| params.width | <code>number</code> | video width |
| params.height | <code>number</code> | video height |
| params.localVideo | <code>string</code> | local video document id |
| params.remoteVideo | <code>string</code> | remote video document id |
| params.remoteAudio | <code>string</code> | remote audio document id |
| params.getThrough | <code>boolean</code> | getThrough process function |
| params.hangupCall | <code>boolean</code> | hangupCall process function |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="initRTCEngine" %}{% endlanying_code_snippet %}
```
### rtcManage.destroy() ⇒ <code>null</code> {#module_rtcmanage__destroy}
Destroy function（destroy rtc environment）

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Type |
| --- |
| <code>null</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="destroy" %}{% endlanying_code_snippet %}
```
### rtcManage.sendRTCMessage(msg) ⇒ <code>number</code> {#module_rtcmanage__sendrtcmessage}
Send RTC message

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  
**Returns**: <code>number</code> - client generate RTC message id  

| Param | Type | Description |
| --- | --- | --- |
| msg | <code>object</code> | message body |
| msg.uid | <code>string</code> | receiver ID |
| msg.content | <code>string</code> | message content |
| msg.config | <code>string</code> &#124; <code>object</code> | message config fields |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="sendRTCMessage" %}{% endlanying_code_snippet %}
```
### rtcManage.joinRoom(params) ⇒ <code>null</code> {#module_rtcmanage__joinroom}
Join RTC room

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | initialization parameters |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="joinRoom" %}{% endlanying_code_snippet %}
```
### rtcManage.leaveRoom() ⇒ <code>null</code> {#module_rtcmanage__leaveroom}
Leave RTC room

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Type |
| --- |
| <code>null</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="leaveRoom" %}{% endlanying_code_snippet %}
```
### rtcManage.publish(type, hasVideo, hasAudio) ⇒ <code>null</code> {#module_rtcmanage__publish}
Publish local video/audio streams

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| type | <code>enum</code> | disable flag |
| hasVideo | <code>boolean</code> | has video stream |
| hasAudio | <code>boolean</code> | has audio stream |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="publish" %}{% endlanying_code_snippet %}
```
### rtcManage.unPublish() ⇒ <code>null</code> {#module_rtcmanage__unpublish}
Unpublish operation

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Type |
| --- |
| <code>null</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="publish" %}{% endlanying_code_snippet %}
```
### rtcManage.subscribe(sources) ⇒ <code>null</code> {#module_rtcmanage__subscribe}
Subscribe remote video/audio streams

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type |
| --- | --- |
| sources | <code>Array</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="subscribe" %}{% endlanying_code_snippet %}
```
### rtcManage.unSubscribe(id) ⇒ <code>null</code> {#module_rtcmanage__unsubscribe}
UnSubscribe stream operation

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| id | <code>number</code> | unSubscribe stream id |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="unSubscribe" %}{% endlanying_code_snippet %}
```
### rtcManage.muteLocalAudio(mute) ⇒ <code>null</code> {#module_rtcmanage__mutelocalaudio}
Mute local audio or not

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| mute | <code>boolean</code> | mute flag |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="muteLocalAudio" %}{% endlanying_code_snippet %}
```
### rtcManage.muteLocalVideo(mute) ⇒ <code>null</code> {#module_rtcmanage__mutelocalvideo}
Mute local video or not

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| mute | <code>boolean</code> | mute flag |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="muteLocalVideo" %}{% endlanying_code_snippet %}
```
### rtcManage.muteRemoteAudio(stream, mute) ⇒ <code>null</code> {#module_rtcmanage__muteremoteaudio}
Mute remote audio or not

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| stream | <code>object</code> | mute stream id |
| mute | <code>boolean</code> | mute flag |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="muteRemoteAudio" %}{% endlanying_code_snippet %}
```
### rtcManage.muteRemoteVideo(stream, mute) ⇒ <code>null</code> {#module_rtcmanage__muteremotevideo}
Mute remote video or not

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| stream | <code>object</code> | mute stream id |
| mute | <code>boolean</code> | mute flag |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="muteRemoteVideo" %}{% endlanying_code_snippet %}
```
### rtcManage.getJanusObject() ⇒ <code>object</code> {#module_rtcmanage__getjanusobject}
Get janus object handler

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Type |
| --- |
| <code>null</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="getJanusObject" %}{% endlanying_code_snippet %}
```
### rtcManage.getPublishHandler() ⇒ <code>object</code> {#module_rtcmanage__getpublishhandler}
Get publisher object handler

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Type |
| --- |
| <code>null</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="getPublishHandler" %}{% endlanying_code_snippet %}
```
### rtcManage.getSubscribeHandler() ⇒ <code>object</code> {#module_rtcmanage__getsubscribehandler}
Get subscriber object handler

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Type |
| --- |
| <code>null</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="getSubscribeHandler" %}{% endlanying_code_snippet %}
```