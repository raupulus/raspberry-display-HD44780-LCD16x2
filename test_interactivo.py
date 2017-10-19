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
import RPi.GPIO as GPIO  # Importar librería para controlar hardware GPIO


##############################
##         Variables        ##
##############################

def mostrar_opciones():
    print('''
        1) Cambiar línea 1 de la pantalla LCD
        2) Cambiar línea 2 de la pantalla LCD
        3) Limpiar pantalla LCD
        0) Salir del script
    ''')


# Iniciar LCD
LCD.lcd_init()


while True:
    # Mostrar Menú con las Opciones
    mostrar_opciones()

    # Permite elegir opción
    opcion = raw_input('Opción → ')

    # Comprobar la opción elegida
    if (opcion == str(1)):
        print('Introduce el nuevo valor para la línea 1')
        tmp = raw_input('Cadena → ')
        LCD.lcd_string(tmp, LCD.LINE_1)
    elif (opcion == str(2)):
        print('Introduce el nuevo valor para la línea 2')
        tmp = raw_input('Cadena → ')
        LCD.lcd_string(tmp, LCD.LINE_2)
    elif (opcion == str(3)):
        LCD.lcd_string('', LCD.LINE_1)
        LCD.lcd_string('', LCD.LINE_2)
    elif (opcion == str(0)):
        print('Limpiando y Cerrando Script')
        GPIO.cleanup()
        break
    else:
        print('Opción no válida')
