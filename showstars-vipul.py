def show_stars(rows):
    for row in range(rows+1):
        for x in range(row):
            print("*",end=" ")
        print("\n")
show_stars(5)
