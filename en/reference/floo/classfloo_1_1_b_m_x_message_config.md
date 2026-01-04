---
title: floo::BMXMessageConfig
summary: Message configuration 

---

# floo::BMXMessageConfig



Message configuration 


`#include <bmx_message_config.h>`

Inherits from BMXBaseObject

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[BadgeCountType](classfloo_1_1_b_m_x_message_config.md#enum-badgecounttype)** { Change, Set}<br>Operation type of the currently read Badge number  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXMessageConfig](classfloo_1_1_b_m_x_message_config.md#function-~bmxmessageconfig)**() |
| void | **[setMentionAll](classfloo_1_1_b_m_x_message_config.md#function-setmentionall)**(bool mentionAll)<br>Set whether to @ all members  |
| bool | **[getMentionAll](classfloo_1_1_b_m_x_message_config.md#function-getmentionall)**()<br>Get whether to @ all members  |
| void | **[setMentionList](classfloo_1_1_b_m_x_message_config.md#function-setmentionlist)**(const std::vector< int64_t > & mentionList)<br>Set the list of notified member ids  |
| std::vector< int64_t > | **[getMentionList](classfloo_1_1_b_m_x_message_config.md#function-getmentionlist)**()<br>Get @ member list  |
| void | **[setMentionedMessage](classfloo_1_1_b_m_x_message_config.md#function-setmentionedmessage)**(const std::string & mentionedMessage)<br>Set @ message  |
| std::string | **[getMentionedMessage](classfloo_1_1_b_m_x_message_config.md#function-getmentionedmessage)**()<br>Get @ message  |
| void | **[setPushMessage](classfloo_1_1_b_m_x_message_config.md#function-setpushmessage)**(const std::string & pushMessage)<br>Set push message  |
| std::string | **[getPushMessage](classfloo_1_1_b_m_x_message_config.md#function-getpushmessage)**()<br>Get push message  |
| void | **[setSenderNickname](classfloo_1_1_b_m_x_message_config.md#function-setsendernickname)**(const std::string & senderNickname)<br>Set nickname of sender  |
| std::string | **[getSenderNickname](classfloo_1_1_b_m_x_message_config.md#function-getsendernickname)**()<br>Get nickname of sender  |
| void | **[setGroupMemberList](classfloo_1_1_b_m_x_message_config.md#function-setgroupmemberlist)**(const std::vector< int64_t > & groupMemberList)<br>Set the list of member ids that require read group messages  |
| std::vector< int64_t > | **[getGroupMemberList](classfloo_1_1_b_m_x_message_config.md#function-getgroupmemberlist)**()<br>Get the list of group member ids that require read group messages  |
| void | **[addGroupMember](classfloo_1_1_b_m_x_message_config.md#function-addgroupmember)**(int64_t id)<br>Member of group member id list with read messages added  |
| void | **[removeGroupMember](classfloo_1_1_b_m_x_message_config.md#function-removegroupmember)**(int64_t id)<br>Empty the list of member ids that require read group messages  |
| void | **[clearGroupMemberList](classfloo_1_1_b_m_x_message_config.md#function-cleargroupmemberlist)**()<br>List of member ids with read group messages emptied  |
| void | **[setIOSConfig](classfloo_1_1_b_m_x_message_config.md#function-setiosconfig)**(const std::string & iosConfig)<br>Set IOS system configuration information  |
| std::string | **[getIOSConfig](classfloo_1_1_b_m_x_message_config.md#function-getiosconfig)**()<br>Get IOS system configuration information  |
| void | **[setAndroidConfig](classfloo_1_1_b_m_x_message_config.md#function-setandroidconfig)**(const std::string & androidConfig)<br>Set Android system configuration information  |
| std::string | **[getAndroidConfig](classfloo_1_1_b_m_x_message_config.md#function-getandroidconfig)**()<br>Get Android system configuration information  |
| void | **[setPushShowBeginTime](classfloo_1_1_b_m_x_message_config.md#function-setpushshowbegintime)**(int beginTime)<br>Set start time for push display  |
| int | **[getPushShowBeginTime](classfloo_1_1_b_m_x_message_config.md#function-getpushshowbegintime)**()<br>Get start time for push display  |
| void | **[setPushShowEndTime](classfloo_1_1_b_m_x_message_config.md#function-setpushshowendtime)**(int endTime)<br>Set end time for push display  |
| int | **[getPushShowEndTime](classfloo_1_1_b_m_x_message_config.md#function-getpushshowendtime)**()<br>Get end time for push display  |
| void | **[setPushTitle](classfloo_1_1_b_m_x_message_config.md#function-setpushtitle)**(const std::string & pushTitle)<br>Set push header  |
| std::string | **[getPushTitle](classfloo_1_1_b_m_x_message_config.md#function-getpushtitle)**()<br>Get push header  |
| bool | **[isSilence](classfloo_1_1_b_m_x_message_config.md#function-issilence)**()<br>Get whether the current push is a silent message  |
| [BadgeCountType](classfloo_1_1_b_m_x_message_config.md#enum-badgecounttype) | **[getBadgeCountType](classfloo_1_1_b_m_x_message_config.md#function-getbadgecounttype)**()<br>Get the badge count of the current push  |
| int | **[getBadgeCount](classfloo_1_1_b_m_x_message_config.md#function-getbadgecount)**(int count)<br>Get the badge count of the current push  |
| void | **[setUsername](classfloo_1_1_b_m_x_message_config.md#function-setusername)**(const std::string & username)<br>Set username  |
| std::string | **[getUsername](classfloo_1_1_b_m_x_message_config.md#function-getusername)**()<br>Get username  |
| std::string | **[serialize](classfloo_1_1_b_m_x_message_config.md#function-serialize)**() const<br>Serialization operation  |
| BMXMessageConfigPtr | **[createMessageConfig](classfloo_1_1_b_m_x_message_config.md#function-createmessageconfig)**(bool mentionAll) |

## Friends

|                | Name           |
| -------------- | -------------- |
| std::string | **[encodeBMXMessageConfig](classfloo_1_1_b_m_x_message_config.md#friend-encodebmxmessageconfig)**(BMXMessageConfigPtr )  |
| BMXMessageConfigPtr | **[decodeBMXMessageConfig](classfloo_1_1_b_m_x_message_config.md#friend-decodebmxmessageconfig)**(const std::string & config)  |

## Public Types Documentation

### enum BadgeCountType

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| Change | | The type of operation to read the Badge count is increment or decrement. Positive number is increment and negative number is decrement.   |
| Set | | Set the Badge count to the current count   |



Operation type of the currently read Badge number 

## Public Functions Documentation

### function ~BMXMessageConfig

```cpp
inline virtual ~BMXMessageConfig()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="~BMXMessageConfig" %}{% endlanying_code_snippet %}
```
### function setMentionAll

```cpp
void setMentionAll(
    bool mentionAll
)
```

Set whether to @ all members 

**Parameters**: 

  * **mentionAll** 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="setMentionAll" %}{% endlanying_code_snippet %}
```
### function getMentionAll

```cpp
bool getMentionAll()
```

Get whether to @ all members 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getMentionAll" %}{% endlanying_code_snippet %}
```
### function setMentionList

```cpp
void setMentionList(
    const std::vector< int64_t > & mentionList
)
```

Set the list of notified member ids 

**Parameters**: 

  * **mentionList** 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="setMentionList" %}{% endlanying_code_snippet %}
```
### function getMentionList

```cpp
std::vector< int64_t > getMentionList()
```

Get @ member list 

**Return**: std::vector<int64_t> 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getMentionList" %}{% endlanying_code_snippet %}
```
### function setMentionedMessage

```cpp
void setMentionedMessage(
    const std::string & mentionedMessage
)
```

Set @ message 

**Parameters**: 

  * **mentionedMessage** 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="setMentionedMessage" %}{% endlanying_code_snippet %}
```
### function getMentionedMessage

```cpp
std::string getMentionedMessage()
```

Get @ message 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getMentionedMessage" %}{% endlanying_code_snippet %}
```
### function setPushMessage

```cpp
void setPushMessage(
    const std::string & pushMessage
)
```

Set push message 

**Parameters**: 

  * **pushMessage** 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="setPushMessage" %}{% endlanying_code_snippet %}
```
### function getPushMessage

```cpp
std::string getPushMessage()
```

Get push message 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getPushMessage" %}{% endlanying_code_snippet %}
```
### function setSenderNickname

```cpp
void setSenderNickname(
    const std::string & senderNickname
)
```

Set nickname of sender 

**Parameters**: 

  * **senderNickname** 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="setSenderNickname" %}{% endlanying_code_snippet %}
```
### function getSenderNickname

```cpp
std::string getSenderNickname()
```

Get nickname of sender 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getSenderNickname" %}{% endlanying_code_snippet %}
```
### function setGroupMemberList

```cpp
void setGroupMemberList(
    const std::vector< int64_t > & groupMemberList
)
```

Set the list of member ids that require read group messages 

**Parameters**: 

  * **groupMemberList** 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="setGroupMemberList" %}{% endlanying_code_snippet %}
```
### function getGroupMemberList

```cpp
std::vector< int64_t > getGroupMemberList()
```

Get the list of group member ids that require read group messages 

**Return**: std::vector<int64_t> 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getGroupMemberList" %}{% endlanying_code_snippet %}
```
### function addGroupMember

```cpp
void addGroupMember(
    int64_t id
)
```

Member of group member id list with read messages added 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="addGroupMember" %}{% endlanying_code_snippet %}
```
### function removeGroupMember

```cpp
void removeGroupMember(
    int64_t id
)
```

Empty the list of member ids that require read group messages 

**Return**: std::vector<int64_t> 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="removeGroupMember" %}{% endlanying_code_snippet %}
```
### function clearGroupMemberList

```cpp
void clearGroupMemberList()
```

List of member ids with read group messages emptied 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="clearGroupMemberList" %}{% endlanying_code_snippet %}
```
### function setIOSConfig

```cpp
void setIOSConfig(
    const std::string & iosConfig
)
```

Set IOS system configuration information 

**Parameters**: 

  * **iosConfig** 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="setIOSConfig" %}{% endlanying_code_snippet %}
```
### function getIOSConfig

```cpp
std::string getIOSConfig()
```

Get IOS system configuration information 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getIOSConfig" %}{% endlanying_code_snippet %}
```
### function setAndroidConfig

```cpp
void setAndroidConfig(
    const std::string & androidConfig
)
```

Set Android system configuration information 

**Parameters**: 

  * **androidConfig** 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="setAndroidConfig" %}{% endlanying_code_snippet %}
```
### function getAndroidConfig

```cpp
std::string getAndroidConfig()
```

Get Android system configuration information 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getAndroidConfig" %}{% endlanying_code_snippet %}
```
### function setPushShowBeginTime

```cpp
void setPushShowBeginTime(
    int beginTime
)
```

Set start time for push display 

**Parameters**: 

  * **beginTime** 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="setPushShowBeginTime" %}{% endlanying_code_snippet %}
```
### function getPushShowBeginTime

```cpp
int getPushShowBeginTime()
```

Get start time for push display 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getPushShowBeginTime" %}{% endlanying_code_snippet %}
```
### function setPushShowEndTime

```cpp
void setPushShowEndTime(
    int endTime
)
```

Set end time for push display 

**Parameters**: 

  * **endTime** 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="setPushShowEndTime" %}{% endlanying_code_snippet %}
```
### function getPushShowEndTime

```cpp
int getPushShowEndTime()
```

Get end time for push display 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getPushShowEndTime" %}{% endlanying_code_snippet %}
```
### function setPushTitle

```cpp
void setPushTitle(
    const std::string & pushTitle
)
```

Set push header 

**Parameters**: 

  * **pushTitle** 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="setPushTitle" %}{% endlanying_code_snippet %}
```
### function getPushTitle

```cpp
std::string getPushTitle()
```

Get push header 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getPushTitle" %}{% endlanying_code_snippet %}
```
### function isSilence

```cpp
bool isSilence()
```

Get whether the current push is a silent message 

**Return**: bool 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="isSilence" %}{% endlanying_code_snippet %}
```
### function getBadgeCountType

```cpp
BadgeCountType getBadgeCountType()
```

Get the badge count of the current push 

**Return**: BadgeCountType 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getBadgeCountType" %}{% endlanying_code_snippet %}
```
### function getBadgeCount

```cpp
int getBadgeCount(
    int count
)
```

Get the badge count of the current push 

**Return**: int 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getBadgeCount" %}{% endlanying_code_snippet %}
```
### function setUsername

```cpp
void setUsername(
    const std::string & username
)
```

Set username 

**Parameters**: 

  * **username** 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="setUsername" %}{% endlanying_code_snippet %}
```
### function getUsername

```cpp
std::string getUsername()
```

Get username 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="getUsername" %}{% endlanying_code_snippet %}
```
### function serialize

```cpp
std::string serialize() const
```

Serialization operation 

**Return**: std::string 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="serialize" %}{% endlanying_code_snippet %}
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
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXMessageConfig",function="createMessageConfig" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800