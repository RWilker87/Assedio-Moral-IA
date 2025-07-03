from experta import *
from core.explicador import Explicador

class FatoAssedio(Fact):
    pass

class SistemaAssedio(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.resultados = []
        self.trace = []
        self.explicador = Explicador(self.trace)

    @Rule(FatoAssedio(humilhacao=True, em_publico=True))
    def humilhacao_publica(self):
        self.resultados.append("Assédio Moral por Humilhação Pública.")
        self.resultados.append("Constrangimentos ou gritos na frente de outras pessoas.")
        self.trace.append({
            "regra": "Humilhação Pública",
            "explicacao": "Foi identificado constrangimento em local público."
        })

    @Rule(FatoAssedio(isolamento=True, comunicacao=False))
    def isolamento_social(self):
        self.resultados.append("Assédio Moral por Isolamento Social.")
        self.resultados.append("Afastamento forçado ou quebra de comunicação com colegas.")
        self.trace.append({
            "regra": "Isolamento Social",
            "explicacao": "O relato descreve exclusão e ausência de comunicação com o grupo."
        })

    @Rule(FatoAssedio(tipo="criticas_exageradas", repetitivo=True))
    def criticas_excessivas(self):
        self.resultados.append("Assédio Moral por Críticas Excessivas.")
        self.resultados.append("Críticas constantes e injustas.")
        self.trace.append({
            "regra": "Críticas Excessivas",
            "explicacao": "Houve críticas injustas e frequentes no ambiente de trabalho."
        })

    @Rule(FatoAssedio(tipo_conversa="conversa_dificil", repetitivo=False))
    def conversa_dificil_unica(self):
        self.resultados.append("Situação não configura assédio moral.")
        self.trace.append({
            "regra": "Conversa Difícil",
            "explicacao": "Foi relatada apenas uma conversa dura ou de feedback isolado, o que não caracteriza assédio."
        })

    @Rule(FatoAssedio(relacao="vertical"))
    def relacao_vertical(self):
        self.resultados.append("Assédio Moral Vertical.")
        self.resultados.append("Agressões vindas de superiores hierárquicos.")
        self.trace.append({
            "regra": "Vertical",
            "explicacao": "O agressor tem posição hierárquica superior à vítima."
        })

    @Rule(FatoAssedio(relacao="horizontal"))
    def relacao_horizontal(self):
        self.resultados.append("Assédio Moral Horizontal.")
        self.resultados.append("Ataques vindos de colegas de mesmo nível.")
        self.trace.append({
            "regra": "Horizontal",
            "explicacao": "O agressor é colega do mesmo nível hierárquico da vítima."
        })

    @Rule(FatoAssedio(relacao="misto"))
    def relacao_mista(self):
        self.resultados.append("Assédio Moral Misto.")
        self.resultados.append("Condutas abusivas vindas de colegas e superiores ao mesmo tempo.")
        self.trace.append({
            "regra": "Misto",
            "explicacao": "A vítima sofre assédio de diferentes níveis hierárquicos (superiores e colegas)."
        })

    @Rule(FatoAssedio(metas_irreais=True, estresse_excessivo=True))
    def organizacional(self):
        self.resultados.append("Assédio Organizacional.")
        self.resultados.append("Cobrança excessiva de metas, sobrecarga e pressão institucional.")
        self.trace.append({
            "regra": "Organizacional",
            "explicacao": "Foram relatadas metas inalcançáveis e ambiente de trabalho opressor."
        })

    @Rule(FatoAssedio(denuncia=True, isolamento=True))
    def retaliação(self):
        self.resultados.append("Assédio Moral por Retaliação.")
        self.resultados.append("Afastamento ou perseguição após tentativa de denúncia.")
        self.trace.append({
            "regra": "Retaliação",
            "explicacao": "A vítima relatou isolamento após uma tentativa de denúncia ou exposição do problema."
        })

    @Rule(FatoAssedio(abuso_poder=True, repetitivo=True))
    def ameaca_intimidacao(self):
        self.resultados.append("Assédio Moral por Ameaça ou Intimidação.")
        self.resultados.append("Ameaças verbais, cobranças autoritárias ou criação de ambiente de medo.")
        self.trace.append({
            "regra": "Ameaça ou Intimidação",
            "explicacao": "Há indícios de abuso de poder com comportamento intimidador recorrente."
        })

    @Rule(FatoAssedio(humilhacao=True, tipo="criticas_exageradas"))
    def desqualificacao(self):
        self.resultados.append("Assédio Moral por Desqualificação Profissional.")
        self.resultados.append("Críticas com objetivo de rebaixar ou invalidar a competência profissional.")
        self.trace.append({
            "regra": "Desqualificação Profissional",
            "explicacao": "Críticas humilhantes foram usadas para diminuir a autoestima profissional da vítima."
        })

    @Rule(FatoAssedio(tarefas_excessivas=True, relacao="horizontal"))
    def atribuicao_injusta(self):
        self.resultados.append("Assédio Moral por Atribuição Injusta de Tarefas.")
        self.resultados.append("Colegas repassam tarefas excessivas de forma injustificada.")
        self.trace.append({
            "regra": "Atribuição Injusta",
            "explicacao": "A vítima relatou sobrecarga imposta por colegas de trabalho."
        })

    @Rule(FatoAssedio(isolamento=True, comunicacao=False, repetitivo=True))
    def exclusao_decisoria(self):
        self.resultados.append("Assédio Moral por Exclusão Decisória.")
        self.resultados.append("A vítima foi excluída sistematicamente de decisões, reuniões ou grupos.")
        self.trace.append({
            "regra": "Exclusão Decisória",
            "explicacao": "A vítima relatou ser impedida de participar de decisões ou comunicação importantes."
        })

    def get_resultados(self):
        return self.resultados
