
import lcddriver
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

display = lcddriver.lcd()

TRIG = 23 
ECHO = 24

print ("Distance Measurement In Progress")
display.lcd_display_string("Distance :", 1)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
try:
    while True:

        GPIO.output(TRIG, False)
        print ("Waiting For Sensor To Settle")
        
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(ECHO)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        result = str(distance)+" cm"
        display.lcd_display_string(result,2);

except KeyboardInterrupt: 
    print("Cleaning up!")
    GPIO.cleanup()
