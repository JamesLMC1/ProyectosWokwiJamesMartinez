from machine import Pin
from time import sleep

# Configuración de los pines
verde_pin = Pin(2, Pin.OUT)
amarillo_pin = Pin(4, Pin.OUT)
rojo_pin = Pin(5, Pin.OUT)

# Función para encender el semáforo
while True:
    # Luz roja
    rojo_pin.value(1)
    print('Pare')
    sleep(2)
    rojo_pin.value(0)
    print('Deténgase')
    
    # Luz amarilla
    amarillo_pin.value(1)
    print('Baje la velocidad')
    sleep(2)
    amarillo_pin.value(0)
    print('Alístese')
    
    # Luz verde
    verde_pin.value(1)
    print('Arranque')
    sleep(2)
    verde_pin.value(0)
    print('Acelere')