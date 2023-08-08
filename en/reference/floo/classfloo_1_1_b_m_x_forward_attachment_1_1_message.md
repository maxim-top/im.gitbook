---
title: floo::BMXForwardAttachment::Message
summary: Custom message to forward attachment
---

# floo::BMXForwardAttachment::Message

Custom message to forward attachment

`#include <bmx_forward_attachment.h>`

## Public Functions

|         | Name                                                                                                                                                                        |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|         | [**Message**](classfloo\_1\_1\_b\_m\_x\_forward\_attachment\_1\_1\_message.md#function-message)(std::shared\_ptr< [BMXMessage](classfloo\_1\_1\_b\_m\_x\_message.md) > msg) |
| virtual | [**\~Message**](classfloo\_1\_1\_b\_m\_x\_forward\_attachment\_1\_1\_message.md#function-\~message)()                                                                       |

## Public Attributes

|                                                                    | Name                                                                                                            |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| int64\_t                                                           | [**msgId**](classfloo\_1\_1\_b\_m\_x\_forward\_attachment\_1\_1\_message.md#variable-msgid)                     |
| int64\_t                                                           | [**fromId**](classfloo\_1\_1\_b\_m\_x\_forward\_attachment\_1\_1\_message.md#variable-fromid)                   |
| int64\_t                                                           | [**clientTimestamp**](classfloo\_1\_1\_b\_m\_x\_forward\_attachment\_1\_1\_message.md#variable-clienttimestamp) |
| int64\_t                                                           | [**serverTimestamp**](classfloo\_1\_1\_b\_m\_x\_forward\_attachment\_1\_1\_message.md#variable-servertimestamp) |
| std::string                                                        | [**content**](classfloo\_1\_1\_b\_m\_x\_forward\_attachment\_1\_1\_message.md#variable-content)                 |
| [Type](classfloo\_1\_1\_b\_m\_x\_message\_attachment.md#enum-type) | [**contentType**](classfloo\_1\_1\_b\_m\_x\_forward\_attachment\_1\_1\_message.md#variable-contenttype)         |
| BMXMessageAttachmentPtr                                            | [**attachment**](classfloo\_1\_1\_b\_m\_x\_forward\_attachment\_1\_1\_message.md#variable-attachment)           |
| JSON                                                               | [**extension**](classfloo\_1\_1\_b\_m\_x\_forward\_attachment\_1\_1\_message.md#variable-extension)             |

## Public Functions Documentation

### function Message

```cpp
Message(
    std::shared_ptr< BMXMessage > msg
)
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='Message'></div>
```

### function \~Message

```cpp
inline virtual ~Message()
```

## Public Attributes Documentation

### variable msgId

```cpp
int64_t msgId;
```

### variable fromId

```cpp
int64_t fromId;
```

### variable clientTimestamp

```cpp
int64_t clientTimestamp;
```

### variable serverTimestamp

```cpp
int64_t serverTimestamp;
```

### variable content

```cpp
std::string content;
```

### variable contentType

```cpp
Type contentType;
```

### variable attachment

```cpp
BMXMessageAttachmentPtr attachment;
```

### variable extension

```cpp
JSON extension;
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='Message'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
