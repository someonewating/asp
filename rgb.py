import sys
import wiringpi
from wiringpi import GPIO

blue = 0
green = 2
red = 3

wiringpi.wiringPiSetup()
wiringpi.pinMode(0, GPIO.OUTPUT)
wiringpi.pinMode(2, GPIO.OUTPUT)
wiringpi.pinMode(3, GPIO.OUTPUT)

while True:
    try:   
        print("blue")
        wiringpi.digitalWrite(blue, GPIO.HIGH)
        wiringpi.delay(1000)
        wiringpi.digitalWrite(blue, GPIO.LOW)
        
        print("green")
        wiringpi.digitalWrite(green, GPIO.HIGH)
        wiringpi.delay(1000)
        wiringpi.digitalWrite(green, GPIO.LOW)
        
        print("red")
        wiringpi.digitalWrite(red, GPIO.HIGH)
        wiringpi.delay(1000)
        wiringpi.digitalWrite(red, GPIO.LOW)

    except KeyboardInterrupt:
        wiringpi.digitalWrite(blue, GPIO.LOW)
        wiringpi.digitalWrite(green, GPIO.LOW)
        wiringpi.digitalWrite(red, GPIO.LOW)
        print("\n exit")
        sys.exit(0)