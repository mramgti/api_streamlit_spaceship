import streamlit as st
import pandas as pd
import joblib
from xgboost import XGBClassifier

# Carregar os modelos salvos
logistic_model = joblib.load('logistic_regression_model.pkl')
knn_model = joblib.load('knn_model.pkl')
gb_model = joblib.load('gradient_boosting_model.pkl')
xgb_model = joblib.load('xgboost_model.pkl')

# Função para fazer previsões com base na entrada do usuário
def make_prediction(model, input_data):
    # Previsão do modelo
    prediction = model.predict(input_data)
    return prediction

# Interface do usuário com Streamlit
st.title("Previsão de Transporte da Espaçonave Titanic")

# Criar inputs para o usuário
home_planet = st.selectbox("Home Planet", ['Earth', 'Mars', 'Europa'])
cryosleep = st.selectbox("CryoSleep", [True, False])
destination = st.selectbox("Destination", ['TRAPPIST-1e', '55 Cancri e', 'PSO J318.5-22'])
age = st.number_input("Age", min_value=0, max_value=100, value=25)
vip = st.selectbox("VIP", [True, False])
room_service = st.number_input("Room Service", min_value=0, value=0)
food_court = st.number_input("Food Court", min_value=0, value=0)
shopping_mall = st.number_input("Shopping Mall", min_value=0, value=0)
spa = st.number_input("Spa", min_value=0, value=0)
vr_deck = st.number_input("VR Deck", min_value=0, value=0)
grouped = st.selectbox("Grouped", [True, False])
deck = st.selectbox("Deck", ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
side = st.selectbox("Side", ['Port', 'Starboard'])
has_expenses = st.selectbox("Has Expenses", [True, False])
is_embryo = st.selectbox("Is Embryo", [True, False])

# Transformar dados de entrada em um DataFrame
input_data = pd.DataFrame({
    'HomePlanet': [home_planet],
    'CryoSleep': [cryosleep],
    'Destination': [destination],
    'Age': [age],
    'VIP': [vip],
    'RoomService': [room_service],
    'FoodCourt': [food_court],
    'ShoppingMall': [shopping_mall],
    'Spa': [spa],
    'VRDeck': [vr_deck],
    'Grouped': [grouped],
    'Deck': [deck],
    'Side': [side],
    'Has_expenses': [has_expenses],
    'Is_Embryo': [is_embryo]
})

# Codificar as entradas usando get_dummies
input_data_encoded = pd.get_dummies(input_data)
# Obter as colunas que estavam presentes no conjunto de treinamento
training_columns = joblib.load('training_columns.pkl') # Carregue as colunas do treinamento original
# Ajustar as colunas do input_data_encoded para ter as mesmas colunas do conjunto de treinamento
input_data_encoded = input_data_encoded.reindex(columns=training_columns, fill_value=0)

# Fazer previsões
if st.button('Predict'):
    with st.spinner('Making predictions...'):
        logistic_pred = make_prediction(logistic_model, input_data_encoded)
        knn_pred = make_prediction(knn_model, input_data_encoded)
        gb_pred = make_prediction(gb_model, input_data_encoded)
        xgb_pred = make_prediction(xgb_model, input_data_encoded)

        st.write(f'Logistic Regression Prediction: {logistic_pred[0]}')
        st.write(f'KNN Prediction: {knn_pred[0]}')
        st.write(f'Gradient Boosting Prediction: {gb_pred[0]}')
        st.write(f'XGBoost Prediction: {xgb_pred[0]}')
