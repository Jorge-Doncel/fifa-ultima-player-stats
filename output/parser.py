#!/usr/bin/env python3

import pandas as pd
import numpy as np
from fun import *
from argparse import ArgumentParser
from data_fifa import *


def parser():
    parser = ArgumentParser(description="This data pipeline allow you to compare two players in their highest score in FIFA ULTIMATE TEAM 2020")
    parser.add_argument("--player1", help="Choose first football player. Add the first letter of each word in capital letters", nargs="+")
    parser.add_argument("--player2", help="Choose second football player. Add the first letter of each word in capital letters", nargs="+")                    


    args = parser.parse_args()
    player1 = ' '.join(args.player1)
    player2 = ' '.join(args.player2)

    return player1, player2

    



