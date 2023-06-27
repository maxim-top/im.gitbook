# 安卓客户端快速开发

本页面供快速集成使用，了解更多请访问[详细文档](../reference/floo-android.md)

## Android SDK 集成说明

### SDK 架构

蓝莺IM SDK（代号 floo ）底层使用 C++ 实现，各平台（Android、iOS、Linux等）在此基础上再行封装， 完成本地库的开发，以达到多平台复用的目的，并保持跨平台协议实现的一致性。 floo-android 作为供安卓使用的本地应用库，有两种 API 可供开发者使用，即低级 API 和高级 API，也即同步接口和异步接口。

#### 低级 API (low-level)

同步调用接口，类名以Service结尾，为方便理解，下文说明中用 L/S 表示，其中 L 表示 Low-level, S 表示 Sync。

如前所述，floo-android 主体由 [SWIG](http://www.swig.org/index.php) 框架自动生成。用 SWIG 生成的 Java 代码，通过 JNI 方式调用底层 C++ 类库，因此大部分接口均为同步，即调用接口后，完成后返回结果。

代码生成和转换的过程中，相关数据结构得以直接映射到底层类库，减少了内存拷贝，因此其性能接近于直接调用底层库。

同步方式的服务类如下：

```
- BMXClient: SDK功能聚合类，包含了所有的service类、实现了网络事件监听接口
- BMXChatService: 消息发送、消息历史获取、会话列表
- BMXUserService: 注册账号、登入、登出、我的设置
- BMXRosterService: 好友列表、黑名单
- BMXGroupService: 群管理（创建、解散、查找、设置、成员管理、邀请、申请、接受、拒绝）
```

#### 高级 API (high-level)

异步调用接口，类名以Manager结尾，为方便理解，下文用 H/A 表示，其中 H 表示 High-level, A 表示 Async。

考虑到开发者集成方便，我们也基于此类重新封装了高级 API，使用了更为友好的数据结构，并完成了异步封装。

简单来讲，相关调用会在子线程执行具体操作（例如：搜索好友），当前线程会直接返回不会阻塞。具体操作的结果则通过回调函数通知调用方，后者可以在其中处理 UI 刷新等业务逻辑。

异步方式的服务类如下：

```
- BaseManeger:Manger管理基础类
- ChatManager:消息发送、消息历史获取、会话列表
- UserManager:注册账号、登入、登出、我的设置
- RosterManager:好友列表、黑名单
- BMXCallBack:无类型接口回调
- BMXDataCallBack<T>: 泛型类型带数据回调
```

#### 其他工具类

```
- BMXGroupServiceListener:群事件监听
- BMXUserServiceListener:用户事件监听
- BMXRosterServiceListener:好友事件监听
- BMXNetworkListener:网络事件监听接口，由BMXClient实现
- BMXConversation:会话
- BMXMessage:消息
- BMXGroup:群
- BMXRosterItem花名册项（好友、陌生人、黑名单、前好友）
- BMXUserProfile:用户信息
```

#### 类库示意图如下

```
                                                 +---> BMXUserService
                                                 |
                              +---------------+  +---> BMXChatService
                              |               |  |
                          +---+ 低级 API: L/S  +------> BMXRosterService
                          |   |               |  |
                          |   +---------------+  +---> BMXGroupService
                          |
                          |                         +---> BMXUserManager
                          |   +---------------+     |
+----------------------+  |   |               |     +---> BMXChatManager
|                      |  +---+ 高级 API: H/A +-----+
| 蓝莺 IM SDK: Floo     +--+   |               |     +---> BMXRosterManager
|                      |  |   +---------------+     |
+----------------------+  |                         +---> BMXGroupManager
                          |
                          |                       +--->  BMXClient
                          |   +----------------+  |
                          |   |                |  +--->  BMXSDKConfig
                          +---+ Utility：工具类 +--+
                              |                |  +--->  BMXMessage
                              +----------------+  |
                                                  +--->  BMXConversation
                                                  |
                                                  +--->  BMXUserProfile
                                                  |
                                                  +--->  BMXGroup
                                                  |
                                                  +--->  BMXDevice
```

### 导入SDK

SDK导入可以选择aar格式或者jar+so格式

#### aar格式

* 下载aar文件到项目的libs目录
* 在build.gradle文件dependencies块中增加依赖，参照[lanying-im-android源码](https://github.com/maxim-top/lanying-im-android/blob/master/app/build.gradle#L94)使用最新版。新版的gradle只要声明了对libs目录的依赖，无须再单独声明对其中aar文件的依赖。

#### jar+so格式

* 下载jar包和so库到项目的libs目录
* 在build.gradle文件中增加：implementation fileTree(dir: 'libs', include: \['\*.jar'])

### 权限配置

在AndroidManifest.xml 里增加加以下权限：

```
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_LOCATION_EXTRA_COMMANDS" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.WRITE_CONTACTS" />
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.CHANGE_WIFI_STATE" />
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.CALL_PHONE" />
    <uses-permission android:name="android.permission.READ_CONTACTS" />
    <uses-permission android:name="android.permission.WAKE_LOCK" />
```

### APP混淆 <a href="#app-hun-xiao" id="app-hun-xiao"></a>

```
在 ProGuard 文件中加入：-keep class im.floo.floolib.**{*;}
```

### 快速集成

#### BMXClient初始化

**第一步 导入so库文件**

在 app 入口类中增加导入

```
    static {
        System.loadLibrary("floo");
    }
```

**第二步 初始化BMXClient**

```
    // 设置存储路径
    String appPath = AppContextUtils.getAppContext().getFilesDir().getPath();
    File dataPath = new File(appPath + "/data_dir");
    File cachePath = new File(appPath + "/cache_dir");
    dataPath.mkdirs();
    cachePath.mkdirs();

	// 设置推送平台对应的ID
    String pushId = getPushId();

    // 配置sdk config
    BMXSDKConfig config = new BMXSDKConfig(BMXClientType.Android, "1", dataPath.getAbsolutePath(),
                cachePath.getAbsolutePath(), TextUtils.isEmpty(pushId) ? "MaxIM" : pushId);
    config.setConsoleOutput(true);
    config.setLogLevel(BMXLogLevel.Debug);

	// 初始化BMXClient
    BMXClient bmxClient = BMXClient.create(conf);
```

注意： 如果使用高级API（异步调用方式），需要通过以下方法获取到服务类API的实体：

```
- ChatManager: 通过bmxClient.getChatManager()获取到消息的manager对象。
- UserManager: 通过bmxClient.getUserManager()获取到用户的manager对象。
- GroupManager: 通过bmxClient.getGroupManager()获取到群相关的manager对象。
- RosterManager: 通过bmxClient.getRosterManager()获取到roster的manager对象。
```

#### 注册用户

L/S: 同步调用传入BMXUserProfile对象引用，调用之后即可获取profile信息。

```
   bmxClient.signUpNewUser("zhangsan", "sFo!slk1x", new BMXUserProfile());
```

H/A: 异步调用在BMXDataCallBack回调中返回profile实例。

```
   bmxClient.getUserManager().signUpNewUser("zhangsan", "sFo!slk1x", new BMXDataCallBack<BMXUserProfile>(){
        @Override
        public void onResult(BMXErrorCode bmxErrorCode, BMXUserProfile bmxUserProfile) {
           //返回profile
        }
   	});
```

#### 登录

两种登录模式：一种是普通手动登录，另一种是快速登录模式，手动登录包含了获取token和建立tcp连接的两个步骤，快速登录则将token缓存至本地。

L/S: 通过返回值BMXErrorCode判断是否成功。

```
	// 参数：username(用户名) password(密码)
   bmxClient.getUserService().signInByName("zhangsan", "sFo!slk1x");
   bmxClient.getUserService().fastSignInByName("zhangsan", "sFo!slk1x");
```

H/A: 在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

```
   bmxClient.getUserManager().signInByName("zhangsan", "sFo!slk1x", new BMXCallBack(){
   	      @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
   	});
   bmxClient.getUserManager().signInByName("zhangsan", "sFo!slk1x", new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
   	});
```

#### 获取会话列表

L/S: 通过传入BMXConversationList对象引用,调用成功后即可获取会话列表。

```
   BMXConversationList cl = bmxClient.getChatService().getAllConversations();
   for (int i=0; i<cl.size(); i++){
       BMXConversation c = cl.get(i);
       Log.e("conversation id:",""+c.conversationId());
   }
```

H/A: 在BMXDataCallBack回调中获取到会话列表。

```
   bmxClient.getChatManager().getAllConversations(new BMXDataCallBack<BMXConversationList>() {
       @Override
        public void onResult(BMXErrorCode bmxErrorCode, BMXConversationList list) {
          //返回BMXConversation实例
          for (int i=0; i<cl.size(); i++){
            BMXConversation c = cl.get(i);
            Log.e("conversation id:",""+c.conversationId());
          }
        }
   });
```

#### 断开连接

L/S: 通过返回值获取到BMXErrorCode判断是否成功。

```
bmxClient.getUserService().signOut();
```

H/A: 在BMXCallBack回调中根据BMXErrorCode判断。

```
   bmxClient.getUserManager().signOut(new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {
            //返回BMXErrorCode
          }
   	});
```

### 用户体系

* 添加好友

> L/S: 通过返回值获取到BMXErrorCode判断是否成功。 参数说明: rosterId reason(申请添加原因)

```
   bmxClient.getRosterService().apply(22342342, "Hi, I'm Lisi");
```

> H/A: 在BMXCallBack回调中获取到BMXErrorCode判断是否成功。

```
   bmxClient.getRosterManager().apply(22342342, "Hi, I'm Lisi", new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {
            //返回BMXErrorCode
          }
   	});
```

* 删除好友

> L/S: 通过返回值获取到BMXErrorCode判断是否成功。

```
   bmxClient.getRosterService().remove(22342342);
```

> H/A: 在BMXCallBack回调中获取到BMXErrorCode判断是否成功。

```
   bmxClient.getRosterManager().remove(22342342, new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {
            //返回BMXErrorCode
          }
   	});
```

* 同意添加好友

> L/S: 通过返回值获取到BMXErrorCode判断是否成功。

```
   //参数说明: rosterId
   bmxClient.getRosterService().accept(333453112);
```

> H/A: 在BMXCallBack回调中获取到BMXErrorCode判断是否成功。

```
   bmxClient.getRosterManager().accept(333453112, new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {
            //返回BMXErrorCode
          }
   	});
```

* 拒绝添加好友

> L/S: 通过返回值获取到BMXErrorCode判断是否成功。

```
   //参数说明: rosterId  reason(拒绝原因)

   bmxClient.getRosterService().decline(333453112,"I'm not Lisi");
```

> H/A: 在BMXCallBack回调中获取到BMXErrorCode判断是否成功。

```
   bmxClient.getRosterManager().decline(333453112,"I'm not Lisi", new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {
             //返回BMXErrorCode
          }
   	});
```

* 获取花名册

> L/S: 通过传入ListOfLongLong对象引用, 调用成功后可获取rosterId的列表。

```
   ListOfLongLong roster = new ListOfLongLong();
   bmxClient.getRosterService().get(roster, true);
   for (int i=0; i<roster.size(); i++){
       long roster_id = roster.get(i);
       Log.e("roster id:",""+roster_id);
   }
```

> H/A: 在BMXDataCallBack回调中获取rosterId列表。

```
   bmxClient.getRosterManager().get(roster, true, new BMXDataCallBack<ListOfLongLong>(){
         @Override
         public void onResult(BMXErrorCode bmxErrorCode, ListOfLongLong list) {
            //返回ListOfLongLong实例
            for (int i=0; i<list.size(); i++){
              long roster_id = list.get(i);
              Log.e("roster id:",""+roster_id);
            }
        }
   });
```

### 基础功能

#### 单聊

单聊是指一对一的聊天功能，单聊的 BMXConversationType 是 BMXConversationSingle，toId 是单聊对象的 userId。

#### 群聊

群聊是指附带角色和权限的用户集合内进行的内部广播方式的聊天功能， BMXConversationType 是 BMXConversationGroup，toId 是群组 Id。

#### 群组管理

* 创建群组

> L/S: 通过传入BMXGroup对象引用, 调用成功后可获取群信息。

```
    //参数说明: option(群配置信息)  group(群信息)

    BMXGroupService.CreateGroupOptions options = new BMXGroupService.CreateGroupOptions(name, desc, publicCheckStatus);
    options.setMMembers(members);

    BMXGroup group = new BMXGroup();
    bmxClient.getGroupService().create(options, group);
```

> H/A: 在BMXDataCallBack回调中获取群信息。

```
   bmxClient.getGroupManager().create(option, new BMXDataCallBack<BMXGroup>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode, BMXGroup group) {
            //返回BMXGroup实例
          }
   	});
```

* 加入群组

> L/S: 通过返回值获取到BMXErrorCode判断是否成功。

```
	//参数说明: group(群信息)  message(申请入群原因)
    bmxClient.getGroupService().join(group, message);
```

> H/A: 在BMXCallBack回调中获取到BMXErrorCode判断是否成功。

```
   bmxClient.getGroupManager().join(group, message, new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {
            //返回BMXErrorCode实例
          }
   	});
```

* 退出群组 参数说明: group(群信息)

> L/S: 通过返回值获取到BMXErrorCode判断是否成功。

```
   bmxClient.getGroupService().leave(group);
```

> H/A: 在BMXCallBack回调中获取到BMXErrorCode判断是否成功。

```
   bmxClient.getGroupManager().leave(group, new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {
            //返回BMXErrorCode实例
          }
   	});
```

* 解散群组

> L/S: 通过返回值获取到BMXErrorCode判断是否成功。

```
   //参数说明: group(群信息)
   bmxClient.getGroupService().destroy(group);
```

> H/A: 在BMXCallBack回调中获取到BMXErrorCode判断是否成功。

```
   bmxClient.getGroupManager().destroy(group, new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {
            //返回BMXErrorCode实例
          }
   	});
```

* 获取群成员列表

> L/S: 通过传入BMXGroupMemberList对象引用, 调用成功后可获取群成员列表信息。

```
    //参数说明: group(群信息) forceRefresh(是否从server获取)
    boolean forceRefresh = true;

    BMXGroupMemberList memberList = new BMXGroupMemberList();
    bmxClient.getGroupService().getMembers(group, memberList, forceRefresh);
```

> H/A: 在BMXDataCallBack回调中获取群成员列表信息。

```
   bmxClient.getGroupManager().getMembers(group, forceRefresh, new BMXDataCallBack<BMXGroupMemberList>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode, BMXGroupMemberList list) {
            //返回BMXGroupMemberList实例
          }
   	});
```

* 获取群组列表

> L/S: 通过传入BMXGroupList对象引用, 调用成功后可获取群列表信息。

```
   //参数说明: forceRefresh(是否从server获取)
   BMXGroupList list = new BMXGroupList();
   bmxClient.getGroupService().search(list, true);
```

> H/A: 在BMXDataCallBack回调中获取群列表信息。

```
    bmxClient.getGroupManager().getGroupList(true, new BMXDataCallBack<BMXGroupList>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode, BMXGroupList list) {
            //返回BMXGroupList实例
          }
    });
```

* 获取群组信息

> L/S: 通过传入BMXGroup对象引用, 调用成功后可获取群信息。

```
	//参数说明: groupId  forceRefresh(是否从server获取)
   BMXGroup bmxGroup = new BMXGroup();
   bmxClient.getGroupService().search(mGroupId, bmxGroup, true);
```

> H/A: 在BMXDataCallBack回调中获取群信息。

```
   bmxClient.getGroupManager().getGroupList(mGroupId, true, new BMXDataCallBack<BMXGroup>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode, BMXGroup group) {
            //返回BMXGroup实例
          }
   	});
```

### 消息发送

登录成功之后才能进行聊天操作。发消息时，单聊和群聊调用的是统一接口，区别只是要设置下 BMXConversationType

#### 消息的远程推送

开发者配置好远程推送的证书，且在代码中申请好权限，并将 deviceToken 传给蓝莺IM服务器，当接收者不在线的时候，蓝莺IM服务器会自动通过远程推送将消息发过去。

注： 推送的内容由发送消息接口的 pushContent 字段决定，内置消息发送的时候如果该字段没有值，将使用默认内容推送；自定义消息必须设置该字段，否则将不会推送。

* deviceToken传给蓝莺IM接口

> L/S: 通过返回值获取到BMXErrorCode判断是否成功。

```
    //参数说明: pushToken(推送token)
    bmxClient.getUserService().bindDevice(pushToken);
```

> H/A: 在BMXCallBack回调中获取到BMXErrorCode判断是否成功。

```
   bmxClient.getUserManager().bindDevice(pushToken, new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {
            //返回BMXErroeCode实例
          }
   	});
```

#### 消息内容格式

**文本消息**

```
//参数说明: from(发送者id)  to(接收者id)  type(单群聊类型)  text(文本内容)
BMXMessage msg = BMXMessage.createMessage(from, to, type, to, text);
```

**图片消息**

```
//参数说明: from(发送者id)  to(接收者id)  type(单群聊类型)  w(图片宽)   h(图片高)  path(图片本地路径)  size(图片大小)

BMXImageAttachment.Size size = new BMXMessageAttachment.Size(w, h);
BMXImageAttachment imageAttachment = new BMXImageAttachment(path, size);
BMXMessage msg = BMXMessage.createMessage(from, to, type, to, imageAttachment);
```

**文件消息**

参数说明: from(发送者id) to(接收者id) type(单群聊类型) path(文件本地路径) name(文件名称)

```
BMXFileAttachment fileAttachment = new BMXFileAttachment(path, name);
BMXMessage msg = BMXMessage.createMessage(from, to, type, to, fileAttachment);
```

**位置消息**

参数说明: from(发送者id) to(接收者id) type(单群聊类型) latitude(纬度) longitude(经度) address(地址)

```
BMXLocationAttachment locationAttachment = new BMXLocationAttachment(latitude, longitude, address);
BMXMessage msg = BMXMessage.createMessage(from, to, type, to, locationAttachment);
```

**语音消息**

参数说明: from(发送者id) to(接收者id) type(单群聊类型) path(语音本地路径) time(语音时长)

```
BMXVoiceAttachment voiceAttachment = new BMXVoiceAttachment(path, time);
BMXMessage msg = BMXMessage.createMessage(from, to, type, to, voiceAttachment);
```

#### 消息操作

* 发送

> L/S:

```
    //参数说明: BMXMessage(消息实体)
    bmxClient.getChatService().sendMessage(msg);
```

> H/A:

```
    //发送消息状态，需要注册消息接收监听
    bmxClient.getChatManager().sendMessage(msg);
```

* 转发

> L/S:

```
	//参数说明: BMXMessage(消息实体)
   bmxClient.getChatService().forwardMessage(msg);
```

> H/A:

```
    //发送消息状态，需要注册消息接收监听
	//参数说明: BMXMessage(消息实体)
    bmxClient.getChatManager().forwardMessage(msg);
```

* 重发

> L/S:

```
   //参数说明: BMXMessage(消息实体)
   bmxClient.getChatService().resendMessage(msg);
```

> H/A:

```
    //发送消息状态，需要注册消息接收监听
    bmxClient.getChatManager().resendMessage(msg);
```

* 撤回

> L/S:

```
	//参数说明: BMXMessage(消息实体)
    bmxClient.getChatService().recallMessage(msg);
```

> H/A:

```
    //发送消息状态，需要注册消息接收监听
    bmxClient.getChatManager().recallMessage(msg);
```

* 下载消息附件

调用说明: 在FileCallBack中传入下载url,onProgress获取下载进度,onFail返回下载失败,onFinish返回成功的路径。

```
    bmxClient.getChatManager().downloadAttachment(message, new FileCallback(body.url()) {
        @Override
        protected void onProgress(long percent, String path, boolean isThumbnail) {
        }

        @Override
        protected void onFinish(String url, boolean isThumbnail) {
            BMImageLoader.getInstance().display(mImageView, "file://" + body.path(), mImageConfig);
        }

        @Override
        protected void onFail(String path, boolean isThumbnail) {
        }
    });
```

### 消息接收监听

* 注册消息回调

```
private BMXChatServiceListener mChatListener = new BMXChatServiceListener() {

    @Override
    public void onStatusChanged(BMXMessage msg, BMXErrorCode error) {
    //消息状态更新
    }

    @Override
    public void onAttachmentStatusChanged(BMXMessage msg, BMXErrorCode error, int percent) {
    //附件状态更新
    }

    @Override
    public void onRecallStatusChanged(BMXMessage msg, BMXErrorCode error) {
    //撤回状态更新
    }

    @Override
    public void onReceive(BMXMessageList list) {
    //收到消息
    }

    @Override
    public void onReceiveSystemMessages(BMXMessageList list) {
    //收到系统通知
    }

    @Override
    public void onReceiveReadAcks(BMXMessageList list) {
    //收到已读回执
    }

    @Override
    public void onReceiveDeliverAcks(BMXMessageList list) {
    //收到消息到达回执
    }

    @Override
    public void onReceiveRecallMessages(BMXMessageList list) {
    //收到撤回消息通知
    }

    @Override
    public void onAttachmentUploadProgressChanged(BMXMessage msg, int percent) {
    //附件上传进度更新
    }

};
```

### 功能进阶

BMXMessageObject实体中，提供可扩展属性(extensionJson 和 configJson) extensionJson 为开发使用的扩展字段，例如编辑状态。 configJson 为SDK自用的扩展字段，例如mention功能，push功能

*   群组@功能

    群组中支持 @ 功能，满足您 @ 指定用户或 @所有人的需求，开发者在BMXMessage中通过设置config字段来实现群主@功能，已经@成员后的会下发推送通知

```
    // 文本功能添加@对象
    if (atMap != null && !atMap.isEmpty()) {
        MentionBean mentionBean = new MentionBean();
        mentionBean.setSenderNickname(senderName);
        mentionBean.setPushMessage(pushText);
        // @对象的存储信息 包括全部成员或者部分成员
        if (atMap.containsKey("-1")) {
            // @全部
            String atTitle = atMap.get("-1");
            if (!TextUtils.isEmpty(atTitle) && text.contains(atTitle)) {
                // 如果包含全部直接走全部 还需要判断文本消息是否包含完成的@名称 如果没有就不触发@
                mentionBean.setMentionAll(true);
            }
        } else {
            // @部分成员 需要遍历添加@信息
            List<Long> atIds = new ArrayList<>();
            mentionBean.setMentionAll(false);
            for (Map.Entry<String, String> entry : atMap.entrySet()) {
                // 发送文字包含@对象的名称时再加入 防止输入框@对象名称被修改
                if (entry.getValue() != null && !TextUtils.isEmpty(entry.getValue())
                    && text.contains(entry.getValue())) {
                    // @部分成员 feed信息只需要feedId和userId 所以需要去除无用的信息
                    atIds.add(Long.valueOf(entry.getKey()));
                    }
                }
            mentionBean.setMentionList(atIds);
        }
        msg.setConfig(new Gson().toJson(mentionBean));
    }
```

* 消息正在输入状态

```
    String INPUT_STATUS = "input_status";

    interface InputStatus {
        // 空
        String NOTHING_STATUS = "nothing";

        // 键盘弹起
        String TYING_STATUS = "typing";
    }

    String extension = "";
    try {
        JSONObject object = new JSONObject();
        object.put(INPUT_STATUS,
            tag == MessageInputBar.OnInputPanelListener.TAG_OPEN
                    ? InputStatus.TYING_STATUS
                    : InputStatus.NOTHING_STATUS);
        extension = object.toString();
    } catch (JSONException e) {
        e.printStackTrace();
    }

    BMXMessage msg = BMXMessage.createMessage(from, to, type, to, "");
    if (msg == null) {
        return null;
    }
    msg.setDeliveryQos(BMXMessage.DeliveryQos.AtMostOnce);
    msg.setExtension(extension);
```

## RTC 音视频通话
蓝莺 IM 系统的RTC通话功能，需要客户端集成floo-android和floo-rtc-android两个SDK。floo-android为音视频通话提供了信令通道，floo-rtc-android实现了RTC通话相关的业务逻辑。所以，实现音视频通话的前提是已经集成了floo-android，并实现了登录和收发消息功能。

蓝莺 IM RTC SDK 目前实现了一对一的视频和语音通话功能。下载地址为：https://github.com/maxim-top/floo-rtc-android/releases。

* 下载aar文件到项目的libs目录
* 在build.gradle文件dependencies块中增加依赖，参照[lanying-im-android源码](https://github.com/maxim-top/lanying-im-android/blob/master/app/build.gradle#L94)使用最新版。新版的gradle只要声明了对libs目录的依赖，无须再单独声明对其中aar文件的依赖。


### 创建用户界面
1. 导入视频画面类依赖
```
import top.maxim.rtc.view.BMXRtcRenderView;
import top.maxim.rtc.view.RTCRenderView;
```

2. 在通话界面创建两个画面的容器布局（本例中为大画面全屏，小画面居右上）
```
    <FrameLayout
        android:id="@+id/video_view_container_large"
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:background="@color/color_black" />

    <FrameLayout
        android:id="@+id/video_view_container_small"
        android:layout_width="120dp"
        android:layout_height="212dp"
        android:background="@color/color_black"
        android:layout_gravity="right"
        android:visibility="gone" />

```

3. 添加本地画面到小画面容器布局
```
        ViewGroup smallViewGroup = mVideoContainer.findViewById(R.id.video_view_container_small);
        //呼叫过程中，对方画面为空，则将本地画面全屏
        if (mRemoteView == null){
            ViewGroup.LayoutParams layoutParams = smallViewGroup.getLayoutParams();
            layoutParams.width = ViewGroup.LayoutParams.MATCH_PARENT;
            layoutParams.height = ViewGroup.LayoutParams.MATCH_PARENT;
            smallViewGroup.setLayoutParams(layoutParams);
        }
        smallViewGroup.setVisibility(View.VISIBLE);
        mLocalView = new RTCRenderView(this);
        mLocalView.init();
        mLocalView.setScalingType(BMXRtcRenderView.ScalingType.SCALE_ASPECT_FILL);
        mLocalView.getSurfaceView().setZOrderMediaOverlay(true);
        RelativeLayout.LayoutParams layoutParams = new RelativeLayout.LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        layoutParams.addRule(RelativeLayout.CENTER_VERTICAL);
        smallViewGroup.addView(mLocalView, layoutParams);
```
4. 添加对方画面到大画面容器布局
```
        //将原本全屏的本地画面还原为小尺寸
        if (mLocalView != null){
            ViewGroup smallViewGroup = mVideoContainer.findViewById(R.id.video_view_container_small);
            ViewGroup.LayoutParams layoutParams = smallViewGroup.getLayoutParams();
            layoutParams.width = getPixelsFromDp(120);
            layoutParams.height = getPixelsFromDp(212);
            smallViewGroup.setLayoutParams(layoutParams);
            mLocalView.setScalingType(BMXRtcRenderView.ScalingType.SCALE_ASPECT_FILL);
        }

        ViewGroup largeViewGroup = mVideoContainer.findViewById(R.id.video_view_container_large);
        largeViewGroup.setVisibility(View.VISIBLE);
        mRemoteView = new RTCRenderView(this);
        mRemoteView.init();
        mRemoteView.setScalingType(BMXRtcRenderView.ScalingType.SCALE_ASPECT_FILL);

        FrameLayout.LayoutParams layoutParams = new FrameLayout.LayoutParams(ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        layoutParams.gravity = Gravity.CENTER;
        largeViewGroup.addView(mRemoteView, layoutParams);

```

### 音视频通话业务逻辑
1. 导入RTCManager

```
import top.maxim.rtc.RTCManager;
```

2. 添加事件监听

```
mEngine = RTCManager.getInstance().getRTCEngine();
mEngine.addRTCEngineListener(mListener = new BMXRTCEngineListener() {

    @Override
    public void onJoinRoom(String info, long roomId, BMXErrorCode error) {
        super.onJoinRoom(info, roomId, error);
        mRoomId = roomId;
        if (BaseManager.bmxFinish(error)) {
            mEngine.publish(BMXVideoMediaType.Camera, mHasVideo, true);
            Log.e(TAG, "加入房间成功 开启发布本地流, roomId= " + roomId + "msg = " + info);
        } else {
            Log.e(TAG, "加入房间失败 roomId= " + roomId + "msg = " + info);
        }
    }

    @Override
    public void onLeaveRoom(String info, long roomId, BMXErrorCode error, String reason) {
        super.onLeaveRoom(info, roomId, error, reason);
        if (BaseManager.bmxFinish(error)) {
            Log.e(TAG, "离开房间成功 roomId= " + roomId + "msg = " + reason);
        }else{
            Log.e(TAG, "离开房间失败 roomId= " + roomId + "msg = " + reason);
        }
    }

    @Override
    public void onMemberJoined(long roomId, long usedId) {
        super.onMemberJoined(roomId, usedId);
        Log.e(TAG, "远端用户加入 uid= " + usedId);
    }

    @Override
    public void onMemberExited(long roomId, long usedId, String reason) {
        super.onMemberExited(roomId, usedId, reason);
        Log.e(TAG, "远端用户离开 uid= " + usedId);
        //回收界面
        onRemoteLeave();
    }

    @Override
    public void onLocalPublish(BMXStream stream, String info, BMXErrorCode error) {
        super.onLocalPublish(stream, info, error);
        if (BaseManager.bmxFinish(error)) {
            //打开本地视频画面，发送呼叫消息
            onUserJoin(stream);
            Log.e(TAG, "发布本地流成功 开启预览 msg = " + info);
        }else{
            Log.e(TAG, "发布本地流失败 msg = " + info);
        }
    }

    @Override
    public void onLocalUnPublish(BMXStream stream, String info, BMXErrorCode error) {
        super.onLocalUnPublish(stream, info, error);
        if (BaseManager.bmxFinish(error)) {
            Log.e(TAG, "停止发布本地流成功 msg = " + info);
        }else{
            Log.e(TAG, "停止发布本地流失败 msg = " + info);
        }
    }

    @Override
    public void onRemotePublish(BMXStream stream, String info, BMXErrorCode error) {
        super.onRemotePublish(stream, info, error);
        if (BaseManager.bmxFinish(error)) {
            mEngine.subscribe(stream);
            Log.e(TAG, "远端发布流 开启订阅");
        }else{
            Log.e(TAG, "远端发布流失败 msg = " + info);
        }
    }

    @Override
    public void onRemoteUnPublish(BMXStream stream, String info, BMXErrorCode error) {
        super.onRemoteUnPublish(stream, info, error);
        if (BaseManager.bmxFinish(error)) {
            Log.e(TAG, "远端取消发布流");
            BMXVideoCanvas canvas = new BMXVideoCanvas();
            canvas.setMStream(stream);
            mEngine.stopRemoteView(canvas);
            //停止订阅
            mEngine.unSubscribe(stream);
            //回收界面
            onRemoteLeave();
        }else{
            Log.e(TAG, "远端取消发布流失败 msg = " + info);
        }
    }

    @Override
    public void onSubscribe(BMXStream stream, String info, BMXErrorCode error) {
        super.onSubscribe(stream, info, error);
        if (BaseManager.bmxFinish(error)) {
            //展示对方视频画面
            onRemoteJoin(stream);
            mPickupTimestamp = getTimeStamp();
            Log.e(TAG, "订阅远端流成功 msg = " + info);
        } else {
            Log.e(TAG, "订阅远端流失败 msg = " + info);
        }
    }

    @Override
    public void onUnSubscribe(BMXStream stream, String info, BMXErrorCode error) {
        super.onUnSubscribe(stream, info, error);
        if (BaseManager.bmxFinish(error)) {
            Log.e(TAG, "取消订阅远端流成功, 开启预览 msg = " + info);
        } else {
            Log.e(TAG, "取消订阅远端流失败 msg = " + info);
        }
    }
});
```

3. 加入房间

```
    //设置视频分辨率
    BMXVideoConfig config = new BMXVideoConfig();
    config.setProfile(EngineConfig.VIDEO_PROFILE);
    mEngine.setVideoProfile(config);

    //设置用户ID、pin密码和房间ID
    BMXRoomAuth auth = new BMXRoomAuth();
    auth.setMUserId(mUserId);
    auth.setMRoomId(mRoomId);//主叫方无须设置roomId，房间创建成功事件会返回系统分配的roomId；被叫方需要设置与主叫方一样的roomId
    auth.setMToken(mPin);//房间pin密码，建议随机生成高强度密码
    mEngine.joinRoom(auth);
```

4. 挂断通话

```
    public void onCallHangup(View view){
        //发送挂断消息
        sendRTCHangupMessage();
        leaveRoom();
        finish();
    }
```

5. 回收界面

```
    private void onRemoteLeave() {
        removeRemoteView();
        mHandler.removeAll();
        finish();
    }
```

6. 打开本地画面，发送呼叫消息

```
    private void onUserJoin(BMXStream info){
        if(info == null){
            return;
        }
        if (mHasVideo) {
            runOnUiThread(() -> {
                addLocalView();
                BMXVideoCanvas canvas = new BMXVideoCanvas();
                canvas.setMView(mLocalView.getObtainView());
                canvas.setMStream(info);
                mEngine.startPreview(canvas);
            });
        } else {

        }
        if (mIsInitiator) {
            //用户加入放入房间 发送给对方信息
            sendRTCCallMessage();
        }
    }
```

7. 打开对方画面

```
    private void onRemoteJoin(BMXStream info) {
        if(info == null){
            return;
        }
        runOnUiThread(() -> {
            if (mHasVideo) {
                addRemoteView();
                BMXVideoCanvas canvas = new BMXVideoCanvas();
                canvas.setMView(mRemoteView.getObtainView());
                canvas.setMUserId(info.getMUserId());
                canvas.setMStream(info);
                mEngine.startRemoteView(canvas);
            }
        });
    }
```

8. 通话结束时回收资源

```
    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (mEngine != null) {
            mEngine.removeRTCEngineListener(mListener);
            mListener = null;
        }
        RTCManager.getInstance().removeRTCServiceListener(mRTCListener);
        mRTCListener = null;
    }
```

### 使用rtcService实现音视频通话信令

1. 添加事件监听

private BMXRTCServiceListener mRTCListener = new BMXRTCServiceListener(){

    public void onRTCCallMessageReceive(BMXMessage msg) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    //暂停以处理稍后收到的对应通话的挂断消息（mHungupCalls），
                    // 这样可以避免弹出已结束的通话
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    throw new RuntimeException(e);
                }
                String callId = msg.config().getRTCCallId();
                if (mHungupCalls.contains(callId)){
                    mHungupCalls.remove(callId);
                    ackMessage(msg);
                    return;
                }
                long roomId = msg.config().getRTCRoomId();
                long chatId = msg.config().getRTCInitiator();
                long myId = SharePreferenceUtils.getInstance().getUserId();
                if (myId == chatId){
                    return;
                }
                //如果已在通话中，则发送忙线消息给对方
                if (RTCManager.getInstance().getRTCEngine().isOnCall){
                    replyBusy(callId, myId, chatId);
                    return;
                }
                String pin = msg.config().getRTCPin();
                if(mActivityRef != null && mActivityRef.get() != null){
                    Context context = mActivityRef.get();
                    if (msg.type() == BMXMessage.MessageType.Single) {
                        //打开通话界面（呼入中）
                        SingleVideoCallActivity.openVideoCall(context, chatId, roomId, callId,
                                false, msg.config().getRTCCallType(), pin, msg.msgId());
                    }
                }
            }
        }, "onRTCCallMessageReceive").start();
    }

    public void onRTCPickupMessageReceive(BMXMessage msg) {
        if (msg.config().getRTCCallId().equals(mCallId) && msg.fromId() == mUserId){
            leaveRoom();
            ackMessage(msg);
        }
    }

    public void onRTCHangupMessageReceive(BMXMessage msg) {
        long otherId = mEngine.otherId;
        if (msg.config().getRTCCallId().equals(mCallId) &&
                (msg.fromId()==otherId
                || msg.content().equals("busy")
                || msg.content().equals("rejected")
                || msg.content().equals("canceled")
                || msg.content().equals("timeout")
                || !mEngine.isOnCall)){
            leaveRoom();
            ackMessage(msg);
        }
    }

};
RTCManager.getInstance().addRTCServiceListener(mRTCListener);


