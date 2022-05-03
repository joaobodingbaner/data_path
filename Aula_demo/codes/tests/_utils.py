import random
import time
from datetime import datetime
from decimal import Decimal
from typing import Any, Dict, Iterator

import pandas as pd


def get_df_bitcoin_trade():
    data = {'amount':[0.002, 0.0177606],
            'date':[1501871382, 1501871387],
            'price':[9723, 9735],
            'tid':[739718, 739719],
            'type':["sell", "buy"],}
 
    df = pd.DataFrame(data)
    return df

get_df_bitcoin_trade()

