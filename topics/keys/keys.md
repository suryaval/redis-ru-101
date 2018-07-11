# Redis keys

Implemented everything in redis-cli

### SET

*   set key-name value
>   set jon snow

*   set key-name only if it does not exist

    >   set jon snow nx

    *   result = (nil) if key already exists
    *   result = OK if key does not exist and this operation created the key

*   force set key-name even if it exists

    >   set jon snow xx

    *   result = OK; this operation has overwritten the existing key

### GET

*   get value of a key stored in redis
    *   get key-name
    >   get jon
    *   result = "snow"

### EXPIRE

*   expire the keys with a time
    *   expire key-name time-in-seconds
    >   expire jon 10
    *   result = (integer) 1

### TTL
*   Find the TTL for the key
    *   TTL key-name
    >   TTL jon
    *   result = 10

# PTTL
```
expire something 5000
(integer) 1
pttl something
(integer) 4986657
127.0.0.1:6379> ttl something
(integer) 4980
```
### PEXPIRE
*   expire the keys with a time
    *   expire key-name time-in-milli-seconds
    >   expire jon 1000
    *   result = (integer) 1

### PERSIST

*   remove the expiration time on a key
    *   persist key-name
    >   persist jon

### EXPIREAT

*   takes unix timestamp instead of expire taking seconds
    *   EXPIREAT key-name <time>
    >   EXPIREAT jon 86400

    ```
     set something nothing nx
    OK
    127.0.0.1:6379> expireat something 86400
    (integer) 1
    127.0.0.1:6379> ttl something
    (integer) -2
    ```

### PEXPIREAT
*   takes unix timestamp in milli seconds
    >   PEXPIREAT jon 1555555555005
### EXISTS

*   determine if a key exists

    > exists key-name
    *   exists jon

### WILD CARD key search

*   search all keys with a wild card search

    *   keys *name*
    >   keys *jon*
    *   result = 1) "jon"


