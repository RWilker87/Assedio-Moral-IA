class Explicador:
    def __init__(self, trace):
        self.trace = trace

    def gerar_explicacoes(self):
        return [f"**{item['regra']}**: {item['explicacao']}" for item in self.trace]