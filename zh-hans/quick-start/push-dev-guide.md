---
description: 推送开发指南（PUSH） 推送 SDK 集成说明 SDK 架构 快速集成 高级调用形式 高级接口 设置监听 厂商推送集成
keywords: 推送开发, PUSH, AI智能体, AI开源
---
# 推送开发指南（PUSH）

注：如果您是IM开发者，请直接参照[IM开发文档](floo-android-quick-start.md)中的Push推送部分。

本页面供快速集成使用，了解更多请访问[详细文档](../reference/floo-android.md)

### 推送 SDK 集成说明

蓝莺推送是基于蓝莺IM技术基础上研发，只需要一次集成，就可以同时拥有推送和IM两大服务，提高研发效率的同时，也会极大降低企业的 IT 支出。

使用蓝莺推送没有额外费用。

由于默认即支持各主流厂商通道，为了进一步减低集成难度，蓝莺推送实现时也内置了证书设置与更新机制。简单来说，就是开发者集成蓝莺推送之后，只需要在控制台设置好各厂商推送的证书，前端将厂商推送 SDK 打包，即可自动完成系统厂商的适配。不再需要针对性调整各种推送令牌的申请和设置。

注意：与其他推送厂商不同的是，蓝莺推送 SDK 专注于推送通道的建设和服务，并不会收集终端信息，如果你有类似广告业务，需要单独集成广告 SDK，或者将业务数据标签通过接口设置后才能使用。

如前所述，由于蓝莺推送 SDK 与 IM SDK 是同一个 SDK，推送功能只是在原有 IM SDK 基础上增加了推送接口。因此集成方式均与 IM SDK 相同，快速集成文档亦可参见蓝莺IM安卓端快速集成，蓝莺IM iOS 端快速集成。

### SDK 架构

推送功主要涉及以下三个类：

```
BMXClient
|----BMXPushService
    |----BMXPushServiceListener
    |----BMXPushManager
```

其中 BMXPushService、BMXPushManager 均为推送设置类，前者是同步调用类，后者异步调用类，实现时根据需要在两者中二选一即可。

其他功能类分别是：

* BMXCallBack : 无类型接口回调
* BMXDataCallBack : 泛型类型带数据回调
* BMXPushServiceListener : 推送事件监听
* BMXMessage : 推送消息
* BMXUserProfile : 推送用户信息

下文以安卓 SDK 为例介绍推送 API。

### 快速集成

**第一步 导入SDK**

SDK导入可以选择aar格式或者jar+so格式

#### aar格式

