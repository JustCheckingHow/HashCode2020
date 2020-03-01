import glob
import os
import sys

import numpy as np
from sklearn.model_selection import GridSearchCV

from algo import NaiveAlgo
from parser_books import parse_data


def save_output(filename, libs):
    f = open(filename, "w")

    f.write(str(len(libs)) + "\n")
    for ID in libs:
        f.write(f"{ID} {len(libs[ID])}\n")
        out_str = " ".join([str(l) for l in list(libs[ID])])
        f.write(out_str + "\n")

    f.close()


if __name__ == "__main__":
    save_folder = 'data'
    solution_folder = 'solutions'
    os.makedirs(solution_folder, exist_ok=True)
    fname = sys.argv[1]
    param_dict = {
        '_number_of_scans_power': 2,
        '_number_of_scan_weight': 1,
        '_signup_time_weight': 1,
        '_mapped_sum_weight': 1
    }

    fname = glob.glob(f"{save_folder}/{fname}*.txt")[0].replace('\\', '/')
    libs, books_values, days = parse_data(fname)
    clf = NaiveAlgo()

    parameters = {
        '_number_of_scans_power': (1, 5),
        '_mapped_power': (1, 5),
        '_signup_power': (1, 5),
        '_number_of_scans_power': (1, 5)
    }

    array = [libs, books_values, days]

    clf.grid_search(inputs=array, param_grid=parameters, processors=4)

    
    # points = 0
    # if fname == "all":
    #     for fname in glob.glob("data/*.txt"):
    #         libs, books_values, days = parse_data(fname)
    #         algo = NaiveAlgo(libs, books_values, days)
    #         libs, _ = algo.solve()
    #         points += algo.counter.score

    #         f = fname.split("\\")[-1]
    #         save_output(f"3_solution_{f}", libs)
    # else:
    #     fname = glob.glob(f"data/{fname}*.txt")[0].replace("\\", "/")
    #     libs, books_values, days = parse_data(fname)
    #     algo = NaiveAlgo(libs, books_values, days)
    #     libs, _ = algo.solve()
    #     save_output(f"solution_{fname.split('/')[-1]}", libs)

    # print(points)
