import re
from typing import Dict, List
from experta import *

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

class TextoParaAnalisar(Fact):
    pass


class FatoExtraido(Fact):
    pass


class RelacaoDefinida(Fact):
    pass


class ExtratorDeFatosEngine(KnowledgeEngine):
    PALAVRAS_ISOLAMENTO = ["isolar", "excluir", "ignorar", "deixaram de lado", "me evitam", "me tiraram do grupo",
                           "ninguem conversa", "ficar sozinho", "me afastaram", "me bloquearam", "me deixaram de fora",
                           "me cortaram", "romperam o contato", "me silenciaram", "nao me incluem", "nao me chamam"]
    PALAVRAS_SEM_COMUNICACAO = ["ignorar", "sem resposta", "sem retorno", "nao me respondem", "ninguem fala",
                                "evitam conversa", "me cortaram das reunioes", "me excluem dos emails",
                                "bloquearam comunicacao"]
    PALAVRAS_HUMILHACAO = ["humilhar", "constranger", "vergonha", "me diminuiram", "me expuseram", "foi vexatorio",
                           "gritaram comigo", "piadas sobre mim", "fui ridicularizado", "me zombaram",
                           "fui menosprezado", "fui ofendido", "palavras ofensivas", "xingamento", "apelidos maldosos",
                           "sarcasmo contra mim"]
    PALAVRAS_EM_PUBLICO = ["na frente de todos", "em publico", "diante dos outros", "na reuniao", "na sala cheia",
                           "na frente da turma", "com plateia", "perto de todo mundo"]
    PALAVRAS_CRITICAS = ["critica", "gritou", "exagerada", "injusta", "acusacoes infundadas", "reclamacoes constantes",
                         "cobranca injusta", "me apontam defeitos", "nunca estou bom", "me cobram demais",
                         "me rebaixam profissionalmente", "so sabem criticar"]
    PALAVRAS_REPETITIVO = ["sempre", "todo dia", "frequente", "repetido", "acontece direto", "de novo", "mais uma vez",
                           "constantemente", "toda semana", "recorrente", "ja virou rotina", "e toda hora"]
    PALAVRAS_CONVERSA_DIFICIL = ["feedback", "conversa dificil", "avaliacao", "cobranca", "reuniao sobre desempenho",
                                 "me chamou pra conversar", "puxao de orelha", "discussao profissional",
                                 "alerta formal"]
    PALAVRAS_VERTICAL = ["chefe", "superior", "coordenador", "professor", "gestor", "gerente", "meu lider",
                         "meu orientador", "orientador", "diretor", "chefiado"]
    PALAVRAS_HORIZONTAL = ["colega", "amigo de trabalho", "igual a mim", "parceiro de equipe", "outro servidor",
                           "companheiro de sala", "outro aluno", "membro da equipe"]
    PALAVRAS_MISTO = ["todos", "superior e colegas", "grupo inteiro", "a equipe toda", "professor e colegas",
                      "lider e membros", "coordenador e subordinados"]
    PALAVRAS_ABUSO_PODER = ["abuso", "autoridade", "mandao", "me forcam", "poder", "se aproveita", "ameaça",
                            "imposicao", "chantagem", "intimidacao", "ameaçam cortar salario", "pressao psicologica",
                            "se impõe", "nao posso dizer nao", "me obrigam", "impoem medo"]
    PALAVRAS_TAREFAS_EXCESSIVAS = ["sobrecarregado", "muita tarefa", "excesso de trabalho", "sem pausa",
                                   "trabalho demais", "tudo em cima de mim", "me lotam de coisa", "me afogo de tarefa",
                                   "duas funcoes", "responsabilidades demais", "demandas injustas", "dobro de trabalho"]
    PALAVRAS_METAS_IRREAIS = ["meta impossivel", "prazo absurdo", "inalcancavel", "muito pouco tempo", "sem condicoes",
                              "objetivo inatingivel", "pedem o impossivel", "tarefa inviavel", "cobranças sem lógica",
                              "expectativas irreais"]
    PALAVRAS_ESTRESSE = ["estresse", "pressao", "ansiedade", "fico nervoso", "peso psicologico", "mal estar mental",
                         "sofrimento emocional", "trabalho adoecedor", "ambiente toxico", "exaustao", "esgotado",
                         "problema emocional", "sem saude mental", "exaustao constante", "nao aguento mais"]
    PALAVRAS_DENUNCIA = ["quero denunciar", "como denunciar", "denuncia", "relatar", "reportar", "procurar ouvidoria",
                         "fiz queixa", "procurei ajuda", "denunciei", "vou formalizar"]

    def _contem(self, texto: str, palavras: List[str]) -> bool:
        return any(p in texto for p in palavras)

    @Rule(TextoParaAnalisar(texto=MATCH.texto), test=lambda texto, self: self._contem(texto, self.PALAVRAS_ISOLAMENTO))
    def _fato_isolamento(self): self.declare(FatoExtraido(chave='isolamento', valor=True))

    @Rule(TextoParaAnalisar(texto=MATCH.texto),
          test=lambda texto, self: self._contem(texto, self.PALAVRAS_SEM_COMUNICACAO))
    def _fato_sem_comunicacao(self): self.declare(FatoExtraido(chave='comunicacao', valor=False))

    @Rule(TextoParaAnalisar(texto=MATCH.texto), test=lambda texto, self: self._contem(texto, self.PALAVRAS_HUMILHACAO))
    def _fato_humilhacao(self): self.declare(FatoExtraido(chave='humilhacao', valor=True))

    @Rule(TextoParaAnalisar(texto=MATCH.texto), test=lambda texto, self: self._contem(texto, self.PALAVRAS_EM_PUBLICO))
    def _fato_em_publico(self): self.declare(FatoExtraido(chave='em_publico', valor=True))

    @Rule(TextoParaAnalisar(texto=MATCH.texto), test=lambda texto, self: self._contem(texto, self.PALAVRAS_CRITICAS))
    def _fato_tipo_critica(self): self.declare(FatoExtraido(chave='tipo', valor='criticas_exageradas'))

    @Rule(TextoParaAnalisar(texto=MATCH.texto), test=lambda texto, self: self._contem(texto, self.PALAVRAS_REPETITIVO))
    def _fato_repetitivo(self): self.declare(FatoExtraido(chave='repetitivo', valor=True))

    @Rule(TextoParaAnalisar(texto=MATCH.texto),
          test=lambda texto, self: self._contem(texto, self.PALAVRAS_CONVERSA_DIFICIL))
    def _fato_tipo_conversa(self): self.declare(FatoExtraido(chave='tipo_conversa', valor='conversa_dificil'))

    @Rule(TextoParaAnalisar(texto=MATCH.texto), test=lambda texto, self: self._contem(texto, self.PALAVRAS_ABUSO_PODER))
    def _fato_abuso_poder(self): self.declare(FatoExtraido(chave='abuso_poder', valor=True))

    @Rule(TextoParaAnalisar(texto=MATCH.texto),
          test=lambda texto, self: self._contem(texto, self.PALAVRAS_TAREFAS_EXCESSIVAS))
    def _fato_tarefas_excessivas(self): self.declare(FatoExtraido(chave='tarefas_excessivas', valor=True))

    @Rule(TextoParaAnalisar(texto=MATCH.texto),
          test=lambda texto, self: self._contem(texto, self.PALAVRAS_METAS_IRREAIS))
    def _fato_metas_irreais(self): self.declare(FatoExtraido(chave='metas_irreais', valor=True))

    @Rule(TextoParaAnalisar(texto=MATCH.texto), test=lambda texto, self: self._contem(texto, self.PALAVRAS_ESTRESSE))
    def _fato_estresse_excessivo(self): self.declare(FatoExtraido(chave='estresse_excessivo', valor=True))

    @Rule(TextoParaAnalisar(texto=MATCH.texto), test=lambda texto, self: self._contem(texto, self.PALAVRAS_DENUNCIA))
    def _fato_denuncia(self): self.declare(FatoExtraido(chave='denuncia', valor=True))

    # --- Regras com Lógica de Prioridade para 'relação' ---

    @Rule(NOT(RelacaoDefinida()), TextoParaAnalisar(texto=MATCH.texto), salience=10,
          test=lambda texto, self: self._contem(texto, self.PALAVRAS_VERTICAL))
    def _fato_relacao_vertical(self):
        self.declare(FatoExtraido(chave='relacao', valor='vertical'))
        self.declare(RelacaoDefinida())

    @Rule(NOT(RelacaoDefinida()), TextoParaAnalisar(texto=MATCH.texto), salience=5,
          test=lambda texto, self: self._contem(texto, self.PALAVRAS_HORIZONTAL))
    def _fato_relacao_horizontal(self):
        self.declare(FatoExtraido(chave='relacao', valor='horizontal'))
        self.declare(RelacaoDefinida())

    @Rule(NOT(RelacaoDefinida()), TextoParaAnalisar(texto=MATCH.texto), salience=1,
          test=lambda texto, self: self._contem(texto, self.PALAVRAS_MISTO))
    def _fato_relacao_mista(self):
        self.declare(FatoExtraido(chave='relacao', valor='misto'))
        self.declare(RelacaoDefinida())

def extrair_fatos(texto: str) -> Dict:
    engine = ExtratorDeFatosEngine()
    engine.reset()

    texto_normalizado = normalizar_texto(texto)
    engine.declare(TextoParaAnalisar(texto=texto_normalizado))
    engine.run()

    resultados = {}
    for fato in engine.facts.values():
        if isinstance(fato, FatoExtraido):
            resultados[fato['chave']] = fato['valor']

    chaves_booleanas = ["isolamento", "humilhacao", "em_publico", "repetitivo", "abuso_poder", "tarefas_excessivas",
                        "metas_irreais", "estresse_excessivo", "denuncia"]
    for chave in chaves_booleanas:
        resultados.setdefault(chave, False)

    resultados.setdefault('comunicacao', True) 
    resultados.setdefault('tipo', "")
    resultados.setdefault('tipo_conversa', "")
    resultados.setdefault('relacao', "")

    return resultados