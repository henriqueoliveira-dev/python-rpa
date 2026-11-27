from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
from openpyxl import load_workbook
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# --------------------------------------------------
# ABRIR PLANILHA
# --------------------------------------------------

nomeCaminhoArquivo = r"C:\Users\Henrique Oliveira\OneDrive\Documentos\Projeto-RPA\DadosFormulario.xlsx"

planilha_aberta = load_workbook(filename=nomeCaminhoArquivo)

sheet_selecionada = planilha_aberta["Dados"]


# --------------------------------------------------
# PERCORRER AS LINHAS DA PLANILHA
# --------------------------------------------------

for linha in range(2, sheet_selecionada.max_row + 1):

    nome = sheet_selecionada[f"A{linha}"].value
    email = sheet_selecionada[f"B{linha}"].value
    telefone = sheet_selecionada[f"C{linha}"].value
    sexo = sheet_selecionada[f"D{linha}"].value
    sobre = sheet_selecionada[f"E{linha}"].value


    # --------------------------------------------------
    # ABRIR NAVEGADOR
    # --------------------------------------------------

    navegadorFormulario = opcoesSelenium.Chrome()

    navegadorFormulario.get(
        "https://www.surveymonkey.com/r/WLXYDX2"
    )

    espera = WebDriverWait(navegadorFormulario, 10)


    # --------------------------------------------------
    # NOME
    # --------------------------------------------------

    campo_nome = espera.until(
        EC.presence_of_element_located(
            (By.NAME, "166517069")
        )
    )

    campo_nome.send_keys(nome)
    print("Página aberta:", navegadorFormulario.current_url)
    print("Título:", navegadorFormulario.title)

    # --------------------------------------------------
    # E-MAIL
    # --------------------------------------------------

    campo_email = espera.until(
        EC.presence_of_element_located(
            (By.NAME, "166517072")
        )
    )

    campo_email.send_keys(email)


    # --------------------------------------------------
    # TELEFONE
    # --------------------------------------------------

    campo_telefone = espera.until(
        EC.presence_of_element_located(
            (By.NAME, "166517070")
        )
    )

    campo_telefone.send_keys(telefone)


    # --------------------------------------------------
    # SOBRE
    # --------------------------------------------------

    campo_sobre = espera.until(
        EC.presence_of_element_located(
            (By.NAME, "166517073")
        )
    )

    campo_sobre.send_keys(sobre)


    # --------------------------------------------------
    # SEXO
    # --------------------------------------------------

    if sexo == "Masculino":

        botao_masculino = espera.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[contains(., 'Masculino')]")
            )
        )

        botao_masculino.click()

    elif sexo == "Feminino":

        botao_feminino = espera.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[contains(., 'Feminino')]")
            )
        )

        botao_feminino.click()


    # --------------------------------------------------
    # ENVIAR FORMULÁRIO
    # --------------------------------------------------

    botao_enviar = espera.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="view-pageNavigation"]/div/button')
        )
    )

    botao_enviar.click()


    # --------------------------------------------------
    # FECHAR NAVEGADOR
    # --------------------------------------------------

    navegadorFormulario.quit()