import RPi.GPIO as GPIO
import time
import grovepi
import math

GPIO.setmode(GPIO.BOARD)

moisture_sensor = 0
#temphum_sensor = 5
#light_sensor = 2
print("imports")

try:
    #def getSensor():
    #print("b4 temp hum")
    #[temp,hum] = grovepi.dht(temphum_sensor, 0)
    #print("temp =", temp, "C\thumidity =", hum,"%")
    #print("after temp hum")

    print("b4 analog read")
    moisture = grovepi.analogRead(moisture_sensor)
    time.sleep(.5)
    print(moisture)
    print("after analog read")
    #temperature = grovepi.analogRead(temphum_sensor)
    #light = grovepi.analogRead(light_sensor)

    #b = 4275
    #r0 = 100000
    #r = 1023.0 / temperature - 1.0
    #r = 100000.0 * r
    #temperature = round(1.0 / (math.log(r/100000.0) / b + 1 / 298.15) - 273.15, 3)

    #moisture = round(float(1 - (moisture - 500) / 250), 3)

    #light = light

    #print("temp: ", temperature)
    #print("mois: ", moisture)
    #print("light: ", light)

except IOError:
    print("Error")
#except KeyboardInterrupt:
    #exit()
except Exception as e:
    print(e)

#getSensor()
