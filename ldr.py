import RPI.GPIO as GPIO
import time
from gpiozero import MCP3008

GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
pwm = GPIO.PWM(21, 100)

print("\nPress Ctrl+C to quit \n")
dc = 0
pwm.start(dc)
divider = MCP3008(0)

try:
    while True:
        print(int(divider.value * 100))
        pwm.ChangeDutyCycle(int(divider.value * 100))
except KeyboardInterrupt:
    print("Ctrl+C pressed - ending program")

pwm.stop()
GPIO.cleanup()