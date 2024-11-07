from flask import Flask, redirect

app = Flask(__name__)


@app.route("/")
def redirector():
    return redirect('https://www.ap.be')