2. 发送呼叫消息

```
public String sendRTCCallMessage(BMXMessageConfig.RTCCallType type, long roomId, long from, long to,
                                    String pin) {
    BMXMessageConfig con = BMXMessageConfig.createMessageConfig(false);
    con.setRTCCallInfo(type, roomId, from, BMXMessageConfig.RTCRoomType.Broadcast, pin);
    con.setIOSConfig("{\"mutable_content\":true,\"loc-key\":\"call_in\"}");
    BMXMessage msg = BMXMessage.createRTCMessage(from, to, BMXMessage.MessageType.Single, to, "");
    msg.setConfig(con);
    msg.setExtension("{\"rtc\":\"call\"}");
    handlerMessage(msg);
    return con.getRTCCallId();
}
```

3. 发送接听消息

```
public void sendRTCPickupMessage(long from, long to, String callId) {
    BMXMessageConfig con = BMXMessageConfig.createMessageConfig(false);
    con.setRTCPickupInfo(callId);
    BMXMessage msg = BMXMessage.createRTCMessage(from, to, BMXMessage.MessageType.Single, to, "");
    msg.setConfig(con);
    handlerMessage(msg);
}
```

4. 发送挂断消息

```
public void sendRTCHangupMessage(long from, long to, String callId, String content, String iosConfig) {
    BMXMessageConfig con = BMXMessageConfig.createMessageConfig(false);
    con.setRTCHangupInfo(callId);
    BMXMessage msg = BMXMessage.createRTCMessage(from, to, BMXMessage.MessageType.Single, to, content);
    msg.setConfig(con);
    handlerMessage(msg);
}
```
