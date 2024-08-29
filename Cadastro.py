import streamlit as st
import pandas as pd
from datetime import date

# Função para gravar os dados no arquivo CSV
def gravar_dados(nome, data_nasc, sexo):
    # Verifica se o nome foi preenchido e a data de nascimento é válida
    if nome and data_nasc <= date.today():
        with open("cliente.csv", "a", encoding="utf-8") as file:
            # Escreve os dados no arquivo CSV
            file.write(f"{nome}, {data_nasc}, {sexo}\n")
        
        # Define o estado de sucesso para True
        st.session_state["sucesso"] = True
        # Limpa os campos de entrada redefinindo as chaves no estado da sessão
        st.session_state["nome_cliente"] = ""
        st.session_state["data_nasc"] = date.today()
        st.session_state["sexo"] = " "
    else:
        # Define o estado de sucesso para False
        st.session_state["sucesso"] = False

# Configuração da página do Streamlit
st.set_page_config(
    page_title="Cadastro pessoal",
    page_icon="🔰"
)

# Título da página
st.title("Cadastro de cliente")
st.divider()

# Campos de entrada
nome = st.text_input("Digite seu nome", key="nome_cliente")
data_nasc = st.date_input("Data nascimento",format="DD/MM/YYYY", key="data_nasc")
sexo = st.selectbox("Gênero", ["Feminino", "Masculino", " "], key="sexo")

# Botão de cadastro
btn_cadastrar = st.button("Cadastrar", on_click=gravar_dados, args=[nome, data_nasc, sexo])

# Mensagem de sucesso ou erro após o cadastro
if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!", icon="✔")
    else:
        st.error("Houve algum problema no cadastro!", icon="❌")
