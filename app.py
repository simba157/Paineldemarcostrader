import streamlit as st
import pandas as pd
import requests

# Configurações da página
st.set_page_config(
    page_title="Painel Asiático em Tempo Real", 
    layout="wide"
)

st.title("📈 Painel Asiático em Tempo Real")

# Função para buscar seus sinais (substitua a URL pela sua API ou lógica de coleta)
@st.cache_data(ttl=30)
def fetch_asia_signals():
    # Exemplo: GET na sua API que retorna JSON com campos: time, pair, signal, confidence
    url = "https://sua-api-de-sinais.com/asia"
    resp = requests.get(url, timeout=5)
    data = resp.json()
    return pd.DataFrame(data)

# Carrega os sinais e exibe em tabela
try:
    df = fetch_asia_signals()
    if df.empty:
        st.warning("Nenhum sinal disponível no momento.")
    else:
        st.dataframe(
            df, 
            use_container_width=True, 
            hide_index=True
        )
except Exception as e:
    st.error(f"Erro ao buscar sinais: {e}")

# Rodapé com atualização automática (a cada 30s, pelo cache acima)
st.caption("Atualização automática a cada 30 segundos.")
