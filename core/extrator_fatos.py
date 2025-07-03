import re
from typing import Dict

def normalizar_texto(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r'[áàâã]', 'a', texto)
    texto = re.sub(r'[éê]', 'e', texto)
    texto = re.sub(r'[íî]', 'i', texto)
    texto = re.sub(r'[óôõ]', 'o', texto)
    texto = re.sub(r'[úû]', 'u', texto)
    texto = re.sub(r'ç', 'c', texto)
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto

def extrair_fatos(texto: str) -> Dict:
    texto = normalizar_texto(texto)

    fatos = {
        "isolamento": any(p in texto for p in [
            "isolar", "excluir", "ignorar", "deixaram de lado", "me evitam", "me tiraram do grupo",
            "ninguem conversa", "ficar sozinho", "me afastaram", "me bloquearam", "me deixaram de fora",
            "me cortaram", "romperam o contato", "me silenciaram", "nao me incluem", "nao me chamam"
        ]),
        "comunicacao": not any(p in texto for p in [
            "ignorar", "sem resposta", "sem retorno", "nao me respondem", "ninguem fala",
            "evitam conversa", "me cortaram das reunioes", "me excluem dos emails", "bloquearam comunicacao"
        ]),
        "humilhacao": any(p in texto for p in [
            "humilhar", "constranger", "vergonha", "me diminuiram", "me expuseram", "foi vexatorio", 
            "gritaram comigo", "piadas sobre mim", "fui ridicularizado", "me zombaram", "fui menosprezado",
            "fui ofendido", "palavras ofensivas", "xingamento", "apelidos maldosos", "sarcasmo contra mim"
        ]),
        "em_publico": any(p in texto for p in [
            "na frente de todos", "em publico", "diante dos outros", "na reuniao", 
            "na sala cheia", "na frente da turma", "com plateia", "perto de todo mundo"
        ]),
        "tipo": "criticas_exageradas" if any(p in texto for p in [
            "critica", "gritou", "exagerada", "injusta", "acusacoes infundadas", "reclamacoes constantes",
            "cobranca injusta", "me apontam defeitos", "nunca estou bom", "me cobram demais", 
            "me rebaixam profissionalmente", "so sabem criticar"
        ]) else "",
        "repetitivo": any(p in texto for p in [
            "sempre", "todo dia", "frequente", "repetido", "acontece direto", "de novo", "mais uma vez", 
            "constantemente", "toda semana", "recorrente", "ja virou rotina", "e toda hora"
        ]),
        "tipo_conversa": "conversa_dificil" if any(p in texto for p in [
            "feedback", "conversa dificil", "avaliacao", "cobranca", "reuniao sobre desempenho",
            "me chamou pra conversar", "puxao de orelha", "discussao profissional", "alerta formal"
        ]) else "",
        "relacao": (
            "vertical" if any(p in texto for p in [
                "chefe", "superior", "coordenador", "professor", "gestor", "gerente", "meu lider", 
                "meu orientador", "orientador", "diretor", "chefiado"
            ]) else
            "horizontal" if any(p in texto for p in [
                "colega", "amigo de trabalho", "igual a mim", "parceiro de equipe", "outro servidor",
                "companheiro de sala", "outro aluno", "membro da equipe"
            ]) else
            "misto" if any(p in texto for p in [
                "todos", "superior e colegas", "grupo inteiro", "a equipe toda", "professor e colegas",
                "lider e membros", "coordenador e subordinados"
            ]) else ""
        ),
        "abuso_poder": any(p in texto for p in [
            "abuso", "autoridade", "mandao", "me forcam", "poder", "se aproveita", "ameaça", 
            "imposicao", "chantagem", "intimidacao", "ameaçam cortar salario", "pressao psicologica",
            "se impõe", "nao posso dizer nao", "me obrigam", "impoem medo"
        ]),
        "tarefas_excessivas": any(p in texto for p in [
            "sobrecarregado", "muita tarefa", "excesso de trabalho", "sem pausa", "trabalho demais",
            "tudo em cima de mim", "me lotam de coisa", "me afogo de tarefa", "duas funcoes", 
            "responsabilidades demais", "demandas injustas", "dobro de trabalho"
        ]),
        "metas_irreais": any(p in texto for p in [
            "meta impossivel", "prazo absurdo", "inalcancavel", "muito pouco tempo", "sem condicoes",
            "objetivo inatingivel", "pedem o impossivel", "tarefa inviavel", "cobranças sem lógica",
            "expectativas irreais"
        ]),
        "estresse_excessivo": any(p in texto for p in [
            "estresse", "pressao", "ansiedade", "fico nervoso", "peso psicologico", "mal estar mental",
            "sofrimento emocional", "trabalho adoecedor", "ambiente toxico", "exaustao", "esgotado",
            "problema emocional", "sem saude mental", "exaustao constante", "nao aguento mais"
        ]),
        "denuncia": any(p in texto for p in [
            "quero denunciar", "como denunciar", "denuncia", "relatar", "reportar", "procurar ouvidoria",
            "fiz queixa", "procurei ajuda", "denunciei", "vou formalizar"
        ])
    }

    return fatos
