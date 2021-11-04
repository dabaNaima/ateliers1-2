def frequency(str,char):
    cmpt=0
    for x in str :
        if x==char:
            cmpt+=1
    return cmpt
    #test 
string=input(" enter une chaine :")
char=input("enter un caractere :")
print("la frequence est :",frequency(string,char))
