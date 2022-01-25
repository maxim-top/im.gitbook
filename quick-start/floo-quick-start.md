# C++ SDK (floo) Quick integration指南

This page is for quick integration, visit[detailed documentation](https://maximtop.com/docs/floo)

## SDK overall architecture

SDK architecture description

* BMXClient:SDK function aggregation class that contains all service classes and implements the network event listening interface.
* BMXChatService: Message sending, message history retrieval, session list
* BMXUserService: Register account, login, logout, my settings
* BMXRosterService: Friend list, blacklist
* BMXGroupService: Group management (create, dissolve, search, set, member management, invite, apply, accept, reject)
* BMXChatServiceListener: Message delivery event, message sent result event listening
* BMXGroupServiceListener: Group event listening
* BMXUserServiceListener: User event listening
* BMXRosterServiceListener: Friend event listening
* BMXNetworkListener: Network event listening interface, implemented by BMXClient
* BMXConversation: Session
* BMXMessage: Message
* BMXGroup: Group
* BMXRosterItem Roster item (friend, stranger, blacklist, former friend)
* BMXUserProfile: User information

Relationship among main classes is as follows:

```
>BMXClient
>|----BMXNetworkListener
>|----BMXChatService
>    |----BMXChatServiceListener
>    |----BMXConversation
>    |----BMXMessage
>|----BMXUserService
>    |----BMXUserServiceListener
>    |----BMXUserProfile
>|----BMXRosterService
>    |----BMXRosterServiceListener
>    |----BMXRosterItem
>|----BMXGroupService
>    |----BMXGroupServiceListener
>    |----BMXGroup
```

## SDK integration

1. SDK document description
2. Add system library dependencies Before import SDK in your project, you need to add following system library references.

* libz decompression library
* libcrypto openssl encryption library
* libsqlite3 sqlite3 local database
* lcurl libcurl network library
* lcurses ncurses library, which is required to run the embedded version of our demo

### I. Initialize, import of related header file

```
#include "bmx_client.h"
config = BMXSDKConfigPtr(new BMXSDKConfig(BMXClientType::macOS, "10", "./data", "./data", "2.0", "1234", "userAgent"));
config->setAppID("dxgeuidhhutk");
config->setDeviceUuid("b81f412e-fcb2-44fb-9f44-5e8e5b1e809e");
config->setConsoleOutput(false);
client = BMXClient::create(config);
```

### II. Register user

```
BMXUserProfilePtr profile;
BMXErrorCode errorCode = config->getUserService().signUpNewUser("maximtest1", "123456", "1", profile);
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "signUpNewUser successs!" << std::endl;
} else {
  std::cout << "signUpNewUser failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

### III. Login connected server

Pass the account password you obtained in the previous step into the -signInById method through the UserService class, a singleton of BMXClient, to establish a connection with the server.

Two login modes provided: One for normal manual login, and the other for quick login

```
BMXErrorCode errorCode = client->getUserService().signInByName("maximtest1", "1");
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "signInByName successs!" << std::endl;
} else {
  std::cout << "signInByName failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}

// Quick login needs no getting token
BMXErrorCode errorCode = client->getUserService().fastSignInByName("maximtest1", "1");
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "signInByName successs!" << std::endl;
} else {
  std::cout << "signInByName failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

### IV. Get session list

Get a list of all sessions through the singleton of BMXClient, getAllConversations method of ChatService class. It returns an array list of BMXConversationPtr objects.

If you need to get a list of offline sessions for multi-device synchronization, it’s required to configure the setLoadAllServerConversations property value to true at SDK initialization, and only get the local session list by default.

```
BMXConversationList list = client->getChatService().getAllConversations();
```

### V. Disconnect

When you disconnect from MaxIM server, it stops receiving later messages by default.

```
BMXErrorCode errorCode = client->getChatService().signOut();
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "signInByName successs!" << std::endl;
} else {
  std::cout << "signInByName failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

## User friend system

* Add friend

```
BMXErrorCode errorCode = client->getRosterService().apply(rosterId, "apply");
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "apply successs!" << std::endl;
} else {
  std::cout << "apply failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

* Delete friend

```
BMXErrorCode errorCode = client->getRosterService().remove(rosterId);
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "remove successs!" << std::endl;
} else {
  std::cout << "remove failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

* Agree to add friend

```
BMXErrorCode errorCode = client->getRosterService().accept(rosterId);
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "accept successs!" << std::endl;
} else {
  std::cout << "accept failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

* Reject to add friend

```
BMXErrorCode errorCode = client->getRosterService().decline(rosterId, "reason");
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "decline successs!" << std::endl;
} else {
  std::cout << "decline failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

* Get friend list

Developers can choose to get friend list data from server or locally with the forceRefresh parameter. If it is set to NO, when the local data is empty, it will automatically get the data from server and return the result.

```
std::vector<int64_t> list;
BMXErrorCode errorCode = client->getRosterService().get(list, true);
if (list.size() > 0) {
  cout << list[0] << endl;
}
```

## Basic features

### Message format

* Text
* Emoji
* Voice clip
* Video clip
* Image
* Geo-location
* Custom message

### Single chat

Single chat is the most basic chat interface, which provides a variety of input contents such as text, emoji, voice clip, image, etc., and solves the communication bottleneck of users in App. BMXConversationType of single chat is BMXConversationSingle, and toId is userId of single chat object.

### Group chat

Group chat refers to the chat function of internal broadcast mode in the user set with roles and permissions. BMXConversationType of group is BMXConversationGroup, and toId is group Id.

* Create group

Developers can register to listener, then receive corresponding callback notifications after group created, thus do some UI processing.

```
BMXGroupPtr group;
BMXGroupService::CreateGroupOptions options("Test", "Test", "Test");
BMXErrorCode errorCode = client->getGroupService().create(options, group);
if (BMXErrorCode::NoError == errorCode) {
  std::cout << "create group successs!" << std::endl;
} else {
  std::cout << "create group failure!" << std::endl;
  std::cout << getErrorMessage(errorCode) << std::endl;
}
```

* Join group

```
BMXErrorCode errorCode = client->getGroupService().join(group, message);
```

* Quit group

```
BMXErrorCode errorCode = client->getGroupService().leave(group);
```

* Dissolve group

```
BMXErrorCode errorCode = client->getGroupService().destroy(group);
```

* Get group member list

```
BMXGroupMemberResultPagePtr result;
std::string cursor = "";
int pageSize = 100;

do {
  errorCode = client->getGroupService().getMembers(group, result, cursor, pageSize);
  cursor = result->cursor();
  for (auto member : result->result()) {
    cout << member->mUid << endl;
  }
} while (cursor.size());
```

* Get group list

```
@param list Group id list, pass in an empty list function and fetch the returned group id list here.
@param forceRefresh True to force fetching from server, sdk will automatically fetch from server if local fetching failed.
BMXGroupList list;
bool forceRefresh = false;
BMXErrorCode errorCode = client->getGroupService().search(list, forceRefresh);
```

* Get group information

```
BMXGroupPtr group;
errorCode = client->getGroupService().search(groupId, group, true);
```

## Message sending

You can't chat until login successfully. When sending messages, single chat and group chat call the same unified interface, but the only difference is to set BMXConversationType.

### Build message body

* Text message

```
/**
  * @param from Message sender Id
  * @param to Message receiver Id
  * @param type Message type
  * @param conversationId Session id
  * @param content Message content
  **/
  BMXMessagePtr msg = BMXMessage::createMessage(2272061685216, 2272061881760, (BMXMessage::MessageType)1, 2272061881760, "test");
```

* Image message

```
/**
  * @param path Local path
  * @param size Image size, width and height
  * @param displayName Display name
  **/
BMXImageAttachmentPtr attachment(new BMXImageAttachment(path, size, displayName));
BMXMessagePtr msg = BMXMessage::createMessage(2272061685216, 2272061881760, (BMXMessage::MessageType)1, 2272061881760, attachment);
```

* File message

```
BMXFileAttachmentPtr attachment(new BMXFileAttachment(path, displayName));
BMXMessagePtr msg = BMXMessage::createMessage(2272061685216, 2272061881760, (BMXMessage::MessageType)1, 2272061881760, attachment);
```

* Location message

```
BMXLocationAttachmentPtr attachment(new BMXLocationAttachment(latitude, longitude, address));
BMXMessagePtr msg = BMXMessage::createMessage(2272061685216, 2272061881760, (BMXMessage::MessageType)1, 2272061881760, attachment);
```

* Voice message

```
BMXVoiceAttachmentPtr attachment(new BMXVoiceAttachmentPtr(path, duration, displayName));
BMXMessagePtr msg = BMXMessage::createMessage(2272061685216, 2272061881760, (BMXMessage::MessageType)1, 2272061881760, attachment);
```

* Video-message

```
BMXVideoAttachmentPtr attachment(new BMXVideoAttachment(path, duration, size, displayName));
BMXMessagePtr msg = BMXMessage::createMessage(2272061685216, 2272061881760, (BMXMessage::MessageType)1, 2272061881760, attachment);
```

### Message operation

After message body is built, call the sendMessage: method through the singleton of BMXClient, ChatService class, and pass in the built message body, so that the message can be sent. Message status changes are notified by a listener callback of the registered BMXChatServiceListener type.

* Send

```
client->getChatService().sendMessage(msg);
```

* Forward

```
BMXMessagePtr forwardMsg = BMXMessage::createForwardMessage(msg, from, to, type, conversationId);
client->getChatService().forwardMessage(msg);
```

* Resend

```
client->getChatService().resendMessage(msg);
```

* Revoke

```
client->getChatService().recallMessage(msg);
```

* Download message attachment

```
client->getChatService().downloadAttachment(msg);
```

### Message delivery listening

Register message callback

```
client->getChatService().addChatListener(listener); //Add chat listener
client->getChatService().removeChatListener(listener);  //Remove chat listener
```

* Message notification received

```
void onReceive(const BMXMessageList& list)  {}
```

* Status callback notificated after message sending

```
void onStatusChanged(BMXMessagePtr msg, BMXErrorCode error) {}
```

* Status callback of attachment sending

```
void onAttachmentUploadProgressChanged(BMXMessagePtr msg, int percent)  {}
```

* Status changes of attachment donwloading

```
void onAttachmentStatusChanged(BMXMessagePtr msg, BMXErrorCode error, int percent)  {}
```

## Advanced features

Extension fields in BMXMessage entity provide extensible attributes (extension and config). Extension for development use, such as edit status. Config is an extension field for SDK's own use, such as the mention function and the push function.

* Group @ function Support @ function in group to meet the needs of your @ specified user or @ every member. Developers can realize the @ function of group Owner by setting setConfig in BMXMessage, and push notifications will be sent on the mobile side after @ members operation. You can set the @ notification list by setting the setMentionList in the Config object. Set whether to @ all group members through setMentionAll.
* Typing message

```
// ExtensionJson can be used to extend the message being edited, (json format, which can extend a variety of user-defined functions)
void setExtension(const JSON&)
```

You can use setExtension function of BMXMessage to set information in json format, to indicate the client-side is typing.

* Search for message

Search for specified message by keyword

```
/**
  * @param keywords Keyword to search
  * @param refTime Start time of message searching
  * @param size Max. number of messages to search
  * @param result List of searched result, initially pass in an empty list externally.
  * @param Direction Message search direction, default（Direction::Up）to search from earlier messages
  **/
BMXErrorCode errorCode = client->getChatService().searchMessages(keywords, refTime, size, result, direction);
```
