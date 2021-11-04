def fibona(n):
 if n<=1:
  return n
 else:
  return fibona(n-1)+fibona(n-2)
a=int(input("donner le a "))
print(a)
print("fiboner de",a,"est ",fibona(a))