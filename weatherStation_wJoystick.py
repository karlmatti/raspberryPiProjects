from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

e = (0, 0, 0)
w = (255, 255, 255)

sense.clear()
while True:
  sense.show_message("^ Temperatuur > Ohurohk < Ohuniiskus")
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
          
      # Check which direction
      if event.direction == "up":
          temp = str(round(sense.temp, 2)
          sense.show_message(“Temperatuur: “ + temp)
      elif event.direction == "right":
          rohk = str(round(sense.get_pressure(), 2))
          sense.show_message("Ohurohk: " + rohk)
      elif event.direction == "left":
          niiskus = str(round(sense.get_humidity(), 2))
          sense.show_message("Ohuniiskus: " + niiskus)
  
