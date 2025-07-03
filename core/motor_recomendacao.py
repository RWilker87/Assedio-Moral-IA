from typing import Dict, Any, List, Tuple

def gerar_recomendacao(classificacao: str, base_conhecimento: Dict[str, Any]) -> Tuple[List[str], List[str]]:
    recomendacoes = []
    canais = []

    o_que_fazer_data = base_conhecimento.get("o_que_fazer", [])

    if "Não foram encontrados" in classificacao:
        recomendacoes.append(
            "Se você acredita que está em uma situação de conflito, desconforto ou injustiça, "
            "considere buscar um diálogo com a Ouvidoria para obter orientação e apoio."
        )
        recomendacoes.append(
            "Consulte o 'Guia de Bolso sobre Assédio Moral' para entender melhor as condutas descritas e "
            "verifique se sua experiência se encaixa em alguma delas."
        )
        canais.append("Ouvidoria da UFAPE (atendimento sigiloso e institucional).")

    else:
        # Recomendação geral para vítimas
        for item in o_que_fazer_data:
            if item["titulo"] == "Como proceder se você for a vítima":
                recomendacoes.extend(item["passos"])
                break

        # Canais gerais
        for item in o_que_fazer_data:
            if item["titulo"] == "Canais de Denúncia":
                canais.extend(item["passos"])
                break

        # Reforço empático e direcionado conforme classificação
        if "Isolamento" in classificacao:
            recomendacoes.append("Busque se reconectar com pessoas de confiança. O isolamento pode ser um sinal de abuso coletivo ou institucional.")
        if "Vertical" in classificacao:
            recomendacoes.append("Abuso por superiores deve ser registrado. Anote datas e comportamentos e leve à Ouvidoria.")
        if "Horizontal" in classificacao:
            recomendacoes.append("Conflitos entre colegas também são assédio. Documente os fatos e procure ajuda formal.")
        if "Misto" in classificacao:
            recomendacoes.append("Quando o assédio vem de várias direções, a intervenção institucional é essencial.")
        if "Críticas Excessivas" in classificacao:
            recomendacoes.append("Criticar com frequência, especialmente em público, é uma forma de humilhação. Registre as ocorrências.")
        if "Organizacional" in classificacao:
            recomendacoes.append("Cobranças com metas inalcançáveis e gestão por estresse configuram assédio organizacional.")

    # Remover duplicatas e retornar
    return list(set(recomendacoes)), list(set(canais))
