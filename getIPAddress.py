# used https://diyrobocars.com/2017/11/27/displaying-your-raspberry-pi-ip-address-on-bootup/
# https://ubuntu.com/tutorials/gpio-on-raspberry-pi#3-basic-gpio-example
# used https://roboindia.com/tutorials/raspberry-seven-segment/

import os, socket, fcntl, struct, time, sys, digitLibrary
import lgpio as GPIO

GPIO.setmode(GPIO.BOARD)

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
    s.fileno(),
    0x8915, # SIOCGIFADDR
    struct.pack('256s', ifname[:15])
    )[20:24])

# self explanatory function - outputs ip
# need to find a way to use this to output ip on screen
def printIP():
    print("Wifi: ", get_ip_address('wlan0'))
    print("Ethernet: ", get_ip_address('eth0'))

def setupPins():
    #setup output pins
    GPIO.setup(35, GPIO.OUT)      //GPIO19
    GPIO.setup(12, GPIO.OUT)      //GPIO18
    GPIO.setup(36, GPIO.OUT)      //GPIO16
    GPIO.setup(33, GPIO.OUT)      //GPIO13
    GPIO.setup(32, GPIO.OUT)      //GPIO12
    GPIO.setup(38, GPIO.OUT)      //GPIO20
    GPIO.setup(40, GPIO.OUT)      //GPIO21

def pinList():
    return([35,12,36,33,32,38,40])

# clears display
def clearWriteDisplay(digit):
    gpin = pinList()
    for x in range (0,7):
        GPIO.output(gpin[x], digitLibrary.digits("clr")[x])
        for i in range (0,7):
            GPIO.output(gpin[x], digitLibrary.digits(digit)[x])


def GPIO():
    #describes pins to output to
    pin = 0

    h = GPIO.gpiochip_open(0)
    GPIO.gpio_claim_output(h, pin)

    try:
        while True:
            # turn on gpio pin
            # the 1 is "on"
            GPIO.gpio_write(h, pin, 1)
            time.sleep(1)

            # turn the gpio pin off
            # the 0 is "off"
            GPIO.gpio_write(h, pin, 0)
            time.sleep(1)

    #runs until interrupted by keyboard press
    except KeyboardInterrupt:
        GPIO.gpio_write(h, pin, 0)
        GPIO.gpiochip_close(h)

