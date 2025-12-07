import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

df = pd.read_csv(r'C:\Users\Matheus\OneDrive\Desktop\ML-CARPRED\CarPrice_Assignment.csv')

#Criei uma nova coluna Brand para armazenar as marcas
df['brand'] = df['CarName'].apply(lambda x: x.split()[0])

#Removi a Coluna car_ID e symboling e CarName
df.drop(['car_ID' , 'symboling', 'CarName'], axis=1, inplace=True)

#todas as letras minusculas da brand para concertar erros ortograficos
df['brand'] = df['brand'].str.lower()
df['brand'] = df['brand'].replace({
    'toyouta': 'toyota',
    'vokswagen': 'volkswagen',
    'vw': 'volkswagen',
    'porcshce': 'porsche',
    'maxda': 'mazda'
})

#transfomar colunas de texto em binario
df = pd.get_dummies(df, columns=[
    'fueltype', 'aspiration', 'doornumber', 'carbody',
    'drivewheel', 'enginelocation', 'enginetype',
    'cylindernumber', 'fuelsystem', 'brand'
], drop_first=True)

#definindo X e Y e treinos/testes
x = df.drop('price', axis=1) 
y = df['price']
x_train, x_test, y_train, y_test = train_test_split(x,y)

#instanciando o modelo selecionado
modelo = LinearRegression()

#treinando o modelo com os valores de treino
modelo.fit(x_train, y_train)

#predicao do modelo com os valores de teste 
predicoes = modelo.predict(x_test)


plt.figure(figsize=(7, 7))
plt.scatter(y_test, predicoes)  
plt.xlabel("Valores reais (y_test)")
plt.ylabel("Previsões (predicoes)")
plt.title("Valores reais vs Previsões")
min_val = min(y_test.min(), predicoes.min())
max_val = max(y_test.max(), predicoes.max())
plt.plot([min_val, max_val], [min_val, max_val])
plt.show()

mae = mean_absolute_error(y_test, predicoes)
mse = mean_squared_error(y_test, predicoes)
rmse = np.sqrt(mse)

print("MAE :", mae)
print("MSE :", mse)
print("RMSE:", rmse)