import Jetson.GPIO as GPIO
import time

button = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN)


while True:
    # if not GPIO.input(button):
    #     print("TEST_1")
    # else:
    #     print("TEST_2")
    print(GPIO.input(button))
    time.sleep(1)
