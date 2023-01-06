import json
import re
import time

import uuid

import pandas as pd


def highlight_col(x):
    # copy df to new - original data are not changed
    df = x.copy()
    # set by condition
    mask = df['mask'] == 'new'
    mask2 = df['mask'] == 'old'
    df.loc[mask, :] = 'background-color: yellow'
    df.loc[~mask, :] = 'background-color: ""'
    df.loc[mask2, :] = 'background-color: blue'

    return df


if __name__ == '__main__':
    df1 = pd.read_excel('./闪支付消费券-20221021.xlsx')
    df2 = pd.read_excel('./闪支付消费券.xlsx')

    df3 = df1.copy()
    df3.loc[~df1.apply(tuple, 1).isin(df2.apply(tuple, 1)), 'mask'] = 'new'

    df4 = df2.copy()
    df4.loc[~df2.apply(tuple, 1).isin(df1.apply(tuple, 1)), 'mask'] = 'old'

    df = pd.concat([df3, df4], ignore_index=True)

    df.style.apply(highlight_col, axis=None).to_excel('./闪支付商家差异对比.xlsx')
