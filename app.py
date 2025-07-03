import streamlit as st

st.set_page_config(
    page_title="Sistema Especialista - Análise de Assédio Moral",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.ufape.edu.br/br/ouvidoria',
        'Report a bug': "https://github.com/RWilker87/Assedio-Moral-IA/issues",
        'About': """
        **Sistema Especialista para Análise de Casos de Assédio Moral na UFAPE**

        Desenvolvido como projeto acadêmico para a disciplina de Inteligência Artificial.
        Este sistema visa orientar e informar a comunidade acadêmica, com base nos 
        documentos oficiais da universidade.
        """
    }
)
st.title("Sistema Especialista para Análise de Casos de Assédio Moral")
st.subheader("Universidade Federal do Agreste de Pernambuco (UFAPE)")

st.markdown("---")

st.markdown(
    """
    ### Bem-vindo(a)!

    Utilize o menu na barra lateral à esquerda para navegar pelas funcionalidades:

    - **Analisar Situação:** Descreva um caso para que o sistema o analise com base nos
      regulamentos da UFAPE e forneça uma orientação.
    - **Consultar o Guia:** Explore o conteúdo do "Guia de Bolso sobre Assédio Moral"
      para tirar dúvidas específicas.
    - **Sobre o Projeto:** Conheça mais sobre os objetivos e a estrutura deste trabalho.
    """
)

st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; font-size: 0.9em;">
        <p>Desenvolvido para a disciplina de Inteligência Artificial - UFAPE</p>
        <p>Baseado no <strong>Guia de Bolso sobre Assédio Moral</strong> e no <strong>Regimento Geral da UFAPE</strong>.</p>
    </div>
    """,
    unsafe_allow_html=True
)