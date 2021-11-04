from array import *
def tri_par_Bul(T):
  tmp=0
  for i in range(len(T)-1,1):
        for j in range(0,i-1):
            if T[j] > T[j+1]:
               tmp=T[j]
               T[j]= T[j+1]
               T[j+1]=tmp
  return T
def tri_par_selection(T):
   for i in range(len(T)):
      # Trouver le min
       x = i
       for j in range(i+1, len(T)):
           if T[x] > T[j]:
               x = j
                
       tmp = T[i]
       T[i] = T[x]
       T[x] = tmp
   return T
def tri_insertion(T): 
    # Parcour de 1 à la taille du tab
    for i in range(1, len(T)): 
        k = T[i] 
        j = i-1
        while j >= 0 and k < T[j] : 
                T[j + 1] = T[j] 
                j -= 1
        T[j + 1] = k
    return T
tab = [10, 5,0, 3, 80, 14]
print("le triage de tab par selection est ",tri_par_selection(tab))
print("le triage de tab par bull est ",tri_par_Bul(tab))
print("le triage de tab par insertion est ",tri_insertion(tab))