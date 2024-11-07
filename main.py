from flask import request
from flask import Flask, redirect, url_for
from flask import render_template
import sqlite3
import random
from logging.config import dictConfig

con = sqlite3.connect("URL_Shortner.sqlite")
cur = con.cursor()
app = Flask(__name__)



dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file":{
                "class": "logging.FileHandler",
                "filename": "logger.log",
                "formatter": "default",
            }
        },
        "root": {"level": "DEBUG", "handlers": ["console", "file"]},
    }
)

cur.execute("CREATE TABLE IF NOT EXISTS Links(URL, Alias)")
con.close()


def randomstring():
    rand_string = ""
    for i in range(0, 16):
        rand_int = random.randint(97, 122)
        rand_string += chr(rand_int)
    return rand_string


@app.route("/", methods=["POST", "GET"])
def home():
    errors = []
    data = []
    if request.method == "POST":
        if request.form["url"] != "":
            with sqlite3.connect("URL_Shortner.sqlite") as con_1:
                cur_1 = con_1.cursor()
                data.append((request.form["url"], randomstring()))
                cur_1.executemany("""INSERT INTO Links VALUES (?, ?)""", data)
                con_1.commit()
            return render_template("succes.html")
        else:
            errors.append("Geen URL opgegeven")
            return render_template("fail.html", errors=errors)
    return render_template("home.html")


@app.route("/<url>")
def url_match(url):
    app.logger.debug(f"{url} bezocht")
    with sqlite3.connect("URL_Shortner.sqlite") as con_1:
        cur_1 = con_1.cursor()
        if cur_1.execute("SELECT Alias FROM Links WHERE Alias = ?", [url]).fetchone() is not None:
            res = cur_1.execute("SELECT * FROM Links WHERE Alias = ?", [url]).fetchone()
            return redirect(res[0])
        else:
            return render_template("fail.html")


if __name__ == '__main__':
    app.run(debug=False)
