"Autor: Ramon Guabiraba"
"Proyecto: M14"
"Titulo: Analisis de Tienda Online"

#Importamos la librería flask
from flask import Flask, render_template, request
from dataframe import getNombre, getMedidas, getInventario, getImagenes, createMatPlob
from conexionBBDD import registrarGraficos, getAllGraficos

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
        
#Ruta para la pagina del grafico
@app.route("/grafico",methods=["POST"])
def paginaGrafico():
        try:
            if request.method == 'POST':
                figura = createMatPlob(request)
                if figura != "":
                    registrarGraficos(figura)
                    return render_template("graffic.html",img=figura)
                return render_template("index.html")
        except:
            return render_template("index.html")
        
#Ruta para la pagina del grafico
@app.route("/graficoUnico",methods=["POST"])
def paginaUnicoGrafico():
        try:
            if request.method == 'POST':
                respuesta = request.form
                ruta = respuesta["ruta"]
                return render_template("graffic.html",img=ruta)
            return render_template("list.html")
        except:
            return render_template("list.html")
        
#Ruta para la pagina del lista
@app.route("/lista",methods=["POST"])
def paginaLista():
        try:
            if request.method == 'POST':
                graficos = getAllGraficos()
                return render_template("list.html",graficos=graficos)
        except:
            return render_template("graffic.html")

#Iniciamos la aplicación
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(host='localhost', port=5000, debug=True)
