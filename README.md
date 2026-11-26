# 🤖 Python RPA — Automação de Processos com Python

> **Transformando processos manuais e repetitivos em automações com Python.**

Este repositório reúne minha evolução prática no desenvolvimento de soluções de **RPA (Robotic Process Automation)** utilizando Python.

Mais do que uma coleção de scripts, este projeto representa a construção gradual de uma base de automação capaz de **interagir com aplicações, navegadores, arquivos, planilhas, APIs e sistemas**, sempre buscando reduzir tarefas manuais e tornar processos mais rápidos, organizados e confiáveis.

O repositório está em **desenvolvimento contínuo**. Novas automações, experimentos e soluções serão incorporados conforme novos cenários forem desenvolvidos.

---

## 🎯 O que estou construindo

A proposta deste projeto é explorar como Python pode ser utilizado para automatizar diferentes etapas de um processo:

```text
                    PROCESSO MANUAL
                           │
                           ▼
                 ┌───────────────────┐
                 │ Identificar tarefa │
                 │ repetitiva         │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Processar dados   │
                 │ Excel / CSV / API │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Executar processo │
                 │ automaticamente   │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Gerar / atualizar │
                 │ informações       │
                 └─────────┬─────────┘
                           │
                           ▼
                  PROCESSO AUTOMATIZADO
```

O objetivo é evoluir de pequenas automações para **fluxos completos de RPA**, conectando diferentes tecnologias dentro de um mesmo processo.

---

# 🧩 Áreas de automação

Ao longo do desenvolvimento, o projeto aborda diferentes formas de automação.

### 🖥️ Automação de aplicações

Interação automatizada com o ambiente Windows utilizando **PyAutoGUI**.

Exemplos:

- Controle de mouse e teclado
- Abertura de aplicações
- Navegação entre janelas
- Execução de comandos
- Interação com aplicações desktop
- Automação baseada em interface gráfica

---

### 🌐 Automação Web

Automação de navegadores utilizando **Selenium**.

Aplicações desenvolvidas envolvem:

- Abertura automática do navegador
- Navegação em páginas Web
- Localização de elementos HTML
- Utilização de `NAME` e `XPATH`
- Preenchimento de campos
- Captura de informações
- Execução automatizada de operações no navegador

A evolução deste módulo também contempla **automação de preenchimento de formulários Web**, permitindo transformar dados estruturados em ações automatizadas dentro de sistemas.

---

### 📊 Automação de dados e Excel

O projeto também trabalha com a utilização de planilhas como fonte e destino de informações.

Entre os processos explorados:

- Leitura de planilhas
- Criação de arquivos Excel
- Escrita de dados
- Processamento de registros em lote
- Organização de informações
- Exportação de resultados
- Integração entre Excel e automações Python

---

### 🔌 Integração com APIs

Outra parte importante do projeto é a utilização de APIs para transformar consultas manuais em processos automatizados.

Exemplos desenvolvidos:

- Consulta de CEP
- Consulta de dados empresariais por CNPJ
- Consumo de APIs HTTP/HTTPS
- Processamento de respostas JSON
- Tratamento de dados
- Exportação dos resultados para Excel

---

# 🚀 De scripts para processos

A evolução deste repositório segue uma linha de desenvolvimento:

```text
Python
   │
   ▼
Automação de tarefas
   │
   ▼
PyAutoGUI
   │
   ▼
Automação de aplicações
   │
   ▼
Excel / CSV
   │
   ▼
APIs e JSON
   │
   ▼
Selenium
   │
   ▼
Automação Web
   │
   ▼
Formulários e processos
   │
   ▼
Integração de etapas
   │
   ▼
RPA
```

A intenção é deixar de pensar apenas em **"automatizar uma ação"** e passar a pensar em **"automatizar um processo"**.

---

# 🛠️ Tecnologias

As tecnologias utilizadas variam conforme cada automação.

| Tecnologia | Utilização |
|---|---|
| 🐍 Python | Desenvolvimento das automações |
| 🖱️ PyAutoGUI | Automação de mouse, teclado e aplicações |
| 🌐 Selenium | Automação e interação com navegadores |
| 📊 Pandas | Tratamento e processamento de dados |
| 📗 OpenPyXL | Leitura e escrita de Excel |
| 📑 XlsxWriter | Criação de planilhas |
| 🔌 HTTP / HTTPS | Comunicação com APIs |
| 📦 JSON | Processamento de dados estruturados |
| 🔧 Git | Controle de versão |
| 🐙 GitHub | Versionamento e documentação |
| 💻 VS Code | Ambiente de desenvolvimento |

