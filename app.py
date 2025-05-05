
from flask import Flask, jsonify, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # ← Dit laat CORS toe vanaf alle origins


app = Flask(__name__)

@app.route("/signaleringen")
def signaleringen():
    try:
        url = "https://handhavingsrecht.nl/signaleringen/"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        return Response(resp.content, status=resp.status_code, content_type=resp.headers.get('Content-Type'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="localhost", port=3000)
