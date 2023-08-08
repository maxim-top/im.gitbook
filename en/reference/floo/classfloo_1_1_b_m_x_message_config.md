---
title: floo::BMXMessageConfig
summary: Message configuration
---

# floo::BMXMessageConfig

Message configuration

`#include <bmx_message_config.h>`

Inherits from BMXBaseObject

## Public Types

|            | Name                                                                                                                                                                               |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enum class | <p><a href="classfloo_1_1_b_m_x_message_config.md#enum-badgecounttype"><strong>BadgeCountType</strong></a> { Change, Set}<br>Operation type of the currently read Badge number</p> |

## Public Functions

|                                                                                    | Name                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| virtual                                                                            | [**\~BMXMessageConfig**](classfloo\_1\_1\_b\_m\_x\_message\_config.md#function-\~bmxmessageconfig)()                                                                                                                                                |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setmentionall"><strong>setMentionAll</strong></a>(bool mentionAll)<br>Set whether to @ all members</p>                                                                                   |
| bool                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getmentionall"><strong>getMentionAll</strong></a>()<br>Get whether to @ all members</p>                                                                                                  |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setmentionlist"><strong>setMentionList</strong></a>(const std::vector&#x3C; int64_t > &#x26; mentionList)<br>Set the list of notified member ids</p>                                     |
| std::vector< int64\_t >                                                            | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getmentionlist"><strong>getMentionList</strong></a>()<br>Get @ member list</p>                                                                                                           |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setmentionedmessage"><strong>setMentionedMessage</strong></a>(const std::string &#x26; mentionedMessage)<br>Set @ message</p>                                                            |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getmentionedmessage"><strong>getMentionedMessage</strong></a>()<br>Get @ message</p>                                                                                                     |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setpushmessage"><strong>setPushMessage</strong></a>(const std::string &#x26; pushMessage)<br>Set push message</p>                                                                        |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getpushmessage"><strong>getPushMessage</strong></a>()<br>Get push message</p>                                                                                                            |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setsendernickname"><strong>setSenderNickname</strong></a>(const std::string &#x26; senderNickname)<br>Set nickname of sender</p>                                                         |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getsendernickname"><strong>getSenderNickname</strong></a>()<br>Get nickname of sender</p>                                                                                                |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setgroupmemberlist"><strong>setGroupMemberList</strong></a>(const std::vector&#x3C; int64_t > &#x26; groupMemberList)<br>Set the list of member ids that require read group messages</p> |
| std::vector< int64\_t >                                                            | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getgroupmemberlist"><strong>getGroupMemberList</strong></a>()<br>Get the list of group member ids that require read group messages</p>                                                   |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-addgroupmember"><strong>addGroupMember</strong></a>(int64_t id)<br>Member of group member id list with read messages added</p>                                                           |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-removegroupmember"><strong>removeGroupMember</strong></a>(int64_t id)<br>Empty the list of member ids that require read group messages</p>                                               |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-cleargroupmemberlist"><strong>clearGroupMemberList</strong></a>()<br>List of member ids with read group messages emptied</p>                                                             |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setiosconfig"><strong>setIOSConfig</strong></a>(const std::string &#x26; iosConfig)<br>Set IOS system configuration information</p>                                                      |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getiosconfig"><strong>getIOSConfig</strong></a>()<br>Get IOS system configuration information</p>                                                                                        |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setandroidconfig"><strong>setAndroidConfig</strong></a>(const std::string &#x26; androidConfig)<br>Set Android system configuration information</p>                                      |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getandroidconfig"><strong>getAndroidConfig</strong></a>()<br>Get Android system configuration information</p>                                                                            |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setpushshowbegintime"><strong>setPushShowBeginTime</strong></a>(int beginTime)<br>Set start time for push display</p>                                                                    |
| int                                                                                | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getpushshowbegintime"><strong>getPushShowBeginTime</strong></a>()<br>Get start time for push display</p>                                                                                 |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setpushshowendtime"><strong>setPushShowEndTime</strong></a>(int endTime)<br>Set end time for push display</p>                                                                            |
| int                                                                                | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getpushshowendtime"><strong>getPushShowEndTime</strong></a>()<br>Get end time for push display</p>                                                                                       |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setpushtitle"><strong>setPushTitle</strong></a>(const std::string &#x26; pushTitle)<br>Set push header</p>                                                                               |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getpushtitle"><strong>getPushTitle</strong></a>()<br>Get push header</p>                                                                                                                 |
| bool                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-issilence"><strong>isSilence</strong></a>()<br>Get whether the current push is a silent message</p>                                                                                      |
| [BadgeCountType](classfloo\_1\_1\_b\_m\_x\_message\_config.md#enum-badgecounttype) | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getbadgecounttype"><strong>getBadgeCountType</strong></a>()<br>Get the badge count of the current push</p>                                                                               |
| int                                                                                | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getbadgecount"><strong>getBadgeCount</strong></a>(int count)<br>Get the badge count of the current push</p>                                                                              |
| void                                                                               | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-setusername"><strong>setUsername</strong></a>(const std::string &#x26; username)<br>Set username</p>                                                                                     |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-getusername"><strong>getUsername</strong></a>()<br>Get username</p>                                                                                                                      |
| std::string                                                                        | <p><a href="classfloo_1_1_b_m_x_message_config.md#function-serialize"><strong>serialize</strong></a>() const<br>Serialization operation</p>                                                                                                         |
| BMXMessageConfigPtr                                                                | [**createMessageConfig**](classfloo\_1\_1\_b\_m\_x\_message\_config.md#function-createmessageconfig)(bool mentionAll)                                                                                                                               |

## Friends

|                     | Name                                                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| std::string         | [**encodeBMXMessageConfig**](classfloo\_1\_1\_b\_m\_x\_message\_config.md#friend-encodebmxmessageconfig)(BMXMessageConfigPtr )       |
| BMXMessageConfigPtr | [**decodeBMXMessageConfig**](classfloo\_1\_1\_b\_m\_x\_message\_config.md#friend-decodebmxmessageconfig)(const std::string & config) |

## Public Types Documentation

### enum BadgeCountType

| Enumerator | Value | Description                                                                                                                             |
| ---------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Change     |       | The type of operation to read the Badge count is increment or decrement. Positive number is increment and negative number is decrement. |
| Set        |       | Set the Badge count to the current count                                                                                                |

Operation type of the currently read Badge number

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

Set whether to @ all members

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

Get whether to @ all members

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

Set the list of notified member ids

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

Get @ member list

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

Set @ message

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

Get @ message

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

Set push message

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

Get push message

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

Set nickname of sender

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

Get nickname of sender

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

Set the list of member ids that require read group messages

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

Get the list of group member ids that require read group messages

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

Member of group member id list with read messages added

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

Empty the list of member ids that require read group messages

**Return**: std::vector\<int64\_t>

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function clearGroupMemberList

```cpp
void clearGroupMemberList()
```

List of member ids with read group messages emptied

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

Set IOS system configuration information

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

Get IOS system configuration information

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

Set Android system configuration information

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

Get Android system configuration information

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

Set start time for push display

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

Get start time for push display

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

Set end time for push display

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

Get end time for push display

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

Set push header

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

Get push header

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function isSilence

```cpp
bool isSilence()
```

Get whether the current push is a silent message

**Return**: bool

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function getBadgeCountType

```cpp
BadgeCountType getBadgeCountType()
```

Get the badge count of the current push

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

Get the badge count of the current push

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

Set username

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

Get username

**Return**: std::string

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXMessageConfig'></div>
```

### function serialize

```cpp
std::string serialize() const
```

Serialization operation

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
