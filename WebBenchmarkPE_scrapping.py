"""

from bs4 import BeautifulSoup
import requests

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
items = soup.find_all('div', class_="benchmark benchmark-done")

for test in items:
    title = items.find('h3', class_="benchmark-name")
    score = items.find('h4', class_="score")

    info = [title, score]
    print(info)

"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://browserbench.org/JetStream/index.html"
driver = webdriver.Chrome()

driver.get(url)

#espera al botón [DONE]

espera = WebDriverWait(driver, 10000)
boton = espera.until(EC.visibility_of_element_located((By.CLASS_NAME, "button"))).click()

#espera a que el test termine

espera2 = WebDriverWait(driver, 10000)
fin = espera2.until(EC.visibility_of_element_located((By.CLASS_NAME, "done")))

#recoger datos 


total_score = driver.find_element(By.ID, "result-summary").text
print("EL TEST HA RESULTADO: \n")
print(total_score)

items = driver.find_element(By.ID, "results").text
print(items)

# for test in items:
#     title = driver.find_element(By.CLASS_NAME, "benchmark-name")
#     score = driver.find_element(By.CLASS_NAME, "score")

#     info = [title, score]
#     print(info)

driver.quit()




