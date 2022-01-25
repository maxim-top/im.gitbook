# Push Push SDK Quick integration指南

This page is for quick integration, visit[detailed documentation](https://maximtop.com/docs/android)

### Push SDK integration description

Maximtop Push is developed based on Maximtop IM technology, which can have both push and IM services with only one integration, improving R&D efficiency and greatly reducing IT expenditure of enterprises.

使用Maximtop Push没有额外费用。

Since the channels of major vendors are supported by default, in order to further reduce the difficulty of integration, certificate settings and updating mechanism are also built into the implementation of Maximtop Push. Simply put, after Maximtop Push integrated, developer only needs to set the certificates pushed by each vendor on the console, and the front end will package the vendor push SDKs, which can automatically complete the adaptation of the system vendor. It is no longer necessary to adjust the application and settings of various push tokens.

Note: Unlike other push vendors, Maximtop Push SDK focuses on the construction and serving of push channels, and does not collect terminal information. If you have similar advertising business, you need to integrate the advertising SDK separately, or set business data tags through the interface before you can use it.

As mentioned earlier, since Maximtop Push SDK and IM SDK are the same SDK, the push function only adds a push interface to the original IM SDK. Therefore, the integration method is the same as that of IM SDK, and the quick integration document can also be found inMaximtop IM for Android Quick Integration，Maximtop IM for iOS Quick Integration。

### SDK architecture

Push function mainly involves the following three classes:

```
BMXClient
|----BMXPushService
    |----BMXPushServiceListener
    |----BMXPushManager
```

Where BMXPushService and BMXPushManager are both push setting classes, the former is a synchronous calling class, and the latter is an asynchronous calling class. You can choose one according to needs when implementing.

Other functional classes are:

* BMXCallBack : Untyped interface callback
* BMXDataCallBack : Generic type with data callback
* BMXPushServiceListener : Push event listening
* BMXMessage : Push message
* BMXUserProfile : Push user message

Android SDK is used as an example for push API below.

### Import SDK into Android Studio

Aar or jar + so formats are selectable in SDK import

#### aar format

* [Download aar file](https://github.com/maxim-top/floo-android/releases)to /lib in project
* Add implementation(name:'floo-android\_3.1.3.aar',ext:'aar') to the dependencies block in build.gradle file

#### jar+so format

* Download jar package and so library to /lib in project
* Add implementation fileTree(dir: ‘libs’, include: \[’\*.jar’]) to build.gradle file

### Permission configuration

Add permissions as follows in AndroidManifest.xml:

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

### Quick integration

#### BMXClient initialization

* Import so library file into app entry class:

```
    static {
        System.loadLibrary("floo");
    }
```

* Initialize BMXClient

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

        String pushId = getPushId();//Set the ID corresponding to push platform
        BMXSDKConfig conf = new BMXSDKConfig(BMXClientType.Android, "1", dataPath.getAbsolutePath(),
                cachePath.getAbsolutePath(), TextUtils.isEmpty(pushId) ? "MaxIM" : pushId);
        conf.setConsoleOutput(true);
        conf.setLogLevel(BMXLogLevel.Debug);
        //Set push appId
        conf.setAppID("appId");
        //Set push secret
        conf.setAppSecret("appSecret");
        //Set the unique id of device
        conf.setDeviceUuid(deviceId);
        //Set production environment
        conf.setEnvironmentType(BMXPushEnvironmentType.Production);
        //Set pushProviderType based-on device model
        conf.setPushProviderType(getProviderType(context));
        BMXSDKConfig.HostConfig hostConfig = new BMXSDKConfig.HostConfig("sync.maxim.top", 443, "https://api.maxim.top");
        conf.setHostConfig(hostConfig);
        //Get BMXClient instance
        BMXClient bmxClient = BMXClient.create(conf);
    }


    //Get type based-on device model
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

#### Advanced invokation form

* BMXPushManager: Get the manager object to push via bmxClient.getPushManager().

#### Enable push

Parameter description: alias (push alias), bmxToken(push token) callBack

```
     SDK will automatically generate an alias if not passed in
     SDK will automatically generate a token and callback via BMXPushServiceListener if not passed in
```

```
Synchronous call
   Calling description: Success is judged by returned value of BMXErrorCode.

   bmxClient.getPushService().start();//No parameter passed in
   bmxClient.getPushService().start("zhangsan");//Pass in alias
   bmxClient.getPushService().start("zhangsan", token);//Pass in alias  token
Asynchronous calling
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   //No parameter passed in
   bmxClient.getPushManager().start(new BMXCallBack<>(){
        @Override
        public void onResult(BMXErrorCode bmxErrorCode) {

        }
   	});
   //Pass in alias
   bmxClient.getPushManager().start("zhangsan",new BMXCallBack<>(){
        @Override
        public void onResult(BMXErrorCode bmxErrorCode) {

        }
    });
   //Pass in alias token
   bmxClient.getPushManager().start("zhangsan", token, new BMXCallBack<>(){
        @Override
        public void onResult(BMXErrorCode bmxErrorCode) {

        }
    });
```

#### Stop push

Parameter description: callBack

```
Synchronous call
   Calling description: Success is judged by returned value of BMXErrorCode.

   bmxClient.getPushService().stop();
Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   bmxClient.getPushManager().stop(new BMXCallBack(){
   	      @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
   	});
```

#### Evoke push

```
Synchronous call
   Calling description: Success is judged by returned value of BMXErrorCode.

   bmxClient.getPushService().resume();

Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   bmxClient.getPushManager().remuse(new BMXCallBack<>() {
       @Override
        public void onResult(BMXErrorCode bmxErrorCode) {
        }
   });
```

#### Get push status

Returned value description: public static enum PushSdkState { Starting(1), Started, Stoped, Offline; }

```
Synchronous call:

   BMXPushService.PushSdkStatus status = bmxClient.getPushService().status();

Asynchronous call:

   BMXPushService.PushSdkStatus status = bmxClient.getPushManager().status();
```

#### Unbind alias

Parameter description: alias (push alias)

```
Synchronous call
   Calling description: Success is judged by returned value of BMXErrorCode.

   bmxClient.getPushService().unbindAlias(alias);
Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   bmxClient.getPushManager().unbindAlias(alias, new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### Get token

```
   Value is only available after start called successfully

Synchronous call:

   String token = bmxClient.getPushService().getToken();

Asynchronous call:

   String token = bmxClient.getPushManager().getToken();
```

#### Get cert

```
   Value is only available after start called successfully, meanwhile it needs to register the certificate with the corresponding vendor and set the correct provideType
   Currently support Huawei, Xiaomi, Meizu, oppo, and vivo

Synchronous call:

   String cert = bmxClient.getPushService().getCert();

Asynchronous call:

   String cert = bmxClient.getPushManager().getCert();
```

#### Bind vendor token

Parameter description: token (the token returned by register vendor push)

```
Synchronous call
   Calling description: Success is judged by returned value of BMXErrorCode.

   bmxClient.getPushService().bindDeviceToken(token);
Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   bmxClient.getPushManager().bindDeviceToken(token, new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### Get information of the user who pushed

Parameter description: forceRefresh (whether to pull from server)

```
Synchronous call
   Calling description: Passing in the BMXPushUserProfile object reference, and push user information can be obtained after successfully called.

   BMXPushUserProfile profile = new BMXPushUserProfile();
   bmxClient.getPushService().getPushProfile(profile, forceRefresh);
Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), and get push user information in BMXDataCallBack<BMXPushUserProfile> callback.

   bmxClient.getPushManager().getPushProfile(forceRefresh, new BMXDataCallBack<BMXPushUserProfile>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode, BMXPushUserProfile profile) {
            //Return BMXPushUserProfile instance
          }
    });
```

### Advanced interface

#### Set push tag

Parameter description: tags (tag list) operationId (the unique id generated manually in this operation)

```
    TagList tags = new TagList();
    tags.add("tag content");

Synchronous call
   Calling description: Success is judged by returned value of BMXErrorCode.

   bmxClient.getPushService().setTags(tags, operationId);
Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   bmxClient.getPushManager().setTags(tags, operationId, new BMXCallBack(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### Get push tag list

Parameter description: operationId (the unique id generated manually in this operation)

Calling description: Passing in the TagList object reference, and tag list information can be obtained after successfully called.

```
Synchronous call

   TagList tags = new TagList();
   bmxClient.getPushService().getTags(tags, operationId);

Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   TagList tags = new TagList();
   bmxClient.getPushManager().getTags(tags, operationId, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### Delete push tag

Parameter description: operationId (the unique id generated manually in this operation)

```
    TagList tags = new TagList();
    tags.add("tag content");

Synchronous call

   bmxClient.getPushService().deleteTags(tags, operationId);

Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   bmxClient.getPushManager().deleteTags(tags, operationId, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### Clear all tags

Parameter description: operationId (the unique id generated manually in this operation)

```
Synchronous call

   bmxClient.getPushService().clearTags(operationId);

Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   bmxClient.getPushManager().clearTags(operationId, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### Set push switch

Parameter description: enable (boolean push switch)

```
Synchronous call

   bmxClient.getPushService().setPushMode(enable);

Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   bmxClient.getPushManager().setPushMode(enable, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### Set push time

Parameter description: startHour (start time of push) endHour (end time of push) in 24-hour Set the daily push time range

```
Synchronous call

   bmxClient.getPushService().setPushTime(startHour, endHour);

Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   bmxClient.getPushManager().setPushTime(startHour, endHour, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### Set silent-push time

Parameter description: startHour (start time of push) endHour (end time of push) in 24-hour Set the daily non-push time range

```
Synchronous call

   bmxClient.getPushService().setSilenceTime(startHour, endHour);

Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   bmxClient.getPushManager().setSilenceTime(startHour, endHour, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {

          }
    });
```

#### Send push message

Parameter description: content(push content)

```
Synchronous call

   bmxClient.getPushService().sendMessage(content);

Asynchronous call

   bmxClient.getPushManager().sendMessage(content);
```

#### Get message list to push

Parameter description: refMsgId(starting message id, passed 0 first) size(number of fetched messagers)

```
Synchronous call
   Calling description: Passing in the BMXMessageList object reference, the push information list can be obtained after successfully called.

   BMXMessageList messageList = new BMXMessageList();
   bmxClient.getPushService().loadLocalPushMessages(refMsgId, size, messageList);
Asynchronous call
   Calling description: Get the manager object via bmxClient.getPushManager(), success is judged by returned BMXErrorCode in BMXCallBack callback.

   BMXMessageList messageList = new BMXMessageList();
   bmxClient.getPushManager().loadLocalPushMessages(refMsgId, size, messageList, new BMXCallBack<>(){
          @Override
          public void onResult(BMXErrorCode bmxErrorCode) {
          }
    });
```

### Set listener

* Register push callback

```
Synchronous call:
   bmxClient.getPushService().addPushListener(mListener);

Asynchronous call:
   bmxClient.getPushManager().addPushListener(mListener);
```

* Remove push callback

```
Synchronous call:
   bmxClient.getPushService().removePushListener(mListener);

Asynchronous call:
   bmxClient.getPushManager().removePushListener(mListener);
```

* Callback example

```
    private BMXPushServiceListener mListener = new BMXPushServiceListener() {

        @Override
        public void onPushStart(String bmxToken) {
            super.onPushStart(bmxToken);
            //Turn on push to return token
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
            //Return vendor-registered certificate You can register vendor’s push channel after obtaining the certificate
        }
    };
```

### Vender push integration

Platform integration only needs to put the integration SDK into your application according to the platform push document, and the corresponding configuration can be set based-on the specified platform requirements (except Huawei).

#### Huawei

Need to be set according to Huawei push platform [Huawei push](https://developer.huawei.com/consumer/cn/doc/development/HMSCore-Guides/android-app-quickstart-0000001071490422)

1. Project-level build.gradle filed added

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

1. App-level build.gradle

```
apply plugin: 'com.huawei.agconnect'
dependencies{
    implementation "com.huawei.hms:push:5.0.4.302"
}
```

1. Finally, download agconnect-services.json from push platform to your app directory.

#### Xiaomi

Integrate according to Xiaomi push platform [Xiaomi push](https://dev.mi.com/console/doc/detail?pId=230)

#### Oppo

Integrate according to Oppo push platform [oppo push](https://open.oppomobile.com/wiki/doc#id=10195)

#### Meizu

Integrate according to Meizu push platform [Meizu push](http://open-wiki.flyme.cn/doc-wiki/index)

#### Google push（FCM）

Google Push Guide [FCM](https://firebase.google.cn/docs/cloud-messaging/android/client?hl=zh-cn)
