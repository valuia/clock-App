from time import *
from os import *
from math import *
import subprocess

class Clock:
    def __init__(self, clock_time, h, m, s):
        self.value = clock_time
        self.hour = h
        self.min = m
        self.sec = s
        self.hours_in_degree = self.hour * 30
        self.min_in_degree = self.min * 0.5
        self.sec_in_degree = self.sec * 6
        self.total = self.hours_in_degree + self.min_in_degree + self.sec_in_degree

    def make_a_output_of_clock(self):
        print(self.value)
        self.math_clock_degree()

    def math_clock_degree(self):
        print(self.total, 'Degree')


def make_time():
    Time = strftime("%I hours : %M minutes : %S seconds %p")
    Hours = int(strftime("%I"))
    Mins = int(strftime("%M"))
    Sec = int(strftime("%S"))
    clock_run = Clock(clock_time=Time, h=Hours, m=Mins, s=Sec)
    clock_run.make_a_output_of_clock()


while make_time:
    subprocess.run('clear', shell=True)
    make_time()
    sleep(1)
