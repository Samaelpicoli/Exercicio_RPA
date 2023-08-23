from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas as pd


from config import *
import process 

#leitura do arquivo csv que será usado para inserir os dados
df = pd.read_csv('datatable.csv', sep=',')


process.login(driver, wdw, username, password)
process.inserir_dados(driver, wdw, df)
process.avaliar_dados(driver, wdw, df)

print('Finalizado!')
driver.close()
