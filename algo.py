import tqdm
import numpy
from utils import Library
from parser_books import parse_data
import numpy as np


class NaiveAlgo:
    def __init__(self, libs, book_vals, days):
        self.libraries = np.array(libs)
        self.book_vals = book_vals
        self.processed = {}
        self.all_days = days
        self.day = 0

    def get_books_priority(self, library):
        mapped = [self.book_vals[i] for i in library.books]
        return np.argsort(mapped)

    def solve(self):
        efficiency = [i.get_efficiency(self.book_vals) for i in self.libraries]
        efficiency = np.argsort(efficiency)[::-1]
        result_dict = {}
        for i, lib in zip(efficiency, self.libraries[efficiency]):
            result_dict[i] = self.get_books_priority(lib)[::-1]
            self.day += lib.signup_time

        return result_dict, efficiency

    def get_parsable_books(self, lib):
        new_books = set(lib.books) - self.processed
        self.processed += lib.books

        num_books_parsable = (self.all_days - self.day) * lib.number_of_scans
        return list(new_books)[:num_books_parsable]


if __name__=="__main__":
    libs, books_values, days = parse_data("data/a_example.txt")
    algo = NaiveAlgo(libs, books_values)
    print(algo.solve())
