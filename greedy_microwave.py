T=int(input())

A=5*60
B=60
C=10
A_count=0
B_count=0
C_count=0

if T%10==0:
    while T>=A:
        T=T-A
        A_count+=1
    while T>=B:
        T=T-B
        B_count+=1
    while T>=C:
        T=T-C
        C_count+=1
    print(A_count,B_count,C_count)
else:
    print(-1)