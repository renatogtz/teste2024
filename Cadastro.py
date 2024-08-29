import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados (nome, data_nasc, Sexo):
    if nome and data_nasc <= date.today():
        with open("cliente.csv" ,"a" ,encoding= "utf-8") as file:
            file.write(f"{nome}, {data_nasc}, {Sexo} \n")
            
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False   

st.set_page_config(
    page_title="Cadastro pessoal" , 
    page_icon="🔰"
)

st.title("Cadastro de cliente")
st.divider( )

nome = st.text_input("Digite seu nome" ,
                     key="nome_cliente")
data_nasc = st.date_input("Data nascimento" ,format="DD/MM/YYYY")
Sexo = st.selectbox("Genero" ,
                    ["Feminino", "Masculino"])

btn_cadastrar =st.button("Cadastrar" ,
                         on_click= gravar_dados,
                         args=[nome, data_nasc, Sexo])
if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastaado com sucesso!" ,
                   icon="✔")
    else:
        st.error("Houve algum problema no cadastro!" ,
                 icon= "❌") 

