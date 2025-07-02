# Sistema Especialista para Análise de Casos de Assédio Moral - UFAPE

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red.svg)


Projeto acadêmico desenvolvido para a disciplina de Inteligência Artificial do curso de Ciência da Computação da Universidade Federal do Agreste de Pernambuco (UFAPE).

## 📖 Sobre o Projeto

Este projeto consiste no desenvolvimento de um sistema especialista com interface web que interpreta situações de potencial assédio moral no ambiente acadêmico. O sistema utiliza como base de conhecimento os regulamentos e guias oficiais da UFAPE para oferecer uma análise fundamentada, classificar a situação descrita e orientar o usuário sobre os procedimentos corretos a serem seguidos.

### 🎯 Objetivo Central

O objetivo central é que o sistema interprete situações instanciadas pelo usuário (por meio de formulários, menus ou perguntas diretas) e ofereça uma resposta precisa, fundamentada nas regras do regulamento escolhido. O sistema deverá possuir uma interface Web construída com Streamlit, capaz de dialogar com o usuário de forma clara, indicar as regras aplicadas e justificar as conclusões obtidas.

## ✨ Funcionalidades Principais

O sistema especialista é capaz de:

1.  **Identificar e Classificar:** Analisar e classificar automaticamente situações relatadas pelos usuários conforme as definições e critérios estabelecidos no "Guia de Bolso sobre Assédio Moral" da Ouvidoria UFAPE.
2.  **Fornecer Orientações Personalizadas:** Oferecer orientações sobre procedimentos de denúncia, acolhimento e proteção à vítima com base na classificação do relato.
3.  **Recomendar Canais Adequados:** Indicar os canais corretos para cada tipo de situação, como a Ouvidoria, Comissão de Ética ou outras autoridades competentes.
4.  **Gerar Relatórios Explicativos:** Criar relatórios que fundamentam cada classificação e recomendação nos artigos, definições e procedimentos específicos dos documentos oficiais.

## 📚 Base de Conhecimento

A "inteligência" do sistema é totalmente baseada em dois documentos oficiais da UFAPE:

1.  **Guia de Bolso sobre Assédio Moral (Fonte Primária):** Define o que é assédio moral, lista exemplos de condutas, descreve os tipos de assédio (vertical, horizontal, etc.) e orienta as vítimas sobre como proceder.
2.  **Regimento Geral da UFAPE (Fonte de Apoio):** Fornece o contexto institucional, descrevendo as competências de órgãos como a **Ouvidoria** e detalhando o **Regime Disciplinar** aplicável a discentes e servidores, que fundamenta a aplicação de possíveis sanções.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Framework Web:** Streamlit

## 📂 Estrutura do Projeto

O projeto está organizado na seguinte estrutura de diretórios para manter a clareza e a modularidade:

```
/projeto_especialista_ufape/
|
|-- 📂 core/
|   |-- 📜 __init__.py
|   |-- 📜 base_conhecimento.py    # Módulo para carregar e consultar as regras
|   |-- 📜 classificador.py        # Lógica de IA para classificar o relato
|   |-- 📜 motor_recomendacao.py   # Lógica para gerar orientações
|   |-- 📜 gerador_relatorio.py    # Módulo para formatar a resposta final
|
|-- 📂 data/
|   |-- 📄 guia_assedio_moral.pdf  # Documento original
|   |-- 📄 base_conhecimento.json  # Conhecimento estruturado para o sistema
|
|-- 📂 pages/
|   |-- 📜 1_Analisar_Situação.py  # Página principal de análise
|   |-- 📜 2_Consultar_o_Guia.py   # Página de consulta direta ao guia
|
|-- 📜 app.py                      # Arquivo principal da aplicação Streamlit
|-- 📜 README.md                   # Este arquivo
```

## 🚀 Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar e executar o projeto em sua máquina.

### Pré-requisitos

* [Python](https://www.python.org/downloads/) (versão 3.9 ou superior)
* [Git](https://git-scm.com/)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/RWilker87/Assedio-Moral-IA](https://github.com/RWilker87/Assedio-Moral-IA)
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd Assedio-Moral-IA
    ```

### Execução

Com o ambiente virtual ativado e as dependências instaladas, execute o seguinte comando no terminal:

```bash
streamlit run app.py
```

A aplicação será iniciada e um endereço local (geralmente `http://localhost:8501`) será aberto automaticamente no seu navegador.
