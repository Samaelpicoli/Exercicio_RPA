from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def login(driver, wdw, username, password):
    #login na página
    try:
        driver.get('https://rpaexercise.aisingapore.org/login')
        driver.maximize_window()
        wdw.until(ec.element_to_be_clickable((By.ID, 'outlined-search')))
        driver.find_element(By.ID, 'outlined-search').send_keys(username)
        driver.find_element(By.ID, 'password').send_keys(password)
        driver.find_element(By.ID, 'login').click()
        return True
    except Exception as e:
        print('Erro no login')
        print(e)
        raise Exception('Erro ao fazer o login')

def inserir_dados(driver, wdw, df):
    #insere os dados do arquivo CSV nos campos solicitados
    try:
        for index, row in df.iterrows():
            wdw.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="newJobPosting"]/span[1]')))
            driver.find_element(By.XPATH, '//*[@id="newJobPosting"]/span[1]').click()
            wdw.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="form-dialog-title"]/h2')))
            print('Iniciou')
            driver.find_element(By.ID, 'jobTitle').send_keys(row['jobTitle'])
            driver.find_element(By.ID, 'jobDescription').send_keys(row['jobDescription'])
            Select(driver.find_element(By.ID, 'hiringDepartment')).select_by_visible_text(row['hiringDepartment'])
            Select(driver.find_element(By.ID, 'educationLevel')).select_by_visible_text(row['educationLevel'])
            driver.find_element(By.ID, 'postingStartDate').send_keys(row['postingStartDate'])
            driver.find_element(By.ID, 'postingEndDate').send_keys(row['postingEndDate'])
            if 'YES' in row['remote'].upper():
                driver.find_element(By.XPATH, '//*[@id="remote"]/label[1]/span[1]/span[1]/input').click()
            else:
                driver.find_element(By.XPATH, '//*[@id="remote"]/label[2]/span[1]/span[1]/input').click()
            if 'FULL' in row['jobType'].upper():
                driver.find_element(By.ID, 'jobTypeFullTime').click()
            if 'PART' in row['jobType'].upper():
                driver.find_element(By.ID, 'jobTypePartTime').click()
            if 'TEMP' in row['jobType'].upper():
                driver.find_element(By.ID, 'jobTypeTemp').click()
            if 'PERMANENT' in row['jobType'].upper():
                driver.find_element(By.ID, 'jobTypePermanent').click()
            driver.find_element(By.XPATH, '//*[@id="submit"]/span[1]').click()
        return True
    except Exception as e:
        print('Erro ao inserir os dados')
        print(e)
        raise Exception('Erro durante a inserção de dados')

def avaliar_dados(driver, wdw, df):
    #Avalia se o candidato será aprovado ou rejeitado, a partir da coleta de alguns dados
    #do site, e compara se o nível de educação é o requirido para a vaga e se a pontuação > 70
    try:
        for i in range(len(df)): 
            i = i+1
            wdw.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="newJobPosting"]/span[1]')))
            driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[2]/div[2]/div[{i}]/div/div[2]/div/a/button/span[1]').click()
            wdw.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="backToList"]/span[1]')))
            text_level_education = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[10]/p').text
            print(text_level_education)
            number_rows = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr')
            for n in range(len(number_rows)):
                n = n+1
                education_level = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{n}]/td[4]').text
                pre_screening_score = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{n}]/td[5]').text
                if education_level.strip() == text_level_education.strip() and int(pre_screening_score) > 70:
                    print('Approved')
                    driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{n}]/td[7]/div/div/button[1]/span[1]').click()
                else:
                    print('Rejected')
                    driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{n}]/td[7]/div/div/button[2]/span[1]').click()
            if i < len(df):
                driver.find_element(By.XPATH, '//*[@id="backToList"]/span[1]').click()
            try:
                finished = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/h2').text 
                if 'Congratulations' in finished:
                    print('Sucesfully')
            except:
                pass
        return True
    except Exception as e:
        print('Erro ao avaliar dados')
        print(e)
        raise Exception('Erro ao avaliar os dados')
