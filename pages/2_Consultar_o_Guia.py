import streamlit as st
import json

def carregar_base_conhecimento():
    try:
        with open('data/Guia_de_Bolso_Assedio_Moral.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("Arquivo 'base_conhecimento.json' não encontrado. Crie o arquivo na pasta 'data'.")
        return {
            "definicao_geral": {
                "titulo": "O que é Assédio Moral?",
                "conteudo": "É a violação da dignidade ou integridade psíquica ou física de outra pessoa por meio de conduta abusiva...",
                "pagina_guia": 11
            },
            "tipos_de_assedio": [
                {
                    "tipo": "Assédio Moral Vertical",
                    "descricao": "Ocorre em uma relação de hierarquia (descendente ou ascendente) entre agressor(a) e assediado(a).",
                    "pagina_guia": 22
                },
                {
                    "tipo": "Assédio Moral Horizontal",
                    "descricao": "Ocorre entre pessoas de mesma hierarquia.",
                    "pagina_guia": 22
                }
            ],
            "condutas": [
                 {
                    "conduta": "Sobrecarga de Tarefas",
                    "descricao": "Sobrecarregar constantemente a pessoa com uma quantidade excessiva de tarefas em comparação aos colegas.",
                    "pagina_guia": 14
                }
            ]
        }

st.set_page_config(page_title="Consultar o Guia", page_icon="📚", layout="wide")

st.title("📚 Consulta ao Guia de Bolso sobre Assédio Moral")
st.markdown("---")

#Carrega os dados
base_conhecimento = carregar_base_conhecimento()

if base_conhecimento:
    #Cria uma lista de todos os tópicos para exibição
    topicos_guia = []
    if 'definicao_geral' in base_conhecimento:
        topicos_guia.append(base_conhecimento['definicao_geral']['titulo'])
    if 'tipos_de_assedio' in base_conhecimento:
        for item in base_conhecimento['tipos_de_assedio']:
            topicos_guia.append(item['tipo'])
    if 'condutas' in base_conhecimento:
         for item in base_conhecimento['condutas']:
            topicos_guia.append(item['conduta'])
    if 'o_que_fazer' in base_conhecimento:
        for item in base_conhecimento['o_que_fazer']:
            topicos_guia.append(item['titulo'])

    #Interface de seleção
    st.sidebar.header("Tópicos do Guia")
    topico_selecionado = st.sidebar.radio("Selecione um tópico para ver os detalhes:", topicos_guia)

    st.header(topico_selecionado)

    #Lógica para exibir o conteúdo do tópico selecionado
    conteudo_encontrado = False
    if 'definicao_geral' in base_conhecimento and base_conhecimento['definicao_geral']['titulo'] == topico_selecionado:
        item = base_conhecimento['definicao_geral']
        st.markdown(f"> {item['conteudo']}")
        st.caption(f"Fonte: Guia de Bolso, pág. {item['pagina_guia']}")
        conteudo_encontrado = True

    if not conteudo_encontrado and 'tipos_de_assedio' in base_conhecimento:
        for item in base_conhecimento['tipos_de_assedio']:
            if item['tipo'] == topico_selecionado:
                st.markdown(f"> {item['descricao']}")
                st.caption(f"Fonte: Guia de Bolso, pág. {item['pagina_guia']}")
                conteudo_encontrado = True
                break
    
    if not conteudo_encontrado and 'condutas' in base_conhecimento:
        for item in base_conhecimento['condutas']:
            if item['conduta'] == topico_selecionado:
                st.markdown(f"> {item['descricao']}")
                st.caption(f"Fonte: Guia de Bolso, pág. {item['pagina_guia']}")
                conteudo_encontrado = True
                break
    
    if not conteudo_encontrado and 'o_que_fazer' in base_conhecimento:
        for item in base_conhecimento['o_que_fazer']:
            if item['titulo'] == topico_selecionado:
                for passo in item['passos']:
                    st.markdown(f"- {passo}")
                st.caption(f"Fonte: Guia de Bolso, pág. {item['pagina_guia']}")
                conteudo_encontrado = True
                break

else:
    st.error("Não foi possível carregar a base de conhecimento.")

