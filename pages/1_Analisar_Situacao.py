import streamlit as st
from core.base_conhecimento import carregar_base
from core.extrator_fatos import extrair_fatos
from core.regras import SistemaAssedio, FatoAssedio
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
        with st.spinner("Analisando o seu relato com base no Guia da Ouvidoria..."):
            base_conhecimento = carregar_base()

            if not base_conhecimento:
                st.error("Erro ao carregar a base de conhecimento.")
            else:
                fatos = extrair_fatos(relato_usuario)

                engine = SistemaAssedio()
                engine.reset()
                engine.declare(FatoAssedio(**fatos))
                engine.run()

                resultados = engine.get_resultados()
                explicacoes = engine.explicador.gerar_explicacoes()

                classificacao_final = resultados[0] if resultados else "Não foram encontrados indícios claros de assédio."
                condutas = [r for r in resultados if r != classificacao_final]

                recomendacoes, canais = gerar_recomendacao(classificacao_final, base_conhecimento)

                resultado_analise = formatar_relatorio(
                    classificacao_final, condutas, recomendacoes, canais, base_conhecimento
                )

        st.markdown("---")
        st.subheader("Resultado da Análise")

        if "Não foram encontrados" in resultado_analise['classificacao']:
            st.warning(f"**Classificação Preliminar:** {resultado_analise['classificacao']}", icon="⚠️")
        else:
            st.error(f"**Classificação Preliminar:** {resultado_analise['classificacao']}", icon="🚨")

        with st.container(border=True):
            st.subheader("Condutas Identificadas:")
            for c in resultado_analise['condutas_identificadas']:
                st.markdown(f"- {c}")

        with st.container(border=True):
            st.subheader("Regras Disparadas:")
            for e in explicacoes:
                st.markdown(f"- {e}")

        with st.container(border=True):
            st.subheader("Fundamentação:")
            st.markdown(f"_{resultado_analise['fundamentacao']}_")

        with st.container(border=True):
            st.subheader("Orientações e Recomendações:")
            for r in resultado_analise['recomendacoes']:
                st.markdown(f"✅ {r}")

        with st.container(border=True):
            st.subheader("Canais Adequados:")
            for canal in resultado_analise['canais']:
                st.markdown(f"➡️ {canal}")
    else:
        st.warning("Por favor, escreva a descrição da situação antes de analisar.")
