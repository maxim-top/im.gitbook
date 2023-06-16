---
title: floo::BMXError

---

# floo::BMXError





## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BMXError](classfloo_1_1_b_m_x_error.md#function-bmxerror)**(BMXErrorCode errorCode) |
| virtual | **[~BMXError](classfloo_1_1_b_m_x_error.md#function-~bmxerror)**() |
| [BMXError](classfloo_1_1_b_m_x_error.md) & | **[operator=](classfloo_1_1_b_m_x_error.md#function-operator=)**(BMXErrorCode errorCode) |
| bool | **[operator==](classfloo_1_1_b_m_x_error.md#function-operator==)**(BMXErrorCode errorCode) |
| bool | **[operator==](classfloo_1_1_b_m_x_error.md#function-operator==)**(const [BMXError](classfloo_1_1_b_m_x_error.md) & error) |
| BMXErrorCode | **[errorCode](classfloo_1_1_b_m_x_error.md#function-errorcode)**() |
| std::string | **[description](classfloo_1_1_b_m_x_error.md#function-description)**() |

## Public Functions Documentation

### function BMXError

```cpp
BMXError(
    BMXErrorCode errorCode
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXError",function="BMXError" %}{% endlanying_code_snippet %}
```
### function ~BMXError

```cpp
virtual ~BMXError()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXError",function="~BMXError" %}{% endlanying_code_snippet %}
```
### function operator=

```cpp
BMXError & operator=(
    BMXErrorCode errorCode
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXError",function="operator=" %}{% endlanying_code_snippet %}
```
### function operator==

```cpp
bool operator==(
    BMXErrorCode errorCode
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXError",function="operator==" %}{% endlanying_code_snippet %}
```
### function operator==

```cpp
bool operator==(
    const BMXError & error
)
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXError",function="operator==" %}{% endlanying_code_snippet %}
```
### function errorCode

```cpp
BMXErrorCode errorCode()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXError",function="errorCode" %}{% endlanying_code_snippet %}
```
### function description

```cpp
std::string description()
```


**Example**:
```
{% lanying_code_snippet repo="lanying-im-embedded",class="BMXError",function="description" %}{% endlanying_code_snippet %}
```
-------------------------------

Updated on 2022-01-26 at 17:20:40 +0800