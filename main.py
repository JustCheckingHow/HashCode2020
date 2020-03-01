from algo import NaiveAlgo
from parser_books import parse_data
import sys
import glob


def save_output(filename, libs):
    f = open(filename, "w")

    f.write(str(len(libs)) + "\n")
    for ID in libs:
        f.write(f"{ID} {len(libs[ID])}\n")
        out_str = " ".join([str(l) for l in list(libs[ID])])
        f.write(out_str + "\n")

    f.close()


if __name__ == "__main__":
    fname = sys.argv[1]
    points = 0
    if fname == "all":
        for fname in glob.glob("data/*.txt"):
            libs, books_values, days = parse_data(fname)
            algo = NaiveAlgo(libs, books_values, days)
            libs, _ = algo.solve()
            points += algo.counter.score

            f = fname.split("\\")[-1]
            save_output(f"3_solution_{f}", libs)
    else:
        fname = glob.glob(f"data/{fname}*.txt")[0].replace("\\", "/")
        libs, books_values, days = parse_data(fname)
        algo = NaiveAlgo(libs, books_values, days)
        libs, _ = algo.solve()
        save_output(f"solution_{fname.split('/')[-1]}", libs)

    print(points)
