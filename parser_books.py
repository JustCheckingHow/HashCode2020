import pandas as pd
from utils import Library


def parse_data(filename):
    with open(filename) as f:
        temp = f.readline().split(" ")
        book_no = temp[0]
        library_no = int(temp[1])
        days = int(temp[2])

        books_values = f.readline().split(" ")
        books_values = [int(b) for b in books_values]
        book_values_dict = {i: b for i, b in enumerate(books_values)}
        libs = []
        for i in range(library_no):
            line1 = f.readline()
            line2 = f.readline()
            libs.append(Library.parse(line1, line2, i))
    return libs, book_values_dict, days
