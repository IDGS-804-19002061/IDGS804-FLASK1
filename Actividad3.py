from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/act3")
def func():

    return render_template("act3.html")

@app.route("/pago", methods=["post"])
def multi():

    if request.method=="post":
        precio=12000
        nombre=request.form.get("nombre")
        compradores=int(request.form.get("compradores"))
        tarjeta=request.form.get("card")
        boletos=int(request.form.get("boletos"))
        max = boletos/compradores
    
        if max >= 7:
        
            res = precio*boletos
            if boletos>5:
                res = res*0.85
            elif boletos>=3:
                res = res*0.90
            else:
                res = res

            if tarjeta=="s":
                res = res*0.90
        else:
            return '''
            <h1>Se ha alcanzado el numero maximo de boletos por comprador</h1>
            '''

    return render_template("pago.html", res=res, nombre=nombre, compradores=compradores, tarjeta=tarjeta, boletos=boletos)


if __name__ == "__main__":
    app.run(debug=True, port = 3000)