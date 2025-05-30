from machine import Pin
import utime

pir = Pin(15, Pin.IN, Pin.PULL_DOWN)
led = Pin(2, Pin.OUT)

# Variable para activar el parpadeo permanente una vez detectado un objeto
activar_parpadeo = False

while True:
    if not activar_parpadeo:
        estado = pir.value()
        print(estado)
        utime.sleep_ms(500)

        if estado == 0:
            print("No detecta Objeto")
            led.value(0)
        else:
            print("Objeto a 30 cm")
            activar_parpadeo = True  # Una vez detectado, activa parpadeo infinito
    else:
        # Parpadeo infinito
        led.value(1)
        utime.sleep_ms(500)
        led.value(0)
        utime.sleep_ms(500)
