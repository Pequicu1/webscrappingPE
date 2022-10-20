#
# --------------------------------
#
# @author Ivan Lopez
# @version 1.0 20/10/2022
#
#
# Alba y Javi os quiero mucho un besito
# --------------------------------
#


import datetime
from readline import append_history_file
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

#espera a que el test termine[DONE]

espera2 = WebDriverWait(driver, 10000)
fin = espera2.until(EC.visibility_of_element_located((By.CLASS_NAME, "done")))

#recoger datos[DONE]

total_score = driver.find_element(By.ID, "result-summary").text
total_score = total_score.split("\n")

scores = [total_score[0]]

items = driver.find_element(By.ID, "results").text


#organizar resultados[DONE]

titulos = ['3d-cube-SP', '3d-raytrace-SP', 'acorn-wtb', 'ai-astar', 'Air', 'async-fs', 'Babylon', 'babylon-wtb', 'base64-SP', 'Basic', 'bomb-workers', 'Box2D', 'cdjs', 'chai-wtb', 'coffeescript-wtb', 'crypto', 'crypto-aes-SP', 'crypto-md5-SP', 'crypto-sha1-SP', 'date-format-tofte-SP', 'date-format-xparb-SP', 'delta-blue', 'earley-boyer', 'espree-wtb', 'first-inspector-code-load', 'FlightPlanner', 'float-mm.c', 'gaussian-blur', 'gbemu', 'gcc-loops-wasm', 'hash-map', 'HashSet-wasm', 'jshint-wtb', 'json-parse-inspector', 'json-stringify-inspector', 'lebab-wtb', 'mandreel', 'ML', 'multi-inspector-code-load', 'n-body-SP', 'navier-stokes', 'octane-code-load', 'octane-zlib', 'OfflineAssembler', 'pdfjs', 'prepack-wtb', 'quicksort-wasm', 'raytrace', 'regex-dna-SP', 'regexp', 'richards', 'richards-wasm', 'segmentation', 'splay', 'stanford-crypto-aes', 'stanford-crypto-pbkdf2', 'stanford-crypto-sha256', 'string-unpack-code-SP', 'tagcloud-SP', 'tsf-wasm', 'typescript', 'uglify-js-wtb', 'UniPoker', 'WSL']

data_into_list = items.split("\n")

i = 0
while( i < len(data_into_list)):
    if data_into_list[i] in titulos:
            scores.append(data_into_list[i + 1])
    i = i + 1

# crea fichero con la hora actual [DONE]
date = datetime.datetime.now()

file_name = ('RES_PE_%s' %(date))

with open(file_name,'w') as f:
    
    f.write(scores.pop(0))

    for i in scores:
        f.write('\n')
        f.write(i)

#Cierra pagina[DONE]
driver.quit()