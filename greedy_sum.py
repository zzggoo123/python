S=int(input())
sum=0
i=1

while sum<S:
    sum+=i
    if sum>S:
        break
    i+=1

print(i-1)