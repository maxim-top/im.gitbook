# 7 推送接口{#push}

## 7.1 获取推送证书{#get__push_certificate}

> GET /push/certificate

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求参数(Query Param)
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| environment | int32 | false | 运行环境， 0 - 开发环境， 1 - 生产环境 , 默认值：1 |
| provider | int32 | true | 证书提供方, 1-APNS，2-华为，3-小米，4-魅族，5-VIVO， 6-OPPO, 7-FCM |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ app_id | string | APP ID |
|⇥ app_key | string | APP KEY |
|⇥ app_secret | string | APP SECRET |
|⇥ certificate | string | 证书 |
|⇥ name | string | 证书名称 |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 7.2 发推送通知{#post__push_notify}

> POST /push/notify

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| audience | object | false |  | 推送目标, 不可为空。类型为字符串或JSONObject:<br>"all", 表示发给所有设备<br>{"tag":["tag1","tag2"]} 表示发给标签为tag1或tag2的设备<br>{"alias":["alias1","alias2"]} 表示发给别名为alias1或alias2的设备<br>{"user_id":[111,222]} 表示发给用户ID为111或222的设备<br>{"push_token":["push_token1","push_token2"]} 表示发给PushToken为push_token1或push_token2的设备<br>使用标签/别名/用户ID/pushToken推送时，列表长度不能超过500 |
| setting | object | false |  | 推送设置，可为空 |
|⇥ request_id | string | false |  | 请求ID，用于请求去重，如果请求ID以前出现过，则不推送。可为空，为空则不去重。 |
|⇥ distribution_strategy | string | false |  | 通知下发策略: combined - 表示先使用蓝莺通道下发，蓝莺不在线，则使用厂商通道下发；mxpush_only - 表示只使用蓝莺通道下发; ospush_only - 表示只使用厂商通道下发。 可为空，为空则默认为combined |
|⇥ ospush_sequence | array[string] | false |  | 厂商推送顺序：ups - 国内厂商(小米/华为/魅族/oppo/vivo); fcm - FCM推送；huawei - 华为推送；xiaomi - 小米推送; oppo - OPPO推送; vivo - VIVO推送, meizu - 魅族推送。可为空，为空则默认为[ups,fcm] |
| message | object | false |  | 推送消息体， 不可为空 |
|⇥ type | string | false |  | 消息类型：text - 文本，image - 图片， cmd - 透传消息。可为空，为空则默认为text |
|⇥ title | string | false |  | 标题。可为空 |
|⇥ body | string | false |  | 内容。可为空 |
|⇥ attachment_url | string | false |  | 附件地址: 图片/音频/视频的URL地址。可为空。如果是图片地址，需要以jpg/jpeg/png结尾，图片大小需小于1M,推荐876*324px |
|⇥ big_text | string | false |  | 大文本： 如果设置此字段，并且厂商支持推送大文本，则使用此字段推送大文本，否则使用body字段的文本推送普通文本 |
|⇥ badge | string | false |  | 应用角标: 如果为数字，则修改角标为此数字；如果以+开头，表示增加此数字到角标，如"+1", 表示角标数加1;如果为空，默认为"+1" |
|⇥ ext | object | false |  | 扩展字段:可为空，类型为JSONObject, 例如: {"key1":123, "key2":"value2"} |
|⇥ show_begin_time | int64 | false |  | 定时展示的开始时间戳(秒), 为空时表示立即展示 |
|⇥ show_end_time | int64 | false |  | 定时展示的结束时间戳(秒)，可为空 |
|⇥ ios | object | false |  | android额外参数，可为空 |
|⇥⇥ sound | string | false |  | 通知提示声音， 可为空 |
|⇥⇥ content_available | boolean | false |  | 对应APNs的content-available，可为空 |
|⇥⇥ mutable_content | boolean | false |  | 对应APNs的mutable-content， 可为空 |
|⇥⇥ category | string | false |  | 对应APNs Payload中的category， 可为空 |
|⇥⇥ thread_id | string | false |  | 对应APNs的thread-id，可为空，通过该属性来对通知进行分组，相同thread-id 的通知归为一组 |
|⇥⇥ subtitle | string | false |  | 对应APNs的subtitle，可为空 |
|⇥⇥ apns_collapse_id | string | false |  | 对应APNs的apns-collapse-id，可为空，通知携带apns-collapse-id 参数，将会覆盖通知中心里携带相同apns-collapse-id的通知。 |
|⇥ android | object | false |  | ios额外参数，可为空 |
|⇥⇥ sound | string | false |  | 通知提示声音，可为空 |
|⇥⇥ channel_id | string | false |  | 通知栏通道，可为空 |
|⇥⇥ click_action | string | false |  | 点击通知的后续动作: intent 打开应用特定页面; open_app 打开应用首页。可为空 |
|⇥⇥ intent | string | false |  | 点击通知打开应用特定页面: 可为空，click_action为intent时不可为空。示例：intent:#Intent;component=包名/activity全路径;S.parm1=value1;S.parm2=value2;end |
|⇥ huawei | object | false |  | huawei厂商额外参数 |
|⇥⇥ sound | string | false |  | 通知提示声音，可为空 |
|⇥⇥ channel_id | string | false |  | 通知栏通道，可为空 |
|⇥⇥ click_action | string | false |  | 点击通知的后续动作: intent 打开应用特定页面; open_app 打开应用首页。可为空 |
|⇥⇥ intent | string | false |  | 点击通知打开应用特定页面: 可为空，click_action为intent时不可为空。示例：intent:#Intent;component=包名/activity全路径;S.parm1=value1;S.parm2=value2;end |
|⇥⇥ badge_class | string | false |  | 桌面图标对应的应用入口Activity类， 比如 com.test.badge.MainActivity， 可为空 |
|⇥ xiaomi | object | false |  | xiaomi厂商额外参数 |
|⇥⇥ sound | string | false |  | 通知提示声音，可为空 |
|⇥⇥ channel_id | string | false |  | 通知栏通道，可为空 |
|⇥⇥ click_action | string | false |  | 点击通知的后续动作: intent 打开应用特定页面; open_app 打开应用首页。可为空 |
|⇥⇥ intent | string | false |  | 点击通知打开应用特定页面: 可为空，click_action为intent时不可为空。示例：intent:#Intent;component=包名/activity全路径;S.parm1=value1;S.parm2=value2;end |
|⇥ oppo | object | false |  | oppo厂商额外参数 |
|⇥⇥ sound | string | false |  | 通知提示声音，可为空 |
|⇥⇥ channel_id | string | false |  | 通知栏通道，可为空 |
|⇥⇥ click_action | string | false |  | 点击通知的后续动作: intent 打开应用特定页面; open_app 打开应用首页。可为空 |
|⇥⇥ intent | string | false |  | 点击通知打开应用特定页面: 可为空，click_action为intent时不可为空。示例：intent:#Intent;component=包名/activity全路径;S.parm1=value1;S.parm2=value2;end |
|⇥ vivo | object | false |  | vivo厂商额外参数 |
|⇥⇥ sound | string | false |  | 通知提示声音，可为空 |
|⇥⇥ channel_id | string | false |  | 通知栏通道，可为空 |
|⇥⇥ click_action | string | false |  | 点击通知的后续动作: intent 打开应用特定页面; open_app 打开应用首页。可为空 |
|⇥⇥ intent | string | false |  | 点击通知打开应用特定页面: 可为空，click_action为intent时不可为空。示例：intent:#Intent;component=包名/activity全路径;S.parm1=value1;S.parm2=value2;end |
|⇥⇥ push_mode | int32 | false |  | 推送模式： 0-正式推送；1-测试推送，不填默认为0 |
|⇥⇥ classification | int32 | false |  | 消息类型 0：运营类消息，1：系统类消息。不填默认为0 |
|⇥ flyme | object | false |  | 魅族厂商额外参数 |
|⇥⇥ sound | string | false |  | 通知提示声音，可为空 |
|⇥⇥ channel_id | string | false |  | 通知栏通道，可为空 |
|⇥⇥ click_action | string | false |  | 点击通知的后续动作: intent 打开应用特定页面; open_app 打开应用首页。可为空 |
|⇥⇥ intent | string | false |  | 点击通知打开应用特定页面: 可为空，click_action为intent时不可为空。示例：intent:#Intent;component=包名/activity全路径;S.parm1=value1;S.parm2=value2;end |
|⇥ fcm | object | false |  | fcm厂商额外参数 |
|⇥⇥ sound | string | false |  | 通知提示声音，可为空 |
|⇥⇥ channel_id | string | false |  | 通知栏通道，可为空 |
|⇥⇥ click_action | string | false |  | 点击通知的后续动作: intent 打开应用特定页面; open_app 打开应用首页。可为空 |
|⇥⇥ intent | string | false |  | 点击通知打开应用特定页面: 可为空，click_action为intent时不可为空。示例：intent:#Intent;component=包名/activity全路径;S.parm1=value1;S.parm2=value2;end |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | object | 结果数据 |
|⇥ task_id | int64 | 任务ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

## 7.3 查询推送统计结果{#post__push_task_detail}

> POST /push/task/detail

#### 请求头
|  参数名称 |  数据类型 | 必填 |  描述 |
|  ------ |  ------ |  ------ |  ------ |
| access-token | string | false | 令牌 |
| app_id | string | true | 应用ID |
| group_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此群ID的管理员身份来调用此接口 |
| user_id | int64 | false | 仅当access-token为管理员token时，可以设置此字段，表示以此用户ID的身份来调用此接口 |

#### 请求体(Request Body)
|  参数名称 |  数据类型 | 必填  |  默认值 |  描述 |
|  ------ |  ------ |  ------ |  ------ |  ------ |
| list | array[int64] | false |  |  |

#### 响应体
● 200 响应数据格式：JSON

|  参数名称 |  类型 |  描述 |
|  ------ |  ------ |  ------ |
| code | int32 | 返回码，200是成功 |
| data | array[object] | 结果数据 |
|⇥ apns_received | int64 | APNs通道送达数 |
|⇥ apns_sent | int64 | APNs通道发送数 |
|⇥ apns_target | int64 | APNs通道有效目标数 |
|⇥ fcm_received | int64 | FCM通道送达数 |
|⇥ fcm_sent | int64 | FCM通道发送数 |
|⇥ fcm_target | int64 | FCM通道有效目标数 |
|⇥ flyme_received | int64 | 魅族通道送达数 |
|⇥ flyme_sent | int64 | 魅族通道发送数 |
|⇥ flyme_target | int64 | 魅族通道有效目标数 |
|⇥ huawei_received | int64 | 华为通道送达数 |
|⇥ huawei_sent | int64 | 华为通道发送数 |
|⇥ huawei_target | int64 | 华为通道有效目标数 |
|⇥ mxpush_received | int64 | 蓝莺通道送达数 |
|⇥ mxpush_sent | int64 | 蓝莺通道发送数 |
|⇥ mxpush_target | int64 | 蓝莺通道有效目标数 |
|⇥ oppo_received | int64 | oppo通道送达数 |
|⇥ oppo_sent | int64 | oppo通道发送数 |
|⇥ oppo_target | int64 | oppo通道有效目标数 |
|⇥ vivo_received | int64 | vivo通道送达数 |
|⇥ vivo_sent | int64 | vivo通道发送数 |
|⇥ vivo_target | int64 | vivo通道有效目标数 |
|⇥ xiaomi_received | int64 | 小米通道送达数 |
|⇥ xiaomi_sent | int64 | 小米通道发送数 |
|⇥ xiaomi_target | int64 | 小米通道有效目标数 |
|⇥ task_id | int64 | 推送任务ID |
| message | string | 错误信息，如果成功，该项为null |
#### 接口描述
> 

