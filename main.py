#BIBLIOTECAS UTILIZADAS NO PROCESSO
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd
import requests

#MÓDULOS UTILIZADOS NO PROCESSO
from config import usuario, senha
import processo 
import pega_arquivo as get

status_loop = 'ON'
estado = 'INITIALIZATION'

while status_loop == 'ON':

    match estado:

        case 'INITIALIZATION':
            try:
                options = webdriver.ChromeOptions()
                options.add_argument("--disable-notifications")
                driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
                wdw = WebDriverWait(driver, 40)
                processo.login(driver, wdw, usuario, senha)
                estado = 'GET TRANSACTION'
                continue
            except Exception as error:
                print(f'Erro durante a inicialização: {error}')
                estado = 'END'
                continue
            
        case 'GET TRANSACTION':
            try:
                nome_arquivo = get.solicitar_csv()
                arquivo = pd.read_csv(nome_arquivo, sep=',')
                estado = 'PROCESS'
                continue
            except Exception as error:
                print(f'Erro durante a captura dos dados: {error}')
                estado = 'END'
                continue

        case 'PROCESS':
            try:
                processo.inserir_dados(driver, wdw, arquivo)
                processo.avaliar_dados(driver, wdw, arquivo)
                estado = 'END'
                continue
            except Exception as error:
                print(f'Erro durante o processamento: {error}')
                estado = 'END'
                continue

        case 'END':
            print('Finalizado!')
            driver.close()
            status_loop = 'OFF'
            continue
