import streamlit as st
import sqlite3

# Função para conectar ao banco de dados
def connect_to_db():
    return sqlite3.connect('spaceship.db')

# Função para criar um novo registro
def create_record(conn, table):
    cursor = conn.cursor()
    st.write(f"Adicionar novo registro na tabela {table}")

    if table == "train":
        PassengerId = st.text_input("PassengerId (ex: 0001_01):")
        HomePlanet = st.text_input("HomePlanet (ex: Earth):")
        CryoSleep = st.selectbox("CryoSleep", [0, 1], format_func=lambda x: "Sim" if x else "Não")
        Cabin = st.text_input("Cabin (ex: B/0/P):")
        Destination = st.text_input("Destination (ex: TRAPPIST-1e):")
        Age = st.number_input("Age", min_value=0)
        VIP = st.selectbox("VIP", [0, 1], format_func=lambda x: "Sim" if x else "Não")
        RoomService = st.number_input("RoomService", min_value=0.0)
        FoodCourt = st.number_input("FoodCourt", min_value=0.0)
        ShoppingMall = st.number_input("ShoppingMall", min_value=0.0)
        Spa = st.number_input("Spa", min_value=0.0)
        VRDeck = st.number_input("VRDeck", min_value=0.0)
        Name = st.text_input("Name (ex: Juanna Vines):")
        Transported = st.selectbox("Transported", [0, 1], format_func=lambda x: "Sim" if x else "Não")

        if st.button("Adicionar Registro"):
            cursor.execute(
                '''INSERT INTO train (PassengerId, HomePlanet, CryoSleep, Cabin, Destination, Age, VIP,
                RoomService, FoodCourt, ShoppingMall, Spa, VRDeck, Name, Transported)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (PassengerId, HomePlanet, CryoSleep, Cabin, Destination, Age, VIP, RoomService, FoodCourt,
                ShoppingMall, Spa, VRDeck, Name, Transported)
            )
            conn.commit()
            st.success("Registro criado com sucesso!")

    else:
        PassengerId = st.text_input("PassengerId (ex: 0001_01):")
        HomePlanet = st.text_input("HomePlanet (ex: Earth):")
        CryoSleep = st.selectbox("CryoSleep", [0, 1], format_func=lambda x: "Sim" if x else "Não")
        Cabin = st.text_input("Cabin (ex: B/0/P):")
        Destination = st.text_input("Destination (ex: TRAPPIST-1e):")
        Age = st.number_input("Age", min_value=0)
        VIP = st.selectbox("VIP", [0, 1], format_func=lambda x: "Sim" if x else "Não")
        RoomService = st.number_input("RoomService", min_value=0.0)
        FoodCourt = st.number_input("FoodCourt", min_value=0.0)
        ShoppingMall = st.number_input("ShoppingMall", min_value=0.0)
        Spa = st.number_input("Spa", min_value=0.0)
        VRDeck = st.number_input("VRDeck", min_value=0.0)
        Name = st.text_input("Name (ex: Juanna Vines):")

        if st.button("Adicionar Registro"):
            cursor.execute(
                '''INSERT INTO test_submit (PassengerId, HomePlanet, CryoSleep, Cabin, Destination, Age, VIP,
                RoomService, FoodCourt, ShoppingMall, Spa, VRDeck, Name)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (PassengerId, HomePlanet, CryoSleep, Cabin, Destination, Age, VIP, RoomService, FoodCourt,
                ShoppingMall, Spa, VRDeck, Name)
            )
            conn.commit()
            st.success("Registro criado com sucesso!")

# Função para ler os registros
def read_records(conn, table):
    cursor = conn.cursor()
    # Selecionando os primeiros 10 registros
    cursor.execute(f"SELECT * FROM {table} ORDER BY PassengerId ASC LIMIT 10")
    first_10 = cursor.fetchall()
    # Selecionando os últimos 10 registros
    cursor.execute(f"SELECT * FROM {table} ORDER BY PassengerId DESC LIMIT 10")
    last_10 = cursor.fetchall()

    st.write(f"Primeiros 10 registros da tabela {table}")
    st.table(first_10)
    st.write(f"Últimos 10 registros da tabela {table}")
    st.table(last_10)

# Função principal do aplicativo Streamlit
def main():
    st.title("Aplicativo CRUD para o Banco de Dados SpaceShip")
    conn = connect_to_db()

    # Seleção da tabela
    table = st.selectbox("Selecione a tabela para operar:", ["train", "test_submit"])
    
    # Seleção da operação
    operation = st.selectbox("Escolha uma operação:", ["Criar", "Ler"])

    if operation == "Criar":
        create_record(conn, table)
    elif operation == "Ler":
        read_records(conn, table)

    conn.close()

if __name__ == "__main__":
    main()
