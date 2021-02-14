import random

def solution(A):
    x=0
    B=[]
    C=[]
    D=[]
    D1=[]
    for i in range(len(A)):
        if i%2==0:
            B.append(0)
            C.append(1)
        else:
            B.append(1)
            C.append(0)
    for i in range(len(A)):
        if A[i]!=B[i]:
            D.append(A.index(A[i],i,len(A)))
        if A[i]!=C[i]:
            D1.append(A.index(A[i], i, len(A)))
    if len(D)<=len(D1):
        x=len(D)
        for i in range(len(D)):
            A[D[i]]=B[D[i]]
    elif len(D)>len(D1):
        x = len(D1)
        for i in range(len(D1)):
            A[D1[i]] = C[D1[i]]
    return x

N=random.randint(1,10)
A=[]
for i in range(N):
    A.append(random.randint(0,1))

solution(A)
