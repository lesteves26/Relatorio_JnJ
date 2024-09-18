import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

st.set_page_config(page_title="Relatório Geral J&J Brasil")

st.title("Relatório Geral J&J Brasil")


# Criando o menu lateral - sidebar
with st.container():
    st.sidebar.title("Grupo Operacional")

    grupo = ['Global Service', 'Innovative Medicine', 'MedTech', 'Surgical Vision', 'Vision Care']
    grupo_selecionado = st.sidebar.selectbox('Selecione o Grupo', grupo)
    st.header(f"{grupo_selecionado}")

    #ano = ['2023', '2024']
    #ano_selecionado = st.sidebar.multiselect('Selecione o ano', ano)

    logo = (r'C:\Users\Lucas Esteves Pereir\Documents\Relatorio JnJ - Streamlit\Relatorio_JnJ\Imagem1 vamover.png')
    
    st.logo(logo)


#Gráficos
eventos = pd.read_excel(r'C:\Users\Lucas Esteves Pereir\Documents\Relatorio JnJ - Streamlit\Relatorio_JnJ\template real.xlsx')

eventos['data_nova'] = pd.to_datetime(eventos['Data'], errors='coerce')

eventos['Ano'] = eventos['Data'].dt.year
eventos['Mês'] = eventos['Data'].dt.to_period('M')

anos = eventos['Ano'].dropna().unique()

ano_selecionado = st.sidebar.multiselect('Selecionar ano', anos, default=anos)

eventos_filtrados = eventos[eventos['Ano'].isin(ano_selecionado)]

eventos_por_mes = eventos_filtrados.groupby (['Mês', 'Tipo']).size().unstack(fill_value=0)

eventos_por_mes.index = eventos_por_mes.index.to_timestamp()
eventos_por_mes = eventos_por_mes.sort_index()


st.line_chart(eventos_por_mes)