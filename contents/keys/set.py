import redis

r = redis.StrictRedis(host="172.22.230.26",port=6379,db=0)

print("**-|Setting value of Jon to Snow|-**")

val = r.set("Jon","Snow")

if val == True:
    print("Key Setting Succeeded")
    print(r.get("Jon"))
else:
    print("Key Setting Failed")

res = r.set("Jon","Targareyan","nx")

print(res)