from flask import Flask, jsonify, render_template
import random
import json

app = Flask(__name__)

data = json.load(open("./data.json", "r")) # load fal data from json file

@app.route("/fal")
def fal(): # returns a random fal as json response
    return jsonify(random.choice(data)) 

@app.route("/hx/fal")
def hx_fal(): # returns a random fal as html response for htmx
    fal = random.choice(data)
    return render_template("fal.html", id=fal["id"], ghazal=fal["ghazal"], fal=fal["fal"])

@app.route("/")
def main(): # main page
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True)
