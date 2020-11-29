from collections import deque  
x=deque([5,4,3,2,1])
for i in range(5):
    x.rotate(1)
    for j in x:
        print(j,end=" ")
    print("")