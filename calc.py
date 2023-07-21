def calculate():
    numbx = input("First digit? \n")
    numby = input("Second digit? \n")
    answer = float(numbx) + float(numby)
    print(answer)
    calculate()

calculate()




