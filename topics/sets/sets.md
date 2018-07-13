# Sets

*   Unordered collection of unique strings

    *   Difference

    *   Intersect

    *   Union

*   sets are not nested

## SADD

```
smembers some-set
1) "train"
2) "boat"
3) "ship"
4) "motorcycle"
5) "car"
6) "aeroplane"
7) "bicycle"
8) "bus"
127.0.0.1:6379> sscan some-set 0 match motor
1) "0"
2) (empty list or set)
127.0.0.1:6379> sscan some-set 0 match motor*
1) "0"
2) 1) "motorcycle"
127.0.0.1:6379> sscan some-set 0 match *cycle
1) "0"
2) 1) "bicycle"
   2) "motorcycle"
127.0.0.1:6379> sismember some-set ship
(integer) 1
127.0.0.1:6379> sismember some-set kayak
(integer) 0
```

## SCARD

*   Gives the number of members in a set
```
 scard some-set
(integer) 8
```

## SDIFF
```
sadd ground-transport bicycle motorcycle car bus
(integer) 4
127.0.0.1:6379> smembers ground-transport
1) "car"
2) "bicycle"
3) "bus"
4) "motorcycle"
127.0.0.1:6379> smembers some-set
1) "train"
2) "boat"
3) "ship"
4) "motorcycle"
5) "car"
6) "aeroplane"
7) "bicycle"
8) "bus"
127.0.0.1:6379> sdiff some-set ground-transport
1) "train"
2) "aeroplane"
3) "boat"
4) "ship"
127.0.0.1:6379> sdiff ground-transport some-set
(empty list or set)
```

#   SDIFFSTORE

```
127.0.0.1:6379> sdiffstore ground-transport some-set result
(integer) 8
127.0.0.1:6379> smembers some-set
1) "train"
2) "boat"
3) "ship"
4) "motorcycle"
5) "car"
6) "aeroplane"
7) "bicycle"
8) "bus"
127.0.0.1:6379>
```

# SINTER
```
127.0.0.1:6379> sinter ground-transport some-set
1) "motorcycle"
2) "car"
3) "bicycle"
4) "bus"
```

# SREM

```
127.0.0.1:6379> smembers ground-transport
1) "train"
2) "boat"
3) "ship"
4) "motorcycle"
5) "car"
6) "bicycle"
7) "aeroplane"
8) "bus"
127.0.0.1:6379> srem ground-transport train
(integer) 1
127.0.0.1:6379> srem ground-transport boat ship aeroplane
(integer) 3
127.0.0.1:6379> smembers ground-transport
1) "motorcycle"
2) "car"
3) "bicycle"
4) "bus"
```

# SSCAN
```
127.0.0.1:6379> sscan ground-transport 0 match *
1) "0"
2) 1) "car"
   2) "bicycle"
   3) "motorcycle"
   4) "bus"
```