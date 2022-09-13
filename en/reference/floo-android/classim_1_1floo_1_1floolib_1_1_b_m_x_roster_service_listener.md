---
title: im::floo::floolib::BMXRosterServiceListener
summary: Friend change listener 

---

# im::floo::floolib::BMXRosterServiceListener



Friend change listener 

## Public Functions

|                | Name           |
| -------------- | -------------- |
| synchronized void | **[delete](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-delete)**() |
| void | **[swigReleaseOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-swigreleaseownership)**() |
| void | **[swigTakeOwnership](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-swigtakeownership)**() |
| void | **[onFriendAdded](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onfriendadded)**(long sponsorId, long recipientId)<br>Add friend  |
| void | **[onFriendRemoved](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onfriendremoved)**(long sponsorId, long recipientId)<br>Delete friend  |
| void | **[onApplied](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onapplied)**(long sponsorId, long recipientId, String message)<br>Request of adding friend received  |
| void | **[onApplicationAccepted](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onapplicationaccepted)**(long sponsorId, long recipientId)<br>Request of adding friend approved  |
| void | **[onApplicationDeclined](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onapplicationdeclined)**(long sponsorId, long recipientId, String reason)<br>Request of adding friend rejected  |
| void | **[onBlockListAdded](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onblocklistadded)**(long sponsorId, long recipientId)<br>Add to blacklist  |
| void | **[onBlockListRemoved](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onblocklistremoved)**(long sponsorId, long recipientId)<br>Delete blacklist  |
| void | **[onRosterInfoUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onrosterinfoupdate)**([BMXRosterItem](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_item.md) item)<br>Update user information  |
| void | **[onRosterListUpdate](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-onrosterlistupdate)**()<br>Triggered when client pulls new contact from server, used to update user contact list, and call local fetching contact via SDK for all member information  |
| | **[BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-bmxrosterservicelistener)**() |
| void | **[registerRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-registerrosterservice)**([BMXRosterService](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service.md) service) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-bmxrosterservicelistener)**(long cPtr, boolean cMemoryOwn) |
| void | **[finalize](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-finalize)**() |
| void | **[swigDirectorDisconnect](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-swigdirectordisconnect)**() |
| long | **[getCPtr](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#function-getcptr)**([BMXRosterServiceListener](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md) obj) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| transient boolean | **[swigCMemOwn](classim_1_1floo_1_1floolib_1_1_b_m_x_roster_service_listener.md#variable-swigcmemown)**  |

## Public Functions Documentation

### function delete

```java
inline synchronized void delete()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="delete" %}{% endlanying_code_snippet %}
```
### function swigReleaseOwnership

```java
inline void swigReleaseOwnership()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="swigReleaseOwnership" %}{% endlanying_code_snippet %}
```
### function swigTakeOwnership

```java
inline void swigTakeOwnership()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="swigTakeOwnership" %}{% endlanying_code_snippet %}
```
### function onFriendAdded

```java
inline void onFriendAdded(
    long sponsorId,
    long recipientId
)
```

Add friend 

**Parameters**: 

  * **sponsorId** Operation initiator 
  * **recipientId** Operation recipient 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="onFriendAdded" %}{% endlanying_code_snippet %}
```
### function onFriendRemoved

```java
inline void onFriendRemoved(
    long sponsorId,
    long recipientId
)
```

Delete friend 

**Parameters**: 

  * **sponsorId** Operation initiator 
  * **recipientId** Operation recipient 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="onFriendRemoved" %}{% endlanying_code_snippet %}
```
### function onApplied

```java
inline void onApplied(
    long sponsorId,
    long recipientId,
    String message
)
```

Request of adding friend received 

**Parameters**: 

  * **sponsorId** Operation initiator 
  * **recipientId** Operation recipient 
  * **message** Friend request message 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="onApplied" %}{% endlanying_code_snippet %}
```
### function onApplicationAccepted

```java
inline void onApplicationAccepted(
    long sponsorId,
    long recipientId
)
```

Request of adding friend approved 

**Parameters**: 

  * **sponsorId** Operation initiator 
  * **recipientId** Operation recipient 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="onApplicationAccepted" %}{% endlanying_code_snippet %}
```
### function onApplicationDeclined

```java
inline void onApplicationDeclined(
    long sponsorId,
    long recipientId,
    String reason
)
```

Request of adding friend rejected 

**Parameters**: 

  * **sponsorId** Operation initiator 
  * **recipientId** Operation recipient 
  * **reason** Reason for application rejection 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="onApplicationDeclined" %}{% endlanying_code_snippet %}
```
### function onBlockListAdded

```java
inline void onBlockListAdded(
    long sponsorId,
    long recipientId
)
```

Add to blacklist 

**Parameters**: 

  * **sponsorId** Operation initiator 
  * **recipientId** Operation recipient 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="onBlockListAdded" %}{% endlanying_code_snippet %}
```
### function onBlockListRemoved

```java
inline void onBlockListRemoved(
    long sponsorId,
    long recipientId
)
```

Delete blacklist 

**Parameters**: 

  * **sponsorId** Operation initiator 
  * **recipientId** Operation recipient 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="onBlockListRemoved" %}{% endlanying_code_snippet %}
```
### function onRosterInfoUpdate

```java
inline void onRosterInfoUpdate(
    BMXRosterItem item
)
```

Update user information 

**Parameters**: 

  * **item** Updated friend information 


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="onRosterInfoUpdate" %}{% endlanying_code_snippet %}
```
### function onRosterListUpdate

```java
inline void onRosterListUpdate()
```

Triggered when client pulls new contact from server, used to update user contact list, and call local fetching contact via SDK for all member information 

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="onRosterListUpdate" %}{% endlanying_code_snippet %}
```
### function BMXRosterServiceListener

```java
inline BMXRosterServiceListener()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="BMXRosterServiceListener" %}{% endlanying_code_snippet %}
```
### function registerRosterService

```java
inline void registerRosterService(
    BMXRosterService service
)
```


## Protected Functions Documentation

**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="registerRosterService" %}{% endlanying_code_snippet %}
```
### function BMXRosterServiceListener

```java
inline BMXRosterServiceListener(
    long cPtr,
    boolean cMemoryOwn
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="BMXRosterServiceListener" %}{% endlanying_code_snippet %}
```
### function finalize

```java
inline void finalize()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="finalize" %}{% endlanying_code_snippet %}
```
### function swigDirectorDisconnect

```java
inline void swigDirectorDisconnect()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="swigDirectorDisconnect" %}{% endlanying_code_snippet %}
```
### function getCPtr

```java
static inline long getCPtr(
    BMXRosterServiceListener obj
)
```


## Protected Attributes Documentation

### variable swigCMemOwn

```java
transient boolean swigCMemOwn;
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-android",class="BMXRosterServiceListener",function="getCPtr" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:18:31 +0800