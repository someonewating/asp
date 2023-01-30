import wiringpi
from wiringpi import GPIO

blue = 0
green = 2
red = 3

wiringpi.wiringPiSetup()
wiringpi.pinMode(0, GPIO.OUTPUT)
wiringpi.pinMode(2, GPIO.OUTPUT)
wiringpi.pinMode(3, GPIO.OUTPUT)

def sick_off():
    wiringpi.digitalWrite(red, GPIO.LOW)

def sick():
    wiringpi.digitalWrite(red, GPIO.HIGH)

def track():
    wiringpi.digitalWrite(blue, GPIO.HIGH)

def track_off():
    wiringpi.digitalWrite(blue, GPIO.LOW)
