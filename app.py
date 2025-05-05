from flask import Flask, jsonify, Response, request, make_response
import requests

app = Flask(__name__)

@app.route("/signaleringen")
def signaleringen():
    try:
        url = "https://handhavingsrecht.nl/signaleringen/"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)

        # Maak expliciete response
        response = make_response(resp.content, resp.status_code)
        response.headers["Content-Type"] = "text/html"
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "GET"
        return response

    except Exception as e:
        response = make_response(jsonify({"error": str(e)}), 500)
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response

import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

