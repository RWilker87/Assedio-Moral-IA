from experta import *
from core.explicador import Explicador

class FatoAssedio(Fact): pass

class SistemaAssedio(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.trace = []
        self.resultados = []
        self.explicador = Explicador(self.trace)

    @Rule(FatoAssedio(isolamento=True, comunicacao=False))
    def isolamento(self):
        self.trace.append({"regra": "Isolamento", "explicacao": "Houve isolamento e recusa de comunicação."})
        self.resultados.append("Assédio Moral por Isolamento Social.")

    @Rule(FatoAssedio(humilhacao=True, em_publico=True))
    def humilhacao(self):
        self.trace.append({"regra": "Humilhação Pública", "explicacao": "A vítima foi humilhada em público."})
        self.resultados.append("Assédio Moral por Humilhação Pública.")

    @Rule(FatoAssedio(tipo='criticas_exageradas', repetitivo=True))
    def criticas(self):
        self.trace.append({"regra": "Críticas Exageradas", "explicacao": "Houve críticas injustas e frequentes."})
        self.resultados.append("Assédio Moral por Críticas Excessivas.")

    @Rule(FatoAssedio(tipo_conversa='conversa_dificil', humilhacao=False))
    def conversa_dificil(self):
        self.trace.append({"regra": "Conversa Difícil", "explicacao": "Situação difícil sem humilhação."})
        self.resultados.append("Situação não configura assédio moral.")

    @Rule(FatoAssedio(relacao='vertical', abuso_poder=True))
    def vertical(self):
        self.trace.append({"regra": "Assédio Vertical", "explicacao": "Abuso de poder por superior."})
        self.resultados.append("Assédio Moral Vertical.")

    @Rule(FatoAssedio(relacao='horizontal', humilhacao=True, repetitivo=True))
    def horizontal(self):
        self.trace.append({"regra": "Assédio Horizontal", "explicacao": "Abusos entre colegas de mesma hierarquia."})
        self.resultados.append("Assédio Moral Horizontal.")

    @Rule(FatoAssedio(relacao='misto', isolamento=True, tarefas_excessivas=True))
    def misto(self):
        self.trace.append({"regra": "Assédio Misto", "explicacao": "Condutas abusivas entre pares e superiores."})
        self.resultados.append("Assédio Moral Misto.")

    @Rule(FatoAssedio(tipo='organizacional', metas_irreais=True, estresse_excessivo=True))
    def organizacional(self):
        self.trace.append({"regra": "Assédio Organizacional", "explicacao": "Gestão por estresse e metas irreais."})
        self.resultados.append("Assédio Organizacional.")

    @Rule(FatoAssedio(denuncia=True))
    def recomendar_denuncia(self):
        self.trace.append({"regra": "Recomendação", "explicacao": "Recomenda-se denúncia formal."})
        self.resultados.append("Recomenda-se denúncia via FalaBR.")

    def get_resultados(self):
        return self.resultados

    def get_trace(self):
        return self.trace