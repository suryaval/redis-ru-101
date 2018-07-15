# Sorted Sets

*   Ordered collection of unique strings

*   Floating Point Score

*   can be manipulated by value, position, score or lexicographically

*   Set commands are applicable:
    *   Union
    *   Intersection

*   cannot be nested

*   consists of extra argument called score


## ZADD

```
127.0.0.1:6379> zadd sset nx 1 vijayawada
(integer) 1
127.0.0.1:6379> zadd sset nx 1 andhra
(integer) 1
127.0.0.1:6379> zadd sset nx 2 hyderabad
(integer) 1
127.0.0.1:6379> zadd sset nx 2 telangana
(integer) 1
127.0.0.1:6379> zrange sset 0 1
1) "andhra"
2) "vijayawada"
127.0.0.1:6379> zrange sset 0 -1
1) "andhra"
2) "vijayawada"
3) "hyderabad"
4) "telangana"
```
## ZRANGE


## ZREVRANGE

## ZRANK

## ZREVRANK

## ZSCORE

```
127.0.0.1:6379> zscore sset vijayawada
"1"
127.0.0.1:6379> zscore sset hyderabad
"2"
127.0.0.1:6379> zscore sset andhra
"1"
127.0.0.1:6379> zscore sset telangana
"2"
```

# ZCOUNT

```
127.0.0.1:6379> zcount sset 0 1
(integer) 2
127.0.0.1:6379> ZRANGE SSET 0 1
(empty list or set)
127.0.0.1:6379> ZRANGE SSET 1 2
(empty list or set)
127.0.0.1:6379> ZRANGE sset 1 2
1) "vijayawada"
2) "hyderabad"
127.0.0.1:6379> ZRANGE sset 0 1
1) "andhra"
2) "vijayawada"
```

