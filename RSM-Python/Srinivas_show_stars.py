rows=int(input('Enter the number of rows'))
def show_stars(rows):
    for i in range(0,rows+1):
        for j in range(i):
            print('*',end='')
        print()
show_stars(rows)