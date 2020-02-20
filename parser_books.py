import pandas as pd
from utils import Library
import tqdm


def parse_data(filename):
    with open(filename) as f:
        temp = f.readline().split(" ")
        book_no = temp[0]
        library_no = int(temp[1])
        days = int(temp[2])

        books_values = f.readline().split(" ")
        books_values = [int(b) for b in books_values]
        libs = []
        for i in tqdm.trange(library_no):
            line1 = f.readline()
            line2 = f.readline()
            libs.append(Library.parse(line1, line2))
    return libs, books_values, days 