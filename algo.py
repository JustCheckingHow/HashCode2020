from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tqdm

from parser_books import parse_data
from utils import Library


class NaiveAlgo:
    def __init__(self, libs, book_vals, days, param_dict=None):
        self.libraries = np.array(libs)
        self.book_vals = book_vals
        self.processed = set()
        self.all_days = days
        self.day = 0
        self.freq = defaultdict(int)
        self.prepare()

        # params
        if param_dict is None:
            self.param_dict = {
                '_number_of_scans_power': 2,
                '_number_of_scan_weight': 1,
                '_signup_time_weight': 1,
                '_mapped_sum_weight': 1
            }
        else:
            self.param_dict = param_dict

    def get_params(self, deep=False):
        """
        Get the parameters of the model 
        """
        param_dict = {}
        for param in self.param_names:
            param_dict[param] = getattr(self, param)
        return param_dict

    def set_params(self, **param):
        """
        Set the internal params of the model 
        """
        for p in param:
            setattr(self, p, param[p])

    def get_books_priority(self, library):
        mapped = [self.book_vals[i] / self.freq[i] for i in library.books]
        return np.argsort(mapped)

    def library_novelty(self, library):
        new_books = set(library.books) - self.found_books

    def prepare(self):
        for lib in self.libraries:
            for book in lib.books:
                self.freq[book] += 1

    def solve(self):
        result_dict = {}
        efficiency_vals = [
            i.get_efficiency(self.book_vals, self.all_days)
            for i in self.libraries
        ]
        efficiency = np.argsort(efficiency_vals)[::-1]

        for i, lib in zip(tqdm.tqdm(efficiency), self.libraries[efficiency]):
            sorted_books = lib.books[self.get_books_priority(lib)[::-1]]
            res = self.get_parsable_books(sorted_books, lib.number_of_scans,
                                          lib.signup_time)
            if len(res) != 0:
                result_dict[i] = res
                self.day += lib.signup_time

            if self.day > self.all_days:
                break

        return result_dict, efficiency

    def get_parsable_books(self, sorted_books, number_of_scans, signup):
        new_books = set(sorted_books) - self.processed

        num_books_parsable = (self.all_days - self.day -
                              signup) * (number_of_scans)
        lst = list(new_books)[:num_books_parsable]
        for i in lst:
            self.book_vals[i] = 0
        new_books = set(lst)
        self.processed = self.processed.union(new_books)

        return new_books

    def parse_data(self, filename):
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
                libs.append(Library.parse(line1, line2, i, self.param_dict))
        return libs, book_values_dict, days


if __name__ == "__main__":
    libs, books_values, days = parse_data("data/e_so_many_books.txt")
    algo = NaiveAlgo(libs, books_values, days)
    algo.solve()
