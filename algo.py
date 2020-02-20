import tqdm
import numpy
from utils import Library
from parser_books import parse_data
import numpy as np
import matplotlib.pyplot as plt

class NaiveAlgo:
    def __init__(self, libs, book_vals, day_no):
        self.libraries = np.array(libs)
        self.book_vals = book_vals
        self.found_books = None
        self.day_no = day_no

    def get_books_priority(self, library):
        mapped = [self.book_vals[i] for i in library.books]
        return np.argsort(mapped)

    def library_novelty(self, library):
        new_books = set(library.books)-self.found_books

    def solve(self):
        order = []

        efficiency_vals = [i.get_efficiency(self.book_vals, self.day_no) for i in self.libraries]
        efficiency = np.argsort(efficiency_vals)[::-1]
        order.append(efficiency[0])

        # Parse info of the most efficient library
        result_dict = {}
        lib = self.libraries[efficiency[0]]
        result_dict[0] = self.get_books_priority(lib)[::-1]
        self.found_books = set(lib.books)

        for i, lib in zip(tqdm.tqdm(efficiency), self.libraries[efficiency]):
            result_dict[i] = lib.books[self.get_books_priority(lib)[::-1]]

        plt.hist(efficiency_vals)
        plt.show()
        return result_dict, efficiency

if __name__=="__main__":
    libs, books_values, days = parse_data("data/e_so_many_books.txt")
    algo = NaiveAlgo(libs, books_values, days)
    algo.solve()