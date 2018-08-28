# Hashes

## UseCases

*   Ratelimiting of APIs

# HSET

```
127.0.0.1:6379> hset cisco:sanjose building 1
(integer) 1
127.0.0.1:6379> hset cisco:sanjose street tasman
(integer) 1
```

```
127.0.0.1:6379> hset cisco:bangalore building 1
(integer) 1
127.0.0.1:6379> hset cisco:bangalore street electronic-city
(integer) 1
```

# HEXISTS
```
127.0.0.1:6379> hexists cisco:sanjose building
(integer) 1
127.0.0.1:6379> hexists cisco:sanjose buildinw
(integer) 0
```
# HDEL
127.0.0.1:6379> hdel cisco:bangalore building street
(integer) 2

# HINCRBY
hincrby cisco:bangalore cars 3

# HINCRBYFLOAT
```
127.0.0.1:6379> hincrbyfloat cisco:sanjose building 0.5
"2.5"
127.0.0.1:6379> hgetall cisco:sanjose
 1) "building"
 2) "2.5"
 3) "street"
 4) "tasman"
 5) "employee"
 6) "200"
 7) "cars"
 8) "300"
 9) "bikes"
```
# HSET
```
hset cisco:bangalore cars 2
```
# HSETNX
```
127.0.0.1:6379> hsetnx cisco:sanjose bikes 2
(integer) 1
127.0.0.1:6379> hsetnx cisco:sanjose cars 2
(integer) 0
```
# HGET
```
127.0.0.1:6379> hget cisco:bangalore street
"electronic-city"
```
# HGETALL
```
127.0.0.1:6379> hgetall cisco:sanjose
1) "building"
2) "1"
3) "street"
4) "tasman"
127.0.0.1:6379> hgetall cisco:bangalore
1) "building"
2) "1"
3) "street"
4) "electronic-city"
```
# HSCAN
```
127.0.0.1:6379> hscan cisco:sanjose 19
1) "0"
2) 1) "building"
   2) "2"
   3) "street"
   4) "tasman"
   5) "employee"
   6) "200"
   7) "cars"
```
# HKEYS
```
127.0.0.1:6379> hkeys cisco:sanjose
1) "building"
2) "street"
3) "employee"
4) "cars"
```
# HVALS
```
127.0.0.1:6379> hvals cisco:sanjose
1) "2"
2) "tasman"
3) "200"
4) "300"
```
# HMSET
```
127.0.0.1:6379> hmset cisco:sanjose employee 200 cars 300
OK
127.0.0.1:6379> hgetall cisco:sanjose
1) "building"
2) "2"
3) "street"
4) "tasman"
5) "employee"
6) "200"
7) "cars"
8) "300"
```

# HMGET
```
127.0.0.1:6379> hmget cisco:sanjose employee cars street
1) "200"
2) "300"
3) "tasman"
```
