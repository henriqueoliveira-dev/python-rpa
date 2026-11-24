# Automação de Consulta e Extração de Dados de CNPJ

## Sobre o Projeto

Este projeto consiste no desenvolvimento de três aplicações em Python voltadas à automação da consulta, extração, tratamento e armazenamento de informações cadastrais de empresas brasileiras por meio do CNPJ.

As aplicações utilizam a API da ReceitaWS para obter informações empresariais, automatizando tarefas que normalmente seriam realizadas manualmente.

O projeto faz parte de um conjunto de estudos e aplicações práticas de **RPA (Robotic Process Automation)**, com foco em produtividade, organização de dados e automação de processos administrativos.

## Objetivo

Desenvolver soluções automatizadas capazes de consultar informações empresariais a partir de um CNPJ, tratar os dados retornados pela API e exportar os resultados para planilhas Excel.

## Aplicações Desenvolvidas

### 1. Consulta de Dados Empresariais por CNPJ

Aplicação responsável por realizar consultas individuais de CNPJ utilizando a API da ReceitaWS.

**Funcionalidades:**
- Consulta individual de um CNPJ de exemplo definido no próprio script.
- Requisição HTTP utilizando `http.client`.
- Comunicação segura via HTTPS.
- Recebimento e leitura da resposta da API.
- Decodificação dos dados em formato JSON.
- Tratamento de erros de comunicação e respostas HTTP.

### 2. Tratamento e Organização de Dados Empresariais

Aplicação destinada ao tratamento das informações retornadas pela API, organizando dados simples e estruturas aninhadas.

**Funcionalidades:**
- Tratamento de atividades principais e secundárias.
- Organização dos dados do quadro societário (QSA).
- Conversão de estruturas complexas em informações legíveis.
- Tratamento de campos adicionais, como Simples Nacional e SIMEI.
- Preparação dos dados para armazenamento em planilhas.

### 3. Extração e Exportação de Dados para Excel

Aplicação responsável por armazenar os dados empresariais consultados em uma planilha Excel.

**Funcionalidades:**
- Integração entre consulta de CNPJ e exportação dos resultados.
- Organização dos dados utilizando DataFrame.
- Exportação automática para arquivos `.xlsx`.
- Utilização da biblioteca Pandas.
- Armazenamento dos dados em diretório definido pelo usuário.

## Tecnologias e Bibliotecas

| Tecnologia | Aplicação |
|---|---|
| Python | Linguagem principal |
| http.client | Requisições HTTP/HTTPS |
| JSON | Leitura e interpretação dos dados |
| Pandas | Organização e manipulação dos dados |
| OpenPyXL | Integração com arquivos Excel |
| ReceitaWS API | Consulta de informações empresariais |

## Informações Consultadas

As consultas podem retornar informações como:

- CNPJ;
- Razão social;
- Nome fantasia;
- Situação cadastral;
- Data de abertura;
- Telefone;
- E-mail;
- Endereço completo;
- Atividade econômica principal;
- Atividades econômicas secundárias;
- Quadro societário;
- Informações sobre Simples Nacional e SIMEI.

A disponibilidade dos campos depende dos dados retornados pela API.

## Estrutura do Projeto

```text
Python.RPA4/
│
├── README.md
└── extracaocnpj/
    │
    ├── extracaocnpj_v1.py
    ├── extracaocnpj_v2.py
    └── extracaocnpj_v3.py
```

## Instalação e Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/henriqueoliveira-dev/python-rpa.git
```

### 2. Acessar a pasta do projeto

```bash
cd python-rpa/Python.RPA4/extracaocnpj
```

### 3. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
python -m pip install pandas openpyxl
```

## Como Executar

Execute a aplicação desejada pelo terminal:

```bash
python extracaocnpj_v1.py
```

Para executar as demais aplicações, utilize seus respectivos nomes de arquivo.

## Exportação dos Dados

As aplicações que possuem exportação para Excel permitem armazenar os dados consultados em arquivos `.xlsx`.

Exemplo de arquivo gerado:

```text
Projeto-RPA/
│
└── dados_empresa.xlsx
```

O script `extracaocnpj_v2.py` grava por padrão `dados_empresa.xlsx` no diretório de execução; é possível passar outro nome ao chamar a função `salvar_dados_empresa_excel`. O script em lote espera `CNPJ.xlsx` ao lado do arquivo Python, com uma aba `CNPJ` e coluna `CNPJ`, e grava ou substitui a aba `Dados`.

## Tratamento de Erros

As aplicações possuem mecanismos para identificar situações como:

- Falhas na comunicação com a API;
- Respostas HTTP diferentes de 200;
- Erros na decodificação do JSON;
- Retornos de erro da API;
- Ausência de informações cadastrais.

## Observações

- A consulta depende da disponibilidade da API ReceitaWS.
- A API pode possuir limites de requisições e condições de utilização.
- Os dados retornados devem ser utilizados respeitando as condições de uso da API e a legislação aplicável.
- Recomenda-se validar as informações obtidas antes de utilizá-las em processos empresariais.

## Aprendizados Técnicos

Este projeto permite aplicar conhecimentos práticos em:

- Integração com APIs REST;
- Requisições HTTP e HTTPS;
- Manipulação de dados JSON;
- Funções e modularização em Python;
- Tratamento de exceções;
- Manipulação de planilhas Excel;
- Automação de processos administrativos;
- Organização e estruturação de projetos Python.

## Autor

**Henrique Oliveira**

Desenvolvedor Python | Automação RPA

GitHub: https://github.com/henriqueoliveira-dev

---

Projeto desenvolvido com o objetivo de aplicar Python na automação de processos reais de consulta, extração e organização de dados empresariais.
