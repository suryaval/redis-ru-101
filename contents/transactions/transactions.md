# Transactions

Serialized and executed sequentially

Follows ACID: Atomicity, Consistency, Isolation & Durability

Redis does not support nested transactions i.e. cannot use multi inside a multi

## MULTI
    Indicates the start of a transaction

## EXEC
    executes the queued commands

## DISCARD
    throws away queued commands

```
127.0.0.1:6379> multi
OK
127.0.0.1:6379> set something 0
QUEUED
127.0.0.1:6379> incrby something 100000
QUEUED
127.0.0.1:6379> get something
QUEUED
127.0.0.1:6379> exec
1) OK
2) (integer) 100000
3) "100000"
127.0.0.1:6379> multi
OK
127.0.0.1:6379> incrby something -1000000
QUEUED
127.0.0.1:6379> get something
QUEUED
127.0.0.1:6379> discard
OK
127.0.0.1:6379> get something
"100000"
```
## Optimistic Concurrency Control

### WATCH
    
*   Called before multi

*   Multiple watch commands are cumulative

*   Local to client i.e. not global

### UNWATCH