Novas ferramentas serão adicionadas conforme os processos de automação evoluírem.

---

# 📂 Estrutura do projeto

O repositório é organizado por etapas de desenvolvimento e diferentes tipos de automação.

```text
python-rpa/
│
├── Python.RPA1/
│   └── Automação Web / Excel
│
├── Python.RPA2/
│   └── Automação com PyAutoGUI
│
├── Python.RPA3/
│   └── APIs / CEP / Excel
│
├── Python.RPA4/
│   └── APIs / CNPJ / Processamento de dados
│
├── Python.RPA5/
│   └── Automação Web / Formulários / RPA
│
└── README.md
```

> A estrutura continuará sendo atualizada conforme novos processos e automações forem incorporados ao projeto.

---

# ⚙️ Tipos de processos explorados

O projeto busca trabalhar com cenários encontrados em atividades administrativas e operacionais, como:

- 📄 Transferência de informações entre sistemas
- 📊 Processamento de planilhas
- 🌐 Preenchimento de formulários Web
- 🔎 Consulta e extração de informações
- 🔌 Integração com APIs
- 🖥️ Automação de aplicações desktop
- 📁 Manipulação de arquivos
- 🔄 Processamento de dados em lote
- 📋 Geração e atualização de informações
- 🤖 Execução automática de tarefas repetitivas

---

# 🧠 Conceito por trás do projeto

Uma automação de RPA não precisa apenas executar comandos.

Ela pode seguir um fluxo completo:

```text
ENTRADA
  │
  ├── Excel
  ├── CSV
  ├── API
  └── Sistema
       │
       ▼
PROCESSAMENTO
       │
       ├── Validação
       ├── Tratamento
       └── Organização
       │
       ▼
AUTOMAÇÃO
       │
       ├── Aplicação Desktop
       ├── Navegador
       └── Sistema Web
       │
       ▼
RESULTADO
       │
       ├── Excel
       ├── Sistema
       ├── Relatório
       └── Banco de dados
```

Esse é o caminho que estou utilizando para evoluir meus conhecimentos de Python para **automação de processos e desenvolvimento de soluções mais completas**.

---

# 📈 Evolução contínua

Este repositório não representa um projeto finalizado.

Ele acompanha minha evolução prática em:

- Python
- Automação
- RPA
- Automação Web
- Manipulação de dados
- APIs
- Excel
- Integração entre sistemas

Novos projetos serão adicionados gradualmente, principalmente aqueles que envolvem **problemas reais e processos que podem ser automatizados**.

---

# 🔭 Próximos passos

A evolução planejada inclui automações cada vez mais próximas de cenários reais:

- [x] Automação de mouse e teclado
- [x] Automação de aplicações Windows
- [x] Manipulação de arquivos Excel
- [x] Consumo de APIs
- [x] Processamento de dados
- [x] Automação Web com Selenium
- [ ] Automação de formulários Web
- [ ] Processamento de dados em lote
- [ ] Fluxos RPA completos
- [ ] Integração entre diferentes sistemas
- [ ] Registro e monitoramento das execuções
- [ ] Projetos de automação orientados a problemas reais

---

# 💡 Por que RPA?

Muitos processos ainda dependem de atividades manuais:

```text
Copiar dados
     ↓
Abrir sistema
     ↓
Preencher campos
     ↓
Salvar
     ↓
Repetir
     ↓
Repetir
     ↓
Repetir...
```

A automação permite transformar esse fluxo em:

```text
Dados de entrada
       ↓
      BOT
       ↓
Processamento
       ↓
Sistema
       ↓
Resultado
```

O objetivo deste projeto é justamente explorar essa transformação utilizando **Python como ferramenta de automação**.

---

# 👨‍💻 Autor

## Henrique Oliveira

Estudante de **Análise e Desenvolvimento de Sistemas**, com foco no desenvolvimento de soluções utilizando:

**Python • RPA • Automação • APIs • Backend • Banco de Dados • Desenvolvimento de Sistemas**

Este repositório faz parte da minha evolução prática no desenvolvimento de soluções de automação e integração de sistemas.

---

### ⭐ Em desenvolvimento

> **Automação não é apenas fazer o computador executar uma tarefa.  
> É transformar um processo manual em uma solução que possa ser executada de forma inteligente, consistente e repetível.**

---
