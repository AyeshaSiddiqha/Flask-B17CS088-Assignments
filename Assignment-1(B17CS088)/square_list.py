l=[]
n=int(input("enter number of elements "))
for x in range(n):
    l.append(int(input()))
print(list(map(lambda x:x**2,l)))