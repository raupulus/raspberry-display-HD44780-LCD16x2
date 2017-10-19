# raspberry_LCD16x2
Pequeña librería para el modelo 1602 chip HD44780 con el que trabajar más fácil

Mediante los GPIO podemos trabajar de una forma muy sencilla con nuestra raspberry PI, con este script se pretende facilitar el uso de este tipo de pantallas y/o hacer que este funcionando desde el mismo momento en el cual se conecta. También tiene como objetivo servir de apoyo para ser integrado en otros proyectos más ambiciosos como mostrar mensajes de twitter por dicha LCD.

## Dependencias (Solo probado en Raspbian stable)
```Raspbian
sudo apt install -y raspi-gpio python3-rpi.gpio python3-pigpio python3-gpiozero python-rpi.gpio python-pigpio python-gpiozero pigpio
```
