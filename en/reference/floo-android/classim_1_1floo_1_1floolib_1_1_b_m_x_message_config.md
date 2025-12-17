---
title: im::floo::floolib::BMXMessageConfig
summary: Message configuration
---

# im::floo::floolib::BMXMessageConfig

Message configuration

Inherits from BMXBaseObject

## Public Functions

|                                                                            | Name                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| synchronized void                                                          | [**delete**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-delete)()                                                                                                                                                     |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setmentionall"><strong>setMentionAll</strong></a>(boolean mentionAll)<br>Set whether to @ all members</p>                                                      |
| boolean                                                                    | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getmentionall"><strong>getMentionAll</strong></a>()<br>Get whether to @ all members</p>                                                                        |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setmentionlist"><strong>setMentionList</strong></a>(ListOfLongLong mentionList)<br>Set the list of notified member ids</p>                                     |
| ListOfLongLong                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getmentionlist"><strong>getMentionList</strong></a>()<br>Get @ member list</p>                                                                                 |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setmentionedmessage"><strong>setMentionedMessage</strong></a>(String mentionedMessage)<br>Set @ message</p>                                                    |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getmentionedmessage"><strong>getMentionedMessage</strong></a>()<br>Get @ message</p>                                                                           |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushmessage"><strong>setPushMessage</strong></a>(String pushMessage)<br>Set push message</p>                                                                |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushmessage"><strong>getPushMessage</strong></a>()<br>Get push message</p>                                                                                  |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setsendernickname"><strong>setSenderNickname</strong></a>(String senderNickname)<br>Set nickname of sender</p>                                                 |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getsendernickname"><strong>getSenderNickname</strong></a>()<br>Get nickname of sender</p>                                                                      |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setgroupmemberlist"><strong>setGroupMemberList</strong></a>(ListOfLongLong groupMemberList)<br>Set the list of member ids that require read group messages</p> |
| ListOfLongLong                                                             | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getgroupmemberlist"><strong>getGroupMemberList</strong></a>()<br>Get the list of group member ids that require read group messages</p>                         |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-addgroupmember"><strong>addGroupMember</strong></a>(long id)<br>Member of group member id list with read messages added</p>                                    |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-removegroupmember"><strong>removeGroupMember</strong></a>(long id)<br>Empty the list of member ids that require read group messages</p>                        |
| void                                                                       | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-cleargroupmemberlist"><strong>clearGroupMemberList</strong></a>()<br>List of member ids with read group messages emptied</p>                                   |
| void                                                                       | [**setIOSConfig**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setiosconfig)(String iosConfig)                                                                                                                         |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getiosconfig"><strong>getIOSConfig</strong></a>()<br>Get iOS message configuration</p>                                                                         |
| void                                                                       | [**setAndroidConfig**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setandroidconfig)(String androidConfig)                                                                                                             |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getandroidconfig"><strong>getAndroidConfig</strong></a>()<br>Get Android message configuration</p>                                                             |
| void                                                                       | [**setPushShowBeginTime**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushshowbegintime)(int beginTime)                                                                                                            |
| int                                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushshowbegintime"><strong>getPushShowBeginTime</strong></a>()<br>Get start time of push message displayed</p>                                              |
| void                                                                       | [**setPushShowEndTime**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushshowendtime)(int endTime)                                                                                                                  |
| int                                                                        | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushshowendtime"><strong>getPushShowEndTime</strong></a>()<br>Get end time of push message displayed</p>                                                    |
| void                                                                       | [**setPushTitle**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-setpushtitle)(String pushTitle)                                                                                                                         |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getpushtitle"><strong>getPushTitle</strong></a>()<br>Get tittle of push message</p>                                                                            |
| boolean                                                                    | [**isSilence**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-issilence)()                                                                                                                                               |
| BMXMessageConfig.BadgeCountType                                            | [**getBadgeCountType**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getbadgecounttype)()                                                                                                                               |
| int                                                                        | [**getBadgeCount**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getbadgecount)(int count)                                                                                                                              |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-getusername"><strong>getUsername</strong></a>()<br>Get username of message sender</p>                                                                          |
| String                                                                     | <p><a href="classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-serialize"><strong>serialize</strong></a>()<br>Serialization operation</p>                                                                                     |
| [BMXMessageConfig](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md) | [**createMessageConfig**](classim_1_1floo_1_1floolib_1_1_b_m_x_message_config.md#function-createmessageconfig)(boolean mentionAll)                                                                                                         |

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

Set whether to @ all members

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

Get whether to @ all members

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

Set the list of notified member ids

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

Get @ member list

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

Set @ message

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

Get @ message

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

Set push message

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

Get push message

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

Set nickname of sender

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

Get nickname of sender

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

Set the list of member ids that require read group messages

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

Get the list of group member ids that require read group messages

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

Member of group member id list with read messages added

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

Empty the list of member ids that require read group messages

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function clearGroupMemberList

```java
inline void clearGroupMemberList()
```

List of member ids with read group messages emptied

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

Get iOS message configuration

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

Get Android message configuration

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

Get start time of push message displayed

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

Get end time of push message displayed

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

Get tittle of push message

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

Get username of message sender

**Example**:

```

<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-android' data-class='BMXMessageConfig'></div>

```

### function serialize

```java
inline String serialize()
```

Serialization operation

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
