#!/usr/bin/env python3

import pandas as pd
import numpy as np


fifa = pd.read_csv("fifa_clean.csv", index_col=0)
fifa= pd.DataFrame(fifa)