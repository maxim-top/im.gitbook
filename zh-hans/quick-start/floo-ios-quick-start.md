---
keywords: IOS 客户端, 音视频通话, Chat AI SDK, AI Agent
description: >-
  IOS 客户端快速开发前期准备 方式一：自动集成/CocoaPods 方式二：手动集成 快速集成 一、初始化 二、注册用户 三、登录链接服务器
  四、会话列表功能 五、断开连接 用户好友 基础功能 单聊 群聊 消息发送 构建消息实体 文本消息 图片消息 文件消息 位置消息 语音消息 消息操作
  消息接收监听 功能进阶 RTC 音视频通话 方式一：自动集成/CocoaPods 方式二：手动集成 添加We
---

# IOS 客户端快速开发

本页面供快速集成使用，了解更多请访问[详细文档](../reference/floo-ios.md)

## 前期准备

蓝莺 IM SDK 提供两种集成方式，可以通过 CocoaPods 自动集成我们的 floo-ios，也可以通过手动下载 floo-ios.framework, 手动添加到项目中。

### 方式一：自动集成/CocoaPods

提示：如果未安装cocoapods，请参照 [CocoaPods安装](https://cocoapods.org)

1.  在 Podfile 文件中加入 floo-ios :

    ```
    pod 'floo-ios'
    ```
2.  执行安装 ，命令如下

    ```
    pod install
    ```

    提示：如果无法安装 SDK 最新版本，运行以下命令更新本地的 CocoaPods 仓库列表

    ```
    pod repo update
    ```

### 方式二：手动集成

1. [下载 floo-ios.framework](https://package.lanyingim.com/floo-ios.zip) , 然后将文件引用到您的项目中。
2.  添加系统库依赖

    您除了在工程中导入 SDK 之前，还需要添加如下系统库的引用。

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

    注意：

    如果您的工程内已经引用libcrypto.a，为避免引入冲突不需要再次导入工程。

    如果您的工程内没有引用libcrypto.a，请解压下载的SDK包将libcrypto.a导入工程。
3. 在 Xcode 项目 Build Settings - Other Linker Flags 中，增加 "-ObjC"。
4. 设置 App 支持 HTTPS
5. 推送证书制作

## 快速集成

### 一、初始化

在您需要使用蓝莺IM SDK 功能的类中，import 相关头文件。

```
#import <floo-ios/floo_proxy.h>
```

您在使用蓝莺IM SDK 所有功能之前，您必须先调用此方法初始化 SDK。 在 App 的整个生命周期中，您只需要将 SDK 初始化一次。

```
    //设置数据和缓存目录路径
    NSString* dataDir = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES).firstObject stringByAppendingPathComponent:@"ChatData"];
    NSFileManager *fileManager = [NSFileManager defaultManager];
    if (![fileManager fileExistsAtPath:dataDir]) {
        [fileManager createDirectoryAtPath:dataDir withIntermediateDirectories:YES attributes:nil error:nil];
    }
    NSString* cacheDir = [NSSearchPathForDirectoriesInDomains(NSCachesDirectory, NSUserDomainMask, YES).firstObject stringByAppendingString:@"UserCache"];
    if (![fileManager fileExistsAtPath:cacheDir]) {
        [fileManager createDirectoryAtPath:cacheDir withIntermediateDirectories:YES attributes:nil error:nil];
    }
    NSLog(@"dataDir = %@", dataDir);
    NSLog(@"cacheDir = %@", cacheDir);
  
    //User agent信息
    NSString* phoneName = [[UIDevice currentDevice] name];
    NSString* localizedModel = [[UIDevice currentDevice] localizedModel];
    NSString* systemName = [[UIDevice currentDevice] systemName];
    NSString* phoneVersion = [[UIDevice currentDevice] systemVersion];
  
    NSString *userAgent = [NSString stringWithFormat:NSLocalizedString(@"Device_name_name", @"设备名称:%@;%@;%@;%@"), phoneName,localizedModel,systemName,phoneVersion];
    // pushCertName: DEV: apns_maximtop_dev_2022_11; DIST: apns_maximtop_distribution_2022_11
    //创建SDK配置
    BMXSDKConfig *config  = [[BMXSDKConfig alloc] initWithType:BMXClientType_iOS vsn:@"1" dataDir:dataDir
        cacheDir:cacheDir sDKVersion:@"1" pushCertName:@"apns_maximtop_distribution_2022_11" userAgent:userAgent
        appId:[AppIDManager sharedManager].appid.appId appSecret:@"47B13PBIAPDARZKD" deliveryAck:false];
    config.appID = [AppIDManager sharedManager].appid.appId;
    config.appSecret = @"47B13PBIAPDARZKD";
    config.loadAllServerConversations = YES;
    [config setLogLevel: BMXLogLevel_Debug];
    
    IMAcount *accout = [IMAcountInfoStorage loadObject];
    if (accout.isLogin) {
        if ([HostConfigManager checkLocalConfig]) {
            BMXSDKConfigHostConfig * hostConfig = [[BMXSDKConfigHostConfig alloc]initWithIm:[HostConfigManager sharedManager].IMServer port:[[HostConfigManager sharedManager].IMPort intValue] rest:[HostConfigManager sharedManager].restServer];
            config.hostConfig = hostConfig;
            config.enableDNS = NO;

        } else {
            config.enableDNS = YES;
        }
    } else {
        config.enableDNS = YES;
    }
    
    config.verifyCertificate = NO;
    //创建客户端实例
    [BMXClient createWithConfig: config];
```

### 二、注册用户

通过 BMXClient的单例，UserService类，传入 -signUpMobile:password:vertifyCode:userName:方法，注册IM账户。

```
    [[BMXClient sharedClient] signUpNewUserWithUsername:name password:password completion:^(BMXUserProfile *profile, BMXError *error) {
        if (error.errorCode == BMXErrorCode_NoError){
            [self registerLoginByName:name password:password];
        } else if (error.errorCode == BMXErrorCode_UserAlreadyExist){
            [self.config showErrorText:NSLocalizedString(@"This_username_already_exists", @"该用户名已存在")];
        } else if (error.errorCode == BMXErrorCode_InvalidRequestParameter) {
            [HQCustomToast showDialog:NSLocalizedString(@"username_constraint", @"用户名仅支持字母数字下划线中文组合，且不能是纯数字，不能以maxim、mta开头") time:5.0f];
        } else {
            [HQCustomToast showDialog:[error description]];
        }
    }];
```

### 三、登录链接服务器

将您在上一步获取到的 账号密码，通过 BMXClient的单例，UserService类，传入 -signInByNameWithName 方法，即可建立与服务器的连接。

提供两种登录模式：一种是普通手动登录，另一种是快速登录模式

```
[[BMXClient sharedClient] signInByNameWithName:name password:password completion:^(BMXError *error) {
        if (!error) {
            NSLog(@"登录成功 username = %lld , password = %@",name, password);
          } else {
            NSLog(@"失败 errorCode = %lu ", error.errorCode);
        }
     }];

// 快速登录（跳过获取token环节）
[[BMXClient sharedClient] fastSignInByNameWithName:name password:password completion:^(BMXError *error) {
 if (!error) {
     NSLog(@"登录成功 username = %@ , password = %@", name, password);
 } else {
     NSLog(@"失败 errorCode = %ld ", error.errorCode);
 }
}];
```

### 四、会话列表功能

通过 BMXClient的单例，ChatService类，传入 -getAllConversationsWithCompletion 方法，获取所有会话列表。返回BMXConversation对象的数组列表。

如果需要获取多设备同步的离线会话列表，需要在SDK初始化配置loadAllServerConversations属性值为Yes，默认只获取本地会话列表。

```
 [[[BMXClient sharedClient] chatService] getAllConversationsWithCompletion:^(BMXConversationList *res) {
    NSLog(@"%ld", res.size);
  }];
```

### 五、断开连接

在断开与蓝莺IM服务器的连接时，默认会停止接收远程推送,会自动解绑设备devicetoken.

```
    [[BMXClient sharedClient] signOutWithUid:(NSInteger)self.profile.userId ignoreUnbindDevice:NO completion:^(BMXError * _Nonnull error) {
        if (!error) {
            NSLog(@"Log out successfully");
        } else {
           NSLog(@"Log out failed");
        }
    }];
```

## 用户好友

*   添加好友

    ```
    [[[BMXClient sharedClient] rosterService] applyWithRosterId:rosterId message:reason completion:^(BMXError *error) {
        MAXLog(@"%lld", rosterId);
        if (!error) {
            MAXLog(@"申请成功");
        } else {
            MAXLog(@"申请失败");
        }
    }];

    ```
*   删除好友

    ```
      [[[BMXClient sharedClient] rosterService] removeWithRosterId:rosterId completion:^(BMXError *error) {

      }];
    ```
*   同意添加好友

    ```
      [[[BMXClient sharedClient] rosterService] acceptWithRosterId:rosterId completion:^(BMXError *error) {
      	 if (!error) {
          MAXLog(@"添加成功");
       }
          MAXLog(@"%@", error);

      }];
    ```
*   拒绝添加好友

    ```
      [[[BMXClient sharedClient] rosterService] declineWithRosterId:roster reason:reason completion:^(BMXError *error) {

      }];
    ```
*   获取好友列表

    开发者可以通过参数forceRefresh,选择从服务器或者是从本地获取好友列表数据。

    如果设置为NO, 当本地数为空，会自动从服务器去获取数据后返回结果。

    ```
      [[[BMXClient sharedClient] rosterService] get:forceRefresh completion:^(ListOfLongLong *list, BMXError *error) {
      if (!error) {
          MAXLog(@"%ld", rostIdList.count);
          [self searchRostersByidArray:[NSArray arrayWithArray:rostIdList]];
      }
      }];
    ```

## 基础功能

### 单聊

单聊是最基本的聊天界面，提供文字、表情、语音片段、图片等多种输入内容，解决 App 内用户的沟通瓶颈。单聊的 BMXConversationType 是 BMXConversationSingle，toId 是单聊对象的 userId。示例代码见后文“消息操作”一节：[消息操作](floo-ios-quick-start.md#消息操作)

### 群聊

群组的 BMXConversationType 是 BMXConversationGroup，toId 是群组 Id。

* 创建群组

开发者可以注册监听，创建群组成功后, 收到相应回调通知,开发者可以进行一些UI处理。

```
    // 构建创建群组信息实体
    BMXCreatGroupOption *option = [[BMXCreatGroupOption alloc] initWithGroupName:title groupDescription:description isPublic:YES];
    option.message = message;  // 建群时成员收到的邀请信息
    option.members = ids;   //建群时添加的成员列表
    [[[BMXClient sharedClient] groupService] createWithOptions:option completion:^(BMXGroup *group, BMXError *error) {
        if (!error) {
        }
    }];
```

*   加入群组

    ```
      /**
      加入一个群，根据群设置可能需要管理员批准

      @param group BMXGroup
      @param message 申请信息
      @param aCompletionBlock Error
      */
      - (void)joinGroup:(BMXGroup *)group
        message:(NSString *)message
       completion:(void(^)(BMXError *error))aCompletionBlock;
    ```
*   退出群组

    ```
       [[[BMXClient sharedClient] groupService] leaveWithGroup: self.group completion:^(BMXError *error) {
          if (!error) {
          }
      }];
    ```
*   解散群组

    ```
       [[[BMXClient sharedClient] groupService] destroyWithGroup:self.group completion:^(BMXError *error) {
          if (!error) {
            NSLog(@"销毁群");
        }
      }];
    ```
*   获取群成员列表

    ```
       [[[BMXClient sharedClient] groupService] getMembers:self.group forceRefresh:YES completion:^(NSArray<BMXGroupMemberList * *members, BMXError *error) {
          NSLog(@"%ld", members.size);
       }];
    ```
*   获取群组列表

    ```
      	/**
       获取群组列表

       @param forceRefresh 如果设置了forceRefresh则从服务器拉取
       @param aCompletionBlock GroupList, Error
       */
      [[[BMXClient sharedClient] groupService] get:forceRefresh completion:^(BMXGroupList *groupList, BMXError *error) {
      		if (!error) {
        NSLog(@"%ld", groupList.size);
      }
      }];
    ```
*   获取群组信息

    ```
      [[[BMXClient sharedClient] groupService] fetchGroupByIdWithGroupId:self.group.groupId forceRefresh:forceRefresh completion:^(BMXGroup *group, BMXError *error) {
       self.group = group;
      }];
    ```

## 消息发送

登录成功之后才能进行聊天操作。发消息时，单聊和群聊调用的是统一接口，区别只是要设置下 BMXConversationType

消息的远程推送：

开发者配置好远程推送的证书，且在代码中申请好权限，并将 deviceToken 传给蓝莺IM服务器，当接收者不在线的时候，蓝莺IM服务器会自动通过远程推送将消息发过去。

注： 推送的内容由发送消息接口的 pushContent 字段决定，内置消息发送的时候如果该字段没有值，将使用默认内容推送；自定义消息必须设置该字段，否则将不会推送。

以下是将 deviceToken 传给蓝莺IM接口

```
[[[BMXClient sharedClient] userService] bindDeviceWithToken:deviceToken completion:^(BMXError *error) {
      NSLog(@"绑定成功");
 }];
```

### 构建消息实体

### 文本消息

```
    BMXMessage *message;
    long long toId = 0;
    NSInteger conversationId = self.conversationId;
    if (self.messageType == BMXMessage_MessageType_Single) {
        toId = self.currentRoster.rosterId;
    }else {
        toId = self.currentGroup.groupId;
    }
    BMXMessage *message = [BMXMessage createMessageWithFrom:[self.account.usedId longLongValue] to:toId type:self.messageType conversationId:conversationId content:content];
```

### 图片消息

```
    UIImage *image = contentImg;
    NSData *imageData = UIImageJPEGRepresentation(image,1.0f);
    NSData *thumImageData =  UIImageJPEGRepresentation(image,1.0f);
    IMAcount *account = [IMAcountInfoStorage loadObject];
    BMXMessageAttachmentSize *sz = [[BMXMessageAttachmentSize alloc] initWithWidth:image.size.width height:image.size.height];
    BMXImageAttachment *imageAttachment = [[BMXImageAttachment alloc] initWithData:imageData thumbnailData:thumImageData imageSize:sz displayName:@"" conversationId: roster.rosterId];
    BMXMessage *msg;
    msg = [BMXMessage createMessageWithFrom:[account.usedId longLongValue] to:roster.rosterId type: BMXMessage_MessageType_Single conversationId:roster.rosterId attachment:imageAttachment];
    if (msg) {
	[[[BMXClient sharedClient] chatService] sendMessageWithMsg: msg completion:nil];
	[self.navigationController popViewControllerAnimated:YES];
    }

```

### 文件消息

```
 BMXFileAttachment *fileAttachment = [[BMXFileAttachment alloc] initWithData:dic[@"data"] displayName:dic[@"displayName"] conversationId: (long)self.conversationId];
            messageObject = [self configMessage:fileAttachment];
            messageModel.content = dic[@"displayName"];
```

### 位置消息

```
   NSDictionary *locationInfo = (NSDictionary *)content;
   double latitude = [locationInfo[@"latitude"] doubleValue];
   double longitude = [locationInfo[@"longitude"] doubleValue];
   NSString *address = locationInfo[@"address"];
            
    BMXLocationAttachment *locationment = [[BMXLocationAttachment alloc] initWithLatitude:latitude longitude:longitude address:address];
    messageObject = [self configMessage:locationment];
    messageModel.content = [NSString stringWithFormat:NSLocalizedString(@"Current_location", @"当前位置：%@"),locationment.address];
```

### 语音消息

```
    NSString *voicePath = (NSString *)content;
    BMXVoiceAttachment *vocieAttachment = [[BMXVoiceAttachment alloc] initWithPath:voicePath duration:duartion displayName:@"voice"];
    messageObject = [self configMessage:vocieAttachment];
    messageModel.vociePath = voicePath;
    messageModel.content = [NSString stringWithFormat:@"  %d s",duartion];
```

### 消息操作

消息实体构建完成后，通过 BMXClient的单例，ChatService类，调用 -sendMessage: 方法，将构建好的消息实体传入，即可实现消息发送

*   发送

    ```
     /**
      发送消息，消息状态变化会通过listener通知
     **/
     [[[BMXClient sharedClient] chatService] sendMessageWithMsg: messageObject completion:^(BMXError *aError) {
        }];
    ```
*   转发

    ```
     /**
     简单转发消息，用户应当通过BMXMessagseObject,initWithForwardMessage先创建转发消息
     **/
     BMXMessage *m = [BMXMessage createForwardMessageWithMsg:self.currentMessage.messageObjc from:[self.account.usedId longLongValue] to:group.groupId type:BMXMessage_MessageType_Group conversationId:group.groupId];
    [[[BMXClient sharedClient] chatService] forwardMessageWithMsg:m completion:nil];
    ```
*   重发

    ```
      /**
     重新发送消息，消息状态变化会通过listener通知
     **/
     [[[BMXClient sharedClient] chatService]resendMessageWithMsg:self.messageModel.messageObjc completion:^(BMXMessageObject *message, BMXError *error) {
     }];
    ```
*   撤回

    ```
     /**
     撤回消息，消息状态变化会通过listener通知
     **/
     [[[BMXClient sharedClient] chatService] recallMessageWithMsg: self.currentMessage.messageObjc completion:nil];
    ```
*   下载消息附件

    ```
       /**
      * 下载附件，下载状态变化和进度通过listener通知
      **/
       [[[BMXClient sharedClient] chatService] downloadAttachmentWithMsg:messagemodel.messageObjc completion:^(BMXError *aError) {
       }];
    ```

## 消息接收监听

注册消息回调

```
    /**
     * 添加聊天监听者
     **/
    [[[BMXClient sharedClient] chatService] addDelegate:self delegateQueue:dispatch_get_main_queue()];
	
    /**
      * 移除聊天监听者
      **/
    [[[BMXClient sharedClient] chatService] removeDelegate:self];
```

*   接收到消息通知

    ```
      /**
      * 收到消息
      **/
      - (void)receivedMessages:(NSArray<BMXMessage*> *)messages {

      	  if (message.contentType == BMXContentTypeText) {
          			// 收到文本消息，UI等处理

            } else if (message.contentType == BMXContentTypeImage) {
                	// 收到图片消息

            } else if (message.contentType == BMXContentTypeVoice) {
      				// 收到语音消息

            } else if (message.contentType == BMXContentTypeLocation) {
             		// 收到位置消息

            } else if (message.contentType == BMXContentTypeFile) {
                	// 收到文件消息

            }
      }
    ```
*   消息发送后状态回调通知

    ```
      //  消息状态发生变化
      - (void)messageStatusChanged:(BMXMessage *)message
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
*   附件消息发送状态回调

    ```
      - (void)messageAttachmentUploadProgressChanged:(BMXMessage *)message percent:(int)percent {
      // percent为上传进度百分比

      }
    ```
*   消息提醒设置 通过 BMXClient的单例，UserService类，以下方法可以设置消息推送提醒

    ```
      [[[BMXClient sharedClient] userService] setEnablePush:state completion:^(BMXError *error) {
            if (!error) {
                [HQCustomToast showDialog:NSLocalizedString(@"Set_successfully", @"设置成功")];
            }
        }];
    ```
*   附件消息下载状态变化

    ```
      /**
      * 附件下载状态发生变化
      **/
      - (void)messageAttachmentStatusDidChanged:(BMXMessage *)message
                        error:(BMXError*)error
                      percent:(int)percent;
    ```

## 功能进阶

#### 自定义消息

BMXMessage实体中，提供可扩展属性(extension 和 config) extension 为开发使用的扩展字段，例如编辑状态。 config 为SDK自用的扩展字段，例如mention功能，push功能

*   群组@功能

    群组中支持 @ 功能，满足您 @ 指定用户或 @ 所有人的需求，开发者在BMXMessage中通过设置config 来实现群主@功能，已经@成员后的会下发推送通知
*   消息正在输入状态

    ```
      // 可以使用extension，来扩展正在编辑状态消息，（json格式，可以扩展多种自定义功能）
      @property (nonatomic, copy) NSString *extension;
    ```
*   消息阅读回执

    ```
      //全部消息是否已读
      @property (nonatomic,assign) BOOL isRead;
      //接受消息是否发送已读回执
      @property (nonatomic,assign) BOOL isReadAcked;
      //接受消息是否发送已送达
      @property (nonatomic, assign) BOOL isDeliveryAcked;
    ```
*   多端阅读消息数同步

    BMXConversation 实体提供消息未读数量和会话中所有消息数量

    ```
      /** 
       未读消息数量 
      */
      @property (nonatomic,assign, readonly) NSInteger unreadNumber;
      
      /**
       会话中所有消息数量
      */
      @property (nonatomic,assign, readonly) NSInteger messageCount;
    ```
*   消息搜索

    根据关键字搜索指定消息内容

    ```
      [[[BMXClient sharedClient] chatService] searchMessagesByKeyWordsWithKeywords:keywords refTime:0 size:100 arg5:BMXConversation_Direction_Up completion:^(BMXMessageListList *result, BMXError *aError) {

      }];
    ```

## RTC 音视频通话

蓝莺 IM 系统的RTC通话功能，需要客户端集成floo-ios和floo-rtc-ios两个SDK。floo-ios为音视频通话提供了信令通道，floo-rtc-ios实现了RTC通话相关的业务逻辑。所以，实现音视频通话的前提是已经集成了floo-ios，并实现了登录和收发消息功能。

蓝莺 IM RTC SDK 目前实现了一对一的视频和语音通话功能。集成方式有两种：可以通过 CocoaPods 自动集成我们的 floo-rtc-ios，也可以通过手动下载 floo-rtc-ios.framework, 手动添加到项目中。

### 方式一：自动集成/CocoaPods

提示：如果未安装cocoapods，请参照 [CocoaPods安装](https://cocoapods.org)

1.  在 Podfile 文件中加入 floo-rtc-ios :

    ```
    pod 'floo-rtc-ios'
    ```
2.  执行安装 ，命令如下

    ```
    pod install
    ```

    提示：如果无法安装 SDK 最新版本，运行以下命令更新本地的 CocoaPods 仓库列表

    ```
    pod repo update
    ```

### 方式二：手动集成

[下载 floo-rtc-ios.framework](https://package.lanyingim.com/floo-rtc-ios.zip) , 然后将文件引用到您的项目中。

### 添加WebRTC依赖

在 Podfile文件中加入

```
  pod 'GoogleWebRTC', '~> 1.1'
```

### 创建用户界面

```
//创建对方画面视图
#if defined(RTC_SUPPORTS_METAL)
            _remoteVideoView = [[RTCMTLVideoView alloc] initWithFrame:CGRectZero];
#else
            RTCEAGLVideoView *remoteView = [[RTCEAGLVideoView alloc] initWithFrame:CGRectZero];
            _remoteVideoView = remoteView;
#endif            
            [self addSubview:_remoteVideoView];
//创建本地画面视图
            _localVideoView = [[UIView alloc] initWithFrame:CGRectZero];
            [self addSubview:_localVideoView];
```

### 音视频通话业务逻辑

1. 导入RTCEngineManager

```
    #import <floo-rtc-ios/RTCEngineManager.h>
```

2. 添加事件监听

在类接口声明中添加协议：BMXRTCEngineProtocol：

```
@interface CallViewController () < BMXRTCEngineProtocol >
```

添加BMXRTCEngineProtocol事件监听：

```
    [[RTCEngineManager engineWithType:kMaxEngine] addDelegate:self];
```

3. 加入房间

```
    //设置视频分辨率
    BMXVideoConfig *videoConfig = [[BMXVideoConfig alloc] init];
    [videoConfig setWidth:720];
    [videoConfig setHeight:1280];
    [[RTCEngineManager engineWithType:kMaxEngine] setVideoProfile:videoConfig];
    //设置用户ID、pin密码和房间ID
    BMXRoomAuth *auth = [[BMXRoomAuth alloc] init];
    [auth setMUserId:userId];
    [auth setMToken:pin]; //房间pin密码，建议随机生成高强度密码
    [auth setMRoomId:roomId]; //主叫方无须设置roomId，房间创建成功事件会返回系统分配的roomId；被叫方需要设置与主叫方一样的roomId
    [[RTCEngineManager engineWithType:kMaxEngine] joinRoomWithAuth:auth];
```

4. 加入房间结果回调

```
- (void)onJoinRoomWithInfo:(NSString*)info roomId:(long long)roomId error:(BMXErrorCode)error{
    //保存房间ID
    _roomId = roomId;
    if (error == BMXErrorCode_NoError) {
        //发布本地音视频流
        [[RTCEngineManager engineWithType:kMaxEngine] publishWithType:BMXVideoMediaType_Camera hasVideo:_hasVideo hasAudio:YES];
        //主叫方开始发送呼叫的消息
        if (_isCaller) {
            [self sendCallMessage];
        }
    }
}
```

5. 收到对方视频流

```
- (void)onSubscribeWithStream:(BMXStream*)stream info:(NSString*)info error:(BMXErrorCode)error{
    if (error != BMXErrorCode_NoError) {
        return;
    }
    BOOL hasVideo = [stream getMEnableVideo];
    if (hasVideo) {
        BMXVideoCanvas *canvas = [[BMXVideoCanvas alloc] init];
        [canvas setMUserId:[stream getMUserId]];
        //设置用于渲染对方视频画面的视图
        [canvas setMView:(void*)_videoCallView.remoteVideoView];
        //渲染对方视频画面
        [[RTCEngineManager engineWithType:kMaxEngine] startRemoteViewWithCanvas:canvas];
    }
}
```

6. 挂断通话

```
- (void)hangupByMe:(BOOL)byMe{
    //主动挂断一方需要通知对方挂断
    if (byMe) {
        [self sendHangupMessage];
    }
    //离开房间
    [[RTCEngineManager engineWithType:kMaxEngine] leaveRoom];
    //移除监听
    [[RTCEngineManager engineWithType:kMaxEngine] removeDelegate:self];
}
```

### 使用rtcService实现音视频通话信令

1. 添加事件监听

在类接口声明中添加协议：BMXRTCServiceProtocol：

```
@interface CallViewController () < BMXRTCEngineProtocol, BMXRTCServiceProtocol >
```

添加BMXChatServiceProtocol和BMXRTCServiceProtocol事件监听：

```
    [[RTCEngineManager engineWithType:kMaxEngine] addDelegate:self];
    [[[BMXClient sharedClient] rtcService] addDelegate:self];
```

2. 发送呼叫消息

```
- (void)sendCallMessage{
    //封装呼叫消息config
    BMXMessageConfig *config = [BMXMessageConfig createMessageConfigWithMentionAll: NO];
    [config setRTCCallInfo:_hasVideo?BMXMessageConfig_RTCCallType_VideoCall:BMXMessageConfig_RTCCallType_AudioCall roomId:_roomId initiator:_myId roomType:BMXMessageConfig_RTCRoomType_Broadcast pin:_pin];
    _callId = config.getRTCCallId;

    BMXMessage *msg = [BMXMessage createRTCMessageWithFrom:_myId to:_peerId type:BMXMessage_MessageType_Single conversationId:_peerId content:@"new call"];
    msg.config = config;
    //设置消息扩展信息，离线时服务端会发送推送
    [msg setExtension:@"{\"rtc\":\"call\"}"];
    [[[BMXClient sharedClient] rtcService] sendRTCMessageWithMsg:msg completion:^(BMXError *aError) {
    }];
}
```

3. 发送接听消息

```
- (void)sendPickupMessage{
    //封装接听消息config
    BMXMessageConfig *config = [BMXMessageConfig createMessageConfigWithMentionAll: NO];
    [config setRTCPickupInfo:_callId];
    BMXMessage *msg = [BMXMessage createRTCMessageWithFrom:_myId to:_peerId type:BMXMessage_MessageType_Single conversationId:_peerId content:@""];
    msg.config = config;
    [[[BMXClient sharedClient] rtcService] sendRTCMessageWithMsg:msg completion:^(BMXError *aError) {
    }];
    //发送消息已读回执，确认主叫端呼叫的那条消息
    [self ackMessageWithMessageId:_messageId];
}

- (void)ackMessageWithMessageId:(long long)messageId{
    BMXMessage *msg = [[[BMXClient sharedClient] chatService] getMessage:messageId];
    if (msg) {
        [[[BMXClient sharedClient] chatService] ackMessageWithMsg:msg];
    }
}

```

4. 发送挂断消息

```
- (void)sendHangupMessage{
    //封装挂断消息config
    BMXMessageConfig *config = [BMXMessageConfig createMessageConfigWithMentionAll: NO];
    if (_callId) {
        [config setRTCHangupInfo:_callId];
        _callId = nil;
    }
    //设置消息内容，用于界面展示通话时长、已取消、已拒绝、未接听等
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
        //同步挂断消息，用于实时更新会话界面的通话历史记录
        NSNotification *noti = [NSNotification notificationWithName:@"call" object:self userInfo:@{@"event":@"hangup"}];
        //发送通知
        [[NSNotificationCenter defaultCenter]postNotification:noti];
    }];
}

在会话界面处理挂断消息：
- (void)receiveNoti:(NSNotification*)noti
{
    NSString *event = noti.userInfo[@"event"];
    if ([event isEqualToString:@"hangup"]) {
        [[[BMXClient sharedClient] chatService] retrieveHistoryMessagesWithConversation:self.conversation refMsgId:0 size:1 completion:^(BMXMessageList *messageList, BMXError *error) {
            //会话界面的通话历史记录
            //...
       }];
    }
}

```

5. 挂断通话

```
- (void)hangupByMe:(BOOL)byMe{
    //主动挂断一方需要通知对方挂断
    if (byMe) {
        [self sendHangupMessage];
    }
    //离开房间
    [[RTCEngineManager engineWithType:kMaxEngine] leaveRoom];
    //移除监听
    [[RTCEngineManager engineWithType:kMaxEngine] removeDelegate:self];
    [[[BMXClient sharedClient] rtcService] removeDelegate:self];
}
```

6. 被叫方处理接收到的呼叫消息

```
#pragma mark - BMXRTCServiceProtocol
- (void)onRTCCallMessageReceiveWithMsg:(BMXMessage*)message {
    //解析呼叫消息config字段
    long long roomId = message.config.getRTCRoomId;
    long long myId = [self.account.usedId longLongValue];
    long long peerId = message.config.getRTCInitiator;
    if (myId == peerId){
        return;
    }
    NSString *pin = message.config.getRTCPin;
    NSString *callId = message.config.getRTCCallId;
    BOOL hasVideo = message.config.getRTCCallType == 1;
    //打开呼叫界面
    //...
}
```

7. 处理接收到的挂断消息

```
- (void)onRTCHangupMessageReceiveWithMsg:(BMXMessage*)msg {
    //离开房间并确认消息为已读
}
```

8. 处理接收到的接听消息

```
- (void)onRTCPickupMessageReceiveWithMsg:(BMXMessage*)msg{
    //如果消息是我的其它终端发送的
    if ([msg.config.getRTCCallId isEqualToString: _callId] && msg.fromId == _myId) {
        //关闭呼叫界面并确认消息已读
    }
}
```
