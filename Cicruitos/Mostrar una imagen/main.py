from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import time
import uos

# Configuración del display OLED
ANCHO = 128
ALTO = 64

# Inicialización I2C
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ANCHO, ALTO, i2c)

def cargar_imagen_desde_archivo(ruta_archivo):
    try:
        # Leer el contenido del archivo
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
        
        # Convertir el texto a bytearray
        # Asumimos que el formato es: 0x00, 0x01, 0xFF,... etc.
        bytes_str = contenido.split(',')
        datos = bytearray()
        
        for byte_str in bytes_str:
            byte_str = byte_str.strip()
            if byte_str.startswith('0x'):
                datos.append(int(byte_str, 16))
        
        return datos
    except Exception as e:
        print("Error al cargar imagen:", e)
        return bytearray([0x00] * (ANCHO * ALTO // 8))  # Devuelve pantalla en blanco

def mostrar_imagen(ruta_archivo):
    # Cargar datos de la imagen
    imagen_data = cargar_imagen_desde_archivo(ruta_archivo)
    
    # Crear FrameBuffer
    imagen = framebuf.FrameBuffer(imagen_data, ANCHO, ALTO, framebuf.MONO_HLSB)
    
    # Mostrar en pantalla
    oled.fill(0)
    oled.blit(imagen, 0, 0)
    oled.show()
    print("Imagen mostrada correctamente")

# Ruta al archivo con los datos de la imagen
ARCHIVO_IMAGEN = "txt.txt"

# Mostrar la imagen
mostrar_imagen(ARCHIVO_IMAGEN)

# Mantener la imagen visible
while True:
    time.sleep(1)