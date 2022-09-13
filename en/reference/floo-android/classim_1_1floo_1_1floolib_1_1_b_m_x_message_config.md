---
title: im::floo::floolib::BMXMessageConfig
summary: Message configuration 

---

# im::floo::floolib::BMXMessageConfig



Message configuration 

Inherits from BMXBaseObject

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-delete)**() |
| void | **[setMentionAll](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setmentionall)**(boolean mentionAll)<br>Set whether to @ all members  |
| boolean | **[getMentionAll](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getmentionall)**()<br>Get whether to @ all members  |
| void | **[setMentionList](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setmentionlist)**(ListOfLongLong mentionList)<br>Set the list of notified member ids  |
| ListOfLongLong | **[getMentionList](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getmentionlist)**()<br>Get @ member list  |
| void | **[setMentionedMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setmentionedmessage)**(String mentionedMessage)<br>Set @ message  |
| String | **[getMentionedMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getmentionedmessage)**()<br>Get @ message  |
| void | **[setPushMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushmessage)**(String pushMessage)<br>Set push message  |
| String | **[getPushMessage](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushmessage)**()<br>Get push message  |
| void | **[setSenderNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setsendernickname)**(String senderNickname)<br>Set nickname of sender  |
| String | **[getSenderNickname](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getsendernickname)**()<br>Get nickname of sender  |
| void | **[setGroupMemberList](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setgroupmemberlist)**(ListOfLongLong groupMemberList)<br>Set the list of member ids that require read group messages  |
| ListOfLongLong | **[getGroupMemberList](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getgroupmemberlist)**()<br>Get the list of group member ids that require read group messages  |
| void | **[addGroupMember](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-addgroupmember)**(long id)<br>Member of group member id list with read messages added  |
| void | **[removeGroupMember](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-removegroupmember)**(long id)<br>Empty the list of member ids that require read group messages  |
| void | **[clearGroupMemberList](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-cleargroupmemberlist)**()<br>List of member ids with read group messages emptied  |
| void | **[setIOSConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setiosconfig)**(String iosConfig) |
| String | **[getIOSConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getiosconfig)**()<br>Get iOS message configuration  |
| void | **[setAndroidConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setandroidconfig)**(String androidConfig) |
| String | **[getAndroidConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getandroidconfig)**()<br>Get Android message configuration  |
| void | **[setPushShowBeginTime](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushshowbegintime)**(int beginTime) |
| int | **[getPushShowBeginTime](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushshowbegintime)**()<br>Get start time of push message displayed  |
| void | **[setPushShowEndTime](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushshowendtime)**(int endTime) |
| int | **[getPushShowEndTime](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushshowendtime)**()<br>Get end time of push message displayed  |
| void | **[setPushTitle](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushtitle)**(String pushTitle) |
| String | **[getPushTitle](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushtitle)**()<br>Get tittle of push message  |
| boolean | **[isSilence](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-issilence)**() |
| BMXMessageConfig.BadgeCountType | **[getBadgeCountType](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getbadgecounttype)**() |
| int | **[getBadgeCount](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getbadgecount)**(int count) |
| String | **[getUsername](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getusername)**()<br>Get username of message sender  |
| String | **[serialize](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-serialize)**()<br>Serialization operation  |
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

Set whether to @ all members 

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

Get whether to @ all members 

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

Set the list of notified member ids 

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

Get @ member list 

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

Set @ message 

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

Get @ message 

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

Set push message 

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

Get push message 

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

Set nickname of sender 

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

Get nickname of sender 

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

Set the list of member ids that require read group messages 

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

Get the list of group member ids that require read group messages 

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

Member of group member id list with read messages added 

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

Empty the list of member ids that require read group messages 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="removeGroupMember" %}{% endlanying_code_snippet %}
```
### function clearGroupMemberList

```java
inline void clearGroupMemberList()
```

List of member ids with read group messages emptied 

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

Get iOS message configuration 

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

Get Android message configuration 

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

Get start time of push message displayed 

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

Get end time of push message displayed 

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

Get tittle of push message 

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

Get username of message sender 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXMessageConfig",function="getUsername" %}{% endlanying_code_snippet %}
```
### function serialize

```java
inline String serialize()
```

Serialization operation 

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