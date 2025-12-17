---
title: im::floo::floolib::BMXMessageConfig
summary: 消息配置
---

# im::floo::floolib::BMXMessageConfig

消息配置

Inherits from BMXBaseObject

## Public Functions

|                                                                            | Name                                                                                                                                                                                             |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| synchronized void                                                          | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-delete)()                                                                                                           |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setmentionall"><strong>setMentionAll</strong></a>(boolean mentionAll)<br>设置是否@全员</p>                                 |
| boolean                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getmentionall"><strong>getMentionAll</strong></a>()<br>获取是否@全员</p>                                                   |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setmentionlist"><strong>setMentionList</strong></a>(ListOfLongLong mentionList)<br>设置通知成员id列表</p>                    |
| ListOfLongLong                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getmentionlist"><strong>getMentionList</strong></a>()<br>获取@成员列表</p>                                                 |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setmentionedmessage"><strong>setMentionedMessage</strong></a>(String mentionedMessage)<br>设置@消息</p>                  |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getmentionedmessage"><strong>getMentionedMessage</strong></a>()<br>获取@消息</p>                                         |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushmessage"><strong>setPushMessage</strong></a>(String pushMessage)<br>设置推送消息</p>                                |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushmessage"><strong>getPushMessage</strong></a>()<br>获取推送消息</p>                                                  |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setsendernickname"><strong>setSenderNickname</strong></a>(String senderNickname)<br>设置发送者昵称</p>                      |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getsendernickname"><strong>getSenderNickname</strong></a>()<br>获取发送者昵称</p>                                           |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setgroupmemberlist"><strong>setGroupMemberList</strong></a>(ListOfLongLong groupMemberList)<br>设置需要群已读消息的群成员id列表</p> |
| ListOfLongLong                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getgroupmemberlist"><strong>getGroupMemberList</strong></a>()<br>获取需要群已读消息的群成员id列表</p>                               |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-addgroupmember"><strong>addGroupMember</strong></a>(long id)<br>添加群已读消息的群成员id列表成员</p>                                |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-removegroupmember"><strong>removeGroupMember</strong></a>(long id)<br>清除需要群已读消息的群成员id列表成员</p>                        |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-cleargroupmemberlist"><strong>clearGroupMemberList</strong></a>()<br>清空群已读消息的群成员id列表</p>                             |
| void                                                                       | [**setIOSConfig**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setiosconfig)(String iosConfig)                                                                               |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getiosconfig"><strong>getIOSConfig</strong></a>()<br>获取iOS消息配置</p>                                                   |
| void                                                                       | [**setAndroidConfig**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setandroidconfig)(String androidConfig)                                                                   |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getandroidconfig"><strong>getAndroidConfig</strong></a>()<br>获取Android消息配置</p>                                       |
| void                                                                       | [**setPushShowBeginTime**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushshowbegintime)(int beginTime)                                                                  |
| int                                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushshowbegintime"><strong>getPushShowBeginTime</strong></a>()<br>获取推送消息开始展示时间</p>                                |
| void                                                                       | [**setPushShowEndTime**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushshowendtime)(int endTime)                                                                        |
| int                                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushshowendtime"><strong>getPushShowEndTime</strong></a>()<br>获取推送消息结束展示时间</p>                                    |
| void                                                                       | [**setPushTitle**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushtitle)(String pushTitle)                                                                               |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushtitle"><strong>getPushTitle</strong></a>()<br>获取推送消息标题</p>                                                    |
| boolean                                                                    | [**isSilence**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-issilence)()                                                                                                     |
| BMXMessageConfig.BadgeCountType                                            | [**getBadgeCountType**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getbadgecounttype)()                                                                                     |
| int                                                                        | [**getBadgeCount**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getbadgecount)(int count)                                                                                    |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getusername"><strong>getUsername</strong></a>()<br>获取消息发送者用户名</p>                                                    |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-serialize"><strong>serialize</strong></a>()<br>序列化操作</p>                                                             |
| [BMXMessageConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md) | [**createMessageConfig**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-createmessageconfig)(boolean mentionAll)                                                               |

## Protected Functions

