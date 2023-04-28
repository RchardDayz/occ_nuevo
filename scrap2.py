#IMPORTANDO LIBRERIAS
from csv import DictWriter
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import random
from datetime import date
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


#LIMPIANDO PANTALLA
os.system("cls")
#os.system("del occtest.csv")

# DEFINIENDO OPCIONES DE NAVEGADOR
options = webdriver.FirefoxOptions()

#Esta instruccione s para que minimice la ventana del explorador
# options.add_argument('--headless')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

# CREAR NAVEGADOR ROBOT ABRIENDO FIREFOX
driver = webdriver.Firefox(executable_path="geckodriver", options=options)
driver.delete_all_cookies()

#Se establece la url
url = "https://www.occ.com.mx/empleos/?page=1"
driver.get(url)
sleep(5)

contador_paguina= 1

#Se extrae el total de anuncios
Total_anuncios = driver.find_element(By.XPATH, '//p[@class="text-0-2-82 small-0-2-90 midEmphasis-0-2-104"]').text
print("Total de Anuncios en México: " + (Total_anuncios))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)

#Se establece el total de paguinas
total_paguinas = driver.find_element(By.XPATH, '//li[@class="li-0-2-627"]').text
print("Total de paguinas: " + str(total_paguinas))

#Se establece el total de anuncios en la paguina
anuncios = driver.find_elements(By.XPATH, '//*[starts-with(@id,"jobcard")]')
print("Anuncios encontrados: " + str(len(anuncios)))
sleep(5)

numero_random = random.randint(5, 20)

detetctor_linea = 0
gatillo = 0
while gatillo < 2:
    gatillo +=1
    contador_paguina +=1

    for anuncio in anuncios:
        
        fecha = ''
        try:
            fecha = WebDriverWait(anuncio, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'date-0-2-570'))).text
            print('Fecha: ' + str(fecha))
        except Exception as err:
            print(err)
            break
            
        puesto = ''
        try:
            puesto =  WebDriverWait(anuncio, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'longWord-0-2-578'))).text
            print('Puesto: ' + str(puesto))
        except Exception as err:
            print(err)
            break

        empresa = ''
        try:
            empresa = WebDriverWait(anuncio, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "fresnel-greaterThanOrEqual-sm"))).text
            print("EMPRESA: " + str(empresa))
        except:
            print('EMPRESA: ', 'Empresa Confidencial')

        sueldo = ''
        try:
            sueldo =  WebDriverWait(anuncio, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "salary-0-2-562"))).text
            print("SUELDO: " + str(sueldo))
        except Exception as err:
            print(err)
            break

        ciudad = ''
        try:
            ciudad =  WebDriverWait(anuncio, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "zonesLinks-0-2-604"))).text
            print("CIUDAD: " + str(ciudad))
        except Exception as err:
            print(err)
            break

        url_busqueda = ''
        try:
            url_busqueda =  WebDriverWait(anuncio, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'jobcard-0-2-561'))).get_attribute('href')
            print("URL_BUSQUEDA: " + str(url_busqueda))
        except Exception as err:
            print(err)
            break

    # Aqui busco la iteracción de las paguinas
    try:
        paguina_nueva= str(url).replace("?page=1", "?page=" + str(contador_paguina))
        print(paguina_nueva)
        driver.get(paguina_nueva)
        sleep(numero_random)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(numero_random)
    except Exception as err:
        print(err)
        break
      

print("Raspado terminado")

'''
este es el codigo para extraer informacion adentro de los anuncios

despues de la variabel anuncios voy a poner la siguiente linea de codigo
este bucle for lo tendria que poner despues del cogo para extraer la url del anuncio

links = []
for link in url_busqueda:
    comentarios = link.find_element(By.CLASS_NAME, 'la etiqueta de los comentarios').text
    links.append(comentarios)

print('comentarios: ', comentarios)

'''





