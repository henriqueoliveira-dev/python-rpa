# 🐍 Python RPA — Automação de Processos com Python

Repositório dedicado ao desenvolvimento de soluções de **Automação Robótica de Processos (RPA)** utilizando Python, com foco na automação de tarefas repetitivas, extração de dados, consumo de APIs, manipulação de planilhas e integração com serviços disponíveis na internet.

O objetivo deste repositório é desenvolver e documentar projetos práticos, aplicando conceitos de programação, automação e manipulação de dados para solucionar problemas do cotidiano e otimizar processos.

---

## 📌 Objetivos do Repositório

- Desenvolver soluções de automação utilizando Python.
- Automatizar consultas e extração de informações na internet.
- Consumir APIs por meio de requisições HTTP.
- Manipular e organizar dados utilizando Pandas.
- Automatizar a criação e atualização de planilhas Excel.
- Desenvolver scripts para reduzir atividades manuais e repetitivas.
- Aplicar boas práticas de organização, documentação e versionamento de código.

---

## 🛠️ Tecnologias e Bibliotecas

As principais tecnologias e bibliotecas utilizadas nos projetos são:

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal de desenvolvimento. |
| Selenium | Automação e interação com páginas web. |
| HTTP Client | Realização de requisições HTTP. |
| JSON | Leitura e manipulação de dados estruturados. |
| Pandas | Manipulação, organização e tratamento de dados. |
| OpenPyXL | Leitura e gravação de planilhas Excel. |
| XlsxWriter | Criação e formatação de arquivos Excel. |
| Git | Controle de versão dos projetos. |
| GitHub | Armazenamento e documentação dos códigos. |

---

# 📂 Projetos Desenvolvidos

## 1. Automação de Cotação do Dólar

### 📌 Descrição

Projeto desenvolvido para automatizar a consulta da cotação do dólar utilizando Python e Selenium.

A proposta é utilizar a automação de navegador para acessar informações disponíveis na internet, reduzindo a necessidade de consultas manuais.

### 📄 Arquivos do Projeto

**`importcao_dolar.py`**

Responsável pela automação da consulta da cotação do dólar.

Principais conceitos aplicados:

- Automação de navegador com Selenium.
- Navegação em páginas web.
- Localização e extração de informações.
- Execução de tarefas automatizadas com Python.

**`criandoUmAquivoExcel.py`**

Responsável pela criação de uma planilha Excel utilizando a biblioteca XlsxWriter.

Principais conceitos aplicados:

- Criação de arquivos Excel.
- Manipulação de planilhas.
- Organização de informações em formato tabular.
- Utilização da biblioteca XlsxWriter.

### 🎯 Objetivo do Projeto

Praticar automação web e manipulação de arquivos Excel, aplicando Python para facilitar a coleta e organização de informações.

---

## 2. Consulta e Extração de CEP com API ViaCEP

### 📌 Descrição

Projeto desenvolvido para realizar consultas de endereços por meio da API pública ViaCEP.

A solução utiliza requisições HTTP para obter informações de endereços a partir de um CEP, permitindo retornar, organizar e armazenar os dados em planilhas Excel.

O projeto apresenta três etapas de desenvolvimento, demonstrando a evolução de uma consulta individual até a automação de consultas em lote.

### 📄 Arquivos do Projeto

### 2.1. `extracao01.py` — Consulta Individual de CEP

**Descrição:**

Script responsável por consultar um CEP informado pelo usuário e retornar os dados disponibilizados pela API ViaCEP.

**Funcionamento:**

1. Recebe o CEP por meio da função `input()`.
2. Estabelece uma conexão HTTP utilizando `http.client`.
3. Realiza uma requisição GET para a API ViaCEP.
4. Recebe a resposta da API.
5. Converte o conteúdo JSON em um objeto Python.
6. Verifica se o CEP foi encontrado.
7. Exibe as informações do endereço no terminal.

**Bibliotecas utilizadas:**

- `http.client`
- `json`

**Conceitos aplicados:**

- Funções em Python.
- Requisições HTTP.
- Consumo de APIs.
- Conversão de JSON.
- Estruturas condicionais.
- Entrada e saída de dados.

---

### 2.2. `extracao02.py` — Consulta de CEP com Exportação para Excel

**Descrição:**

Evolução do primeiro script, adicionando a capacidade de organizar os dados retornados pela API ViaCEP e exportá-los para uma planilha Excel.

**Funcionamento:**

1. Solicita ao usuário um CEP.
2. Realiza a consulta na API ViaCEP.
3. Recebe os dados do endereço.
4. Verifica se o CEP foi encontrado.
5. Converte as informações em um DataFrame utilizando Pandas.
6. Exporta os dados para um arquivo Excel.

