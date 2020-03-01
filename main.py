from algo import NaiveAlgo
from parser_books import parse_data
import sys
import glob
import os 

def save_output(filename, libs):
    f = open(filename, 'w')

    f.write(str(len(libs)) + '\n')
    for ID in libs:
        f.write(f"{ID} {len(libs[ID])}\n")
        out_str = ' '.join([str(l) for l in list(libs[ID])])
        f.write(out_str + '\n')

    f.close()


if __name__ == "__main__":
    fname = sys.argv[1]
    param_dict = {
        '_number_of_scans_power': 2,
        '_number_of_scan_weight': 1,
        '_signup_time_weight': 1,
        '_mapped_sum_weight': 1
    }

    save_folder = 'data'
    solution_folder = 'solutions'
    os.makedirs(solution_folder, exist_ok=True)
    if fname == "all":
        for fname in glob.glob(f"{save_folder}/*.txt"):
            libs, books_values, days = parse_data(fname)
            algo = NaiveAlgo(libs, books_values, days, param_dict=param_dict)
            libs, _ = algo.solve()
            f = fname.split('\\')[-1]
            save_output(f"3_solution_{f}", libs)
    else:
        fname = glob.glob(f"{save_folder}/{fname}*.txt")[0].replace('\\', '/')
        libs, books_values, days = parse_data(fname)
        algo = NaiveAlgo(libs, books_values, days, param_dict=param_dict)
        libs, _ = algo.solve()
        save_output(f"{solution_folder}/solution_{fname.split('/')[-1]}", libs)
