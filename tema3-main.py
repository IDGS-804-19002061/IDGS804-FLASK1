from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo Perron"

@app.route("/hola")
def hola():
    return "Hola IDGS-804"

#  Pasamos un string
@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}" 

#  Pasamos un int
@app.route("/numero/<int:n>")
def numero(n):
    return f"Numero {n}" 

#  Pasamos mas de un parametro
@app.route("/user/<int:id>/<string:username>")
def usern(id, username):
    return f"ID:  {id} Nombre: {username}" 

if __name__ == "__main__":
    app.run(debug=True, port = 3000)