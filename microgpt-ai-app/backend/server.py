from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json.get("prompt")

    result = subprocess.run(
        ["python3", "microgpt.py"],
        capture_output=True,
        text=True
    )

    return jsonify({"response": result.stdout})

if __name__ == "__main__":
    app.run(port=5000)
