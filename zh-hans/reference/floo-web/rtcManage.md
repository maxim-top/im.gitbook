# rtcManage
## rtcManage {#module_rtcmanage}
音视频管理


* [rtcManage](#module_rtcmanage)
    * _static_
        * [.initRTCEngine(params)](#module_rtcmanage__initrtcengine) ⇒ <code>null</code>
        * [.destroy()](#module_rtcmanage__destroy) ⇒ <code>null</code>
        * [.sendRTCMessage(msg)](#module_rtcmanage__sendrtcmessage) ⇒ <code>number</code>
        * [.joinRoom(params)](#module_rtcmanage__joinroom) ⇒ <code>null</code>
        * [.leaveRoom()](#module_rtcmanage__leaveroom) ⇒ <code>null</code>
        * [.publish(type, hasVideo, hasAudio)](#module_rtcmanage__publish) ⇒ <code>null</code>
        * [.unPublish()](#module_rtcmanage__unpublish) ⇒ <code>null</code>
        * [.subscribe(sources)](#module_rtcmanage__subscribe) ⇒ <code>null</code>
        * [.muteLocalAudio(mute)](#module_rtcmanage__mutelocalaudio) ⇒ <code>null</code>
        * [.muteLocalVideo(mute)](#module_rtcmanage__mutelocalvideo) ⇒ <code>null</code>
        * [.muteRemoteAudio(stream, mute)](#module_rtcmanage__muteremoteaudio) ⇒ <code>null</code>
        * [.muteRemoteVideo(stream, mute)](#module_rtcmanage__muteremotevideo) ⇒ <code>null</code>
        * [.getJanusObject()](#module_rtcmanage__getjanusobject) ⇒ <code>object</code>
        * [.getPublishHandler()](#module_rtcmanage__getpublishhandler) ⇒ <code>object</code>
        * [.getSubscribeHandler()](#module_rtcmanage__getsubscribehandler) ⇒ <code>object</code>
    * _inner_
        * [~unSubscribe(id)](#module_rtcmanage__unsubscribe) ⇒ <code>null</code>

### rtcManage.initRTCEngine(params) ⇒ <code>null</code> {#module_rtcmanage__initrtcengine}
发起端发起音视频呼叫

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 初始化参数 |
| params.server | <code>string</code> | RTC服务器地址 |
| params.id | <code>number</code> | 音视频用户id |
| params.name | <code>string</code> | 音视频用户名称 |
| params.receiver | <code>number</code> | 音视频用户对方id |
| params.caller | <code>boolean</code> | 是否为呼叫发起者 |
| params.secret | <code>string</code> | 创建的房间操作密码 |
| params.pin | <code>string</code> | 创建的房间加入pin码 |
| params.hasVideo | <code>boolean</code> | 是否存在视频流 |
| params.hasAudio | <code>boolean</code> | 是否存在音频流 |
| params.width | <code>number</code> | 视频流画面宽度 |
| params.height | <code>number</code> | 视频流画面高度 |
| params.localVideo | <code>string</code> | 本地video标签id |
| params.remoteVideo | <code>string</code> | 远程video标签id |
| params.remoteAudio | <code>string</code> | 远程audio标签id |
| params.getThrough | <code>boolean</code> | 音视频通话是否接通 |
| params.hangupCall | <code>boolean</code> | 音视频通话是否挂断 |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="initRTCEngine" %}{% endlanying_code_snippet %}
```
### rtcManage.destroy() ⇒ <code>null</code> {#module_rtcmanage__destroy}
销毁操作（在关闭音视频界面时使用）

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Type |
| --- |
| <code>null</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="destroy" %}{% endlanying_code_snippet %}
```
### rtcManage.sendRTCMessage(msg) ⇒ <code>number</code> {#module_rtcmanage__sendrtcmessage}
发送音视频消息

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  
**Returns**: <code>number</code> - 客户端生成的消息ID  

| Param | Type | Description |
| --- | --- | --- |
| msg | <code>object</code> | 消息体 |
| msg.uid | <code>string</code> | 接收者ID |
| msg.content | <code>string</code> | 消息内容 |
| msg.config | <code>string</code> &#124; <code>object</code> | 扩展字段 |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="sendRTCMessage" %}{% endlanying_code_snippet %}
```
### rtcManage.joinRoom(params) ⇒ <code>null</code> {#module_rtcmanage__joinroom}
加入房间操作

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| params | <code>object</code> | 初始化参数 |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="joinRoom" %}{% endlanying_code_snippet %}
```
### rtcManage.leaveRoom() ⇒ <code>null</code> {#module_rtcmanage__leaveroom}
离开加入房间操作

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Type |
| --- |
| <code>null</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="leaveRoom" %}{% endlanying_code_snippet %}
```
### rtcManage.publish(type, hasVideo, hasAudio) ⇒ <code>null</code> {#module_rtcmanage__publish}
发布本地流操作

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| type | <code>enum</code> | 禁止标记 |
| hasVideo | <code>boolean</code> | 是否发布视频 |
| hasAudio | <code>boolean</code> | 是否发布音频 |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="publish" %}{% endlanying_code_snippet %}
```
### rtcManage.unPublish() ⇒ <code>null</code> {#module_rtcmanage__unpublish}
取消发布流操作

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Type |
| --- |
| <code>null</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="publish" %}{% endlanying_code_snippet %}
```
### rtcManage.subscribe(sources) ⇒ <code>null</code> {#module_rtcmanage__subscribe}
订阅流信息操作

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type |
| --- | --- |
| sources | <code>Array</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="subscribe" %}{% endlanying_code_snippet %}
```
### rtcManage.muteLocalAudio(mute) ⇒ <code>null</code> {#module_rtcmanage__mutelocalaudio}
禁止本地发布音频流操作

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| mute | <code>boolean</code> | 禁止标记 |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="muteLocalAudio" %}{% endlanying_code_snippet %}
```
### rtcManage.muteLocalVideo(mute) ⇒ <code>null</code> {#module_rtcmanage__mutelocalvideo}
禁止本地发布视频流操作

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| mute | <code>boolean</code> | 禁止标记 |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="muteLocalVideo" %}{% endlanying_code_snippet %}
```
### rtcManage.muteRemoteAudio(stream, mute) ⇒ <code>null</code> {#module_rtcmanage__muteremoteaudio}
禁止远程订阅音频流操作

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| stream | <code>object</code> | 订阅流对象 |
| mute | <code>boolean</code> | 禁止标记 |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="muteRemoteAudio" %}{% endlanying_code_snippet %}
```
### rtcManage.muteRemoteVideo(stream, mute) ⇒ <code>null</code> {#module_rtcmanage__muteremotevideo}
禁止远程订阅视频流操作

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| stream | <code>object</code> | 订阅流对象 |
| mute | <code>boolean</code> | 禁止标记 |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="muteRemoteVideo" %}{% endlanying_code_snippet %}
```
### rtcManage.getJanusObject() ⇒ <code>object</code> {#module_rtcmanage__getjanusobject}
获取Janus对象句柄

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Type |
| --- |
| <code>null</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="getJanusObject" %}{% endlanying_code_snippet %}
```
### rtcManage.getPublishHandler() ⇒ <code>object</code> {#module_rtcmanage__getpublishhandler}
获取发布操作对象句柄

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Type |
| --- |
| <code>null</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="getPublishHandler" %}{% endlanying_code_snippet %}
```
### rtcManage.getSubscribeHandler() ⇒ <code>object</code> {#module_rtcmanage__getsubscribehandler}
获取订阅操作对象句柄

**Kind**: static method of [<code>rtcManage</code>](#module_rtcmanage)  

| Type |
| --- |
| <code>null</code> | 

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="getSubscribeHandler" %}{% endlanying_code_snippet %}
```
### rtcManage~unSubscribe(id) ⇒ <code>null</code> {#module_rtcmanage__unsubscribe}
取消订阅流操作

**Kind**: inner method of [<code>rtcManage</code>](#module_rtcmanage)  

| Param | Type | Description |
| --- | --- | --- |
| id | <code>number</code> | 取消订阅的流id |

**Example**  
```js
{% lanying_code_snippet repo="lanying-im-web",class="rtcManage",function="unSubscribe" %}{% endlanying_code_snippet %}
```