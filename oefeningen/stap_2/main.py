from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def quote():
    f = open('../stap 8.2/pagecontents.txt', 'r')
    text = f.read()
    print(text)
    f.close()
    return render_template("home.html", text=text)


if __name__ == '__main__':
    app.run()
