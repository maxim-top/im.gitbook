---
title: floo::BMXMessageConfig
summary: 消息配置 

---

# floo::BMXMessageConfig



消息配置 


`#include <bmx_message_config.h>`

Inherits from BMXBaseObject

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum class| **[BadgeCountType](classfloo_1_1_b_m_x_message_config.md#enum-badgecounttype)** { Change, Set}<br>当前读取的Badge数字的操作类型  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXMessageConfig](classfloo_1_1_b_m_x_message_config.md#function-~bmxmessageconfig)**() |
| void | **[setMentionAll](classfloo_1_1_b_m_x_message_config.md#function-setmentionall)**(bool mentionAll)<br>设置是否@全员  |
| bool | **[getMentionAll](classfloo_1_1_b_m_x_message_config.md#function-getmentionall)**()<br>获取是否@全员  |
| void | **[setMentionList](classfloo_1_1_b_m_x_message_config.md#function-setmentionlist)**(const std::vector< int64_t > & mentionList)<br>设置通知成员id列表  |
| std::vector< int64_t > | **[getMentionList](classfloo_1_1_b_m_x_message_config.md#function-getmentionlist)**()<br>获取@成员列表  |
| void | **[setMentionedMessage](classfloo_1_1_b_m_x_message_config.md#function-setmentionedmessage)**(const std::string & mentionedMessage)<br>设置@消息  |
| std::string | **[getMentionedMessage](classfloo_1_1_b_m_x_message_config.md#function-getmentionedmessage)**()<br>获取@消息  |
| void | **[setPushMessage](classfloo_1_1_b_m_x_message_config.md#function-setpushmessage)**(const std::string & pushMessage)<br>设置推送消息  |
| std::string | **[getPushMessage](classfloo_1_1_b_m_x_message_config.md#function-getpushmessage)**()<br>获取推送消息  |
| void | **[setSenderNickname](classfloo_1_1_b_m_x_message_config.md#function-setsendernickname)**(const std::string & senderNickname)<br>设置发送者昵称  |
| std::string | **[getSenderNickname](classfloo_1_1_b_m_x_message_config.md#function-getsendernickname)**()<br>获取发送者昵称  |
| void | **[setGroupMemberList](classfloo_1_1_b_m_x_message_config.md#function-setgroupmemberlist)**(const std::vector< int64_t > & groupMemberList)<br>设置需要群已读消息的群成员id列表  |
| std::vector< int64_t > | **[getGroupMemberList](classfloo_1_1_b_m_x_message_config.md#function-getgroupmemberlist)**()<br>获取需要群已读消息的群成员id列表  |
| void | **[addGroupMember](classfloo_1_1_b_m_x_message_config.md#function-addgroupmember)**(int64_t id)<br>添加群已读消息的群成员id列表成员  |
| void | **[removeGroupMember](classfloo_1_1_b_m_x_message_config.md#function-removegroupmember)**(int64_t id)<br>清除需要群已读消息的群成员id列表成员  |
| void | **[clearGroupMemberList](classfloo_1_1_b_m_x_message_config.md#function-cleargroupmemberlist)**()<br>清空群已读消息的群成员id列表  |
| void | **[setIOSConfig](classfloo_1_1_b_m_x_message_config.md#function-setiosconfig)**(const std::string & iosConfig)<br>设置IOS系统配置信息  |
| std::string | **[getIOSConfig](classfloo_1_1_b_m_x_message_config.md#function-getiosconfig)**()<br>获取IOS系统配置信息  |
| void | **[setAndroidConfig](classfloo_1_1_b_m_x_message_config.md#function-setandroidconfig)**(const std::string & androidConfig)<br>设置Android系统配置信息  |
| std::string | **[getAndroidConfig](classfloo_1_1_b_m_x_message_config.md#function-getandroidconfig)**()<br>获取Android系统配置信息  |
| void | **[setPushShowBeginTime](classfloo_1_1_b_m_x_message_config.md#function-setpushshowbegintime)**(int beginTime)<br>设置推送显示开始时间  |
| int | **[getPushShowBeginTime](classfloo_1_1_b_m_x_message_config.md#function-getpushshowbegintime)**()<br>获取推送显示开始时间  |
| void | **[setPushShowEndTime](classfloo_1_1_b_m_x_message_config.md#function-setpushshowendtime)**(int endTime)<br>设置推送显示结束时间  |
| int | **[getPushShowEndTime](classfloo_1_1_b_m_x_message_config.md#function-getpushshowendtime)**()<br>获取推送显示结束时间  |
| void | **[setPushTitle](classfloo_1_1_b_m_x_message_config.md#function-setpushtitle)**(const std::string & pushTitle)<br>设置推送标题  |
| std::string | **[getPushTitle](classfloo_1_1_b_m_x_message_config.md#function-getpushtitle)**()<br>获取推送标题  |
| bool | **[isSilence](classfloo_1_1_b_m_x_message_config.md#function-issilence)**()<br>获取当前的推送消息是否是静默消息  |
| [BadgeCountType](classfloo_1_1_b_m_x_message_config.md#enum-badgecounttype) | **[getBadgeCountType](classfloo_1_1_b_m_x_message_config.md#function-getbadgecounttype)**()<br>获取当前的推送消息中badge计数  |
| int | **[getBadgeCount](classfloo_1_1_b_m_x_message_config.md#function-getbadgecount)**(int count)<br>获取当前的推送消息中badge计数  |
| void | **[setUsername](classfloo_1_1_b_m_x_message_config.md#function-setusername)**(const std::string & username)<br>设置用户名  |
| std::string | **[getUsername](classfloo_1_1_b_m_x_message_config.md#function-getusername)**()<br>获得用户名  |
| std::string | **[serialize](classfloo_1_1_b_m_x_message_config.md#function-serialize)**() const<br>序列化操作  |
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
| Change | | 读取Badge计数的操作类型为增加或减少。正数为增加负数为减少   |
| Set | | 设置Badge的计数为当前的计数值   |



当前读取的Badge数字的操作类型 

## Public Functions Documentation

### function ~BMXMessageConfig

```cpp
inline virtual ~BMXMessageConfig()
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


### function getMentionAll

```cpp
bool getMentionAll()
```

获取是否@全员 

**Return**: bool 

### function setMentionList

```cpp
void setMentionList(
    const std::vector< int64_t > & mentionList
)
```

设置通知成员id列表 

**Parameters**: 

  * **mentionList** 


### function getMentionList

```cpp
std::vector< int64_t > getMentionList()
```

获取@成员列表 

**Return**: std::vector<int64_t> 

### function setMentionedMessage

```cpp
void setMentionedMessage(
    const std::string & mentionedMessage
)
```

设置@消息 

**Parameters**: 

  * **mentionedMessage** 


### function getMentionedMessage

```cpp
std::string getMentionedMessage()
```

获取@消息 

**Return**: std::string 

### function setPushMessage

```cpp
void setPushMessage(
    const std::string & pushMessage
)
```

设置推送消息 

**Parameters**: 

  * **pushMessage** 


### function getPushMessage

```cpp
std::string getPushMessage()
```

获取推送消息 

**Return**: std::string 

### function setSenderNickname

```cpp
void setSenderNickname(
    const std::string & senderNickname
)
```

设置发送者昵称 

**Parameters**: 

  * **senderNickname** 


### function getSenderNickname

```cpp
std::string getSenderNickname()
```

获取发送者昵称 

**Return**: std::string 

### function setGroupMemberList

```cpp
void setGroupMemberList(
    const std::vector< int64_t > & groupMemberList
)
```

设置需要群已读消息的群成员id列表 

**Parameters**: 

  * **groupMemberList** 


### function getGroupMemberList

```cpp
std::vector< int64_t > getGroupMemberList()
```

获取需要群已读消息的群成员id列表 

**Return**: std::vector<int64_t> 

### function addGroupMember

```cpp
void addGroupMember(
    int64_t id
)
```

添加群已读消息的群成员id列表成员 

### function removeGroupMember

```cpp
void removeGroupMember(
    int64_t id
)
```

清除需要群已读消息的群成员id列表成员 

**Return**: std::vector<int64_t> 

### function clearGroupMemberList

```cpp
void clearGroupMemberList()
```

清空群已读消息的群成员id列表 

### function setIOSConfig

```cpp
void setIOSConfig(
    const std::string & iosConfig
)
```

设置IOS系统配置信息 

**Parameters**: 

  * **iosConfig** 


### function getIOSConfig

```cpp
std::string getIOSConfig()
```

获取IOS系统配置信息 

**Return**: std::string 

### function setAndroidConfig

```cpp
void setAndroidConfig(
    const std::string & androidConfig
)
```

设置Android系统配置信息 

**Parameters**: 

  * **androidConfig** 


### function getAndroidConfig

```cpp
std::string getAndroidConfig()
```

获取Android系统配置信息 

**Return**: std::string 

### function setPushShowBeginTime

```cpp
void setPushShowBeginTime(
    int beginTime
)
```

设置推送显示开始时间 

**Parameters**: 

  * **beginTime** 


### function getPushShowBeginTime

```cpp
int getPushShowBeginTime()
```

获取推送显示开始时间 

**Return**: int 

### function setPushShowEndTime

```cpp
void setPushShowEndTime(
    int endTime
)
```

设置推送显示结束时间 

**Parameters**: 

  * **endTime** 


### function getPushShowEndTime

```cpp
int getPushShowEndTime()
```

获取推送显示结束时间 

**Return**: int 

### function setPushTitle

```cpp
void setPushTitle(
    const std::string & pushTitle
)
```

设置推送标题 

**Parameters**: 

  * **pushTitle** 


### function getPushTitle

```cpp
std::string getPushTitle()
```

获取推送标题 

**Return**: std::string 

### function isSilence

```cpp
bool isSilence()
```

获取当前的推送消息是否是静默消息 

**Return**: bool 

### function getBadgeCountType

```cpp
BadgeCountType getBadgeCountType()
```

获取当前的推送消息中badge计数 

**Return**: BadgeCountType 

### function getBadgeCount

```cpp
int getBadgeCount(
    int count
)
```

获取当前的推送消息中badge计数 

**Return**: int 

### function setUsername

```cpp
void setUsername(
    const std::string & username
)
```

设置用户名 

**Parameters**: 

  * **username** 


### function getUsername

```cpp
std::string getUsername()
```

获得用户名 

**Return**: std::string 

### function serialize

```cpp
std::string serialize() const
```

序列化操作 

**Return**: std::string 

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


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800