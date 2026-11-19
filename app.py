import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="ACIDENTES", layout="wide", page_icon="🏙️")

caminho_arquivo = "acidentes.xlsx"

xlsx = pd.ExcelFile(caminho_arquivo)
dados_totais = []
for sheet in xlsx.sheet_names:
    df = pd.read_excel(xlsx, sheet_name=sheet)
    dados_totais.append(df)

st.dataframe(df)

dias = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]

diasemana = (
    df.groupby("dia_semana", as_index=False)["quantidade_pessoas"].sum()
)

st.dataframe(diasemana)