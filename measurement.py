from fastapi import FastAPI
import re


class Measurement:
    def measure(self):
        device = "/sys/bus/w1/devices/28-3c01f0952927/w1_slave"
        with open(device) as f:
            lines = f.readlines()
            line = lines[1]
            pattern = re.compile(r"t=\d+")
            matched_text = pattern.search(line)
            text = matched_text.group()
            stliped = text.replace('t=', '')
            result = float(stliped) / 1000
        return result
