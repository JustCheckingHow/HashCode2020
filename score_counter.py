import numpy


class ScoreCounter:
    def __init__(self, book_vals):
        self.processed = set()
        self.book_vals = book_vals
        self.score = 0
        self.dupes = 0
        self.params = None

    def add(self, books):
        for book in books:
            if book not in self.processed:
                self.processed.add(book)
                self.score += self.book_vals[book]
            else:
                self.dupes += 1

    def summary(self):
        print("Score:", self.score)
        print("Book processed:", len(self.processed))
        print("Duplicates:", self.dupes)
        if self.params:
            print(f"Params {self.params}")
