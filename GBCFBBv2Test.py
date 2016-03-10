import os
import time
clear = lambda: os.system('clear')
i2cdetect = lambda: os.system('i2cdetect -y -r 1')
writeEEP = lambda: os.system('./w.sh')
readEEP = lambda: os.system('./r.sh')


import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
from Adafruit_I2C import Adafruit_I2C

gpios = ["P9_11", "P9_13", "P9_14", "P9_16", "P9_24", "P9_25", "P9_26", "P9_27"]
ains = ["AIN0", "AIN1", "AIN2", "AIN3",]
#Digital output 
clear()
print "\n========    Grove Base Cape for Beaglebone v2 Test program    ========\n"
print "1. GPIO OUTPUT TEST\n"
print "    Please test all the IOs which have gpio function"
print "\n    All the Digital pins are set to High.\n"

for io in gpios:
    GPIO.setup(io, GPIO.OUT)
    GPIO.output(io, GPIO.HIGH)
raw_input("Press Enter to next step.")

print "\n    All the Digital pins are set to LOW.\n"
for	io in gpios:
    GPIO.output(io, GPIO.LOW)
raw_input("Press Enter to next step.")

#Digital input 
try:
    while True:
        clear()
        print "\n========    Grove Base Cape for Beaglebone v2 Test program    ========\n"
        print "2. GPIO INPUT TEST\n"
        print "    Please test all the IOs which have gpio function"
        print "\n    All the Digital pins are set to Input.\n"
        inputs = []
        for io in gpios:
            GPIO.setup(io, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
            if GPIO.input(io):
                inputs.append("HIGH ")
            else:
                inputs.append(" LOW ")
        print gpios
        print inputs
        print "\nPress Ctrl+C to next step.\n"
        time.sleep(0.5)
        
except KeyboardInterrupt:
    clear()
    
#Analog input
try:
    ADC.setup()
    while True:
        clear()
        print "\n========    Grove Base Cape for Beaglebone v2 Test program    ========\n"
        print "3. ANALOG INPUT TEST\n"
        print "    Please test all the analog inputs "
        print "\n    See the input values below.\n"
        inputs = []
        for ain in ains:
            inputs.append(ADC.read(ain))
        print ains
        for v in inputs:
            print "  %2.3f" % v ,
        print "\n\nPress Ctrl+C to next step.\n"
        time.sleep(0.5)
        
except KeyboardInterrupt:
    clear()

#i2cdetect 
try:
    while True:
        clear()
        print "\n========    Grove Base Cape for Beaglebone v2 Test program    ========\n"
        print "4. I2C detect \n"
        print "    Please put several i2c groves to the I2C_2 ports "
        print "\n    See if beaglebone can detect the pluged in devices.\n"
        i2cdetect()
        print "\nPress Ctrl+C to next step.\n"
        time.sleep(1)
        
except KeyboardInterrupt:
    clear()

#Write eeprom
print "\n========    Grove Base Cape for Beaglebone v2 Test program    ========\n"
print "5. Cape EEPROM program\n"
print "    Please short the jumper(it's DNP) to disable eeprom write protection\n    and set the SW2 dip switch to 11\n"
raw_input("Press Enter to start write cape info to eeprom.")
print "\n Write data: \n"
print "?U3?A1Grove Base Cape for BeagleBone00A2SeeedstudioBB-GREEN-GROVE00103030035\n"
writeEEP()

print "\n Read data: \n"
readEEP()

print "done!!\n"
