import matplotlib
import pandas as pd
import flask
import itertools
from markupsafe import Markup
from flask import request, render_template, Flask
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/inputs", methods=["POST"])
def process():
    mother_raw = request.form.get("mother")
    father_raw = request.form.get("father")
    mother_l = list(mother_raw)
    father_l = list(father_raw)
    counter = 0
    storage = []
    mother = []
    father = []
    for m in mother_l:
        if counter == 0:
            storage.append(m)
            counter = 1
        elif counter == 1:
            storage.append(m)
            mother.append(storage.copy())
            counter = 0
            storage = []
    storage = []
    counter = 0
    for f in father_l:
        if counter == 0:
            storage.append(f)
            counter = 1
        elif counter == 1:
            storage.append(f)
            father.append(storage.copy())
            counter = 0
            storage = []
    ht = "<tr>"
    rowcolc = len(mother)
    ht += "<th></th>"
    print(mother)
    fatherc = list(itertools.product(*father))
    motherc = list(itertools.product(*mother))
    for headering in motherc:
        ht += "<th>"
        ht += "".join(headering)
        ht += "</th>"
    html_str = "</tr>"
    for i in range(rowcolc + 1):
        html_str += "<tr>"
        html_str += "<td>" + "".join(fatherc[i]) + "</td>"
        for _ in range(rowcolc + 1):
            html_str += "<td></td>"
    return render_template("table.html", head=Markup(ht),  cont=Markup(html_str))
if __name__ == "__main__":
    app.run(debug=True)