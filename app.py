from flask import Flask, render_template, request
import random as r
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ljubezen", methods = ["POST"])
def love_calc():
    #print(request.form)
    i1 = request.form["ime1"]
    i2 = request.form["ime2"]
    pr = 0
    if i1.strip().lower() == "leon" or i2.strip().lower() == "leon":
        pr = r.randint(90,100)
    elif i1.strip().lower() == "žiga" or i2.strip().lower() == "žiga":
                pr = r.randint(0,10)
    else:
        pr = r.randint(0,100)
    if pr <= 30:
        k = "Pozabi"
    elif pr <= 70:
        k = "Morda"
    else:
        k = "Poroka!"
    if i1.strip().lower() == i2.strip().lower():
        pr = 100
        k = "samoljublje"
    if "x" in i1.lower() or "x" in i2.lower():
        pr = min(pr * 2,100)
        # recimo
    b = i1[:len(i1)//2] + i2[len(i2)//2:]

    return render_template("index.html",ime1 = i1, ime2 = i2, p = pr, iz = k, li = b)
  
app.run(debug = True)