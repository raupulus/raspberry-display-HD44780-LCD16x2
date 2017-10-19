#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

# El objetivo de este script de pruebas es que se pida al usuario que línea cambiar y la cadena

##############################
##    Importar Librerías    ##
##############################

import LCD_LIB_16x2 as LCD

##############################
##         Variables        ##
##############################

def mostrar_opciones():
    print('''
        1) Cambiar línea 1 de la pantalla LCD
        2) Cambiar línea 2 de la pantalla LCD
        0) Salir del script
    ''')
