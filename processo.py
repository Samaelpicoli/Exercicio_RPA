from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec

def login(driver, wdw, username, password):
    #inicializa a página e faz o login  
    driver.get('https://rpaexercise.aisingapore.org/login')
    driver.maximize_window()
    wdw.until(ec.element_to_be_clickable((By.ID, 'outlined-search')))
    driver.find_element(By.ID, 'outlined-search').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID, 'login').click()
    
def inserir_dados(driver, wdw, arquivo):
    #faz a inserção dos dados do arquivo csv na página
    for index, row in arquivo.iterrows():
        wdw.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="newJobPosting"]/span[1]')))
        driver.find_element(By.XPATH, '//*[@id="newJobPosting"]/span[1]').click()
        wdw.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="form-dialog-title"]/h2')))
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
        

def avaliar_dados(driver, wdw, arquivo):
    #faz a avaliação se o candidato será aprovado ou rejeitado, a partir da coleta de alguns dados
    #do site, e compara se o nível de educação é o requirido para a vaga e se a pontuação é maior que 70
    #ao final, ele tira um print da conclusão do projeto
    
    for i in range(len(arquivo)): 
        i = i+1
        wdw.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="newJobPosting"]/span[1]')))
        driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[2]/div[2]/div[{i}]/div/div[2]/div/a/button/span[1]').click()
        wdw.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="backToList"]/span[1]')))
        nivel_educacional_requerido = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/div[10]/p').text
        number_rows = driver.find_elements(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr')
        for n in range(len(number_rows)):
            n = n+1
            nivel_educacional_candidato = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{n}]/td[4]').text
            score = driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{n}]/td[5]').text
            
            if nivel_educacional_candidato.strip() == nivel_educacional_requerido.strip() and int(score) > 70:
                driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{n}]/td[7]/div/div/button[1]/span[1]').click()
            else:
                driver.find_element(By.XPATH, f'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/table/tbody/tr[{n}]/td[7]/div/div/button[2]/span[1]').click()
        
        if i < len(arquivo):
            driver.find_element(By.XPATH, '//*[@id="backToList"]/span[1]').click()

    
    finished = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/h2').text 
    if 'Congratulations' in finished:
        driver.save_screenshot('Congratulations.png')
        print('Sucesso')
