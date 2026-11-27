# 🤖 Automação de Formulário Web com Python

Automação de preenchimento de formulário Web utilizando **Python + Selenium + Excel**, desenvolvida como parte da evolução prática em RPA.

O projeto lê os dados de uma planilha Excel, percorre os registros e utiliza o Selenium para preencher automaticamente um formulário Web.

A proposta é transformar um processo manual e repetitivo em um fluxo automatizado.

---

## 🎯 Objetivo

Automatizar o seguinte processo:

```text
Excel
  │
  ▼
Ler dados
  │
  ▼
Selecionar registro
  │
  ▼
Abrir navegador
  │
  ▼
Acessar formulário Web
  │
  ▼
Preencher campos
  │
  ├── Nome
  ├── E-mail
  ├── Telefone
  ├── Sexo
  └── Sobre
  │
  ▼
Enviar formulário
  │
  ▼
Fechar navegador
```

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| 🐍 Python | Desenvolvimento da automação |
| 🌐 Selenium | Controle e automação do navegador |
| 📊 OpenPyXL | Leitura da planilha Excel |
| ⏳ WebDriverWait | Espera explícita dos elementos |
| 🔎 By.NAME | Localização dos campos |
| 🔎 By.XPATH | Localização de elementos Web |
| 🧩 Expected Conditions | Validação da disponibilidade dos elementos |
| 🌐 Google Chrome | Navegador utilizado na automação |

---

## 📊 Entrada de dados

Os dados são obtidos através de uma planilha Excel.

Exemplo de estrutura:

| Nome | E-mail | Telefone | Sexo | Sobre |
|---|---|---|---|---|
| Amanda Martins | amanda@email.com | (11) 9876-3284 | Feminino | Automação com Python |
| João Silva | joao@email.com | (11) 99999-9999 | Masculino | Desenvolvimento |

A automação inicia a leitura a partir da **segunda linha**, considerando a primeira linha como cabeçalho.

---

## ⚙️ Funcionamento

O programa utiliza `openpyxl` para abrir a planilha e acessar a aba `Dados`.

Em seguida:

1. Percorre as linhas da planilha.
2. Obtém os valores de cada registro.
3. Abre o Google Chrome.
4. Acessa o formulário Web.
5. Aguarda os elementos utilizando `WebDriverWait`.
6. Preenche os campos.
7. Seleciona o sexo correspondente.
8. Localiza o botão de envio.
9. Envia o formulário.
10. Fecha o navegador.
11. Continua para o próximo registro.

---

## 🔎 Localização dos elementos

O projeto utiliza diferentes estratégias do Selenium para localizar elementos.

### Por `NAME`

```python
(By.NAME, "166517069")
```

Utilizado para localizar campos como:

- Nome
- E-mail
- Telefone
- Sobre

### Por `XPATH`

```python
(By.XPATH, "//label[contains(., 'Masculino')]")
```

Utilizado para localizar opções específicas do formulário.

Também é utilizado para localizar o botão de envio:

```python
(By.XPATH, '//*[@id="view-pageNavigation"]/div/button')
```

---

## ⏳ Espera explícita

Em vez de depender somente de `sleep()`, o projeto utiliza:

```python
WebDriverWait()
```

com:

```python
EC.presence_of_element_located()
```

e:

```python
EC.element_to_be_clickable()
```

Isso permite que o Selenium aguarde o elemento estar disponível antes de executar a ação.

---

## 🔄 Processamento em lote

Uma das principais características deste projeto é a possibilidade de processar vários registros:

```text
Registro 1 → Formulário → Envio
Registro 2 → Formulário → Envio
Registro 3 → Formulário → Envio
Registro 4 → Formulário → Envio
        ...
```

Dessa forma, o processo não depende da digitação manual de cada registro.

---

## 📁 Estrutura

```text
automacao_formulario_excel/
│
├── README.md
├── automacao_formulario.py
└── DadosFormulario.xlsx
```

---

## 🚀 Evolução do projeto

Este projeto representa uma evolução de automações simples para um fluxo mais próximo de um processo real de RPA:

```text
Selenium
   ↓
Localização de elementos
   ↓
Preenchimento manual via código
   ↓
Leitura de Excel
   ↓
Processamento de vários registros
   ↓
Automação de formulário
   ↓
Fluxo RPA
```

---

## 📚 Conceitos praticados

- Selenium WebDriver
- Google Chrome
- `By.NAME`
- `By.XPATH`
- `send_keys()`
- `click()`
- `WebDriverWait`
- Expected Conditions
- OpenPyXL
- Leitura de Excel
- Laços `for`
- Processamento de múltiplos registros
- Automação Web
- RPA

---

## ⚠️ Observação

O formulário utilizado neste projeto serve como ambiente de estudo e demonstração da automação.

Os identificadores dos elementos (`NAME` e `XPATH`) podem mudar caso a estrutura da página seja alterada.

---

## 🎯 Próximas evoluções

- [ ] Tratamento de erros por registro
- [ ] Registro de sucesso/fal