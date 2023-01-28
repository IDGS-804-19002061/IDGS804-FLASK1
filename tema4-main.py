from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/suma", methods=["GET", "POST"])
def suma():
    if request.method=="POST":
        num1=request.form.get("num1")
        num2=request.form.get("num2")
        return f"<h1>La suma es {int(num1) + int(num2)}</h1>"
    else:
        return '''
        <form action="suma" method="POST">
        <label>N1: </label>
        <input type="text" name="num1"/><br></br><br></br>
        <label>N2: </label>
        <input type="text" name="num2"/><br></br><br></br>
        <input type="submit" value="Calcular"/><br></br><br></br>
        </form>
        '''


if __name__ == "__main__":
    app.run(debug=True, port = 3000)