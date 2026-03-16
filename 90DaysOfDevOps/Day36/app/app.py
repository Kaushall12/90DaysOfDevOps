from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host=os.environ.get("DB_HOST"),
            database=os.environ.get("POSTGRES_DB"),
            user=os.environ.get("POSTGRES_USER"),
            password=os.environ.get("POSTGRES_PASSWORD")
        )
        return "Flask App connected to PostgreSQL successfully!"
    except Exception as e:
        return str(e)

app.run(host="0.0.0.0", port=5000)