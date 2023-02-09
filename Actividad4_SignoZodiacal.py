from flask import Flask, render_template, request, make_response
from datetime import date

app = Flask(__name__)

@app.route("/act4")
def func():
    return render_template("act4.html")
    
@app.route("/preguntas", methods=["post"])
def preguntas():
    resp = make_response(render_template("preguntas.html"))
    resp.set_cookie('nombre', request.form.get("nombre"))
    resp.set_cookie('aPaterno', request.form.get("aPaterno"))
    resp.set_cookie('aMaterno', request.form.get("aMaterno"))
    resp.set_cookie('dia', request.form.get("dia"))
    resp.set_cookie('mes', request.form.get("mes"))
    resp.set_cookie('año', request.form.get("año"))
    resp.set_cookie('sexo', request.form.get("sexo"))
    return resp

@app.route("/signoResultado", methods=["post"])
def pago():
    preguntas = {
        "pregunta1": request.form.get("pregunta1"),
        "pregunta2": request.form.get("pregunta2"),
        "pregunta3": request.form.get("pregunta3"),
        "pregunta4": request.form.get("pregunta4"),
        "pregunta5": request.form.get("pregunta5")
    }
    
    cal = 0
    for i in preguntas:
        if(preguntas[i]=="b"):
            cal= cal + 1

    year = int(request.cookies.get("año"))
    edad = calculateAge(year)
    signo = ""

    dragon = [1940, 1952, 1964, 1976, 1988, 2000, 2012]
    rata = [1936, 1948, 1960, 1972, 1984, 1996, 2008]
    buey = [1937, 1949, 1961, 1973, 1985, 1997, 2009]
    tigre = [1938, 1950, 1962, 1974, 1986, 1998, 2010]
    conejo = [1939, 1951, 1963, 1975, 1987, 1999, 2011]
    serpiente = [1941, 1953, 1965, 1977, 1989, 2001, 2013]
    caballo = [1942, 1954, 1966, 1978, 1990, 2002, 2014]
    cabra = [1943, 1955, 1967, 1979, 1991, 2003, 2015]
    mono = [1944, 1956, 1968, 1980, 1992, 2004, 2016]
    gallo = [1945, 1957, 1969, 1981, 1993, 2005, 2017]
    perro = [1946, 1958, 1970, 1982, 1994, 2006, 2018]
    cerdo = [1947, 1959, 1971, 1983, 1995, 2007, 2019]

    if year in dragon:
        signo = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Dragon-300x257.jpg"
    elif year in rata:
        signo = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Rata-300x257.jpg"
    elif year in buey:
        signo = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Buey-300x257.jpg"
    elif year in tigre:
        signo = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Tigre-300x257.jpg"
    elif year in conejo:
        signo = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Conejo-300x257.jpg"
    elif year in serpiente:
        signo = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Serpiente-300x257.jpg"
    elif year in caballo:
        signo = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Caballo-300x257.jpg"
    elif year in cabra:
        signo = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Cabra-300x257.jpg"
    elif year in mono:
        signo = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Mono-300x257.jpg"
    elif year in gallo:
        signo = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Gallo-300x257.jpg"
    elif year in perro:
        signo = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Perro-300x257.jpg"
    elif year in cerdo:
        signo = "http://www.ccl.uanl.mx/wp-content/uploads/2018/02/06_horoscopo_chino_Cerdo-300x257.jpg"
    
    data = {
        "nombre": request.cookies.get("nombre"),
        "aPaterno": request.cookies.get("aPaterno"),
        "aMaterno": request.cookies.get("aMaterno"),
        "sexo": request.cookies.get("sexo"),
        "edad": edad,
        "cal": cal,
        "signo": signo
    }
    return render_template("signoResultado.html", data=data)

def calculateAge(year):
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (int(request.cookies.get("mes")), int(request.cookies.get("dia"))))
 
    return age


if __name__ == "__main__":
    app.run(debug=True, port = 3000)
    