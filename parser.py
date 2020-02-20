import pandas as pd
from utils import Library



def parse_data(filename):
    with open(filename) as f:
        temp = f.readline().split(" ")
        book_no = temp[0]
        library_no = temp[1]
        days = temp[2]

        books_values = f.readline().split(" ")
        libs = []
        for i in range(library_no):
            line1 = f.readline()
            line2 = f.readline()
            libs.append(Library.parse(line1, line2))
    return libs, books_values, days 