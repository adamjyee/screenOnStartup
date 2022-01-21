# used https://diyrobocars.com/2017/11/27/displaying-your-raspberry-pi-ip-address-on-bootup/
# https://ubuntu.com/tutorials/gpio-on-raspberry-pi#3-basic-gpio-example
import os, socket, fcntl, struct, time, lgpio

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
    s.fileno(),
    0x8915, # SIOCGIFADDR
    struct.pack('256s', ifname[:15])
    )[20:24])


def printIP():
    print("Wifi: ", get_ip_address('wlan0'))
    print("Ethernet: ", get_ip_address('eth0'))

def GPIO():
    pass