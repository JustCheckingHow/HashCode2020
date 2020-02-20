from algo import NaiveAlgo
from parser_books import parse_data

def save_output(filename, libs):
    f = open(filename, 'w')
    
    f.write(str(len(libs)) + '\n')
    
    for ID in libs:     
        f.write(f"{ID} {len(libs[ID])}\n")

        for book_id in libs[ID]:
            f.write(str(book_id) + ' ')
        f.write('\n')

    f.close()

if __name__ == "__main__":
    libs, books_values, days = parse_data("data/a_example.txt")
    algo = NaiveAlgo(libs, books_values)
    libs, _ = algo.solve()
    save_output("a_output.txt", libs)