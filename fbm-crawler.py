#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 10:05:12 2016

@author: migueld
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# Entrar en la página de la FBM
driver = webdriver.Firefox()
driver.get("http://competiciones.feb.es/autonomicas/Resultados.aspx?a=14")

# Ir a las categorías y buscar la categoría
elem = driver.find_element_by_id("controlNavegacion_categoriasDropDownList")
for i in range(0, 13):    
    elem.send_keys(Keys.ARROW_DOWN)
elem.send_keys(Keys.ENTER)

# Esperar un segundo
time.sleep(1)

# Ir a los grupos y buscar el grupo
elem = driver.find_element_by_id("gruposDropDownList")
elem.send_keys(Keys.ARROW_DOWN)
elem.send_keys(Keys.ENTER)

# Esperar 2 segundos
time.sleep(2)

# Ir a las jornadas, y obtener la jornada actual
elem = driver.find_element_by_id("jornadasDropDownList")
jornada = elem.find_element_by_xpath("option[@selected='selected']").text
num_jornada = int(jornada.split(" ")[1])
print(num_jornada)

# Desplazarse por el combobox de jornadas hasta la primera
for i in range(0, num_jornada):
    elem.send_keys(Keys.ARROW_UP)
elem.send_keys(Keys.ENTER)


# Para cada jornada, obtener el contenido y guardarlo
for i in range(1, 11):
    time.sleep(2)
    html_source = driver.page_source
    html_output = open("Jornada"+str(i)+".html", "w")
    html_output.write(html_source.encode("utf-8"))
    time.sleep(2)
    elem = driver.find_element_by_id("jornadasDropDownList")
    elem.send_keys(Keys.ARROW_DOWN)
    elem.send_keys(Keys.ENTER)

driver.close()