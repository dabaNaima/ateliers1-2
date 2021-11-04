def fact_pour_som(i):
  if (i==1):
      return 1
  else:
      return(i*fact_pour_som(i-1))
som=0
for i in range(5):
    som=som+fact_pour_som(i+1)/(i+1)
print("la somme de sériee  donnée est= ",som)
