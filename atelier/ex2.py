def conversion(x):
    if x> 1:
        conversion(x // 2)
    print(x % 2, end='')
n_décimal = int(input(" un nombre decimal: "))
conversion(n_décimal)