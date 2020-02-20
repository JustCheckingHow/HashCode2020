from algo import NaiveAlgo
from parser_books import parse_data

def save_output(filename, libs):
    f = open(filename, 'w')
    
    f.write(str(len(libs)) + '\n')
    assert len(list(set(libs))) == len(libs)
    print(len(libs))
    for ID in libs:     
        f.write(f"{ID} {len(libs[ID])}\n")
        out_str = ' '.join([str(l) for l in libs[ID].tolist()])
        f.write(out_str + '\n')

    f.close()

if __name__ == "__main__":
    libs, books_values, days = parse_data("data/e_so_many_books.txt")
    algo = NaiveAlgo(libs, books_values, days)
    libs, _ = algo.solve()
    save_output("e_output.txt", libs)
