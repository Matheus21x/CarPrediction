import pandas as pd

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

print(df['brand'].unique())
