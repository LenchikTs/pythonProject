import random

def solution(A):
    C=list(sorted(A))
    x=1
    for i in C:
        if i>0:
            if x == i:
                if C.count(i)==1:
                    x += 1
                else:
                    for k in range(C.count(i)-1):
                        C.pop(C.index(i,0,len(C)))
                    x += 1
            else:
                break
    return x

#A=[4,6,1,2,1,3,-8,1,2,2,6,10,9]
A=[]
for k in range(10):
    A.append(random.randint(-10,10))

solution(A)
#xxx