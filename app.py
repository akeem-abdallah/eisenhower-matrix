from flask import Flask, send_file, jsonify, request
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

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/api/tasks")
def get_tasks():
    conn = sqlite3.connect("tasks.db")
    rows = conn.execute("SELECT text, quadrant, completed FROM tasks").fetchall()
    conn.close()
    result = []
    for row in rows:
        result.append({"text": row[0], "quadrant": row[1], "completed": bool(row[2])})
    return jsonify(result)

@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    conn = sqlite3.connect("tasks.db")
    conn.execute("INSERT INTO tasks (text, quadrant, completed) VALUES (?, ?, ?)", (data["text"], data["quadrant"], data["completed"]))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)