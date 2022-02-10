# 即时通讯开发指南（IM）

## 产品概述

美信拓扑是可以一键启用多云架构的即时通讯云服务。企业可以通过集成即时通讯 IM SDK，配合使用云服务，可以为应用快速添加聊天功能。集成SDK后，典型的应用架构如下：

![美信拓扑开放平台架构](.gitbook/assets/1.png)

依靠十余年的即时通讯 IM 技术积累，美信拓扑IM SDK和服务 API 都已经过优化设计，通过更加简单的接口提供更加专业的服务。

一键启用多云架构，是美信拓扑即时通讯云服务的独特优势。

一键启用意味着，从基础功能到服务定制，均可通过控制台一键操作即开即用；而多云架构，支持应用在公有云、专有云和私有云的不同部署方式自由迁移，顺应业务发展阶段，无缝迁移无忧切换。

配合无所不能的控制台，你需要做的只有两件事，一是客户端集成美信拓扑 IM SDK，二是服务端对接美信拓扑 API 服务。本文主要介绍客户端 SDK 集成相关工作。

美信拓扑 IM SDK 跨平台的，包括移动端（iOS/Android）、PC桌面端（Linux/Windows/Mac）、Web浏览器端（包括H5）以及微信小程序等。为了最大程度的复用，并提高服务质量，美信拓扑 IM SDK 技术栈如下：

![美信拓扑IM SDK 技术栈](.gitbook/assets/2.jpeg)

1. 统一设计并实现二进制即时通讯协议 XSYNC ，分别实现了 C++ 版和 Javascript 版；
2. 在 C++ 通讯库的基础上封装了全平台的 C++ SDK，并以此为基础继续封装了移动端（iOS/Android）和PC桌面端（Linux/Windows/Mac）SDK；
3. 移动端在实现美信拓扑 DemoApp 前均封装了本地的 UI Kit 库，但 iOS 和 Android 稍有不同，iOS 通过 Object-C 封装 SDK 后进一步转化成 Swift 库，而 Android 则通过 Swig 框架和 JNI 技术直接封装了 Java 库供上层使用；
4. PC桌面端通过 Electron 封装 C++ 通讯库后，与 Web 浏览器端共享一套由 Vue.js 实现的 UI 组件；
5. Javascript 通讯库通过 WebAssembly 加密封装后提供给 Web 浏览器端（包括H5）使用；
6. 微信小程序由于平台原因，除协议库外均与 Web 浏览器端不同，系统层调用了微信的网络和存储库，上层用的微信的 UI Kit；

## 新手接入指南

开始集成所有客户端之前，你需要通过美信拓扑控制台，创建应用并获取应用的 AppID 然后在各端设置。

1. 创建账号

