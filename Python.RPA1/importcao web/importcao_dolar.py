import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def consultar_cotacao(navegador, moeda):
    campo_pesquisa = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )
    campo_pesquisa.clear()
    campo_pesquisa.send_keys(f"{moeda} hoje", Keys.RETURN)
    elemento_valor = WebDriverWait(navegador, 15).until(
        EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')
        )
    )
    return elemento_valor.text


def main():
    navegador = webdriver.Chrome()
    try:
        navegador.get("https://www.google.com/")
        for moeda in ("Dólar", "Euro"):
            try:
                valor = consultar_cotacao(navegador, moeda)
            except TimeoutException:
                print(f"Não foi possível localizar a cotação de {moeda}.")
                continue
            print(f"{moeda}: {valor}")
            time.sleep(1)
    finally:
        navegador.quit()


if __name__ == "__main__":
    main()
