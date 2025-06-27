import re
from typing import Dict, Any, List, Tuple
from experta import *

#Normalização do texto para evitar erros
def normalizar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r'[áàâã]', 'a', texto)
    texto = re.sub(r'[éê]', 'e', texto)
    texto = re.sub(r'[íî]', 'i', texto)
    texto = re.sub(r'[óôõ]', 'o', texto)
    texto = re.sub(r'[úû]', 'u', texto)
    texto = re.sub(r'ç', 'c', texto)
    texto = re.sub(r'[^\w\s]', '', texto) # Remove pontuação
    return texto

def classificar_situacao(relato_usuario: str, base_conhecimento: Dict[str, Any]) -> Tuple[str, List[str]]:
    texto = normalizar_texto(relato_usuario)
    
    #Identificar o tipo de relação (Vertical, Horizontal), seguindo o guia de bolso
    tipo_assedio = "Não especificado"
    if any(palavra in texto for palavra in ["chefe", "superior", "coordenador", "professor", "gestor", "gerente"]):
        tipo_assedio = "Assédio Moral Vertical"
    elif any(palavra in texto for palavra in ["colega", "parceiro de equipe", "colega de trabalho"]):
        tipo_assedio = "Assédio Moral Horizontal"

    #Identificar as condutas específicas
    condutas_identificadas = []
    
    #Mapeamento de palavras-chave para cada conduta
    mapa_palavras_chave = {
        "Privar de instrumentos de trabalho": ["instrumento", "ferramenta", "acesso", "sistema", "computador"],
        "Sonegar ou dar informações incorretas": ["informacao", "errada", "sonegar", "esconder", "dados incorretos"],
        "Deixar a pessoa ociosa ou em situações humilhantes": ["ocioso", "sem tarefa", "humilhante", "constrangedor"],
        "Criticar de forma exagerada ou injusta": ["critica", "exagerada", "injusta", "em publico", "gritou"],
        "Sobrecarga de Tarefas": ["sobrecarregar", "muita tarefa", "excesso de trabalho", "prazo curto"],
        "Exigir tarefas urgentes desnecessariamente": ["urgente", "pra ontem", "pressao", "correria"],
        "Atribuir tarefas incompatíveis com a função": ["funcao diferente", "tarefa inferior", "tarefa superior"],
        "Dificultar ou impedir promoções": ["promocao", "impedir", "dificultar", "crescimento"],
        "Isolar a pessoa no ambiente de trabalho": ["isolar", "ignorar", "excluir", "nao falam comigo"],
        "Agredir verbalmente": ["gritar", "xingar", "ofender", "agressao verbal", "desprezo"],
        "Espalhar boatos e fofocas": ["fofoca", "boato", "espalhar mentiras", "desmoralizar"],
        "Invadir a privacidade": ["privacidade", "mexer nas coisas", "ler email", "escutar ligacao"],
        "Ignorar a presença da pessoa": ["ignorar", "fingir que nao ve", "nao cumprimenta"]
    }
    
    for conduta_info in base_conhecimento.get("condutas", []):
        nome_conduta = conduta_info["conduta"]
        palavras_chave = mapa_palavras_chave.get(nome_conduta, [])
        
        if any(palavra in texto for palavra in palavras_chave):
            condutas_identificadas.append(f"{nome_conduta} (Pág. {conduta_info['pagina_guia']} do Guia)")

    #Determinar a classificação final
    if not condutas_identificadas:
        classificacao_final = "Não foram encontrados indícios claros de assédio"
    else:
        #Se encontrou condutas mas não o tipo, classifica como genérico
        if tipo_assedio == "Não especificado":
            classificacao_final = "Indícios de Assédio Moral"
        else:
            classificacao_final = tipo_assedio

    return classificacao_final, condutas_identificadas

