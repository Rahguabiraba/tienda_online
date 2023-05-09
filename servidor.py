"Autor: Ramon Guabiraba"
"Proyecto: M14"
"Titulo: Tienda Online"

#Importamos la librería flask
from flask import Flask, render_template, url_for, redirect, request
from dataframe import getNombre, getMedidas, getInventario, getImagenes

#Instanciamos el modulo para nuestra app principal
app = Flask(__name__)

#Ruta para la pagina inicial
@app.route("/",methods=["GET"])
def paginaInicio():
        try:
            if request.method == 'GET':
                nombres = getNombre()
                medidas = getMedidas()
                inventario = getInventario()
                imagenes = getImagenes()
                cantidad = len(nombres)
                return render_template("index.html",cantidad=cantidad,nombres=nombres,medidas=medidas,inventario=inventario,imagenes=imagenes)
        except:
            return render_template("index.html")

#Iniciamos la aplicación
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(host='localhost', port=5000, debug=True)
