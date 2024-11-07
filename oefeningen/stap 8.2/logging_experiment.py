from flask import Flask
from flask import render_template
import logging

logging.basicConfig(filename='keuzemenu.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(message)s', datefmt='%A')
app = Flask(__name__)

@app.route("/")
def quote():
    app.logger.info("pagina bezocht")
    f = open('pagecontents.txt', 'r')
    text = f.read()
    app.logger.debug(text)
    f.close()
    return render_template("index.html", text=text)


app.run(debug=True)