注册并登陆[美信拓扑控制台](https://console.maximtop.com)

1. 创建应用

登录成功后，点击创建应用

![](.gitbook/assets/1-1.create\_app.png)

创建应用成功后，应用信息页面内获得该应用的 App ID 等重要信息，也可以点击功能页进行配置。

![](.gitbook/assets/1-2.app\_info.png)

## 服务端

### API 文档

[服务端 API](reference/server-api/)

### 私有部署安装

下载[安装包](https://package.maximtop.com/linux/amd64/maxim.ctl) 后直接在控制台按照步骤操作，亦可查看[详细安装文档](quick-start/how-to-deploy-private-cloud.md)

## 客户端SDK

美信拓扑IM 客户端SDK，代号 floo。文中有 IM SDK 的地方将会用 floo 代替。

### API详细文档

1. [iOS API](reference/floo-ios/constants.md)
2. [Android API](reference/floo-ios/protocols.md)
3. [Web API](reference/floo-web.md)，微信小程序API与此完全相同
4. [C++ API](reference/floo-android.md)

### 平台兼容

美信拓扑支持以下平台：

| 平台      | 兼容性                                        |
| ------- | ------------------------------------------ |
| iOS     | 兼容iOS 9.0 +                                |
| Android | 兼容Android 4.1 +                            |
| Web     | 兼容 IE10 及以上、Chrome、Firefox、Safari等         |
| PC      | Node.js版本SDK支持Electron开发框架，但仅支持 x86\_64 架构 |
| Linux   | C++版本SDK，支持 x86/x86-x64/ARM/MIPS 架构        |

### Changelog

待补充，请参考[源码更新](https://github.com/maxim-top/)

### 客户端错误码

| 错误编码                              | 描述信息                                                                      |
| --------------------------------- | ------------------------------------------------------------------------- |
| InvalidParam                      | Input parameters are invalid                                              |
| NotFound                          | Operate object is NOT exist                                               |
| UserNotLogin                      | User have NOT signed in                                                   |
| UserAlreadyLogin                  | User have signed in using another account                                 |
| UserAuthFailed                    | User sign in authentication failed, user name/id or password is incorrect |
| UserPermissionDenied              | User is NOT granted for the operation.                                    |
| UserNotExist                      | User is NOT exist                                                         |
| UserAlreadyExist                  | User has already exist                                                    |
| UserFrozen                        | User was frozen                                                           |
| UserBanned                        | User was banned to send message                                           |
| UserRemoved                       | User account was removed                                                  |
| UserTooManyDevice                 | User sign in from too many devices                                        |
| UserPasswordChanged               | User password was changed from other device                               |
| UserKickedBySameDevice            | User was kicked out by the same device                                    |
| UserKickedByOtherDevices          | User was kicked out by another device                                     |
| UserAbnormal                      | User sign in status is abnomal, advise to sign in again                   |
| UserCancel                        | User cancel operation                                                     |
| InvalidVerificationCode           | invalid verification code                                                 |
| InvalidRequestParameter           | invalid request parameter(s)                                              |
| InvalidUserNameParameter          | invalud username parameter                                                |
| MissingAccessToken                | missing access token                                                      |
| CurrentUserIsInRoster             | current user is in roster                                                 |
| CurrentUserIsInBlocklist          | current user is in block list                                             |
| AnswerFailed                      | the application does not exist or has already expired                     |
| InvalidToken                      | invalid token                                                             |
| RosterNotFriend                   | User was not in roster friend list                                        |
| RosterBlockListExist              | User was block by roster                                                  |
| RosterRejectApplication           | User application was reject by roster                                     |
| GroupServerDbError                | Server db error                                                           |
| GroupNotExist                     | Group NOT Found                                                           |
| GroupNotMemberFound               | User is NOT group member                                                  |
| GroupMsgNotifyTypeUnknown         | Unknown msg\_notify\_type                                                 |
| GroupOwnerCannotLeave             | Owner can not leave group                                                 |
| GroupTransferNotAllowed           | Group only can transfer to group member                                   |
| GroupRecoveryMode                 | Group is recovery mode                                                    |
| GroupExceedLimitGlobal            | Global group count exceed limit                                           |
| GroupExceedLimitUserCreate        | Group count user created exceed limit                                     |
| GroupExceedLimitUserJoin          | Group count user joined exceed limit                                      |
| GroupCapacityExceedLimit          | Group capacity exceed limit                                               |
| GroupMemberPermissionRequired,    | This operation needs group member permission                              |
| GroupAdminPermissionRequired,     | This operation needs group admin permission                               |
| GroupOwnerPermissionRequired      | This operation needs group owner permission                               |
| GroupApplicationExpiredOrHandled, | Application has expired or be handled                                     |
| GroupInvitationExpiredOrHandled,  | Invitation has expired or be handled                                      |
| GroupKickTooManyTimes             | User has been kicked too many times                                       |
| GroupMemberExist                  | User is already in group                                                  |
| GroupBlockListExist               | User is in group block list                                               |
| GroupAnnouncementNotFound         | Group announcement is not found                                           |
| GroupAnnouncementForbidden        | Group announcement has been forbidden by system admin                     |
| GroupSharedFileNotFound           | Group shared file is not found                                            |
| GroupSharedFileOperateNotAllowed  | Do not have permission operate shared file                                |
| GroupMemberBanned                 | Group banned member to send message                                       |
| SignInCancelled                   | Sign in operation was cancelled                                           |
| SignInTimeout                     | Sign in operation was timeout                                             |
| SignInFailed                      | Sign in operation failed                                                  |
| DbOperationFailed                 | Datebase read/write failed                                                |
| MessageInvalid                    | Message is invalid                                                        |
| MessageOutRecallTime              | Out of recall permission time                                             |
| MessageRecallDisabled             | Disable recall message                                                    |
| MessageCensored                   | Message include censored content                                          |
| MessageInvalidType                | Message don't support the operation                                       |
| ServerNotReachable                | Server is NOT reachable                                                   |
| ServerUnknownError                | Unknown server error                                                      |
| ServerInvalid                     | Server is invalid                                                         |
| ServerDecryptionFailed            | Server decryption failed                                                  |
| ServerEncryptMethodUnsupported    | Server don't support encrypt method                                       |
| ServerBusy                        | Server is busy                                                            |
| ServerNeedRetry                   | Server need retry                                                         |
| ServerTimeOut                     | Server time out                                                           |
| ServerConnectFailed               | Server connect failed                                                     |
| ServerDNSFailed                   | Server get DNS list failed                                                |
| ServerNeedReconnected             | Server changed need reconnect again                                       |
| ServerFileUploadUnknownError      | Server file upload unknow error                                           |
| ServerFileDownloadUnknownError    | Server file download unknow error                                         |
| ServerInvalidLicense              | Server invalid license                                                    |
| ServerLicenseLimit                | Server license limit                                                      |
| ServerAppFrozen                   | Server App frozen                                                         |
| ServerTooManyRequest              | Server too many request                                                   |
| ServerNotAllowOpenRegister        | Server not allow open register                                            |
| ServerFireplaceUnknownError       | Server Fireplace unknown error                                            |
| ServerResponseInvalid             | Server response invald                                                    |
| ServerInvalidUploadUrl            | Server invalid upload url                                                 |