**Bibliotecas utilizadas:**

- `http.client`
- `json`
- `pandas`
- `openpyxl`

**Conceitos aplicados:**

- Consumo de APIs.
- Manipulação de dados.
- Criação de DataFrames.
- Exportação de informações para Excel.
- Organização de arquivos.

---

### 2.3. `extracaocep03.py` — Consulta Automatizada de Múltiplos CEPs

**Descrição:**

Terceira etapa do projeto, desenvolvida para automatizar a consulta de vários CEPs armazenados em uma planilha Excel.

Diferentemente das versões anteriores, o usuário não precisa informar cada CEP individualmente no terminal. O script realiza a leitura dos dados diretamente de uma planilha e executa as consultas automaticamente.

**Funcionamento:**

1. Acessa uma planilha Excel utilizando Pandas.
2. Realiza a leitura da aba denominada `CEP`.
3. Obtém os valores da coluna `CEP`.
4. Percorre os CEPs utilizando uma estrutura de repetição `for`.
5. Realiza requisições HTTP para a API ViaCEP.
6. Verifica se cada CEP possui um endereço válido.
7. Organiza os dados retornados em um DataFrame.
8. Armazena os resultados em uma aba denominada `Dados` na mesma planilha Excel.

**Informações extraídas:**

- CEP
- Logradouro
- Bairro
- Localidade
- UF

**Bibliotecas utilizadas:**

- `http.client`
- `json`
- `pandas`
- `openpyxl`

**Conceitos aplicados:**

- Automação de consultas em lote.
- Leitura de arquivos Excel.
- Consumo de APIs.
- Estruturas de repetição.
- Tratamento de dados.
- Manipulação de DataFrames.
- Gravação de resultados em planilhas.
- Organização de informações em múltiplas abas.

### 🎯 Objetivo do Projeto

Desenvolver uma solução capaz de automatizar a consulta de endereços em larga escala, utilizando uma fonte de dados Excel como entrada e outra aba da mesma planilha para armazenar os resultados.

---

# 📚 Conhecimentos Aplicados

Durante o desenvolvimento dos projetos, foram trabalhados os seguintes conhecimentos:

- Fundamentos da linguagem Python.
- Criação e reutilização de funções.
- Importação e utilização de bibliotecas.
- Requisições HTTP e consumo de APIs.
- Manipulação de dados JSON.
- Automação de navegação web.
- Leitura e escrita de arquivos Excel.
- Tratamento e organização de dados com Pandas.
- Estruturas condicionais e de repetição.
- Controle de versão com Git.
- Versionamento e publicação de projetos no GitHub.

---

# 🚀 Como Executar os Projetos

### 1. Pré-requisitos

É necessário ter instalado:

- Python 3.
- Visual Studio Code ou outro editor de código.
- Git.
- Bibliotecas utilizadas em cada projeto.

### 2. Clonar o repositório

```bash
git clone https://github.com/henriqueoliveira-dev/python-rpa.git
```

### 3. Acessar a pasta do projeto

```bash
cd python-rpa/Python.RPA3/extracao_cep_para_excel
```

### 4. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 5. Ativar o ambiente virtual no Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 6. Instalar as bibliotecas necessárias

Para os projetos que utilizam Pandas e Excel:

```bash
python -m pip install pandas openpyxl XlsxWriter selenium
```

### 7. Executar os scripts

Exemplo para consulta individual de CEP:

```bash
python extracao01.py
```

Exemplo para consulta automatizada de múltiplos CEPs:

```bash
python extracaocep03.py
```

**Observação:** os comandos devem ser executados nesta pasta. Os scripts `extracao02.py` e `extracaocep03.py` precisam das dependências `pandas` e `openpyxl` (instale com `python -m pip install pandas openpyxl`). O script em lote espera um arquivo `CEP.xlsx` ao lado do próprio script, com uma aba `CEP` e coluna `CEP`; ele grava ou substitui a aba `Dados`. O arquivo de saída de `extracao02.py` é `endereco.xlsx` no diretório de execução.

---

# 📈 Evolução dos Projetos

Este repositório representa a evolução prática dos conhecimentos em Python e automação de processos, começando por scripts de consulta e extração de informações e avançando para soluções que integram APIs, tratamento de dados e planilhas Excel.

Os projetos serão atualizados continuamente, conforme novos conhecimentos e soluções de automação forem desenvolvidos.

---

## 👨‍💻 Autor

**Henrique Oliveira**

Desenvolvimento de projetos práticos com Python, automação de processos (RPA), consumo de APIs e manipulação de dados.

🔗 **GitHub:** [henriqueoliveira-dev](https://github.com/henriqueoliveira-dev)

---

