#!/usr/bin/env python3

import pandas as pd
import numpy as np
from fun import *
from argparse import ArgumentParser
from data_fifa import *


def parser():
    parser = ArgumentParser(description="Este programa es para comparar dos jugadores en su máxima puntuación en el FIFA ULTIMATE TEAM 2020")
    parser.add_argument("--player1", help="Elige primer futbolista. Añade la primera letra de cada palabra en mayúscula", nargs="+")
    parser.add_argument("--player2", help="Elige segundo futbolista. Añade la primera letra de cada palabra en mayúscula", nargs="+")                    


    args = parser.parse_args()
    player1 = ' '.join(args.player1)
    player2 = ' '.join(args.player2)

    return player1, player2

    



