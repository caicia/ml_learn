import datetime
import random

import pandas as pd
import numpy as np
import swifter

if __name__ == '__main__':
    df = pd.DataFrame(np.random.randint(0, 10000, size=(100000000, 2)), columns=['nums_2', 'nums_1'])

    print(df.head(5))
    start = datetime.datetime.now()
    df.swifter.apply(lambda x: x['nums_2'] - x['nums_1'], axis=1).reset_index()
    end = datetime.datetime.now()
    print(end - start)  # 0:00:00.190617

    start = datetime.datetime.now()
    df.apply(lambda x: x['nums_2'] - x['nums_1'], axis=1).reset_index()
    end = datetime.datetime.now()
    print(end - start)  # 0:00:13.222674

