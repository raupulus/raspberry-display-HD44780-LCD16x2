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

##############################
##    Importar Librerías    ##
##############################

##############################
##         Variables        ##
##############################

import urllib2  # Librería para obtener web

# Función para obtener IP
def getIp():
    # Variable donde guardar la dirección IP
    ip = ''

    # Añadir web html a variable
    web = urllib2.urlopen('http://checkip.dyndns.org').read()

    # Recorrer html descargado en busca de números que conforman la ip
    for line in str(web):
        # Extraer números y puntos separadores
        if line in str(range(10)) + '.':
            ip += line

    print ('La ip es → ' + ip.strip())
    return ip.strip()

