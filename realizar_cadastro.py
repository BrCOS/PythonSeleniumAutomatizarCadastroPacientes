from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

file = 'arquivo_tratado_xlsx'
df = pd.read_excel(file)

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

browser.get("link_do_site")#colocar o link direto da pagina de login
browser.maximize_window()

login = browser.find_element(By.ID, 'Email')
login.send_keys('email_ou_login')

senha = browser.find_element(By.ID, 'Password')
senha.send_keys('senha')

entrar = browser.find_element(By.ID, 'btnLogin')
entrar.click()

time.sleep(5)

btn_pacientes = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Pacientes')))
btn_pacientes.click()

time.sleep(5)

for index, row in df.iterrows():
    btn_add = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn.btn-default.btn-circle')))
    btn_add.click()

    time.sleep(5)

    nome = browser.find_element(By.ID, 'Nome')
    data = browser.find_element(By.ID, 'Nascimento')
    e_mail = browser.find_element(By.ID, 'Email')
    tel = browser.find_element(By.ID, 'Dados_Telefone1')

    nome.send_keys(row['Paciente'])
    data.send_keys(row['DtNascimento'])
    tel.send_keys(row['Celular'])

    if pd.notna(row['E_Mail']):
        e_mail.send_keys(row['E_Mail'])

    btn_finish = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btnPacienteConfirmar')))
    btn_finish.click()

    time.sleep(5)

    btn_finish2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btnPacienteFechar')))
    btn_finish2.click()

    time.sleep(5)

    browser.get("link_do_site")

    time.sleep(5)