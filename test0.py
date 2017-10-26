#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

# El objetivo de este script de pruebas es crear un bucle con mensajes sencillos
# Ejecutando este script podemos saber si la parte de hardware está correctamente conectada

##############################
##    Importar Librerías    ##
##############################
import time  # Importamos la libreria time --> time.sleep
import LCD_LIB_16x2 as LCD
import RPi.GPIO as GPIO  # Importar librería para controlar hardware GPIO

##############################
##         Variables        ##
##############################


# Inicializar Pantalla
LCD.lcd_init()

while True:
    # Enviando mensaje a cada línea
    LCD.lcd_string("  Rasbperry Pi ",LCD.LINE_1)
    LCD.lcd_string("16x2 LCD Pruebas",LCD.LINE_2)

    time.sleep(3) # 3 segundos delay

    # Enviando mensaje a cada línea
    LCD.lcd_string("1234567890123456",LCD.LINE_1)
    LCD.lcd_string("abcdefghijklmnop",LCD.LINE_2)

    time.sleep(3) # 3 segundos delay

    # Enviando mensaje a cada línea
    LCD.lcd_string("    Fryntiz ",LCD.LINE_1)
    LCD.lcd_string(" www.fryntiz.es ",LCD.LINE_2)

    time.sleep(10)
GPIO.cleanup()
