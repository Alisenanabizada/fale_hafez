from flask import Flask, jsonify
import random
import json

app = Flask(__name__)

data = json.load(open("./data.json", "r"))

@app.route("/fal")
def fal():
    return jsonify(random.choice(data))

app.run(host="0.0.0.0", port=9999, debug=True)
