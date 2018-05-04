#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

# Script con una función que muestra por la pantalla LCD la dirección
# ip pública del equipo/dispositivo que ejecuta el script

# Resolviendo dependencias en Debian y Raspbian:
# sudo apt install geoip-bin python-geoip python-geoip2 python3-geoip

##############################
##    Importar Librerías    ##
##############################

##############################
##         Variables        ##
##############################

import urllib3  # Librería para obtener web
import commands  # Usado para obtener información del país
import LCD_LIB_16x2 as LCD
import RPi.GPIO as GPIO  # Importar librería para controlar hardware GPIO

# Función para obtener IP
def getIp():
    # Variable donde guardar la dirección IP
    ip = ''

    # Añadir web html a variable
    web = urllib3.urlopen('http://checkip.dyndns.org').read()

    # Recorrer html descargado en busca de números que conforman la ip
    for line in str(web):
        # Extraer números y puntos separadores
        if line in str(range(10)) + '.':
            ip += line

    print ('La ip es → ' + ip.strip())
    return str(ip.strip())

#Función para obtener País
def getPais(IP):
    # Extraer cadena con el pais
    pais = commands.getoutput("geoiplookup " + str(IP))

    # Limpiar País
    pais = pais.split('\n')[0].split(': ')[1]

    # Si no está instalado el programa "geoiplookup"
    if pais == "sh: geoiplookup: not found":
        print("Necesitas instalar geoiplookup para poder continuar")
        pais = ''
    #Cuando ocurre un error o extrae cadena no válida
    elif len(str(pais)) > 200:
        print("No ha sido posible conseguir el país para la IP → " + str(IP))
        pais = ''

    # Devuelve el país o la cadena vacía
    print('El país es → ' + pais)
    return pais

def mostrar():
    # Inicializar Pantalla
    LCD.lcd_init()

    # Obtener datos
    ip = getIp()
    pais = getPais(ip)

    # Enviando mensaje a cada línea
    LCD.lcd_string(ip, LCD.LINE_1)
    LCD.lcd_string(pais, LCD.LINE_2)

# Llamada a la función mostrar()
mostrar()
