import numpy as np

class Library:
    def __init__(self, books, signup_time, number_of_scans):
        self.signup_time = int(signup_time)
        self.number_of_scans = int(number_of_scans)
        self.books = [int(b) for b in books]

    @staticmethod
    def parse(line1, line2):
        signup_time = int(line1.split(" ")[1])
        books_per_day = int(line1.split(" ")[2])

        books = [int(x) for x in line2.split()]
        return Library(books, signup_time, books_per_day)

    def get_efficiency(self, val_map):
        mapped = [val_map[i] for i in self.books]

        return (np.sum(mapped)/self.signup_time)/self.number_of_scans
