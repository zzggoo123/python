# import pandas as pd

N=input()
pp=[]
maxvalue=0

c69=N.count("6")+N.count("9")
cc=round(c69/2)
N=N.replace('6','9')
N=N.replace('9',' ' ,c69-cc)

for i in set(N):
    if N.count(i) > maxvalue:
        maxvalue = N.count(i)
print(maxvalue)

# print(pd.Series(list(N)).value_counts().get(0))