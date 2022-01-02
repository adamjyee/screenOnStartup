#used https://diyrobocars.com/2017/11/27/displaying-your-raspberry-pi-ip-address-on-bootup/
import os
import socket
import fcntl
import struct

def get_ip_address(ifname):
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 return socket.inet_ntoa(fcntl.ioctl(
 s.fileno(),
 0x8915, # SIOCGIFADDR
 struct.pack('256s', ifname[:15])
 )[20:24])

print("Wifi: ", get_ip_address('wlan0'))
print("Ethernet: ", get_ip_address('eth0'))