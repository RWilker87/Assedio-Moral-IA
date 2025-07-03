# ⚖️ Sistema Especialista para Análise de Casos de Assédio Moral — UFAPE

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red.svg)

Projeto acadêmico desenvolvido para a disciplina de **Inteligência Artificial** do curso de **Ciência da Computação** da Universidade Federal do Agreste de Pernambuco (UFAPE).

---

## 🧠 Sobre o Projeto

Este sistema especialista visa **identificar e analisar possíveis casos de assédio moral** no contexto acadêmico ou institucional, com base em documentos oficiais da UFAPE. Ele interpreta automaticamente relatos do usuário, **classifica a situação**, **explica o porquê** e fornece **orientações claras e seguras** sobre o que fazer, como fazer e para onde ir.

Tudo isso é feito por meio de uma interface intuitiva, desenvolvida em **Streamlit**, e apoiada por um **motor de inferência baseado em regras**.

---

## 🎯 Objetivos

- ✅ Interpretar relatos textuais sobre possíveis situações de assédio moral  
- ✅ Aplicar um sistema de regras com motor de inferência para classificar o caso  
- ✅ Fornecer **recomendações personalizadas** e indicar os **canais adequados** de denúncia  
- ✅ Servir como ferramenta pedagógica e de apoio à comunidade acadêmica da UFAPE

---

## ✨ Funcionalidades

✔️ **Análise automática de relatos** com base em regras explícitas  
✔️ **Classificação do tipo de assédio moral**: vertical, horizontal, organizacional, etc.  
✔️ **Fundamentação explicável das decisões**  
✔️ **Sugestões de condutas e medidas corretivas**  
✔️ **Consulta interativa ao "Guia de Bolso sobre Assédio Moral"**  
✔️ **Interface Web intuitiva (com Streamlit)**

---

## 📚 Fontes da Base de Conhecimento

🟢 **Guia de Bolso sobre Assédio Moral — Ouvidoria UFAPE**  
🔵 **Regimento Geral da UFAPE (complementar)**

Esses documentos embasam todas as regras, condutas, orientações e recomendações do sistema.

---

## 🛠️ Tecnologias Utilizadas

| Camada         | Ferramenta        |
|----------------|-------------------|
| Linguagem      | Python 3.9+        |
| Framework Web  | Streamlit         |
| Motor de Inferência | [Experta](https://experta.readthedocs.io/) (baseada em CLIPS) |
| Extração de Fatos | Expressões Regulares + Heurística |

---

## 📂 Estrutura do Projeto

```
📁 projeto/
├── core/                  # Núcleo da lógica de inferência
│   ├── base_conhecimento.py
│   ├── classificador.py
│   ├── regras.py
│   ├── motor_recomendacao.py
│   ├── explicador.py
│   ├── gerador_relatorio.py
│   └── extrator_fatos.py
│
├── data/
│   └── Guia_de_Bolso_Assedio_Moral.json
│
├── pages/
│   ├── 1_Analisar_Situacao.py
│   └── 2_Consultar_o_Guia.py
│
├── app.py                # Arquivo principal (Streamlit)
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo
```

---

## 🚀 Como Executar o Projeto Localmente

### 🔧 Pré-requisitos

- Python 3.9 ou superior  
- Git  
- (Opcional) Ambiente virtual com venv ou conda

### 📦 Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/RWilker87/Assedio-Moral-IA
cd Assedio-Moral-IA

# 2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt
```

### ▶️ Execução

```bash
streamlit run app.py
```

> Acesse o navegador em http://localhost:8501

---

## 👤 Autores

| Nome                          | GitHub                             |
|-------------------------------|-------------------------------------|
| Victor Winicius Barros Santos | [@VictorW-dev](https://github.com/VictorW-dev) |
| Rian Wilker Santos Melo       | [@RWilker87](https://github.com/RWilker87)     |

---

## 📣 Agradecimentos

Este projeto foi desenvolvido como uma proposta pedagógica para o uso prático de sistemas especialistas em IA, com apoio da disciplina e dos documentos da Ouvidoria da UFAPE.

---

## 🛡️ Aviso

> O sistema é apenas uma ferramenta auxiliar. **Não substitui orientação jurídica ou institucional formal.**
