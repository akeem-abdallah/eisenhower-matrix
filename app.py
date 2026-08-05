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

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    conn = sqlite3.connect("tasks.db")
    rows = conn.execute("SELECT id, text, quadrant, completed FROM tasks").fetchall()
    conn.close()
    result = []
    for row in rows:
        result.append({"id": row[0], "text": row[1], "quadrant": row[2], "completed": bool(row[3])})
    return jsonify(result)

@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if "text" not in data or "quadrant" not in data:
        return jsonify({"error": "text and quadrant are required"}), 400
    conn = sqlite3.connect("tasks.db")
    cursor = conn.execute("INSERT INTO tasks (text, quadrant, completed) VALUES (?, ?, ?)", (data["text"], data["quadrant"], data["completed"]))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": new_id})

@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    conn = sqlite3.connect("tasks.db")
    conn.execute("UPDATE tasks SET completed = ? WHERE id = ?", (data["completed"], task_id))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = sqlite3.connect("tasks.db")
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)