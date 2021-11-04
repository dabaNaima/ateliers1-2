list=[11,45,8,11,23,45,23,45,89]
dic={}
for valeur in list:
    if valeur not in dic.keys():
        dic[valeur]=1
    else:
        dic[valeur]=dic[valeur]+1
print(dic)
