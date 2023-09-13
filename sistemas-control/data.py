import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.metrics import ConfusionMatrixDisplay

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

# Importar datos de test
archivo3 = "caracteristicas/testdata.xlsx"
base_datos2 = pd.read_excel(archivo3)
print(base_datos2)

# Asignar las columnas de los archivos en excel
X_text = base_datos2[['AspectRatio', 'Duration']].values
Y_text = base_datos2[['Character']]

X_train = base_datos[['AspectRatio', 'Duration']]
Y_train = base_datos[['Character']].values

# Generar el modelo usando el algoritmo KNN
n_neighbors = 15
knn = KNeighborsClassifier(n_neighbors, weights='uniform')
knn.fit(X_train, Y_train)

# Predecir los valores de test
prediccion = knn.predict(X_text)
print(prediccion, '\n')

# Evaluar el modelo
isCorrect = prediccion == base_datos2['Character']
print(isCorrect, '\n')

# Imprimir la precisión del modelo
print("Precisión del modelo de entrenamiento: {:.2f}".format(
    knn.score(X_train, Y_train)))
print("Precisión del conjunto de evaluación {:.2f}".format(
    knn.score(X_text, Y_text)))

print(confusion_matrix(Y_text, prediccion), '\n')

confusion_matrix = metrics.confusion_matrix(Y_text, prediccion)
cm_display = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix, display_labels=['J', 'M', 'V'])

cm_display.plot()
plt.show()

# Generar un reporte de clasiicación
print(metrics.classification_report(Y_text, prediccion))
