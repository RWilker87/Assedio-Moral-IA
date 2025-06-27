from typing import Dict, Any, List, Tuple

def gerar_recomendacao(classificacao: str, base_conhecimento: Dict[str, Any]) -> Tuple[List[str], List[str]]:
    recomendacoes = []
    canais = []

    #Busca as recomendações padrão do guia
    o_que_fazer_data = base_conhecimento.get("o_que_fazer", [])

    if "Não foram encontrados" in classificacao:
        #Recomendações para casos não conclusivos
        recomendacoes.append(
            "Se você acredita que está em uma situação de conflito, desconforto ou injustiça, "
            "considere buscar um diálogo com a Ouvidoria para obter orientação."
        )
        recomendacoes.append(
            "Consulte o 'Guia de Bolso sobre Assédio Moral' para entender melhor as definições e "
            "verificar se sua situação se enquadra em alguma das condutas descritas."
        )
        canais.append("Ouvidoria da UFAPE (para orientação e mediação de conflitos).")
    else:
        #Recomendações padrão para vítimas de assédio
        for item in o_que_fazer_data:
            if item["titulo"] == "Como proceder se você for a vítima":
                recomendacoes.extend(item["passos"])
                break
        
        #Canais de denúncia padrão
        for item in o_que_fazer_data:
            if item["titulo"] == "Canais de Denúncia":
                canais.extend(item["passos"])
                break
                
    return recomendacoes, canais
