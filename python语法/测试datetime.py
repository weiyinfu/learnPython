from datetime import datetime

x = datetime.fromtimestamp(1000)
import time
import pandas as pd

y = x.timestamp()
print(x, y)
