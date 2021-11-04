def som(n):
 if n==1:
    return 1
 else:
    return  n+som(n-1)
n=int(input("donner un nombre"))
print(n)
print("la somme est equale",som(n))