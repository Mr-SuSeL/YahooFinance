from selenium import webdriver
# pip install webdriver-manager
# pip install selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# Nowa wersja selenium wymaga by czytać "by":
from selenium.webdriver.common.by import By

import time
import os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
# /html/body/div/header/div/div[1]/div/form/fieldset/input
# //*[@id="id-search-field"]

options = Options()
options.page_load_strategy = 'normal'
# options.headless = True

# Odkomentuj poniżej jeśli nie masz zainstalowanego Chrome'a
# driver = webdriver.Chrome( ChromeDriverManager().install(), options = options )
driver = webdriver.Chrome( options = options )
driver.get("https://python.org")
driver.maximize_window()
# searchInput = driver.find_element(By.XPATH, "/html/body/div/header/div/div[1]/div/form/fieldset/input")
searchInput = driver.find_element(By.ID, "id-search-field")
# searchInput = driver.find_element_by_xpath('//*[@id="id-search-field"]') # To już nie zadziała w Selenium_v4
searchInput.send_keys("django")

time.sleep(25)
driver.quit()