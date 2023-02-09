from flask import Flask, render_template, request

class Pago:
        
        def __init__(self, precio, boletos, compradores):
                self.precio = int(precio)
                self.boletos = int(boletos)
                self.compradores = int(compradores)
                self.max = self.boletos/self.compradores
                self.total = self.precio * self.boletos

        def descuento(self):
            if self.boletos>5:
                self.total = self.total*0.85
            elif self.boletos>=3:
                self.total = self.total*0.90
            else:
                self.total = self.total

        def descuentoTarjeta(self, tarjeta):
            if tarjeta=="s":
                self.total = self.total*0.90
            else:
                self.total = self.total

app = Flask(__name__)

@app.route("/act3")
def func():
    return render_template("act3.html")
    

@app.route("/pago", methods=["post"])
def pago():
    pago = Pago(
        12, 
        int(request.form.get("boletos")),
        int(request.form.get("compradores"))
        )

    tarjeta = request.form.get("tarjeta")

    if pago.max >7:
        return render_template("error.html")
    else:
        pago.descuento()
        pago.descuentoTarjeta(tarjeta)
        return render_template("pago.html", res=pago.total)

    


if __name__ == "__main__":
    app.run(debug=True, port = 3000)