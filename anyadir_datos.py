import pandas as pd
import sqlite3

#conectamos a nuestra base de datos ya creada y con sus tablas
conexion = sqlite3.connect("videojuegos.db")
cursor = conexion.cursor()

#Con estas lineas siguientes vamos a cargar el excel con los datos
archivo_datos= "Datos_Tablas_Videojuegos.xlsx"
xls = pd.ExcelFile(archivo_datos)

#Cargamos las hojas con datos en la tabla SQLite3
for hojan in xls.sheet_names:
    df = pd.read_excel(xls, sheet_name=Usuario)
    df.to_sql(Usuario, conexion, if_exists="replace", index=False)

conexion.close()
print("Datos importados correctamente")