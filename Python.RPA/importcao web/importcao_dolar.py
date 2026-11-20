
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver as opcoes_selenium

from selenium.webdriver.common.by import By

import pyautogui as tempoPausaComputador
import pyautogui as teclasAtalhoTeclado
import time

# Abrir navegador
meuNavegador = opcoes_selenium.Chrome()

# Acessar Google
meuNavegador.get('https://www.google.com/')

# Aguardar carregamento
time.sleep(3)

# Localizar campo de pesquisa e digitar
meuNavegador.find_element(By.NAME, 'q').send_keys('Dolar hoje')

# Aguardar
time.sleep(3)

meuNavegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)

time.sleep(10)


valorDolarPeloGoogle = meuNavegador.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).text

print(valorDolarPeloGoogle)

#--------------------------------------------------------------

#achando valor do Euro

time.sleep(3)

meuNavegador.find_element(By.NAME, 'q').send_keys("")

time.sleep(3)

teclasAtalhoTeclado.press('tab')

time.sleep(3)

teclasAtalhoTeclado.press('enter')


time.sleep(3)

meuNavegador.find_element(By.NAME, 'q').send_keys('Euro hoje')

time.sleep(3)

meuNavegador.find_element(By.NAME, 'q').send_keys(Keys.RETURN)

time.sleep(10)


valorEuroPeloGoogle = meuNavegador.find_element(
    By.XPATH,
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]'
).text

print(valorEuroPeloGoogle)