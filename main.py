from algo import NaiveAlgo
from parser_books import parse_data
import sys
import glob
from multiprocessing import Pool


def save_output(filename, libs):
    f = open(filename, 'w+')

    f.write(str(len(libs)) + "\n")
    for ID in libs:
        f.write(f"{ID} {len(libs[ID])}\n")
        out_str = " ".join([str(l) for l in list(libs[ID])])
        f.write(out_str + "\n")

    f.close()


fname = None
maxi = 0

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def calc(A):
    # global maxi
    maxi = 0
    best = []
    print("calc:", fname)
    for B in arr:
        for C in arr:
            points = 0
            libs, books_values, days = parse_data(fname)
            for i, lib in enumerate(libs):
                libs[i].A = A
                libs[i].B = B
                libs[i].C = C
            algo = NaiveAlgo(libs, books_values, days)
            libs, _ = algo.solve()
            points = algo.counter.score
            maxi = max(maxi, points)
            if points == maxi:
                best = [A, B, C]
            #save_output(f"solution_{fname.split('/')[-1]}", libs)
            print(A, B, C, points, maxi)
    return (best, maxi)

def search(fname_temp):
    maxi = 0
    global fname
    fname = glob.glob(f"data/{fname_temp}*.txt")[0].replace('\\', '/')
    print(fname)
    with Pool(6) as p:
        out = p.map(calc, arr)
    print(out)

if __name__ == "__main__":
    fname = sys.argv[1]
    #print("fname: ", fname)
    if len(sys.argv) == 3 and sys.argv[2] == '-s':
        #print(fname)
        search(fname)
        exit(0)
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
