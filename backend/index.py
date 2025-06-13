from flask import Flask, jsonify, request
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

# To run the app: flask --app index run
@app.route("/")
def home():
    res = {
        "res": "Hello, Flask! Happy Two Years!"
    }
    return jsonify(res)

def checkSavings():
    with open("savings.txt", "r") as file:
        lines = file.readlines()
        if lines:
            lastLine = lines[-1].strip()
            savings = lastLine.split('|')[0]
            return savings

@app.route("/update")
def updateSavings():
    currentSavings = float(request.args.get("savings"))
    previousSavings = float(checkSavings())

    # Update the savings file
    try:
        with open("savings.txt", "a") as file:
            currentDate = datetime.date.today()
            file.write(f"\n{currentSavings}|{currentDate}")
    except FileNotFoundError:
        res = {
            "res": "File not found."
        }

    # Return true if savings went up
    if currentSavings > previousSavings:
        res = {
            "res": "true"
        }
    # Return false if savings went down or stayed the same
    else:
        res = {
            "res": "false"
        }
    return jsonify(res)