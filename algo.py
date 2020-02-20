import tqdm
import numpy
from utils import Library
from parser_books import parse_data

if __name__=="__main__":
    libs, books_values, days = parse_data("data/a_example.txt")
    print(libs, books_values, days)
    print(libs[1].books)