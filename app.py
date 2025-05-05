from flask import Flask, jsonify, Response, request, make_response
import requests

app = Flask(__name__)

@app.route("/signaleringen")
def signaleringen():
    try:
        url = "https://handhavingsrecht.nl/signaleringen/"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)
        response = make_response(resp.content, resp.status_code)
        response.headers["Content-Type"] = resp.headers.get('Content-Type', 'text/html')
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        error_response = jsonify({"error": str(e)})
        error_response.headers["Access-Control-Allow-Origin"] = "*"
        return error_response, 500

if __name__ == "__main__":
    app.run()
