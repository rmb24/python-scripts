import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn.metrics import ConfusionMatrixDisplay

# Importar la base de datos featuredata
archivo = "features.xlsx"
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
                      hue="Character", data=base_datos, palette="Set2")

plt.savefig("grafico.png")

# # Importar datos de test
archivo3 = "tesdataletters.xlsx"
base_datos2 = pd.read_excel(archivo3)
print(base_datos2)

# # Asignar las columnas de los archivos en excel
X_test = base_datos2[['AspectRatio', 'Duration']].values
Y_test = base_datos2[['Character']]

X_train = base_datos[['AspectRatio', 'Duration']]
Y_train = base_datos[['Character']].values

# Generar el modelo usando el algoritmo KNN
n_neighbors = 28
knn = KNeighborsClassifier(n_neighbors, weights='uniform')
knn.fit(X_train, Y_train)

# Predecir los valores de test
prediccion = knn.predict(X_test)
print(prediccion, '\n')

# Evaluar el modelo
isCorrect = prediccion == base_datos2['Character']
print(isCorrect, '\n')

# Imprimir la precisión del modelo
print("Precisión del modelo de entrenamiento: {:.2f}".format(
    knn.score(X_train, Y_train)))
print("Precisión del conjunto de evaluación {:.2f}".format(
    knn.score(X_test, Y_test)))

print(confusion_matrix(Y_test, prediccion), '\n')

confusion_matrix = metrics.confusion_matrix(Y_test, prediccion)
cm_display = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix, display_labels=['A', 'C', 'E', 'G', 'I', 'K', 'M', 'O', 'Q', 'S', 'U', 'W', 'Y'])

cm_display.plot()
plt.show()

# Generar un reporte de clasiicación
print(metrics.classification_report(Y_test, prediccion))

# Grafica de sensibilidad

knn_range = range(1, 35)
scores = []
for k in knn_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, Y_train)
    scores.append(knn.score(X_test, Y_test))

plt.figure()
plt.xlabel('k')
plt.ylabel('accuracy')
plt.scatter(knn_range, scores)
plt.xticks([0, 5, 10, 15, 20, 25, 30, 35])
plt.show()
