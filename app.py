import streamlit as st
import joblib
import pandas as pd

#interacao usuario e modelo para previsao de preços
# Carregando o modelo 
modelo = joblib.load('modelo_carros_simples.pkl')

st.title("🚗 Prevendo Preços de Carros")
st.write("Insira os dados do veículo abaixo para estimar o valor de mercado.")

# Criando os campos para o usuário digitar
col1, col2 = st.columns(2) 
with col1:
    horsepower = st.number_input("Cavalos de Potência (Horsepower)", min_value=50, max_value=500, value=100)
    enginesize = st.number_input("Tamanho do Motor", min_value=50, max_value=350, value=120)
with col2:
    highwaympg = st.number_input("Consumo na Estrada (MPG)", min_value=10, max_value=60, value=30)
    curbweight = st.number_input("Peso do Carro (lbs)", min_value=1000, max_value=5000, value=2500)

if st.button("💰 Calcular Preço"):
    dados_novos = pd.DataFrame([[horsepower, enginesize, highwaympg, curbweight]], 
                               columns=['horsepower', 'enginesize', 'highwaympg', 'curbweight'])
    
    preco_previsto = modelo.predict(dados_novos)[0]
    
    st.success(f"O preço estimado é: US$ {preco_previsto:,.2f}")