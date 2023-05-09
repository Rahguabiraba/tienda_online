"Autor: Ramon Guabiraba"
"Proyecto: M14"
"Titulo: Tienda Online"

#Importamos la librería flask
from flask import Flask, render_template, url_for, redirect

#Instanciamos el modulo para nuestra app principal
app = Flask(__name__)

#Ruta para la pagina inicial
@app.route("/")
def paginaInicio():
    return render_template("index.html")

#Iniciamos la aplicación
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(host='localhost', port=5000, debug=True)
