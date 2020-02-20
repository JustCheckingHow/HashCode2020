import tqdm
import numpy
from utils import Library
from parser_books import parse_data
import numpy as np


class NaiveAlgo:
    def __init__(self, libs, book_vals):
        self.libraries = np.array(libs)
        self.book_vals = book_vals

    def get_books_priority(self, library):
        mapped = [self.book_vals[i] for i in library.books]
        return np.argsort(mapped)

    def solve(self):
        efficiency = [i.get_efficiency(self.book_vals) for i in self.libraries]
        efficiency = np.argsort(efficiency)[::-1]
        result_dict = {}
        for i, lib in zip(efficiency, self.libraries[efficiency]):
            result_dict[i] = self.get_books_priority(lib)[::-1]

        return result_dict, efficiency

if __name__=="__main__":
    libs, books_values, days = parse_data("data/a_example.txt")
    algo = NaiveAlgo(libs, books_values)
    print(algo.solve())