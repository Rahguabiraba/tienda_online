#Importamos la libreria pandas
import pandas as pd

#Usamos un dataframe vacío
productos = pd.DataFrame()
#Pasamos todo el contenido del fichero a una variable
fichero = pd.read_csv(f"datos/Productos.csv")
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








