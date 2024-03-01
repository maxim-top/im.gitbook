# IOS SDK Quick Start

This page is for quick integration, visit [detailed documentation](../reference/floo-ios.md)

## Previous preparation

Lanying IM SDK provides two ways to integrate our floo-ios, automatically through CocoaPods or manually add it to the project by downloading the floo-ios.framework model manually.

### Mode I: Auto integration/CocoaPods

Hint: If cocoapods is not installed, please refer to [CocoaPods installation](https://cocoapods.org)

1.  Add floo-ios to Prodfile:

    ```
    pod 'floo-ios'
    ```
2.  Install with the following command

    ```
    pod install
    ```

    Hint: If you cannot install the latet version of SDK, run the following command to update your local CocoaPods repo list

    ```
    pod repo update
    ```

### Mode II: Manual integration

1. [Download floo-ios.framework](https://package.lanyingim.com/floo-ios.zip) , and then reference the file to your project.
2.  Add system library dependencies

    Before importing SDK to your project, please add the following system library references.

    * libc++abi.tbd
    * libstdc++.tbd
    * libz.tbd
    * libc++.tbd
    * libresolv.tbd
    * libcrypto.a
    * UIKit.framework
    * QuartzCore.framework
    * ImageIO.framework
    * CoreVideo.framework
    * CoreMedia.framework
    * CoreGraphics.framework
    * AVFoundation.framework
    * AssetsLibrary.framework

    Note：

    If libcrypto.a is already referenced within your project, no need to import it again to avoid introducing conflicts.

    If libcrypto.a is not referenced in your project yet, please unzip the downloaded SDK package to import libcrypto.a into your project.
3. In Xcode project’s Build Settings - Other Linker Flags, add “-ObjC”.
4. Set App to support HTTPS
5. Make push certificate

## Quick integration

### I. Initialization

Import the related header file in the class where you need to use Lanying IM SDK functionality.

```
#import "BMXClient.h"
```

You must call this method to initialize Lanying IM SDK before you can use all of its features. You only need to initialize the SDK once in the whole life cycle of the App.

```
// Set storage path

NSString* dataDir = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES).firstObject stringByAppendingPathComponent:@“ChatData”];

NSString* cacheDir = [NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES).firstObject stringByAppendingString:@“UserCache”];

// Initialization

BMXSDKConfig *config = [[BMXSDKConfig alloc] initConfigWithDataDir:dataDir cacheDir:cacheDir pushCertName:@“Your APNS Certification” userAgent:@“userAgent”];

config.appID = @“Your AppID”;

[[BMXClient sharedClient] registerWithSDKConfig:config];
```

### II. Register user

Pass in signUpMobile:password:vertifyCode:userName: method through the singleton of BMXClient, UserService class, to register IM account.

```
[[[BMXClient sharedClient] userService] signUpMobile:mobile password:password vertifyCode:vertifyCode userName:username completion:^(BMXUserProfile *profile, BMXError *aError) {

        [HQCustomToast hideWating];
        if(!aError) {
             NSLog(@"Registered");
        }  else {
             NSLog(@"Failed errorCode = %ld ", error.errorCode);
        }
     }];
```

### III. Login connected server

Pass the account password you obtained in the previous step into the -signInById method through the UserService class, a singleton of BMXClient, to establish a connection with the server.

Two login modes provided: One for normal manual login, and the other for quick login

```
[[BMXClient sharedClient] signInById:userid password:password completion:^(BMXError *error) {
        if (!error) {
            NSLog(@"Login successful username = %lld , password = %@",userid, password);
          } else {
            NSLog(@"Failed errorCode = %lu ", error.errorCode);
        }
     }];

// Quick login without getting token
[[BMXClient sharedClient] fastSignInById: userid password:password  completion:^(BMXError *error) {
 if (!error) {
     NSLog(@"Login successful username = %@ , password = %@", userid, password);
 } else {
     NSLog(@"Failed errorCode = %ld ", error.errorCode);
 }
}];
```

### IV. Conversation list function

Pass in getAllConversationsWithCompletion method through the singleton of BMXClient, ChatService class, to get a list of all conversations. Then return an array list of BMXConversation objects.

If you need to get a list of offline conversations for multi-device synchronization, you need to configure the loadAllServerConversations property value to Yes at SDK initialization, and only get the local conversation list by default.

```
 [[[BMXClient sharedClient] chatService] getAllConversationsWithCompletion:^(NSArray *conversations) {
    NSLog(@"%ld", conversations.count);
  }];
```

### V. Disconnect

devicetoken.When disconnected from Lanying IM server, remote push is stopped by default and device devicetoken is automatically unbound.

```
 [[[BMXClient sharedClient] userService] signOutWithcompletion:^(BMXError *error) {
    if (!error) {
    NSLog(@"Quit successfully");
    }
 }];
```

## User friend

*   Add friend

    ```
       [[[BMXClient sharedClient] rosterService] applyAddRoster:rosterId reason:reason completion:^(BMXRoster *roster, BMXError *error) {
        if (!error) {
        MAXLog(@"Application successful");
      } else {
        MAXLog(@"Application failed");
      }

      }];
    ```
*   Delete friend

    ```
      [[[BMXClient sharedClient] rosterService] removeRosterById:@"880" withCompletion:^(BMXError *error) {

      }];
    ```
*   Agree to add friend

    ```
      [[[BMXClient sharedClient] rosterService] acceptRosterById:@"880" withCompletion:^(BMXError *error) {
      	 if (!error) {
          MAXLog(@"Added successfully");
       }
          MAXLog(@"%@", error);

      }];
    ```
*   Reject to add friend

    ```
      [[[BMXClient sharedClient] rosterService] declineRosterById:@"880" withReason:reason completion:^(BMXError *error) {

      }];
    ```
*   Get friend list

    Developers can choose to get friend list data from server or locally via parameter forceRefresh.

    If set to NO, when the local data is empty, it will automatically get the data from server and return the result.

    ```
      [[[BMXClient sharedClient] rosterService] getRosterListforceRefresh:YES completion:^(NSArray *rostIdList, BMXError *error) {
      if (!error) {
          MAXLog(@"%ld", rostIdList.count);
          [self searchRostersByidArray:[NSArray arrayWithArray:rostIdList]];
      }
      }];
    ```

## Basic features

### Single chat

Single chat is the most basic chat interface, which provides a variety of input contents such as text, emoji, voice clip, image, etc., and solves the communication bottleneck of users in App. BMXConversationType of single chat is BMXConversationSingle, and toId is userId of single chat object. See demo code in [Message operation](#Message operation)

### Group chat

Group’s BMXConversationType is BMXConversationGroup，toId is group Id。

* Create group

Developers can register to listener, then receive corresponding callback notifications after group created, thus do some UI processing.

```
    // Build information body of created group
    BMXCreatGroupOption *option = [[BMXCreatGroupOption alloc] initWithGroupName:title groupDescription:description isPublic:YES];
    option.message = message;  // Invitation information received by members when group created
    option.members = ids;   // Member list added when group created
    [[[BMXClient sharedClient] groupService] creatGroupWithCreateGroupOption:option completion:^(BMXGroup *group, BMXError *error) {
        if (!error) {
        }
    }];
```

*   Join group

    ```
      /**
      Join a group, which may require admin approval depending on group settings

      @param group BMXGroup
      @param message Application information
      @param aCompletionBlock Error
      */
      - (void)joinGroup:(BMXGroup *)group
        message:(NSString *)message
       completion:(void(^)(BMXError *error))aCompletionBlock;
    ```
*   Quit group

    ```
       [[[BMXClient sharedClient] groupService] leaveGroup:self.group completion:^(BMXError *error) {
          if (!error) {
          }
      }];
    ```
*   Dissolve group

    ```
       [[[BMXClient sharedClient] groupService] destroyGroup:group completion:^(BMXError *error) {
          if (!error) {
            NSLog(@"Destroy group");
        }
      }];
    ```
*   Get group member list

    ```
       [[[BMXClient sharedClient] groupService] getMembers:self.group forceRefresh:YES completion:^(NSArray<BMXGroupMember * *groupList, BMXError *error) {
          NSLog(@"%ld", groupList.count);
       }];
    ```
*   Get group list

    ```
      	/**
       Get group list

       @param forceRefresh Pull from server if forceRefresh is set
       @param aCompletionBlock GroupList, Error
       */
      [[[BMXClient sharedClient] groupService] getGroupListForceRefresh:NO completion:^(NSArray *groupList, BMXError *error) {
      		if (!error) {
        NSLog(@"%ld", groupList.count);
      }
      }];
    ```
*   Get group information

    ```
      [[[BMXClient sharedClient] groupService] getGroupInfoByGroupId:self.group.groupId forceRefresh:YES completion:^(BMXGroup *group, BMXError *error) {
       self.group = group;
      }];
    ```

## Message sending

You can't chat until you login successfully. When sending messages, single chat and group chat call the same unified interface, but the only difference is to set BMXConversationType.

Remote push of messages:

Developer shall configure the certificate for remote push, apply for permission in code, and send the deviceToken to Lanying IM server. When receiver is not online, Lanying IM server will automatically send the message through remote push.

Note: The pushed content is determined by the pushContent field of the sending message interface. If this field is empty-valued when the built-in message is sent, the default content will be pushed; user-defined messages must set this field, otherwise they will not be pushed.

Pass deviceToken to Lanying IM interface as follows:

```
[[[BMXClient sharedClient] userService] bindDevice:deviceToken completion:^(BMXError *error) {
      NSLog(@"Binding succeeded");
 }];
```

### Build message body

### Text message

```
 /**
 Create text message

 @param content Content
 @param fromId Send id
 @param toId Receive id
 @param mtype Message id
 @param conversationId Conversation id
 @return BMXMessageObject
 */
 BMXMessageObject *messageObject = [[BMXMessageObject alloc] initWithBMXMessageText:message
                                                              fromId:[self.account.usedId longLongValue]
                                                                toId:toId
                                                                type:self.messageType
                                                      conversationId:conversationId];
```

### Image message

```
	/**
  Create image-message object

  @param aData Binary data
  @param aThumbnailData Thumbnail
  @param imageSize Image size
  @param conversationId Conversation IDID
  @return BMXImageAttachment
  */
 BMXImageAttachment *imageAttachment = [[BMXImageAttachment alloc] initWithData:imageData thumbnailData:thumImageData imageSize:image.size conversationId:[NSString stringWithFormat:@"%lld",self.conversationId]];
```

### File message

```
 BMXFileAttachment *fileAttachment = [[BMXFileAttachment alloc] initWithData:dic[@"data"] displayName:dic[@"displayName"] fileLength:integer conversationId:[NSString stringWithFormat:@"%lld",self.conversationId]];
 BMXMessageObject *messageObject = [[BMXMessageObject alloc] initWithBMXMessageAttachment: fileAttachment
                                                                    fromId:[self.account.usedId longLongValue]
                                                                      toId:toId type:self.messageType
                                                            conversationId:conversationId];
```

### Location message

```
 BMXLocationAttachment *locationment = [[BMXLocationAttachment alloc] initWithLatitude:latitude longitude:longitude address:address]
 BMXMessageObject *messageObject = [[BMXMessageObject alloc] initWithBMXMessageAttachment: locationAttachment
                                                                    fromId:[self.account.usedId longLongValue]
                                                                      toId:toId type:self.messageType
                                                            conversationId:conversationId];
```

### Voice message

```
 BMXVoiceAttachment *vocieAttachment = [[BMXVoiceAttachment alloc] initWithPath:voicePath displayName:@"voice" duration:duartion];
 BMXMessageObject *messageObject = [[BMXMessageObject alloc] initWithBMXMessageAttachment: vocieAttachment
                                                                    fromId:[self.account.usedId longLongValue]
                                                                      toId:toId type:self.messageType
                                                            conversationId:conversationId];
```

### Message operation

After message body is built, call the -sendMessage: method through the singleton of BMXClient, ChatService class, and pass in the built message body to send the message

*   Send

    ```
     /**
      Send a message, and the message status change is notified via listener
     **/
     [[[BMXClient sharedClient] chatService] sendMessage:messageObject completion:^(BMXMessageObject *message, BMXError *error) {
       MAXLog(@"Send message%@", error);
     }];
    ```
*   Forward

    ```
     /**
     Simple forwarding message, users should create forwarding message first through BMXMessagseObject, initWithForwardMessage
     **/
     BMXMessageObject *m = [[BMXMessageObject alloc] initWithForwardMessage:self.currentMessage fromId:[self.account.usedId longLongValue] toId:roster.rosterId type:BMXMessageTypeSingle conversationId:roster.rosterId];
     [[[BMXClient sharedClient] chatService] forwardMessage:m];
    ```
*   Resend

    ```
      /**
     Resend this message, and the message status change is notified via listener
     **/
     [[[BMXClient sharedClient] chatService] resendMessage: self.messageModel.messageObjc completion:^(BMXMessageObject *message, BMXError *error) {
     }];
    ```
*   Revoke

    ```
     /**
     Recall a message, and the message status change is notified via listener
     **/
     [[[BMXClient sharedClient] chatService] recallMessage:message completion:nil];
    ```
*   Download message attachment

    ```
       /**
      * Download attachment, and download status changes and progress are notified through listener
      **/
       [[[BMXClient sharedClient] chatService] downloadAttachment:message downloadProgress:nil completion:nil];
    ```

## Message delivery listening

Register message callback

```
	/**
    * Add chat listener
    **/
	- (void)addChatListener:(id<BMXChatServiceProtocol>)listener;

	/**
	 * Remove chat listener
	**/
	- (void)removeChatListener:(id<BMXChatServiceProtocol>)listener;
```

*   Message notification received

    ```
      /**
      * Messages received
      **/
      - (void)receivedMessages:(NSArray<BMXMessageObject*> *)messages {

      	  if (message.contentType == BMXContentTypeText) {
          			// Text-message received, wait for processing by UI

            } else if (message.contentType == BMXContentTypeImage) {
                	// Image-message received

            } else if (message.contentType == BMXContentTypeVoice) {
      				// Voice-message received

            } else if (message.contentType == BMXContentTypeLocation) {
             		// Location-message received

            } else if (message.contentType == BMXContentTypeFile) {
                	// File-message received

            }
      }
    ```
*   Status callback notificated after message sending

    ```
      // Message status changed
      - (void)messageStatusChanged:(BMXMessageObject *)message
                     error:(BMXError *)error {

         if (message && !error) {
          switch ( message.deliverystatus) {
              case BMXDeliveryStatusNew:
                  messageModel.status = MessageDeliveryState_Pending;
                  break;
              case BMXDeliveryStatusDelivering:
                  messageModel.status = MessageDeliveryState_Delivering;
                  break;
              case BMXDeliveryStatusDeliveried:
                  messageModel.status = MessageDeliveryState_Delivered;
                  break;
              case BMXDeliveryStatusFailed:
                  messageModel.status = MessageDeliveryState_Failure;
                  break;
              case BMXDeliveryStatusRecalled:
                  messageModel.status = MessageDeliveryState_Pending;
                  break;

              default:
                  break;
          }
          [messagecell layoutSubviews];

      	}

      }
    ```
*   Status callback of attachment sending

    ```
      - (void)messageAttachmentUploadProgressChanged:(BMXMessageObject *)message percent:(int)percent {
      // percent of uploading progress

      }
    ```
*   Message reminder settings You can set message push reminder as follows via the singleton of BMXClient, UserService class.

    ```
      /**
      Set whether push is allowed

      @param enablePushStatus BOOL
      */
      - (void)setEnablePushStatus:(BOOL)enablePushStatus
               completion:(void(^)(BMXError *error))aCompletionBlock;

      /**
        Set whether to push details

        @param enablePushDetail BOOL
       */
    ```

p - (void)setEnablePushDetail:(BOOL)enablePushDetail completion:(void(^)(BMXError \*error))aCompletionBlock;

*   Status changes of attachment donwloading

    ```
      /**
      * Attachment download status changed
      **/
      - (void)messageAttachmentStatusDidChanged:(BMXMessageObject *)message
                        error:(BMXError*)error
                      percent:(int)percent;
    ```

## Advanced features

#### Custom messages

BMXMessageObject entity provides extensible attributes (extensionJson and configJson), extensionJson is an extension field for development use, such as edit status; configJson is an extension field for SDK's own use, such as mention and push functions.

*   Group @ function

    Support @ function in group to meet the needs of your @ specified user or @ every member. Developers can realize the @ function of group Owner by setting setConfig in BMXMessageObject, and push notifications will be sent to all @ members.
*   Typing message

    ```
      // ExtensionJson can be used to extend the message being edited, (json format, which can extend a variety of user-defined functions)
      @property (nonatomic, copy) NSString *extensionJson;
    ```
*   Message read acknowledgement

    ```
      //Whether all messages read
      @property (nonatomic,assign) BOOL isRead;
      //Whether to send a read acknowledgement after message delivered
      @property (nonatomic,assign) BOOL isReadAcked;
      //Whether to send a delivery acknowledgement after message received
      @property (nonatomic, assign) BOOL isDeliveryAcked;
    ```
*   Multi-terminal read message count synchronization

    BMXConversation entity provides unread message count and total number of messages in conversation /\*\* Unread message count \*/ @property (nonatomic,assign, readonly) NSInteger unreadNumber;

    ```
      /**
       Number of all messages in conversation
      */
      @property (nonatomic,assign, readonly) NSInteger messageCount;
    ```
*   Search for message

    Search for specified message by keyword

    ```
      /**
       Search for messages

       @param keywords Keyword
       @param refTime Time
       @param size Page
       @param directionType Message order
       @param aCompletionBlock Search result
      */

      [[[BMXClient sharedClient] chatService] searchMessages:@"Haha" refTime:0 size:100 directionType:BMXMessageDirectionUp completion:^(NSArray *array, BMXError *error) {

      }];
    ```
## RTC AV Call
The RTC call function needs to integrate floo-ios and floo-rtc-ios on the client side.Floo-ios provides a signaling channel for AV calls, and floo-rtc-ios implements the business logic in RTC calls. Therefore, before implementing AV calls, it is necessary to integrate floo-ios, and implement the features of login and messaging.

Floo-rtc-android supports one-to-one AV calls. You can integrate floo-rtc-ios by CocoaPods automatically, or download floo-rtc-ios.framework, and add it to the project manually.

### Plan A：By CocoaPods

Tips：If CocoaPods is not installed, please refer to [CocoaPods](https://cocoapods.org)

1.  Add a floo-ios pod into the Podfile:

    ```
    pod 'floo-rtc-ios'
    ```
2.  Install it by shell script:

    ```
    pod install
    ```

    Tips：If the latest version of the SDK cannot be installed, run the following command to update the local CocoaPods repository.

    ```
    pod repo update
    ```

### Plan B：By manual

Download [floo-rtc-ios.framework](https://package.lanyingim.com/floo-rtc-ios.zip) , put the unzipped framework into your project。

### Add a dependency

Add a GoogleWebRTC pod into the Podfile

```
  pod 'GoogleWebRTC', '~> 1.1'
```

### Create the user interface

```
//Create the remote video view
#if defined(RTC_SUPPORTS_METAL)
            _remoteVideoView = [[RTCMTLVideoView alloc] initWithFrame:CGRectZero];
#else
            RTCEAGLVideoView *remoteView = [[RTCEAGLVideoView alloc] initWithFrame:CGRectZero];
            _remoteVideoView = remoteView;
#endif            
            [self addSubview:_remoteVideoView];
//Create the local video view
            _localVideoView = [[UIView alloc] initWithFrame:CGRectZero];
            [self addSubview:_localVideoView];
```

### Business logic of an AV call
1. Import the RTCEngineManager

```
    #import <floo-rtc-ios/RTCEngineManager.h>
```

2. Add a RTC engine delegate

Add BMXRTCEngineProtocol to interface：
```
@interface CallViewController () < BMXRTCEngineProtocol >
```

Add a BMXRTCEngineProtocol delegate：
```
    [[RTCEngineManager engineWithType:kMaxEngine] addDelegate:self];
```

3. Join a room(Make a call)

```
    //Set the video resolution
    BMXVideoConfig *videoConfig = [[BMXVideoConfig alloc] init];
    [videoConfig setWidth:720];
    [videoConfig setHeight:1280];
    [[RTCEngineManager engineWithType:kMaxEngine] setVideoProfile:videoConfig];
    BMXRoomAuth *auth = [[BMXRoomAuth alloc] init];
    [auth setMUserId:userId];
    [auth setMToken:pin]; //The room password
    // The caller does not need to set the roomId, it will be returned when
    // the room is successfully created; the callee needs to set the same 
    // roomId as the caller
    [auth setMRoomId:roomId];
    [[RTCEngineManager engineWithType:kMaxEngine] joinRoomWithAuth:auth];
```

4. Join room result

```
- (void)onJoinRoomWithInfo:(NSString*)info roomId:(long long)roomId error:(BMXErrorCode)error{
    _roomId = roomId;
    if (error == BMXErrorCode_NoError) {
        //Publish the local stream
        [[RTCEngineManager engineWithType:kMaxEngine] publishWithType:BMXVideoMediaType_Camera hasVideo:_hasVideo hasAudio:YES];
        if (_isCaller) {
            [self sendCallMessage];
        }
    }
}
```

5. Received the remote video stream

```
- (void)onSubscribeWithStream:(BMXStream*)stream info:(NSString*)info error:(BMXErrorCode)error{
    if (error != BMXErrorCode_NoError) {
        return;
    }
    BOOL hasVideo = [stream getMEnableVideo];
    if (hasVideo) {
        BMXVideoCanvas *canvas = [[BMXVideoCanvas alloc] init];
        [canvas setMUserId:[stream getMUserId]];
        //Set the remote video view
        [canvas setMView:(void*)_videoCallView.remoteVideoView];
        //Render the remote video view
        [[RTCEngineManager engineWithType:kMaxEngine] startRemoteViewWithCanvas:canvas];
    }
}
```

6. Hangup the call, release the resources

```
- (void)hangupByMe:(BOOL)byMe{
    if (byMe) {
        [self sendHangupMessage];
    }
    [[RTCEngineManager engineWithType:kMaxEngine] leaveRoom];
    [[RTCEngineManager engineWithType:kMaxEngine] removeDelegate:self];
}
```

### Implement AV call signaling with RTC service

1. Add a delegate

Add BMXRTCServiceProtocol to interface ：
```
@interface CallViewController () < BMXRTCEngineProtocol, BMXRTCServiceProtocol >
```

Add a BMXRTCServiceProtocol delegate：
```
    [[RTCEngineManager engineWithType:kMaxEngine] addDelegate:self];
    [[[BMXClient sharedClient] rtcService] addDelegate:self];
```

2. Send a RTC call message

```
- (void)sendCallMessage{
    BMXMessageConfig *config = [BMXMessageConfig createMessageConfigWithMentionAll: NO];
    [config setRTCCallInfo:_hasVideo?BMXMessageConfig_RTCCallType_VideoCall:BMXMessageConfig_RTCCallType_AudioCall roomId:_roomId initiator:_myId roomType:BMXMessageConfig_RTCRoomType_Broadcast pin:_pin];
    _callId = config.getRTCCallId;

    BMXMessage *msg = [BMXMessage createRTCMessageWithFrom:_myId to:_peerId type:BMXMessage_MessageType_Single conversationId:_peerId content:@"new call"];
    msg.config = config;
    [msg setExtension:@"{\"rtc\":\"call\"}"];
    [[[BMXClient sharedClient] rtcService] sendRTCMessageWithMsg:msg completion:^(BMXError *aError) {
    }];
}
```

3. Send a RTC pickup message

```
- (void)sendPickupMessage{
    BMXMessageConfig *config = [BMXMessageConfig createMessageConfigWithMentionAll: NO];
    [config setRTCPickupInfo:_callId];
    BMXMessage *msg = [BMXMessage createRTCMessageWithFrom:_myId to:_peerId type:BMXMessage_MessageType_Single conversationId:_peerId content:@""];
    msg.config = config;
    [[[BMXClient sharedClient] rtcService] sendRTCMessageWithMsg:msg completion:^(BMXError *aError) {
    }];
    //Send a message read ACK to confirm the message that the caller made the call
    [self ackMessageWithMessageId:_messageId];
}

- (void)ackMessageWithMessageId:(long long)messageId{
    BMXMessage *msg = [[[BMXClient sharedClient] chatService] getMessage:messageId];
    if (msg) {
        [[[BMXClient sharedClient] chatService] ackMessageWithMsg:msg];
    }
}

```

4. Send a RTC hangup message

```
- (void)sendHangupMessage{
    BMXMessageConfig *config = [BMXMessageConfig createMessageConfigWithMentionAll: NO];
    if (_callId) {
        [config setRTCHangupInfo:_callId];
        _callId = nil;
    }
    NSTimeInterval duration = 0.0;
    NSString *content = @"canceled"; //Caller canceled
    if (!_isCaller) {
        content = @"rejected"; //Callee rejected
    }else{
        if (_ringTimes == 0) { //Callee not responding
            content = @"timeout";
        }
    }
    if (_pickupTimestamp > 1.0) {
        duration = [self getTimeStamp] - _pickupTimestamp;
    }
    if (duration > 1.0) {
        content = [NSString stringWithFormat:@"%.0f", duration];
    }
    BMXMessage *msg = [BMXMessage createRTCMessageWithFrom:_myId to:_peerId type:BMXMessage_MessageType_Single conversationId:_peerId content:content];
    msg.config = config;
    [[[BMXClient sharedClient] rtcService] sendRTCMessageWithMsg:msg completion:^(BMXError *aError) {
        NSNotification *noti = [NSNotification notificationWithName:@"call" object:self userInfo:@{@"event":@"hangup"}];
        [[NSNotificationCenter defaultCenter]postNotification:noti];
    }];
}

Handle hangup messages in the conversation page：
- (void)receiveNoti:(NSNotification*)noti
{
    NSString *event = noti.userInfo[@"event"];
    if ([event isEqualToString:@"hangup"]) {
        [[[BMXClient sharedClient] chatService] retrieveHistoryMessagesWithConversation:self.conversation refMsgId:0 size:1 completion:^(BMXMessageList *messageList, BMXError *error) {
            // Display the history messages
            //...
       }];
    }
}

```

5. Hangup a call

```
- (void)hangupByMe:(BOOL)byMe{
    if (byMe) {
        [self sendHangupMessage];
    }
    [[RTCEngineManager engineWithType:kMaxEngine] leaveRoom];
    [[RTCEngineManager engineWithType:kMaxEngine] removeDelegate:self];
    [[[BMXClient sharedClient] rtcService] removeDelegate:self];
}
```

6. The callee received a call message

```
#pragma mark - BMXRTCServiceProtocol
- (void)onRTCCallMessageReceiveWithMsg:(BMXMessage*)message {
    long long roomId = message.config.getRTCRoomId;
    long long myId = [self.account.usedId longLongValue];
    long long peerId = message.config.getRTCInitiator;
    if (myId == peerId){
        return;
    }
    NSString *pin = message.config.getRTCPin;
    NSString *callId = message.config.getRTCCallId;
    BOOL hasVideo = message.config.getRTCCallType == 1;
    //Open the call page
    //...
}
```

7. Received a hangup message

```
- (void)onRTCHangupMessageReceiveWithMsg:(BMXMessage*)msg {
    //Leave the room and ACK the message as read
}
```

8. Received a pickup message
```
- (void)onRTCPickupMessageReceiveWithMsg:(BMXMessage*)msg{
    //If the message is sent by my other terminal
    if ([msg.config.getRTCCallId isEqualToString: _callId] && msg.fromId == _myId) {
        //Close the call page and ACK the message as read
    }
}
```
