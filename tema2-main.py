from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola Mundo Perron"

@app.route("/hola")
def hola():
    return "Hola IDGS-804"

if __name__ == "__main__":
    app.run(debug=True, port = 3000)