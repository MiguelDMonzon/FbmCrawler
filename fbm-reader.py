#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 11:38:37 2016

@author: migueld
"""
from lxml import html


def parse_string(unicode_string):
    
    string = str(unicode_string.encode("utf-8"))
    string = string.replace("\xc3\x82\xc2\xb4", "'")
    return string



jornadas = 7

csv_jornadas = open("jornadas.csv", "w")
csv_clasificaciones = open("clasificaciones.csv", "w")

csv_jornadas.write("local;visitante;resultado;dia;hora\n")
csv_clasificaciones.write("clasificacion;equipo;PJ;PG;PE;PP;PF;PC;Puntos;Racha\n")

for i in range(1, jornadas+1):
    
    html_source = open("Jornada"+str(i)+".html").read()
    tree = html.document_fromstring(html_source)
    
    print("ABRIENDO JORNADA "+str(i))
    

    a = tree.xpath("//table[@id='jornadaDataGrid']")
    partidos_jornada= a[0].getchildren()[0].getchildren()
    for j in range(0, len(partidos_jornada)):
        partido = partidos_jornada[j].getchildren()[0].getchildren()[0].text
        local = partido.split("-")[0]
        visitante = partido.split("-")[2]
        resultado = partidos_jornada[j].getchildren()[1].getchildren()[0].text
        dia = partidos_jornada[j].getchildren()[2].getchildren()[0].text
        hora = partidos_jornada[j].getchildren()[3].getchildren()[0].text
    
        output = parse_string(local) + ";" +\
             parse_string(visitante) + ";" +\
             parse_string(resultado) + ";" +\
             parse_string(dia) + ";" +\
             parse_string(hora) + "\n"
        print(output)
        csv_jornadas.write(output)
    
    
    a = tree.xpath("//table[@id='clasificacionDataGrid']")
    equipos = a[0].getchildren()[0].getchildren()
    
    # Recorrer las filas de la tabla de clasificación
    # La primera se omite ya que funciona de cabecera
    for k in range(1, len(equipos)):
        
        clasificacion = equipos[k].getchildren()[0].getchildren()[0].text
        equipo = equipos[k].getchildren()[1].getchildren()[0].text
        PJ = equipos[k].getchildren()[2].getchildren()[0].text
        PG = equipos[k].getchildren()[3].getchildren()[0].text
        PE = equipos[k].getchildren()[4].getchildren()[0].text
        PP = equipos[k].getchildren()[5].getchildren()[0].text
        PF = equipos[k].getchildren()[6].getchildren()[0].text
        PC = equipos[k].getchildren()[7].getchildren()[0].text
        puntos = equipos[k].getchildren()[8].getchildren()[0].text
        racha = equipos[k].getchildren()[9].getchildren()[0].text
    
        output = parse_string(clasificacion) + ";" + parse_string(equipo) + ";" +\
                parse_string(PJ) + ";" + parse_string(PG) + ";" +\
                parse_string(PE) +";" + parse_string(PP) + ";" +\
                parse_string(PF) + ";" +\
                parse_string(PC) + ";" + parse_string(puntos) + ";" +\
                parse_string(racha) + "\n"
    
        print(output)
        csv_clasificaciones.write(output)
        
        
        
        
        
        
        