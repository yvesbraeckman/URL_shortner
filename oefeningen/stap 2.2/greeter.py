from flask import request
from flask import Flask
from flask import render_template


app = Flask(__name__)

first_name = ""
last_name = ""


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        global first_name
        first_name = request.form["fname"]

        global last_name
        last_name = request.form["lname"]

        print(first_name, last_name)
    return render_template("home.html")


@app.route("/greet", methods=["POST", "GET"])
def greet():
    param_1 = ""
    param_2 = ""
    param_1 = request.args.get("fname")
    param_2 = request.args.get("lname")
    if param_1 != "" and param_2 != "":
        return f"hallo, {param_1} {param_2}"
    return f"hallo, {first_name} {last_name}"

