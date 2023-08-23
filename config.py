from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
wdw = WebDriverWait(driver, 40)

username = 'jane007'
password = 'TheBestHR123'