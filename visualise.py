import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from parser_books import parse_data


def visualise_basic(filename):
    libs, books_values, days =  parse_data(filename)
    print(libs, books_values, days)
    for lib in libs:
        print(lib.books)


    # 
visualise_basic('data/a_example.txt')