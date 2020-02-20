import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from parser_books import parse_data


def visualise_basic(filename):
    libs, books_values, days, book_values_dict =  parse_data(filename)
    print(libs, books_values, days)
    print(book_values_dict)

    total_books_value = sum(book_values_dict.values())
    total_books = len(book_values_dict)

    lib_scores = {}
    for lib_id, lib in enumerate(libs):
        lib_score = sum([book_values_dict[b] for b in book_values_dict])
        # lib_scores[lib_id] 
    # 
visualise_basic('data/a_example.txt')