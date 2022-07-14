from time import sleep
import re


device = "/sys/bus/w1/devices/28-3c01f0952927/w1_slave"
while True:
    with open(device) as f:
        lines = f.readlines()
        line = lines[1]
        pattern = re.compile(r"t=\d+")
        matched_text = pattern.search(line)
        text = matched_text.group()
        stliped = text.replace('t=', '')
        result = float(stliped) / 1000
        print(result)
