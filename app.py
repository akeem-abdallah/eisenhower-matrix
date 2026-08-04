from flask import Flask, send_file, jsonify
import sqlite3
app = Flask(__name__)

conn = sqlite3.connect("tasks.db")
conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        text TEXT,
        quadrant TEXT,
        completed BOOLEAN
    )
""")
conn.close()

tasks = [
    {"text": "Buy groceries", "quadrant": "q1", "completed": False},
    {"text": "Learn Flask", "quadrant": "q2", "completed": False}
]

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/api/tasks")
def get_tasks():
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True)