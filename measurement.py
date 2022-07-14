from fastapi import FastAPI
import re


class Measurement:
    def __init__(self) -> None:
        self.device = "/sys/bus/w1/devices/28-3c01f0952927/w1_slave"

    def measure(self):
        with open(self.device) as f:
            lines = f.readlines()
            stliped = self.__extract_temperature(lines)
            result = self.__calculate_temperature(stliped)
        return result

    def __calculate_temperature(self, pre_text):
        result = float(pre_text) / 1000
        return result

    def __extract_temperature(self, lines):
        line = lines[1]
        pattern = re.compile(r"t=\d+")
        matched_text = pattern.search(line)
        text = matched_text.group()
        stliped = text.replace('t=', '')
        return stliped
