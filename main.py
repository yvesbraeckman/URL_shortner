from flask import request
from flask import Flask, redirect
from flask import render_template
import sqlite3
import random
from logging.config import dictConfig
from functools import wraps
from collections import OrderedDict


con = sqlite3.connect("URL_Shortner.sqlite")
cur = con.cursor()
app = Flask(__name__)

def remember_recent_calls(f):
    cache = OrderedDict()

    @wraps(f)
    def wrapper(*args, **kwargs):
            arg = list(kwargs.values())[0]
            if arg in cache:
                return cache[arg]
            else:
                result = f(*args, **kwargs)
                cache[arg] = result
                if len(cache) >= 5:
                    cache.popitem(last=False)
                return result
    return wrapper


def randomstring():
    rand_string = ""
    for i in range(0, 16):
        rand_int = random.randint(97, 122)
        rand_string += chr(rand_int)
    return rand_string


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
                "level":"WARNING"
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

cur.execute('CREATE TABLE IF NOT EXISTS Links(URL, Alias)')
con.close()


@app.route("/", methods=["POST", "GET"])
def home():
    errors = []
    data = []
    if request.method == "POST":
        if request.form["url"] != "":
            with sqlite3.connect("URL_Shortner.sqlite") as con_1:
                alias = randomstring()
                cur_1 = con_1.cursor()
                data.append((request.form["url"], alias))
                cur_1.executemany("""INSERT INTO Links VALUES (?, ?)""", data)
                con_1.commit()
                print(alias)
            return render_template("succes.html")
        else:
            errors.append("Geen URL opgegeven")
            return render_template("fail.html", errors=errors)
    return render_template("home.html")


@app.route("/<url>")
@remember_recent_calls
def url_match(url):
    with sqlite3.connect("URL_Shortner.sqlite") as con_1:
        cur_1 = con_1.cursor()
        if cur_1.execute("SELECT Alias FROM Links WHERE Alias = ?", [url]).fetchone() is not None:
            res = cur_1.execute("SELECT * FROM Links WHERE Alias = ?", [url]).fetchone()
            app.logger.warning(f"{res[0]} bezocht")
            return redirect(res[0])
        else:
            return render_template("fail.html")


if __name__ == '__main__':
    app.run(debug=False)
