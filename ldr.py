import RPi.GPIO as GPIO
from gpiozero import MCP3008
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
pwm = GPIO.PWM(21, 100)

print("\nVajuta Ctrl+C et väljuda \n")
pwm.start(0)
divider = MCP3008(0)
try:
    while True:
        print(int(divider.value * 100))
        pwm.ChangeDutyCycle(int(divider.value * 100))
        sleep(0.2)
except KeyboardInterrupt:
    print("Ctrl+C vajutatud - väljun programmist")
pwm.stop()
GPIO.cleanup()
