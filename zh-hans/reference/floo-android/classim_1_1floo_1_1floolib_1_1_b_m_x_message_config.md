---
title: im::floo::floolib::BMXMessageConfig
summary: 消息配置 

---

# im::floo::floolib::BMXMessageConfig



消息配置 

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-delete)**() |
| void | **[setMentionAll](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setmentionall)**(boolean mentionAll)<br>设置是否@全员  |
| boolean | **[getMentionAll](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getmentionall)**()<br>获取是否@全员  |
| void | **[setMentionList](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setmentionlist)**(ListOfLongLong mentionList)<br>设置通知成员id列表  |
| ListOfLongLong | **[getMentionList](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getmentionlist)**()<br>获取@成员列表  |
| void | **[setMentionedMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setmentionedmessage)**(String mentionedMessage)<br>设置@消息  |
| String | **[getMentionedMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getmentionedmessage)**()<br>获取@消息  |
| void | **[setPushMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushmessage)**(String pushMessage)<br>设置推送消息  |
| String | **[getPushMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushmessage)**()<br>获取推送消息  |
| void | **[setSenderNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setsendernickname)**(String senderNickname)<br>设置发送者昵称  |
| String | **[getSenderNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getsendernickname)**()<br>获取发送者昵称  |
| void | **[setGroupMemberList](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setgroupmemberlist)**(ListOfLongLong groupMemberList)<br>设置需要群已读消息的群成员id列表  |
| ListOfLongLong | **[getGroupMemberList](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getgroupmemberlist)**()<br>获取需要群已读消息的群成员id列表  |
| void | **[addGroupMember](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-addgroupmember)**(long id)<br>添加群已读消息的群成员id列表成员  |
| void | **[removeGroupMember](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-removegroupmember)**(long id)<br>清除需要群已读消息的群成员id列表成员  |
| void | **[clearGroupMemberList](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-cleargroupmemberlist)**()<br>清空群已读消息的群成员id列表  |
| void | **[setIOSConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setiosconfig)**(String iosConfig) |
| String | **[getIOSConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getiosconfig)**()<br>获取iOS消息配置  |
| void | **[setAndroidConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setandroidconfig)**(String androidConfig) |
| String | **[getAndroidConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getandroidconfig)**()<br>获取Android消息配置  |
| void | **[setPushShowBeginTime](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushshowbegintime)**(int beginTime) |
| int | **[getPushShowBeginTime](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushshowbegintime)**()<br>获取推送消息开始展示时间  |
| void | **[setPushShowEndTime](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushshowendtime)**(int endTime) |
| int | **[getPushShowEndTime](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushshowendtime)**()<br>获取推送消息结束展示时间  |
| void | **[setPushTitle](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushtitle)**(String pushTitle) |
| String | **[getPushTitle](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushtitle)**()<br>获取推送消息标题  |
| boolean | **[isSilence](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-issilence)**() |
| BMXMessageConfig.BadgeCountType | **[getBadgeCountType](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getbadgecounttype)**() |
| int | **[getBadgeCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getbadgecount)**(int count) |
| String | **[getUsername](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getusername)**()<br>获取消息发送者用户名  |
| String | **[serialize](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-serialize)**()<br>序列化操作  |
| [BMXMessageConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md) | **[createMessageConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-createmessageconfig)**(boolean mentionAll) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXMessageConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-bmxmessageconfig)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-finalize)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getcptr)**([BMXMessageConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md) obj) |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="delete" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="setMentionAll" %}{% endlanying_code_snippet %}
```
### function getMentionAll

```java
inline boolean getMentionAll()
```

获取是否@全员 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getMentionAll" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="setMentionList" %}{% endlanying_code_snippet %}
```
### function getMentionList

```java
inline ListOfLongLong getMentionList()
```

获取@成员列表 

**Return**: std::vector<int64_t> 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getMentionList" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="setMentionedMessage" %}{% endlanying_code_snippet %}
```
### function getMentionedMessage

```java
inline String getMentionedMessage()
```

获取@消息 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getMentionedMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="setPushMessage" %}{% endlanying_code_snippet %}
```
### function getPushMessage

```java
inline String getPushMessage()
```

获取推送消息 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getPushMessage" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="setSenderNickname" %}{% endlanying_code_snippet %}
```
### function getSenderNickname

```java
inline String getSenderNickname()
```

获取发送者昵称 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getSenderNickname" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="setGroupMemberList" %}{% endlanying_code_snippet %}
```
### function getGroupMemberList

```java
inline ListOfLongLong getGroupMemberList()
```

获取需要群已读消息的群成员id列表 

**Return**: std::vector<int64_t> 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getGroupMemberList" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="addGroupMember" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="removeGroupMember" %}{% endlanying_code_snippet %}
```
### function clearGroupMemberList

```java
inline void clearGroupMemberList()
```

清空群已读消息的群成员id列表 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="clearGroupMemberList" %}{% endlanying_code_snippet %}
```
### function setIOSConfig

```java
inline void setIOSConfig(
    String iosConfig
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="setIOSConfig" %}{% endlanying_code_snippet %}
```
### function getIOSConfig

```java
inline String getIOSConfig()
```

获取iOS消息配置 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getIOSConfig" %}{% endlanying_code_snippet %}
```
### function setAndroidConfig

```java
inline void setAndroidConfig(
    String androidConfig
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="setAndroidConfig" %}{% endlanying_code_snippet %}
```
### function getAndroidConfig

```java
inline String getAndroidConfig()
```

获取Android消息配置 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getAndroidConfig" %}{% endlanying_code_snippet %}
```
### function setPushShowBeginTime

```java
inline void setPushShowBeginTime(
    int beginTime
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="setPushShowBeginTime" %}{% endlanying_code_snippet %}
```
### function getPushShowBeginTime

```java
inline int getPushShowBeginTime()
```

获取推送消息开始展示时间 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getPushShowBeginTime" %}{% endlanying_code_snippet %}
```
### function setPushShowEndTime

```java
inline void setPushShowEndTime(
    int endTime
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="setPushShowEndTime" %}{% endlanying_code_snippet %}
```
### function getPushShowEndTime

```java
inline int getPushShowEndTime()
```

获取推送消息结束展示时间 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getPushShowEndTime" %}{% endlanying_code_snippet %}
```
### function setPushTitle

```java
inline void setPushTitle(
    String pushTitle
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="setPushTitle" %}{% endlanying_code_snippet %}
```
### function getPushTitle

```java
inline String getPushTitle()
```

获取推送消息标题 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getPushTitle" %}{% endlanying_code_snippet %}
```
### function isSilence

```java
inline boolean isSilence()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="isSilence" %}{% endlanying_code_snippet %}
```
### function getBadgeCountType

```java
inline BMXMessageConfig.BadgeCountType getBadgeCountType()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getBadgeCountType" %}{% endlanying_code_snippet %}
```
### function getBadgeCount

```java
inline int getBadgeCount(
    int count
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getBadgeCount" %}{% endlanying_code_snippet %}
```
### function getUsername

```java
inline String getUsername()
```

获取消息发送者用户名 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getUsername" %}{% endlanying_code_snippet %}
```
### function serialize

```java
inline String serialize()
```

序列化操作 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="serialize" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="createMessageConfig" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="BMXMessageConfig" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="finalize" %}{% endlanying_code_snippet %}
```
### function getCPtr

```java
static inline long getCPtr(
    BMXMessageConfig obj
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800