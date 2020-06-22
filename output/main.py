#!/usr/bin/env python3

from parser import parser
from fun import *

if __name__ == "__main__":
    pl1, pl2 = parser()
    data = comparation(pl1, pl2)
    print(data)