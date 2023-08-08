---
title: floo::BMXMessageConfig
summary: 消息配置
---

# floo::BMXMessageConfig

消息配置

`#include <bmx_message_config.h>`

Inherits from BMXBaseObject

## Public Types

|            | Name                                                                                                                                               |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_config.md#enum-badgecounttype"><strong>BadgeCountType</strong></a> { Change, Set}<br>当前读取的Badge数字的操作类型</p> |

## Public Functions

|                                                                                    | Name                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                                                                            | [**\~BMXMessageConfig**](classfloo\_1\_1\_b\_m\_x\_message\_config.md#function-\~bmxmessageconfig)()                                                                                                      |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setmentionall"><strong>setMentionAll</strong></a>(bool mentionAll)<br>设置是否@全员</p>                                                              |
| bool                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getmentionall"><strong>getMentionAll</strong></a>()<br>获取是否@全员</p>                                                                             |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setmentionlist"><strong>setMentionList</strong></a>(const std::vector&#x3C; int64_t > &#x26; mentionList)<br>设置通知成员id列表</p>                    |
| std::vector< int64\_t >                                                            | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getmentionlist"><strong>getMentionList</strong></a>()<br>获取@成员列表</p>                                                                           |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setmentionedmessage"><strong>setMentionedMessage</strong></a>(const std::string &#x26; mentionedMessage)<br>设置@消息</p>                          |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getmentionedmessage"><strong>getMentionedMessage</strong></a>()<br>获取@消息</p>                                                                   |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setpushmessage"><strong>setPushMessage</strong></a>(const std::string &#x26; pushMessage)<br>设置推送消息</p>                                        |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getpushmessage"><strong>getPushMessage</strong></a>()<br>获取推送消息</p>                                                                            |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setsendernickname"><strong>setSenderNickname</strong></a>(const std::string &#x26; senderNickname)<br>设置发送者昵称</p>                              |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getsendernickname"><strong>getSenderNickname</strong></a>()<br>获取发送者昵称</p>                                                                     |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setgroupmemberlist"><strong>setGroupMemberList</strong></a>(const std::vector&#x3C; int64_t > &#x26; groupMemberList)<br>设置需要群已读消息的群成员id列表</p> |
| std::vector< int64\_t >                                                            | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getgroupmemberlist"><strong>getGroupMemberList</strong></a>()<br>获取需要群已读消息的群成员id列表</p>                                                         |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-addgroupmember"><strong>addGroupMember</strong></a>(int64_t id)<br>添加群已读消息的群成员id列表成员</p>                                                       |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-removegroupmember"><strong>removeGroupMember</strong></a>(int64_t id)<br>清除需要群已读消息的群成员id列表成员</p>                                               |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-cleargroupmemberlist"><strong>clearGroupMemberList</strong></a>()<br>清空群已读消息的群成员id列表</p>                                                       |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setiosconfig"><strong>setIOSConfig</strong></a>(const std::string &#x26; iosConfig)<br>设置IOS系统配置信息</p>                                         |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getiosconfig"><strong>getIOSConfig</strong></a>()<br>获取IOS系统配置信息</p>                                                                           |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setandroidconfig"><strong>setAndroidConfig</strong></a>(const std::string &#x26; androidConfig)<br>设置Android系统配置信息</p>                         |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getandroidconfig"><strong>getAndroidConfig</strong></a>()<br>获取Android系统配置信息</p>                                                               |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setpushshowbegintime"><strong>setPushShowBeginTime</strong></a>(int beginTime)<br>设置推送显示开始时间</p>                                               |
| int                                                                                | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getpushshowbegintime"><strong>getPushShowBeginTime</strong></a>()<br>获取推送显示开始时间</p>                                                            |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setpushshowendtime"><strong>setPushShowEndTime</strong></a>(int endTime)<br>设置推送显示结束时间</p>                                                     |
| int                                                                                | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getpushshowendtime"><strong>getPushShowEndTime</strong></a>()<br>获取推送显示结束时间</p>                                                                |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setpushtitle"><strong>setPushTitle</strong></a>(const std::string &#x26; pushTitle)<br>设置推送标题</p>                                              |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getpushtitle"><strong>getPushTitle</strong></a>()<br>获取推送标题</p>                                                                                |
| bool                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-issilence"><strong>isSilence</strong></a>()<br>获取当前的推送消息是否是静默消息</p>                                                                            |
| [BadgeCountType](classfloo\_1\_1\_b\_m\_x\_message\_config.md#enum-badgecounttype) | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getbadgecounttype"><strong>getBadgeCountType</strong></a>()<br>获取当前的推送消息中badge计数</p>                                                           |
| int                                                                                | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getbadgecount"><strong>getBadgeCount</strong></a>(int count)<br>获取当前的推送消息中badge计数</p>                                                          |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setusername"><strong>setUsername</strong></a>(const std::string &#x26; username)<br>设置用户名</p>                                                  |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getusername"><strong>getUsername</strong></a>()<br>获得用户名</p>                                                                                   |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-serialize"><strong>serialize</strong></a>() const<br>序列化操作</p>                                                                                 |
| BMXMessageConfigPtr                                                                | [**createMessageConfig**](classfloo\_1\_1\_b\_m\_x\_message\_config.md#function-createmessageconfig)(bool mentionAll)                                                                                     |

## Friends

|                     | Name                                                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| std::string         | [**encodeBMXMessageConfig**](classfloo\_1\_1\_b\_m\_x\_message\_config.md#friend-encodebmxmessageconfig)(BMXMessageConfigPtr )       |
| BMXMessageConfigPtr | [**decodeBMXMessageConfig**](classfloo\_1\_1\_b\_m\_x\_message\_config.md#friend-decodebmxmessageconfig)(const std::string & config) |

## Public Types Documentation

### enum BadgeCountType

| Enumerator | Value | Description                     |
| ---------- | ----- | ------------------------------- |
| Change     |       | 读取Badge计数的操作类型为增加或减少。正数为增加负数为减少 |
| Set        |       | 设置Badge的计数为当前的计数值               |

当前读取的Badge数字的操作类型

## Public Functions Documentation

### function \~BMXMessageConfig

```cpp
inline virtual ~BMXMessageConfig()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function setMentionAll

```cpp
void setMentionAll(
    bool mentionAll
)
```

设置是否@全员

**Parameters**:

* **mentionAll**

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getMentionAll

```cpp
bool getMentionAll()
```

获取是否@全员

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function setMentionList

```cpp
void setMentionList(
    const std::vector< int64_t > & mentionList
)
```

设置通知成员id列表

**Parameters**:

* **mentionList**

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getMentionList

```cpp
std::vector< int64_t > getMentionList()
```

获取@成员列表

**Return**: std::vector\<int64\_t>

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function setMentionedMessage

```cpp
void setMentionedMessage(
    const std::string & mentionedMessage
)
```

设置@消息

**Parameters**:

* **mentionedMessage**

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getMentionedMessage

```cpp
std::string getMentionedMessage()
```

获取@消息

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function setPushMessage

```cpp
void setPushMessage(
    const std::string & pushMessage
)
```

设置推送消息

**Parameters**:

* **pushMessage**

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getPushMessage

```cpp
std::string getPushMessage()
```

获取推送消息

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function setSenderNickname

```cpp
void setSenderNickname(
    const std::string & senderNickname
)
```

设置发送者昵称

**Parameters**:

* **senderNickname**

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getSenderNickname

```cpp
std::string getSenderNickname()
```

获取发送者昵称

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function setGroupMemberList

```cpp
void setGroupMemberList(
    const std::vector< int64_t > & groupMemberList
)
```

设置需要群已读消息的群成员id列表

**Parameters**:

* **groupMemberList**

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getGroupMemberList

```cpp
std::vector< int64_t > getGroupMemberList()
```

获取需要群已读消息的群成员id列表

**Return**: std::vector\<int64\_t>

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function addGroupMember

```cpp
void addGroupMember(
    int64_t id
)
```

添加群已读消息的群成员id列表成员

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function removeGroupMember

```cpp
void removeGroupMember(
    int64_t id
)
```

清除需要群已读消息的群成员id列表成员

**Return**: std::vector\<int64\_t>

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function clearGroupMemberList

```cpp
void clearGroupMemberList()
```

清空群已读消息的群成员id列表

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function setIOSConfig

```cpp
void setIOSConfig(
    const std::string & iosConfig
)
```

设置IOS系统配置信息

**Parameters**:

* **iosConfig**

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getIOSConfig

```cpp
std::string getIOSConfig()
```

获取IOS系统配置信息

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function setAndroidConfig

```cpp
void setAndroidConfig(
    const std::string & androidConfig
)
```

设置Android系统配置信息

**Parameters**:

* **androidConfig**

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getAndroidConfig

```cpp
std::string getAndroidConfig()
```

获取Android系统配置信息

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function setPushShowBeginTime

```cpp
void setPushShowBeginTime(
    int beginTime
)
```

设置推送显示开始时间

**Parameters**:

* **beginTime**

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getPushShowBeginTime

```cpp
int getPushShowBeginTime()
```

获取推送显示开始时间

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function setPushShowEndTime

```cpp
void setPushShowEndTime(
    int endTime
)
```

设置推送显示结束时间

**Parameters**:

* **endTime**

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getPushShowEndTime

```cpp
int getPushShowEndTime()
```

获取推送显示结束时间

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function setPushTitle

```cpp
void setPushTitle(
    const std::string & pushTitle
)
```

设置推送标题

**Parameters**:

* **pushTitle**

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getPushTitle

```cpp
std::string getPushTitle()
```

获取推送标题

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function isSilence

```cpp
bool isSilence()
```

获取当前的推送消息是否是静默消息

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getBadgeCountType

```cpp
BadgeCountType getBadgeCountType()
```

获取当前的推送消息中badge计数

**Return**: BadgeCountType

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getBadgeCount

```cpp
int getBadgeCount(
    int count
)
```

获取当前的推送消息中badge计数

**Return**: int

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function setUsername

```cpp
void setUsername(
    const std::string & username
)
```

设置用户名

**Parameters**:

* **username**

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getUsername

```cpp
std::string getUsername()
```

获得用户名

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function serialize

```cpp
std::string serialize() const
```

序列化操作

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function createMessageConfig

```cpp
static BMXMessageConfigPtr createMessageConfig(
    bool mentionAll
)
```

## Friends

### friend encodeBMXMessageConfig

```cpp
friend std::string encodeBMXMessageConfig(
    BMXMessageConfigPtr 
);
```

### friend decodeBMXMessageConfig

```cpp
friend BMXMessageConfigPtr decodeBMXMessageConfig(
    const std::string & config
);
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
