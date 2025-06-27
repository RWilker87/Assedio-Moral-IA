from typing import Dict, Any, List

def formatar_relatorio(classificacao: str, condutas_identificadas: List[str], recomendacoes: List[str], canais: List[str], base_conhecimento: Dict[str, Any]) -> Dict[str, Any]:
    # Monta a fundamentação com base na definição geral de assédio
    fundamentacao = base_conhecimento.get("definicao_geral", {}).get("conteudo", 
        "A análise baseia-se nas definições do 'Guia de Bolso sobre Assédio Moral' da Ouvidoria UFAPE.")
    
    # Caso não encontre indícios, a fundamentação é outra
    if "Não foram encontrados" in classificacao:
        fundamentacao = "O relato não contém palavras-chave diretamente associadas às condutas de assédio listadas no Guia da Ouvidoria."
        condutas_identificadas = ["Nenhuma conduta específica do guia foi identificada claramente."]


    relatorio = {
        "classificacao": classificacao,
        "condutas_identificadas": condutas_identificadas,
        "fundamentacao": fundamentacao,
        "recomendacoes": recomendacoes,
        "canais": canais
    }
    
    return relatorio
