import RPi.GPIO as GPIO
from gpiozero import MCP3008
from Tkinder import *
master = Tk()


GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
pwm = GPIO.PWM(21, 100)

print("\nVajuta Ctrl+C et väljuda \n")
pwm.start(0)

w = Scale(master, from_=0, to=100,
  orient=HORIZONTAL, command=update)
def update(duty):
  pwm.ChangeDutyCycle(float(duty))
