import redis

redis_db = redis.StrictRedis(host="localhost", port=63370, db=0)

redis_db.keys()

redis_db.set("full stack", "python")

redis_db.keys()

redis_db.get("full stack")

redis_db.incr("twilio")

redis_db.get("twilio")

redis_db.delete("twilio")

redis_db.get("twilio")

