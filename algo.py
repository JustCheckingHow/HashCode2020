from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tqdm

from score_counter import ScoreCounter
from utils import Library
import itertools
from multiprocessing import Pool


def save_output(filename, libs):
    f = open(filename, "w")

    f.write(str(len(libs)) + "\n")
    for ID in libs:
        f.write(f"{ID} {len(libs[ID])}\n")
        out_str = " ".join([str(l) for l in list(libs[ID])])
        f.write(out_str + "\n")

    f.close()


class NaiveAlgo:
    def __init__(self,
                 _number_of_scans_power=2,
                 _signup_power=1,
                 _mapped_power=1):
        # params
        self._number_of_scans_power = _number_of_scans_power
        self._mapped_power = _mapped_power

        self._signup_power = _signup_power

        self.param_names = [
            '_number_of_scans_power',
            '_mapped_power',
            '_signup_power',
        ]

    def get_params(self, deep=False):
        """
        Get the parameters of the model 
        """
        param_dict = {}
        for param in self.param_names:
            param_dict[param] = getattr(self, param)
        return param_dict

    def set_params(self, **kwargs):
        """
        Set the internal params of the model 
        """
        self._number_of_scans_power = kwargs['_number_of_scans_power']
        self._signup_power = kwargs['_signup_power']

        self._mapped_power = kwargs['_mapped_power']

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
        remaining = self.all_days - self.day
        return np.any([lib.signup_time <= remaining for lib in self.libraries])

    def solve(self):
        self.param_dict = self.get_params()
        result_dict = {}
        efficiency_vals = [
            i.get_efficiency(self.book_vals, self.all_days, **self.param_dict)
            for i in self.libraries
        ]
        efficiency = np.argsort(efficiency_vals)[::-1]

        for i, lib in zip(efficiency, self.libraries[efficiency]):
            sorted_books = lib.books[self.get_books_priority(lib)[::-1]]
            res = self.get_parsable_books(sorted_books, lib.number_of_scans,
                                          lib.signup_time)
            if len(res) != 0:
                result_dict[i] = res
                self.counter.add(list(res))

                self.day += lib.signup_time
                self.consecutive_deadlines = 0
            else:
                self.consecutive_deadlines += 1
            if self.consecutive_deadlines >= self.threshold:
                if not self.any_parsable():
                    break

            if self.day > self.all_days:
                break

        self.counter.params = self.param_dict
        # self.counter.summary()
        return result_dict, efficiency

    def get_parsable_books(self, sorted_books, number_of_scans, signup):
        new_books = set(sorted_books) - self.processed

        num_books_parsable = max(0, (self.all_days - self.day - signup) *
                                 (number_of_scans))
        lst = list(new_books)[:num_books_parsable]
        new_books = set(lst)
        self.processed = self.processed.union(new_books)

        return new_books

    def score(self):
        return self.counter.score()

    def fit(self, inputs):
        # data
        input_dat, param_names, params = inputs[0], inputs[1], inputs[2]
        libs, books_values, days = input_dat[0], input_dat[1], input_dat[2]
        param_dict = {k: v for k, v in zip(param_names, params)}
        self.set_params(**param_dict)

        self.libraries = np.array(libs)
        self.book_vals = books_values
        self.processed = set()
        self.all_days = days
        self.consecutive_deadlines = 0
        self.threshold = 15
        self.day = 0
        self.freq = defaultdict(int)
        self.prepare()
        # initialise score counter
        self.counter = ScoreCounter(self.book_vals)
        libs, _ = self.solve()
        return libs, param_dict, self.counter.score

    def grid_search(self, inputs, param_grid, processors=4):
        param_names = sorted(param_grid)
        groups = itertools.product(*(param_grid[Name] for Name in param_names))

        with Pool(processors) as p:
            result = p.map(self.fit, [(inputs, param_names, param_comb)
                                      for param_comb in groups])

            max_res = 0
            max_params = None
            max_libs = None
            for res in result:
                libs, pm, score = res
                if score >= max_res:
                    max_res = score
                    max_params = pm
                    max_libs = libs
            print(max_params, max_res)
            # save_output(f"solutions/solution.txt", max_libs)
            return max_libs, max_params