* [下载aar文件](https://github.com/maxim-top/floo-android/releases)到项目的libs目录
* 在build.gradle文件dependencies块中增加：implementation(name:'floo-android\_3.1.3.aar',ext:'aar')

#### jar+so格式

* 下载jar包和so库到项目的libs目录
* 在build.gradle文件中增加：implementation fileTree(dir: 'libs', include: \['\*.jar'])

**第二步 项目配置**
> 权限配置

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

> 在app入口类中导入so库文件：

```
    static {
        System.loadLibrary("floo");
    }
```

**第三步 初始化BMXClient**

```
    public static void initClient(int index) {
        if (bmxClient != null){
            return;
        }
        String appPath = AppContextUtils.getAppContext().getFilesDir().getPath();
        File dataPath = new File(appPath + "/data_dir");
        File cachePath = new File(appPath + "/cache_dir");
        dataPath.mkdirs();
        cachePath.mkdirs();

        String pushId = getPushId();//设置推送平台对应的ID
        BMXSDKConfig conf = new BMXSDKConfig(BMXClientType.Android, "1", dataPath.getAbsolutePath(),
                cachePath.getAbsolutePath(), TextUtils.isEmpty(pushId) ? "MaxIM" : pushId);
        conf.setConsoleOutput(true);
        conf.setLogLevel(BMXLogLevel.Debug);
        //设置推送appId
        conf.setAppID("appId");
        //设置推送secret
        conf.setAppSecret("appSecret");
        //设置设备的唯一设备id
        conf.setDeviceUuid(deviceId);
        //设置生产环境
        conf.setEnvironmentType(BMXPushEnvironmentType.Production);
        //根据设备机型设置pushProviderType
        conf.setPushProviderType(getProviderType(context));
        //获取BMXClient实例
        BMXClient bmxClient = BMXClient.create(conf);
    }


    //根据机型获取type
    private static BMXPushProviderType getProvideType(Context context){
        if (isHuawei(context)) {
            return BMXPushProviderType.HuaWei;
        }
        if (isXiaomi(context)) {
            return BMXPushProviderType.XiaoMi;
        }
        if (isMeizu(context)) {
            return BMXPushProviderType.MeiZu;
        }
        if (isOppo(context)) {
            return BMXPushProviderType.OPPS;
        }
        if (isVivo(context)) {
            return BMXPushProviderType.VIVO;
        }
        return BMXPushProviderType.Unknown;
    }
```

### 高级调用形式

* BMXPushManager: 通过bmxClient.getPushManager()获取到推送的manager对象。

#### 开启推送

参数说明: alias(push别名), bmxToken(推送token) callBack

```
     如果不传入alias  SDK会自动生成
     如果不传入token  SDK会自动生成并通过BMXPushServiceListener回调
```

```
同步调用形式
   调用说明: 通过返回值BMXErrorCode判断是否成功。

   bmxClient.getPushService().start();//不传入参数
   bmxClient.getPushService().start("zhangsan");//传入alias
   bmxClient.getPushService().start("zhangsan", token);//传入alias  token
异步调用形式
   调用说明: 通过bmxClient.getPushManager()获取manager对象,在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   //不传入参数
   bmxClient.getPushManager().start(new BMXCallBack<>(){
        @Override
        public void onResult(BMXErrorCode bmxErrorCode) {

        }
   	});
   //传入alias
   bmxClient.getPushManager().start("zhangsan",new BMXCallBack<>(){
        @Override
        public void onResult(BMXErrorCode bmxErrorCode) {

        }
    });
   //传入alias token
   bmxClient.getPushManager().start("zhangsan", token, new BMXCallBack<>(){
        @Override
        public void onResult(BMXErrorCode bmxErrorCode) {

        }
    });
```

#### 停止推送

参数说明: callBack

```
同步调用
   调用说明: 通过返回值BMXErrorCode判断是否成功。

   bmxClient.getPushService().stop();
异步调用
   调用说明: 通过bmxClient.getPushManager()获取manager对象,在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   bmxClient.getPushManager().stop(new BMXCallBack(){
   	      @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
   	});
```

#### 唤起推送

```
同步调用
   调用说明: 通过返回值BMXErrorCode判断是否成功。

   bmxClient.getPushService().resume();

异步调用
   调用说明: 通过bmxClient.getPushManager()获取manager兑现, 在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   bmxClient.getPushManager().remuse(new BMXCallBack<>() {
       @Override
        public void onResult(BMXErrorCode bmxErrorCode) {
        }
   });
```

#### 获取推送的状态

返回值说明: public static enum PushSdkStatus { Starting(1), Started, Stoped, Offline; }

```
同步调用:

   BMXPushService.PushSdkStatus status = bmxClient.getPushService().status();

异步调用:

   BMXPushService.PushSdkStatus status = bmxClient.getPushManager().status();
```

#### 解绑别名

参数说明: alias(push别名)

```
同步调用
   调用说明: 通过返回值BMXErrorCode判断是否成功。

   bmxClient.getPushService().unbindAlias(alias);
异步调用
   调用说明: 通过bmxClient.getPushManager()获取manager对象,在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   bmxClient.getPushManager().unbindAlias(alias, new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### 获取token

```
   需要在start成功之后调用才有值

同步调用:

   String token = bmxClient.getPushService().getToken();

异步调用:

   String token = bmxClient.getPushManager().getToken();
```

#### 获取cert

```
   需要在start成功之后调用才有值,  同时需要在对应厂商注册证书并且设置对应的provideType才可获取到
   目前支持   华为  小米  魅族  oppo  vivo

同步调用:

   String cert = bmxClient.getPushService().getCert();

异步调用:

   String cert = bmxClient.getPushManager().getCert();
```

#### 绑定厂商token

参数说明: token(注册厂商推送返回的token)

```
同步调用
   调用说明: 通过返回值BMXErrorCode判断是否成功。

   bmxClient.getPushService().bindDeviceToken(token);
异步调用
   调用说明: 通过bmxClient.getPushManager()获取manager对象,在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   bmxClient.getPushManager().bindDeviceToken(token, new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### 获取推送用户信息

参数说明: forceRefresh(是否从server拉取)

```
同步调用
   调用说明: 通过传入BMXPushUserProfile对象引用, 调用成功后可获取推送用户信息。

   BMXPushUserProfile profile = new BMXPushUserProfile();
   bmxClient.getPushService().getPushProfile(profile, forceRefresh);
异步调用
   调用说明: 通过bmxClient.getPushManager()获取到manager对象, 在BMXDataCallBack<BMXPushUserProfile>回调中获取推送用户信息。

   bmxClient.getPushManager().getPushProfile(forceRefresh, new BMXDataCallBack<BMXPushUserProfile>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode, BMXPushUserProfile profile) {
            //返回BMXPushUserProfile实例
          }
    });
```

### 高级接口

#### 设置推送标签（tag）

参数说明: tags(tag列表) operationId(此次操作的唯一id 手动生成唯一标识)

```
    TagList tags = new TagList();
    tags.add("tag内容");

同步调用
   调用说明: 通过返回值BMXErrorCode判断是否成功。

   bmxClient.getPushService().setTags(tags, operationId);
异步调用
   调用说明: 通过bmxClient.getPushManager()获取manager对象,在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   bmxClient.getPushManager().setTags(tags, operationId, new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### 获取推送标签（tag）列表

参数说明: operationId(此次操作的唯一id 手动生成唯一标识)

调用说明: 通过传入TagList对象引用, 调用成功后可获取tag列表信息。

```
同步调用

   TagList tags = new TagList();
   bmxClient.getPushService().getTags(tags, operationId);

异步调用
   调用说明: 通过bmxClient.getPushManager()获取到manager对象, 在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   TagList tags = new TagList();
   bmxClient.getPushManager().getTags(tags, operationId, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### 删除推送标签（tag）

参数说明: operationId(此次操作的唯一id 手动生成唯一标识)

```
    TagList tags = new TagList();
    tags.add("tag内容");

同步调用

   bmxClient.getPushService().deleteTags(tags, operationId);

异步调用
   调用说明: 通过bmxClient.getPushManager()获取到manager对象, 在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   bmxClient.getPushManager().deleteTags(tags, operationId, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### 清除所有标签（tag）

参数说明: operationId(此次操作的唯一id 手动生成唯一标识)

```
同步调用

   bmxClient.getPushService().clearTags(operationId);

异步调用
   调用说明: 通过bmxClient.getPushManager()获取到manager对象, 在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   bmxClient.getPushManager().clearTags(operationId, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### 设置推送开关

参数说明: enable(boolean 推送开关)

```
同步调用

   bmxClient.getPushService().setPushMode(enable);

异步调用
   调用说明: 通过bmxClient.getPushManager()获取到manager对象, 在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   bmxClient.getPushManager().setPushMode(enable, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### 设置推送时间

参数说明: startHour(推送开启时间) endHour(推送结束时间) 24小时制 设置每天的推送时间区间

```
同步调用

   bmxClient.getPushService().setPushTime(startHour, endHour);

异步调用
   调用说明: 通过bmxClient.getPushManager()获取到manager对象, 在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   bmxClient.getPushManager().setPushTime(startHour, endHour, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### 设置推送静默时间

参数说明: startHour(推送开启时间) endHour(推送结束时间) 24小时制 设置每天的不推送时间区间

```
同步调用

   bmxClient.getPushService().setSilenceTime(startHour, endHour);

异步调用
   调用说明: 通过bmxClient.getPushManager()获取到manager对象, 在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   bmxClient.getPushManager().setSilenceTime(startHour, endHour, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### 发送推送消息

参数说明: content(推送内容)

```
同步调用

   bmxClient.getPushService().sendMessage(content);

异步调用

   bmxClient.getPushManager().sendMessage(content);
```

#### 获取推送的消息列表

参数说明: refMsgId(起始消息id 第一次传0) size(获取的消息数量)

```
同步调用
   调用说明: 通过传入BMXMessageList对象引用, 调用成功后可获取推送消息列表。

   BMXMessageList messageList = new BMXMessageList();
   bmxClient.getPushService().loadLocalPushMessages(refMsgId, size, messageList);
异步调用
   调用说明: 通过bmxClient.getPushManager()获取到manager对象, 在BMXCallBack回调中返回BMXErrorCode 判断是否成功。

   BMXMessageList messageList = new BMXMessageList();
   bmxClient.getPushManager().loadLocalPushMessages(refMsgId, size, messageList, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {
          }
    });
```

### 设置监听

* 注册推送回调

```
同步调用:
   bmxClient.getPushService().addPushListener(mListener);

异步调用:
   bmxClient.getPushManager().addPushListener(mListener);
```

* 移除推送回调

```
同步调用:
   bmxClient.getPushService().removePushListener(mListener);

异步调用:
   bmxClient.getPushManager().removePushListener(mListener);
```

* 回调示例

```
    private BMXPushServiceListener mListener = new BMXPushServiceListener() {

        @Override
        public void onPushStart(String bmxToken) {
            super.onPushStart(bmxToken);
            //推送开启返回token
            Log.d(TAG, "onPushStart" + bmxToken);
        }

        @Override
        public void onPushStop() {
            super.onPushStop();
            Log.d(TAG, "onPushStop");
        }

        @Override
        public void onGetTags(String operationId) {
            super.onGetTags(operationId);
            Log.d(TAG, "onGetTags" + operationId);
        }

        @Override
        public void onSetTags(String operationId) {
            super.onSetTags(operationId);
            Log.d(TAG, "onSetTags" + operationId);
        }

        @Override
        public void onDeleteTags(String operationId) {
            super.onDeleteTags(operationId);
            Log.d(TAG, "onDeleteTags" + operationId);
        }

        @Override
        public void onClearTags(String operationId) {
            super.onClearTags(operationId);
            Log.d(TAG, "onClearTags" + operationId);
        }

        @Override
        public void onStatusChanged(BMXMessage msg, BMXErrorCode error) {
            super.onStatusChanged(msg, error);
            Log.d(TAG, "onStatusChanged" + msg.content());
        }

        @Override
        public void onReceivePush(BMXMessageList list) {
            super.onReceivePush(list);
            Log.d(TAG, "onReceivePush");
        }

        @Override
        public void onCertRetrieved(String cert) {
            super.onCertRetrieved(cert);
            Log.d(TAG, "onCertRetrieved" + cert);
            //返回厂商注册的证书   获取到证书之后可以对厂商的push通道进行注册
        }
    };
```

### 厂商推送集成

各平台集成只需要按照平台推送文档将集成SDK放入应用中, 对应的配置按照平台要求配置即可（华为除外）。

#### 华为

需要按照华为推送平台设置 [华为推送](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/android-app-quickstart-0000001071490422)

1. project级别的build.gradle文件增加

```
repositories {
    google()
    jcenter()
    maven {
        url 'https://developer.huawei.com/repo/'
    }
}

allprojects {
    repositories {
        google()
        jcenter()
        maven {
            url 'https://developer.huawei.com/repo/'
        }
    }
}
```

1. app级别build.gradle

```
apply plugin: 'com.huawei.agconnect'
dependencies{
    implementation "com.huawei.hms:push:5.0.4.302"
}
```

1. 最后从推送平台下载 agconnect-services.json，放入app目录下。

#### 小米

按照小米推送平台集成 [小米推送](https://dev.mi.com/console/doc/detail?pId=230)

#### Oppo

按照OPPO推送平台集成 [oppo推送](https://open.oppomobile.com/wiki/doc#id=10195)

#### 魅族

按照魅族推送平台集合 [魅族推送](http://open-wiki.flyme.cn/doc-wiki/index)

#### 谷歌推送（FCM）

Google推送指南 [FCM](https://firebase.google.cn/docs/cloud-messaging/android/client?hl=zh-cn)
