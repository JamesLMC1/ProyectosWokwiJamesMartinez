from machine import Pin
import time

led = Pin(12, Pin.OUT)
led.on()
time.sleep(10)
led.off()
