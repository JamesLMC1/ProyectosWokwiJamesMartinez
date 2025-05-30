from machine import Pin
from hcsr04 import HCSR04
from time import sleep

medidor = HCSR04(trigger_pin=5, echo_pin=18)
led = Pin(2, Pin.OUT)

while True:
    try:
        distancia = medidor.distance_cm()
        print("Distancia es =", distancia, "cm")

        if distancia >= 30:
            led.value(1)
            print("Encendido en Alerta")
        else:
            led.value(0)
            print("No hay nadie, todo good")

        sleep(2)

    except Exception as e:
        print("Error, no hay señal:", e)
        print("Algo anda mal")