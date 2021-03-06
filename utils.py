import numpy as np

class Library:
    def __init__(self, books, signup_time, number_of_scans, id):
        self.id = id
        self.signup_time = int(signup_time)
        self.number_of_scans = int(number_of_scans)
        self.books = np.array(books).astype(int)
        self._mapped = None
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0

        self.A = 1
        self.B = 3
        self.C = 3

    @staticmethod
    def parse(line1, line2, id):
        signup_time = int(line1.split(" ")[1])
        books_per_day = int(line1.split(" ")[2])

        books = [int(x) for x in line2.split()]
        return Library(books, signup_time, books_per_day, id)

    def get_mapped(self, val_map):
        if self._mapped is None:
            self._mapped = [val_map[i] for i in self.books]
        return self._mapped

    def get_efficiency(self, val_map, day_no):
        mapped = self.get_mapped(val_map)

        return (np.sum(mapped) ** self.A/(self.signup_time ** self.B))*(self.number_of_scans**self.C)