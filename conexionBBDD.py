import sqlite3 as sql

def registrarGraficos(ruta):
    try:
        conector = sql.connect("database/graficos.db")
        cursor = conector.cursor()
        cursor.execute(f"INSERT INTO figuras (imagen) VALUES ('{ruta}')")
        conector.commit()
        conector.close()
        return 
    except Exception as ex:
        print(ex)

def getAllGraficos():
    try:
        conector = sql.connect("database/graficos.db")
        cursor = conector.cursor()
        cursor.execute(f"SELECT * FROM figuras")
        datos = cursor.fetchall()
        conector.commit()
        conector.close()

        #La funcion nos devuelve todos los datos, pero vamos a necesitar solamente de las rutas
        rutas = []
        for i in range(0,len(datos)):
            rutas.append(datos[i][1])

        return rutas
    except Exception as ex:
        print(ex)