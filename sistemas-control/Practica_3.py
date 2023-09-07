# importar librerías
import matplotlib.pyplot as plt
import pandas as pd

# nombres de los archivos
archivos = ["J.xlsx", "M.xlsx", "V.xlsx"]

# iterar sobre los archivos
for archivo in archivos:
    # importar datos de archivo excel
    datos = pd.read_excel("Datos/" + archivo)

    # Utilizar solo dos columnas de datos
    valores = datos[['X', 'Y']]

    # Graficar la información X,Y
    ax = valores.plot(x='X', y='Y')
    ax.set_title("Datos de " + archivo[:-5])

    plt.show()

    datos.X = datos.X*1.5

    datos.Time = (datos.Time-datos.Time[0])/1000
    tx = datos.plot(x='Time', y='X')

    # Extracción de características
    # Obtner el tiempo de escritura de cada letra
    elementos = len(datos)
    duracion = datos.Time[elementos-1]

    # Relación de rango
    rangoY = max(datos.Y)-min(datos.Y)
    rangoX = max(datos.X)-min(datos.X)
    aratio = rangoY/rangoX

    # Exportar la base de datos
    datos.to_excel("Datos/Nuevos/base_datos" + archivo[:-5] + ".xlsx")

    # Base de datos sin indices
    datos.to_excel("Datos/Nuevos/base_datos" +
                   archivo[:-5] + "2.xlsx", index=False)
