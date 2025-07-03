class Explicador:
    def __init__(self, trace):
        self.trace = trace

    def gerar_explicacoes(self):
        return [
            f"**{item['regra']}**: {item['explicacao']}"
            for item in self.trace
            if isinstance(item, dict) and 'regra' in item and 'explicacao' in item
        ]
