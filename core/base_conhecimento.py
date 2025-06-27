import json
import streamlit as st
from typing import Dict, Any
@st.cache_data
def carregar_base() -> Dict[str, Any]:
    try:
        with open('data/Guia_de_Bolso_Assedio_Moral.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("ERRO CRÍTICO: Arquivo ''data/Guia_de_Bolso_Assedio_Moral.json' não foi encontrado.")
        return {}
