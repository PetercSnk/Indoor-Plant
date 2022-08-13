import RPi.GPIO as GPIO
import time
import grovepi
import math

GPIO.setmode(GPIO.BOARD)

moisture_sensor = 0
temphum_sensor = 1
light_sensor = 2

def getSensor():
    moisture = grovepi.analogRead(moisture_sensor)
    temperature = grovepi.analogRead(temphum_sensor)
    light = grovepi.analogRead(light_sensor)

    b = 4275
    r0 = 100000
    r = 1023.0 / temperature - 1.0
    r = 100000.0 * r
    temperature = round(1.0 / (math.log(r/100000.0) / b + 1 / 298.15) - 273.15, 3)

    moisture = round(float(1 - (moisture - 500) / 250), 3)

    light = light

    print("temp: ", temperature)
    print("mois: ", moisture)
    print("light: ", light)

getSensor()