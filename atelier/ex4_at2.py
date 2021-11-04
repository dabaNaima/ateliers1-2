set1={23,42,65,57,78,83,29}
set2={57,83,29,67,73,43,48}
ins=set1&set2

for valeur in ins:
    set1.discard(valeur)
print(ins)
print(set1)
