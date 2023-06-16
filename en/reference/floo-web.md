#  Lanying IM SDK:floo-web API introduction

## Selection guide

Lanying IM front end provides 3 versions of Web SDK, please choose on needs:

1.  [Web version](https://github.com/maxim-top/lanying-im-web), which is mainly used by PC desktop browsers and suitable for various traditional front-end applications;
2.  [Uni-app version](https://github.com/maxim-top/lanying-im-uniapp), developed based-on DCloud.io uni-app framework, for H5 and various Applets (WeChat/Alypay/Baidu/Toutiao/QQ/DingTalk/Taobao), and also suitable for iOS, Android, QuickApp and other platforms;
3.  [WeChat Applet version](https://github.com/maxim-top/lanying-im-miniprogram), a native version for WeChat Applet standard, with the same features as the uni-app version;

The following documenting takes the Web version as an example, and all versions are basically the same. Our DemoApp source code has been opened already, so it is recommended to check for development.

## Previous preparation

Download the corresponding SDK file, address of desktop Web version is :[floo-2.0.0.js](https://package.lanyingim.com/floo-2.0.0.js), and refer to it in code.

## Initialization

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

1.  Script: You can import it directly and use window.flooIM()
```
    import "floo-2.0.0.js";
    
    const im = new window.flooIM(config);
```
This approach mainly supports script tag references in browsers, but there are initialization concurrency issues, so try-catch-retry is used, see[lanying-im-web source](https://github.com/maxim-top/lanying-im-web/blob/master/src/ui/index.vue#L85).

2.  module mode,import flooim first,then use flooim()
```
    import flooim from 'floo-2.0.0';
    
    const im = flooim(config);
```
## base

Login
```
        im.login({
          mobile:String, #or name
          name:String,
          password:String,
        })
```   

Listen  
See the Event Notification section of this document for event list
```
        im.on('events', (ret) => {
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
Unlisten
```
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
QR code login
```
      im.qrlogin({
        password,
        user_id
      });
      
```
token login
```
        im.tokenLogin(user_id, token)
      
```
## userManage

User registeration
```
        userManage.asyncRegister({
          username,
          password
        }).then(() => {
          //
        });
      
```
Get token of logged-in user
```
        const token =  im.userManage.getToken();
      
```
Get uid of logged-in user
```
        const cuid = im.userManage.getUid();
      
```
Get appid
```
        const appid = im.userManage.getAppid();
      
```
Get recent reply list
```
        const list = im.userManage.getConversationList();
      
```
Send verification code
```
        im.userManage
        .asyncUserSendSms({
          mobile,
        })
        .then(() => {
          //
        });
      
```
Send verification code (in image)
```
        im.userManage
        .asyncCaptchaSms({
          captcha,
          image_id,
          mobile,
        })
        .then(() => {
          //
        });
      
```
Check whether username is available
```
        im.userManage.asyncUserNameCheck(username).then(() => {
          //
        });
      
```
Bind mobile number - bind with signature
```
        im.userManage.asyncUserMobileBindSign({
            mobile,
            sign,
          }).then(() => {
            //
          });
      
```
Login with mobile number and verification vode
```
        im.userManage.asyncUserMobileLogin({
          captcha,
          mobile
        })
        .then(res => {
          //
        });
      
```
Update mobile number
```
        im.userManage
        .asyncUpdateMobile({ mobile })
        .then(() => {
          //
        });
      
```
Update avatar
```
        im.userManage
        .asyncUpdateAvatar({
          avatar
        })
        .then(() => {
          //
        });
      
```
Update nickname
```
        im.userManage.asyncUpdateNickName({ nick_name }).then(() => {
          //
        });
      
```
Get user profile
```
        im.userManage.asyncGetProfile(true).then(res => {
          //
        })
      
```
Update user profile
```
        im.userManage.asyncUpdateProfile({
          username,
          avatar
        }).then(res => {
          //
        })
      
```
Get user settings
```
        im.userManage.asyncGetSettings().then(res => {
          //
        })
      
```
Modify user settings
```
        im.userManage
        .asyncUpdateSettings({ 
          "auth_answer": "string",
          "auth_mode": 0,
          "auth_question": "string",
          "auto_download": true,
          "group_confirm": true,
          "id": 0,
          "no_push": true,
          "no_push_detail": true,
          "no_push_end_hour": 0,
          "no_push_start_hour": 0,
          "no_sounds": true,
          "push_nick_name": "string",
          "user_id",
          "vibratory": true
        }).then(() => {
          //
        });
      
```
## rosterManage

Get friend id list
```
        im.rosterManage.asyncGetRosterIdList().then(res => {
          //
        });
      
```
Get friend information
```
        im.rosterManage.asyncGetRosterInfo(state.sid).then(res => {
          //
        })
      
```
Get user details by id list
```
        im.rosterManage.asnycGetRosterListDetailByIds(rosterIdList).then(res => {
          //
        });
      
```
Get chat message by id
```
        const rosterMessages = im.rosterManage.getRosterMessageByRid(uid);
      
```
Read message
```
        im.rosterManage.readRosterMessage(uid);
      
```
Delete friend
```
        im.rosterManage
        .asyncDeleteRoster({ user_id})
        .then(() => {
          alert("Friend deleted");
        });
      
```
Get all cached new users
```
        const userMaps = im.rosterManage.getAllRosterDetail();
      
```
Revoke a message, only valid for last 5 minutes
```
        im.rosterManage.recallMessage(user_id, message_id);
      
```
Delete message
```
        im.rosterManage.deleteMessage(user_id, message_id);
      
```
Get number of user's unreads
```
        const unreadCount = im.rosterManage.getUnreadCount(user_id) :
      
```
Set message to unread
```
        im.rosterManage.unreadMessage(user_id, message_id);
      
```
Get friend information
```
        const roserInfo = im.rosterManage.getRosterInfo(user_id);
      
```
Get friend request list
```
        im.rosterManage
        .asyncGetApplyList({ cursor: "" })
        .then((res = []) => {
          //
        });
      
```
Get blacklist
```
        im.rosterManage
        .asyncGetBlockedlist()
        .then((res = []) => {
          //
        });
      
```
Add to blacklist
```
        im.rosterManage
        .asyncBlockeAdd(user_id)
        .then((res = []) => {
          //
        });
      
```
Remove blacklist
```
        im.rosterManage
        .asyncBlockeRemove(user_id)
        .then((res = []) => {
          //
        });
      
```
Request to add friend
```
        im.rosterManage
        .asyncApply({ user_id, alias })
        .then((res = []) => {
          //
        });
      
```
Approve add-friend request
```
        im.rosterManage
        .asyncAccept({ user_id })
        .then((res = []) => {
          //
        });
      
```
Reject friend request
```
        im.rosterManage
        .asyncDecline({ user_id })
        .then((res = []) => {
          //
        });
      
```
Search for user by name
```
        im.rosterManage
        .asyncSearchRosterByName({ username })
        .then((res = []) => {
          //
        });
      
```
Search for user by ID
```
        im.rosterManage
        .asyncSearchRosterById({ user_id })
        .then((res = []) => {
          //
        });
      
```
## groupManage

Get group information
```
        im.groupManage.asyncGetGroupInfo(group_id, fromServer).then(res => {
          //
        })
      
```
Get the group to join
```
        im.groupManage.asyncGetJoinedGroups().then(res => {
          //
        });
      
```
Open group
```
        // This approach prepares some of necessary information for group chat interface.
        im.groupManage.openGroup(group_id);
      
```
Get all cached group details
```
        const allGroupMap = im.groupManage.getAllGroupDetail();
      
```
Get group members (asynchronous)
```
        im.groupManage.asyncGetGroupMembers(group_id, fromServer).then(res => {
          //
        });
      
```
Get group members (synchronous)
```
        const members = im.groupManage.getGroupMembers(group_id);
      
```
Get group details by id
```
        im.groupManage.asyncGetGroupListDetail(groupIds).then(res => {
          //
        });
      
```
Get group information
```
        const groupMessages = rootState.im.groupManage.getGruopMessage(group_id);
      
```
Set group message to read
```
        im.groupManage.readGroupMessage(group_id)
      
```
Revoke message
```
        im.groupManage.recallMessage(group_id, message_id)
      
```
Get number of unread group messages
```
        const unreadCount = im.groupManage.getUnreadCount(group_id);
      
```
Get the list of group Admins
```
        im.groupManage.asyncGetAdminList({ group_id }).then(res => {
          //
        })
      
```
Add group Admin
```
        im.groupManage.asyncAdminAdd({
          group_id,
          user_list
        })
        .then(() => {
          //
        });
      
```
Remove group Admin
```
        im.groupManage.asyncAdminRemove({ group_id, user_list }).then(() => {
          //
        });
      
```
Get group announcement details
```
        im.groupManage.asyncGetAnouncementById( {announcement_id, group_id} ).then(res => {
          //
        });
      
```
Delete group announcement
```
        im.groupManage
        .asyncAnouncementDelete({ group_id, announcement_id })
        .then(() => {
          //
        });
      
```
Add group announcement
```
        im.groupManage.asyncAnnouncementEdit({ title, content, group_id })
        .then(() => {
          //
        });
      
```
Group announcement list
```
        im.groupManage.asyncGetAnnouncementList({ group_id }).then((res = []) => {
          //
        });
      
```
Create group
```
        im.groupManage.asyncCreate({
          name,
          type,
          avatar,
          description,
          user_list,
        })
        .then(() => {
          //
        });
      
```
Dissolve group
```
        im.groupManage.asyncDestroy({ group_id })
        .then(() => {
          alert("You have dissolved this group.");
        });
      
```
Get group details
```
        im.groupManage.asyncGetInfo({ group_id }).then(res => {
          //
        });
      
```
Update group avatar
```
        im.groupManage.asyncUpdateAvatar({
          group_id,
          value,
        })
        .then(() => {
          alert("Avatar updated");
        });
      
```
Update group description
```
        im.groupManage.asyncUpdateDescription({
          group_id,
          value
        })
        .then(() => {
          //
        });
      
```
Update group name
```
        im.groupManage.asyncUpdateName({
          group_id,
          value
        })
        .then(() => {
          //
        });
      
```
Get group member
```
        im.groupManage.asyncGetMemberList(group_id, fromServer).then(res => {
          //
        });
      
```
Set do-not-disturb conditions for group message
```
        im.groupManage.asyncGroupMsgMutemode({
          group_id,
          msg_mute_mode
        })
        .then(() => {
          this.groupInfo.msg_mute_mode = this.groupInfo.msg_mute_mode ? 0 : 2;
        });
      
```
Get group blacklist
```
        im.groupManage.asyncGroupBannedList({ group_id }).then(res => {
          //
        });
      
```
Ban group member
```
        im.groupManage.asyncGroupBab({ group_id, duration, user_list }).then(() => {
          //
        });
      
```
Unban group member
```
        im.groupManage.asyncGroupUnban({ group_id, user_list }).then(() => {
          //
        });
      
```
Set whether group members can invite new member
```
        im.groupManage.asyncUpdateAllowMemberInvitation({
          group_id,
          value
        })
        .then(() => {
          //
        });
      
```
Set whether group members can modify group information
```
        im.groupManage.asyncUpdateAllowMemberModify({
          group_id,
          value
        })
        .then(() => {
          //
        });
      
```
Set whether to enable read mode in group
```
        im.groupManage.asyncUpdateEnableReadack({
          group_id,
          value
        })
        .then(() => {
          //
        });
      
```
Set whether group history is visible
```
        im.groupManage.asyncUpdateHistoryVisible({
          group_id,
          value
        })
        .then(() => {
          //
        });
      
```
Set whether need to apply for group joining
```
        im.groupManage.asyncUpdateRequireadminapproval({
          group_id,
          apply_approval
        })
        .then(() => {
          //
        });
      
```
Change group Owner
```
        im.groupManage.asyncOwnerTransfer({
          group_id,
          new_owner
        })
        .then(() => {
          //
        });
      
```
Apply to join group
```
        im.groupManage.asyncApply({ group_id, reason })
        .then(() => {
          //
        });
      
```
Accept/reject group membership application
```
        im.groupManage.asyncApplyHandle({
          approval: true/false,
          user_id,
          group_id
        }).then(() => {
          //
        });
      
```
Get group blacklist
```
        im.groupManage.asyncGroupBockedlist({ group_id }).then(res => {
          //
        });
      
```
Add member to blacklist
```
        im.groupManage.asyncGroupBlock({ group_id, user_list }).then(() => {
          //
        });
      
```
Remove member from blacklist
```
        im.groupManage.asyncGroupUnblock({ group_id, user_list })
        .then(() => {
          //
        });
      
```
Kick out group member
```
        im.groupManage.asyncKick({ group_id, user_list }).then(() => {
          //
        });
      
```
Get group invitation list
```
        this.im.groupManage.asyncGetInvitationList().then(res => {
          //
        });
      
```
Invite member to group
```
        im.groupManage.asyncInvite({ group_id, user_list }).then(() => {
          /
        });
      
```
Accept/reject group invitation
```
        im.groupManage.asyncInviteHandle({
          approval: true,
          user_id,
          group_id
        }).then(() => {
          //
        });
      
```
Quit group
```
        im.groupManage.asyncLeave({ group_id })
        .then(() => {
          //
        });
      
```
Modify group profile
```
        im.groupManage.asyncUpdateDisplayName({
          group_id,
          value
        })
        .then(() => {
          //
        });
      
```
Get the list of group membership requests
```
        im.groupManage.asncGetApplicationList({ group_list }).then(rs => {
          //
        });
      
```
Get group file
```
        im.groupManage.asyncGetFileList({ group_id }).then((res = []) => {
          //
        });
      
```
Delete group file
```
        im.groupManage.asyncFileDelete({ file_list, group_id }).then(() => {
          //
        });
      
```
## sysManage

Send message to friend
```
        im.sysManage.sendRosterMessage({
          type,
          uid,
          content,
          attachment
        });
      
```
Send group message
```
        im.sysManage.sendGroupMessage({
          type,
          gid,
          content,
          attachment
        });
      
```
Group-sent @message
```
        im.sysManage.sendMentionMessage({
          gid,
          txt,
          mentionAll,
          mentionList,
          mentionedMessage,
          pushMessage,
          senderNickname
        });
      
```
Send type status
```
        im.sysManage.sendInputStatusMessage(roster_id, "nothing"/"typing");
      
```
Forward message
```
        im.sysManage.forwardMessage({
          uid,
          gid, //either-or
          mid,
        });
      
```
Request history
```
        im.sysManage.requireHistoryMessage(roster_id/group_id, mid, amount);
        // mid:message ID, from which message to fetch history, 0 for the latest message. amount:max. number of messages to fetch.
      
```
Get all unread messages
```
        const allAcks = im.sysManage.getAllMessageStatus() || {};
      
```
Get upload url of group file
```
        im.sysManage.asyncGetGroupAvatarUploadUrl({
          group_id,
          "access-token"
        })
        .then(res => {
          //
        });
      
```
Get upload address of chat file
```
        im.sysManage.asyncGetFileUploadChatFileUrl({
          file_type,
          to_id,
          to_type
        })
        .then(res => {
          //
        });
      
```
Upload file
```
        im.sysManage.asyncFileUpload({
          file,
          fileType,
          to_id,
          toType: "chat",
          chatType: "roster"
        })
        .then(res => {
          //
        })
      
```
Assemble image path
```
        const image = im.sysManage.getImage({ avatar, type='roster', thumbnail=true });
      
```

## rtcManager
Initiate a rtc call
```
        im.rtcManage.initRTCEngine({
          server,
          id,
          name,
          receiver,
          caller,
          callId,
          secret,
          pin,
          hasVideo,
          hasAudio,
          remoteAudio,
          getThrough,
          hangupCall
        });
```
Destroy rtc environment
```
        im.rtcManage.destroy();
```
Send RTC message
```
        im.rtcManage.sendRTCMessage({
          uid,
          content,
          config,
          ext
        });
```
Join RTC room
```
        im.rtcManage.joinRoom({
          server,
          id,
          roomId,
          caller,
          pin,
          hasVideo,
          hasAudio,
          remoteAudio,
          getThrough,
          hangupCall
        });
```
Leave RTC room
```
        im.rtcManage.leaveRoom();
```
Publish video audio streams
```
        im.rtcManage.publish({
          type,
          hasVideo,
          hasAudio,
          width,
          height
        });
```
Unpublish video audio streams
```
        im.rtcManage.unPublish();
```
Subscribe video audio streams
```
        im.rtcManage.subscribe(sources);
```
Unsubscribe video audio streams
```
        im.rtcManage.unSubscribe(id);
```
Switch local audio mute status
```
        im.rtcManage.muteLocalAudio(mute);
```
Switch local video mute status
```
        im.rtcManage.muteLocalVideo(mute);
```
Switch remote audio mute status
```
        im.rtcManage.muteRemoteAudio(stream, mute)
```
Switch remote video mute status
```
        im.rtcManage.muteRemoteVideo(stream, mute)
```
Get Janus Object
```
        im.rtcManage.getJanusObject()
```
Get publisher object
```
        im.rtcManage.getPublishHandler()
```
Get subscriber object
```
        im.rtcManage.getSubscribeHandler()
```

## Event notification

1.  Floo notification
```
Event name:flooNotice
Event content:({category, desc})
{category: 'loginMessage',desc: 'socket connecting...'} // Start connecting
{category: 'loginMessage',desc: 'socket connect success...'} // Connected
{category: 'loginMessage',desc: 'logining socket service...'} // Start logging in
{category: 'loginMessage',desc: 'login socket failure ......'} // Login failed
{category: 'loginMessage',desc: 'login socket success.....'} // Login succeeded
{category: 'loginMessage', desc: 'getting token...' } //Get token
{category: 'loginMessage',desc: 'token sucecc, getting roster lists..'} // Getting token succeeded, start to fetch friend list
{category: 'loginMessage',desc: 'get roster list failure:' + ex.message} // Friend list fetching failed
{category: 'action', desc: 'relogin' } // Need to automatically login
{category: 'action', desc: 'relogin_manually' }  // Need to manually login
{category: 'conversation_deleted',desc: { id, source:'user_operation' }} // Conversation deleted. ID:conversation ID, source: source
{category: 'userNotice', desc:'PASSWORD_CHANGED'} // User password changed
{category: 'userNotice', desc:'FROZEN'} // User account frozen
{category: 'userNotice', desc:'REMOVED'} // User removed
{category: 'userNotice', desc:'KICK_BY_SAME_DEVICE'} // Current device is kicked off the line by the same device
{category: 'userNotice', desc:'KICKED_BY_OTHER_DEVICE'} // Current device is kicked off the line by other device
{category: 'userNotice', desc:'INFO_UPDATED'} // User information changed:profile or setting
{category: 'userNotice', desc:'DEVICE_LOGIN'} // User's other device logged-in
{category: 'userNotice', desc:'DEVICE_LOGOUT'} // User's other device logged-out
{category: 'userNotice', desc:'DEVICE_ADDED'} // New device notified
{category: 'userNotice', desc:'DEVICE_REMOVED'} // Device removal notified
{category: 'userNotice', desc:'CLUSTER_CHANGED'} // User's group changed, please re-login
```
2. Floo error
```
Event name:flooError
Event content:({category, desc})
{category: 'USER_BANNED', desc:'User is banned'}
{category: 'USER_FROZEN', desc:'User is frozen, please contact App Admin.'}
{category: 'APP_FROZEN', desc:'APP is frozen, please login Lanying IM Console for more details.'}
{category: 'LICENSE', desc:'Invalid LICENSE, please make sure service is paid on time.'}
{category: 'LICENSE', desc:'LICENSE user limit reached, please purchase higher service package.'}
{category: 'DNS_FAILED', desc: dnsServer } // DNS error: unaccessible
```
3. Login failed
```
Event name: loginFail
Event content: (desc) description of failure cause
```
4. Login succeeded
```
Event name:loginSuccess
Event content:({})
```
5. Group list update
```
Event name:onGroupListUpdate
Event content:()
```
6. Group member list update
```
Event name:onGroupMemberChanged
Event content: (groupId) group ID
```
7. Group message received
```
Event name: onGroupMessage
Event content: (meta) Message content
```
8. The other party is typing
```
Event name: onInputStateMessage
Event content: ({ext,from,to})  ext:extension field from: sender's user ID to: receiver's user ID
```
9. Group @message received
```
Event name: onMentionMessage
Event content: (meta) Message content
```
10. Message re-unread
```
Event name: onMessageCanceled
Event content: ({uid,mid})  uid: conversation ID, mid: message ID
```
11. Message deleted
```
Event name: onMessageDeleted
Event content: ({uid,mid})  uid: conversation ID, mid: message ID
```
12. Message revoked
```
Event name: onMessageRecalled
Event content: ({uid,mid})  uid: conversation ID, mid: message ID
```
13. Message status change: revoked/deleted/read
```
Event name: onMessageStateChanged
Event content: ({uid,mid})  uid: conversation ID, mid: message ID
```
14. Message history received
```
Event name: onReceiveHistoryMsg
Event content: ({next})  next: Get message history key next time
```
15. Friend information changed
```
Event name: onRosterInfoUpdate
Event content: (rosterIds)  rosterIds: List of friends' user ids
```
16. Friend list changed
```
Event name: onRosterListUpdate
Event content: (meta) Message content of friend notification
```
17. Single chat received
```
Event name: onRosterMessage
Event content: (meta) Message content of friend notification
```
18. Message sending status changed
```
Event name: onSendingMessageStateChanged
Event content: ({state,mid})  state: sending status, valued as sending|failed|sent, mid: client_mid generated by client
```
19. Number of unreads changed
```
Event name: onUnreadChange
Event content: (cid)  conversation ID
```
20. Recent conversation updated
```
Event name: recentlistUpdate
Event content: ()
```
21. Group creation notification
```
Event name: onGroupCreated
Event content: (meta) Content of group notification
```
22. Group dissolution notification
```
Event name: onGroupDestoryed
Event content: (meta) Content of group notification
```
23. Notification of group membership
```
Event name: onGroupJoined
Event content: (meta) Content of group notification
```
24. Group application approved
```
Event name: onGroupApplyAccepted
Event content: (meta) Content of group notification
```
25. Group application rejected
```
Event name: onGroupApplyDeclined
Event content: (meta) Content of group notification
```
26. Banned in group
```
Event name: onGroupBaned
Event content: (meta) Content of group notification
```
27. Unbanned in group
```
Event name: onGroupUnbaned
Event content: (meta) Content of group notification
```
28. Single RTC chat received
```
Event name: onRosterRTCMessage
Event content: (meta) Message content of friend notification
```