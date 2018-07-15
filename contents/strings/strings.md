# Strings

### DECRBY

### INCRBY

### INCRBYFLOAT
```
127.0.0.1:6379> get something
"nothingyes"
127.0.0.1:6379> set anything 100
OK
127.0.0.1:6379> get anything
"100"
127.0.0.1:6379> incrby anything -100
(integer) 0
127.0.0.1:6379> get anything
"0"
127.0.0.1:6379> decrby anything 200
(integer) -200
127.0.0.1:6379> get anything
"-200"
127.0.0.1:6379> incrbyfloat anything 200.00001
"0.00001"
127.0.0.1:6379> get anything
"0.00001"
```
### OBJECT

```
OBJECT encoding anything
"embstr"
127.0.0.1:6379> OBJECT refcount anything
(integer) 1
127.0.0.1:6379> object idletime anything
(integer) 119
```
## APPEND
*   appends the value to the existing value of the key

>   set something nothing
>   append something yes
    result = (integer) 10
>   get something
    ```
    nothingyes
    ```