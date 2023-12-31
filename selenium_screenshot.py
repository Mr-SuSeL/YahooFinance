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

options = Options()
options.page_load_strategy = 'normal'
options.headless = True

# Odkomentuj poniżej jeśli nie masz zainstalowanego Chrome'a
# driver = webdriver.Chrome( ChromeDriverManager().install(), options = options )
driver = webdriver.Chrome( options = options )
driver.get("https://python.org")
driver.maximize_window()
# searchInput = driver.find_element(By.XPATH, "/html/body/div/header/div/div[1]/div/form/fieldset/input")
searchInput = driver.find_element(By.ID, "id-search-field")
# searchInput = driver.find_element_by_xpath('//*[@id="id-search-field"]') # To już nie zadziała w Selenium_v4
searchInput.send_keys("django")

buttonSubmit = driver.find_element(By.ID, "submit")
buttonSubmit.click()
driver.save_screenshot("python.org.1.png")
driver.find_element(By.TAG_NAME, "body").screenshot("python.org.2.png")

# Za pomocą selenium wywołuje kod JavaSript z poziomu Pythona
func = lambda arg: driver.execute_script("return document.body.parentNode.scroll"+arg)
driver.set_window_size( func("Width"), func("Height") )
driver.find_element(By.TAG_NAME, "body").screenshot("python.org.3.png")

time.sleep(10)
driver.quit()