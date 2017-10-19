#!/usr/bin/python
# -*- encoding: utf-8 -*-

#######################################
# ###     Raúl Caro Pastorino     ### #
## ##                             ## ##
### # https://github.com/fryntiz/ # ###
## ##                             ## ##
# ###       www.fryntiz.es        ### #
#######################################

##############################
##    Importar Librerías    ##
##############################
import time  # Importamos la libreria time --> time.sleep
import RPi.GPIO as GPIO  # Importar librería para controlar hardware GPIO

##############################
##         Variables        ##
##############################
# Definiendo los pines que serán usados
LCD_RS = 7
LCD_E = 17
LCD_D4 = 27
LCD_D5 = 22
LCD_D6 = 23
LCD_D7 = 24

# Carácteres por línea → 16
LCD_WIDTH = 16
LCD_CHR = True
LCD_CMD = False

LINE_1 = 0x80 # LCD dirección en la RAM para la primera línea
LINE_2 = 0xC0 # LCD dirección en la RAM para la segunda línea

# Constantes de tiempo para retraso y actualización
E_PULSE = 0.0005
E_DELAY = 0.0005

# Función para activar los pines GPIO de raspberry
def init_GPIO():
    GPIO.setmode(GPIO.BCM) # Use BCM GPIO numbers
    GPIO.setup(LCD_E, GPIO.OUT) # E
    GPIO.setup(LCD_RS, GPIO.OUT) # RS
    GPIO.setup(LCD_D4, GPIO.OUT) # DB4
    GPIO.setup(LCD_D5, GPIO.OUT) # DB5
    GPIO.setup(LCD_D6, GPIO.OUT) # DB6
    GPIO.setup(LCD_D7, GPIO.OUT) # DB7

# Inicializar pantalla LCD
def lcd_init():
    # Activa pines GPIO
    init_GPIO()

    lcd_byte(0x33,LCD_CMD) # 110011 Initialise
    lcd_byte(0x32,LCD_CMD) # 110010 Initialise
    lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
    lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
    lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
    lcd_byte(0x01,LCD_CMD) # 000001 Clear display
    time.sleep(E_DELAY)
