from flask import Flask, render_template, request
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host="redis", port=6379, db=0)

@app.route("/", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        vote = request.form["vote"]
        redis_client.rpush("votes", vote)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)