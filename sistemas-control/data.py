import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Importar la base de datos featuredata
archivo = "caracteristicas/featuredata.xlsx"
base_datos = pd.read_excel(archivo)
print(base_datos)

# Obtener el grafico de dispersion
valoresAspec = base_datos[['AspectRatio']]
valoresDuracion = base_datos[['Duration']]

ax = plt.scatter(x=valoresAspec, y=valoresDuracion)
plt.xlabel("Aspect Ratio")
plt.ylabel("Duration")
plt.title("Grafico de dispersion")
plt.show()

# Mejorar el grafico de dispersion
ax2 = sns.scatterplot(x="AspectRatio", y="Duration",
                      hue="Character", data=base_datos)

plt.savefig("caracteristicas/grafico.png")
