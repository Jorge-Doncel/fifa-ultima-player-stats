#!/usr/bin/env python3

import pandas as pd
import numpy as np
from data_fifa import *
import json
import requests



def download_flags(url, name):
    return urllib.request.urlretrieve(url, name)

def player(player_name):
    player = fifa.loc[fifa['player_extended_name'].str.contains(player_name)]
    player_max_overral = player[player['overall']==player['overall'].max()]
    return pd.DataFrame(player_max_overral)

def comparation(player_1, player_2):
    data_player_1 = player(player_1)
    data_player_2 = player(player_2)
    comparation_player = pd.concat([data_player_1,data_player_2])
    return comparation_player.sort_values(by="overall", ascending = False)