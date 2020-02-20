import pandas as pd
from utils import Library

DATA = "data/a_example.txt"


if __name__ == "__main__":
    with open(DATA) as f:
        temp = f.readline().split(" ")
        book_no = temp[0]
        library_no = int(temp[1])
        days = temp[2]

        books_values = f.readline().split(" ")
        libs = []
        for i in range(library_no):
            line1 = f.readline()
            line2 = f.readline()
            libs.append(Library.parse(line1, line2))
