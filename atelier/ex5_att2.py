list=[47,64,69,37,76,83,95,97]
dic={'ahmed':64,'laila':37,'mohamed':83,"imad":97}
for valeur in list:
    if valeur is not dic.keys():
        list.remove(valeur)
print(list)
