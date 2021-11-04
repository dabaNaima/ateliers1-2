list=[11,45,8,23,14,12,78,45,89]
l1=[]
l2=[]
l3=[]
n=len(list)
x=int(n/3)
for i in range(x):
    l1.insert(-x,list[i])
for i in range(x,2*x):
    l2.insert(-2*x,list[i])
for i in range(2*x,n):
    l3.insert(-n,list[i])
print(l1)
print(l2)
print(l3)