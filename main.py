from time import sleep
import re


device = "/sys/bus/w1/devices/28-3c01f0952927/w1_slave"
while True:
    with open(device) as f:
        lines = f.readlines()
        print(lines)
