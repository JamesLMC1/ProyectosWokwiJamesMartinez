from machine import Pin, I2C
from ssd1306 import SSD1306_I2C 
import time

# Tamaño del display OLED
ancho = 128
alto = 64

# Inicialización del bus I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

# Inicialización del display OLED
oled = SSD1306_I2C(ancho, alto, i2c)

# Mostrar el mensaje "Hola mundo"
oled.fill(0)  # Limpiar la pantalla

# Mostrar texto en diferentes líneas
 

oled.text("_________________", 0, 2) 
oled.text("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣", 0, 2)  
oled.text("Hola ", 34, 16) 
oled.text("chicos", 25, 26)   
oled.text("de las 2", 12, 36) 

oled.text("_________________", 0, 52) 
oled.text("♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣", 0, 52)   
 

oled.show()
time.sleep(19)

