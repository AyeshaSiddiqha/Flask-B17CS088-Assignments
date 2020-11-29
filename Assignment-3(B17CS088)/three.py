l1=[]
l=[]
print("Enter values for map:")
for _ in range(5):
    l1.append(int(input()))
def mymap(x,y):
    for a in y:
	    l.append(x(a))
    return l

print(list(mymap(lambda x:x*x*x,l1)))


l2=[]
l=[]
print("Enter values for filter:")
for _ in range(5):
    l2.append(int(input()))

def myfilter(t,u):
    for a in u:
        if t(a):
	        l.append(a)
    return l
print("odd numbers:")
print(list(myfilter(lambda x:x%2,l2)))