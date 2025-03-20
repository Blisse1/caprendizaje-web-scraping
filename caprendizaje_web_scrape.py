import time, os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from dotenv import load_dotenv
load_dotenv()

options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

def find_element_and_click(selector, name):
    element = driver.find_element(selector, name)
    element.click()

def login_to_caprendizaje():
    response = driver.get(os.getenv("CAPRENDIZAJE_URL_WEB"))
    try:
        find_element_and_click(By.ID, "aprendices")
        user_input = driver.find_element(By.ID, "tbLoginUsuario")
        user_input.send_keys(os.getenv("CAPRENDIZAJE_USER"))
        password_input = driver.find_element(By.ID, "__tbPasswordUsuario")
        password_input.send_keys(os.getenv("CAPRENDIZAJE_PASSWORD"))
        find_element_and_click(By.ID, "ini_session_aprendiz")
        print("Logueo Exitoso")
    except:
        print("Logueo Fallido")

def clear_announcement():
    announcement_element = driver.find_element(By.ID, "modalImagen")
    announcement_element.send_keys(Keys.ESCAPE)
    print("Anuncio Quitado")

# Filtro para la ciudad de Bogotá
def cities_filter():
    actions = [
        (By.ID, "sel_departamento"),
        (By.CSS_SELECTOR, "#sel_departamento > option:nth-child(6)"),
        (By.ID, "sel_ciudad"),
        (By.CSS_SELECTOR, "#sel_ciudad > option:nth-child(2)"),
        (By.ID, "btn_buscar_solicitud")
    ]

    for selector, element in actions:
        find_element_and_click(selector, element)

    print("Ciudades Filtradas")

def get_empresas():
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    siguiente_button = soup.find("button", id="btn_pagina_siguiente")

    lista_nombre_empresas = []

    while(siguiente_button["style"] == "display: initial;"):
        time.sleep(3) # esperar 3 segundos a que cargue el contenido

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        nombres_empresas = soup.find_all("label", class_="aprendizLabelTituloSolicitudesBA") 

        for empresa in nombres_empresas:
            lista_nombre_empresas.append(empresa.get_text())
        siguiente_button = soup.find("button", id="btn_pagina_siguiente") # actualiza la variable siguiente_button de acuerdo al parseo

        if(siguiente_button["style"] == "display: none;"):
            break
        find_element_and_click(By.ID, "btn_pagina_siguiente")

    with open("empresas.txt", "w+") as f:
        f.writelines([i + "\n" for i in lista_nombre_empresas])

print("Sacando empresas... esto puede demorar unos segundos")
login_to_caprendizaje()
time.sleep(3)
clear_announcement()
find_element_and_click(By.ID, "enlace3") # seccion empresas
time.sleep(3)
cities_filter()
time.sleep(3)

get_empresas()
print("Empresas Listas. Revise su archivo local empresas.txt")
