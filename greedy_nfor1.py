import time
start_time=time.time() #측정 시작

N,K=map(int,input().split())

count=0

while N!=1 :
    if(N%K==0):
        N/=K
        count+=1
    else:
        N-=1
        count+=1

print(count)

end_time=time.time() #측정 종료
print("수행시간:", end_time-start_time)