from flask import Flask, send_file, jsonify
app = Flask(__name__)

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