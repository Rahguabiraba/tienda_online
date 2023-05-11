#Importamos la libreria pandas
import pandas as pd
from matplotlib import pyplot as plt
import random

#Usamos un dataframe vacío
productos = pd.DataFrame()
#Pasamos todo el contenido del fichero a una variable
fichero = pd.read_csv(f"static/datos/Productos.csv")
#Concatenamos el dataframe con los datos
productos = pd.concat([productos,fichero])

def getNombre():
    nombres = []
    for producto in productos["Nombre"]:
        nombres.append(producto)
    return nombres

def getMedidas():
    medidas = []
    for producto in productos["Medidas"]:
        medidas.append(producto)
    return medidas

def getInventario():
    inventario = []
    for producto in productos["Inventario"]:
        inventario.append(producto)
    return inventario

def getImagenes():
    imagenes = []
    for producto in productos["Imágenes"]:
        imagenes.append(producto)
    return imagenes

def createMatPlob(request):
    # Pasamos la respuesta del formulario a una variable
    respuesta = request.form

    # Pasar las informaciones del formulario a las variables
    numeros = respuesta['inventario']
    nombres = respuesta['productos']
    #Usamos la función split porque los nombres y inventario vienen como un unico string separado por comas
    nums = numeros.split(",")
    productos = nombres.split(",")

    inventario = []
    for numero in nums:
        inventario.append(int(numero))
    
    #Creamos un diccionario para unir nombres y inventario
    listaCompleta = {}
    for i in range(0,len(inventario)):
        listaCompleta[inventario[i]] = productos[i]
    
    #Ordenamos el diccionario en orden cresciente ordenando las keys
    numbers = listaCompleta.keys()
    #Usamos la función sorted para ordenar los numeros
    listaOrdenada = sorted(numbers)

    #Pasamos a una nueva lista
    nuevaLista = {}
    for keys in listaOrdenada:
        #Las claves serán nuestras columnas
        nuevaLista[keys] = listaCompleta[keys]

    #Creamos la nueva figura
    x = list(nuevaLista.values())
    y = nuevaLista.keys()
    plt.figure(figsize=(10,6))
    plt.bar(x,y,color='darkorchid')
    plt.xticks(rotation=25)
    #Generamos un numero random para que los ficheros nunca sean iguales
    sufix = random.randint(1, 1000)
    #Pasamos la ruta a una variable
    ruta = f"static/src/figura{sufix}.png"

    plt.savefig(ruta,bbox_inches='tight',dpi=100)
    return ruta







