S=input()
result=0

for n in S:
    m=int(n)
    if result<2 or m<2:
        result+=m
    else:
        result*=m

print(result)