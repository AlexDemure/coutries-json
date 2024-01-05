import csv
import multiprocessing
import os
import pathlib
from functools import partial


def chunks(iterate, size):
    for i in range(0, len(iterate), size):
        yield iterate[i:i + size]


def multiprocess(f, *args, iterable):
    with multiprocessing.Pool(len(iterable)) as pool:
        results = pool.map(partial(f, *args), iterable)
    return results


def tuple_to_dict(keys: list[str], row: tuple) -> dict:
    dct = dict()

    for index, key in enumerate(keys):
        try:
            dct[key] = row[index]
        except IndexError:
            dct[key] = None

    return dct


def check_file(filepath: str) -> bool:
    return pathlib.Path(filepath).is_file()


def check_dir(dirpath: str) -> None:
    if not pathlib.Path(dirpath).is_dir():
        os.makedirs(dirpath, exist_ok=True)


def string_to_csv(string: str) -> list[tuple]:
    return list(csv.reader(string.split("\n"), delimiter='\t'))


def txtf(filename: str) -> str:
    return f"{filename}.txt"


def zipf(filename) -> str:
    return f"{filename}.zip"
