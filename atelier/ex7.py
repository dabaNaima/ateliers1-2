def envers (mot):
 

    "inverse une chaine de caractères" 

    resultat=""                 

    for lettre in mot:          

     resultat=lettre+resultat  

    return resultat             
str = 'Hello python'
print("inverse de str",envers(str))