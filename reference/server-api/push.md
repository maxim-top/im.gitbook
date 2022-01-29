
## 4    Push interface

## 4.1  Get push certificate

> GET  /push/certificate

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Query Param
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|environment||Run environment, 0 - development environment, 1 - production environment, default: 1|
|provider||Certificate provider, 1-APNS,2-Huawei,3-Xiaomi,4-Meizu,5-VIVO, 6-OPPO, 7-FCM|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false|Push certificate information|
|⇥ app_id|string||false|APP ID|
|⇥ app_key|string||false|APP KEY|
|⇥ app_secret|string||false|APP SECRET|
|⇥ certificate|string||false|Certificate|
|⇥ name|string||false|Certificate name|
| message|string||false|Error information, null means success|


### Interface Description
> 




## 4.2  Send push notification

> POST  /push/notify

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| audience|object||false|Target of push, cannot be blank. Type is string or JSONObject:<br>"all", means push to all devices<br>{"tag":["tag1","tag2"]} means push to devices labeled tag1 or tag2<br>{"alias":["alias1","alias2"]} means push to devices with alias1 or alias2<br>{"user_id":[111,222]} means push to devices with user ID 111 or 222<br>{"push_token":["push_token1","push_token2"]} means push to devices with PushToken push_token1 or push_token2<br>List length cannot exceed 500 when pushed with tag/alias/user ID/pushToken<br>|
| setting|object||false|Push settings, can be blank|
|⇥ request_id|string||false|Request ID for request deduplication, not pushed if request ID has been present before. Can be blank, which means no deduplication.|
|⇥ distribution_strategy|string||false|**to-be-translate**|
|⇥ ospush_sequence|array[string]||false|**to-be-translate**|
| message|object||false|Message body pushed|
|⇥ type|string||false|Message type:text - text,image - image, cmd - pass-through message. Can be blank, which means text by default|
|⇥ title|string||false|Tittle, can be blank|
|⇥ body|string||false|Content, can be blank|
|⇥ attachment_url|string||false|Attachment address: URL address of image/audio/video, can be blank. If it is an image address, it needs to end with .jpg/jpeg/png, and the picture size should be less than 1M. 876*324 px is recommended|
|⇥ big_text|string||false|**to-be-translate**|
|⇥ badge|string||false|Badge: If it is a number, modify the badge to this number; If starts with +, means adding this number to badge, ex. “+1” means adding 1 to badge; If blank, default “+1"|
|⇥ ext|object||false|Extension field: Can be blank, JSONObject type, ex. {"key1":123, "key2":"value2"}|
|⇥ show_begin_time|int32||false|Start timestamp of timed presentation (seconds), blank for immediate presentation|
|⇥ show_end_time|int32||false|End timestamp of timed presentation (seconds), can be blank|
|⇥ ios|object||false|Ios platform extra parameter, can be blank|
|⇥⇥ sound|string||false|Notification alert sound, can be blank|
|⇥⇥ content_available|boolean||false|Corresponding to content-available in APNs, can be blank|
|⇥⇥ mutable_content|boolean||false|Corresponding to mutable-content in APNs, can be blank|
|⇥⇥ category|string||false|Corresponding to category in APNs Payload, can be blank|
|⇥⇥ thread_id|string||false|Corresponding to thread-id in APNs, can be blank; which is used for grouping notifications by thread-id|
|⇥⇥ subtitle|string||false|**to-be-translate**|
|⇥⇥ apns_collapse_id|string||false|**to-be-translate**|
|⇥ android|object||false|Additional parameter for android platform, can be blank|
|⇥⇥ sound|string||false|Message alert sound, can be blank|
|⇥⇥ channel_id|string||false|Notification bar channel, can be blank|
|⇥⇥ click_action|string||false|What to do after notification clicked: intent to open a specific page; open_app to open App homepage. Can be blank.|
|⇥⇥ intent|string||false|Click notification to open a specific page: can be blank, unless click_action is intent. Ex. intent:#Intent;component= package name/activity full path; S.parm1=value1;S.parm2=value2;end|
|⇥ huawei|object||false|Huawei vendor extra parameter, can be blank; if set, will override the corresponding attribute in Android|
|⇥⇥ sound|string||false|Message alert sound, can be blank|
|⇥⇥ channel_id|string||false|Notification bar channel, can be blank|
|⇥⇥ click_action|string||false|What to do after notification clicked: intent to open a specific page; open_app to open App homepage. Can be blank.|
|⇥⇥ intent|string||false|Click notification to open a specific page: can be blank, unless click_action is intent. Ex. intent:#Intent;component= package name/activity full path; S.parm1=value1;S.parm2=value2;end|
|⇥⇥ badge_class|string||false|The application entry Activity class corresponding to the desktop icon, such as com.test.badge.MainActivity, which can be blank|
|⇥ xiaomi|object||false|xiaomi vendor extra parameter, can be blank. If set, will override the corresponding attribute in Android|
|⇥⇥ sound|string||false|Message alert sound, can be blank|
|⇥⇥ channel_id|string||false|Notification bar channel, can be blank|
|⇥⇥ click_action|string||false|What to do after notification clicked: intent to open a specific page; open_app to open App homepage. Can be blank.|
|⇥⇥ intent|string||false|Click notification to open a specific page: can be blank, unless click_action is intent. Ex. intent:#Intent;component= package name/activity full path; S.parm1=value1;S.parm2=value2;end|
|⇥ oppo|object||false|Oppo vendor extra parameter, can be blank; if set, will override the corresponding attribute in Android|
|⇥⇥ sound|string||false|Message alert sound, can be blank|
|⇥⇥ channel_id|string||false|Notification bar channel, can be blank|
|⇥⇥ click_action|string||false|What to do after notification clicked: intent to open a specific page; open_app to open App homepage. Can be blank.|
|⇥⇥ intent|string||false|Click notification to open a specific page: can be blank, unless click_action is intent. Ex. intent:#Intent;component= package name/activity full path; S.parm1=value1;S.parm2=value2;end|
|⇥ vivo|object||false|vivo vendor extra parameter, can be blank. If set, will override the corresponding attribute in Android|
|⇥⇥ sound|string||false|Message alert sound, can be blank|
|⇥⇥ channel_id|string||false|Notification bar channel, can be blank|
|⇥⇥ click_action|string||false|What to do after notification clicked: intent to open a specific page; open_app to open App homepage. Can be blank.|
|⇥⇥ intent|string||false|Click notification to open a specific page: can be blank, unless click_action is intent. Ex. intent:#Intent;component= package name/activity full path; S.parm1=value1;S.parm2=value2;end|
|⇥⇥ push_mode|int32||false|Push mode: 0 - production push; 1 - testing push. Default 0|
|⇥⇥ classification|int32||false|Message type: 0 - operational message; 1 - system message. Default 0|
|⇥ flyme|object||false|Meizu vendor extra parameter, can be blank; if set, will override the corresponding attribute in Android|
|⇥⇥ sound|string||false|Message alert sound, can be blank|
|⇥⇥ channel_id|string||false|Notification bar channel, can be blank|
|⇥⇥ click_action|string||false|What to do after notification clicked: intent to open a specific page; open_app to open App homepage. Can be blank.|
|⇥⇥ intent|string||false|Click notification to open a specific page: can be blank, unless click_action is intent. Ex. intent:#Intent;component= package name/activity full path; S.parm1=value1;S.parm2=value2;end|
|⇥ fcm|object||false|FCM vendor extra parameter, can be blank; if set, will override the corresponding attribute in Android|
|⇥⇥ sound|string||false|Message alert sound, can be blank|
|⇥⇥ channel_id|string||false|Notification bar channel, can be blank|
|⇥⇥ click_action|string||false|What to do after notification clicked: intent to open a specific page; open_app to open App homepage. Can be blank.|
|⇥⇥ intent|string||false|Click notification to open a specific page: can be blank, unless click_action is intent. Ex. intent:#Intent;component= package name/activity full path; S.parm1=value1;S.parm2=value2;end|

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|object||false||
|⇥ task_id|int32||false|**to-be-translate**|
| message|string||false|Error information, null means success|


