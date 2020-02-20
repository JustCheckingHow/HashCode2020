import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from parser_books import parse_data
from tqdm import tqdm
from collections import Counter 

def visualise_basic(filename):
    libraries, book_values_dict, days =  parse_data(filename)
    total_books_value = sum(book_values_dict.values())
    total_books = len(book_values_dict)

    lib_scores = {}
<<<<<<< HEAD
    for lib_id, lib in enumerate(libs):
        lib_score = sum([book_values_dict[b] for b in book_values_dict])
        # lib_scores[lib_id] 
    # 
visualise_basic('data/a_example.txt')
=======
    lib_days = {}
    lib_unique = {}
    lib_weighted = {}
    lib_scans = {}
    for lib_id, lib in tqdm(enumerate(libraries), total=len(libraries)):
        lib_score = sum([book_values_dict[b] for b in lib.books])
        lib_scores[lib_id] = lib_score
        lib_days[lib_id] = lib.signup_time
        lib_scans[lib_id] = lib.number_of_scans
        # check unique books
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
    lib_scores = Counter(lib_scores)
    scores = [l[1] for l in lib_scores.most_common()]
    ax1.bar(libs, scores, color='r')
    ax1.set_xticks(libs, libs)
    ax1.set_title("Library score potential")


    # number of unique books 
    fig2, ax2 = plt.subplots()
    unique_books = list(lib_unique.values())
    unique_books = [len(subset) for subset in unique_books]
    unique_books = sorted(unique_books, reverse=True)
    ax2.bar(libs, unique_books, color='g')
    ax2.set_xticks(libs, libs)
    ax2.set_title("Library unique books")


    # weighted score of unique books 
    fig3, ax3 = plt.subplots()
    unqiue_scores = list(lib_weighted.values())
    unqiue_scores = sorted(unqiue_scores)
    ax3.bar(libs, unqiue_scores, color='b')
    ax3.set_xticks(libs, libs)
    ax3.set_title("Library unique score")

    fig4, ax4 = plt.subplots()
    days_lib = list(lib_days.values())
    days_lib = sorted(days_lib, reverse=True)
    ax4.bar(libs, days_lib, color='orange')
    ax4.set_xticks(libs, libs)
    ax4.set_title("Library signup days")

    fig5, ax5 = plt.subplots()
    multi = list(lib_scans.values())
    multi = sorted(multi, reverse=True)
    ax5.bar(libs, multi, color='black')
    ax5.set_xticks(libs, libs)
    ax5.set_title("Library multi books")

    plt.show()
    
# visualise_basic('data/b_read_on.txt')
visualise_basic('data/c_incunabula.txt')
>>>>>>> f4d2c04f4e4a3de55c5e7d708f7d816b559e98df
