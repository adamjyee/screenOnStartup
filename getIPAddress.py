# used https://diyrobocars.com/2017/11/27/displaying-your-raspberry-pi-ip-address-on-bootup/
# https://ubuntu.com/tutorials/gpio-on-raspberry-pi#3-basic-gpio-example

# lgpio returns an error on anything other than linux because it's a linux library
# 
import os, socket, fcntl, struct, time, lgpio


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

def GPIO():
    #describes pins to output to
    pin = 0

    h = lgpio.gpiochip_open(0)
    lgpio.gpio_claim_output(h, pin)

    try:
        while True:
            # turn on gpio pin
            # the 1 is "on"
            lgpio.gpio_write(h, pin, 1)
            time.sleep(1)

            # turn the gpio pin off
            # the 0 is "off"
            lgpio.gpio_write(h, pin, 0)
            time.sleep(1)

    #runs until interrupted by keyboard press
    except KeyboardInterrupt:
        lgpio.gpio_write(h, pin, 0)
        lgpio.gpiochip_close(h)

