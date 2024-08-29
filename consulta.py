import streamlit as st
import pandas as pd

dados = pd.read_csv("cliente.csv")

st.title("Cliente cadastro")
st.divider()
st.dataframe(dados)
