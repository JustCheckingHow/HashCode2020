import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from parser_books import parse_data
from tqdm import tqdm

def visualise_basic(filename):
    libraries, book_values_dict, days =  parse_data(filename)
    total_books_value = sum(book_values_dict.values())
    total_books = len(book_values_dict)

    lib_scores = {}
    lib_days = {}
    lib_unique = {}
    lib_weighted = {}
    for lib_id, lib in tqdm(enumerate(libraries), total=len(libraries)):
        lib_score = sum([book_values_dict[b] for b in lib.books])
        lib_scores[lib_id] = lib_score
        lib_days[lib_id] = lib.signup_time

        # check unique bookss
        my_unique_set = set(lib.books)
        for j in range(0, len(libraries)):
            if lib_id == j:
                continue
            my_unique_set -= set(libraries[j].books)
        lib_unique[lib_id] = list(my_unique_set)
        my_unique_score = 0
        if my_unique_set:
            for b in my_unique_set:
                my_unique_score += book_values_dict[b]
        lib_weighted[lib_id] = my_unique_score


    libs = list(lib_scores.keys())


    # total score potential
    fig1, ax1 = plt.subplots()
    scores = list(lib_scores.values())
    ax1.bar(libs, scores, color='r')
    ax1.set_xticks(libs, libs)
    ax1.set_title("Library score potential")


    # number of unique books 
    fig2, ax2 = plt.subplots()
    unique_books = list(lib_unique.values())
    unique_books = [len(subset) for subset in unique_books]
    ax2.bar(libs, unique_books, color='g')
    ax2.set_xticks(libs, libs)
    ax2.set_title("Library unique books")


    # weighted score of unique books 
    fig3, ax3 = plt.subplots()
    unqiue_scores = list(lib_weighted.values())
    ax3.bar(libs, unqiue_scores, color='b')
    ax3.set_xticks(libs, libs)
    ax3.set_title("Library unique score")


    plt.show()
    
visualise_basic('data/c_incunabula.txt')