---
title: floo::BMXNetworkListener
---

# floo::BMXNetworkListener

Inherited by [floo::BMXClient](classfloo\_1\_1\_b\_m\_x\_client.md)

## Public Functions

|              | Name                                                                                                                                     |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| virtual      | [**\~BMXNetworkListener**](classfloo\_1\_1\_b\_m\_x\_network\_listener.md#function-\~bmxnetworklistener)()                               |
| virtual void | [**onNetworkChanged**](classfloo\_1\_1\_b\_m\_x\_network\_listener.md#function-onnetworkchanged)(BMXNetworkType type, bool reconnect) =0 |

## Public Functions Documentation

### function \~BMXNetworkListener

```cpp
inline virtual ~BMXNetworkListener()
```

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXNetworkListener'></div>
```

### function onNetworkChanged

```cpp
virtual void onNetworkChanged(
    BMXNetworkType type,
    bool reconnect
) =0
```

**Reimplemented by**: [floo::BMXClient::onNetworkChanged](classfloo\_1\_1\_b\_m\_x\_client.md#function-onnetworkchanged)

**Example**:

```
<div data-gb-custom-block data-tag="lanying_code_snippet" data-0=',function=' data-repo='lanying-im-embedded' data-class='BMXNetworkListener'></div>
```



Updated on 2022-01-26 at 17:20:40 +0800
