import streamlit as st
import time
from core.base_conhecimento import carregar_base
from core.classificador import classificar_situacao
from core.motor_recomendacao import gerar_recomendacao
from core.gerador_relatorio import formatar_relatorio

st.set_page_config(page_title="Análise de Situação", page_icon="🔍", layout="wide")

st.title("🔍 Análise de Situação")
st.markdown("---")

st.info(
    """
    **Instruções:** Descreva a situação que você vivenciou ou presenciou da forma mais detalhada possível.
    Inclua informações sobre **quem** são os envolvidos (ex: superior, colega, etc.), **o que** aconteceu,
    **onde** e **quando**. Quanto mais detalhes, mais precisa será a análise do sistema.
    """
)

relato_usuario = st.text_area(
    "Descreva a situação aqui:",
    height=250,
    placeholder="Exemplo: Meu superior costuma me sobrecarregar de tarefas, me entrega demandas urgentes no fim do expediente e já me criticou de forma exagerada na frente de outros colegas."
)

if st.button("Analisar Situação", type="primary"):
    if relato_usuario.strip():
        with st.spinner("Analisando o seu relato com base nos regulamentos... Por favor, aguarde."):
            
            #Carregar a base de conhecimento
            base_conhecimento = carregar_base()
            
            if not base_conhecimento:
                 st.error("Falha ao carregar a base de conhecimento. A análise não pode continuar.")
            else:
                #Classificar a situação
                classificacao, condutas = classificar_situacao(relato_usuario, base_conhecimento)
                
                #Gerar recomendações com base na classificação
                recomendacoes, canais = gerar_recomendacao(classificacao, base_conhecimento)
                
                #Formatar o relatório final
                resultado_analise = formatar_relatorio(classificacao, condutas, recomendacoes, canais, base_conhecimento)


        st.markdown("---")
        st.subheader("Resultado da Análise")
        
        #Exibe o relatório gerado pela lógica real
        if "Não foram encontrados" in resultado_analise['classificacao']:
             st.warning(f"**Classificação Preliminar:** {resultado_analise['classificacao']}", icon="⚠️")
        else:
             st.error(f"**Classificação Preliminar:** {resultado_analise['classificacao']}", icon="🚨")


        with st.container(border=True):
            st.subheader("Condutas Identificadas (com base no Guia da Ouvidoria):")
            for conduta in resultado_analise['condutas_identificadas']:
                st.markdown(f"- {conduta}")

        with st.container(border=True):
            st.subheader("Fundamentação:")
            st.markdown(f"_{resultado_analise['fundamentacao']}_")

        with st.container(border=True):
            st.subheader("Orientações e Recomendações:")
            for rec in resultado_analise['recomendacoes']:
                st.markdown(f"✅ {rec}")

        with st.container(border=True):
            st.subheader("Canais Adequados:")
            for canal in resultado_analise['canais']:
                st.markdown(f"➡️ {canal}")


    else:
        st.warning("Por favor, descreva a situação no campo de texto antes de analisar.")

