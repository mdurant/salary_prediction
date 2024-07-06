import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm

# Cargar el dataset
data = pd.read_csv("Salary_Data.csv")
print(data.head())

# Verificar valores nulos
print(data.isnull().sum())

# Visualización de la relación entre salario y experiencia
figure = px.scatter(data_frame=data,
                    x="Salary",
                    y="YearsExperience",
                    size="YearsExperience",
                    trendline="ols")
figure.show()

# Dividir los datos en conjuntos de entrenamiento y prueba
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

x = np.asarray(data[["YearsExperience"]])
y = np.asarray(data[["Salary"]])
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

# Entrenar el modelo
model = LinearRegression()
model.fit(xtrain, ytrain)

# Predicción de salario
a = float(input("Años de Experiencia: "))
features = np.array([[a]])
print("Predicción de Sueldo =", model.predict(features))