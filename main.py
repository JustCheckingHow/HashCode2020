import glob
import os
import sys

import numpy as np
from sklearn.model_selection import GridSearchCV

from algo import NaiveAlgo, save_output
from parser_books import parse_data

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
        '_number_of_scans_power': [i for i in np.arange(0.2, 2, 0.3)],
        '_mapped_power': [i for i in np.arange(0.2, 2, 0.3)],
        '_signup_power': [i for i in np.arange(0.2, 2, 0.3)],
    }

    array = [libs, books_values, days]

    max_libs, max_params = clf.grid_search(inputs=array,
                                           param_grid=parameters,
                                           processors=4)
    print(f"Done optimising! {max_params}")
    fname = 'all'
    clf.fit([[libs, books_values, days],
             list(max_params.keys()),
             list(max_params.values())])

    print("DOING FOR ALL")
    points = 0
    if fname == "all":
        for fname in glob.glob("data/*.txt"):
            libs, books_values, days = parse_data(fname)

            max_libs, _, score = clf.fit([[libs, books_values, days],
                                   list(max_params.keys()),
                                   list(max_params.values())])
            points += score

            f = fname.split("\\")[-1]
            save_output(f"3_solution_{f}", max_libs)
    # else:
    #     fname = glob.glob(f"data/{fname}*.txt")[0].replace("\\", "/")
    #     libs, books_values, days = parse_data(fname)
    #     algo = NaiveAlgo(libs, books_values, days)
    #     libs, _ = algo.solve()
    #     save_output(f"{solution_folder}/solution_{fname.split('/')[-1]}", libs)

    print(points)
