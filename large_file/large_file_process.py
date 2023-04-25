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


@time_
def parallel(df_, n_workers_):
    """
    CPU time: 15.6875 s
    Wall time: 214.70771419999983 s
    :param df_:
    :param n_workers_:
    :return:
    """
    result = Parallel(n_jobs=n_workers_, backend="multiprocessing")(
        delayed(clean_text)
        (text) for text in tqdm(df_['Description'])
    )
    return result


def proc_batch(batch):
    return [
        clean_text(text) for text in batch
    ]


@time_
def parallel_batch(df_, n_workers_):
    """
    CPU time: 2.140625 s
    Wall time: 216.43949939999948 s
    :param df_:
    :param n_workers_:
    :return:
    """
    def batch_file(array):
        file_len = len(array)
        batch_size = round(file_len / n_workers_)
        batches_ = [
            array[ix: ix + batch_size]
            for ix in tqdm(range(0, file_len, batch_size))
        ]

        return batches_

    batches = batch_file(df_['Description'])

    batches_output = Parallel(n_jobs=n_workers_, backend="multiprocessing")(
        delayed(proc_batch)
        (batch) for batch in tqdm(batches)
    )

    df_['Description'] = [j for i in batches_output for j in i]


@time_
def tqdm_parallel(df_, n_workers_):
    """
    CPU time: 4.0625 s
    Wall time: 215.92957169999954 s
    :param df_:
    :param n_workers_:
    :return:
    """
    from tqdm.contrib.concurrent import process_map
    batch = round(len(df_) / n_workers_)

    df_['Description'] = process_map(clean_text, df_['Description'], max_workers=n_workers_, chunksize=batch)


if __name__ == "__main__":

    n_workers = 2 * mp.cpu_count()
    print(f"{n_workers} worker are available")

    # https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents
    file_name = "US_Accidents_Dec21_updated.csv"
    df = read_csv(file_name)
    print(f"Shape: {df.shape}\n\nColumns Names: \n{df.columns}\n")

    # serial(df)
    # multi_mp(df, n_workers)
    # parallel(df, n_workers)
    # parallel_batch(df, n_workers)
    tqdm_parallel(df, n_workers)