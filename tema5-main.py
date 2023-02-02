from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def func():
    return render_template("index.html")

@app.route("/users")
def users():
    return render_template("users.html")

@app.route("/students")
def students():
    return render_template("students.html")




if __name__ == "__main__":
    app.run(debug=True, port = 3000)