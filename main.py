def save_output(filename, libs):
    f = open(filename, 'a')
    
    f.write(str(len(libs)) + '\n')
    
    for ID in libs:     
        f.write(str(ID) + ' ' + str(len(libs[ID])) + '\n')

        for book_id in libs[str(ID)]:
            f.write(str(book_id) + ' ')
        f.write('\n')

    f.close()
