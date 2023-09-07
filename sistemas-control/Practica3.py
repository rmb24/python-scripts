# importar librerías
import matplotlib.pyplot as plt
import pandas as pd

# importar datos de archivo excel
J = "Datos/J.xlsx"
M = "Datos/M.xlsx"
V = "Datos/V.xlsx"
base_datosJ = pd.read_excel(J)
dato_M = pd.read_excel(M)
base_datosV = pd.read_excel(V)

# Verificar la importación de datos
# print(datos)

# Utilizar solo dos columnas de datos
valores = base_datosJ[['X', 'Y']]
print(valores)

# Graficar la información X,Y
ax = valores.plot(x='X', y='Y')
ax.set_title("Datos de J")

plt.show()

base_datosJ.X = base_datosJ.X*1.5
print(base_datosJ)

base_datosJ.Time = (base_datosJ.Time-base_datosJ.Time[0])/1000
tx = base_datosJ.plot(x='Time', y='X')
print(base_datosJ)

# Extracción de características
# Obtner el tiempo de escritura de cada letra
elementos = len(base_datosJ)
duracion = base_datosJ.Time[elementos-1]

# Relación de rango
rangoY = max(base_datosJ.Y)-min(base_datosJ.Y)
rangoX = max(base_datosJ.X)-min(base_datosJ.X)
aratio = rangoY/rangoX

# Exportar la base de datos
base_datosJ.to_excel("Datos/base_datosJ.xlsx")
# importar librerías

# importar datos de archivo excel
J = "Datos/J.xlsx"
M = "Datos/M.xlsx"
V = "Datos/V.xlsx"
base_datosJ = pd.read_excel(J)
base_datosM = pd.read_excel(M)
base_datosV = pd.read_excel(V)

# Utilizar solo dos columnas de datos
valores_J = base_datosJ[['X', 'Y']]
valores_M = base_datosM[['X', 'Y']]
valores_V = base_datosV[['X', 'Y']]

# Graficar la información X,Y
ax = valores_J.plot(x='X', y='Y')
ax.set_title("Datos de J")
plt.show()

ax = valores_M.plot(x='X', y='Y')
ax.set_title("Datos de M")
plt.show()

ax = valores_V.plot(x='X', y='Y')
ax.set_title("Datos de V")
plt.show()

# Procesar datos de J
base_datosJ.X = base_datosJ.X*1.5
base_datosJ.Time = (base_datosJ.Time-base_datosJ.Time[0])/1000

# Extracción de características
# Obtner el tiempo de escritura de cada letra
elementos_J = len(base_datosJ)
duracion_J = base_datosJ.Time[elementos_J-1]

# Relación de rango
rangoY_J = max(base_datosJ.Y)-min(base_datosJ.Y)
rangoX_J = max(base_datosJ.X)-min(base_datosJ.X)
aratio_J = rangoY_J/rangoX_J

# Exportar la base de datos
base_datosJ.to_excel("base_datosJ.xlsx")

# Base de datos sin indices
base_datosJ.to_excel("base_datosJ2.xlsx", index=False)

# Procesar datos de M
base_datosM.X = base_datosM.X*1.5
base_datosM.Time = (base_datosM.Time-base_datosM.Time[0])/1000

# Extracción de características
# Obtner el tiempo de escritura de cada letra
elementos_M = len(base_datosM)
duracion_M = base_datosM.Time[elementos_M-1]

# Relación de rango
rangoY_M = max(base_datosM.Y)-min(base_datosM.Y)
rangoX_M = max(base_datosM.X)-min(base_datosM.X)
aratio_M = rangoY_M/rangoX_M

# Exportar la base de datos
base_datosM.to_excel("base_datosM.xlsx")

# Base de datos sin indices
base_datosM.to_excel("base_datosM2.xlsx", index=False)

# Procesar datos de V
base_datosV.X = base_datosV.X*1.5
base_datosV.Time = (base_datosV.Time-base_datosV.Time[0])/1000

# Extracción de características
# Obtner el tiempo de escritura de cada letra
elementos_V = len(base_datosV)
duracion_V = base_datosV.Time[elementos_V-1]

# Relación de rango
rangoY_V = max(base_datosV.Y)-min(base_datosV.Y)
rangoX_V = max(base_datosV.X)-min(base_datosV.X)
aratio_V = rangoY_V/rangoX_V

# Exportar la base de datos
base_datosV.to_excel("base_datosV.xlsx")

# Base de datos sin indices
base_datosV.to_excel("base_datosV2.xlsx", index=False)
# Base de datos sin indices
base_datosJ.to_excel("base_datosJ2.xlsx", index=False)
