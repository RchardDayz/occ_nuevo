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
url = "https://www.occ.com.mx/empleos/"
driver.get(url)
sleep(5)

#Se extrae el total de anuncios
Total_anuncios = driver.find_element(By.XPATH, '//p[@class="text-0-2-82 small-0-2-90 midEmphasis-0-2-104"]').text
print("Total de Anuncios en México: " + (Total_anuncios))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)

#Se establece el total de paguinas
total_paguinas = driver.find_element(By.CSS_SELECTOR, "li.li-0-2-625:nth-child(4)").text
print("Total de paguinas: " + str(total_paguinas))

#Se establece el total de anuncios en la paguina
anuncios = driver.find_elements(By.XPATH, '//*[starts-with(@id,"jobcard")]')
print("Anuncios encontrados: " + str(len(anuncios)))
sleep(5)

detetctor_linea = 0
gatillo = 0
while gatillo < 3:
    gatillo +=1

    for anuncio in anuncios:
        try:
            fecha = anuncio.find_element(By.CLASS_NAME, 'date-0-2-568').text
            print('Fecha: ' + str(fecha))
        except:
            pass
        try:
            puesto = anuncio.find_element(By.CLASS_NAME, 'longWord-0-2-576').text
            print('Puesto: ' + str(puesto))
        except Exception as err:
            print(err)

        try:
            empresa = anuncio.find_element(By.CLASS_NAME, "fresnel-greaterThanOrEqual-sm").text
            print("EMPRESA: " + str(empresa))
        except:
            print('EMPRESA: ', 'Empresa Confidencial')

        try:
            sueldo = anuncio.find_element(By.CLASS_NAME, "salary-0-2-568").text
            print("SUELDO: " + str(sueldo))
        except Exception as err:
            print(err)


        try:
            ciudad = anuncio.find_element(By.CLASS_NAME, "zonesLinks-0-2-602").text
            print("CIUDAD: " + str(ciudad))
        except:
            pass

        try:
            url_busqueda = anuncio.find_element(By.CLASS_NAME, 'jobcard-0-2-559').get_attribute('href')
            print("URL_BUSQUEDA: " + str(url_busqueda))
        except:
            pass

    # Aqui busco la interacción de las paguinas
    try:
        div = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "flex-0-2-4")))
        ul = WebDriverWait(div, 20).until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
        li_boton2 = WebDriverWait(ul, 20).until(EC.presence_of_element_located((By.XPATH, "//li[@class='btn-0-2-618 next-0-2-620'][@tabindex='0']")))
        svg_boton2 = WebDriverWait(li_boton2, 20).until(EC.presence_of_element_located((By.TAG_NAME, "svg"))).click()
        sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(5)  # espera 5 segundos para que cargue la página siguiente
    except NoSuchElementException:
        print("No se encontró el botón 2")
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





