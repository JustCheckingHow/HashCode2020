import tqdm
from utils import Library
from parser_books import parse_data
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from score_counter import ScoreCounter


class NaiveAlgo:
    def __init__(self, libs, book_vals, days):
        self.libraries = np.array(libs)
        self.book_vals = book_vals
        self.processed = set()
        self.all_days = days
        self.day = 0
        self.freq = defaultdict(int)
        self.prepare()
        self.counter = ScoreCounter(book_vals)
        self.consecutive_deadlines = 0
        self.threshold = 15

    def get_books_priority(self, library):
        mapped = [self.book_vals[i] / self.freq[i] for i in library.books]
        return np.argsort(mapped)

    def library_novelty(self, library):
        new_books = set(library.books) - self.found_books

    def prepare(self):
        for lib in self.libraries:
            for book in lib.books:
                self.freq[book] += 1

    def any_parsable(self):
        remaining = self.all_days-self.day
        return np.any([lib.signup_time<=remaining for lib in self.libraries])

    def solve(self):
        result_dict = {}
        efficiency_vals = [
            i.get_efficiency(self.book_vals, self.all_days) for i in self.libraries
        ]
        efficiency = np.argsort(efficiency_vals)[::-1]
        for i, lib in zip(efficiency, self.libraries[efficiency]):
            sorted_books = lib.books[self.get_books_priority(lib)[::-1]]
            res = self.get_parsable_books(
                sorted_books, lib.number_of_scans, lib.signup_time
            )
            if len(res) != 0:
                result_dict[i] = res
                self.counter.add(list(res))

                self.day += lib.signup_time
                self.consecutive_deadlines = 0
            else:
                self.consecutive_deadlines += 1
            if self.consecutive_deadlines>=self.threshold:
                if not self.any_parsable():
                    break

        self.counter.summary()
        return result_dict, efficiency

    def get_parsable_books(self, sorted_books, number_of_scan, signup):
        new_books = set(sorted_books) - self.processed

        num_books_parsable = max(
            0, (self.all_days - self.day - signup) * (number_of_scan)
        )
        lst = list(new_books)[:num_books_parsable]
        new_books = set(lst)
        self.processed = self.processed.union(new_books)

        return new_books


if __name__ == "__main__":
    libs, books_values, days = parse_data("data/e_so_many_books.txt")
    algo = NaiveAlgo(libs, books_values, days)
    algo.solve()
