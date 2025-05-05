from flask import Flask, jsonify, Response, request, make_response
import requests

app = Flask(__name__)

@app.route("/signaleringen")
def signaleringen():
    try:
        url = "https://handhavingsrecht.nl/signaleringen/"
        headers = {"User-Agent": "Mozilla/5.0"}
        resp = requests.get(url, headers=headers, timeout=10)

        # Maak expliciet een response-object
        response = make_response(resp.content, resp.status_code)
        response.headers["Content-Type"] = "text/html"
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control]()
