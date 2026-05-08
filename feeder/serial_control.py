import serial
import time

arduino = serial.Serial('COM3', 9600)

time.sleep(2)

def feed_dog():

    arduino.write(b"FEED\n")

    response = arduino.readline().decode().strip()

    return response