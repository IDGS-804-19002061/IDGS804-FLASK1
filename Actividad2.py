from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/act2")
def func():

    return render_template("act2.html")

@app.route("/resultado", methods=["post"])
def multi():

    p1=int(request.form.get("punto1"))
    p2=int(request.form.get("punto2"))
    p3=int(request.form.get("punto3"))
    p4=int(request.form.get("punto4"))
    res= math.sqrt(math.pow((p3-p1),2)+math.pow((p4-p2),2))
    return render_template("res2.html", res=res, p1=p1, p2=p2, p3=p3, p4=p4)



if __name__ == "__main__":
    app.run(debug=True, port = 3000)