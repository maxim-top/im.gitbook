---
title: floo::BMXNetworkListener

---

# floo::BMXNetworkListener





Inherited by [floo::BMXClient](classfloo_1_1_b_m_x_client.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BMXNetworkListener](classfloo_1_1_b_m_x_network_listener.md#function-~bmxnetworklistener)**() |
| virtual void | **[onNetworkChanged](classfloo_1_1_b_m_x_network_listener.md#function-onnetworkchanged)**(BMXNetworkType type, bool reconnect) =0 |

## Public Functions Documentation

### function ~BMXNetworkListener

```cpp
inline virtual ~BMXNetworkListener()
```


### function onNetworkChanged

```cpp
virtual void onNetworkChanged(
    BMXNetworkType type,
    bool reconnect
) =0
```


**Reimplemented by**: [floo::BMXClient::onNetworkChanged](classfloo_1_1_b_m_x_client.md#function-onnetworkchanged)


-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800