# Parallel Computing
import multiprocessing as mp

from joblib import Parallel, delayed

from tqdm import tqdm

# Data Ingestion
import pandas as pd

# Text Processing
import re

from nltk.corpus import stopwords

import string
from tools.time_wraps import time_
import nltk
nltk.download('stopwords')


@time_
def read_csv(file_):
    df_ = pd.read_csv(file_)

    return df_


def clean_text(text):
    # Remove stop words
    stops = stopwords.words("english")
    text = " ".join([word for word in text.split() if word not in stops])
    # Remove special character
    text = text.translate(str.maketrans('', '', string.punctuation))
    # removing the extra spaces
    text = re.sub(' +', '', text)
    return text


@time_
def serial(df_):
    """
    CPU time: 698.078125 s
    Wall time: 699.3184386 s
    :param df_:
    :return:
    """
    tqdm.pandas()
    df_['Description'] = df_['Description'].progress_apply(clean_text)


@time_
def multi_mp(df_, n_workers_):
    """
    CPU time: 2.59375 s
    Wall time: 213.37318369999957 s
    :param df_:
    :param n_workers_:
    :return:
    """
    p = mp.Pool(n_workers_)

    df_['Description'] = p.map(clean_text, tqdm(df_['Description']))


if __name__ == "__main__":

    n_workers = 2 * mp.cpu_count()
    print(f"{n_workers} worker are available")

    # https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents
    file_name = "US_Accidents_Dec21_updated.csv"
    df = read_csv(file_name)
    print(f"Shape: {df.shape}\n\nColumns Names: \n{df.columns}\n")

    # serial(df)
    # multi_mp(df, n_workers)
