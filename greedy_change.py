money=int(input())
yen=[500, 100, 50, 10, 5, 1]
result=0

change_money=1000-money

for loof in yen:
    result+=change_money//loof
    change_money%=loof

print(result)