|      | Name                                                                                                                                                                   |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      | [**BMXMessageConfig**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-bmxmessageconfig)(long cPtr, boolean cMemoryOwn)                                |
| void | [**finalize**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-finalize)()                                                                             |
| long | [**getCPtr**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getcptr)([BMXMessageConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md) obj) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function setMentionAll

```java
inline void setMentionAll(
    boolean mentionAll
)
```

设置是否@全员

**Parameters**:

* **mentionAll**

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getMentionAll

```java
inline boolean getMentionAll()
```

获取是否@全员

**Return**: bool

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function setMentionList

```java
inline void setMentionList(
    ListOfLongLong mentionList
)
```

设置通知成员id列表

**Parameters**:

* **mentionList**

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getMentionList

```java
inline ListOfLongLong getMentionList()
```

获取@成员列表

**Return**: std::vector\<int64\_t>

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function setMentionedMessage

```java
inline void setMentionedMessage(
    String mentionedMessage
)
```

设置@消息

**Parameters**:

* **mentionedMessage**

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getMentionedMessage

```java
inline String getMentionedMessage()
```

获取@消息

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function setPushMessage

```java
inline void setPushMessage(
    String pushMessage
)
```

设置推送消息

**Parameters**:

* **pushMessage**

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getPushMessage

```java
inline String getPushMessage()
```

获取推送消息

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function setSenderNickname

```java
inline void setSenderNickname(
    String senderNickname
)
```

设置发送者昵称

**Parameters**:

* **senderNickname**

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getSenderNickname

```java
inline String getSenderNickname()
```

获取发送者昵称

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function setGroupMemberList

```java
inline void setGroupMemberList(
    ListOfLongLong groupMemberList
)
```

设置需要群已读消息的群成员id列表

**Parameters**:

* **groupMemberList**

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getGroupMemberList

```java
inline ListOfLongLong getGroupMemberList()
```

获取需要群已读消息的群成员id列表

**Return**: std::vector\<int64\_t>

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function addGroupMember

```java
inline void addGroupMember(
    long id
)
```

添加群已读消息的群成员id列表成员

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function removeGroupMember

```java
inline void removeGroupMember(
    long id
)
```

清除需要群已读消息的群成员id列表成员

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function clearGroupMemberList

```java
inline void clearGroupMemberList()
```

清空群已读消息的群成员id列表

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function setIOSConfig

```java
inline void setIOSConfig(
    String iosConfig
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getIOSConfig

```java
inline String getIOSConfig()
```

获取iOS消息配置

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function setAndroidConfig

```java
inline void setAndroidConfig(
    String androidConfig
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getAndroidConfig

```java
inline String getAndroidConfig()
```

获取Android消息配置

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function setPushShowBeginTime

```java
inline void setPushShowBeginTime(
    int beginTime
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getPushShowBeginTime

```java
inline int getPushShowBeginTime()
```

获取推送消息开始展示时间

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function setPushShowEndTime

```java
inline void setPushShowEndTime(
    int endTime
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getPushShowEndTime

```java
inline int getPushShowEndTime()
```

获取推送消息结束展示时间

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function setPushTitle

```java
inline void setPushTitle(
    String pushTitle
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getPushTitle

```java
inline String getPushTitle()
```

获取推送消息标题

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function isSilence

```java
inline boolean isSilence()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getBadgeCountType

```java
inline BMXMessageConfig.BadgeCountType getBadgeCountType()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getBadgeCount

```java
inline int getBadgeCount(
    int count
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getUsername

```java
inline String getUsername()
```

获取消息发送者用户名

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function serialize

```java
inline String serialize()
```

序列化操作

**Return**: std::string

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function createMessageConfig

```java
static inline BMXMessageConfig createMessageConfig(
    boolean mentionAll
)
```

## Protected Functions Documentation

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function BMXMessageConfig

```java
inline BMXMessageConfig(
    long cPtr,
    boolean cMemoryOwn
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function finalize

```java
inline void finalize()
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function getCPtr

```java
static inline long getCPtr(
    BMXMessageConfig obj
)
```

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>
```

***

Updated on 2022-01-26 at 17:18:31 +0800
