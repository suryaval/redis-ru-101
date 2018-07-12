# Lists

*   Ordered collection of strings

*   Duplicates are allowed

*   elements can be added and removed at left or right

*   elements can be inserted relative to another

*   used to implement stacks and queues

*   are not nested

*   can be implemented as a linked list

### UseCases

*   Inter Process Communication

*   Activity Streams

## PUSH

    *   LPUSH

    *   RPUSH

## POP

    *   RPUSH

    *   RPOP

```
127.0.0.1:6379> lpush usa:states-codes california:ca pennsylvania:pa maryland:md virginia:va texas:tx
(integer) 5
127.0.0.1:6379> llen usa:states-codes
(integer) 5
127.0.0.1:6379> lrange usa:states-codes 0 -1
1) "texas:tx"
2) "virginia:va"
3) "maryland:md"
4) "pennsylvania:pa"
5) "california:ca"
127.0.0.1:6379> rpush usa:states-codes oregon:or arizona:az nevada:nv maine:mn vermont:vt newyork:ny newjersey:nj
(integer) 12
127.0.0.1:6379> llen usa:states-codes
(integer) 12
127.0.0.1:6379> lrange usa:states-codes 0 -1
 1) "texas:tx"
 2) "virginia:va"
 3) "maryland:md"
 4) "pennsylvania:pa"
 5) "california:ca"
 6) "oregon:or"
 7) "arizona:az"
 8) "nevada:nv"
 9) "maine:mn"
10) "vermont:vt"
11) "newyork:ny"
12) "newjersey:nj"
127.0.0.1:6379> lpop usa:states-codes
"texas:tx"
127.0.0.1:6379> lrange usa:states-codes 0 -1
 1) "virginia:va"
 2) "maryland:md"
 3) "pennsylvania:pa"
 4) "california:ca"
 5) "oregon:or"
 6) "arizona:az"
 7) "nevada:nv"
 8) "maine:mn"
 9) "vermont:vt"
10) "newyork:ny"
11) "newjersey:nj"
127.0.0.1:6379> rpop usa:states-codes
"newjersey:nj"
127.0.0.1:6379> lrange usa:states-codes 0 -1
 1) "virginia:va"
 2) "maryland:md"
 3) "pennsylvania:pa"
 4) "california:ca"
 5) "oregon:or"
 6) "arizona:az"
 7) "nevada:nv"
 8) "maine:mn"
 9) "vermont:vt"
10) "newyork:ny"
```

