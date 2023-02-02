from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/operasbas")
def func():

    return render_template("operasbas.html")

@app.route("/resultado", methods=["post"])
def multi():

    num1=request.form.get("txtNum1")
    num2=request.form.get("txtNum2")
    res = int(num1) * int(num2)
    
    return render_template("resultado.html", res=res, num1=num1, num2=num2)



if __name__ == "__main__":
    app.run(debug=True, port = 3000)