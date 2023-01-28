from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/suma", methods=["GET", "POST"])
def suma():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        opc=str(request.form.get("radio"))
        
        if opc == "s":
            return f"<h1>La suma es {int(num1) + int(num2)}</h1>"
        
        elif opc == "r":
            return f"<h1>La resta es {int(num1) - int(num2)}</h1>"

        elif opc == "m":
            return f"<h1>La multiplicacion es {int(num1) * int(num2)}</h1>"

        elif opc == "d":
            return f"<h1>La dvision es {int(num1) / int(num2)}</h1>"
        return ""
    else:
        return '''
        <form action="suma" method="POST">
        <label>Suma </label>
        <input type="radio" name="radio" value="s"/><br></br>
        <label>Resta </label>
        <input type="radio" name="radio" value="r"/><br></br>
        <label>Mutiplicacion </label>
        <input type="radio" name="radio" value="m"/><br></br>
        <label>Dvision </label>
        <input type="radio" name="radio" value="d"/><br></br>

        <label>N1: </label>
        <input type="text" name="num1"/><br></br>
        <label>N2: </label>
        <input type="text" name="num2"/><br></br>
        <input type="submit" value="Calcular"/><br></br><br></br>
        </form>
        '''


if __name__ == "__main__":
    app.run(debug=True, port = 3000)