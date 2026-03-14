from flask import Flask
import psycopg2
import redis

app = Flask(__name__)

@app.route("/")
def home():
    try:
        psycopg2.connect(
        host="db",
        database="devopsdb",
        user="admin",
        password="admin"
    )

        r = redis.Redis(host="redis", port=6379)

        return "Connected to Postgres & Redis successfully!"

    except Exception as e:
        return str(e)

app.run(host="0.0.0.0", port=5000)