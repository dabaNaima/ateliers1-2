def compte(n):
  if n < 10:
   return 1
  else:
   return(compte(n//10//10)+compte(n // 10)) 
  
a=int(input("donner un nombre "))
print(a)
print("le nombre  des chiffres de nombre donné egale ",compte(a))
