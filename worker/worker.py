import time
import redis
import psycopg2

redis_client = redis.StrictRedis(host="redis", port=6379, db=0)
conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="db")

while True:
    votes = redis_client.lrange("votes", 0, -1)
    with conn.cursor() as cur:
        for vote in votes:
            cur.execute("INSERT INTO votes (vote) VALUES (%s)", (vote.decode("utf-8"),))
        conn.commit()
    redis_client.delete("votes")
    time.sleep(10)