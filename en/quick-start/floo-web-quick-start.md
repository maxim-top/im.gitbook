---
description: Web SDK Quick Start guide for initialization, user registration, login, message formats, user friend operations, and basic to advanced messaging capabilities including RTC messages.
keywords: Web SDK, Quick Start, RTC SDK, AI智能体
---
# Web SDK Quick Start

This page is for quick integration, visit [detailed documentation](../reference/floo-web.md)

## Selection guide

Lanying IM front end provides 3 versions of Web SDK, please choose on needs:

1. [Web version](https://github.com/maxim-top/lanying-im-web), which is mainly used by PC desktop browsers and suitable for various traditional front-end applications;
2. [Uni-app version](https://github.com/maxim-top/lanying-im-uniapp), developed based-on DCloud.io uni-app framework, for H5 and various Applets (WeChat/Alypay/Baidu/Toutiao/QQ/DingTalk/Taobao), and also suitable for iOS, Android, QuickApp and other platforms;
3. [WeChat Applet version](https://github.com/maxim-top/lanying-im-miniprogram), a native version for WeChat Applet standard, with the same features as the uni-app version;

The following documenting takes the Web version as an example, and all versions are basically the same. Our DemoApp source code has been opened already, so it is recommended to check for development.

## Previous preparation

1. Login our official website console, get your appid and replace the following YOU\_APP\_IDs with it.
2. Download SDK [floo-3.0.0.js](https://package.lanyingim.com/floo-3.0.0.js)
3. For RTC develop, a dependency library, such as webrtc-adapter, must be introduced in the local development environment. Refer to the dependencies file package.json of the Lanying IM Web version. Then use yarn or npm to install the dependency package.

## Quick integration

### I. Initialization

Set AppID first

```
const config = {
  // dnsServer: "https://dns.lanyingim.com/v2/app_dns",
  appid: "YOUR_APP_ID",
  ws: false, // The uniapp version needs to be set to true, the web version needs to be set to false
  autoLogin: true
  };
```

Then create an im object for global invocation.

Two modes are currently supported:

1. Script: You can import it directly and use window.flooIM()

```
import "floo-3.0.0.js";

const im = new window.flooIM(config);
```

This approach mainly supports script tag references in browsers, but there are initialization concurrency issues, so try-catch-retry is used, see [lanying-im-web source](https://github.com/maxim-top/lanying-im-web/blob/master/src/ui/index.vue#L85)。

2. module mode，import flooim first，then use flooim()

```
import flooim from 'floo-3.0.0';

const im = flooim(config);
```

### II. Register user

Register user via the asyncRegister of IM’s userManager

```
im.userManage.asyncRegister(this.user).then(() => {
  console.log("Registered");
}).catch(ex => {
  console.log(ex.message);
});
```

### III. Login connected server

If the SDK sets autoLogin to true, you will not need to login if you open or refresh the page again after the first login. For the first login, call im.login

```
im.login({
  user,
  password,
});
```

You can listen for login information or progress:

```
im.on({
  'loginMessage': message => {console.log(message)}
});
```

### IV. Get conversation list

Direcly call userManage’s getConversationList, returning lists of names, ids, types, and unreads

```
const list = im.userManage.getConversationList();
console.log(list);
```

### V. Disconnect

im login information is stored in localstorage, you can delete it and refresh to implement by yourself

```
window.localStorage.clear();
window.location.reload();
```

## User friend

### Add friend

How to call im.rosterManage’s asyncApply method:

```
im.rosterManage.asyncApply({ user_id, alias })
  .then(() => {
    console.log("Request sent successfully!");
});
```

### Delete friend

Call rosterManage’s asyncDeleteRoster method to delete friend

```
im.rosterManage.asyncDeleteRoster({ user_id })
  .then(() => {
    console.log("Friend deleted");
});
```

### Agree to add friend

Call rosterManage’s asyncAccept method to approve friend request

```
im.rosterManage.asyncAccept({ user_id }).then(() => {
  console.log("Friend request has been approved");
});
```

### Reject to add friend

Call rosterManage’s asyncDecline method to reject friend request

```
im.rosterManage.asyncDecline({ user_id }).then(() => {
  console.log("Friend request has been rejected");
});
```

### Get friend list

Call rosterManage’s getAllRosterDetail method to get friend list

```
const list = im.rosterManage.getAllRosterDetail();
```

Listen onRosterListUpdate to instantly view changes to user list

```
im.on({
  onRosterListUpdate: function() {
    const list = im.rosterManage.getAllRosterDetail();
  }
})
```

## Basic features

### Single chat

Single chat is the most basic chat interface, which provides a variety of input contents, ex. text, emoji, image and so on.

### Single RTC chat

Single RTC chat is the most basic chat interface, which provides a variety of 1v1 audio chat and 1v1 video chat.

### Group chat

Group chat, where many members participate together.

1. Create group

Call groupManage’s asyncCreate method to create a group

```
im.groupManage
  .asyncCreate({
    name,
    type, // Yes/No pulbic， 0， 1
    avatar,
    description,
    user_list, // user ids
  })
  .then(() => {
    console.log("Group created");
  });
```

2. Join group

Call groupManage’s asyncApply method to apply to join a group

```
im.groupManage
  .asyncApply({ group_id, reason })
  .then(() => {
    console.log("Request sent successfully!");
  });
```

3. Quit group

Call groupManage’s asyncLeave method to quit a group

```
im.groupManage
  . asyncLeave({ group_id })
  .then(() => {
    console.log("Quitted group");
  });
```

4. Dissolve group

Call groupManage’s asyncDestroy method to dissolve a group

```
im.groupManage
  .asyncDestroy({ group_id })
  .then(() => {
    console.log("Group dissolved");
  });
```

5. Get group member list

Call groupManage’s getGroupMembers method to get a list of all members

```
const members = im.groupManage.getGroupMembers(state.sid);
console.log(members);
```

6. Get group list Call groupManage’s asyncGetJoinedGroups method to get groups that all users joined

```
im.groupManage.asyncGetJoinedGroups().then(res => {
  console.log(res);
});
```

7. Get group information Call groupManage’s asyncGetGroupInfo method to get group details

```
groupManage.asyncGetGroupInfo(group_id).then(res => {
  console.log(res);
});
```

## Message sending

You can't chat until login successfully. When sending messages, single chat and group chat are divided seperately. For easier operation, it only supports sending text, images, files, location, 1v1 rtc video call and 1v1 rtc audio call at present. group chat only supports text, images, files, location at present.

### Build message body

### Text message

```
const message = {
  uid,  // User id, only used for single chat
  gid,  // id, only used for group chat
  content, // Message text
  priority， // Set the dissemination priority of messages in the range of 0-10. The message level sent by ordinary member in chatroom defaults to 5, which can be discarded, while Admin defaults to 0 and messages will not be discarded. Other values can be set according to the business.
}
```

### Image message

```
const fileInfo = {
  dName,  // file name
  fLen,   // file size
  width,  // image width
  height, // image height
  url,    // image url
};
const message = {
  type: 'image',
  uid,
  git, // uid, gid User or A group in which sent to, respectively
  content: "",
  attachment: fileInfo,
  priority, //Set priority of message dissemination
});
```

### File message

```
const fileInfo = {
  dName,  // file name
  fLen,   // file size
  width,  // image width
  height, // image height
  url,    // image url
};
const message = {
  type: 'file',
  uid,
  git, // uid, gid User or A group in which sent to, respectively
  content: "",
  attachment: fileInfo,
  priority, //Set priority of message dissemination
});
```

### Location message
```
const message = {
  type: 'location',
  uid,
  git, // uid, gid User or A group in which sent to, respectively
  content: '',
  attachment: {
    lat,    //latitude
    lon,    //longitude
    addr,   //address name
  }
});
```

### RTC message
```
const message = {
  type: 'rtc',
  uid,
  git,          // uid, gid User or A group in which sent to, respectively
  content: '',  // 消息文本内容
  config: {
    action,     //operation type （pickup、reject、hangup and so on）
    callId,     //call id
  }
});
```

### Message operation

After message body is built, call the -sendMessage: method through the singleton of BMXClient, ChatService class, and pass in the built message body to send the message

#### Send

```
im.sysManage.sendRosterMessage(message);
//or
im.sysManage.sendGroupMessage(message);
```

#### Forward

```
const fmessage = {
  mid, // Message id
  uid,
  gid, // uid or gid
}
im.sysManage.forwardMessage(message);
```

#### Revoke

```
const fmessage = {
  mid, // Message id
  uid,
  gid, // uid or gid
}
im.sysManage.recallMessage(message);
```

## Message delivery listening

### Message notification received

```
im.on({
  onRosterMessage: function(message) {
    console.log(message);
  }
});

im.on({
  onGroupMessage: function(message) {
    console.log(message);
  }
});
```

### Status callback notificated after message sending

```
im.on({  // Status changed
  onMessageStatusChanged: function(mStatus) {
    console.log(mStatus.mid, mStatus.status);
  }
});

im.on({ //Message revoked
  onMessageRecalled: function(mid) {
    console.log(mid);
  }
});

im.on({ //Message deleted
  onMessageDeleted: function(mid) {
    console.log(mid);
  }
});

im.on({ //Message revoked
  onMessageRecalled: function(mid) {
    console.log(mid);
  }
});

im.on({ //Message unread set
  onMessageCanceled: function(mid) {
    console.log(mid);
  }
});
```

## Advanced features

### Group @ function

```
im.sysManage.sendMentionMessage({
  gid,
  txt, // Text-message
  mentionAll, // Whether to @every member
  mentionList, // [id,id ...]
  mentionedMessage, // mention content
  pushMessage, // push
  senderNickname // sender nickname
});
```

### Typing message

```
im.sysManage.sendInputStatusMessage({
  uid,
  status, // nothing or typing
});
```

### Search for message

Search for specified message by keyword

```
const ret = im.sysManage.makeSearch(keyword);
let { groupArr = [], rosterArr = [] } = ret;
if(groupArr.lenght) {
  console.dir(groupArr[0]);
  // group_id/user_id, name/username, content, avatar
}
```

### Initiate single RTC call
```
Initiate single rtc call
im.rtcManage.initRTCEngine(message);
//or join single rtc call
im.rtcManage.joinRoom(message);
```

### Send RTC call message
```
im.rtcManage.sendRTCMessage(message);
```

### Receive RTC call message
```
im.on({
  onRosterRTCMessage: function(message) {
    console.log(message);
  }
});
im.on({
  onGroupRTCMessage: function(message) {
    console.log(message);
  }
});
```