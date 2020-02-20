import tqdm
import numpy
from utils import Library
from parser_books import parse_data
import numpy as np


class NaiveAlgo:
    def __init__(self, libs, book_vals):
        self.libraries = libs
        self.book_vals = book_vals

    def solve(self):
        efficiency = [i.get_efficiency(self.book_vals) for i in self.libraries]
        return np.argsort(efficiency)

if __name__=="__main__":
    libs, books_values, days = parse_data("data/a_example.txt")
    algo = NaiveAlgo(libs, books_values)
    print(algo.solve())