### Interface Description
> Enable push function in background management to send push notification.
Specific request parameters can be found in Model.
Common request format as follows:
1. Push text to all devices
{
  "audience": "all",
  "message": {
    "type": "text",
    "title": "this is push title",
    "body": "this is push body"
  }
}
2. Push pictures to devices with push_token token1 or token2
{
  "audience": {"push_token":["token1","token2"]},
  "message": {
    "type": "image",
    "title": "this is push title",
    "body": "this is push body",
    "attachment_url": "https://xxx.com/images/1.jpg"
  }
}
3. Push a pass-through message to all devices labeled Beijing or shanghai, pass-through message will not be displayed on notification bar
{
  "audience": {"tag":["beijing","shanghai"]},
  "message": {
    "type": "cmd",
    "title": "this is push title",
    "body": "this is push body",
    "ext": {"key1": 12345, "key2": "xxx" }
  }
}




## 4.3  **to-be-translate**

> POST  /push/task/detail

### Request Header
| Parameter name | Default | Description |
| ------ | ------ | ------ |
|access-token||Token||app_id||App ID||group_id||This field can be set only if access-token is an Admin token, means call this interface as an Admin for this group ID||user_id||This field can be set only if access-token is a user token, means call this interface as a group member for this user ID|

### Request Body
| Parameter name | Data Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| list|array[int32]||false||

### Response Body
● 200 Response data format:JSON
| Parameter name | Type | Default | Not null | Description |
| ------ | ------ | ------ | ------ | ------ |
| code|int32||false|Return code, 200 is success|
| data|array[object]||false|Result data|
|⇥ apns_received|int32||false|**to-be-translate**|
|⇥ apns_sent|int32||false|**to-be-translate**|
|⇥ apns_target|int32||false|**to-be-translate**|
|⇥ fcm_received|int32||false|**to-be-translate**|
|⇥ fcm_sent|int32||false|**to-be-translate**|
|⇥ fcm_target|int32||false|**to-be-translate**|
|⇥ flyme_received|int32||false|**to-be-translate**|
|⇥ flyme_sent|int32||false|**to-be-translate**|
|⇥ flyme_target|int32||false|**to-be-translate**|
|⇥ huawei_received|int32||false|**to-be-translate**|
|⇥ huawei_sent|int32||false|**to-be-translate**|
|⇥ huawei_target|int32||false|**to-be-translate**|
|⇥ mxpush_received|int32||false|**to-be-translate**|
|⇥ mxpush_sent|int32||false|**to-be-translate**|
|⇥ mxpush_target|int32||false|**to-be-translate**|
|⇥ oppo_received|int32||false|**to-be-translate**|
|⇥ oppo_sent|int32||false|**to-be-translate**|
|⇥ oppo_target|int32||false|**to-be-translate**|
|⇥ vivo_received|int32||false|**to-be-translate**|
|⇥ vivo_sent|int32||false|**to-be-translate**|
|⇥ vivo_target|int32||false|**to-be-translate**|
|⇥ xiaomi_received|int32||false|**to-be-translate**|
|⇥ xiaomi_sent|int32||false|**to-be-translate**|
|⇥ xiaomi_target|int32||false|**to-be-translate**|
|⇥ task_id|int32||false|**to-be-translate**|
| message|string||false|Error information, null means success|


### Interface Description
> 



