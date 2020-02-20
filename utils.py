class Library:
    def __init__(self, books, signup_time, number_of_scans):
        self.signup_time = signup_time
        self.number_of_scans = number_of_scans
        self.books = books

    @staticmethod
    def parse(line1, line2):
        signup_time = int(line1.split(" ")[1])
        books_per_day = int(line1.split(" ")[2])

        books = line2.split()
        return Library(books, signup_time, books_per_day)


